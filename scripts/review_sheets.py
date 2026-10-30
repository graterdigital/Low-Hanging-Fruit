#!/usr/bin/env python3
"""One persistent Google Sheet per client for APPROVE-tier review (alt text now; other skills can add tabs later).

    python scripts/review_sheets.py setup <slug> [--share overwatch@graterdigital.com]   # create the workbook, record its id in clients/<slug>.yaml
    python scripts/review_sheets.py push <slug>            # append new images from the newest alt CSV to the "alt text" tab (existing rows untouched)
    python scripts/review_sheets.py pull <slug>            # read decisions back: merge new_alt into the repo CSV, mark rows "merged"
    python scripts/review_sheets.py mark-applied <slug>    # after --alt-apply: stamp merged rows "applied <date>"
    python scripts/review_sheets.py status                 # one line per client: sheet id, pending / merged / applied counts

Credentials: a Google service account. Put the JSON key at the path in GOOGLE_SERVICE_ACCOUNT (environment or .env at the
repo root; default secrets/google-service-account.json, git-ignored). Share each sheet with the service account's
client_email, or let `setup` create the sheet as the service account and share it with the humans in --share.
Needs: pip install gspread google-auth

Tab "alt text" columns: image_key | tier | uses | on_pages | example_page | image | current_alt | suggestion | new_alt | status | note | added
status: pending (needs a human) -> merged (pulled into the repo CSV) -> applied <date>; "skip" (or a blank new_alt at pull time) leaves the image alone.
A human only edits new_alt (and note). Everything else is written by the scripts.
"""
import argparse, csv, datetime, os, re, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_redirect_map import load_env
TAB = "alt text"
COLS = ["image_key", "tier", "uses", "on_pages", "example_page", "image", "current_alt", "suggestion", "new_alt", "status", "note", "added"]

def client_path(slug): return ROOT / "clients" / f"{slug}.yaml"
def load_client(slug): return yaml.safe_load(client_path(slug).read_text(encoding="utf-8"))

def gc():
    load_env()
    key = os.environ.get("GOOGLE_SERVICE_ACCOUNT", str(ROOT / "secrets" / "google-service-account.json"))
    if not Path(key).exists(): sys.exit(f"service account key not found at {key}; see docs/setup-machine.md (Google service account)")
    try:
        import gspread
    except ImportError:
        sys.exit("pip install gspread google-auth")
    return gspread.service_account(filename=key)

def set_sheet_id(slug, sheet_id, title):
    """Write review.alt_sheet_id into the client file without disturbing its comments: text edit, not a YAML dump."""
    p = client_path(slug); s = p.read_text(encoding="utf-8")
    line = f"  alt_sheet_id: {sheet_id}   # \"{title}\" in Google Sheets; scripts/review_sheets.py"
    if re.search(r"^review:\s*$", s, re.M):
        if re.search(r"^\s+alt_sheet_id:", s, re.M): s = re.sub(r"^\s+alt_sheet_id:.*$", line, s, count=1, flags=re.M)
        else: s = re.sub(r"^(review:\s*\n)", r"\1" + line + "\n", s, count=1, flags=re.M)
    else:
        s = s.rstrip("\n") + "\n\nreview:\n" + line + "\n"
    p.write_text(s, encoding="utf-8")

def sheet_for(slug, client=None):
    c = client or load_client(slug)
    sid = ((c.get("review") or {}).get("alt_sheet_id") or "").strip()
    if not sid or sid == "unknown": sys.exit(f"clients/{slug}.yaml has no review.alt_sheet_id; run: python scripts/review_sheets.py setup {slug}")
    return sid

LEGACY = ["image_key", "tier", "uses", "on_pages", "example_page", "image", "current_alt", "suggestion", "new_alt", "note"]   # sheets made by hand on 2026-10-30

