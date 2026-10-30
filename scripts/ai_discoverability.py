#!/usr/bin/env python3
"""Report and tune how a site is seen by AI search and training crawlers, from Ahrefs Site Audit's
"AI Discoverability" category plus the site's public robots.txt.

    python scripts/ai_discoverability.py <slug>                      # report -> reports/<slug>/ai-discoverability-<crawl>.md
                                                                     # (+ proposed robots.txt when the client policy differs from what is live)
    python scripts/ai_discoverability.py <slug> --probe              # same, plus an SSH look at live: robots.txt file vs virtual, IndexNow plugin state
    python scripts/ai_discoverability.py <slug> --apply-robots       # dry: show the diff, check whether the target serves a file or WordPress's virtual robots.txt
    python scripts/ai_discoverability.py <slug> --apply-robots --apply                       # write robots.txt on staging (backup + change log)
    python scripts/ai_discoverability.py <slug> --apply-robots --target live --apply [--yes] # same on live; type the slug to confirm
    python scripts/ai_discoverability.py --all                       # roster: docs/ai-bot-policy.md, one row per client with an Ahrefs project

Read-and-route by design. The only write this script can make is the robots.txt file (APPROVE tier: the client has to
decide the policy first, in clients/<slug>.yaml under `ai:`). Everything else in the report is routed to another skill
or flagged for a human. Needs AHREFS_API_KEY in the environment or .env at the repo root (reuses build_redirect_map's helpers).

`--cache` keeps the raw Ahrefs responses in tmp/ahrefs-cache/<slug>/ and reuses them on the next run, so the report can be
re-rendered without spending API units. `--robots-file <path>` uses a saved copy of robots.txt instead of fetching it (offline runs).

Ahrefs' `indexnow_status` column is about Ahrefs' OWN auto-submission (a Site Audit crawl setting that needs an IndexNow key file
hosted at the site root), not about the site's SEO plugin pinging IndexNow on publish. The report keeps the two apart; `--probe`
checks the plugin side over SSH.
"""
import argparse, datetime, difflib, json, re, subprocess, sys, urllib.error, urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from build_redirect_map import load_env, ahrefs, UA, norm_host  # noqa: E402

CATEGORY = "AI Discoverability"
SKIP_PLUGINS = "handl-utm-grabber-v3"
SAMPLE_SELECT = ("url,traffic,http_code,page_is_noindex,allowed_search_bots,blocked_search_bots,allowed_training_bots,"
                 "blocked_training_bots,robots_error,robots_sitemaps,http_header_robots,meta_robots,indexnow_status,indexnow_reason")
ISSUE_SELECT = ("url,traffic,http_code,is_rendered,size_uncompressed,time_to_first_byte,loading_time,ai_content_level,"
                "jsonld_schema_types,ml_page_types,blocked_search_bots,blocked_training_bots")
# Indexable HTML pages only. http_code alone lets images, CSS and JS through (they carry bot columns too) and they would crowd
# out real pages in a traffic-sorted sample.
SAMPLE_WHERE = json.dumps({"and": [{"field": "http_code", "is": ["eq", 200]}, {"field": "is_html", "is": ["eq", True]},
                                   {"field": "page_is_noindex", "is": ["eq", False]}]})
JS_WIDGET_PLUGINS = ("reviews", "feed", "instagram", "sby", "testimonial", "elfsight", "trustindex", "widget")
INDEXNOW_PLUGINS = {"indexnow": "IndexNow (Microsoft Bing, free)", "fast-indexing-api": "Rank Math Instant Indexing (free)",
                    "aioseo-index-now": "AIOSEO IndexNow addon", "wordpress-seo-premium": "Yoast SEO Premium (IndexNow built in, on by default)"}
MARK_START = "# --- AI crawler policy: managed by ai-discoverability (edit clients/<slug>.yaml, not this block) ---"
MARK_END = "# --- end AI crawler policy ---"

# Fallback universe if a crawl returns no bot columns. The live lists come from Ahrefs' own classification
# (allowed_* + blocked_* on the sampled pages), so these only matter for a site Ahrefs has never crawled.
SEARCH_BOTS_FALLBACK = ["Amazonbot", "Amzn-SearchBot", "Amzn-User", "Applebot", "ChatGPT-User", "Claude-SearchBot", "Claude-User",
                        "Claude-Web", "DuckAssistBot", "GitHubCopilotChat", "Google-Agent", "Googlebot", "MistralAI-User",
                        "OAI-SearchBot", "Perplexity-User", "PerplexityBot", "YouBot"]
TRAINING_BOTS_FALLBACK = ["Applebot-Extended", "ClaudeBot", "DeepseekBot", "GPTBot", "Google-Extended", "Meta-ExternalAgent",
                          "anthropic-ai", "xAI-Bot"]
NEVER_BLOCK = {"googlebot"}   # blocking Googlebot removes the page from Search itself, AI Overviews included

