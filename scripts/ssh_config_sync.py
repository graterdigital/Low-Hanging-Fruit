#!/usr/bin/env python3
"""Build SSH config entries for every Kinsta and WP Engine environment and link them to client files.

Run from the repo root on the machine that will run fixes (Windows PowerShell, macOS, or Linux):

    python scripts/ssh_config_sync.py            # preview: prints what it would write, changes nothing
    python scripts/ssh_config_sync.py --apply    # writes ~/.ssh/config.d entries and updates clients/*.yaml

Credentials come from environment variables only; nothing is stored in the repo:
    KINSTA_API_KEY        MyKinsta > Company settings > API Keys
    KINSTA_COMPANY_ID     MyKinsta > Company settings > Billing details (the company UUID)
    WPENGINE_API_USER     my.wpengine.com/api_access
    WPENGINE_API_PASSWORD same page

Either host can be skipped by leaving its variables unset.

What it writes:
  ~/.ssh/grater_hosts        one "Host <alias>" block per environment. Aliases: <slug> for live/production,
                             <slug>-staging / <slug>-dev for the others. The slug is the primary domain
                             without its ending, which matches clients/<slug>.yaml.
  ~/.ssh/config              gets a single line "Include grater_hosts" added at the top if it isn't there.
  clients/<slug>.yaml        hosting.provider, hosting.ssh_alias, hosting.staging_environment, hosting.access
                             filled in when a match is found. Other fields are left alone.

Requires: pip install requests pyyaml
"""
import argparse, os, re, sys, glob, json
from pathlib import Path

try:
    import requests, yaml
except ImportError:
    sys.exit("pip install requests pyyaml")

KEY_FILE = "~/.ssh/id_ed25519"

def slug_of(domain: str) -> str:
    d = domain.lower().strip().rstrip("/")
    d = re.sub(r"^https?://", "", d)
    d = re.sub(r"^www\.", "", d)
    return d.split(".")[0]

def kinsta_envs():
    key, company = os.environ.get("KINSTA_API_KEY"), os.environ.get("KINSTA_COMPANY_ID")
    if not (key and company):
        print("Kinsta: KINSTA_API_KEY / KINSTA_COMPANY_ID not set, skipping")
        return []
    h = {"Authorization": f"Bearer {key}"}
    r = requests.get("https://api.kinsta.com/v2/sites", params={"company": company, "include_environments": "true"}, headers=h, timeout=60)
    r.raise_for_status()
    out = []
    for site in r.json()["company"]["sites"]:
        for env in site.get("environments", []):
            cfg = requests.get(f"https://api.kinsta.com/v2/sites/{site['id']}/environments/{env['id']}/ssh/config", headers=h, timeout=60)
            if cfg.status_code != 200:
                print(f"Kinsta: no SSH config for {site['name']}/{env['name']} ({cfg.status_code}); is SSH enabled for it?")
                continue
            c = cfg.json()
            out.append({
                "provider": "kinsta",
                "site": site["name"],
                "env": env["name"],                      # live, staging, ...
                "domain": (env.get("primaryDomain") or {}).get("name") or "",
                "host": c["host"], "port": str(c["port"]), "user": c["user"],
                "wp_version": env.get("wordpress_version"),
            })
    print(f"Kinsta: {len(out)} environments")
    return out

def wpengine_envs():
    u, p = os.environ.get("WPENGINE_API_USER"), os.environ.get("WPENGINE_API_PASSWORD")
    if not (u and p):
        print("WP Engine: WPENGINE_API_USER / WPENGINE_API_PASSWORD not set, skipping")
        return []
    out, offset = [], 0
    while True:
        r = requests.get("https://api.wpengineapi.com/v1/installs", params={"limit": 100, "offset": offset}, auth=(u, p), timeout=60)
        r.raise_for_status()
        j = r.json()
        for inst in j.get("results", []):
            out.append({
                "provider": "wpengine",
                "site": (inst.get("site") or {}).get("name") or inst["name"],
                "env": inst.get("environment") or "production",   # production, staging, development
                "domain": inst.get("primary_domain") or inst.get("cname") or "",
                "host": f"{inst['name']}.ssh.wpengine.net", "port": "22", "user": inst["name"],
                "wp_version": None,
            })
        if not j.get("next"):
            break
        offset += 100
    print(f"WP Engine: {len(out)} installs")
    return out

