#!/usr/bin/env python3
"""fix-meta: SEO titles and meta descriptions through the SEO plugin, every piece of text reviewed by a human first.

    python scripts/fix_meta.py <slug> --probe                  # queue + drafts -> reports/<slug>/meta-<crawl>.md (+ .json); nothing else is written
    python scripts/fix_meta.py <slug> --probe --draft          # same, plus model-drafted titles/descriptions (ANTHROPIC_API_KEY in .env)
    python scripts/fix_meta.py <slug> --sheet                  # push the queue to the "meta" tab of the client's review sheet (upsert by URL)
       (a human fills new_title / new_description and sets status to "approved")
    python scripts/fix_meta.py <slug> --fix                    # dry run of the approved rows on staging
    python scripts/fix_meta.py <slug> --fix --apply            # write them on staging
    python scripts/fix_meta.py <slug> --fix --apply --target live [--yes]   # live; type the slug to confirm; rows become "applied <date>"
    python scripts/fix_meta.py <slug> --rollback changes/<provider>/<slug>/backup/<stamp>-fix-meta-<target>.json [--apply]

APPROVE tier, always: searchers read this text. The skill never truncates to a character count and never writes anything a
human has not typed or approved in the sheet. Yoast only in v1 (postmeta _yoast_wpseo_title / _yoast_wpseo_metadesc via
scripts/php/set_meta.php over SSH + wp eval-file); AIOSEO sites are reported as "manual in AIOSEO".

Queue order is GSC impressions x (1 - CTR) when the Ahrefs project has GSC connected (ahrefs.gsc_connected: yes), else
Ahrefs traffic, then page type. Drafts come from, in order: reports/<slug>/meta-drafts.json (hand-written, keyed by path),
--draft (one model call per page with the page text and the top GSC query), or the bio template when the page is a person.
Every draft carries a `basis` so the reviewer knows what to look hardest at.

`--cache` keeps the raw Ahrefs responses in tmp/ahrefs-cache/<slug>/ and reuses them (same as ai_discoverability.py).
Needs AHREFS_API_KEY in .env at the repo root; the sheet needs the Google service account (docs/setup-machine.md).
"""
import argparse, datetime, json, os, re, subprocess, sys, urllib.error, urllib.parse, urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from build_redirect_map import load_env, ahrefs, UA, wpengine_webroot  # noqa: E402

SKIP_PLUGINS = "handl-utm-grabber-v3"
SKILL = "fix-meta"
# Ahrefs issue names this skill reads (indexable variants only; the names are stable across projects, the ids are not guaranteed).
ISSUE_NAMES = {
    "Meta description tag missing or empty": "description missing",
    "Page and SERP titles do not match":     "serp mismatch",
    "Title tag missing or empty":            "title missing",
    "Multiple title tags":                   "multiple titles",
    "Multiple meta description tags":        "multiple descriptions",
    "Duplicate titles":                      "duplicate title",
    "Duplicate meta descriptions":           "duplicate description",
}
PAGE_SELECT = ("url,title,serp_title,is_page_title_used_in_serp,meta_description,h1,traffic,ml_page_types,"
               "duplicate_title_canonical_hreflang,duplicate_description_canonical_hreflang,page_is_noindex,http_code")
ARCHIVE_RE = re.compile(r"/(category|tag|author)/|/page/\d+/?$|/\d{4}/\d{2}(/\d{2})?/?$|/feed/?$")
SEP_RE = re.compile(r"\s+(?:-|\||–|—|:|•|·)\s+")
SHEET_TAB = "meta"
SHEET_COLS = ["url", "page_type", "impressions", "ctr", "position", "top_query", "current_title", "serp_title", "proposed_title",
              "new_title", "current_description", "proposed_description", "new_description", "basis", "status", "note", "updated"]
HUMAN_COLS = {"new_title", "new_description", "status", "note"}
MAIN_STOP = re.compile(r"^#{2,6}\s*(reviews?|testimonials?|what our clients say|let'?s get started|get started|contact us|useful links|related|share|recent posts|categories)\b", re.I)

def log(*a): print(*a, file=sys.stderr)
def urlpath(u):
    p = urllib.parse.urlsplit(u); return (p.path or "/") + (("?" + p.query) if p.query else "")
def norm(u):
    """Join key for GSC vs Site Audit URLs: scheme/host-insensitive, trailing-slash-insensitive, lower-cased host."""
    p = urllib.parse.urlsplit(u.strip()); host = re.sub(r"^www\.", "", p.netloc.lower())
    return host + (p.path.rstrip("/") or "/")
def first(v):
    if isinstance(v, list): return (v[0] if v else "") or ""
    return v or ""
def pct(v):
    """GSC `ctr` from the Ahrefs API is a percentage (1.75 = 1.75 %), not a fraction."""
    return float(v or 0)

# ---------- Ahrefs with optional cache ----------
class Api:
    def __init__(self, slug, cache):
        self.dir = ROOT / "tmp" / "ahrefs-cache" / slug if cache else None
        if self.dir: self.dir.mkdir(parents=True, exist_ok=True)
    def get(self, name, path, **params):
        f = self.dir / f"{name}.json" if self.dir else None
        if f and f.exists(): return json.loads(f.read_text(encoding="utf-8"))
        data = ahrefs(path, **params)
        if f: f.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        return data

