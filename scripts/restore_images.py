#!/usr/bin/env python3
"""Put original image files back from a fix-images backup.

    python scripts/restore_images.py <slug> --target live --only madison-alexander,sarah-price      # named files (+ their sub-sizes)
    python scripts/restore_images.py <slug> --target live --all                                     # everything that run touched
    python scripts/restore_images.py <slug> --target live --all --dry                               # list only

Reads changes/<provider>/<slug>/backup/<stamp>-fix-images-<target>/result.json, pushes each matching file's `orig/`
copy back to the remote path recorded there, rewrites the .webp sibling with cwebp when --webp is given (for hosts
that serve name.webp), flushes caches, and verifies the remote byte size against the pushed copy.

Which backup: the OLDEST run for the target unless --result names one. Every run (dry or apply) pulls the server's
files into orig/ before compressing, so the oldest run's orig/ is the true original; a later run's orig/ is the
earlier run's output. Dry runs count: their rows say "would replace" instead of "replaced", but the orig/ copy is the
same pull. (2026-11-02: the first staging run was a dry run, so filtering on "replaced" only found 0 files and
restored nothing; that is why this reads both.)
"""
import argparse, datetime, json, subprocess, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SKIP = "handl-utm-grabber-v3"
RESTORABLE = ("replaced", "would replace")

def run(args, inp=None):
    r = subprocess.run(args, input=inp, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace"), r.stderr.decode("utf-8", "replace")

def load_rows(res: Path):
    return [r for r in json.loads(res.read_text(encoding="utf-8")) if r.get("action") in RESTORABLE]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug"); ap.add_argument("--target", choices=["staging", "live"], default="staging")
    ap.add_argument("--only", help="comma-separated substrings of file paths to restore")
    ap.add_argument("--all", action="store_true"); ap.add_argument("--dry", action="store_true")
    ap.add_argument("--webp", action="store_true", help="also rewrite name.webp next to each restored file with cwebp -q 85")
    ap.add_argument("--result", help="a specific backup's result.json (default: the oldest run for the target)")
    ap.add_argument("--webroot", default="public")
    a = ap.parse_args()
    if not a.only and not a.all: sys.exit("give --only <substrings> or --all")
    client = yaml.safe_load((ROOT / "clients" / f"{a.slug}.yaml").read_text(encoding="utf-8"))
    h = client["hosting"]; alias = (h["ssh_alias"] if a.target == "live" else h["staging_environment"]).split(",")[0].strip()
    provider = str(h.get("provider") or "other").lower()
    if provider == "wpengine" and a.webroot == "public": a.webroot = f"sites/{alias}"
    cdir = ROOT / "changes" / provider / a.slug
    if a.result:
        res = Path(a.result).resolve()
    else:
        runs = sorted((cdir / "backup").glob(f"*-fix-images-{a.target}/result.json"))
        if not runs: sys.exit(f"no fix-images backup for {a.target} under {cdir / 'backup'}")
        # Oldest run that actually holds pulled files. A later run's orig/ is an earlier run's output, not the real original.
        res = next((r for r in runs if load_rows(r)), None)
        if res is None: sys.exit(f"{len(runs)} runs found for {a.target} but none has restorable rows (replaced / would replace)")
        was_dry = not any(r.get("action") == "replaced" for r in load_rows(res))
        print(f"{len(runs)} run(s) for {a.target}; restoring from the OLDEST with pulled files: {res.parent.name}"
              + (" (a dry run; its orig/ is the server's file as of that pull)" if was_dry else "") + ". Use --result to pick another.")
    bdir = res.parent
    rows = load_rows(res)
    if a.only: rows = [r for r in rows if any(s in r["path"] for s in a.only.split(","))]
    if not rows: sys.exit(f"0 files match in {bdir.name}; nothing restored (check --only, or --result)")
    print(f"{len(rows)} files to restore on {a.target} ({alias}) from {bdir.name}")
    done, failed = [], []
    for r in rows:
        local = bdir / "orig" / Path(r["path"]).name
        if not local.exists(): failed.append((r["path"], "no orig copy")); print(f"  !! {r['path']}: no orig copy"); continue
        if a.dry: print(f"  would restore {r['path']} ({local.stat().st_size//1024} KB)"); continue
        code, out, err = run(["scp", "-q", str(local), f"{alias}:{r['remote']}"])
        if code == 0: done.append(r); print(f"  OK {r['path']} ({local.stat().st_size//1024} KB)")
        else: failed.append((r["path"], err.strip())); print(f"  !! {r['path']}: {err.strip()}")
    if a.dry: return
    # verify: remote byte size must equal the pushed copy
    verified = mismatched = 0
    if done:
        script = "\n".join(f"stat -c '%s %n' '{r['remote']}'" for r in done) + "\n"
        code, out, err = run(["ssh", alias, "bash -s"], script.encode("utf-8"))
        sizes = {line.split(" ", 1)[1]: int(line.split(" ", 1)[0]) for line in out.splitlines() if " " in line}
        for r in done:
            want = (bdir / "orig" / Path(r["path"]).name).stat().st_size
            got = sizes.get(r["remote"])
            if got == want: verified += 1
            else: mismatched += 1; print(f"  ?? {r['path']}: remote is {got} bytes, pushed {want}")
        print(f"verified on server: {verified} match, {mismatched} mismatch")
    if a.webp and done:
        script = "\n".join(f"cwebp -quiet -q 85 '{r['remote']}' -o '{r['remote'].rsplit('.',1)[0]}.webp' && echo OK || echo FAIL {r['remote']}" for r in done) + "\n"
        code, out, err = run(["ssh", alias, "bash -s"], script.encode("utf-8"))
        print(f"webp siblings: {out.count('OK')} written, {out.count('FAIL')} failed")
    for c in (f"cd {a.webroot} && wp --skip-plugins={SKIP} cache flush", f"cd {a.webroot} && wp --skip-plugins={SKIP} kinsta cache purge --all"):
        code, out, err = run(["ssh", alias, c]); print((out + err).strip().splitlines()[-1:] or ["(no output)"])
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    log = [f"# fix-images: restore originals on {client['domain']} ({a.target})", "", f"Run {stamp} · alias `{alias}` · from `{bdir.name}` · filter `{a.only or 'all'}` · webp siblings {'rewritten' if a.webp else 'untouched'}", "",
           f"Restored {len(done)}, failed {len(failed)}, size-verified on server {verified} (mismatch {mismatched}).", ""] + [f"- `{r['path']}`" for r in done] + [f"- FAILED `{p}`: {e}" for p, e in failed]
    (cdir / f"{stamp}-fix-images-{a.target}-restore.md").write_text("\n".join(log) + "\n", encoding="utf-8")
    print(f"Log: {cdir / f'{stamp}-fix-images-{a.target}-restore.md'}")

if __name__ == "__main__":
    main()
