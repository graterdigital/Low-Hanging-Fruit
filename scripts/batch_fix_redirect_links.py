#!/usr/bin/env python3
"""Run fix-redirect-links across every client on one host, with gates between the steps.

    python scripts/batch_fix_redirect_links.py --provider kinsta                 # stage-only: map -> staging dry -> staging apply
    python scripts/batch_fix_redirect_links.py --provider kinsta --live          # ...then live dry -> live apply for sites that passed
    python scripts/batch_fix_redirect_links.py --provider kinsta --only a,b,c    # subset of slugs
    python scripts/batch_fix_redirect_links.py --provider kinsta --skip x,y      # leave some out
    python scripts/batch_fix_redirect_links.py --provider kinsta --live --no-stage   # live only, for sites whose staging already passed

Per site, in order, stopping that site (never the batch) at the first gate it fails:
  1. build the redirect map from Ahrefs (build_redirect_map.py); 0 swaps -> nothing to do, reported, next site
  2. dry run on staging; every swap must hit something in posts/meta/options, else "unmatched swaps" is reported (not a stop)
  3. apply on staging; any post save error or failed cache flush -> stop
  4. (--live) dry run on live; posts/meta counts must be within --tolerance of the staging dry run (default 25%), else stop:
     a big gap means staging is stale or live changed, and a human should look
  5. (--live) apply on live (--yes is implied: this script IS the confirmation step), same error checks
A summary of every site lands in changes/<provider>/_batch-<stamp>.md. Sites with no staging alias run live only when
--allow-no-staging is given; otherwise they are listed as "needs staging".
"""
import argparse, datetime, json, subprocess, sys, traceback
from pathlib import Path
import importlib.util

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
spec = importlib.util.spec_from_file_location("frl", HERE / "fix_redirect_links.py"); frl = importlib.util.module_from_spec(spec); spec.loader.exec_module(frl)

class Args:  # minimal stand-in for the argparse namespace fix_redirect_links.run() expects
    def __init__(self, slug, target, apply=False, probe=False, map=None, checkjson=False):
        self.slug, self.target, self.apply, self.probe, self.map, self.checkjson = slug, target, apply, probe, map, checkjson
        self.webroot, self.yes = "public", True

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

def counts(res): return (len(res["posts"]), len(res["meta"]), sum(res["totals"].values()))

