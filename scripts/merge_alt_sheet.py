#!/usr/bin/env python3
"""Merge a reviewed alt-text sheet (exported from Google Sheets / Excel as CSV) back into the repo's alt CSV.

    python scripts/merge_alt_sheet.py changes/<provider>/<slug>/<stamp>-fix-images-alt.csv <exported-review.csv>

The export is either the per-image review sheet (one row per `image_key`, fanned out to every occurrence of that image in
the repo CSV) or an older per-row sheet (matched by `id`). Only `new_alt` (and `note`, if present) are taken from the
export; every other column keeps the repo value. Prints what changed. Occurrences the export does not cover are left as they were.
"""
import csv, sys
from pathlib import Path

def main():
    if len(sys.argv) != 3: sys.exit(__doc__)
    repo, export = Path(sys.argv[1]), Path(sys.argv[2])
    rows = list(csv.DictReader(repo.open(encoding="utf-8-sig")))
    exp = list(csv.DictReader(export.open(encoding="utf-8-sig")))
    by_key = {r["image_key"].strip(): r for r in exp if r.get("image_key")}
    by_id = {r["id"].strip(): r for r in exp if r.get("id")}
    print(f"export: {len(exp)} rows, keyed by {'image_key' if by_key else 'id'}")
    changed = cleared = 0
    for r in rows:
        if r.get("tier") == "D": continue
        e = by_key.get(r.get("image_key", "")) if by_key else by_id.get(r["id"])
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
