# Work orders: boilertechnologies.com

Ahrefs Site Audit project 10134747 · crawl 2026-11-04 · health 96 · 23 active issue types → 9 work orders (1 decisions, 3 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Structured data has Google rich results validation error | schema-fix | APPROVE (skill pending) | 227 | 91 (top 200 of 227) | agency | Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual |
| 2 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 226 | 91 (top 200 of 226) | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 3 | Orphan page (has no incoming internal links) | indexation-review | decide | 20 | 14 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 4 | Category page missing ItemList schema | schema-check | FLAG | 2 | 4 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 5 | Slow page | manual | FLAG | 11 | 3 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 6 | Organization schema missing or incomplete | schema-fix | APPROVE (skill pending) | 1 | 2 | agency | Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 7 | Slow server response for AI crawlers | hosting/cache | FLAG | 8 | 0 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 8 | Product page missing Product schema | schema-check | FLAG | 6 | 0 | agency | Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages. |
| 9 | H1 tag missing or empty | manual | FLAG | 2 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |

## Per item

### 1. Structured data has Google rich results validation error

`issue:structured-data-has-google-rich-results-validation-error` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual

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
- … 217 more in Ahrefs

### 2. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

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

### 3. Orphan page (has no incoming internal links)

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

### 4. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/product` (4 traffic)
- `/gallery`

### 5. Slow page

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

### 6. Organization schema missing or incomplete

`issue:organization-schema-missing-or-incomplete` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (2 traffic)

### 7. Slow server response for AI crawlers

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

### 8. Product page missing Product schema

`issue:product-page-missing-product-schema` · schema-check · FLAG · decider: agency

Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages.

- `/miura-brand-hub`
- `/industrial-commercial-boiler-egypt-lake-leto`
- `/modular-steam-boiler-fort-lauderdale`
- `/hvac-circulator-pump-port-st-lucie`
- `/hvac-circulator-pump-wesley-chapel`
- `/modular-steam-boiler-west-palm-beach`

### 9. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/miura-brand-hub`
- `/miura`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Orphan page (has no incoming internal links)** (20 pages: /boiler-services-fort-myers, /boiler-services-kissimmee, /boiler-services-ocala, /boiler-services-jacksonville, …)

20 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

