#!/usr/bin/env python3
"""Recreate .webp siblings for images a fix-images run replaced, on a host whose web server still serves
<image>.webp (or <image>.<ext>.webp) when a browser accepts WebP. Uses cwebp on the server.

    python scripts/regen_webp_siblings.py <slug> [--target staging|live] [--naming auto|append|replace] [--quality 80]

Reads the newest fix-images apply log's backup/result.json for the list of replaced files (originals and sub-sizes),
then runs cwebp over SSH for each. --naming auto looks at existing .webp files in uploads/ to pick
`photo.png.webp` (append) or `photo.webp` (replace); both are written if it cannot tell.
"""
import argparse, json, subprocess, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SKIP = "handl-utm-grabber-v3"

def ssh(alias, cmd):
    r = subprocess.run(["ssh", alias, cmd], capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace"), r.stderr.decode("utf-8", "replace")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug"); ap.add_argument("--target", choices=["staging", "live"], default="staging")
    ap.add_argument("--naming", choices=["auto", "append", "replace", "both"], default="auto")
    ap.add_argument("--quality", type=int, default=80); ap.add_argument("--webroot", default="public")
    ap.add_argument("--result", help="backup/<stamp>-fix-images-<target>/result.json; default: newest for this target")
    a = ap.parse_args()
    client = yaml.safe_load((ROOT / "clients" / f"{a.slug}.yaml").read_text(encoding="utf-8"))
    h = client["hosting"]; alias = (h["ssh_alias"] if a.target == "live" else h["staging_environment"]).split(",")[0].strip()
    provider = str(h.get("provider") or "other").lower()
    if provider == "wpengine" and a.webroot == "public": a.webroot = f"sites/{alias}"
    cdir = ROOT / "changes" / provider / a.slug / "backup"
    res = Path(a.result) if a.result else sorted(cdir.glob(f"*-fix-images-{a.target}/result.json"))[-1]
    rows = json.loads(res.read_text(encoding="utf-8"))
    rels = sorted({r["path"] for r in rows if r.get("action") == "replaced"})
    print(f"{len(rels)} replaced files from {res.relative_to(ROOT)} on {a.target} ({alias})")

    code, out, _ = ssh(alias, f"cd {a.webroot} && wp --skip-plugins={SKIP} eval 'echo wp_upload_dir()[\"basedir\"];'")
    base = out.strip()
    if not base.startswith("/"): sys.exit("could not resolve uploads dir: " + out)
    naming = a.naming
    if naming == "auto":
        code, out, _ = ssh(alias, f"find {base} -name '*.webp' | head -200")
        names = out.split()
        app = sum(1 for n in names if n.endswith((".png.webp", ".jpg.webp", ".jpeg.webp")))
        rep = len(names) - app
        naming = "append" if app > rep else "replace" if rep > app else "both"
        print(f"naming: {naming} (saw {app} appended-style, {rep} replaced-style .webp files)")
    cmds = []
    for rel in rels:
        src = f"{base}/{rel}"
        outs = []
        if naming in ("append", "both"): outs.append(src + ".webp")
        if naming in ("replace", "both"): outs.append(src.rsplit(".", 1)[0] + ".webp")
        for o in outs: cmds.append(f"cwebp -quiet -q {a.quality} '{src}' -o '{o}' && echo OK '{o}' || echo FAIL '{src}'")
    code, out, err = ssh(alias, " ; ".join(cmds))
    ok = out.count("OK "); fail = out.count("FAIL ")
    print(out[-3000:]); print(f"\n{ok} webp written, {fail} failed")
    for c in (f"cd {a.webroot} && wp --skip-plugins={SKIP} cache flush", f"cd {a.webroot} && wp --skip-plugins={SKIP} kinsta cache purge --all"):
        code, out, err = ssh(alias, c); print((out + err).strip().splitlines()[-1:] or ["(no output)"])

if __name__ == "__main__":
    main()
