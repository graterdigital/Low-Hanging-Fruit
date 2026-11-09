# Work orders: aveluremedspa.com

Ahrefs Site Audit project 9704529 · crawl 2026-11-05 · health 99 · 28 active issue types → 14 work orders (1 decisions, 3 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Slow page | manual | FLAG | 4 | 23 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 2 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 1 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 3 | H1 tag missing or empty | manual | FLAG | 6 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 4 | Category page missing ItemList schema | schema-check | FLAG | 1 | 0 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 5 | FAQ page missing FAQPage schema | schema-check | FLAG | 1 | 0 | client | FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing. |
| 6 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 1 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 7 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 8 | Slow server response for AI crawlers | hosting/cache | FLAG | 1 | 0 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 9 | Pages fix-meta routed to homepage title | homepage title | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 10 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 11 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 12 | Waiting on skill `nofollow-audit` (2 issue types): Page has nofollow outgoing internal links (51); Page has nofollow outgoing internal links  (non-indexable pages) (6) | nofollow-audit | skill pending | 57 | 99 | agency | Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 13 | Waiting on skill `indexation-review` (1 issue type): Indexable page not in sitemap (10) | indexation-review | skill pending | 10 | 0 | agency | Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 14 | Waiting on skill `schema-fix` (1 issue type): Organization schema missing or incomplete (1) | schema-fix | skill pending | 1 | 0 | agency | Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |

## Per item

### 1. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/locations/rochester/` (14 traffic)
- `/locations/waterford/` (9 traffic)
- `/treatments/page/2/`
- `/our-philosophy/`

### 2. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/category/uncategorized/`

### 3. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/privacy-policy/`
- `/treatments_category/facial-peels/`
- `/good-faith-estimate/`
- `/treatments_category/injectables/`
- `/treatments_category/lasers/`
- `/treatments_category/body/`

### 4. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/treatments_category/facial-peels/`

### 5. FAQ page missing FAQPage schema

`issue:faq-page-missing-faqpage-schema` · schema-check · FLAG · decider: client

FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing.

- `/faqs/`

### 6. H1 tag missing or empty  (non-indexable pages)

`issue:h1-tag-missing-or-empty-nonindexable` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/category/uncategorized/`

### 7. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/financing/`

### 8. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/treatments/page/2/`

### 9. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 10. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 11. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 12. Waiting on skill `nofollow-audit` (2 issue types): Page has nofollow outgoing internal links (51); Page has nofollow outgoing internal links  (non-indexable pages) (6)

`pending:nofollow-audit` · nofollow-audit · skill pending · decider: agency

Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/locations/creve-coeur/` (18 traffic)
- `/locations/rochester/` (14 traffic)
- `/treatments/ultherapy/` (12 traffic)
- `/locations/in-greenwood/` (12 traffic)
- `/locations/ocala/` (12 traffic)
- `/locations/waterford/` (9 traffic)
- `/locations/buffalo/` (9 traffic)
- `/locations/mi-novi/` (7 traffic)
- `/locations/mi-grand-rapids/` (2 traffic)
- `/treatments/laser-hair-removal/` (2 traffic)
- … 47 more in Ahrefs

### 13. Waiting on skill `indexation-review` (1 issue type): Indexable page not in sitemap (10)

`pending:indexation-review` · indexation-review · skill pending · decider: agency

Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/faqs/page/6/`
- `/faqs/page/4/`
- `/treatments/page/2/`
- `/faqs/page/2/`
- `/faqs/page/5/`
- `/faqs/page/7/`
- `/faqs/`
- `/faqs/page/8/`
- `/faqs/page/9/`
- `/faqs/page/3/`

### 14. Waiting on skill `schema-fix` (1 issue type): Organization schema missing or incomplete (1)

`pending:schema-fix` · schema-fix · skill pending · decider: agency

Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (1 page: /category/uncategorized/)

1 page on aveluremedspa.com is set so Google does not index it (or does not follow its links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

