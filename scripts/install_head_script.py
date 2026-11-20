#!/usr/bin/env python3
"""Install (or remove) a head snippet on every site of a host as a must-use plugin that prints it on wp_head.

    python scripts/install_head_script.py                                  # dry: every WP Engine site, what it would do
    python scripts/install_head_script.py --apply                          # install on live, purge caches, verify
    python scripts/install_head_script.py --apply --only 22spamd,h-md      # subset (also --skip a,b)
    python scripts/install_head_script.py --provider kinsta --apply        # another host
    python scripts/install_head_script.py --remove --apply                 # rollback: delete the mu-plugin everywhere
    python scripts/install_head_script.py --snippet scripts/snippets/x.html --name gd-x --marker SOME-ID --apply

Why a mu-plugin and not header.php: a parent-theme header.php edit dies on the next theme update, and Elementor Canvas /
landing templates skip header.php but still fire wp_head. One file, same on every site; rollback is deleting it.

Per site (live alias from clients/<slug>.yaml):
  1. fetch the home page; if the marker is already in the HTML and our file is not on the server, skip (someone else installed it)
  2. write wp-content/mu-plugins/<name>.php via a temp file, `php -l` it before it goes live
  3. fetch the home page with a cache-busting query; a 5xx or a missing marker removes the file again and reports the site as failed
  4. purge: wp cache flush, the host's page cache, NitroPack where the client file lists it
  5. fetch the plain home page and say whether the cached copy shows the marker yet
Change log: changes/<provider>/<slug>/<stamp>-head-script-live-<dry|apply>.md, summary changes/<provider>/_batch-<stamp>-head-script-<mode>.md
"""
import argparse, datetime, re, subprocess, sys, urllib.request, urllib.error
from pathlib import Path
try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from build_redirect_map import wpengine_webroot  # noqa: E402

SKIP_PLUGINS = "handl-utm-grabber-v3"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36 GraterDigital-LHF/1.0"

