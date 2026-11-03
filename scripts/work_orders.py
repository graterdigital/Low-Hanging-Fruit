#!/usr/bin/env python3
"""Work orders: everything that needs a human, in one place per client, fed from the latest Ahrefs crawl through routes.yaml.

    python scripts/work_orders.py <slug>                   # report only -> reports/<slug>/work-orders-<crawl>.md (+ .json)
    python scripts/work_orders.py <slug> --cache           # keep/reuse the raw Ahrefs responses in tmp/ahrefs-cache/<slug>/ (offline reruns)
    python scripts/work_orders.py <slug> --sheet           # also upsert the "work orders" tab on the client's review sheet
    python scripts/work_orders.py <slug> --decisions       # read decisions back from the sheet into clients/<slug>.yaml (rules.decisions)
    python scripts/work_orders.py --all [--sheet] [--cache]  # every client with an Ahrefs project
    python scripts/work_orders.py --roster [--sheet]       # roster view from the per-client JSONs -> reports/_roster/work-orders-<date>.md
                                                           # (+ the "work orders" tab on the agency sheet, clients/_agency.yaml review.agency_sheet_id)

What becomes a work order (routes.yaml decides; this script has no list of its own):
  - handler `manual`                                 (template edits, hosting tickets, content calls)
  - tier `FLAG` or `decide`                          (diagnose first / a human must choose; `decide` rows carry a `decider`)
  - handler is a skill still marked `proposed`       ("skill pending": real work nobody is doing yet; drops off when the skill is built)
  - handler `review`                                 (unclassified issue types; classify them in routes.yaml)
  - items a built skill routed out: fix-redirect-links `skipped` + wp_options hits, fix-images product-alt exceptions,
    fix-meta's routed rows, and any `*-workorders.json` a skill writes (see WORKORDERS_JSON below).
Ignored / monitor / built-skill rows never appear: the skills handle those.

Sheet tab "work orders": humans edit owner, status, decision_or_note only. status: open -> needs decision -> in progress -> done | won't fix.
The script refreshes counts, traffic and examples on every run, stamps `cleared <date>` when the next crawl no longer shows the issue,
and with --decisions copies `status: done` rows whose note starts with "decision:" into the client file so no skill asks twice.

Needs AHREFS_API_KEY (environment or .env at the repo root). The sheet commands need the Google service account (docs/setup-machine.md).
"""
import argparse, csv, datetime, json, re, sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from build_redirect_map import load_env, ahrefs  # noqa: E402

TAB = "work orders"
COLS = ["id", "issue", "handler", "tier", "urls_affected", "traffic_at_stake", "what_to_do", "example_urls", "decider",
        "owner", "status", "decision_or_note", "opened", "updated", "cleared"]
HUMAN = ("owner", "status", "decision_or_note")          # never overwritten by the script
OPEN_STATUSES = ("", "open", "needs decision", "in progress")
PAGE_LIMIT = 200                                           # URLs pulled per issue for traffic_at_stake; above this it is a sample
EXAMPLES = 10
PAGINATION = re.compile(r"/page/\d+/?$")
# Format other skills can write next to their reports (reports/<slug>/<stamp>-<skill>-workorders.json or changes/<provider>/<slug>/...):
#   {"skill": "fix-redirect-links", "crawl": "2026-10-29", "items": [{"id": "redirect-links:homepage-redirects", "issue": "...",
#    "tier": "APPROVE", "what_to_do": "...", "decider": "agency", "urls": ["..."], "traffic": 0}]}
WORKORDERS_JSON = "*-workorders.json"

def log(*a): print(*a, file=sys.stderr)
def today(): return datetime.date.today().isoformat()
def path_of(u):
    from urllib.parse import urlsplit
    p = urlsplit(u); return (p.path or "/") + (("?" + p.query) if p.query else "")
def slugify(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

# ---------- inputs ----------
def load_routes():
    r = yaml.safe_load((ROOT / "routes.yaml").read_text(encoding="utf-8"))
    by_id = {}
    for x in r["routes"]:
        for i in x.get("issue_ids") or []: by_id[i] = x
    return r.get("handlers") or {}, by_id

def load_client(slug):
    p = ROOT / "clients" / f"{slug}.yaml"
    if not p.exists(): sys.exit(f"no client file clients/{slug}.yaml")
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}

