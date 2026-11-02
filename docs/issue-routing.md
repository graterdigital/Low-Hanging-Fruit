# Issue routing: what fixes what, across the roster

Written 2026-11-02 from the latest Ahrefs Site Audit crawl of all 40 projects (`reports/_roster/issues-rollup-2026-11-02.csv`, 184 issue types; `routes.yaml` is the machine-readable version every skill should read instead of keeping its own list).

Caveats: purskinclinic and backto30 have broken latest crawls (nearly everything 0 with large "missing" counts), fenceworks-staging is noindex by design, and cmitsolutions (66k URLs) dominates most raw totals. "Sites" below counts projects where the issue is active, which is the better signal for "is this worth a skill".

## 1. Where the roster's issues go

| Handler | Status | Issue types | Max sites | URLs | What it covers |
|---|---|---|---|---|---|
| **ignore** | standard | 9 | 36 | 39.8k | length rules, H1 count, expected redirects, pagination OG. No Google impact. Already excluded by site-triage. |
| **indexation-review** | proposed | 14 | 31 | 33.6k | sitemap hygiene (indexable pages missing from the sitemap on 31 sites, redirects/noindex/non-canonical pages in sitemaps), noindex intent, orphans |
| **fix-redirect-links** | built | 11 | 39 | 32.4k | links to redirects, chains, http→https and double-slash rules to add |
| **nofollow-audit** | proposed | 2 | 19 | 14.5k | internal links carrying rel=nofollow; ruggeddepot 8k and miuraboiler 3k pages means something systematic |
| **manual** | work orders | 6 | 27 | 14.4k | slow pages, missing H1 (template), multiple title tags (plugin conflict), content calls |
| **schema-fix** | proposed | 3 | 21 | 10.3k | Organization schema incomplete on 21 sites; validation errors on 8 |
| **fix-social-tags** | proposed | 4 | 23 | 10.0k | Open Graph incomplete on 23 sites, X cards missing on 12; one SEO-plugin setting each |
| **ai-discoverability** | built | 12 | 25 | 6.7k | bot policy, IndexNow (done), Article type, routed items |
| **fix-images** | built | 5 | 18 | 6.6k | weight, alt text, broken images |
| **fix-broken-links** | proposed | 5 | 23 | 4.9k | links to 404s on 22 sites; sibling of fix-redirect-links |
| **fix-meta** | specified | 4 | 35 | 4.4k | descriptions missing on 29 sites, SERP title mismatch on 35 |
| **monitor** | content phase | 11 | 31 | 1.7k | traffic/ranking drops and "X changed" notices |
| **redirect-rules** | proposed | 8 | 18 | 0.5k | the rules themselves: chains, 302s, loops, redirects in sitemaps, 404s with impressions |
| review | unclassified | 67 | 1 | ~6k | each on a single site; classify when one shows up in a triage |

## 2. New automatable skills, in the order I'd build them

1. **fix-social-tags** (AUTO). 23 sites, one Yoast/AIOSEO setting per site (default social image, X cards on). The cheapest roster-wide win left. Half a day.
2. **fix-broken-links** (AUTO/APPROVE). 22 sites. Same engine as fix-redirect-links with a different target list: for each 404 target, if a redirect rule exists or a same-slug page exists, rewrite; else list for a decision (unlink or retarget). Reuses `replace_links.php`.
3. **indexation-review** (APPROVE). 31 sites have indexable pages missing from the sitemap, 7 have noindex pages in it, 14 have orphans (mooringtech alone 4.7k). Mostly Yoast settings (`wpseo_titles`, `wpseo` options via `wp option patch`) plus an orphan decision list. The archive noindex decision from the hsfamilylaw triage lives here.
4. **redirect-rules** (APPROVE). Fewer URLs but direct ranking relevance: redirects in sitemaps (18 sites), chains (19), 302s that should be 301s (6), 3XX pages still getting organic traffic (6), the homepage-dump redirects from every fix-redirect-links skipped list. Writes through the Redirection plugin (WP-CLI) or Yoast Premium. GSC-driven ordering.
5. **schema-fix** (APPROVE). Organization schema incomplete on 21 sites: name, logo, sameAs from the client file into the SEO plugin's company settings. Validation errors (8 sites, hsfamilylaw's hand-coded LegalService block among them) stay diagnostic.
6. **nofollow-audit** (APPROVE). Investigate first: ruggeddepot's 8,065 pages with nofollow outgoing internal links almost certainly come from one theme or plugin setting. If so, one fix; if editor habit, a search-replace on `rel="nofollow"` for internal hrefs with the same engine as fix-redirect-links.

