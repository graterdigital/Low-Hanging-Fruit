# Low-Hanging-Fruit Toolkit: Plan v1.1

Last updated 2026-10-13 (evening). Pilot site: hsfamilylaw.com (Ahrefs Site Audit project 9704538).
This doc is the source of truth for the build. Update it when a decision changes; don't rely on chat history.

## 0. Status

- **Done:** `site-triage` skill v1, cold-tested on two sites by agents that had only the skill file (hsfamilylaw.com and livingyoungcenter.com). Both reports reconciled every active issue type. Reports live in this project under `reports/<slug>/`, client files under `clients/<slug>.yaml`.
- **Decided:** hsfamilylaw.com is on Kinsta with full access, so the write path is SSH + WP-CLI, with Kinsta staging as the safety net. The toolkit repo will be a private GitHub repo under a Grater Digital account (account not created yet).
- **Next:** repo scaffold, then `fix-redirect-links` (the AUTO-tier skill) against hsfamilylaw.com staging.

## 1. How the pieces fit (read this first)

Four things, each with one job:

| Piece | What it is | What goes in it |
|---|---|---|
| **Skill** | A folder with a `SKILL.md` (instructions) plus optional scripts and reference files | One repeatable procedure, e.g. "triage a site's audit issues". Never anything site-specific. |
| **Client file** | One small config file per site, `clients/<slug>.yaml` | Everything that differs per site: domain, Ahrefs project ID, SEO plugin, page builder, host and access method, GA4/GTM IDs, NAP, do-not-touch notes. Never any procedure, never any credential. |
| **Subagent** | A worker with its own context and a restricted tool list | Noisy jobs whose raw output shouldn't flood the main session: crawling pages, capturing network requests. |
| **Plugin (git repo)** | One versioned repo that bundles all skills, subagents, and the approval hooks | The whole toolkit. Installed on any machine with two commands; updated by pulling a new version. |

The rule that makes it portable: **skills hold the how, client files hold the what.** Running against a new site means adding one client file, not editing a skill.

Every fix skill follows the same contract: read client file → pull findings → build a change list (before/after per URL) → apply only the tier it is allowed to → write a change log with rollback data → re-check.

## 2. Fix tiers

- **AUTO**: applied without review, logged. Reversible and rules-based only.
- **APPROVE**: skill drafts the change list, a human approves, then it applies.
- **FLAG**: report only. Anything touching ad spend, tag containers, robots.txt, or theme templates starts here.

## 3. Pilot findings: hsfamilylaw.com

Full report: `reports/hsfamilylaw/triage-2026-10-08.md` (crawl of 2026-10-08, 473 URLs, health score 91, 36 active issue types collapsed to 8 root causes). Headlines:

- **Two template fixes clear 6 issue types / ~115 URL-symptoms**, all on zero-traffic archives: category/tag archives have no `<h1>` and no description (and 11 tag archives are orphans), and the theme's pagination links page 1 as `/page/1/`, which redirects.
- **The only queue item on pages with traffic** is legacy in-content links to pre-redesign URLs (home plus 14 pages, 308 traffic). Mostly AUTO; five of those old URLs redirect to the homepage and need a real target instead.
- **Page weight:** 25 PNGs of 1.0 to 3.5 MB, including a 1.59 MB background image loaded on 156 pages. No image-optimization plugin detected.
- **Schema:** the 43 validation errors match a hand-coded `LegalService` JSON-LD block in the theme head, separate from Yoast's graph. The failing property isn't exposed by the API; validate the homepage by hand. FLAG.
- **Yoast author sitemap** lists 4 author archives that redirect to home. One setting fixes it.
- **Slow pages (11)** are not page weight (HTML is 25 to 27 KB); needs a timing tool, not a crawl.
- **Per-page work left:** 17 real pages without descriptions (11 attorney bios, 6 core pages), 28 pages where Google rewrites the title (the top one still says "2025" in a 2026 URL), 4 posts missing alt text.

Second test site, livingyoungcenter.com (health 48): three sitewide links (a financing widget pointing at a 404, a footer and a menu link pointing at redirects) explain most of the red. Report: `reports/livingyoungcenter/triage-2026-10-08.md`.

## 4. Borrow vs. build

**Borrow**
- Ahrefs MCP: issue queue and before/after verification (already connected).
- WordPress/agent-skills: official WP-CLI and REST skills for WordPress mechanics.
- Yoast abilities (`yoast-seo/update-post-seo-data`): writes title, description, canonical, robots, social, schema type. Needs WordPress 6.9+ and the MCP Adapter. SEOPress has an equivalent. Rank Math has no per-post write tool, so those sites need WP-CLI post meta.
- claude-seo and marketingskills: audit checklists to adapt, both report-only.
- Google Ads MCP (official, read-only) plus claude-ads checks for the PPC audit.
- chrome-devtools-mcp: network capture for the analytics validator.
- mcp-gsc (community) and Google's GA4 MCP (read-only) for reporting data.