def provider_of(c): return str((c.get("hosting") or {}).get("provider") or "other").lower() or "other"

class Api:
    """Ahrefs with an optional on-disk cache (same layout as ai_discoverability.py: tmp/ahrefs-cache/<slug>/<name>.json)."""
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
    hs = (api.get("project", "site-audit/projects", project_id=pid).get("healthscores") or [{}])[0]
    crawl = (hs.get("date") or "")[:10] or today()
    issues = [i for i in api.get("issues", "site-audit/issues", project_id=pid).get("issues", []) if (i.get("crawled") or 0) > 0]
    return pid, crawl, hs.get("health_score"), issues

def pages_for(api, pid, issue_id):
    return api.get(f"pages-{issue_id}", "site-audit/page-explorer", project_id=pid, issue_id=issue_id, select="url,traffic",
                   order_by="traffic:desc", limit=PAGE_LIMIT).get("pages", [])

# ---------- rows ----------
def is_work_order(route, handlers):
    if not route: return True, "review"                       # unmapped issue type: a human classifies it
    h, tier = route["handler"], str(route.get("tier") or "")
    if h == "manual": return True, "manual"
    if h == "review": return True, "review"
    if tier in ("FLAG", "decide"): return True, tier
    if handlers.get(h) == "proposed": return True, "skill pending"
    return False, ""

def issue_rows(client, api, handlers, by_id, pid, crawl, issues):
    rows, skipped = [], []
    for i in issues:
        route = by_id.get(i["issue_id"]); yes, kind = is_work_order(route, handlers)
        if not yes: continue
        name = i["name"]; handler = route["handler"] if route else "review"
        tier = str(route.get("tier") or "") if route else "?"
        pages = pages_for(api, pid, i["issue_id"])
        urls = [p["url"] for p in pages]
        if urls and all(PAGINATION.search(path_of(u)) for u in urls) and name in ("Indexable page not in sitemap", "Open Graph URL not matching canonical"):
            skipped.append((name, i["crawled"], "all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design"))
            continue
        traffic = round(sum(float(p.get("traffic") or 0) for p in pages))
        sampled = f" (top {PAGE_LIMIT} of {i['crawled']})" if i["crawled"] > len(pages) else ""
        if kind == "skill pending":
            what = f"Skill `{handler}` is planned but not built; until then: " + (route.get("what_to_do") or route.get("note") or "")
        elif kind == "review":
            what = "Not classified in routes.yaml yet: decide the handler and tier there (note: " + ((route or {}).get("note") or "none") + ")"
        else:
            what = route.get("what_to_do") or route.get("note") or ""
        rows.append({"id": f"issue:{slugify(name)}" + ("-nonindexable" if i.get("is_indexable") is False else ""),
                     "issue": name + ("  (non-indexable pages)" if i.get("is_indexable") is False else ""),
                     "handler": (route.get("route") if route and route.get("route") else handler),
                     "tier": tier if kind != "skill pending" else f"{tier} (skill pending)",
                     "urls_affected": i["crawled"], "traffic_at_stake": traffic, "traffic_note": sampled,
                     "what_to_do": what, "examples": [(path_of(p["url"]), int(p.get("traffic") or 0), "traffic") for p in pages[:EXAMPLES]],
                     "decider": (route or {}).get("decider") or ("agency" if kind != "decide" else "client"),
                     "importance": i.get("importance") or "", "source": "ahrefs"})
    return merge_intent(rows), skipped

