# Work orders: aveluremedspa.com

Ahrefs Site Audit project 9704529 · crawl 2026-11-05 · health 99 · 28 active issue types → 14 work orders (1 decisions, 4 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Page has nofollow outgoing internal links | nofollow-audit | APPROVE (skill pending) | 51 | 99 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 2 | Slow page | manual | FLAG | 4 | 23 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 3 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 1 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 4 | H1 tag missing or empty | manual | FLAG | 6 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 5 | Pages fix-meta routed to [] | [] | FLAG | 3 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 6 | Pages fix-meta routed to ['/faqs/page/6/', '/faqs/page/4/', '/treatments/', '/treatments/page/2/', '/treatments_category/facial-peels/', '/faqs/page/2/', '/faqs/page/5/', '/faqs/page/7/', '/faqs/page/8/', '/treatments_category/injectables/', '/treatments_category/lasers/', '/faqs/page/9/', '/faqs/page/3/', '/treatments_category/body/'] | ['/faqs/page/6/', '/faqs/page/4/', '/treatments/', '/treatments/page/2/', '/treatments_category/facial-peels/', '/faqs/page/2/', '/faqs/page/5/', '/faqs/page/7/', '/faqs/page/8/', '/treatments_category/injectables/', '/treatments_category/lasers/', '/faqs/page/9/', '/faqs/page/3/', '/treatments_category/body/'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 7 | Category page missing ItemList schema | schema-check | FLAG | 1 | 0 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 8 | FAQ page missing FAQPage schema | schema-check | FLAG | 1 | 0 | client | FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing. |
| 9 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 1 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 10 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 11 | Slow server response for AI crawlers | hosting/cache | FLAG | 1 | 0 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 12 | Indexable page not in sitemap | indexation-review | APPROVE (skill pending) | 10 | 0 | agency | Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 13 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 6 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 14 | Organization schema missing or incomplete | schema-fix | APPROVE (skill pending) | 1 | 0 | agency | Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |

## Per item

### 1. Page has nofollow outgoing internal links

`issue:page-has-nofollow-outgoing-internal-links` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

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
- … 41 more in Ahrefs

### 2. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/locations/rochester/` (14 traffic)
- `/locations/waterford/` (9 traffic)
- `/treatments/page/2/`
- `/our-philosophy/`

### 3. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/category/uncategorized/`

### 4. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/privacy-policy/`
- `/treatments_category/facial-peels/`
- `/good-faith-estimate/`
- `/treatments_category/injectables/`
- `/treatments_category/lasers/`
- `/treatments_category/body/`

### 5. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `noindex`
- `non-200`
- `homepage title`

### 6. Pages fix-meta routed to ['/faqs/page/6/', '/faqs/page/4/', '/treatments/', '/treatments/page/2/', '/treatments_category/facial-peels/', '/faqs/page/2/', '/faqs/page/5/', '/faqs/page/7/', '/faqs/page/8/', '/treatments_category/injectables/', '/treatments_category/lasers/', '/faqs/page/9/', '/faqs/page/3/', '/treatments_category/body/']

`fix-meta:faqs-page-6-faqs-page-4-treatments-treat` · ['/faqs/page/6/', '/faqs/page/4/', '/treatments/', '/treatments/page/2/', '/treatments_category/facial-peels/', '/faqs/page/2/', '/faqs/page/5/', '/faqs/page/7/', '/faqs/page/8/', '/treatments_category/injectables/', '/treatments_category/lasers/', '/faqs/page/9/', '/faqs/page/3/', '/treatments_category/body/'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`

### 7. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/treatments_category/facial-peels/`

### 8. FAQ page missing FAQPage schema

`issue:faq-page-missing-faqpage-schema` · schema-check · FLAG · decider: client

FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing.

- `/faqs/`

### 9. H1 tag missing or empty  (non-indexable pages)

`issue:h1-tag-missing-or-empty-nonindexable` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/category/uncategorized/`

### 10. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/financing/`

### 11. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/treatments/page/2/`

### 12. Indexable page not in sitemap

`issue:indexable-page-not-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

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

### 13. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/treatments/?e-filter-fac3b0a-treatments_category=body`
- `/category/uncategorized/`
- `/treatments/?e-filter-fac3b0a-treatments_category=facial-peels`
- `/treatments/?e-page-fac3b0a=2`
- `/treatments/?e-filter-fac3b0a-treatments_category=injectables`
- `/treatments/?e-filter-fac3b0a-treatments_category=lasers`

### 14. Organization schema missing or incomplete

`issue:organization-schema-missing-or-incomplete` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (1 page: /category/uncategorized/)

1 page on aveluremedspa.com is set so Google does not index it (or does not follow its links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

