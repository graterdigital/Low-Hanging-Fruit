# Work orders: esthetixmd.com

Ahrefs Site Audit project 9704528 · crawl 2026-11-05 · health 99 · 31 active issue types → 12 work orders (0 decisions, 4 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Product page missing Product schema | schema-check | FLAG | 1 | 2 | agency | Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages. |
| 2 | Slow page | manual | FLAG | 6 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 3 | Category page missing ItemList schema | schema-check | FLAG | 2 | 0 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 4 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 5 | Structured data has schema.org validation error | schema-fix | FLAG | 1 | 0 | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 6 | Pages fix-meta routed to homepage title | homepage title | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 7 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 8 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 9 | Waiting on skill `indexation-review` (1 issue type): Indexable page not in sitemap (17) | indexation-review | skill pending | 17 | 0 | agency | Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 10 | Waiting on skill `fix-broken-links` (3 issue types): 404 page (1); 4XX page (1); Page has links to broken page (3) | fix-broken-links | skill pending | 5 | 0 | agency | Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 11 | Waiting on skill `fix-social-tags` (2 issue types): Open Graph tags missing (1); X (Twitter) card missing (1) | fix-social-tags | skill pending | 2 | 0 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 12 | Waiting on skill `redirect-rules` (1 issue type): 3XX redirect in sitemap (2) | redirect-rules | skill pending | 2 | 0 | agency | Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |

## Per item

### 1. Product page missing Product schema

`issue:product-page-missing-product-schema` · schema-check · FLAG · decider: agency

Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages.

- `/pelvic-suite/ultra-femme-360/` (2 traffic)

### 2. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/blog/category/coolsculpting/page/2/`
- `/gallery/dysport-case-2/`
- `/gallery-category/body-treatments/page/5/`
- `/blog/men-and-women-in-bend-or-look-thinner-and-younger-with-kybella-injection-treatment/`
- `/blog/`
- `/gallery-category/injectables/page/2/`

### 3. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/gallery-category/sculptra/`
- `/gallery-category/weight-loss/`

### 4. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/about-us/financing/`

### 5. Structured data has schema.org validation error

`issue:structured-data-has-schema-org-validation-error` · schema-fix · FLAG · decider: agency

Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit.

- `/body-contouring/coolsculpting-educational-videos/`

### 6. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 7. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 8. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 9. Waiting on skill `indexation-review` (1 issue type): Indexable page not in sitemap (17)

`pending:indexation-review` · indexation-review · skill pending · decider: agency

Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/blog/category/coolsculpting/page/2/`
- `/gallery-category/body-treatments/page/7/`
- `/gallery-category/emsculpt/page/2/`
- `/gallery-category/body-treatments/page/5/`
- `/gallery-category/facial-skin-tightening/`
- `/gallery-category/body-treatments/page/4/`
- `/gallery-category/body-treatments/page/3/`
- `/gallery-category/coolsculpting/page/2/`
- `/gallery-category/juvederm-ultra-and-ultra-plus/page/2/`
- `/gallery-category/injectables/page/4/`
- … 7 more in Ahrefs

### 10. Waiting on skill `fix-broken-links` (3 issue types): 404 page (1); 4XX page (1); Page has links to broken page (3)

`pending:fix-broken-links` · fix-broken-links · skill pending · decider: agency

Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/pelvic-suite/co2-lift-v/`
- … 4 more in Ahrefs

### 11. Waiting on skill `fix-social-tags` (2 issue types): Open Graph tags missing (1); X (Twitter) card missing (1)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/subscribe-and-save/`
- … 1 more in Ahrefs

### 12. Waiting on skill `redirect-rules` (1 issue type): 3XX redirect in sitemap (2)

`pending:redirect-rules` · redirect-rules · skill pending · decider: agency

Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/gallery/zwave-case-3/`
- `/gallery/medical-weight-loss-case-2/`