def alias_for(e, clients):
    """Pick the alias: client slug if the primary domain matches a client file, else the host's site name."""
    s = slug_of(e["domain"]) if e["domain"] else None
    base = s if s in clients else slug_of(e["site"])
    env = e["env"].lower()
    if env in ("live", "production"):
        return base
    return f"{base}-{'staging' if 'stag' in env else env}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write files; default is preview only")
    args = ap.parse_args()

    clients = {Path(f).stem: f for f in glob.glob("clients/*.yaml") if not f.endswith("_template.yaml")}
    envs = kinsta_envs() + wpengine_envs()
    if not envs:
        sys.exit("Nothing to do.")

    blocks, matched, unmatched = [], {}, []
    for e in envs:
        alias = alias_for(e, clients)
        blocks.append(f"Host {alias}\n    HostName {e['host']}\n    Port {e['port']}\n    User {e['user']}\n    IdentityFile {KEY_FILE}\n")
        s = slug_of(e["domain"]) if e["domain"] else None
        if s in clients:
            matched.setdefault(s, {"provider": e["provider"], "live": None, "staging": None, "wp_version": None})
            if e["env"].lower() in ("live", "production"):
                matched[s]["live"] = alias; matched[s]["wp_version"] = e["wp_version"]
            elif "stag" in e["env"].lower():
                matched[s]["staging"] = alias
        else:
            unmatched.append(f"{e['provider']}: {e['site']} ({e['env']}) {e['domain'] or 'no domain'} -> alias {alias}")

    print("\n--- SSH blocks ---\n" + "\n".join(blocks))
    print("--- Client files to update ---")
    for s, m in matched.items():
        print(f"  {s}: provider={m['provider']} ssh_alias={m['live']} staging={m['staging']}")
    if unmatched:
        print("--- Environments with no client file (alias written anyway) ---")
        for u in unmatched: print("  " + u)
    missing = sorted(set(clients) - set(matched))
    print(f"--- Client files with no host match ({len(missing)}): {', '.join(missing)}")

    if not args.apply:
        print("\nPreview only. Re-run with --apply to write.")
        return

    ssh_dir = Path.home() / ".ssh"; ssh_dir.mkdir(exist_ok=True)
    (ssh_dir / "grater_hosts").write_text("# Generated by scripts/ssh_config_sync.py. Re-run it instead of editing.\n\n" + "\n".join(blocks), encoding="utf-8")
    cfg = ssh_dir / "config"
    existing = cfg.read_text(encoding="utf-8") if cfg.exists() else ""
    if "Include grater_hosts" not in existing:
        cfg.write_text("Include grater_hosts\n\n" + existing, encoding="utf-8")
    print(f"\nWrote {ssh_dir / 'grater_hosts'} and ensured Include line in {cfg}")

    for s, m in matched.items():
        path = clients[s]; text = Path(path).read_text(encoding="utf-8")
        def setf(txt, key, val):
            pat = re.compile(rf"^(\s+{key}:)\s*.*$", re.M)
            return pat.sub(lambda mm: f"{mm.group(1)} {val}", txt, count=1) if pat.search(txt) else txt
        text = setf(text, "provider", m["provider"])
        text = setf(text, "access", "ssh+wp-cli")
        if m["live"]: text = setf(text, "ssh_alias", m["live"])
        text = setf(text, "staging_environment", m["staging"] or "none")
        if m["wp_version"]: text = setf(text, "wp_version", m["wp_version"])
        Path(path).write_text(text, encoding="utf-8")
    print(f"Updated {len(matched)} client files. Review with git diff, then commit.")

if __name__ == "__main__":
    main()
