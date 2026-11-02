#!/usr/bin/env python3
"""Run fix-meta across the roster: probe + review-sheet push for every client (the review half), or the approved-rows apply.

    python scripts/batch_fix_meta.py                                   # every client with an Ahrefs project: --probe --sheet (drafts: --draft if ANTHROPIC_API_KEY is set)
    python scripts/batch_fix_meta.py --provider kinsta                 # one host
    python scripts/batch_fix_meta.py --only a,b --skip c               # subset
    python scripts/batch_fix_meta.py --max-pages 20 --no-draft         # cheaper: fewer page-text pulls (~50 Ahrefs units each), no model drafts
    python scripts/batch_fix_meta.py --fix                             # staging dry run of the approved sheet rows on every site
    python scripts/batch_fix_meta.py --fix --apply                     # staging apply
    python scripts/batch_fix_meta.py --fix --apply --target live --yes # live, unattended; rows become "applied <date>"

Review mode never writes to a site. Per site: probe -> reports/<slug>/meta-<crawl>.md, then the `meta` tab on the client's
review sheet (sites with no review.alt_sheet_id get the report only and are listed). Fix mode runs scripts/fix_meta.py --fix per
site with the flags given; a site with no approved rows, no staging/live alias, or a non-Yoast SEO plugin is reported, not failed.
Summary table: changes/<provider or _all>/_batch-<stamp>-fix-meta-<review|fix-<target>-<dry|apply>>.md
"""
import argparse, datetime, os, re, subprocess, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from build_redirect_map import load_env  # noqa: E402

def clients_for(provider, only, skip):
    out = []
    for p in sorted((ROOT / "clients").glob("*.yaml")):
        if p.name.startswith("_"): continue
        c = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        slug = c.get("slug", p.stem)
        if provider and str((c.get("hosting") or {}).get("provider", "")).lower() != provider: continue
        if only and slug not in only: continue
        if slug in skip: continue
        if str((c.get("platform") or {}).get("cms", "")).lower() not in ("wordpress", "unknown", ""): continue
        pid = (c.get("ahrefs") or {}).get("site_audit_project_id")
        if not pid or str(pid) in ("0", "unknown"): continue
        out.append((slug, c))
    return out

def run(args):
    # PYTHONUTF8: the child prints "→" and "·"; piped stdout on Windows would otherwise be cp1252 and the child would crash.
    r = subprocess.run([sys.executable, str(HERE / "fix_meta.py"), *args], capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env={**os.environ, "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"})
    return r.returncode, (r.stdout or "") + (r.stderr or "")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", help="kinsta | wpengine | other; default every client")
    ap.add_argument("--only"); ap.add_argument("--skip", default="")
    ap.add_argument("--max-pages", type=int, default=40, dest="max_pages")
    ap.add_argument("--no-draft", action="store_true", dest="no_draft", help="review mode: skip model drafts even if ANTHROPIC_API_KEY is set")
    ap.add_argument("--no-sheet", action="store_true", dest="no_sheet", help="review mode: reports only")
    ap.add_argument("--cache", action="store_true")
    ap.add_argument("--fix", action="store_true"); ap.add_argument("--apply", action="store_true")
    ap.add_argument("--target", choices=["staging", "live"], default="staging"); ap.add_argument("--yes", action="store_true")
    a = ap.parse_args()
    load_env()
    only = set(a.only.split(",")) if a.only else None; skip = {x for x in a.skip.split(",") if x}
    sites = clients_for(a.provider, only, skip)
    if not sites: sys.exit("no matching client files")
    draft = (not a.no_draft) and bool(os.environ.get("ANTHROPIC_API_KEY")) and not a.fix
    if not a.fix and not a.no_draft and not draft: print("Note: ANTHROPIC_API_KEY not set; only bio pages get drafts (template). Others land on the sheet as 'needs draft'.")
    if a.fix and a.apply and a.target == "live" and not a.yes: sys.exit("batch live apply needs --yes (the per-site prompt would stop the batch)")
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    mode = f"fix-{a.target}-{'apply' if a.apply else 'dry'}" if a.fix else "review"
    print(f"fix-meta {mode} on {len(sites)} site(s)" + (f" ({a.provider})" if a.provider else "") + (" with model drafts" if draft else ""))
    rows = []
    for slug, c in sites:
        if a.fix:
            args = [slug, "--fix", "--target", a.target] + (["--apply"] if a.apply else []) + (["--yes"] if a.yes else [])
            code, out = run(args)
            last = (out.strip().splitlines() or [""])[-1]
            res = "ok" if code == 0 else "error"
            detail = re.sub(r"^\S+: ", "", last)[:220]
        else:
            args = [slug, "--probe", "--max-pages", str(a.max_pages)] + (["--draft"] if draft else []) + (["--cache"] if a.cache else [])
            code, out = run(args)
            if code != 0:
                res, detail = "error", (out.strip().splitlines() or [""])[-1][:220]
            else:
                m = re.search(r"(\d+) flagged URLs → (\d+) to write, (\d+) no action(.*)", out)
                m2 = re.search(r"titles proposed (\d+) · descriptions proposed (\d+) · needs draft (\d+)", out)
                detail = (f"{m[1]} flagged → {m[2]} to write, {m[3]} no action{m[4].strip()}" if m else "?") + (f" · titles {m2[1]}, descriptions {m2[2]}, needs draft {m2[3]}" if m2 else "")
                sid = ((c.get("review") or {}).get("alt_sheet_id") or "").strip()
                if a.no_sheet: res = "report only"
                elif not sid or sid == "unknown": res = "no sheet"; detail += " · no review sheet (report only)"
                else:
                    code2, out2 = run([slug, "--sheet"])
                    s = re.search(r"sheet: (.*?) \(from", out2)
                    res = "ok" if code2 == 0 else "sheet error"
                    detail += " · " + (s[1] if s else (out2.strip().splitlines() or [""])[-1][:160])
        rows.append((slug, res, detail)); print(f"  {slug:26} {res:12} {detail}")
    outdir = ROOT / "changes" / (a.provider or "_all"); outdir.mkdir(parents=True, exist_ok=True)
    p = outdir / f"_batch-{stamp}-fix-meta-{mode}.md"
    p.write_text("\n".join([f"# Batch fix-meta {mode}" + (f" on {a.provider}" if a.provider else " (all clients)"), "", f"Run {stamp} · {len(sites)} site(s)" + (" · model drafts on" if draft else ""), "",
                            "| Site | Result | Detail |", "|---|---|---|"] + [f"| {s} | {r} | {d} |" for s, r, d in rows]) + "\n", encoding="utf-8")
    print(f"Summary: {p}")

if __name__ == "__main__":
    main()
