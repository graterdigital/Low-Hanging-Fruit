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
            conn = env.get("ssh_connection") or {}
            ip = (conn.get("ssh_ip") or {}).get("external_ip"); port = conn.get("ssh_port")
            if not (ip and port):
                print(f"Kinsta: no SSH details for {site['name']}/{env['name']}; is SSH enabled for it?")
                continue
            out.append({
                "provider": "kinsta", "site_key": f"kinsta:{site['id']}",
                "site": site["name"], "env": env["name"],              # live, staging, ...
                "domain": (env.get("primaryDomain") or {}).get("name") or "",
                "host": ip, "port": str(port), "user": site["name"],  # Kinsta's SSH user is the site name
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
            site = inst.get("site") or {}
            out.append({
                "provider": "wpengine", "site_key": f"wpengine:{site.get('id') or inst['name']}",
                "site": site.get("name") or inst["name"],
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

def is_live(env): return env.lower() in ("live", "production")
def env_suffix(env):
    e = env.lower()
    return "staging" if "stag" in e else ("dev" if "dev" in e else e)

def group_sites(envs, clients):
    """Group environments by hosting site and pick one base alias per site from its live environment."""
    sites = {}
    for e in envs:
        sites.setdefault(e["site_key"], []).append(e)
    result = []
    for key, group in sites.items():
        live = [e for e in group if is_live(e["env"])]
        probe = live[0] if live else group[0]
        s = slug_of(probe["domain"]) if probe["domain"] else None
        matched_slug = s if s in clients else None
        base = matched_slug or (s if s and not probe["domain"].endswith((".kinsta.cloud", ".wpengine.com", ".wpenginepowered.com")) else slug_of(probe["site"]))
        result.append({"base": base, "client": matched_slug, "envs": group, "live": live})
    return result

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write files; default is preview only")
    args = ap.parse_args()

    clients = {Path(f).stem: f for f in glob.glob("clients/*.yaml") if not f.endswith("_template.yaml")}
    envs = kinsta_envs() + wpengine_envs()
    if not envs:
        sys.exit("Nothing to do.")

    blocks, matched, unmatched, used = [], {}, [], set()
    for site in group_sites(envs, clients):
        aliases = {}
        for e in site["envs"]:
            alias = site["base"] if is_live(e["env"]) else f"{site['base']}-{env_suffix(e['env'])}"
            n, cand = 2, alias
            while cand in used:
                cand = f"{alias}-{n}"; n += 1
            used.add(cand); aliases[cand] = e
            blocks.append(f"Host {cand}\n    HostName {e['host']}\n    Port {e['port']}\n    User {e['user']}\n    IdentityFile {KEY_FILE}\n")
        if site["client"]:
            live_alias = next((a for a, e in aliases.items() if is_live(e["env"])), None)
            stg = [a for a, e in aliases.items() if env_suffix(e["env"]) == "staging"]
            wpv = next((e["wp_version"] for e in site["envs"] if is_live(e["env"]) and e.get("wp_version")), None)
            matched[site["client"]] = {"provider": site["envs"][0]["provider"], "live": live_alias, "staging": ", ".join(stg) if stg else None, "wp_version": wpv}
        else:
            doms = ", ".join(sorted({e["domain"] for e in site["envs"] if e["domain"]})) or "no domain"
            unmatched.append(f"{site['envs'][0]['provider']}: {site['base']} [{', '.join(aliases)}] {doms}")

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
