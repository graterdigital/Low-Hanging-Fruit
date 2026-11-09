# Work orders: boilertechnologies.com

Ahrefs Site Audit project 10134747 · crawl 2026-11-04 · health 96 · 23 active issue types → 8 work orders (1 decisions, 2 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Orphan page (has no incoming internal links) | indexation-review | decide | 20 | 14 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 2 | Category page missing ItemList schema | schema-check | FLAG | 2 | 4 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 3 | Slow page | manual | FLAG | 11 | 3 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 4 | Slow server response for AI crawlers | hosting/cache | FLAG | 8 | 0 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 5 | Product page missing Product schema | schema-check | FLAG | 6 | 0 | agency | Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages. |
| 6 | H1 tag missing or empty | manual | FLAG | 2 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 7 | Waiting on skill `schema-fix` (2 issue types): Structured data has Google rich results validation error (227); Organization schema missing or incomplete (1) | schema-fix | skill pending | 228 | 91 | agency | Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual |
| 8 | Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (226) | fix-social-tags | skill pending | 226 | 91 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |

## Per item

### 1. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/boiler-services-fort-myers` (14 traffic)
- `/boiler-services-kissimmee`
- `/boiler-services-ocala`
- `/boiler-services-jacksonville`
- `/miura-boiler-dealer-tampa`
- `/boiler-services-sarasota`
- `/boiler-services-gainesville`
- `/boiler-services-cape-coral`
- `/boiler-services-lakewood-ranch`
- `/commercial-water-heater-orlando`
- … 10 more in Ahrefs

### 2. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/product` (4 traffic)
- `/gallery`

### 3. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/boiler-supplier-miami` (3 traffic)
- `/boiler-pumps-pinellas-park`
- `/blog/industrial-electric-boilers-over-traditional-heating-systems`
- `/miura-boiler-services-fort-lauderdale`
- `/industrial-commercial-boiler-bloomingdale`
- `/industrial-commercial-boiler-egypt-lake-leto`
- `/miura-boiler-services-st-petersburg`
- `/boiler-pumps-palm-harbor`
- `/boiler-services-in-englewood`
- `/blog/how-to-optimize-your-industrial-boilers-maximum-efficiency`
- … 1 more in Ahrefs

### 4. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/boiler-pumps-pinellas-park`
- `/miura-boiler-services-fort-lauderdale`
- `/industrial-commercial-boiler-bloomingdale`
- `/miura-boiler-services-st-petersburg`
- `/boiler-pumps-palm-harbor`
- `/boiler-services-in-englewood`
- `/blog/how-to-optimize-your-industrial-boilers-maximum-efficiency`
- `/modular-steam-boiler-west-palm-beach`

### 5. Product page missing Product schema

`issue:product-page-missing-product-schema` · schema-check · FLAG · decider: agency

Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages.

- `/miura-brand-hub`
- `/industrial-commercial-boiler-egypt-lake-leto`
- `/modular-steam-boiler-fort-lauderdale`
- `/hvac-circulator-pump-port-st-lucie`
- `/hvac-circulator-pump-wesley-chapel`
- `/modular-steam-boiler-west-palm-beach`

### 6. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/miura-brand-hub`
- `/miura`

### 7. Waiting on skill `schema-fix` (2 issue types): Structured data has Google rich results validation error (227); Organization schema missing or incomplete (1)

`pending:schema-fix` · schema-fix · skill pending · decider: agency

Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual

- `/boiler-services-west-palm-beach` (28 traffic)
- `/boiler-services-fort-myers` (14 traffic)
- `/boiler-services-miami` (11 traffic)
- `/blog/miura-boiler-systems-explained-compact-design-powerful-output` (8 traffic)
- `/ex-series-steam-boilers` (8 traffic)
- `/manufacturing-and-industrial-plants` (5 traffic)
- `/product` (4 traffic)
- `/boiler-supplier-miami` (3 traffic)
- `/blog/5-benefits-of-industrial-steam-boilers-for-manufacturing` (3 traffic)
- `/boiler-systems-and-water-heaters-for-hotels-resorts-and-country-clubs` (3 traffic)
- … 218 more in Ahrefs

### 8. Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (226)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/boiler-services-west-palm-beach` (28 traffic)
- `/boiler-services-fort-myers` (14 traffic)
- `/boiler-services-miami` (11 traffic)
- `/blog/miura-boiler-systems-explained-compact-design-powerful-output` (8 traffic)
- `/ex-series-steam-boilers` (8 traffic)
- `/manufacturing-and-industrial-plants` (5 traffic)
- `/product` (4 traffic)
- `/boiler-supplier-miami` (3 traffic)
- `/blog/5-benefits-of-industrial-steam-boilers-for-manufacturing` (3 traffic)
- `/boiler-systems-and-water-heaters-for-hotels-resorts-and-country-clubs` (3 traffic)
- … 216 more in Ahrefs

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Orphan page (has no incoming internal links)** (20 pages: /boiler-services-fort-myers, /boiler-services-kissimmee, /boiler-services-ocala, /boiler-services-jacksonville, …)

20 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