def pull(client, api):
    pid = client["ahrefs"]["site_audit_project_id"]
    proj = api.get("project", "site-audit/projects", project_id=pid)
    hs = (proj.get("healthscores") or [{}])[0]
    crawl = (hs.get("date") or "")[:10] or datetime.date.today().isoformat()
    issues = api.get("issues", "site-audit/issues", project_id=pid).get("issues", [])
    found = {}
    for i in issues:
        if i["name"] in ISSUE_NAMES and i.get("is_indexable") is not False:
            found[i["name"]] = i
    pages = {}   # url -> row with "reasons"
    for name, i in found.items():
        if not (i.get("crawled") or 0): continue
        key = "issue-" + re.sub(r"\W+", "-", name).lower()
        rows = api.get(key, "site-audit/page-explorer", project_id=pid, issue_id=i["issue_id"], select=PAGE_SELECT,
                       order_by="traffic:desc", limit=500).get("pages", [])
        for r in rows:
            p = pages.setdefault(r["url"], dict(r, reasons=[]))
            p["reasons"].append(ISSUE_NAMES[name])
    # A broader title sample to learn the site's brand suffix (the issue rows alone can be mostly archives).
    sample = api.get("title-sample", "site-audit/page-explorer", project_id=pid, select="url,title,h1,traffic",
                     order_by="traffic:desc", limit=100,
                     where=json.dumps({"and": [{"field": "http_code", "is": ["eq", 200]}, {"field": "is_html", "is": ["eq", True]},
                                                {"field": "page_is_noindex", "is": ["eq", False]}]})).get("pages", [])
    gsc = {}
    if str((client.get("ahrefs") or {}).get("gsc_connected", "")).lower() in ("yes", "true"):
        d_to = datetime.date.today() - datetime.timedelta(days=1); d_from = d_to - datetime.timedelta(days=90)
        try:
            for g in api.get("gsc-pages", "gsc/pages", project_id=pid, date_from=d_from.isoformat(), date_to=d_to.isoformat(), limit=5000).get("pages", []):
                gsc[norm(g["page"])] = g
        except SystemExit as e:
            log(f"GSC not available ({str(e)[:100]}); queue falls back to Ahrefs traffic")
    return {"pid": pid, "crawl": crawl, "health": hs.get("health_score"), "found": found, "pages": pages, "sample": sample, "gsc": gsc,
            "gsc_window": f"{d_from} to {d_to}" if gsc else ""}

# ---------- brand suffix ----------
def detect_brand(titles):
    """Most common tail after the last separator across the site's titles, with its separator. ('Hastings Shadmehry', ' - ')."""
    counts = {}
    for t in titles:
        m = list(SEP_RE.finditer(t))
        if not m: continue
        tail = t[m[-1].end():].strip(); sep = m[-1].group(0)
        if 2 <= len(tail) <= 40: counts[(tail, sep)] = counts.get((tail, sep), 0) + 1
    if not counts: return "", " - "
    (tail, sep), n = max(counts.items(), key=lambda kv: kv[1])
    return (tail, sep) if n >= 3 else ("", " - ")

def without_brand(title, brand):
    t = title.strip()
    if brand and t.lower().endswith(brand.lower()):
        t = t[: -len(brand)].rstrip()
        t = re.sub(r"\s*(?:-|\||–|—|:|•|·)\s*$", "", t)
    return t.strip()

def lev(a, b):
    a, b = a.lower(), b.lower()
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1): cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]

# ---------- classification ----------
def page_kind(row):
    ml = str(row.get("ml_page_types") or "")
    if ml.startswith("/Listing/Business") or ml.startswith("/Core_Page/Team") or re.search(r"/(firm|team|attorneys?|staff|our-team|people)/[^/]+/?$", urlpath(row["url"])): return "people"
    if ml.startswith("/Article") or re.search(r"/blog/[^/]+/?$", urlpath(row["url"])): return "post"
    if ml.startswith("/Product") or "/product/" in urlpath(row["url"]): return "product"
    return "core"

def classify_title(row, brand, sep):
    """What Google did with the title, and whether a new title is worth proposing. Returns (kind, proposed, why)."""
    title = first(row.get("title")); serp = (row.get("serp_title") or "").strip(); h1 = first(row.get("h1")).strip()
    path = urlpath(row["url"]); core = without_brand(title, brand)
    # a second, different brand-looking tail (typo: "Hasting Shadmehry")
    m = list(SEP_RE.finditer(title)); tail = title[m[-1].end():].strip() if m else ""
    if brand and tail and tail.lower() != brand.lower() and 0 < lev(tail, brand) <= 2:
        return "brand typo", f"{title[: m[-1].start()].strip()}{sep}{brand}", f"brand suffix reads '{tail}'"
    if re.search(r"[a-z][A-Z][a-z]", core) and h1:   # two titles glued together ("LinksPrenuptial")
        return "glued", f"{h1}{sep}{brand}" if brand else h1, "title is two titles concatenated; H1 used instead"
    years_t = set(re.findall(r"\b20\d\d\b", title)); years_u = set(re.findall(r"\b20\d\d\b", path + " " + h1))
    if years_t and years_u and not (years_t & years_u):
        y_old, y_new = sorted(years_t)[-1], sorted(years_u)[-1]
        return "stale year", title.replace(y_old, y_new), f"title says {y_old}, URL/H1 say {y_new}"
    if "serp mismatch" not in row["reasons"]: return "", "", ""
    if row.get("is_page_title_used_in_serp") is True: return "used as-is", "", ""
    if not serp: return "no serp title", "", "Ahrefs has no SERP title for this page"
    s = serp.rstrip(" .…").lower()
    if s == core.lower() or s == title.lower(): return "brand dropped", "", "Google shows the title minus the brand suffix; normal, nothing to do"
    if serp.endswith(("...", "…")) and core.lower().startswith(s): return "truncated", "", "display truncation only"
    if h1 and s == without_brand(h1, brand).lower():
        return "rewritten to H1", f"{h1}{sep}{brand}" if brand else h1, "Google replaced the title with the H1; proposing the H1 as the title"
    if brand and s.startswith(brand.lower()):
        return "brand moved first", "", "Google leads with the brand (navigational queries); leave"
    return "rewritten", f"{serp.rstrip(' .…')}{sep}{brand}" if brand and not serp.endswith(("...", "…")) else "", f"Google shows '{serp}'"