# Where each AI Discoverability check goes. (skill, tier, one-line reason)
ROUTES = {
    "Indexable page blocked from all AI search bots":  ("ai-discoverability", "APPROVE", "robots.txt policy; compare with the client's `ai:` block"),
    "Indexable page blocked from some AI search bots": ("ai-discoverability", "APPROVE", "robots.txt policy; compare with the client's `ai:` block"),
    "Inconsistent AI training bot policy":             ("ai-discoverability", "APPROVE", "robots.txt groups disagree; one managed block fixes it"),
    "Main content requires JavaScript rendering":      ("theme/plugin (by hand)", "FLAG", "the plugin or widget rendering the main copy client-side needs server-side output or fallback text"),
    "Slow server response for AI crawlers":            ("hosting/cache", "FLAG", "TTFB, not a crawl fix; check server cache and the host's APM"),
    "Page size exceeds 2 MB crawl limit":              ("fix-images", "AUTO", "page weight; images are almost always the cause"),
    "Similar AI-generated content":                    ("content (Phase 4)", "FLAG", "near-duplicate generated copy; rewrite or consolidate"),
    "Article page missing Article schema":             ("schema-check", "FLAG", "Ahrefs' ML classed the page as an article; Yoast emits Article only for posts"),
    "Category page missing ItemList schema":           ("schema-check", "FLAG", "archive/listing page without ItemList"),
    "FAQ page missing FAQPage schema":                 ("schema-check", "FLAG", "FAQ rich results are gone from Google (2026-05-07); add FAQPage only if it matches visible Q&A and the client wants it for other engines"),
    "Organization schema missing or incomplete":       ("schema-check", "FLAG", "usually the homepage; the SEO plugin's Organization settings (name, logo, sameAs) fill it"),
    "Product page missing Product schema":             ("schema-check", "FLAG", "WooCommerce emits Product; a non-Woo product page needs the SEO plugin's schema type set"),
}

def log(*a): print(*a, file=sys.stderr)
def yn(v): return {True: "yes", False: "no"}.get(v, str(v))

# ---------- Ahrefs with optional cache ----------
class Api:
    def __init__(self, slug, cache):
        self.dir = ROOT / "tmp" / "ahrefs-cache" / slug if cache else None
        if self.dir: self.dir.mkdir(parents=True, exist_ok=True)
    def get(self, name, path, **params):
        f = self.dir / f"{name}.json" if self.dir else None
        if f and f.exists():
            return json.loads(f.read_text(encoding="utf-8"))
        data = ahrefs(path, **params)
        if f: f.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        return data

