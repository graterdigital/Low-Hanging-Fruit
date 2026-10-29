#!/usr/bin/env python3
"""Put original image files back from a fix-images backup.

    python scripts/restore_images.py <slug> --target live --only madison-alexander,sarah-price      # named files (+ their sub-sizes)
    python scripts/restore_images.py <slug> --target live --all                                     # everything that run replaced
    python scripts/restore_images.py <slug> --target live --all --dry                               # list only

Reads changes/<provider>/<slug>/backup/<stamp>-fix-images-<target>/result.json (newest for the target unless --result),
pushes each matching file's `orig/` copy back to the remote path recorded there, rewrites the .webp sibling with cwebp
when --webp is given (for hosts that serve name.webp), and flushes caches. Writes a short log next to the other logs.
"""
import argparse, datetime, json, subprocess, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SKIP = "handl-utm-grabber-v3"

def run(args, inp=None):
    r = subprocess.run(args, input=inp, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace"), r.stderr.decode("utf-8", "replace")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug"); ap.add_argument("--target", choices=["staging", "live"], default="staging")
    ap.add_argument("--only", help="comma-separated substrings of file paths to restore")
    ap.add_argument("--all", action="store_true"); ap.add_argument("--dry", action="store_true")
    ap.add_argument("--webp", action="store_true", help="also rewrite name.webp next to each restored file with cwebp -q 85")
    ap.add_argument("--result"); ap.add_argument("--webroot", default="public")
    a = ap.parse_args()
    if not a.only and not a.all: sys.exit("give --only <substrings> or --all")
    client = yaml.safe_load((ROOT / "clients" / f"{a.slug}.yaml").read_text(encoding="utf-8"))
    h = client["hosting"]; alias = (h["ssh_alias"] if a.target == "live" else h["staging_environment"]).split(",")[0].strip()
    provider = str(h.get("provider") or "other").lower()
    if provider == "wpengine" and a.webroot == "public": a.webroot = f"sites/{alias}"
    cdir = ROOT / "changes" / provider / a.slug
    res = Path(a.result) if a.result else sorted((cdir / "backup").glob(f"*-fix-images-{a.target}/result.json"))[-1]
    bdir = res.parent
    rows = [r for r in json.loads(res.read_text(encoding="utf-8")) if r.get("action") == "replaced"]
    if a.only: rows = [r for r in rows if any(s in r["path"] for s in a.only.split(","))]
    print(f"{len(rows)} files to restore on {a.target} ({alias}) from {bdir.relative_to(ROOT)}")
    done, failed = [], []
    for r in rows:
        local = bdir / "orig" / Path(r["path"]).name
        if not local.exists(): failed.append((r["path"], "no orig copy")); print(f"  !! {r['path']}: no orig copy"); continue
        if a.dry: print(f"  would restore {r['path']} ({local.stat().st_size//1024} KB)"); continue
        code, out, err = run(["scp", "-q", str(local), f"{alias}:{r['remote']}"])
        if code == 0: done.append(r); print(f"  OK {r['path']} ({local.stat().st_size//1024} KB)")
        else: failed.append((r["path"], err.strip())); print(f"  !! {r['path']}: {err.strip()}")
    if a.dry: return
    if a.webp and done:
        script = "\n".join(f"cwebp -quiet -q 85 '{r['remote']}' -o '{r['remote'].rsplit('.',1)[0]}.webp' && echo OK || echo FAIL {r['remote']}" for r in done) + "\n"
        code, out, err = run(["ssh", alias, "bash -s"], script.encode("utf-8"))
        print(f"webp siblings: {out.count('OK')} written, {out.count('FAIL')} failed")
    for c in (f"cd {a.webroot} && wp --skip-plugins={SKIP} cache flush", f"cd {a.webroot} && wp --skip-plugins={SKIP} kinsta cache purge --all"):
        code, out, err = run(["ssh", alias, c]); print((out + err).strip().splitlines()[-1:] or ["(no output)"])
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    log = [f"# fix-images: restore originals on {client['domain']} ({a.target})", "", f"Run {stamp} · alias `{alias}` · from `{bdir.name}` · filter `{a.only or 'all'}` · webp siblings {'rewritten' if a.webp else 'untouched'}", "",
           f"Restored {len(done)}, failed {len(failed)}.", ""] + [f"- `{r['path']}`" for r in done] + [f"- FAILED `{p}`: {e}" for p, e in failed]
    (cdir / f"{stamp}-fix-images-{a.target}-restore.md").write_text("\n".join(log) + "\n", encoding="utf-8")
    print(f"Log: {cdir / f'{stamp}-fix-images-{a.target}-restore.md'}")

if __name__ == "__main__":
    main()