# ---------- page text ----------
def main_text(md, max_chars=3500):
    """Trim Ahrefs' page_text_md to the main content: start at the first H1, stop at reviews/footer-style headings."""
    lines = md.splitlines()
    start = next((i for i, l in enumerate(lines) if l.startswith("# ")), 0)
    out = []
    for l in lines[start:]:
        if out and MAIN_STOP.match(l): break
        if re.match(r"^\s*\[?©", l): break
        out.append(l)
    text = "\n".join(out).strip()
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)   # drop link targets
    return text[:max_chars]

def page_text(api, pid, url):
    key = "text-" + re.sub(r"\W+", "-", urlpath(url)).strip("-")[:80] or "home"
    try:
        d = api.get(key, "site-audit/page-content", project_id=pid, target_url=url, select="page_text_md")
    except SystemExit as e:
        log(f"  page text failed for {urlpath(url)}: {str(e)[:100]}"); return ""
    return (d.get("page-content") or d).get("page_text_md") or ""

# ---------- drafting ----------
def bio_fields(text, h1):
    """(name, role, areas[]) from a people page's main text, or None when the page is not shaped like a bio."""
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    role = ""
    for l in lines[1:6]:
        m = re.match(r"^#{2,6}\s*(.+)$", l)
        if m and 2 <= len(m.group(1)) <= 40 and m.group(1).lower() != h1.lower(): role = m.group(1).strip(); break
    areas = []
    m = re.search(r"^#{2,6}\s*areas? of (?:practice|focus)[^\n]*\n((?:\s*-\s*[^\n]+\n?)+)", text, re.I | re.M)
    if m: areas = [re.sub(r"^\s*-\s*", "", a).strip() for a in m.group(1).strip().splitlines()]
    return (h1, role, areas) if role or areas else None

def template_bio(name, role, areas, brand, city):
    where = f" in {city}" if city else ""
    a = ", ".join(areas[:3]) if areas else "family law"
    r = (role or "attorney").lower()
    return f"{name} is {'an' if r[0] in 'aeiou' else 'a'} {r} at {brand or 'the firm'}{where}, practicing {a}."

