# Work orders: curatemedspa.com

Ahrefs Site Audit project 9704524 · crawl 2026-11-05 · health 99 · 35 active issue types → 14 work orders (1 decisions, 5 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Slow page | manual | FLAG | 10 | 68 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 2 | Slow server response for AI crawlers | hosting/cache | FLAG | 2 | 6 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 3 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 1 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 4 | H1 tag missing or empty | manual | FLAG | 6 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 5 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 2 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 6 | Pages fix-meta routed to homepage title | homepage title | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 7 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 8 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 9 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 10 | Waiting on skill `schema-fix` (1 issue type): Organization schema missing or incomplete (1) | schema-fix | skill pending | 1 | 128 | agency | Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 11 | Waiting on skill `nofollow-audit` (2 issue types): Page has nofollow outgoing internal links (9); Page has nofollow outgoing internal links  (non-indexable pages) (2) | nofollow-audit | skill pending | 11 | 61 | agency | Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 12 | Waiting on skill `fix-social-tags` (2 issue types): Open Graph tags incomplete (11); X (Twitter) card missing (1) | fix-social-tags | skill pending | 12 | 21 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 13 | Waiting on skill `redirect-rules` (3 issue types): Canonical from HTTP to HTTPS (7); 302 redirect (5); HTTPS to HTTP redirect (1) | redirect-rules | skill pending | 13 | 0 | agency | Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 14 | Waiting on skill `indexation-review` (1 issue type): Indexable page not in sitemap (1) | indexation-review | skill pending | 1 | 0 | agency | Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |

## Per item

### 1. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/dermal-fillers/` (61 traffic)
- `/iv-hydration-therapy/` (6 traffic)
- `/dermal-fillers-vs-botox-guide/` (1 traffic)
- `/services/vitamin-injections/`
- `/home-2/`
- `/laser-hair-removal-chattanooga-winter/`
- `/skin-tightening-2025/`
- `/sculptra/`
- `/anti-aging-2025/`
- `/botox/`

### 2. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/iv-hydration-therapy/` (6 traffic)
- `/skin-tightening-2025/`

### 3. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/tag/weekly-newsletter/`

### 4. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/locations/ooltewah/`
- `/services/pdo-threads/`
- `/locations/knoxville/`
- `/terms-conditions/`
- `/pdo-threads/`
- `/locations/chattanooga/`

### 5. H1 tag missing or empty  (non-indexable pages)

`issue:h1-tag-missing-or-empty-nonindexable` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/terms-conditions/`
- `/tag/weekly-newsletter/`

### 6. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `/`

### 7. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/financing/`

### 8. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 9. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 10. Waiting on skill `schema-fix` (1 issue type): Organization schema missing or incomplete (1)

`pending:schema-fix` · schema-fix · skill pending · decider: agency

Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (128 traffic)

### 11. Waiting on skill `nofollow-audit` (2 issue types): Page has nofollow outgoing internal links (9); Page has nofollow outgoing internal links  (non-indexable pages) (2)

`pending:nofollow-audit` · nofollow-audit · skill pending · decider: agency

Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/dermal-fillers/` (61 traffic)
- `/privacy-policy/`
- `/blog/`
- `/services/vitamin-injections/`
- `/services/cooltone/`
- `/services/dermal-fillers/`
- `/services/pdo-threads/`
- `/services/iv-therapy/`
- `/pdo-threads/`
- … 2 more in Ahrefs

### 12. Waiting on skill `fix-social-tags` (2 issue types): Open Graph tags incomplete (11); X (Twitter) card missing (1)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/locations/murfreesboro/` (13 traffic)
- `/treatment-for-excessive-sweating-in-2025/` (5 traffic)
- `/locations/nashville/` (3 traffic)
- `/privacy-policy/`
- `/locations/ooltewah/`
- `/blog/`
- `/financing/`
- `/the-reserve`
- `/locations/knoxville/`
- `/terms-conditions/`
- … 2 more in Ahrefs

### 13. Waiting on skill `redirect-rules` (3 issue types): Canonical from HTTP to HTTPS (7); 302 redirect (5); HTTPS to HTTP redirect (1)

`pending:redirect-rules` · redirect-rules · skill pending · decider: agency

Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/dermal-fillers/`
- `/contact/`
- `/injectable-services/`
- `/privacy-policy/`
- `/sculptra/`
- `/botox/`
- `/terms-conditions/`
- … 6 more in Ahrefs

### 14. Waiting on skill `indexation-review` (1 issue type): Indexable page not in sitemap (1)

`pending:indexation-review` · indexation-review · skill pending · decider: agency

Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/the-reserve`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (1 page: /tag/weekly-newsletter/)

1 page on curatemedspa.com is set so Google does not index it (or does not follow its links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