INTENT = ("issue:noindex-page", "issue:noindex-follow-page", "issue:noindex-and-nofollow-page", "issue:nofollow-page")
def merge_intent(rows):
    """Ahrefs reports one hidden page under up to four noindex/nofollow issues; the client answers one question, so it is one row."""
    hits = [r for r in rows if r["id"].split("-nonindexable")[0] in INTENT]
    if len(hits) < 2: return rows
    urls = {}
    for r in hits:
        for p, t, u in r["examples"]: urls.setdefault(p, t)
    merged = {"id": "issue:hidden-pages-confirm-intent", "issue": "Pages hidden from Google (noindex/nofollow): confirm intent",
              "handler": "indexation-review", "tier": "decide", "urls_affected": max(r["urls_affected"] for r in hits), "traffic_at_stake": sum(r["traffic_at_stake"] for r in hits) and max(r["traffic_at_stake"] for r in hits),
              "traffic_note": "", "what_to_do": "Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. "
              + "Ahrefs issues folded in: " + ", ".join(r["issue"] for r in hits) + ".",
              "examples": [(p, t, "traffic") for p, t in list(urls.items())[:EXAMPLES]], "decider": "client", "importance": max(r["importance"] for r in hits), "source": "ahrefs"}
    return [r for r in rows if r not in hits] + [merged]

def newest(globs):
    files = []
    for g in globs: files += list(g[0].glob(g[1]))
    return sorted(files)[-1] if files else None

# Reasons build_redirect_map.py writes on skipped URLs -> (handler, tier, decider, what_to_do); "skip" = expected, no work order.
SKIP_REASONS = {
    "pagination": ("manual", "FLAG", "agency", "Theme template edit: emit the archive root for page 1 (WordPress paginate_links does by default). Diff by hand."),
    "template": ("manual", "FLAG", "agency", "Theme template edit; diff by hand."),
    "homepage": ("redirect-rules", "decide", "client", "Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order."),
    "author archive": ("indexation-review", "APPROVE", "agency", "Yoast > Search Appearance > Archives: disable author archives (or the author sitemap); one setting removes them all."),
    "off-site": ("manual", "decide", "client", "Confirm the off-site redirect is meant; if yes, nothing to do."),
    "intentional": ("manual", "decide", "client", "Confirm the redirect is meant; if yes, nothing to do."),
    "pasted file path": ("fix-images", "APPROVE", "agency", "Re-upload the post's image to the media library and replace the src by hand (fix-images lists it as a broken/redirected image)."),
    "host variant": "skip",
    "query-string": ("redirect-rules", "decide", "agency", "Query-string redirects: decide whether the parameter URLs should link straight to the target or be left (tracking links usually are)."),
}

