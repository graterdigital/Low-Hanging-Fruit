#!/usr/bin/env python3
"""Run the review half of fix-images across every client on one host: probe, staging dry run, alt sheet. Never applies.

    python scripts/batch_fix_images.py --provider kinsta
    python scripts/batch_fix_images.py --provider kinsta --only a,b,c
    python scripts/batch_fix_images.py --provider kinsta --skip x,y

Per site, in order, stopping that site (never the batch) at the first step that fails:
  1. --probe on staging: Ahrefs "Image file size too large" + server inventory -> reports/<slug>/images-<crawl>.md
     (0 flagged files -> "nothing to compress", alt sheet still written)
  2. dry run on staging: pull + compress locally into changes/<provider>/<slug>/backup/<stamp>-fix-images-staging/{orig,new}
     (nothing is pushed; this is the material for the mandatory visual check)
  3. --alt-csv: review sheet with drafted alt text
Summary in changes/<provider>/_batch-<stamp>-fix-images-review.md: per site, files flagged, MB before/after, how many PNGs
were skipped for lack of pngquant, alt rows by tier, and the two paths a human needs next (the backup folder to eyeball,
the sheet to review). Applies are per site, by hand, after that review: see skills/fix-images/SKILL.md.
Sites are skipped (and listed) when they have no staging alias or no Ahrefs project id.
"""
import argparse, datetime, json, re, shutil, subprocess, sys, traceback
from pathlib import Path
try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

def clients_for(provider, only, skip):
    out = []
    for p in sorted((ROOT / "clients").glob("*.yaml")):
        if p.name.startswith("_"): continue
        c = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        h = c.get("hosting") or {}
        if str(h.get("provider", "")).lower() != provider: continue
        slug = c.get("slug", p.stem)
        if only and slug not in only: continue
        if slug in skip: continue
        if str((c.get("platform") or {}).get("cms", "")).lower() not in ("wordpress", "unknown", ""): continue
        out.append((slug, c))
    return out

