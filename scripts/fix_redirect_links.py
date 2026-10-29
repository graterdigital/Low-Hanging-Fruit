#!/usr/bin/env python3
"""Rewrite internal links that point at redirecting URLs so they point at the final page.

    python scripts/fix_redirect_links.py <slug> --map <redirect-map.json>              # dry run on staging
    python scripts/fix_redirect_links.py <slug> --map <redirect-map.json> --apply      # apply on staging
    python scripts/fix_redirect_links.py <slug> --map <redirect-map.json> --target live --apply

Reads clients/<slug>.yaml for the SSH aliases, ships scripts/php/replace_links.php to the site over SSH
with `wp eval-file`, and writes a change log to changes/<provider>/<slug>/ (provider from the client file:
kinsta, wpengine, ...). Dry run is the default; every apply also saves the full before/after content of
each changed post to changes/<provider>/<slug>/backup/ (git-ignored) and flushes the object cache.
A second, report-only log lists wp_options rows that still contain an old URL; the script never edits options.
Live applies ask you to type the slug unless --yes is given.
"""
import argparse, json, re, subprocess, sys, datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SKIP_PLUGINS = "handl-utm-grabber-v3"   # prints PHP warnings under CLI; harmless but noisy

def run_remote(alias, mode, host, swaps, webroot="public", legacy_hosts=None):
    job = json.dumps({"mode": mode, "host": host, "swaps": swaps, "legacy_hosts": legacy_hosts or []})
    php = (HERE / "php" / "replace_links.php").read_text(encoding="utf-8")
    # Prepend the job as a constant so the PHP file itself stays generic.
    payload = "<?php define('REPLACE_LINKS_JOB', " + json.dumps(job) + "); ?>" + php
    cmd = ["ssh", alias, f"cd {webroot} && wp --skip-plugins={SKIP_PLUGINS} eval-file -"]
    r = subprocess.run(cmd, input=payload.encode("utf-8"), capture_output=True)
    out = r.stdout.decode("utf-8", "replace")
    if "===JSON===" not in out:
        sys.exit(f"Remote run failed.\nstdout:\n{out[-2000:]}\nstderr:\n{r.stderr.decode('utf-8','replace')[-2000:]}")
    return json.loads(out.split("===JSON===", 1)[1].strip())

def flush_cache(alias, webroot="public"):
    """wp cache flush after an apply: postmeta is written straight to the table, so a persistent object
    cache (Kinsta's Redis, WP Engine's) would otherwise keep serving the old ACF values."""
    r = subprocess.run(["ssh", alias, f"cd {webroot} && wp --skip-plugins={SKIP_PLUGINS} cache flush"], capture_output=True)
    msg = (r.stdout.decode("utf-8", "replace") + r.stderr.decode("utf-8", "replace")).strip().splitlines()
    return (r.returncode == 0, msg[-1] if msg else "")