def within(a, b, tol):
    hi = max(a, b)
    return hi == 0 or abs(a - b) / hi <= tol

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", required=True, help="kinsta | wpengine | other (matches hosting.provider in client files)")
    ap.add_argument("--only", default="", help="comma-separated slugs")
    ap.add_argument("--skip", default="", help="comma-separated slugs")
    ap.add_argument("--live", action="store_true", help="after staging passes, dry-run and apply on live")
    ap.add_argument("--no-stage", action="store_true", help="skip the staging steps (use with --live when staging already passed)")
    ap.add_argument("--no-map", action="store_true", help="reuse the newest existing map instead of rebuilding from Ahrefs")
    ap.add_argument("--allow-no-staging", action="store_true", help="let sites without a staging alias go straight to live")
    ap.add_argument("--tolerance", type=float, default=0.25, help="allowed relative gap between staging and live dry-run counts")
    a = ap.parse_args()
    only = {s.strip() for s in a.only.split(",") if s.strip()}; skip = {s.strip() for s in a.skip.split(",") if s.strip()}

    sites = clients_for(a.provider, only, skip)
    if not sites: sys.exit(f"No client files with hosting.provider = {a.provider}" + (f" matching {sorted(only)}" if only else ""))
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    print(f"Batch fix-redirect-links on {a.provider}: {len(sites)} site(s){' + LIVE' if a.live else ' (stage only)'}\n")

    summary = []
    for slug, c in sites:
        h = c.get("hosting") or {}
        row = {"slug": slug, "status": "", "swaps": 0, "staging": "-", "live": "-", "notes": [], "logs": []}
        summary.append(row)
        print(f"=== {slug}")
        try:
            if not a.no_map:
                r = subprocess.run([sys.executable, str(HERE / "build_redirect_map.py"), slug], capture_output=True, text=True)
                print(r.stdout.strip())
                if r.returncode != 0:
                    row["status"] = "map failed"; row["notes"].append(r.stderr.strip()[-300:] or r.stdout.strip()[-300:]); continue
            mp = frl.latest_map(slug)
            if not mp: row["status"] = "no map"; continue
            m = json.loads(mp.read_text(encoding="utf-8")); row["swaps"] = len(m["swaps"])
            row["notes"].append(f"map {mp.name}: {len(m['swaps'])} swaps, {len(m.get('skipped', []))} skipped")
            if not m["swaps"]:
                row["status"] = "nothing to do"; continue

            staging_alias = str(h.get("staging_environment") or "").split(",")[0].strip()
            has_staging = staging_alias and staging_alias not in ("unknown", "none", "None")
            stage_counts = None

            if not a.no_stage:
                if not has_staging:
                    if not a.allow_no_staging: row["status"] = "needs staging"; continue
                    row["notes"].append("no staging alias; --allow-no-staging given")
                else:
                    dry = frl.run(Args(slug, "staging", map=str(mp))); row["logs"].append(dry["log"])
                    stage_counts = counts(dry)
                    unmatched = [s["old"] for s in m["swaps"] if s["old"] not in dry["totals"]]
                    if unmatched: row["notes"].append(f"{len(unmatched)} swap(s) had no hits on staging (theme/builder/already fixed): " + ", ".join(unmatched[:3]) + (" ..." if len(unmatched) > 3 else ""))
                    if dry.get("options"): row["notes"].append(f"{len(dry['options'])} wp_options row(s) still reference old URLs; see the -options.md log")
                    if dry.get("refused_n"): row["notes"].append(f"{dry['refused_n']} swap(s) refused for unsafe characters (see log)")
                    if dry.get("guarded"):
                        row["status"] = "json guard tripped"; row["notes"].append(f"{dry['guarded']} meta row(s) would break JSON; nothing applied, see log"); continue
                    if stage_counts[2] == 0:
                        row["staging"] = "0 hits"; row["notes"].append("staging dry run found nothing: staging already fixed, or links live outside post content")
                    else:
                        app = frl.run(Args(slug, "staging", apply=True, map=str(mp))); row["logs"].append(app["log"])
                        row["staging"] = f"{counts(app)[0]}p/{counts(app)[1]}m/{counts(app)[2]}r"
                        if app["errors"] or app.get("flushed") is False:
                            row["status"] = "staging apply errors"; row["notes"].append(f"{app['errors']} save errors, flush={app.get('flushed')}"); continue
                        if str((c.get("platform") or {}).get("page_builder", "")).lower() == "elementor":
                            cj = frl.run(Args(slug, "staging", map=str(mp), checkjson=True))
                            if cj["errors"]:
                                row["status"] = "elementor json invalid"; row["notes"].append(f"{cj['errors']} _elementor_data row(s) invalid on staging after apply; restore and investigate"); continue
                            row["notes"].append(f"elementor json ok ({cj['checked']} rows)")
            if not a.live:
                row["status"] = "staged" if row["staging"] != "-" else "map built"; continue

            ldry = frl.run(Args(slug, "live", map=str(mp))); row["logs"].append(ldry["log"])
            lc = counts(ldry)
            if lc[2] == 0:
                row["live"] = "0 hits"; row["status"] = "live already clean"; continue
            if ldry.get("guarded"):
                row["status"] = "json guard tripped (live)"; row["notes"].append(f"{ldry['guarded']} meta row(s) would break JSON on live; nothing applied"); continue
            if stage_counts and not (within(stage_counts[0], lc[0], a.tolerance) and within(stage_counts[1], lc[1], a.tolerance)):
                row["status"] = "live/staging mismatch"; row["notes"].append(f"staging dry {stage_counts[0]}p/{stage_counts[1]}m vs live dry {lc[0]}p/{lc[1]}m; staging may be stale"); continue
            lapp = frl.run(Args(slug, "live", apply=True, map=str(mp))); row["logs"].append(lapp["log"])
            row["live"] = f"{counts(lapp)[0]}p/{counts(lapp)[1]}m/{counts(lapp)[2]}r"
            if lapp["errors"] or lapp.get("flushed") is False:
                row["status"] = "live apply errors"; row["notes"].append(f"{lapp['errors']} save errors, flush={lapp.get('flushed')}"); continue
            row["status"] = "live applied"
        except SystemExit as e:
            row["status"] = "stopped"; row["notes"].append(str(e)[:300])
        except Exception as e:
            row["status"] = "crashed"; row["notes"].append(f"{type(e).__name__}: {e}"); traceback.print_exc()
        finally:
            print(f"    -> {row['status']}\n")

    outdir = ROOT / "changes" / a.provider; outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / f"_batch-{stamp}-fix-redirect-links{'-live' if a.live else '-stage'}.md"
    lines = [f"# Batch fix-redirect-links: {a.provider} ({'live' if a.live else 'stage only'})", "", f"Run {stamp} · {len(sites)} site(s) · tolerance {a.tolerance:.0%}", "",
             "| site | status | swaps | staging p/m/r | live p/m/r | notes |", "|---|---|---|---|---|---|"]
    for r in summary:
        lines.append(f"| {r['slug']} | **{r['status']}** | {r['swaps']} | {r['staging']} | {r['live']} | {'<br>'.join(n.replace('|', '/') for n in r['notes'])} |")
    lines += ["", "## Logs", ""] + [f"- {r['slug']}: " + ", ".join(f"`{Path(l).relative_to(ROOT)}`" for l in r["logs"]) for r in summary if r["logs"]]
    lines += ["", "p/m/r = posts changed / postmeta rows changed / link replacements. Sites that stopped at a gate did not go further; their logs say why."]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"{'site':24} {'status':24} {'swaps':>5}  {'staging':>14}  {'live':>14}")
    for r in summary: print(f"{r['slug']:24} {r['status']:24} {r['swaps']:>5}  {r['staging']:>14}  {r['live']:>14}")
    print(f"\nSummary: {out}")

if __name__ == "__main__":
    main()