def skill_rows(client):
    """Items the built skills routed to a human. Parsed from the newest report of each; a skill that writes *-workorders.json is read as-is."""
    slug = client["slug"]; provider = provider_of(client); rdir = ROOT / "reports" / slug; cdir = ROOT / "changes" / provider / slug
    rows = []
    # 1. fix-redirect-links: skipped URLs, grouped by reason
    m = newest([(rdir, "redirect-map-*.json")])
    if m:
        d = json.loads(m.read_text(encoding="utf-8")); groups = {}
        for s in d.get("skipped") or []:
            reason = (s.get("reason") or "skipped").split(";")[0].strip()
            g = groups.setdefault(reason, []); g.append((path_of(s["old"]), int(s.get("links") or 0)))
        for reason, items in groups.items():
            items.sort(key=lambda x: -x[1])
            k = SKIP_REASONS.get(next((key for key in SKIP_REASONS if key in reason), None))
            if k is None: k = ("manual", "decide", "agency", "fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave.")
            if k == "skip": continue
            handler, tier, dec, what = k
            rows.append({"id": "redirect-links:" + slugify(reason)[:40], "issue": f"Links to redirect, skipped by fix-redirect-links: {reason}",
                         "handler": handler, "tier": tier, "urls_affected": len(items), "traffic_at_stake": 0,
                         "traffic_note": "", "what_to_do": what, "examples": [(p, n, "links") for p, n in items[:EXAMPLES]], "decider": dec, "importance": "", "source": m.name})
    # 2. fix-redirect-links: wp_options rows still holding old URLs (widgets, menus, theme settings)
    o = newest([(cdir, "*-fix-redirect-links-live-options.md"), (cdir, "*-fix-redirect-links-staging-options.md")]) if cdir.exists() else None
    if o:
        lines = [l for l in o.read_text(encoding="utf-8").splitlines() if l.startswith("| ") and not l.startswith("| option") and not set(l) <= set("|- ")]
        opts = [l.split("|")[1].strip().strip("`") for l in lines]
        if opts:
            rows.append({"id": "redirect-links:wp-options", "issue": "wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings)",
                         "handler": "manual", "tier": "FLAG", "urls_affected": len(opts), "traffic_at_stake": 0, "traffic_note": "",
                         "what_to_do": f"Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in {o.name}.",
                         "examples": [(x, 0, "") for x in opts[:EXAMPLES]], "decider": "agency", "importance": "", "source": o.name})
    # 3. fix-images: product-alt exceptions
    e = newest([(cdir, "*-fix-images-product-alt-exceptions.csv")]) if cdir.exists() else None
    if e:
        ex = list(csv.DictReader(e.open(encoding="utf-8-sig")))
        if ex:
            rows.append({"id": "fix-images:product-alt-exceptions", "issue": "Product images whose alt text needs a human (shared model photos, one-word titles)",
                         "handler": "fix-images", "tier": "APPROVE", "urls_affected": len(ex), "traffic_at_stake": 0, "traffic_note": "",
                         "what_to_do": "Fill new_alt on the 'alt text' tab (rows keyed product-attachment:<id>) or in the exception CSV, then fix-images --alt-apply.",
                         "examples": [(r.get("file", ""), int(r.get("used_by_products") or 0), "products") for r in ex[:EXAMPLES]], "decider": "agency", "importance": "", "source": e.name})
    # 4. fix-meta: rows it routed elsewhere
    mj = newest([(rdir, "meta-*.json")])
    if mj:
        q = (json.loads(mj.read_text(encoding="utf-8")).get("queue") or {}); routed = q.get("routed") or []
        if isinstance(routed, dict): routed = [dict(v, path=k) if isinstance(v, dict) else {"path": k, "route": str(v)} for k, v in routed.items()]
        groups = {}
        for r in routed:
            key = (r.get("route") or r.get("to") or r.get("action") or "routed")
            groups.setdefault(key, []).append(r.get("path") or path_of(r.get("url") or ""))
        for key, paths in groups.items():
            if "archive" in key or "indexation" in key: continue      # the archive decision is already a decide row from the crawl
            rows.append({"id": "fix-meta:" + slugify(str(key))[:40], "issue": f"Pages fix-meta routed to {key}", "handler": str(key), "tier": "FLAG",
                         "urls_affected": len(paths), "traffic_at_stake": 0, "traffic_note": "", "what_to_do": "See the fix-meta report's 'Routed elsewhere' section.",
                         "examples": [(p, 0, "") for p in paths[:EXAMPLES]], "decider": "agency", "importance": "", "source": mj.name})
    # 5. any skill that writes the shared JSON format
    for f in sorted(list(rdir.glob(WORKORDERS_JSON)) + (list(cdir.glob(WORKORDERS_JSON)) if cdir.exists() else [])):
        try: d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as ex2: log(f"  {f.name}: unreadable ({ex2})"); continue
        for it in d.get("items") or []:
            rows.append({"id": it["id"], "issue": it.get("issue", it["id"]), "handler": it.get("handler") or d.get("skill", "manual"), "tier": it.get("tier", "FLAG"),
                         "urls_affected": len(it.get("urls") or []), "traffic_at_stake": int(it.get("traffic") or 0), "traffic_note": "",
                         "what_to_do": it.get("what_to_do", ""), "examples": [(path_of(u), 0, "") for u in (it.get("urls") or [])[:EXAMPLES]],
                         "decider": it.get("decider", "agency"), "importance": "", "source": f.name})
    # one row per id: the newest source wins
    seen = {}
    for r in rows: seen[r["id"]] = r
    return list(seen.values())

TIER_ORDER = {"decide": 0, "FLAG": 1, "APPROVE": 2, "AUTO": 3}
def sort_rows(rows): return sorted(rows, key=lambda r: (-r["traffic_at_stake"], TIER_ORDER.get(r["tier"].split()[0], 9), -r["urls_affected"], r["id"]))

