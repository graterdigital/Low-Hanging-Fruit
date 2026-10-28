#!/usr/bin/env python3
"""Rewrite internal links that point at redirecting URLs so they point at the final page.

    python scripts/fix_redirect_links.py <slug> --map <redirect-map.json>              # dry run on staging
    python scripts/fix_redirect_links.py <slug> --map <redirect-map.json> --apply      # apply on staging
    python scripts/fix_redirect_links.py <slug> --map <redirect-map.json> --target live --apply

Reads clients/<slug>.yaml for the SSH aliases, ships scripts/php/replace_links.php to the site over SSH
with `wp eval-file`, and writes a change log to changes/<slug>/. Dry run is the default; every apply
also saves the full before/after content of each changed post to changes/<slug>/backup/ (git-ignored).
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

def run_remote(alias, mode, host, swaps, webroot="public"):
    job = json.dumps({"mode": mode, "host": host, "swaps": swaps})
    php = (HERE / "php" / "replace_links.php").read_text(encoding="utf-8")
    # Prepend the job as a constant so the PHP file itself stays generic.
    payload = "<?php define('REPLACE_LINKS_JOB', " + json.dumps(job) + "); ?>" + php
    cmd = ["ssh", alias, f"cd {webroot} && wp --skip-plugins={SKIP_PLUGINS} eval-file -"]
    r = subprocess.run(cmd, input=payload.encode("utf-8"), capture_output=True)
    out = r.stdout.decode("utf-8", "replace")
    if "===JSON===" not in out:
        sys.exit(f"Remote run failed.\nstdout:\n{out[-2000:]}\nstderr:\n{r.stderr.decode('utf-8','replace')[-2000:]}")
    return json.loads(out.split("===JSON===", 1)[1].strip())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--map", required=True, help="redirect map JSON (see reports/<slug>/redirect-map-*.json)")
    ap.add_argument("--target", choices=["staging", "live"], default="staging")
    ap.add_argument("--apply", action="store_true", help="write changes; default is dry run")
    ap.add_argument("--webroot", default="public", help="path to WordPress relative to the SSH login dir (Kinsta: public; WP Engine: sites/<install>)")
    args = ap.parse_args()

    client = yaml.safe_load((ROOT / "clients" / f"{args.slug}.yaml").read_text(encoding="utf-8"))
    hosting = client.get("hosting", {})
    alias = hosting.get("ssh_alias") if args.target == "live" else hosting.get("staging_environment")
    if not alias or alias in ("unknown", "none"):
        sys.exit(f"No {args.target} SSH alias in clients/{args.slug}.yaml (hosting.{'ssh_alias' if args.target=='live' else 'staging_environment'}). Run scripts/ssh_config_sync.py first.")
    alias = alias.split(",")[0].strip()
    if hosting.get("provider") == "wpengine" and args.webroot == "public":
        args.webroot = f"sites/{alias}"
    host = client["domain"]
    m = json.loads(Path(args.map).read_text(encoding="utf-8"))
    swaps = m["swaps"]
    if args.target == "live" and args.apply:
        print(f"About to APPLY {len(swaps)} link swaps on LIVE ({alias}). Type the slug to confirm: ", end="", flush=True)
        if input().strip() != args.slug: sys.exit("aborted")

    mode = "apply" if args.apply else "dry"
    print(f"{mode.upper()} on {args.target} ({alias}), {len(swaps)} swap rules, webroot {args.webroot}")
    res = run_remote(alias, mode, host, swaps, args.webroot)

    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    outdir = ROOT / "changes" / args.slug; outdir.mkdir(parents=True, exist_ok=True)
    log = [f"# fix-redirect-links: {host} ({args.target})", "", f"Run {stamp} · mode **{mode}** · alias `{alias}` · map `{Path(args.map).name}`", ""]
    log += ["## Totals (replacements per old URL)", ""] + [f"- `{k}` → {v}" for k, v in sorted(res["totals"].items())] + [""]
    log += [f"## Posts changed ({len(res['posts'])})", "", "| ID | type | title | URL | replacements | applied |", "|---|---|---|---|---|---|"]
    for p in res["posts"]:
        log.append(f"| {p['id']} | {p['type']} | {p['title'][:50]} | {p['url']} | {sum(p['hits'].values())} | {p.get('applied', '-')} |")
    log += ["", f"## Postmeta changed ({len(res['meta'])})", "", "| meta_id | post | key | replacements | note |", "|---|---|---|---|---|"]
    for mm in res["meta"]:
        log.append(f"| {mm['meta_id']} | {mm['post_id']} | {mm['key']} | {sum(mm['hits'].values())} | {mm.get('skipped') or mm.get('applied', '-')} |")
    log += ["", "## Skipped by the map", ""] + [f"- {s.get('old') or s.get('pattern')}: {s['reason']}" for s in m.get("skipped", [])]
    log += ["", "## Rollback", "", "Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.",
            "Postmeta: previous values are in the same backup file."]
    (outdir / f"{stamp}-fix-redirect-links-{args.target}-{mode}.md").write_text("\n".join(log) + "\n", encoding="utf-8")
    if mode == "apply":
        bdir = outdir / "backup"; bdir.mkdir(exist_ok=True)
        (bdir / f"{stamp}-fix-redirect-links-{args.target}.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")

    print(f"\n{len(res['posts'])} posts, {len(res['meta'])} meta rows would change" if mode == "dry" else f"\n{len(res['posts'])} posts, {len(res['meta'])} meta rows changed")
    for k, v in sorted(res["totals"].items()): print(f"  {v:3}  {k}")
    print(f"\nLog: {outdir / (stamp + '-fix-redirect-links-' + args.target + '-' + mode + '.md')}")
    errs = [p for p in res["posts"] if str(p.get("applied", "")).startswith("ERROR")]
    if errs: print(f"\n{len(errs)} posts failed to save; see log.")

if __name__ == "__main__":
    main()