def fetch_text(url, timeout=15):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/plain,*/*"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace"), r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, "", url
    except Exception as e:
        return f"error: {type(e).__name__}", "", url

# ---------- robots.txt model ----------
def parse_robots(text):
    """Split robots.txt into (preamble_lines, groups, trailing_lines). A group = {"agents": [...], "lines": [...raw rule lines...]}.
    Comments and blank lines travel with whatever they sit next to; nothing is reflowed, so the diff shows only real changes."""
    groups, pre, cur, pending = [], [], None, []
    for raw in text.splitlines():
        line = raw.rstrip()
        m = re.match(r"^\s*user-agent\s*:\s*(.*?)\s*(#.*)?$", line, re.I)
        if m:
            if cur is None or cur["lines"]:          # a new group starts after the previous one has rules
                if cur: groups.append(cur)
                cur = {"agents": [], "lines": [], "lead": pending, "raw_agents": []}; pending = []
            cur["agents"].append(m.group(1))
            cur["raw_agents"] += pending + [line]; pending = []
            continue
        if cur is None:
            pre.append(line)
        elif line.strip() == "" or line.lstrip().startswith("#"):
            pending.append(line)                     # held until we know whether a new group follows
        else:
            cur["lines"] += pending + [line]; pending = []
    if cur: groups.append(cur)
    return pre, groups, pending

def render_robots(pre, groups, tail):
    out = list(pre)
    for g in groups:
        out += g.get("lead", []) + g.get("raw_agents", [f"User-agent: {a}" for a in g["agents"]]) + g["lines"]
    out += tail
    return "\n".join(out).rstrip() + "\n"

def strip_managed(text):
    """Remove an earlier managed block, by its markers."""
    if MARK_START not in text: return text
    pattern = re.escape(MARK_START) + r".*?" + re.escape(MARK_END) + r"\n?"
    return re.sub(pattern, "", text, flags=re.S)

def build_robots(current, blocked, universe):
    """Return the new robots.txt: current text minus any group that only addresses managed AI bots, plus one managed block
    disallowing `blocked`. Allowed bots get no group of their own, so they inherit `User-agent: *` like any other crawler."""
    base = strip_managed(current)
    pre, groups, tail = parse_robots(base)
    uni = {u.lower() for u in universe}
    kept = [g for g in groups if not all(a.lower() in uni for a in g["agents"])]
    text = render_robots(pre, kept, tail) if (pre or kept or tail) else ""
    if blocked:
        block = [MARK_START] + [f"User-agent: {b}" for b in blocked] + ["Disallow: /", MARK_END]
        text = text.rstrip("\n") + ("\n\n" if text.strip() else "") + "\n".join(block) + "\n"
    return text

def effective_policy(ai, universe_search, universe_training):
    """Return (blocked set, undecided bool, notes) from the client's ai: block."""
    notes = []
    if not ai: return set(), True, ["no `ai:` block in the client file"]
    s, t = str(ai.get("search_bots", "unknown")).lower(), str(ai.get("training_bots", "unknown")).lower()
    undecided = s not in ("allow", "block") or t not in ("allow", "block")
    blocked = set()
    if s == "block": blocked |= set(universe_search)
    if t == "block": blocked |= set(universe_training)
    for b in ai.get("exceptions") or []:
        if b in blocked: blocked.discard(b); notes.append(f"exception: {b} allowed")
        else: blocked.add(b); notes.append(f"exception: {b} blocked")
    for b in list(blocked):
        if b.lower() in NEVER_BLOCK:
            blocked.discard(b); notes.append(f"{b} is never blocked by this skill (it would remove the site from Google Search)")
    return blocked, undecided, notes

# ---------- data pull ----------
def pull(client, api, sample_limit=40):
    pid = client["ahrefs"]["site_audit_project_id"]
    proj = api.get("project", "site-audit/projects", project_id=pid)
    hs = (proj.get("healthscores") or [{}])[0]
    crawl = (hs.get("date") or "")[:10] or datetime.date.today().isoformat()
    issues = [i for i in api.get("issues", "site-audit/issues", project_id=pid).get("issues", []) if i.get("category") == CATEGORY]
    sample = api.get("sample", "site-audit/page-explorer", project_id=pid, select=SAMPLE_SELECT, order_by="traffic:desc",
                     limit=sample_limit, where=SAMPLE_WHERE).get("pages", [])
    per_issue = {}
    for i in issues:
        if (i.get("crawled") or 0) > 0:
            per_issue[i["name"]] = api.get("issue-" + re.sub(r"\W+", "-", i["name"]).lower(), "site-audit/page-explorer", project_id=pid,
                                           issue_id=i["issue_id"], select=ISSUE_SELECT, order_by="traffic:desc", limit=200).get("pages", [])
    return {"pid": pid, "crawl": crawl, "health": hs.get("health_score"), "issues": issues, "sample": sample, "per_issue": per_issue}

def universe_from(sample):
    s, t = set(), set()
    for p in sample:
        s |= set(p.get("allowed_search_bots") or []) | set(p.get("blocked_search_bots") or [])
        t |= set(p.get("allowed_training_bots") or []) | set(p.get("blocked_training_bots") or [])
    return sorted(s) or SEARCH_BOTS_FALLBACK, sorted(t) or TRAINING_BOTS_FALLBACK

def observed_blocks(sample):
    """Bots blocked on every sampled page vs. only some (an 'inconsistent' policy)."""
    if not sample: return [], [], [], []
    def tally(key):
        counts = {}
        for p in sample:
            for b in p.get(key) or []: counts[b] = counts.get(b, 0) + 1
        every = sorted(b for b, c in counts.items() if c == len(sample)); some = sorted(b for b, c in counts.items() if c < len(sample))
        return every, some
    se, ss = tally("blocked_search_bots"); te, ts = tally("blocked_training_bots")
    return se, ss, te, ts

# ---------- report ----------
def md_url(u): return f"`{urllib_path(u)}`"
def urllib_path(u):
    from urllib.parse import urlsplit
    p = urlsplit(u); return (p.path or "/") + (("?" + p.query) if p.query else "")

def write_report(client, data, robots_status, robots_text, proposed, blocked_policy, undecided, policy_notes, universe, probe=None):
    slug, host = client["slug"], client["domain"]
    sample, issues, per = data["sample"], data["issues"], data["per_issue"]
    us, ut = universe
    se, ss, te, ts = observed_blocks(sample)
    ai = client.get("ai") or {}
    out = [f"# AI discoverability: {host}", "",
           f"Ahrefs Site Audit project {data['pid']} · crawl {data['crawl']} · health {data.get('health')} · {len(sample)} indexable pages sampled (top by traffic) · "
           f"robots.txt source: " + (f"`{robots_status[5:]}` (saved copy)" if str(robots_status).startswith("file ") else f"`{client.get('canonical_host', 'https://'+host).rstrip('/')}/robots.txt` (HTTP {robots_status})"), "",
           "Mostly read-and-route. The only direct change this skill makes is the robots.txt policy block (APPROVE, after the client decides). "
           "Google's position, which this report follows: AI Overviews and AI Mode use Googlebot and need pages that are indexed and snippet-eligible; "
           "`Google-Extended` governs Gemini training and grounding, not Search; no AI-specific files or markup are needed.", ""]

    # 1. Bot access
    out += ["## 1. Bot access (robots.txt)", ""]
    pol_s, pol_t = str(ai.get("search_bots", "unknown")), str(ai.get("training_bots", "unknown"))
    out += [f"Client policy in `clients/{slug}.yaml`: search bots **{pol_s}**, training bots **{pol_t}**" +
            (f", exceptions {ai.get('exceptions')}" if ai.get("exceptions") else "") +
            (f" (decided by {ai.get('policy_confirmed_by')})" if ai.get("policy_confirmed_by") else "") + ".", ""]
    if undecided:
        out += ["**No decision on file.** This is a business call, so the skill stops here on bot access: allowing training bots trades content control for being in the models' "
                "knowledge; blocking them does not affect Google Search, AI Overviews, or any 'search' bot above. Default proposal: allow all search bots, decide training bots "
                "per client, never block Googlebot. Record the decision in the `ai:` block and rerun.", ""]
    for n in policy_notes: out.append(f"- {n}")
    if policy_notes: out.append("")
    out += ["| Bot | Class | Live (sampled pages) | Policy says | Action |", "|---|---|---|---|---|"]
    for b in us + ut:
        cls = "search" if b in us else "training"
        live = "blocked" if b in (se + te) else ("blocked on some pages" if b in (ss + ts) else "allowed")
        want = "undecided" if undecided else ("block" if b in blocked_policy else "allow")
        act = "-" if undecided else ("none" if (want == "block") == (live == "blocked") and live != "blocked on some pages" else ("add to managed block" if want == "block" else "remove its Disallow"))
        out.append(f"| {b} | {cls} | {live} | {want} | {act} |")
    robots_errs = sorted({str(p.get("robots_error")) for p in sample if p.get("robots_error")})
    sm = sorted({s for p in sample for s in (p.get("robots_sitemaps") or [])} | {m.strip() for m in re.findall(r"(?im)^\s*sitemap\s*:\s*(\S+)", robots_text)})
    hdr = sorted({str(h) for p in sample for h in (p.get("http_header_robots") or [])})
    out += ["", f"robots.txt errors reported by Ahrefs: {', '.join(robots_errs) if robots_errs else 'none'} · Sitemap lines: {', '.join('`'+s+'`' for s in sm) if sm else 'none'} · "
            f"X-Robots-Tag headers on sampled pages: {', '.join(hdr) if hdr else 'none'}", ""]
    out += ["Current robots.txt:", "", "```", (robots_text.strip() or "(empty or not fetched)"), "```", ""]
    if proposed is not None:
        diff = list(difflib.unified_diff(robots_text.splitlines(), proposed.splitlines(), "robots.txt (live)", "robots.txt (proposed)", lineterm=""))
        out += ["### Proposed robots.txt (APPROVE)", "",
                "Allowed bots get no group of their own so they inherit `User-agent: *` (robots groups do not inherit; a bot with its own group ignores the `*` rules). "
                f"Blocked bots sit in one managed block between markers, so a rerun replaces the block instead of stacking rules. Saved to `reports/{slug}/robots-proposed-{data['crawl']}.txt`; "
                f"apply with `python scripts/ai_discoverability.py {slug} --apply-robots --apply` (staging) then `--target live --apply`.", ""]
        out += ["```diff"] + (diff or ["(no textual change)"]) + ["```", ""]
    elif not undecided:
        out += ["Live robots.txt already matches the client policy. Nothing to change.", ""]

    # 2. Machine readability + schema + content: one table per issue with URLs
    out += ["## 2. Checks with pages behind them", ""]
    active = [i for i in issues if (i.get("crawled") or 0) > 0]
    if not active:
        out += ["No AI Discoverability check has any URL on this crawl.", ""]
    for i in active:
        name = i["name"]; skill, tier, why = ROUTES.get(name, ("human", "FLAG", "not in this skill's routing table yet"))
        pages = per.get(name, [])
        out += [f"### {name} ({i['crawled']}, {i.get('importance')}) → {skill} · {tier}", "", why[:1].upper() + why[1:] + ".", ""]
        if "JavaScript" in name:
            sus = [x for x in (client.get("platform", {}).get("plugins_seen") or []) + (client.get("platform", {}).get("plugins_active") or []) if any(k in x for k in JS_WIDGET_PLUGINS)]
            if sus: out += [f"Client-side widget plugins on this site (from the client file): {', '.join(sorted(set(sus)))}. One of these is the usual suspect; the fix is server-rendered output or static fallback text in the template.", ""]
        if name.startswith(("Indexable page blocked", "Inconsistent")):
            out += ["See section 1; the fix is the managed robots.txt block.", ""]
        cols = ["URL", "traffic"]
        if "JavaScript" in name: cols += ["rendered?"]
        if "Slow" in name: cols += ["TTFB ms", "load ms"]
        if "2 MB" in name: cols += ["uncompressed KB"]
        if "AI-generated" in name: cols += ["AI content level"]
        if "schema" in name: cols += ["JSON-LD types on page", "Ahrefs page type"]
        out += ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
        for p in pages[:60]:
            row = [md_url(p["url"]), str(int(p.get("traffic") or 0))]
            if "JavaScript" in name: row.append(str(p.get("is_rendered")))
            if "Slow" in name: row += [str(p.get("time_to_first_byte") or ""), str(p.get("loading_time") or "")]
            if "2 MB" in name: row.append(str(round((p.get("size_uncompressed") or 0) / 1024)))
            if "AI-generated" in name: row.append(str(p.get("ai_content_level") or ""))
            if "schema" in name: row += [", ".join(p.get("jsonld_schema_types") or []) or "none", str(p.get("ml_page_types") or "")]
            out.append("| " + " | ".join(row) + " |")
        if len(pages) > 60: out.append(f"| ... {len(pages) - 60} more | | |")
        out.append("")
    if any("schema" in i["name"] for i in active):
        out += ["Schema notes: these are Ahrefs' notices against its own page classification, not Google requirements. Google says no special structured data is needed to appear in AI features; "
                "the rule that matters is that any schema on the page describes what is visibly on the page. Organization schema is worth completing (name, logo, sameAs) through the SEO plugin. "
                "FAQPage no longer earns rich results in Google. Hand the list to `schema-check` with the existing validation-error work.", ""]

    # 3. IndexNow
    st = {}
    for p in sample: st[str(p.get("indexnow_status"))] = st.get(str(p.get("indexnow_status")), 0) + 1
    probe = probe or {}
    out += ["## 3. IndexNow (APPROVE)", "",
            "Google ignores IndexNow; Bing, Yandex, Naver and Seznam use it, and Bing's index feeds ChatGPT search and Copilot. Two separate things can submit URLs, and "
            "Ahrefs only reports on the first:", "",
            f"- **Ahrefs auto-submission** (Site Audit → Crawl settings → IndexNow): status on sampled pages {', '.join(f'`{k}` ×{v}' for k, v in sorted(st.items()))}. "
            "`Indexnow_off` means the crawl setting is off. Turning it on needs an IndexNow key file hosted at the site root and a project boost that includes the feature; "
            "then Ahrefs submits changed, new, redirected and removed pages after each crawl.",
            "- **The site pinging on publish**: Yoast SEO Premium (built in, on by default; not in free Yoast), Rank Math's Instant Indexing plugin, AIOSEO's IndexNow addon, "
            "or Microsoft's free `indexnow` plugin on anything else. This is the one that matters for fresh content, and Ahrefs cannot see it. " +
            (f"Probe over SSH ({probe.get('alias')}): " + (f"**{probe['indexnow']}**" if probe.get("indexnow") else "no IndexNow plugin active" +
             (f"; `wpseo.enable_index_now` = {probe['yoast_index_now']}" if probe.get("yoast_index_now") not in (None, "") else "")) + "."
             if probe.get("alias") else "Not probed (run with `--probe` to check the plugin list over SSH)."),
            "", f"Client file says `ai.indexnow: {yn(ai.get('indexnow', 'unknown'))}`. Recommended for the roster: Microsoft's `indexnow` plugin on free-Yoast sites "
            "(one key file, no settings), and the SEO plugin's own integration where it exists. Record the choice in `ai.indexnow` once it is live.", ""]
    if probe.get("alias"):
        out += [f"Probe also found robots.txt served as **{probe.get('robots_kind')}** on live" +
                (" (WordPress/Yoast generate it; a physical file written by `--apply-robots` takes over and carries the Sitemap line with it)." if probe.get("robots_kind") == "virtual" else "."), ""]

    # 4. Not recommended
    out += ["## 4. Not recommended, on purpose", "",
            "- **llms.txt**: Google Search does not read it, and large-scale studies have found no citation effect. Skip it; if a client insists, it is harmless but does nothing measurable.",
            "- **\"AI-specific\" schema or hidden content for AI**: Google needs none and treats hidden text as spam. Keep copy in the HTML as text; make schema match the page.",
            "- **Blocking Googlebot to stay out of AI Overviews**: removes the page from Search. Use `nosnippet`/`max-snippet` on a page if a client truly wants no AI preview, and expect it to cost regular snippets too.",
            "- **Chunking or rewriting content \"for AI\"**: the levers are the usual ones: indexable, snippet-eligible, fast, text in HTML, accurate schema, Business Profile current.", ""]

    # 5. Reconciliation
    out += ["## 5. Reconciliation", "", f"{CATEGORY} issue types in this crawl: {len(issues)} · with URLs: {len(active)} · zero: {len(issues) - len(active)}", ""]
    out += ["| Check | Importance | URLs | Route |", "|---|---|---|---|"]
    for i in issues:
        r = ROUTES.get(i["name"], ("human", "FLAG", ""))
        out.append(f"| {i['name']} | {i.get('importance')} | {i.get('crawled') or 0} | {r[0]} ({r[1]}) |")
    out.append("")

    # 6. Client file
    out += ["## 6. Client file", "", f"`clients/{slug}.yaml` → `ai.observed` was updated by this run (crawl, robots.txt kind if probed, blocked bots, IndexNow status). "
            "The policy fields (`search_bots`, `training_bots`, `exceptions`, `policy_confirmed_by`) are yours; the skill never writes them.", ""]
    out += ["## Sources", "",
            "- Google: AI features and your website https://developers.google.com/search/docs/appearance/ai-features",
            "- Google: AI optimization guide https://developers.google.com/search/docs/fundamentals/ai-optimization-guide",
            "- Google: robots meta tag / Google-Extended https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers",
            "- Ahrefs: AI Discoverability in Site Audit (feature announcement, Sept 2026) https://ahrefs.com/blog/new-features-september-2026/",
            "- Ahrefs: IndexNow in Site Audit https://help.ahrefs.com/en/articles/9317209-how-to-submit-pages-to-indexnow-within-site-audit",
            "- Yoast: IndexNow is a Premium feature https://yoast.com/yoast-seo-june-28-2022/",
            "- IndexNow https://www.indexnow.org/"]
    return "\n".join(out) + "\n"

# ---------- client file update ----------
def observed_from(data, sample):
    se, ss, te, ts = observed_blocks(sample)
    st = sorted({str(p.get("indexnow_status")) for p in sample})
    return {"crawl": data["crawl"], "blocked_search_bots": se + [b + " (some pages)" for b in ss],
            "blocked_training_bots": te + [b + " (some pages)" for b in ts], "indexnow_status": ", ".join(st) or "unknown"}

def update_client_observed(path, updates):
    """Merge `updates` into the ai.observed block and rewrite only that block, by text, so comments elsewhere in the YAML survive."""
    text = path.read_text(encoding="utf-8")
    current = ((yaml.safe_load(text) or {}).get("ai") or {}).get("observed") or {}
    obs = {**current, **updates}
    block = "  observed:                      # written by ai-discoverability; do not edit by hand\n" + \
            "".join(f"    {k}: {json.dumps(v) if isinstance(v, list) else v}\n" for k, v in obs.items())
    if re.search(r"^ai:\s*$", text, re.M):
        text = re.sub(r"^  observed:.*?(?=^\S|^  \w|\Z)", "", text, flags=re.S | re.M)   # drop old observed sub-block
        # insert observed at the end of the ai: block
        m = re.search(r"^ai:\s*\n((?:  .*\n|\s*\n)*)", text, re.M)
        end = m.end()
        rest = text[end:]
        text = text[:end].rstrip("\n") + "\n" + block + ("\n" if rest and not rest.startswith("\n") else "") + rest
    else:
        text = text.rstrip("\n") + "\n\nai:\n  search_bots: unknown          # allow | block: citations and live answers (ChatGPT, Perplexity, Claude, AI Overviews use Googlebot)\n" \
               "  training_bots: unknown        # allow | block: model training (GPTBot, ClaudeBot, Google-Extended ...)\n  exceptions: []                # bot names that flip the verdict above\n" \
               "  indexnow: unknown             # yes | no | unknown\n  policy_confirmed_by: \"\"       # who at the client decided, and when\n" + block
    path.write_text(text, encoding="utf-8")

# ---------- robots.txt apply over SSH ----------
def ssh(alias, cmd, inp=None):
    try:
        r = subprocess.run(["ssh", alias, cmd], input=inp.encode("utf-8") if inp else None, capture_output=True, timeout=120)
    except (OSError, subprocess.TimeoutExpired) as e:
        return 255, "", f"ssh {alias}: {e}"
    return r.returncode, r.stdout.decode("utf-8", "replace"), r.stderr.decode("utf-8", "replace")

def robots_kind(alias, webroot):
    code, out, err = ssh(alias, f"cd {webroot} && if [ -f robots.txt ]; then echo file; cat robots.txt; else echo virtual; wp --skip-plugins={SKIP_PLUGINS} eval 'do_robots();' 2>/dev/null; fi")
    if code != 0: return "unknown", "", err.strip()
    kind, _, body = out.partition("\n")
    return kind.strip(), body, ""

def live_alias_and_root(client, webroot="public"):
    hosting = client.get("hosting", {})
    alias = (hosting.get("ssh_alias") or "").split(",")[0].strip()
    if not alias or alias in ("unknown", "none"): return None, None
    provider = str(hosting.get("provider") or "other").lower()
    return alias, (f"sites/{alias}" if provider == "wpengine" and webroot == "public" else webroot)

def probe_site(client):
    """Over SSH on live: robots.txt file vs virtual, and which IndexNow mechanism (if any) the site has."""
    alias, webroot = live_alias_and_root(client)
    if not alias: return {"error": "no live SSH alias in the client file"}
    kind, body, err = robots_kind(alias, webroot)
    if kind == "unknown": return {"alias": alias, "error": err}
    code, out, _ = ssh(alias, f"cd {webroot} && wp --skip-plugins={SKIP_PLUGINS} plugin list --status=active --field=name 2>/dev/null; echo ---; "
                              f"wp --skip-plugins={SKIP_PLUGINS} option pluck wpseo enable_index_now 2>/dev/null")
    plugins, _, yoast_flag = out.partition("---")
    active = {p.strip() for p in plugins.splitlines() if p.strip()}
    found = [label for slug, label in INDEXNOW_PLUGINS.items() if slug in active]
    return {"alias": alias, "robots_kind": kind, "robots_body": body, "indexnow": ", ".join(found), "yoast_index_now": yoast_flag.strip()}

def apply_robots(args, client, proposed_path):
    hosting = client.get("hosting", {})
    alias = hosting.get("ssh_alias") if args.target == "live" else hosting.get("staging_environment")
    if not alias or alias in ("unknown", "none"): sys.exit(f"No {args.target} SSH alias in clients/{client['slug']}.yaml")
    alias = alias.split(",")[0].strip()
    provider = str(hosting.get("provider") or "other").lower()
    if provider in ("", "unknown", "none"): provider = "other"
    webroot = args.webroot if not (provider == "wpengine" and args.webroot == "public") else f"sites/{alias}"
    if client.get("rules", {}).get("do_not_touch") and "robots.txt" in client["rules"]["do_not_touch"]:
        sys.exit("robots.txt is in rules.do_not_touch for this client")
    if not proposed_path.exists(): sys.exit(f"No proposed robots.txt at {proposed_path}; run the report first (and make sure the client has a decided `ai:` policy).")
    new = proposed_path.read_text(encoding="utf-8")
    kind, current, err = robots_kind(alias, webroot)
    print(f"{args.target} ({alias}) serves robots.txt as: {kind}" + (f"  [{err}]" if err else ""))
    diff = list(difflib.unified_diff(current.splitlines(), new.splitlines(), f"robots.txt ({args.target}, {kind})", "robots.txt (proposed)", lineterm=""))
    print("\n".join(diff) if diff else "(identical: nothing to write)")
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    outdir = ROOT / "changes" / provider / client["slug"]; outdir.mkdir(parents=True, exist_ok=True)
    mode = "apply" if args.apply else "dry"
    result = ""
    if args.apply and diff:
        if args.target == "live":
            if args.yes: print("APPLY robots.txt on LIVE — confirmed by --yes")
            elif not sys.stdin.isatty(): sys.exit("Live apply needs a terminal to confirm, or pass --yes.")
            else:
                print(f"About to write robots.txt on LIVE ({alias}). Type the slug to confirm: ", end="", flush=True)
                if input().strip() != client["slug"]: sys.exit("aborted")
        bdir = outdir / "backup"; bdir.mkdir(exist_ok=True)
        (bdir / f"{stamp}-ai-discoverability-{args.target}-robots-before.txt").write_text(current, encoding="utf-8")
        code, out, err = ssh(alias, f"cd {webroot} && cat > robots.txt.lhf-new && mv robots.txt.lhf-new robots.txt && wp --skip-plugins={SKIP_PLUGINS} cache flush >/dev/null 2>&1; cat robots.txt", new)
        result = "written" if code == 0 and out.strip() == new.strip() else f"FAILED ({err.strip()[-200:]})"
        if provider == "kinsta": ssh(alias, f"cd {webroot} && wp --skip-plugins={SKIP_PLUGINS} kinsta cache purge --all >/dev/null 2>&1")
        print(f"Write: {result}")
        if args.target == "live":
            st, body, _ = fetch_text(client.get("canonical_host", "https://" + client["domain"]).rstrip("/") + "/robots.txt")
            print(f"Public re-fetch: HTTP {st}, {'matches' if body.strip() == new.strip() else 'does NOT match yet (edge cache?)'}")
    log_lines = [f"# ai-discoverability: robots.txt on {client['domain']} ({args.target})", "",
                 f"Run {stamp} · mode **{mode}** · alias `{alias}` · provider `{provider}` · served as **{kind}** before the run" + (f" · result: {result}" if result else ""), "",
                 "Policy source: the `ai:` block in the client file. Backup of the previous file (or of WordPress's virtual output) in `backup/` next to this log; "
                 "rollback = copy it back to the webroot as `robots.txt`, or delete the file to return to the virtual one.", "", "```diff"] + (diff or ["(no change)"]) + ["```"]
    (outdir / f"{stamp}-ai-discoverability-{args.target}-robots-{mode}.md").write_text("\n".join(log_lines) + "\n", encoding="utf-8")
    print(f"Log: {outdir / f'{stamp}-ai-discoverability-{args.target}-robots-{mode}.md'}")
    if kind != "unknown":
        update_client_observed(ROOT / "clients" / f"{client['slug']}.yaml", {"robots_txt": "file" if (args.apply and result == "written") else kind})

# ---------- roster ----------
def roster(cache):
    rows = []
    for f in sorted((ROOT / "clients").glob("*.yaml")):
        if f.name.startswith("_"): continue
        c = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        pid = (c.get("ahrefs") or {}).get("site_audit_project_id")
        if not pid or str(pid) in ("0", "unknown"): continue
        api = Api(c["slug"], cache)
        try:
            pages = api.get("roster-home", "site-audit/page-explorer", project_id=pid, select=SAMPLE_SELECT, order_by="traffic:desc", limit=5,
                            where=SAMPLE_WHERE).get("pages", [])
        except SystemExit as e:
            rows.append((c["slug"], c.get("ai") or {}, None, str(e)[:60])); continue
        rows.append((c["slug"], c.get("ai") or {}, pages, ""))
        log(f"  {c['slug']}: {len(pages)} pages")
    out = ["# AI bot policy across the roster", "", f"Generated {datetime.date.today().isoformat()} by `scripts/ai_discoverability.py --all` from each site's latest Ahrefs crawl (top 5 live pages). "
           "Policy columns come from each client file's `ai:` block; blocked columns are what robots.txt actually does.", "",
           "| Site | Policy (search / training) | Blocked search bots | Blocked training bots | IndexNow | robots.txt errors |", "|---|---|---|---|---|---|"]
    for slug, ai, pages, err in rows:
        if pages is None: out.append(f"| {slug} | | | | | API error: {err} |"); continue
        se, ss, te, ts = observed_blocks(pages)
        inx = ", ".join(sorted({str(p.get('indexnow_status')) for p in pages}))
        errs = ", ".join(sorted({str(p.get('robots_error')) for p in pages if p.get('robots_error')})) or "-"
        out.append(f"| {slug} | {ai.get('search_bots', '?')} / {ai.get('training_bots', '?')} | {', '.join(se + [b+'*' for b in ss]) or 'none'} | {', '.join(te + [b+'*' for b in ts]) or 'none'} | {inx} | {errs} |")
    out += ["", "`*` = blocked on some of the sampled pages only (inconsistent robots.txt groups)."]
    (ROOT / "docs" / "ai-bot-policy.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Roster: {ROOT / 'docs' / 'ai-bot-policy.md'} ({len(rows)} sites)")

# ---------- main ----------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--all", action="store_true", help="roster view across every client with an Ahrefs project -> docs/ai-bot-policy.md")
    ap.add_argument("--cache", action="store_true", help="keep/reuse raw Ahrefs responses in tmp/ahrefs-cache/<slug>/")
    ap.add_argument("--apply-robots", action="store_true", dest="apply_robots", help="work on the target's robots.txt from the proposed file (dry unless --apply)")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--target", choices=["staging", "live"], default="staging")
    ap.add_argument("--webroot", default="public")
    ap.add_argument("--yes", action="store_true")
    ap.add_argument("--no-client-write", action="store_true", dest="nowrite", help="don't touch clients/<slug>.yaml")
    ap.add_argument("--probe", action="store_true", help="also look at live over SSH: robots.txt file vs virtual, IndexNow plugin state")
    ap.add_argument("--robots-file", dest="robots_file", help="use this saved robots.txt instead of fetching the public one")
    args = ap.parse_args()
    load_env()
    if args.all: return roster(args.cache)
    if not args.slug: ap.error("slug or --all")
    cpath = ROOT / "clients" / f"{args.slug}.yaml"
    client = yaml.safe_load(cpath.read_text(encoding="utf-8"))
    client.setdefault("slug", args.slug)
    pid = (client.get("ahrefs") or {}).get("site_audit_project_id")
    if not pid or str(pid) in ("0", "unknown"): sys.exit(f"clients/{args.slug}.yaml has no ahrefs.site_audit_project_id")

    if args.apply_robots:
        proposed = sorted((ROOT / "reports" / args.slug).glob("robots-proposed-*.txt"))
        return apply_robots(args, client, proposed[-1] if proposed else ROOT / "reports" / args.slug / "robots-proposed-none.txt")

    api = Api(args.slug, args.cache)
    data = pull(client, api)
    home = (client.get("canonical_host") or f"https://{client['domain']}").rstrip("/")
    if args.robots_file:
        status, robots_text = f"file {args.robots_file}", Path(args.robots_file).read_text(encoding="utf-8")
    else:
        status, robots_text, _ = fetch_text(home + "/robots.txt")
        if not isinstance(status, int) or status != 200: robots_text = robots_text or ""
    probe = probe_site(client) if args.probe else None
    if probe and probe.get("error"): log(f"probe: {probe['error']}")
    universe = universe_from(data["sample"])
    blocked, undecided, notes = effective_policy(client.get("ai"), *universe)
    se, ss, te, ts = observed_blocks(data["sample"])
    proposed = None
    if not undecided:
        live_blocked = set(se + te + ss + ts)
        if live_blocked != blocked or ss or ts or (MARK_START in robots_text and not blocked):
            proposed = build_robots(robots_text, sorted(blocked), universe[0] + universe[1])
    outdir = ROOT / "reports" / args.slug; outdir.mkdir(parents=True, exist_ok=True)
    rep = outdir / f"ai-discoverability-{data['crawl']}.md"
    rep.write_text(write_report(client, data, status, robots_text, proposed, blocked, undecided, notes, universe, probe), encoding="utf-8")
    if proposed is not None:
        (outdir / f"robots-proposed-{data['crawl']}.txt").write_text(proposed, encoding="utf-8")
    if not args.nowrite:
        obs = observed_from(data, data["sample"])
        if probe and probe.get("robots_kind"):
            obs["robots_txt"] = probe["robots_kind"]; obs["indexnow_plugin"] = probe.get("indexnow") or "none"
        update_client_observed(cpath, obs)

    active = [i for i in data["issues"] if (i.get("crawled") or 0) > 0]
    print(f"{client['domain']}: crawl {data['crawl']}, {len(data['sample'])} pages sampled, robots.txt HTTP {status}")
    print(f"  blocked search bots: {se or 'none'}{(' (+ some pages: ' + str(ss) + ')') if ss else ''}; blocked training bots: {te or 'none'}{(' (+ some pages: ' + str(ts) + ')') if ts else ''}")
    print(f"  policy: {'UNDECIDED, nothing proposed' if undecided else ('matches live, nothing to change' if proposed is None else f'differs; proposed robots.txt blocks {len(blocked)} bot(s)')}")
    for i in active: print(f"  {i['crawled']:3}  {i['name']}  -> {ROUTES.get(i['name'], ('human','FLAG'))[0]} ({ROUTES.get(i['name'], ('human','FLAG'))[1]})")
    ppath = outdir / f"robots-proposed-{data['crawl']}.txt"
    print(f"Report: {rep}" + (f"\nProposed robots.txt: {ppath}" if proposed is not None else ""))

if __name__ == "__main__":
    main()