Not worth a skill: multiple title tags (17 sites, but one plugin conflict each, diagnose by hand), missing H1 (template edits), slow pages (hosting), "only one inlink" (3.5k URLs across 33 sites, but a content/internal-linking job for Phase 4, not a mechanical fix).

## 3. Manual fixes: the work-orders process

Anything that needs a human (a theme edit, a hosting ticket, a client decision, a content rewrite) goes through one process so it never lives only in a chat.

**Source of truth: `routes.yaml`.** Every Ahrefs issue type has one handler. `manual` entries carry a `what_to_do` line; `decide` is a tier for rows that are a choice rather than a task (noindex the tag archives or not; block training bots or not; where should this dead URL redirect).

**One "work orders" tab per client review sheet** (same Google Sheet that holds the alt-text and AI-discoverability tabs). Columns:

`id | issue | handler | tier | urls_affected | traffic_at_stake | what_to_do | decider (agency/client) | owner | status | decision_or_note | opened | updated | cleared`

- Rows are written by a script (`scripts/work_orders.py <slug> --sheet`) from the latest crawl through `routes.yaml`: every active issue whose handler is `manual`, plus every item a skill routed out (the skipped lists, FLAG rows, exception CSVs). Skills already produce those lists; the script collects them.
- Humans edit `owner`, `status`, `decision_or_note` only. Status: `open` → `needs decision` (if decider must answer) → `in progress` → `done` / `won't fix`. The script sets `cleared <date>` when the next crawl no longer shows the issue, which is the proof the fix worked.
- A `needs decision` row that gets a decision becomes either a skill run (the note names the skill and parameters, e.g. "noindex tags: yes → indexation-review") or a task.

**Roster view.** `scripts/work_orders.py --roster` writes one tab on the agency sheet: all open rows across clients sorted by `traffic_at_stake`, with counts per client. That is the weekly manual backlog for Greg and Tatelyn.

**Template fixes get a diff, not a ticket.** For theme edits (H1 in archive templates, `/page/1/` pagination, hand-coded schema blocks), the work order links to a diff file in `changes/<provider>/<slug>/` that a human applies and tests. The skill that found it writes the diff.

**Client decisions get a one-paragraph brief.** For `decider: client` rows, the work order carries a plain-language paragraph (what it is, the two options, our recommendation) that can be pasted into an email. Decisions are recorded in the client file (`rules:` or the relevant block) so no skill asks twice.

## 4. Immediate to-dos that fell out of the data

- Re-crawl purskinclinic and backto30; their latest crawls are broken.
- ruggeddepot: find what adds rel=nofollow to 8k pages of internal links (likely a theme or plugin option) before anything else on that site; and 8.7k pages linking to redirects.
- cmitsolutions: 494 pages with two title tags, 829 with no H1, 6.8k with incomplete Open Graph, 6.9k indexable pages not in the sitemap. One large site where four template/plugin fixes clear tens of thousands of symptoms. AIOSEO, so fix-meta's writer doesn't apply yet.
- mooringtech: 4.7k orphan pages. Needs a look at how its catalog is linked before any skill runs.
- miuraboiler: 5.5k noindex pages and 3k nofollow outgoing. Confirm intent (events archive?) before indexation-review touches it.