# ---------- report ----------
def ex_text(r, sep="\n"):
    return sep.join(f"{p}" + (f"  ({t} {u})" if t else "") for p, t, u in r["examples"]) + (sep + f"… {r['urls_affected'] - len(r['examples'])} more" if r["urls_affected"] > len(r["examples"]) else "")

def write_report(client, crawl, health, rows, skipped, n_issues):
    slug = client["slug"]; out = ROOT / "reports" / slug; out.mkdir(parents=True, exist_ok=True)
    decide = [r for r in rows if r["tier"].startswith("decide")]
    briefs = [r for r in decide if r["decider"] == "client"]
    lines = [f"# Work orders: {client['domain']}", "",
             f"Ahrefs Site Audit project {client['ahrefs']['site_audit_project_id']} · crawl {crawl} · health {health} · {n_issues} active issue types → {len(rows)} work orders"
             f" ({len(decide)} decisions, {len([r for r in rows if 'skill pending' in r['tier']])} waiting on a skill not yet built) · generated {today()}", "",
             "Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. "
             "Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. "
             "Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.", ""]
    if not rows: lines += ["Nothing needs a human on this crawl.", ""]
    else:
        lines += ["| # | item | goes to | tier | URLs | traffic | decider | what to do |", "|---|---|---|---|---|---|---|---|"]
        for n, r in enumerate(rows, 1):
            lines.append(f"| {n} | {r['issue']} | {r['handler']} | {r['tier']} | {r['urls_affected']} | {r['traffic_at_stake']}{r['traffic_note']} | {r['decider']} | {r['what_to_do']} |")
        lines += ["", "## Per item", ""]
        for n, r in enumerate(rows, 1):
            lines += [f"### {n}. {r['issue']}", "", f"`{r['id']}` · {r['handler']} · {r['tier']} · decider: {r['decider']}" + (f" · source: {r['source']}" if r['source'] != 'ahrefs' else ""), "",
                      r["what_to_do"], ""] + [f"- `{p}`" + (f" ({t} {u})" if t else "") for p, t, u in r["examples"]] + ([f"- … {r['urls_affected'] - len(r['examples'])} more in Ahrefs"] if r["urls_affected"] > len(r["examples"]) else []) + [""]
    if briefs:
        lines += ["## Client briefs", "", "One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.", ""]
        for r in briefs:
            lines += [f"**{r['issue']}** ({r['urls_affected']} page{'s' if r['urls_affected'] != 1 else ''}: " + ", ".join(p for p, _, _ in r["examples"][:4]) + (", …" if r["urls_affected"] > 4 else "") + ")",
                      "", brief_for(r, client), ""]
    if skipped:
        lines += ["## Skipped on purpose", ""] + [f"- {n} ({c}): {why}" for n, c, why in skipped] + [""]
    recorded = ((client.get("rules") or {}).get("decisions") or [])
    if recorded: lines += ["## Decisions already on file", "", "Rows with a decision here are left off the list above; delete the line from `rules.decisions` to reopen one.", ""] + [f"- {d}" for d in recorded] + [""]
    (out / f"work-orders-{crawl}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out / f"work-orders-{crawl}.json").write_text(json.dumps({"slug": slug, "domain": client["domain"], "crawl": crawl, "health": health, "generated": today(),
                                                                "rows": rows, "skipped": skipped}, indent=1, ensure_ascii=False), encoding="utf-8")
    return out / f"work-orders-{crawl}.md"