def model_draft(client, row, text, brand, sep, top_query):
    """One Anthropic API call. Returns {"title":..,"description":..} or None. ANTHROPIC_API_KEY from .env; model from LHF_DRAFT_MODEL."""
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key: return None
    vertical = client.get("vertical", "")
    rules = (f"You write SEO titles and meta descriptions for {client.get('name', client['domain'])} ({client['domain']}), vertical: {vertical}.\n"
             "Rules (Google Search Central): describe the page accurately, unique per page, no keyword lists, no city lists with pipes, no stale years, "
             f"one brand suffix at the end of a title exactly as '{sep.strip()} {brand}' when a brand is given. No character limit, but keep the title one phrase and the description one or two sentences "
             "that answer 'what will I find here'. Work the top search query in naturally only if the page really answers it. Make no claim the page does not make: "
             "for a law firm no outcome promises or superlatives; for a medical spa no treatment-result claims. Write from the page text only. "
             "Return JSON only: {\"title\": \"...\" or \"\", \"description\": \"...\"}. Return an empty title unless asked to draft one.")
    ask = (f"URL: {row['url']}\nH1: {first(row.get('h1'))}\nCurrent title: {first(row.get('title'))}\nGoogle shows: {row.get('serp_title') or ''}\n"
           f"Current description: {first(row.get('meta_description')) or '(none)'}\nTop GSC query: {top_query or '(none)'}\n"
           f"Draft a title: {'yes' if row.get('want_title') else 'no'}\nDraft a description: {'yes' if row.get('want_description') else 'no'}\n\nPage text:\n{text}")
    body = {"model": os.environ.get("LHF_DRAFT_MODEL", "claude-sonnet-5-5"), "max_tokens": 400, "system": rules,
            "messages": [{"role": "user", "content": ask}]}
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=json.dumps(body).encode("utf-8"), method="POST",
                                 headers={"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=90) as r: out = json.loads(r.read().decode("utf-8"))
        txt = "".join(c.get("text", "") for c in out.get("content", []))
        m = re.search(r"\{.*\}", txt, re.S)
        return json.loads(m.group(0)) if m else None
    except Exception as e:
        log(f"  draft failed for {urlpath(row['url'])}: {str(e)[:120]}"); return None

def load_hand_drafts(slug):
    f = ROOT / "reports" / slug / "meta-drafts.json"
    if not f.exists(): return {}
    d = json.loads(f.read_text(encoding="utf-8"))
    return {urlpath("https://x" + (k if k.startswith("/") else "/" + k)): v for k, v in d.items() if isinstance(v, dict)}

# ---------- queue ----------
def build_queue(client, data, api, args):
    brand, sep = detect_brand([first(p.get("title")) for p in data["sample"]] + [first(p.get("title")) for p in data["pages"].values()])
    cfg = (client.get("meta") or {})
    if cfg.get("brand_suffix"): brand = str(cfg["brand_suffix"]); sep = str(cfg.get("separator") or sep)
    city = cfg.get("city") or ""
    hand = load_hand_drafts(client["slug"])
    rows, routed = [], {"archive": [], "noindex": [], "non-200": [], "homepage title": []}
    for url, p in data["pages"].items():
        path = urlpath(url)
        if ARCHIVE_RE.search(path) or str(p.get("ml_page_types") or "").startswith(("/Listing_Collection", "/Core_Page/Blog_Index")):
            routed["archive"].append(path); continue
        if p.get("page_is_noindex"): routed["noindex"].append(path); continue
        if p.get("http_code") not in (200, None): routed["non-200"].append(path); continue
        g = data["gsc"].get(norm(url), {})
        kind = page_kind(p)
        tkind, tprop, twhy = classify_title(p, brand, sep)
        if path == "/" and tprop:
            routed["homepage title"].append(path); tkind, tprop, twhy = tkind, "", twhy + "; homepage title comes from Yoast's site-wide template, change it there"
        want_d = "description missing" in p["reasons"] or "multiple descriptions" in p["reasons"] or "duplicate description" in p["reasons"] \
                 or (p.get("duplicate_description_canonical_hreflang") or 0) > 1
        want_t = bool(tprop) or "title missing" in p["reasons"] or "multiple titles" in p["reasons"] or (p.get("duplicate_title_canonical_hreflang") or 0) > 1
        stale_desc = ""
        if tkind == "stale year":
            yrs = re.findall(r"\b20\d\d\b", first(p.get("title"))); new_y = re.findall(r"\b20\d\d\b", tprop)
            cur_d = first(p.get("meta_description"))
            if yrs and new_y and yrs[-1] in cur_d and yrs[-1] != new_y[-1]:
                stale_desc = cur_d.replace(yrs[-1], new_y[-1]); want_d = True
        if not want_d and not want_t and tkind in ("brand dropped", "truncated", "used as-is", "brand moved first", "no serp title", ""):
            # nothing to write; keep it in the report's "no action" list only
            rows.append({"url": url, "path": path, "page_type": kind, "action": "none", "title_kind": tkind, "why": twhy, "gsc": g, "traffic": p.get("traffic") or 0,
                         "current_title": first(p.get("title")), "serp_title": p.get("serp_title") or "", "current_description": first(p.get("meta_description")), "reasons": p["reasons"]})
            continue
        imp = int(g.get("impressions") or 0); ctr = pct(g.get("ctr"))
        score = imp * (1 - ctr / 100) if g else -1
        rows.append({"url": url, "path": path, "page_type": kind, "action": "write", "title_kind": tkind, "why": twhy, "gsc": g, "traffic": p.get("traffic") or 0,
                     "score": score, "want_title": want_t, "want_description": want_d,
                     "current_title": first(p.get("title")), "serp_title": p.get("serp_title") or "", "h1": first(p.get("h1")),
                     "current_description": first(p.get("meta_description")), "proposed_title": tprop, "proposed_description": stale_desc,
                     "basis": (["description: stale year swapped in the existing description"] if stale_desc else []), "reasons": p["reasons"], "ml": p.get("ml_page_types") or ""})
    order = {"core": 0, "people": 1, "product": 2, "post": 3}
    todo = [r for r in rows if r["action"] == "write"]
    todo.sort(key=lambda r: (-(r["score"] if r["score"] >= 0 else -1), -r["traffic"], order.get(r["page_type"], 9), r["path"]))
    # drafts: hand file > model > template
    seo = str((client.get("platform") or {}).get("seo_plugin", "")).lower()
    n_text = 0
    for r in todo:
        if r["proposed_title"]: r["basis"].append("title: " + r["title_kind"])
        h = hand.get(r["path"])
        if h:   # a hand draft is an explicit decision, so it may add a field the issues did not ask for
            if h.get("title"): r["proposed_title"] = h["title"]; r["want_title"] = True; r["basis"] = [b for b in r["basis"] if not b.startswith("title:")] + ["title: hand draft: " + (h.get("basis") or "")]
            if h.get("description"): r["proposed_description"] = h["description"]; r["want_description"] = True; r["basis"] = [b for b in r["basis"] if not b.startswith("description:")] + ["description: hand draft: " + (h.get("basis") or "")]
        if r["want_description"] and not r["proposed_description"] and n_text < args.max_pages:
            text = main_text(page_text(api, data["pid"], r["url"])); n_text += 1
            r["text_chars"] = len(text)
            got = None
            if args.draft and text:
                got = model_draft(client, r, text, brand, sep, r["gsc"].get("top_keyword"))
            if got and got.get("description"):
                r["proposed_description"] = got["description"].strip(); r["basis"].append("description: from page text (model draft)")
                if got.get("title") and r["want_title"] and not r["proposed_title"]: r["proposed_title"] = got["title"].strip(); r["basis"].append("title: model draft")
            elif r["page_type"] == "people" and text:
                bf = bio_fields(text, r["h1"])
                if bf:
                    r["proposed_description"] = template_bio(bf[0], bf[1], bf[2], brand, city); r["basis"].append("description: templated from fields")
            if not r["proposed_description"]: r["basis"].append("description: needs draft")
        elif r["want_description"] and not r["proposed_description"]:
            r["basis"].append("description: needs draft (page text not pulled; raise --max-pages)")
        if seo == "aioseo": r["basis"].append("manual in AIOSEO (no writer yet)")
    return {"brand": brand, "sep": sep, "rows": rows, "todo": todo, "routed": routed, "seo_plugin": seo}

# ---------- report ----------
def write_report(client, data, q):
    slug, host = client["slug"], client["domain"]
    out = [f"# fix-meta: {host}", "",
           f"Ahrefs Site Audit project {data['pid']} · crawl {data['crawl']} · health {data.get('health')} · brand suffix detected: `{q['sep'].strip()} {q['brand']}`"
           + (f" · GSC {data['gsc_window']} ({len(data['gsc'])} pages)" if data["gsc"] else " · no GSC (queue ordered by Ahrefs traffic)") + "", "",
           "APPROVE tier. Nothing here is written to the site until a human has typed or approved it in the review sheet (`--sheet`, then `--fix`). "
           "Queue order: GSC impressions × (1 − CTR), so the pages Google shows most but clicks least come first.", ""]
    found = {ISSUE_NAMES[n]: (i.get("crawled") or 0) for n, i in data["found"].items()}
    out += ["Issues read: " + ", ".join(f"{k} {v}" for k, v in found.items()) + f" → {len(data['pages'])} distinct URLs: {len(q['todo'])} to write, "
            f"{sum(1 for r in q['rows'] if r['action'] == 'none')} no action, " + ", ".join(f"{k} {len(v)}" for k, v in q["routed"].items() if v) + ".", ""]
    if q["seo_plugin"] == "aioseo": out += ["**This site runs AIOSEO.** The writer is Yoast-only in v1; the queue is for manual entry in AIOSEO.", ""]
    out += ["## Queue (write, in order)", "", "| # | URL | type | impr | CTR | pos | top query | title | description |", "|---|---|---|---|---|---|---|---|---|"]
    for n, r in enumerate(q["todo"], 1):
        g = r["gsc"]
        t = ("**" + r["proposed_title"] + "**" if r["proposed_title"] else ("needs draft" if r["want_title"] else "keep")) + (f" ({r['title_kind']})" if r["title_kind"] else "")
        d = ("**" + r["proposed_description"] + "**") if r["proposed_description"] else ("needs draft" if r["want_description"] else "keep")
        out.append(f"| {n} | `{r['path']}` | {r['page_type']} | {int(g.get('impressions') or 0) if g else '-'} | {pct(g.get('ctr')):.2f}% | {float(g.get('position') or 0):.1f} | {g.get('top_keyword') or ''} | {t} | {d} |"
                   if g else f"| {n} | `{r['path']}` | {r['page_type']} | - | - | - |  | {t} | {d} |")
    out += ["", "## Per page", ""]
    for n, r in enumerate(q["todo"], 1):
        out += [f"### {n}. `{r['path']}` ({r['page_type']}; {', '.join(r['reasons'])})", "",
                f"- current title: {r['current_title']}" + (f"  · Google shows: {r['serp_title']}" if r["serp_title"] else ""),
                f"- H1: {r['h1']}"]
        if r["why"]: out.append(f"- title: {r['title_kind']}: {r['why']}")
        if r["proposed_title"]: out.append(f"- **proposed title:** {r['proposed_title']}")
        out.append(f"- current description: {r['current_description'] or '(none)'}")
        if r["proposed_description"]: out.append(f"- **proposed description:** {r['proposed_description']}")
        out.append(f"- basis: {'; '.join(r['basis']) or 'none'}")
        out.append("")
    noact = [r for r in q["rows"] if r["action"] == "none"]
    if noact:
        out += ["## No action (flagged by Ahrefs, nothing to write)", "", "| URL | Ahrefs issue | what Google did | note |", "|---|---|---|---|"]
        for r in sorted(noact, key=lambda r: -r["traffic"]): out.append(f"| `{r['path']}` | {', '.join(r['reasons'])} | {r['title_kind']} | {r['why']} |")
        out.append("")
    out += ["## Routed elsewhere", ""]
    for k, v in q["routed"].items():
        if not v: continue
        where = {"archive": "`indexation-review` (Yoast taxonomy/archive templates or noindex; one setting covers all of them)", "noindex": "skipped: descriptions on noindexed pages are wasted work",
                 "non-200": "skipped: not a 200", "homepage title": "Yoast → Search Appearance → homepage title template (propose, do not automate)"}[k]
        out.append(f"- **{k}** ({len(v)}): {where}" + (f" — e.g. " + ", ".join(f"`{p}`" for p in v[:6]) if k != "archive" else f" — " + ", ".join(f"`{p}`" for p in v[:8]) + (" …" if len(v) > 8 else "")))
    out += ["", "## Standards applied", "",
            "- Titles: describe the page, match the H1's meaning, one brand suffix, no keyword or city lists, no stale years. Where Google already uses the title "
            "(or merely drops the brand or truncates the display) nothing is proposed; where Google swapped in the H1, the H1 is proposed.",
            "- Descriptions: unique, from the page's own text, one or two sentences answering 'what will I find here', top GSC query worked in only when the page answers it; "
            "no claims the page does not make. Templated bios are fine when the fields are real (Google: programmatic descriptions from page data are acceptable).",
            "- 'Title too long' and 'Meta description too long' are ignored on purpose: Google states no length limit. The skill never truncates.",
            "- Sources: Google title links https://developers.google.com/search/docs/appearance/title-link · snippets https://developers.google.com/search/docs/appearance/snippet · "
            "Ahrefs title-tag study https://ahrefs.com/blog/title-tags-study · SEL on title rewrites https://searchengineland.com/google-changed-76-of-title-tags-in-q1-2025-heres-what-that-means-454847", ""]
    out += ["## Next", "", f"`python scripts\\fix_meta.py {slug} --sheet` pushes the queue to the `meta` tab of the review sheet; a human fills `new_title` / `new_description` "
            "(blank = leave that field alone), sets `status` to `approved`, then `--fix` (staging dry) → `--fix --apply` → `--fix --apply --target live`.", ""]
    return "\n".join(out) + "\n"

# ---------- sheet ----------
def sheet_rows_from_queue(q, data, today):
    rows = []
    for r in q["todo"]:
        g = r["gsc"]
        rows.append([r["url"], r["page_type"], int(g.get("impressions") or 0) if g else "", f"{pct(g.get('ctr')):.2f}" if g else "", f"{float(g.get('position') or 0):.1f}" if g else "",
                     g.get("top_keyword") or "" if g else "", r["current_title"], r["serp_title"], r["proposed_title"], "", r["current_description"], r["proposed_description"], "",
                     "; ".join(r["basis"]), "pending", "", f"{today} (crawl {data['crawl']})"])
    return rows

def open_meta_tab(client):
    from review_sheets import gc
    sid = ((client.get("review") or {}).get("alt_sheet_id") or "").strip()
    if not sid or sid == "unknown": sys.exit(f"no review sheet (review.alt_sheet_id) in clients/{client['slug']}.yaml; run: python scripts/review_sheets.py setup {client['slug']}")
    g = gc(); sh = g.open_by_key(sid)
    try: ws = sh.worksheet(SHEET_TAB)
    except Exception:
        ws = sh.add_worksheet(SHEET_TAB, rows=300, cols=len(SHEET_COLS)); ws.append_row(SHEET_COLS); ws.freeze(rows=1)
    vals = ws.get_all_values(); head = vals[0] if vals else []
    if head != SHEET_COLS:
        if not any(r for r in vals[1:] if any(r)): ws.clear(); ws.update("A1", [SHEET_COLS], value_input_option="RAW"); ws.freeze(rows=1); vals = [SHEET_COLS]
        else: sys.exit(f"'{SHEET_TAB}' tab has unexpected columns {head}; expected {SHEET_COLS}")
    return sh, ws, vals

def push_sheet(client, data, q):
    """Upsert one row per queued URL. Metrics, current values, proposals and basis refresh; new_*, status and note are the human's."""
    sh, ws, vals = open_meta_tab(client)
    today = datetime.date.today().isoformat()
    existing = {r[0]: (i + 2, r + [""] * (len(SHEET_COLS) - len(r))) for i, r in enumerate(vals[1:]) if r and r[0]}
    updates, appends = [], []
    for new in sheet_rows_from_queue(q, data, today):
        if new[0] in existing:
            rn, old = existing[new[0]]
            if old[SHEET_COLS.index("status")].startswith("applied"): continue   # done; the next crawl decides whether it comes back
            merged = [old[i] if SHEET_COLS[i] in HUMAN_COLS else new[i] for i in range(len(SHEET_COLS))]
            if not merged[SHEET_COLS.index("status")]: merged[SHEET_COLS.index("status")] = "pending"
            updates.append((rn, merged))
        else:
            appends.append(new)
    for rn, v in updates: ws.update(range_name=f"A{rn}:{chr(64 + len(SHEET_COLS))}{rn}", values=[v], value_input_option="RAW")
    if appends: ws.append_rows(appends, value_input_option="RAW")
    return f"{len(appends)} added, {len(updates)} refreshed on '{SHEET_TAB}' ({sh.url})"

# ---------- apply ----------
def ssh(alias, cmd, inp=None):
    try:
        r = subprocess.run(["ssh", alias, cmd], input=inp.encode("utf-8") if inp else None, capture_output=True, timeout=300)
    except (OSError, subprocess.TimeoutExpired) as e:
        return 255, "", f"ssh {alias}: {e}"
    return r.returncode, r.stdout.decode("utf-8", "replace"), r.stderr.decode("utf-8", "replace")

def target_alias(client, target, webroot="public"):
    hosting = client.get("hosting", {})
    alias = ((hosting.get("ssh_alias") if target == "live" else hosting.get("staging_environment")) or "").split(",")[0].strip()
    if not alias or alias in ("unknown", "none"): sys.exit(f"no {target} SSH alias in clients/{client['slug']}.yaml")
    provider = str(hosting.get("provider") or "other").lower()
    if provider in ("", "unknown", "none"): provider = "other"
    root = wpengine_webroot(alias) if provider == "wpengine" and webroot == "public" else webroot
    return alias, provider, root

def run_php(alias, webroot, job):
    php = (HERE / "php" / "set_meta.php").read_text(encoding="utf-8")
    payload = "<?php define('META_JOB', " + json.dumps(json.dumps(job, ensure_ascii=False)) + "); ?>" + php
    code, out, err = ssh(alias, f"cd {webroot} || exit 97; wp --skip-plugins={SKIP_PLUGINS} eval-file -", payload)
    if code == 97: raise RuntimeError(f"no such directory {webroot} on {alias}")
    if "===JSON===" not in out: raise RuntimeError((err or out).strip()[-400:])
    return json.loads(out.split("===JSON===", 1)[1].strip())

def fetch_rendered(url):
    """<title> and <meta name=description> as the public page serves them."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
        with urllib.request.urlopen(req, timeout=20) as r: html = r.read(400000).decode("utf-8", "replace")
    except Exception as e:
        return f"fetch failed: {type(e).__name__}", ""
    t = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    d = re.search(r"<meta\s+[^>]*name=[\"']description[\"'][^>]*content=[\"']([^\"']*)[\"']", html, re.I) or re.search(r"<meta\s+[^>]*content=[\"']([^\"']*)[\"'][^>]*name=[\"']description[\"']", html, re.I)
    import html as H
    return (H.unescape(re.sub(r"\s+", " ", t.group(1)).strip()) if t else ""), (H.unescape(d.group(1)) if d else "")

def fix_from_sheet(client, args):
    sh, ws, vals = open_meta_tab(client)
    ci = {c: i for i, c in enumerate(SHEET_COLS)}
    approved = []
    for i, r in enumerate(vals[1:]):
        r = r + [""] * (len(SHEET_COLS) - len(r))
        st = r[ci["status"]].strip().lower()
        if st != "approved": continue
        t, d = r[ci["new_title"]].strip(), r[ci["new_description"]].strip()
        if t.lower() == "skip": t = ""
        if d.lower() == "skip": d = ""
        if not t and not d: continue
        approved.append((i + 2, r, t, d))
    if not approved: return "no approved rows with a new_title or new_description on the sheet"
    seo = str((client.get("platform") or {}).get("seo_plugin", "")).lower()
    if seo != "yoast": return f"seo_plugin is '{seo}'; the writer is Yoast-only (enter these {len(approved)} rows by hand)"
    alias, provider, webroot = target_alias(client, args.target, args.webroot)
    mode = "apply" if args.apply else "dry"
    if args.apply and args.target == "live":
        if args.yes: print("APPLY on LIVE — confirmed by --yes")
        elif not sys.stdin.isatty(): sys.exit("Live apply needs a terminal to confirm, or pass --yes.")
        else:
            print(f"About to write {len(approved)} title/description row(s) on LIVE ({alias}). Type the slug to confirm: ", end="", flush=True)
            if input().strip() != client["slug"]: sys.exit("aborted")
    job = {"mode": mode, "rows": [{"url": r[ci["url"]], "title": t, "description": d} for _, r, t, d in approved]}
    res = run_php(alias, webroot, job)
    rows = res.get("rows", [])
    counts = {}
    for r in rows: counts[r["status"]] = counts.get(r["status"], 0) + 1
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    outdir = ROOT / "changes" / provider / client["slug"]; outdir.mkdir(parents=True, exist_ok=True)
    flush = ""
    if args.apply:
        bdir = outdir / "backup"; bdir.mkdir(exist_ok=True)
        (bdir / f"{stamp}-{SKILL}-{args.target}.json").write_text(json.dumps({"slug": client["slug"], "target": args.target, "stamp": stamp,
            "rows": [r for r in rows if r["status"] == "set"]}, indent=1, ensure_ascii=False), encoding="utf-8")
        c, o, e = ssh(alias, f"cd {webroot} && wp --skip-plugins={SKIP_PLUGINS} cache flush 2>&1" + (f"; wp --skip-plugins={SKIP_PLUGINS} kinsta cache purge --all 2>&1" if provider == "kinsta" else ""))
        flush = (o + e).strip().splitlines()[-1] if (o + e).strip() else f"rc {c}"
    # verify from outside on live
    public = {}
    if args.apply and args.target == "live":
        for r in rows:
            if r["status"] == "set": public[r["url"]] = fetch_rendered(r["url"])
    lines = [f"# {SKILL}: titles and descriptions on {client['domain']} ({args.target})", "",
             f"Run {stamp} · mode **{mode}** · alias `{alias}` · provider `{provider}` · {len(approved)} approved row(s) from the sheet · " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items()))
             + (f" · cache flush: {flush}" if flush else ""), "",
             "Writes Yoast's `_yoast_wpseo_title` / `_yoast_wpseo_metadesc` per post. `rendered` is what Yoast will output for the page "
             "(in a dry run: the current state; after an apply: the new one, so you can see whether Yoast appended its template's brand/separator). "
             + (f"Rollback: `python scripts/fix_meta.py {client['slug']} --rollback changes/{provider}/{client['slug']}/backup/{stamp}-{SKILL}-{args.target}.json --apply`" if args.apply else ""), "",
             "| URL | post | status | title before → after | description before → after | rendered title | rendered description |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        tb, ta = r.get("title_before", ""), r.get("title_after", ""); db, da = r.get("description_before", ""), r.get("description_after", "")
        lines.append(f"| `{urlpath(r['url'])}` | {r.get('id') or ''} {r.get('post_type', '')} | {r['status']} | {tb or '(none)'} → {ta if ta != tb else '='} | {db or '(none)'} → {da if da != db else '='} | {r.get('rendered_title', '')} | {r.get('rendered_description', '')} |")
    if public:
        lines += ["", "## Public re-fetch (live)", "", "| URL | <title> | description |", "|---|---|---|"]
        for u, (t, d) in public.items(): lines.append(f"| `{urlpath(u)}` | {t} | {d} |")
        lines += ["", "An unchanged public value right after the apply is usually the edge cache; re-check in a few minutes."]
    logp = outdir / f"{stamp}-{SKILL}-{args.target}-{mode}.md"
    logp.write_text("\n".join(lines) + "\n", encoding="utf-8")
    # sheet status
    if args.apply and args.target == "live":
        today = datetime.date.today().isoformat(); byurl = {r["url"]: r for r in rows}
        for rn, r, t, d in approved:
            st = byurl.get(r[ci["url"]], {}).get("status")
            if st == "set": ws.update(range_name=f"{chr(65 + ci['status'])}{rn}:{chr(65 + ci['updated'])}{rn}", values=[[f"applied {today}", r[ci["note"]], f"{today} (applied)"]], value_input_option="RAW")
            elif st and st != "already": ws.update(range_name=f"{chr(65 + ci['note'])}{rn}", values=[[(r[ci['note']] + " | " if r[ci['note']] else "") + f"{today}: {st}"]], value_input_option="RAW")
    return f"{mode} on {args.target} ({alias}): " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) + f" · log {logp}"

def rollback(client, backup_path, apply, webroot):
    b = json.loads(Path(backup_path).read_text(encoding="utf-8")); target = b.get("target", "live")
    alias, provider, root = target_alias(client, target, webroot)
    mode = "apply" if apply else "dry"
    if apply and target == "live" and sys.stdin.isatty():
        print(f"About to RESTORE {len(b['rows'])} row(s) on LIVE ({alias}). Type the slug to confirm: ", end="", flush=True)
        if input().strip() != client["slug"]: sys.exit("aborted")
    php = ("$rows = json_decode(ROLLBACK_JOB, true); $out = [];"
           "foreach ($rows as $r) { $id = (int) $r['id']; $res = [];"
           " foreach ([['_yoast_wpseo_title','title_before','title_after'],['_yoast_wpseo_metadesc','description_before','description_after']] as [$k,$bk,$ak]) {"
           "  if ($r[$bk] === $r[$ak]) continue; $cur = (string) get_post_meta($id, $k, true);"
           "  if ($cur !== $r[$ak]) { $res[] = \"$k changed since, left alone\"; continue; }"
           "  if (MODE === 'apply') { if ($r[$bk] === '') delete_post_meta($id, $k); else update_post_meta($id, $k, $r[$bk]); $res[] = \"$k restored\"; } else $res[] = \"$k would restore\"; }"
           " $out[] = ['id' => $id, 'url' => $r['url'], 'result' => implode('; ', $res) ?: 'nothing to restore']; }"
           "if (MODE === 'apply') wp_cache_flush(); echo '===JSON===' . json_encode($out, JSON_UNESCAPED_SLASHES);")
    payload = "<?php define('ROLLBACK_JOB', " + json.dumps(json.dumps(b["rows"], ensure_ascii=False)) + "); define('MODE', '" + mode + "'); " + php
    code, out, err = ssh(alias, f"cd {root} || exit 97; wp --skip-plugins={SKIP_PLUGINS} eval-file -", payload)
    if "===JSON===" not in out: sys.exit(f"remote run failed: {(err or out).strip()[-400:]}")
    res = json.loads(out.split("===JSON===", 1)[1].strip())
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    outdir = ROOT / "changes" / provider / client["slug"]; outdir.mkdir(parents=True, exist_ok=True)
    lines = [f"# {SKILL}: rollback on {client['domain']} ({target})", "", f"Run {stamp} · mode **{mode}** · alias `{alias}` · backup `{Path(backup_path).name}`", "",
             "| URL | post | result |", "|---|---|---|"] + [f"| `{urlpath(r['url'])}` | {r['id']} | {r['result']} |" for r in res]
    (outdir / f"{stamp}-{SKILL}-{target}-rollback-{mode}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    for r in res: print(f"  {r['id']:6} {urlpath(r['url'])}: {r['result']}")
    print(f"Log: {outdir / f'{stamp}-{SKILL}-{target}-rollback-{mode}.md'}")

# ---------- main ----------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--probe", action="store_true", help="build the queue and drafts -> reports/<slug>/meta-<crawl>.md and .json")
    ap.add_argument("--draft", action="store_true", help="with --probe: draft titles/descriptions with the Anthropic API (ANTHROPIC_API_KEY in .env)")
    ap.add_argument("--max-pages", type=int, default=40, dest="max_pages", help="with --probe: how many pages get their text pulled for drafting (≈50 Ahrefs units each)")
    ap.add_argument("--cache", action="store_true", help="keep/reuse raw Ahrefs responses in tmp/ahrefs-cache/<slug>/")
    ap.add_argument("--sheet", action="store_true", help="push the queue from the newest reports/<slug>/meta-<crawl>.json to the 'meta' tab (runs --probe first if none)")
    ap.add_argument("--fix", action="store_true", help="write the approved sheet rows (dry unless --apply)")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--target", choices=["staging", "live"], default="staging")
    ap.add_argument("--yes", action="store_true", help="skip the live confirmation prompt (vetted unattended runs)")
    ap.add_argument("--webroot", default="public")
    ap.add_argument("--rollback", help="backup JSON from an apply; dry unless --apply")
    args = ap.parse_args()
    load_env()
    cpath = ROOT / "clients" / f"{args.slug}.yaml"
    client = yaml.safe_load(cpath.read_text(encoding="utf-8")); client.setdefault("slug", args.slug)
    if args.rollback: return rollback(client, args.rollback, args.apply, args.webroot)
    if args.fix: return print(f"{args.slug}: {fix_from_sheet(client, args)}")
    pid = (client.get("ahrefs") or {}).get("site_audit_project_id")
    if not pid or str(pid) in ("0", "unknown"): sys.exit(f"clients/{args.slug}.yaml has no ahrefs.site_audit_project_id")
    outdir = ROOT / "reports" / args.slug; outdir.mkdir(parents=True, exist_ok=True)
    if args.sheet and not args.probe:
        js = sorted(outdir.glob("meta-*.json"))
        if js:
            saved = json.loads(js[-1].read_text(encoding="utf-8"))
            print(f"{args.slug}: sheet: {push_sheet(client, saved['data'], saved['queue'])} (from {js[-1].name})"); return
        args.probe = True
    if not args.probe: ap.error("one of --probe, --sheet, --fix, --rollback")
    api = Api(args.slug, args.cache)
    data = pull(client, api)
    q = build_queue(client, data, api, args)
    rep = outdir / f"meta-{data['crawl']}.md"
    rep.write_text(write_report(client, data, q), encoding="utf-8")
    slim = {"pid": data["pid"], "crawl": data["crawl"], "health": data["health"], "gsc_window": data["gsc_window"], "gsc": {}, "found": {n: {"crawled": i.get("crawled")} for n, i in data["found"].items()}}
    (outdir / f"meta-{data['crawl']}.json").write_text(json.dumps({"data": slim, "queue": {"brand": q["brand"], "sep": q["sep"], "todo": q["todo"], "routed": q["routed"], "seo_plugin": q["seo_plugin"],
                                                                      "rows": []}}, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{client['domain']}: crawl {data['crawl']}, {len(data['pages'])} flagged URLs → {len(q['todo'])} to write, {sum(1 for r in q['rows'] if r['action'] == 'none')} no action, "
          + ", ".join(f"{k} {len(v)}" for k, v in q["routed"].items() if v))
    print(f"  brand suffix: '{q['sep'].strip()} {q['brand']}' · titles proposed {sum(1 for r in q['todo'] if r['proposed_title'])} · "
          f"descriptions proposed {sum(1 for r in q['todo'] if r['proposed_description'])} · needs draft {sum(1 for r in q['todo'] if any('needs draft' in b for b in r['basis']))}")
    for n, r in enumerate(q["todo"][:12], 1):
        g = r["gsc"]; print(f"  {n:2}. {r['path']:55} {int(g.get('impressions') or 0) if g else '-':>6} impr  {r['title_kind'] or '-':16} {'desc' if r['want_description'] else ''}")
    if len(q["todo"]) > 12: print(f"  … {len(q['todo']) - 12} more in the report")
    print(f"Report: {rep}")
    if args.sheet: print(f"Sheet: {push_sheet(client, data, q)}")

if __name__ == "__main__":
    main()
