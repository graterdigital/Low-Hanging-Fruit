#!/usr/bin/env python3
"""Roll back a fix-redirect-links run from its backup JSON.

    python scripts/restore_changes.py <slug> --backup changes/kinsta/<slug>/backup/<stamp>-fix-redirect-links-staging.json
    python scripts/restore_changes.py <slug> --backup ... --apply
    python scripts/restore_changes.py <slug> --backup ... --only-meta-keys _elementor_data     # restore just those meta keys

Target (staging/live) and alias come from the backup file name and the client file. Dry run is the default and
reports, per row: would restore / already restored / modified since (left alone) / missing. Rows are restored only
when they still hold exactly what the fix wrote, so a human edit made after the run is never overwritten.
Writes a log to changes/<provider>/<slug>/<stamp>-restore-<target>-<mode>.md and flushes the object cache after an apply.
"""
import argparse, json, re, subprocess, sys, datetime
from pathlib import Path
import importlib.util

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
spec = importlib.util.spec_from_file_location("frl", HERE / "fix_redirect_links.py"); frl = importlib.util.module_from_spec(spec); spec.loader.exec_module(frl)
import yaml

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--backup", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only-meta-keys", default="", help="comma-separated meta keys; restores only those meta rows and no posts")
    ap.add_argument("--webroot", default="public")
    args = ap.parse_args()

    bp = Path(args.backup)
    m = re.search(r"-(staging|live)\.json$", bp.name)
    if not m: sys.exit("backup file name should end in -staging.json or -live.json")
    target = m.group(1)
    client = yaml.safe_load((ROOT / "clients" / f"{args.slug}.yaml").read_text(encoding="utf-8"))
    hosting = client.get("hosting", {})
    alias = (hosting.get("ssh_alias") if target == "live" else hosting.get("staging_environment")) or ""
    alias = alias.split(",")[0].strip()
    if not alias or alias in ("unknown", "none"): sys.exit(f"no {target} alias in clients/{args.slug}.yaml")
    provider = str(hosting.get("provider") or "other").lower()
    if provider == "wpengine" and args.webroot == "public": args.webroot = f"sites/{alias}"

    b = json.loads(bp.read_text(encoding="utf-8"))
    posts = [{"id": p["id"], "before": p["before"], "after": p.get("after")} for p in b.get("posts", []) if "before" in p]
    meta = [{"meta_id": x["meta_id"], "before": x["before"], "after": x.get("after")} for x in b.get("meta", []) if "before" in x]
    keys = {k.strip() for k in args.only_meta_keys.split(",") if k.strip()}
    if keys:
        wanted = {x["meta_id"] for x in b.get("meta", []) if x.get("key") in keys}
        meta = [x for x in meta if x["meta_id"] in wanted]; posts = []
    mode = "apply" if args.apply else "dry"
    if target == "live" and args.apply:
        print(f"About to RESTORE {len(posts)} posts and {len(meta)} meta rows on LIVE ({alias}). Type the slug to confirm: ", end="", flush=True)
        if input().strip() != args.slug: sys.exit("aborted")

    job = json.dumps({"mode": mode, "posts": posts, "meta": meta})
    php = (HERE / "php" / "restore_links.php").read_text(encoding="utf-8")
    payload = "<?php define('RESTORE_LINKS_JOB', " + json.dumps(job) + "); ?>" + php
    cmd = ["ssh", alias, f"cd {args.webroot} && wp --skip-plugins={frl.SKIP_PLUGINS} eval-file -"]
    r = subprocess.run(cmd, input=payload.encode("utf-8"), capture_output=True)
    out = r.stdout.decode("utf-8", "replace")
    if "===JSON===" not in out:
        sys.exit(f"Remote run failed.\nstdout:\n{out[-2000:]}\nstderr:\n{r.stderr.decode('utf-8','replace')[-2000:]}")
    res = json.loads(out.split("===JSON===", 1)[1].strip())
    if mode == "apply":
        ok, msg = frl.flush_cache(alias, args.webroot); print(f"Cache flush: {'ok' if ok else 'FAILED'} {msg}")

    def tally(rows):
        t = {}
        for x in rows: t[x["result"].split(";")[0]] = t.get(x["result"].split(";")[0], 0) + 1
        return t
    tp, tm = tally(res["posts"]), tally(res["meta"])
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    outdir = ROOT / "changes" / provider / args.slug; outdir.mkdir(parents=True, exist_ok=True)
    log = [f"# restore from backup: {client['domain']} ({target})", "", f"Run {stamp} · mode **{mode}** · alias `{alias}` · backup `{bp.name}`" + (f" · meta keys {sorted(keys)}" if keys else ""), "",
           "## Posts", ""] + [f"- {k}: {v}" for k, v in tp.items()] + ["", "## Postmeta", ""] + [f"- {k}: {v}" for k, v in tm.items()] + ["", "## Rows not restored", ""]
    log += [f"- post {x['id']}: {x['result']}" for x in res["posts"] if x["result"] not in ("restored", "would restore", "already restored")]
    log += [f"- meta {x['meta_id']}: {x['result']}" for x in res["meta"] if x["result"] not in ("restored", "would restore", "already restored")]
    (outdir / f"{stamp}-restore-{target}-{mode}.md").write_text("\n".join(log) + "\n", encoding="utf-8")
    print(f"{mode.upper()} restore on {target} ({alias}) from {bp.name}")
    print("  posts:", tp); print("  meta: ", tm)
    print(f"Log: {outdir / (stamp + '-restore-' + target + '-' + mode + '.md')}")

if __name__ == "__main__":
    main()