def brief_for(r, client):
    name = client.get("name") or client["domain"]; n = r["urls_affected"]
    if r["id"] in ("issue:hidden-pages-confirm-intent",) or r["id"].startswith("issue:noindex") or r["id"].startswith("issue:nofollow-page"):
        return (f"{n} page{'s' if n != 1 else ''} on {client['domain']} {'are' if n != 1 else 'is'} set so Google does not index {'them' if n != 1 else 'it'} (or does not follow {'their' if n != 1 else 'its'} links). "
                "That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; "
                "(b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.")
    if "blocked" in r["id"] or "training-bot" in r["id"]:
        return (f"Some AI crawlers are blocked from {client['domain']}. Allowing AI search bots (ChatGPT, Perplexity, Claude search) lets those tools cite the site in their answers; "
                "allowing training bots (GPTBot, ClaudeBot, Google-Extended) puts the content into future models. Our default is allow both; blocking training bots does not affect Google Search. "
                "Tell us if you want training bots blocked and we will set it.")
    if r["id"].startswith("issue:orphan"):
        return (f"{n} page{'s' if n != 1 else ''} on the site are not linked from any other page, so visitors and Google only find them through the sitemap. "
                "For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.")
    if r["id"].startswith("redirect-links") and "off-site" in r["id"]:
        return (f"One link on {client['domain']} ({r['examples'][0][0]}) sends visitors to another website. If that is intended, say so and we leave it; if not, tell us where it should go.")
    if "home" in r["id"] and r["id"].startswith("redirect-links"):
        return (f"{n} old URL{'s' if n != 1 else ''} on {client['domain']} currently redirect to the homepage, which loses visitors who click an old link. "
                "For each one we need the page it should go to now (or confirmation that nothing replaces it, in which case we remove the links).")
    if r["decider"] == "client":
        return f"{name}: {r['what_to_do']} ({n} page{'s' if n != 1 else ''} affected.) Our recommendation is in the sheet; reply with your call and we will do the rest."
    return f"Agency call: {r['what_to_do']}"

# ---------- sheet ----------
def sheet_id(client, key="alt_sheet_id"):
    sid = ((client.get("review") or {}).get(key) or "").strip()
    return sid if sid and sid != "unknown" else ""

def open_tab(sh, cols, tab=TAB):
    try: ws = sh.worksheet(tab)
    except Exception:
        ws = sh.add_worksheet(tab, rows=200, cols=len(cols)); ws.append_row(cols); ws.freeze(rows=1); return ws, [cols]
    vals = ws.get_all_values(); head = vals[0] if vals else []
    if head != cols:
        if not any(r for r in vals[1:] if any(r)): ws.clear(); ws.update("A1", [cols], value_input_option="RAW"); ws.freeze(rows=1); vals = [cols]
        else: sys.exit(f"'{tab}' tab has unexpected columns {head}; expected {cols}")
    return ws, vals

def push_sheet(client, crawl, rows):
    from review_sheets import gc
    sid = sheet_id(client)
    if not sid: return f"no review sheet (review.alt_sheet_id) for {client['slug']}; run review_sheets.py setup"
    g = gc(); sh = g.open_by_key(sid); ws, vals = open_tab(sh, COLS)
    existing = {r[0]: (i + 2, r + [""] * (len(COLS) - len(r))) for i, r in enumerate(vals[1:]) if r and r[0]}
    stamp = f"{today()} (crawl {crawl})"; updates, appends = [], []
    for r in sort_rows(rows):
        vals_new = [r["id"], r["issue"], r["handler"], r["tier"], r["urls_affected"], f"{r['traffic_at_stake']}{r['traffic_note']}", r["what_to_do"], ex_text(r), r["decider"]]
        if r["id"] in existing:
            rownum, old = existing[r["id"]]
            updates.append((rownum, vals_new + [old[9], old[10] or "open", old[11], old[12] or today(), stamp, ""]))   # back from cleared if it returned
        else:
            appends.append(vals_new + ["", "open", "", today(), stamp, ""])
    live = {r["id"] for r in rows}
    for rid, (rownum, old) in existing.items():
        if rid not in live and not old[14]:
            updates.append((rownum, old[:13] + [stamp, today()]))
    for rownum, v in updates: ws.update(range_name=f"A{rownum}:O{rownum}", values=[v], value_input_option="RAW")
    if appends: ws.append_rows(appends, value_input_option="RAW")
    return f"{len(appends)} added, {len(updates)} updated on '{TAB}' ({sh.url})"