def open_tab(client_gs, sheet_id):
    sh = client_gs.open_by_key(sheet_id)
    try:
        ws = sh.worksheet(TAB)
    except Exception:
        first = sh.sheet1
        if first.row_values(1) in (LEGACY, COLS):   # a hand-made sheet: adopt its first tab
            first.update_title(TAB); ws = first
        else:
            ws = sh.add_worksheet(TAB, rows=200, cols=len(COLS)); ws.append_row(COLS); ws.freeze(rows=1)
    head = ws.row_values(1)
    if not head: ws.append_row(COLS); ws.freeze(rows=1)
    elif head == LEGACY:   # upgrade in place: insert status before note, add 'added'
        vals = ws.get_all_values()
        new = [COLS] + [r[:9] + [("merged" if (r[8] if len(r) > 8 else "").strip() else "pending"), (r[9] if len(r) > 9 else ""), "2026-10-30"] for r in vals[1:] if any(r)]
        ws.clear(); ws.update("A1", new, value_input_option="RAW"); ws.freeze(rows=1)
        print(f"  upgraded '{TAB}' tab to the current columns ({len(new) - 1} rows)")
    elif head != COLS:
        sys.exit(f"'{TAB}' tab has unexpected columns {head}; expected {COLS}")
    return sh, ws

def read_rows(ws):
    vals = ws.get_all_values()
    return [dict(zip(COLS, r + [""] * (len(COLS) - len(r)))) for r in vals[1:] if any(r)]

def newest_alt_csv(slug, provider):
    files = sorted((ROOT / "changes" / provider / slug).glob("*-fix-images-alt.csv"))
    if not files: sys.exit(f"no alt CSV for {slug}; run: python scripts/fix_images.py {slug} --alt-csv")
    return files[-1]

def review_rows_from_csv(path, domain):
    """Collapse the per-occurrence repo CSV to one row per image_key, as alt_csv's review sheet does."""
    rows = list(csv.DictReader(path.open(encoding="utf-8-sig")))
    order = {"A": 0, "C": 1, "B": 2, "D": 3}
    groups = {}
    for r in rows:
        if r.get("tier") == "D": continue
        k = r.get("image_key") or r["src"]
        g = groups.setdefault(k, {"image_key": k, "tier": r["tier"], "uses": 0, "pages": set(), "example_page": r["page_url"], "image": r["src"].rsplit("/", 1)[-1],
                                  "current_alt": r.get("current_alt", ""), "suggestion": r.get("suggestion", ""), "new_alt": r.get("new_alt", ""), "note": r.get("note", "")})
        g["uses"] += 1; g["pages"].add(r["page_url"])
        if order.get(r["tier"], 9) < order.get(g["tier"], 9): g["tier"] = r["tier"]
    out = []
    for g in groups.values():
        g["on_pages"] = len(g.pop("pages")); g["example_page"] = re.sub(r"^https?://[^/]+", domain, g["example_page"])
        out.append(g)
    out.sort(key=lambda g: (order.get(g["tier"], 9), -g["uses"], g["example_page"]))
    return out, rows

def cmd_setup(a):
    c = load_client(a.slug); g = gc()
    existing = (c.get("review") or {}).get("alt_sheet_id")
    title = f"{a.slug} review"
    if existing and existing != "unknown":
        sh = g.open_by_key(existing); print(f"{a.slug}: sheet already recorded ({existing}): {sh.url}")
    else:
        sh = g.create(title)
        set_sheet_id(a.slug, sh.id, title)
        print(f"{a.slug}: created {sh.url} and recorded review.alt_sheet_id in clients/{a.slug}.yaml")
    sh, ws = open_tab(g, sh.id)
    for who in (a.share or []):
        sh.share(who, perm_type="user", role="writer", notify=False); print(f"  shared with {who}")
    try:
        default = sh.sheet1
        if default.title != TAB and default.title.startswith("Sheet") and not default.get_all_values(): sh.del_worksheet(default)
    except Exception: pass

def cmd_push(a):
    c = load_client(a.slug); provider = str((c.get("hosting") or {}).get("provider") or "other").lower()
    domain = c.get("canonical_host") or f"https://{c['domain']}"
    sid = sheet_for(a.slug, c); g = gc(); sh, ws = open_tab(g, sid)
    have = {r["image_key"] for r in read_rows(ws)}
    path = newest_alt_csv(a.slug, provider)
    review, _ = review_rows_from_csv(path, domain)
    today = datetime.date.today().isoformat()
    new = [[r["image_key"], r["tier"], r["uses"], r["on_pages"], r["example_page"], r["image"], r["current_alt"], r["suggestion"], r["new_alt"],
            "merged" if r["new_alt"] else "pending", r["note"], today] for r in review if r["image_key"] not in have]
    if new: ws.append_rows(new, value_input_option="RAW")
    print(f"{a.slug}: {len(new)} new images appended ({len(review) - len(new)} already on the sheet) from {path.name}: {sh.url}")