def confirm_live(slug, n, alias, yes):
    if yes:
        print(f"APPLY {n} link swaps on LIVE ({alias}) — confirmed by --yes"); return
    if not sys.stdin.isatty():
        sys.exit("Live apply needs a terminal to confirm, or pass --yes.")
    print(f"About to APPLY {n} link swaps on LIVE ({alias}). Type the slug to confirm: ", end="", flush=True)
    if input().strip() != slug: sys.exit("aborted")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--map", required=True, help="redirect map JSON (see reports/<slug>/redirect-map-*.json)")
    ap.add_argument("--target", choices=["staging", "live"], default="staging")
    ap.add_argument("--apply", action="store_true", help="write changes; default is dry run")
    ap.add_argument("--probe", action="store_true", help="locate every raw occurrence of each old URL (posts, meta, options) and stop; changes nothing")
    ap.add_argument("--webroot", default="public", help="path to WordPress relative to the SSH login dir (Kinsta: public; WP Engine: sites/<install>)")
    ap.add_argument("--yes", action="store_true", help="skip the type-the-slug confirmation on a live apply (for vetted, unattended runs)")
    args = ap.parse_args()

    client = yaml.safe_load((ROOT / "clients" / f"{args.slug}.yaml").read_text(encoding="utf-8"))
    hosting = client.get("hosting", {})
    alias = hosting.get("ssh_alias") if args.target == "live" else hosting.get("staging_environment")
    if not alias or alias in ("unknown", "none"):
        sys.exit(f"No {args.target} SSH alias in clients/{args.slug}.yaml (hosting.{'ssh_alias' if args.target=='live' else 'staging_environment'}). Run scripts/ssh_config_sync.py first.")
    alias = alias.split(",")[0].strip()
    provider = str(hosting.get("provider") or "other").strip().lower()
    if provider in ("", "unknown", "none"): provider = "other"
    if provider == "wpengine" and args.webroot == "public":
        args.webroot = f"sites/{alias}"
    host = client["domain"]
    m = json.loads(Path(args.map).read_text(encoding="utf-8"))
    swaps = m["swaps"]
    if args.target == "live" and args.apply:
        confirm_live(args.slug, len(swaps), alias, args.yes)

    if args.probe:
        res = run_remote(alias, "probe", host, swaps, args.webroot, m.get("legacy_hosts"))
        print(f"Install runs on {res['home_host']}; matching hosts: {', '.join(res['hosts'])}")
        occ = res["occurrences"]
        print(f"PROBE on {args.target} ({alias}): {len(occ)} occurrences")
        by = {}
        for o in occ: by.setdefault(o["old"], []).append(o)
        for s_ in swaps:
            items = by.get(s_["old"], [])
            print(f"\n== {s_['old']}  ({len(items)} found)")
            for o in items: print(f"   {o['where']}\n      ...{o['ctx'].replace(chr(10),' ')}...")
        return

    mode = "apply" if args.apply else "dry"
    print(f"{mode.upper()} on {args.target} ({alias}), {len(swaps)} swap rules, webroot {args.webroot}")
    res = run_remote(alias, mode, host, swaps, args.webroot, m.get("legacy_hosts"))
    print(f"Install runs on {res['home_host']}; matching hosts: {', '.join(res['hosts'])}")

    if not isinstance(res.get("totals"), dict): res["totals"] = {}   # PHP encodes an empty array as []
    flushed = None
    if mode == "apply":
        flushed = flush_cache(alias, args.webroot)
        print(f"Cache flush: {'ok' if flushed[0] else 'FAILED'} {flushed[1]}")
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    outdir = ROOT / "changes" / provider / args.slug; outdir.mkdir(parents=True, exist_ok=True)
    base = f"{stamp}-fix-redirect-links-{args.target}"
    log = [f"# fix-redirect-links: {host} ({args.target})", "", f"Run {stamp} · mode **{mode}** · alias `{alias}` · provider `{provider}` · map `{Path(args.map).name}`", ""]
    log += [f"Install host `{res['home_host']}`; hosts matched: {', '.join('`'+h+'`' for h in res['hosts'])}. Entries starting `host:` are legacy-host links moved to the current host.", ""]
    if flushed is not None:
        log += [f"Object cache flush after apply: {'ok' if flushed[0] else 'FAILED'}" + (f" (`{flushed[1]}`)" if flushed[1] else ""), ""]
    log += ["## Totals (replacements per old URL)", ""] + [f"- `{k}` → {v}" for k, v in sorted(res["totals"].items())] + [""]
    log += [f"## Posts changed ({len(res['posts'])})", "", "| ID | type | title | URL | replacements | applied |", "|---|---|---|---|---|---|"]
    for p in res["posts"]:
        log.append(f"| {p['id']} | {p['type']} | {p['title'][:50]} | {p['url']} | {sum(p['hits'].values())} | {p.get('applied', '-')} |")
    log += ["", f"## Postmeta changed ({len(res['meta'])})", "", "| meta_id | post | key | kind | replacements | applied |", "|---|---|---|---|---|---|"]
    for mm in res["meta"]:
        log.append(f"| {mm['meta_id']} | {mm['post_id']} | {mm['key']} | {mm.get('kind','')} | {sum(mm['hits'].values())} | {mm.get('applied', '-')} |")
    log += ["", "## Skipped by the map", ""] + [f"- {s.get('old') or s.get('pattern')}: {s['reason']}" for s in m.get("skipped", [])]
    opts = res.get("options") or []
    log += ["", f"## wp_options still referencing old URLs ({len(opts)}, not changed)", "",
            f"See `{base}-options.md` next to this log. Widgets, theme mods, menus and plugin settings live here and need a hand or a different skill." if opts else "None found."]
    log += ["", "## Rollback", "", "Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.",
            "Postmeta: previous values are in the same backup file."]
    main_log = outdir / f"{base}-{mode}.md"
    main_log.write_text("\n".join(log) + "\n", encoding="utf-8")

    # Secondary, report-only log: wp_options rows that contain an old path or legacy host.
    olog = [f"# fix-redirect-links: wp_options hits for {host} ({args.target})", "",
            f"Run {stamp} · mode **{mode}** · companion to `{main_log.name}`. Report only: the script never edits options.", "",
            "Each row is an option whose value contains an old URL (transients are excluded). `autoload` and size help tell a widget or menu setting from an analytics or cache blob, which can be ignored.", ""]
    if opts:
        olog += ["| option_name | autoload | bytes | old URL | context |", "|---|---|---|---|---|"]
        for o in opts:
            ctx = o["ctx"].replace("\n", " ").replace("|", "\\|")
            olog.append(f"| `{o['option_name']}` | {o['autoload']} | {o['size']} | `{o['old']}` | ...{ctx}... |")
    else:
        olog.append("No option values reference any of the old URLs or legacy hosts.")
    (outdir / f"{base}-options.md").write_text("\n".join(olog) + "\n", encoding="utf-8")

    if mode == "apply":
        bdir = outdir / "backup"; bdir.mkdir(exist_ok=True)
        (bdir / f"{base}.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")

    print(f"\n{len(res['posts'])} posts, {len(res['meta'])} meta rows would change" if mode == "dry" else f"\n{len(res['posts'])} posts, {len(res['meta'])} meta rows changed")
    for k, v in sorted(res["totals"].items()): print(f"  {v:3}  {k}")
    print(f"  {len(opts)} wp_options rows still reference old URLs (not changed; see the -options.md log)")
    print(f"\nLog: {main_log}\nOptions log: {outdir / (base + '-options.md')}")
    errs = [p for p in res["posts"] if str(p.get("applied", "")).startswith("ERROR")]
    if errs: print(f"\n{len(errs)} posts failed to save; see log.")

if __name__ == "__main__":
    main()