def pull_decisions(client, apply=True):
    """status 'done' + decision_or_note starting 'decision:' -> rules.decisions in the client file (text edit, comments kept)."""
    from review_sheets import gc
    sid = sheet_id(client)
    if not sid: return "no review sheet"
    sh = gc().open_by_key(sid)
    try: ws = sh.worksheet(TAB)
    except Exception: return f"no '{TAB}' tab yet"
    vals = ws.get_all_values()
    found = []
    for r in vals[1:]:
        r = r + [""] * (len(COLS) - len(r))
        if r[10].strip().lower() in ("done", "won't fix", "wont fix") and r[11].strip().lower().startswith("decision:"):
            found.append(f"{today()} {r[0]}: {r[11].strip()[9:].strip()}")
    if not found: return "no decisions on the sheet"
    p = ROOT / "clients" / f"{client['slug']}.yaml"; s = p.read_text(encoding="utf-8")
    have = (client.get("rules") or {}).get("decisions") or []
    new = [d for d in found if not any(d.split(" ", 1)[1] == h.split(" ", 1)[1] for h in have if " " in h)]
    if not new: return f"{len(found)} decision(s) already recorded"
    entries = "".join(f"    - {json.dumps(d)}\n" for d in new)
    if re.search(r"^  decisions:\s*$", s, re.M): s = re.sub(r"^(  decisions:\s*\n)", r"\1" + entries.replace("\\", "\\\\"), s, count=1, flags=re.M)
    elif re.search(r"^  decisions:\s*\[\]", s, re.M): s = re.sub(r"^  decisions:\s*\[\].*$", "  decisions:\n" + entries.rstrip("\n"), s, count=1, flags=re.M)
    elif re.search(r"^rules:\s*$", s, re.M): s = re.sub(r"^(rules:\s*\n)", r"\1  decisions:   # written by work_orders.py --decisions; skills read these before asking\n" + entries.replace("\\", "\\\\"), s, count=1, flags=re.M)
    else: s = s.rstrip("\n") + "\nrules:\n  decisions:\n" + entries
    if apply: p.write_text(s, encoding="utf-8")
    return f"{len(new)} decision(s) {'written to' if apply else 'would be written to'} clients/{client['slug']}.yaml"

# ---------- roster ----------
def roster(args):
    rows = []
    for p in sorted((ROOT / "clients").glob("*.yaml")):
        if p.name.startswith("_"): continue
        files = sorted((ROOT / "reports" / p.stem).glob("work-orders-*.json"))
        if not files: continue
        d = json.loads(files[-1].read_text(encoding="utf-8"))
        for r in d["rows"]: rows.append(dict(r, client=p.stem, crawl=d["crawl"]))
    rows = sorted(rows, key=lambda r: (-r["traffic_at_stake"], TIER_ORDER.get(r["tier"].split()[0], 9), r["client"], r["id"]))
    per = {}
    for r in rows:
        c = per.setdefault(r["client"], {"rows": 0, "decide": 0, "traffic": 0, "crawl": r["crawl"]})
        c["rows"] += 1; c["decide"] += r["tier"].startswith("decide"); c["traffic"] += r["traffic_at_stake"]
    out = ROOT / "reports" / "_roster"; out.mkdir(parents=True, exist_ok=True)
    lines = [f"# Work orders: roster", "", f"Generated {today()} from the newest `reports/<slug>/work-orders-*.json` of {len(per)} clients · {len(rows)} open items", "",
             "## By client", "", "| client | crawl | items | decisions | traffic at stake |", "|---|---|---|---|---|"]
    lines += [f"| {c} | {v['crawl']} | {v['rows']} | {v['decide']} | {v['traffic']} |" for c, v in sorted(per.items(), key=lambda kv: -kv[1]["traffic"])]
    lines += ["", "## All items, by traffic at stake", "", "| client | item | goes to | tier | URLs | traffic | decider |", "|---|---|---|---|---|---|---|"]
    lines += [f"| {r['client']} | {r['issue']} | {r['handler']} | {r['tier']} | {r['urls_affected']} | {r['traffic_at_stake']}{r['traffic_note']} | {r['decider']} |" for r in rows]
    f = out / f"work-orders-{today()}.md"; f.write_text("\n".join(lines) + "\n", encoding="utf-8"); print(f"Roster: {f}")
    if args.sheet:
        from review_sheets import gc
        ag = ROOT / "clients" / "_agency.yaml"
        c = yaml.safe_load(ag.read_text(encoding="utf-8")) if ag.exists() else {}
        sid = sheet_id(c or {}, "agency_sheet_id")
        if not sid: print("no agency sheet: put its id in clients/_agency.yaml under review.agency_sheet_id (a blank sheet 'LHF work orders' in the shared folder)"); return
        cols = ["client"] + COLS[:9] + ["status", "opened"]
        sh = gc().open_by_key(sid); ws, _ = open_tab(sh, cols)
        ws.clear(); ws.update("A1", [cols] + [[r["client"], r["id"], r["issue"], r["handler"], r["tier"], r["urls_affected"], f"{r['traffic_at_stake']}{r['traffic_note']}",
                                                r["what_to_do"], ex_text(r), r["decider"], "", r["crawl"]] for r in rows], value_input_option="RAW"); ws.freeze(rows=1)
        try: cw = sh.worksheet("by client")
        except Exception: cw = sh.add_worksheet("by client", rows=100, cols=5)
        cw.clear(); cw.update("A1", [["client", "crawl", "items", "decisions", "traffic at stake"]] + [[c, v["crawl"], v["rows"], v["decide"], v["traffic"]] for c, v in sorted(per.items(), key=lambda kv: -kv[1]["traffic"])], value_input_option="RAW")
        print(f"Agency sheet: {sh.url} ({len(rows)} rows; the roster tab is rebuilt each run, per-client tabs keep their status)")