**Build** (nothing credible exists)
1. Apply layer: takes findings, applies fixes with diff, approval, change log, rollback.
2. Client registry and site profiler (detects SEO plugin, builder, host, tags).
3. Analytics install validator: tag presence, duplicates, consent state, conversion firing.
4. NAP consistency check: site vs. Business Profile vs. directories.
5. Gated Google Ads write-back (negatives, pauses). Much later, if ever.

## 5. Build order

**Phase 0: Foundation.** Plugin repo, client file format (done, see `clients/`), change-log and rollback convention, approval hook on all writes.

**Phase 1: Technical SEO (pilot on hsfamilylaw.com).**
- `site-triage`: Ahrefs issues → root-cause groups → tiered fix queue. Read-only. **Done (v1).**
- `fix-redirect-links` (AUTO)
- `fix-meta` (titles and descriptions through the SEO plugin, APPROVE)
- `fix-images` (weight, format, alt, APPROVE)
- `indexation-review` (archives, sitemap, noindex, APPROVE)
- `schema-check` (FLAG)
- `verify`: compare the next crawl against the baseline.

**Phase 2: Analytics validator.** FLAG only.
**Phase 3: PPC audit.** Read-only: wasted spend, search terms, negatives, conversion tracking health.
**Phase 4: Content improvement.** Start from pages Ahrefs shows losing traffic or rankings (the triage reports list them under "monitoring signals").
**Phase 5: Citations and syndication.** Lowest priority. Evidence says citation weight keeps declining, and Google now tells syndication partners to noindex instead of relying on cross-domain canonicals.

Next test site: one on a different SEO plugin (Rank Math or SEOPress), since both sites tested so far run Yoast.

## 6. Standards the skills encode

Tiebreaker is Google Search Central; then Ahrefs and Search Engine Land. Moz could not be fetched during research, so nothing here is checked against Moz yet.

- Alt text: short and descriptive; decorative images get `alt=""`. No character limit.
- Titles and descriptions: unique per page; no length limit from Google. Never auto-truncate.
- Headings: order and count do not affect rankings. Treat as accessibility; fix a missing H1.
- FAQ rich results stopped showing 2026-05-07; FAQ schema is inert in Google. Don't build for it.
- Self-hosted review stars on LocalBusiness/Organization are ineligible.
- Redirects: link internally to final URLs. Never bulk-redirect 404s to the homepage.
- Sitemaps: only canonical, indexable URLs.
- Core Web Vitals: never lazy-load the LCP image; set image dimensions; serve WebP or AVIF.
- Consent Mode v2: default must be set before any tag fires; required for EEA, UK, Switzerland traffic.
- AI search: stay indexable, keep content in text, keep schema matching the page. llms.txt and "AI-specific" schema are not used by Google.

## 7. Open items

- Create the Grater Digital GitHub account and the private toolkit repo.
- Kinsta SSH details for hsfamilylaw.com go in `~/.ssh/config` on the machine that runs fixes, never in a client file or this project.
- Confirm hsfamilylaw.com's WordPress version (Yoast abilities need 6.9+ if that route is ever used instead of WP-CLI).
- Google Ads MCP: Google's docs say developer tokens were sunset 2026-09-09 but the repo README still asks for one. Resolve before Phase 3.
- Moz cross-check of the standards in section 6.

## 8. Key sources

- Google Search Central: title links https://developers.google.com/search/docs/appearance/title-link · snippets https://developers.google.com/search/docs/appearance/snippet · images https://developers.google.com/search/docs/appearance/google-images · AI optimization guide https://developers.google.com/search/docs/fundamentals/ai-optimization-guide · documentation updates https://developers.google.com/search/updates · canonicalization https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- Ahrefs: site audit study (Patrick Stox) https://ahrefs.com/blog/site-audit-study/ · orphan pages https://ahrefs.com/blog/orphan-pages/ · title tag study https://ahrefs.com/blog/title-tags-study
- Search Engine Land: title rewrites https://searchengineland.com/google-changed-76-of-title-tags-in-q1-2025-heres-what-that-means-454847 · syndication canonicals https://searchengineland.com/google-no-longer-recommends-canonical-tags-for-syndicated-content-406491
- Whitespark local ranking factors https://whitespark.ca/local-search-ranking-factors/
- Tooling: claude-seo https://github.com/AgricIDaniel/claude-seo · WordPress agent-skills https://github.com/WordPress/agent-skills · WordPress MCP Adapter https://github.com/WordPress/mcp-adapter · Yoast abilities https://developer.yoast.com/features/yoast-seo-abilities/posts-seo-data/ · Google Ads MCP https://github.com/googleads/google-ads-mcp · chrome-devtools-mcp https://github.com/ChromeDevTools/chrome-devtools-mcp · Kinsta on SSH + WP-CLI with agents https://kinsta.com/blog/cli-agents-wordpress/
- Claude Code docs: skills https://code.claude.com/docs/en/skills.md · subagents https://code.claude.com/docs/en/sub-agents.md · plugins https://code.claude.com/docs/en/plugins/overview.md
- Authors for source fan-out: Patrick Stox, Barry Schwartz, John Mueller, Louise Linehan, Joshua Hardwick, Cyrus Shepard, Darren Shaw, Lily Ray, David Mihm.