def cmd_pull(a):
    c = load_client(a.slug); provider = str((c.get("hosting") or {}).get("provider") or "other").lower()
    sid = sheet_for(a.slug, c); g = gc(); sh, ws = open_tab(g, sid)
    sheet_rows = read_rows(ws)
    decided = {r["image_key"]: r for r in sheet_rows if r["status"] in ("pending", "merged") and r["new_alt"].strip() and r["new_alt"].strip().lower() != "skip"}
    path = newest_alt_csv(a.slug, provider)
    rows = list(csv.DictReader(path.open(encoding="utf-8-sig")))
    changed = 0
    for r in rows:
        if r.get("tier") == "D": continue
        d = decided.get(r.get("image_key") or r["src"])
        if d and d["new_alt"].strip() != (r.get("new_alt") or "").strip():
            r["new_alt"] = d["new_alt"].strip(); changed += 1
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    # mark merged on the sheet
    status_col = COLS.index("status") + 1
    updates = [{"range": f"{chr(64 + status_col)}{i + 2}", "values": [["merged"]]} for i, r in enumerate(sheet_rows) if r["image_key"] in decided and r["status"] == "pending"]
    if updates: ws.batch_update(updates, value_input_option="RAW")
    will = len([r for r in rows if r.get("tier") != "D" and (r.get("new_alt") or "").strip()])
    print(f"{a.slug}: {len(decided)} decided images on the sheet, {changed} occurrences updated in {path.name}, {will} occurrences will apply; {len(updates)} rows marked merged")
    print(f"  next: python scripts/fix_images.py {a.slug} --alt-apply {path.relative_to(ROOT)}   (dry) then --apply, then --target live --apply, then review_sheets.py mark-applied {a.slug}")

def cmd_mark(a):
    sid = sheet_for(a.slug); g = gc(); sh, ws = open_tab(g, sid)
    sheet_rows = read_rows(ws); status_col = COLS.index("status") + 1; today = datetime.date.today().isoformat()
    updates = [{"range": f"{chr(64 + status_col)}{i + 2}", "values": [[f"applied {today}"]]} for i, r in enumerate(sheet_rows) if r["status"] == "merged"]
    if updates: ws.batch_update(updates, value_input_option="RAW")
    print(f"{a.slug}: {len(updates)} rows marked applied {today}")

def cmd_status(a):
    g = gc()
    for p in sorted((ROOT / "clients").glob("*.yaml")):
        if p.name.startswith("_"): continue
        c = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        sid = (c.get("review") or {}).get("alt_sheet_id")
        if not sid or sid == "unknown": print(f"{p.stem:26} no sheet"); continue
        try:
            sh, ws = open_tab(g, sid); rows = read_rows(ws)
            pend = sum(1 for r in rows if r["status"] == "pending"); merged = sum(1 for r in rows if r["status"] == "merged"); done = sum(1 for r in rows if r["status"].startswith("applied"))
            print(f"{p.stem:26} {len(rows):4} rows  pending {pend:4}  merged {merged:4}  applied {done:4}  {sh.url}")
        except Exception as e:
            print(f"{p.stem:26} ERROR {str(e)[:80]}")

def main():
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("setup"); s.add_argument("slug"); s.add_argument("--share", action="append", help="email to share with (repeatable)"); s.set_defaults(f=cmd_setup)
    s = sub.add_parser("push"); s.add_argument("slug"); s.set_defaults(f=cmd_push)
    s = sub.add_parser("pull"); s.add_argument("slug"); s.set_defaults(f=cmd_pull)
    s = sub.add_parser("mark-applied"); s.add_argument("slug"); s.set_defaults(f=cmd_mark)
    s = sub.add_parser("status"); s.set_defaults(f=cmd_status)
    a = ap.parse_args(); a.f(a)

if __name__ == "__main__":
    main()