def run(args):
    """Run fix_images.py as a subprocess (it uses sys.exit liberally) and return (code, combined output)."""
    r = subprocess.run([sys.executable, str(HERE / "fix_images.py"), *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")

def mb(s):
    m = re.search(r"([\d.]+) (MB|KB) -> ([\d.]+) (MB|KB) across (\d+) originals \+ (\d+) sub-size", s)
    if not m: return None
    def f(v, u): return float(v) * (1 if u == "MB" else 1 / 1024)
    return f(m[1], m[2]), f(m[3], m[4]), int(m[5]), int(m[6])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", required=True)
    ap.add_argument("--only"); ap.add_argument("--skip", default="")
    a = ap.parse_args()
    only = set(a.only.split(",")) if a.only else None; skip = set(x for x in a.skip.split(",") if x)
    sites = clients_for(a.provider, only, skip)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    outdir = ROOT / "changes" / a.provider; outdir.mkdir(parents=True, exist_ok=True)
    pngquant = shutil.which("pngquant") is not None
    print(f"{len(sites)} {a.provider} sites · pngquant {'found' if pngquant else 'NOT on PATH: PNGs will be skipped in the dry run'}")
    rows = []
    for slug, c in sites:
        h = c.get("hosting") or {}; stg = str(h.get("staging_environment") or "unknown")
        pid = (c.get("ahrefs") or {}).get("site_audit_project_id")
        row = {"slug": slug, "domain": c.get("domain"), "status": "", "flagged": None, "before": None, "after": None, "skipped_png": 0,
               "alt": "", "probe_report": "", "backup": "", "sheet": "", "note": ""}
        print(f"\n=== {slug}")
        if stg in ("unknown", "none", ""): row["status"] = "needs staging"; rows.append(row); print("  no staging alias, skipped"); continue
        if not pid or str(pid) == "unknown": row["status"] = "needs ahrefs project"; rows.append(row); print("  no Ahrefs project, skipped"); continue
        try:
            code, out = run([slug, "--probe"])
            if code != 0: row["status"] = "probe failed"; row["note"] = out.strip().splitlines()[-1][:200] if out.strip() else ""; rows.append(row); print("  probe failed:", row["note"]); continue
            m = re.search(r"Ahrefs: (\d+) oversized images", out); row["flagged"] = int(m[1]) if m else None
            m = re.search(r"Report:\s+(\S.*)", out); row["probe_report"] = m[1].strip() if m else ""
            m = re.search(r"(\d+) img without alt", out)
            print(f"  probe: {row['flagged']} flagged, {m[1] if m else '?'} img without alt")
            if row["flagged"]:
                code, out = run([slug])   # staging dry run
                if code != 0: row["status"] = "dry run failed"; row["note"] = out.strip().splitlines()[-1][:200] if out.strip() else ""
                else:
                    r = mb(out)
                    if r: row["before"], row["after"] = round(r[0], 1), round(r[1], 1)
                    row["skipped_png"] = out.count("skipped, pngquant not on PATH")
                    m = re.search(r"Files:\s+(\S.*)", out); row["backup"] = m[1].strip() if m else ""
                    row["status"] = "ready for visual check"
                    print(f"  dry: {row['before']} MB -> {row['after']} MB" + (f", {row['skipped_png']} PNGs skipped (no pngquant)" if row["skipped_png"] else ""))
            else:
                row["status"] = "nothing to compress"; print("  nothing flagged by Ahrefs")
            code, out = run([slug, "--alt-csv"])
            if code == 0:
                m = re.search(r"A (\d+) alt absent · C (\d+) featured images · B (\d+) empty alt inline · D (\d+)", out)
                row["alt"] = f"A {m[1]} · C {m[2]} · B {m[3]}" if m else "written"
                m = re.search(r"rows -> (\S.*)", out); row["sheet"] = m[1].strip() if m else ""
                print(f"  alt sheet: {row['alt']}")
            else:
                row["note"] += " alt sheet failed"
        except Exception:
            row["status"] = "error"; row["note"] = traceback.format_exc().strip().splitlines()[-1][:200]
        rows.append(row)

    md = [f"# fix-images review batch: {a.provider}", "", f"Run {stamp} · {len(rows)} sites · pngquant on this machine: {'yes' if pngquant else 'NO (PNGs skipped; install it and rerun before any apply)'}", "",
          "Nothing was pushed to any site. For each site marked *ready for visual check*: open `backup/.../new/` next to `orig/` at 100% (headshots and gradients first), then apply per site with `python scripts/fix_images.py <slug> --apply`, then live. Alt sheets go to Google Sheets for review, then `merge_alt_sheet.py` and `--alt-apply`.", "",
          "| site | status | flagged | before MB | after MB | PNGs skipped | alt rows (A/C/B) | note |", "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        md.append(f"| {r['slug']} | {r['status']} | {r['flagged'] if r['flagged'] is not None else '-'} | {r['before'] if r['before'] is not None else '-'} | {r['after'] if r['after'] is not None else '-'} | {r['skipped_png'] or '-'} | {r['alt'] or '-'} | {r['note'].strip()} |")
    md += ["", "## Paths", ""]
    for r in rows:
        if r["probe_report"] or r["backup"] or r["sheet"]:
            md += [f"**{r['slug']}**", f"- probe report: `{r['probe_report']}`" if r["probe_report"] else "", f"- dry-run files: `{r['backup']}`" if r["backup"] else "", f"- alt sheet: `{r['sheet']}`" if r["sheet"] else "", ""]
    p = outdir / f"_batch-{stamp}-fix-images-review.md"
    p.write_text("\n".join(x for x in md if x is not None) + "\n", encoding="utf-8")
    print(f"\nSummary: {p}")

if __name__ == "__main__":
    main()