# ---------- main ----------
def run_one(slug, args, handlers, by_id):
    client = load_client(slug)
    pid = (client.get("ahrefs") or {}).get("site_audit_project_id")
    if not pid or pid == "unknown": print(f"{slug}: no Ahrefs project"); return
    api = Api(slug, args.cache)
    try: pid, crawl, health, issues = pull(client, api)
    except SystemExit as e: print(f"{slug}: {e}"); return
    rows, skipped = issue_rows(client, api, handlers, by_id, pid, crawl, issues)
    rows = sort_rows(rows + skill_rows(client))
    decided = {d.split(" ", 2)[1].rstrip(":") for d in ((client.get("rules") or {}).get("decisions") or []) if len(d.split(" ", 2)) > 1}
    rows = [r for r in rows if r["id"] not in decided]          # a recorded decision closes the row until someone deletes it from the client file
    report = write_report(client, crawl, health, rows, skipped, len(issues))
    print(f"{slug}: crawl {crawl}, health {health}, {len(issues)} active issue types -> {len(rows)} work orders ({len([r for r in rows if r['tier'].startswith('decide')])} decisions) · {report.relative_to(ROOT)}")
    if args.sheet: print("  sheet:", push_sheet(client, crawl, rows))
    if args.decisions: print("  decisions:", pull_decisions(client))

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--all", action="store_true", help="every client file with an Ahrefs project id")
    ap.add_argument("--roster", action="store_true", help="roster view from the newest per-client JSONs (run the clients first)")
    ap.add_argument("--sheet", action="store_true", help="upsert the 'work orders' tab (client sheet; with --roster, the agency sheet)")
    ap.add_argument("--decisions", action="store_true", help="copy 'decision:' notes from done rows on the sheet into clients/<slug>.yaml")
    ap.add_argument("--cache", action="store_true", help="keep/reuse raw Ahrefs responses in tmp/ahrefs-cache/<slug>/")
    args = ap.parse_args()
    load_env()
    if args.roster: roster(args); return
    handlers, by_id = load_routes()
    if args.all:
        for p in sorted((ROOT / "clients").glob("*.yaml")):
            if not p.name.startswith("_"): run_one(p.stem, args, handlers, by_id)
    elif args.slug: run_one(args.slug, args, handlers, by_id)
    else: ap.error("give a slug, --all or --roster")

if __name__ == "__main__":
    main()