def ssh(alias, cmd, inp=None, timeout=120):
    try:
        r = subprocess.run(["ssh", "-o", "BatchMode=yes", alias, cmd], input=inp.encode("utf-8") if inp is not None else None, capture_output=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as e:
        return 255, "", f"ssh {alias}: {e}"
    return r.returncode, r.stdout.decode("utf-8", "replace"), r.stderr.decode("utf-8", "replace")

def fetch(url, timeout=30):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*", "Cache-Control": "no-cache"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return 0, str(e)

def plugin_php(name, snippet):
    return ("<?php\n/**\n * Plugin Name: GD Head Script (" + name + ")\n"
            " * Description: Prints a Grater Digital head snippet on every front-end page. Managed by Low-Hanging-Fruit scripts/install_head_script.py; delete this file to remove it.\n"
            " */\nif (!defined('ABSPATH')) exit;\nadd_action('wp_head', function () { ?>\n"
            f"<!-- {name} -->\n{snippet.strip()}\n<!-- /{name} -->\n"
            "<?php }, 1);\n")

def clients_for(provider, only, skip):
    out = []
    for p in sorted((ROOT / "clients").glob("*.yaml")):
        if p.name.startswith("_"): continue
        c = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        slug = c.get("slug", p.stem); h = c.get("hosting") or {}
        if str(h.get("provider", "")).lower() != provider: continue
        if only and slug not in only: continue
        if slug in skip: continue
        out.append((slug, c))
    return out

def one_site(slug, c, a, name, marker, php):
    """Returns (result, detail, log lines)."""
    h = c.get("hosting") or {}; provider = str(h.get("provider", "")).lower()
    alias = str(h.get("ssh_alias") or "").split(",")[0].strip()
    base = (c.get("canonical_host") or f"https://{c.get('domain')}").rstrip("/")
    log = [f"- Site: {base} · alias `{alias or 'none'}`"]
    if str((c.get("platform") or {}).get("cms", "wordpress")).lower() not in ("wordpress", "unknown", ""): return "skipped", "not WordPress", log
    if not alias or alias in ("unknown", "none"): return "skipped", "no live SSH alias in the client file", log
    webroot = wpengine_webroot(alias) if provider == "wpengine" else "public"
    rel = f"wp-content/mu-plugins/{name}.php"
    code, out, err = ssh(alias, f"cd {webroot} && test -f wp-load.php && (test -f {rel} && echo HAVE || echo NONE)")
    if code != 0 or not out.strip(): return "error", f"ssh/webroot failed: {(err or out).strip()[-160:]}", log
    have = "HAVE" in out
    st0, html0 = fetch(base + "/")
    present0 = marker in html0
    log.append(f"- Before: home page HTTP {st0}, marker `{marker}` {'present' if present0 else 'absent'}, mu-plugin file {'exists' if have else 'absent'}")

    if a.remove:
        if not have: return "nothing to do", "mu-plugin not on the server", log
        if not a.apply: return "would remove", rel, log
        code, out, err = ssh(alias, f"cd {webroot} && rm -f {rel} && echo GONE")
        if "GONE" not in out: return "error", f"remove failed: {(err or out).strip()[-160:]}", log
        log.append(f"- Removed `{rel}`"); purges = purge(alias, webroot, provider, c); log.append(f"- Purge: {purges}")
        return "removed", purges, log

    if present0 and not have: return "already present", "marker already in the page from another source (theme, plugin or GTM); nothing installed", log
    if not a.apply: return ("would update" if have else "would install"), f"{webroot}/{rel}", log
    tmp = f"/tmp/{name}-$$.php"
    cmd = (f"cd {webroot} && mkdir -p wp-content/mu-plugins && cat > {tmp} && php -l {tmp} >/dev/null 2>&1 && "
           f"mv {tmp} {rel} && chmod 644 {rel} && echo INSTALLED || (rm -f {tmp}; echo LINTFAIL)")
    code, out, err = ssh(alias, cmd, php)
    if "INSTALLED" not in out: return "error", f"write failed: {(out + err).strip()[-160:]}", log
    log.append(f"- Wrote `{rel}` ({len(php)} bytes). Rollback: `ssh {alias} \"rm {webroot}/{rel}\"` or `python scripts/install_head_script.py --remove --apply --only {slug}`")
    stamp = datetime.datetime.now().strftime("%H%M%S")
    st1, html1 = fetch(f"{base}/?gdcb={stamp}")
    if st1 >= 500 or st1 == 0 or (st1 == 200 and marker not in html1):
        ssh(alias, f"cd {webroot} && rm -f {rel}")
        log.append(f"- Verify FAILED (HTTP {st1}, marker {'present' if marker in html1 else 'absent'}); file removed again")
        return "error", f"verify failed (HTTP {st1}); rolled back", log
    purges = purge(alias, webroot, provider, c)
    st2, html2 = fetch(base + "/")
    cached = "live on cached home page" if marker in html2 else "cached home page not showing it yet (will after cache expiry / purge)"
    nitro = ""
    if marker in html2:
        m = re.search(r"<script[^>]*" + re.escape(marker) + r"[^>]*>", html2)
        tag = m.group(0) if m else ""
        if "nitro" in tag.lower(): nitro = f" · NitroPack is rewriting the tag: `{tag[:140]}` (add an exclusion if it must load undelayed)"
    log += [f"- Verify (cache-busted): HTTP {st1}, marker present", f"- Purge: {purges}", f"- After purge: HTTP {st2}, {cached}{nitro}"]
    return ("updated" if have else "installed"), f"{cached} · purge: {purges}{nitro}", log

def purge(alias, webroot, provider, c):
    wp = f"cd {webroot} && wp --skip-plugins={SKIP_PLUGINS}"
    res = []
    code, _, _ = ssh(alias, f"{wp} cache flush"); res.append(f"object {'ok' if code == 0 else 'FAILED'}")
    code, out, err = ssh(alias, f"{wp} {'kinsta cache purge --all' if provider == 'kinsta' else 'page-cache flush'}"); res.append(f"page {'ok' if code == 0 else 'FAILED'}")
    if "nitropack" in [str(x).lower() for x in ((c.get("platform") or {}).get("perf_plugins") or [])]:
        code, out, err = ssh(alias, f"cd {webroot} && wp nitropack purge"); res.append(f"nitropack {'ok' if code == 0 else 'FAILED: ' + (err or out).strip()[-80:]}")
    return ", ".join(res)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", default="wpengine"); ap.add_argument("--only"); ap.add_argument("--skip", default="")
    ap.add_argument("--snippet", default=str(HERE / "snippets" / "gd-gtm.html")); ap.add_argument("--name", default="gd-head-script")
    ap.add_argument("--marker", help="string that proves the snippet is in the page; default: the first GTM-/G-/AW- id in the snippet")
    ap.add_argument("--apply", action="store_true"); ap.add_argument("--remove", action="store_true")
    a = ap.parse_args()
    snippet = Path(a.snippet).read_text(encoding="utf-8")
    if "<?" in snippet or "?>" in snippet: sys.exit("snippet contains PHP tags; refusing")
    if re.search(r"[‘’“”]", snippet): sys.exit("snippet contains curly quotes; it would not run. Straighten them first.")
    if not re.fullmatch(r"[a-z0-9-]+", a.name): sys.exit("--name: lowercase letters, digits, hyphens")
    m = re.search(r"\b(GTM-[A-Z0-9]+|G-[A-Z0-9]+|AW-\d+)\b", snippet)
    marker = a.marker or (m.group(1) if m else None)
    if not marker: sys.exit("no --marker and no tag id found in the snippet")
    only = set(a.only.split(",")) if a.only else None; skip = {x for x in a.skip.split(",") if x}
    sites = clients_for(a.provider.lower(), only, skip)
    if not sites: sys.exit("no matching client files")
    php = plugin_php(a.name, snippet)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    mode = ("remove-" if a.remove else "") + ("apply" if a.apply else "dry")
    print(f"head-script {mode} on {len(sites)} {a.provider} site(s) · marker {marker} · file wp-content/mu-plugins/{a.name}.php")
    rows = []
    for slug, c in sites:
        try: res, detail, log = one_site(slug, c, a, a.name, marker, php)
        except Exception as e: res, detail, log = "error", f"{type(e).__name__}: {e}"[:200], []
        rows.append((slug, res, detail)); print(f"  {slug:26} {res:16} {detail}")
        if a.apply and res not in ("skipped", "nothing to do"):
            d = ROOT / "changes" / a.provider / slug; d.mkdir(parents=True, exist_ok=True)
            (d / f"{stamp}-head-script-live-{mode}.md").write_text("\n".join([f"# head-script {mode} · {slug} · live", "", f"Run {stamp} · snippet `{Path(a.snippet).name}` · marker `{marker}` · result **{res}**", "", *log, "", "## Snippet", "", "```html", snippet.strip(), "```"]) + "\n", encoding="utf-8")
    outdir = ROOT / "changes" / a.provider; outdir.mkdir(parents=True, exist_ok=True)
    p = outdir / f"_batch-{stamp}-head-script-{mode}.md"
    p.write_text("\n".join([f"# Batch head-script {mode} on {a.provider}", "", f"Run {stamp} · {len(sites)} site(s) · marker `{marker}` · `wp-content/mu-plugins/{a.name}.php`", "", "| Site | Result | Detail |", "|---|---|---|"] + [f"| {s} | {r} | {d} |" for s, r, d in rows]) + "\n", encoding="utf-8")
    bad = [s for s, r, _ in rows if r == "error"]
    print(f"Summary: {p}" + (f"\nFAILED: {', '.join(bad)}" if bad else ""))
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
