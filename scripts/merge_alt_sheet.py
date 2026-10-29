#!/usr/bin/env python3
"""Merge a reviewed alt-text sheet (exported from Google Sheets / Excel as CSV) back into the repo's alt CSV.

    python scripts/merge_alt_sheet.py changes/<provider>/<slug>/<stamp>-fix-images-alt.csv <exported-review.csv>

Rows are matched by `id`. Only `new_alt` (and `note`, if present) are taken from the review export; every other
column keeps the repo value, so a slimmed-down review sheet (fewer columns, Tier D rows left out) merges cleanly.
Prints what changed. Rows in the repo CSV that the export lacks are left as they were.
"""
import csv, sys
from pathlib import Path

def main():
    if len(sys.argv) != 3: sys.exit(__doc__)
    repo, export = Path(sys.argv[1]), Path(sys.argv[2])
    rows = list(csv.DictReader(repo.open(encoding="utf-8-sig")))
    rev = {r["id"].strip(): r for r in csv.DictReader(export.open(encoding="utf-8-sig")) if r.get("id")}
    changed = cleared = 0
    for r in rows:
        e = rev.get(r["id"])
        if e is None: continue
        new = (e.get("new_alt") or "").strip()
        if new != (r["new_alt"] or "").strip():
            print(f"{r['id']:5} {'cleared' if not new else 'changed'}: {r['new_alt'][:60]!r} -> {new[:60]!r}")
            r["new_alt"] = new; changed += 1; cleared += (not new)
        if e.get("note") and e["note"].strip() != (r.get("note") or "").strip():
            r["note"] = e["note"].strip()
    with repo.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(f"\n{changed} rows updated ({cleared} cleared), {len([r for r in rows if r['new_alt'].strip() and r['tier'] != 'D'])} rows will apply. Written to {repo}")

if __name__ == "__main__":
    main()
