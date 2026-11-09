# Work orders: mooringtech.com

Ahrefs Site Audit project 9704542 · crawl 2026-11-05 · health 93 · 58 active issue types → 23 work orders (2 decisions, 14 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | H1 tag missing or empty | manual | FLAG | 48 | 51 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 2 | Category page missing ItemList schema | schema-check | FLAG | 41 | 51 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 3 | Canonical URL has no incoming internal links | indexation-review | APPROVE (skill pending) | 330 | 51 (top 200 of 330) | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 4 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 492 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page. |
| 5 | Orphan page (has no incoming internal links)  (non-indexable pages) | indexation-review | decide | 490 | 0 (top 200 of 490) | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 6 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 492 | 0 (top 200 of 492) | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 7 | Slow page | manual | FLAG | 11 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 8 | Slow server response for AI crawlers | hosting/cache | FLAG | 5 | 0 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 9 | CSS file size too large | manual | FLAG | 1 | 0 | agency | Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket. |
| 10 | Structured data has schema.org validation error | schema-fix | FLAG | 1 | 0 | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 11 | Noindex page in sitemap | indexation-review | APPROVE (skill pending) | 491 | 0 (top 200 of 491) | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 12 | Structured data has Google rich results validation error | schema-fix | APPROVE (skill pending) | 12 | 0 | agency | Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual |
| 13 | Non-canonical page in sitemap | indexation-review | APPROVE (skill pending) | 10 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 14 | Indexable page not in sitemap | indexation-review | APPROVE (skill pending) | 4 | 0 | agency | Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 15 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 2 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 16 | 5XX page in sitemap | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 17 | Indexable page became non-indexable | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 18 | Organization schema missing or incomplete | schema-fix | APPROVE (skill pending) | 1 | 0 | agency | Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 19 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 3 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 20 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 3 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 21 | Page has links to broken page  (non-indexable pages) | fix-broken-links | AUTO/APPROVE (skill pending) | 3 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 22 | 5XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 1 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 23 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 1 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/collections/cases-straps` (19 traffic)
- `/collections/panasonic-tablets` (11 traffic)
- `/collections/havis-vehicle-mounts-and-docking-stations` (8 traffic)
- `/collections/power-adapters` (6 traffic)
- `/collections/panasonic-toughbook-batteries` (5 traffic)
- `/collections/toughbook-55-vehicle-docks` (1 traffic)
- `/collections/panasonic-toughbook-cf-33-accessories` (1 traffic)
- `/blogs/news?page=3`
- `/collections/panasonic-toughbook-g2-accessories`
- `/collections/toughbook-33-vehicle-docking-stations`
- … 38 more in Ahrefs

### 2. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/collections/cases-straps` (19 traffic)
- `/collections/panasonic-tablets` (11 traffic)
- `/collections/havis-vehicle-mounts-and-docking-stations` (8 traffic)
- `/collections/power-adapters` (6 traffic)
- `/collections/panasonic-toughbook-batteries` (5 traffic)
- `/collections/toughbook-55-vehicle-docks` (1 traffic)
- `/collections/panasonic-toughbook-cf-33-accessories` (1 traffic)
- `/collections/panasonic-toughbook-g2-accessories`
- `/collections/toughbook-33-vehicle-docking-stations`
- `/collections/featured`
- … 31 more in Ahrefs

### 3. Canonical URL has no incoming internal links

`issue:canonical-url-has-no-incoming-internal-links` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/products/lps-138` (20 traffic)
- `/products/cf-veb331u` (14 traffic)
- `/products/cf-33uz02ham` (10 traffic)
- `/products/cf-lnddc120` (4 traffic)
- `/products/fz-vzsu1hu` (3 traffic)
- `/products/cf-33tz-0mam`
- `/products/fz-55jz00jbm`
- `/products/ds-gtc-413`
- `/products/fz-vzsut11u`
- `/products/pkg-ds-gtc-902-bw`
- … 320 more in Ahrefs

### 4. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page.

- `/search?q=+cradles`
- `/pages/laptops-for-automotive-tuning`
- `/products/toughbook-20-with-512gb-ssd`
- `/products/toughbook-a3-with-4g-lte-via-verizon`
- `/products/new-mk2-available-units-30-60-day-lead-time-1`
- `/products/toughbook-33-mk2-i7-units`
- `/products/toughbook-40-ram-upgrades-1`
- `/products/cf-54-accessories`
- `/products/toughbook-n1-current-models-1`
- `/products/fz-55-front-expansion-area-quick-release`
- … 482 more in Ahrefs

### 5. Orphan page (has no incoming internal links)  (non-indexable pages)

`issue:orphan-page-has-no-incoming-internal-links-nonindexable` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/products/toughbook-20-with-512gb-ssd`
- `/products/toughbook-a3-with-4g-lte-via-verizon`
- `/products/new-mk2-available-units-30-60-day-lead-time-1`
- `/products/toughbook-33-mk2-i7-units`
- `/products/toughbook-40-ram-upgrades-1`
- `/products/cf-54-accessories`
- `/products/toughbook-n1-current-models-1`
- `/products/fz-55-front-expansion-area-quick-release`
- `/products/cf-54-i5-processor-units`
- `/products/toughbook-54-prime-with-intel-core-i7-7600u-2-80ghz`
- … 480 more in Ahrefs

### 6. H1 tag missing or empty  (non-indexable pages)

`issue:h1-tag-missing-or-empty-nonindexable` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/products/toughbook-20-with-512gb-ssd`
- `/products/toughbook-a3-with-4g-lte-via-verizon`
- `/products/new-mk2-available-units-30-60-day-lead-time-1`
- `/products/toughbook-33-mk2-i7-units`
- `/products/toughbook-40-ram-upgrades-1`
- `/products/cf-54-accessories`
- `/products/toughbook-n1-current-models-1`
- `/products/fz-55-front-expansion-area-quick-release`
- `/products/cf-54-i5-processor-units`
- `/products/toughbook-54-prime-with-intel-core-i7-7600u-2-80ghz`
- … 482 more in Ahrefs

### 7. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/products/c-eb25-a12-1p`
- `/products/ds-pan-1116`
- `/products/ds-pan-1503`
- `/products/7170-0867-00`
- `/products/7160-1732`
- `/products/7160-1266`
- `/products/7300-0035`
- `/products/7160-0986`
- `/products/gad2x8`
- `/products/cf-vnp021u`
- … 1 more in Ahrefs

### 8. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/products/ds-pan-1116`
- `/products/ds-pan-1503`
- `/products/7160-1266`
- `/products/7160-0986`
- `/products/7170-1109-03`

### 9. CSS file size too large

`issue:css-file-size-too-large` · manual · FLAG · decider: agency

Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket.

- `/cdn/shop/t/40/assets/theme.scss.css?v=123564639967827357421790793080`

### 10. Structured data has schema.org validation error

`issue:structured-data-has-schema-org-validation-error` · schema-fix · FLAG · decider: agency

Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit.

- `/products/custom-toughbook-solutions-for-alaska-state-agencies`

### 11. Noindex page in sitemap

`issue:noindex-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/products/toughbook-20-with-512gb-ssd`
- `/products/toughbook-a3-with-4g-lte-via-verizon`
- `/products/new-mk2-available-units-30-60-day-lead-time-1`
- `/products/toughbook-33-mk2-i7-units`
- `/products/toughbook-40-ram-upgrades-1`
- `/products/cf-54-accessories`
- `/products/toughbook-n1-current-models-1`
- `/products/fz-55-front-expansion-area-quick-release`
- `/products/cf-54-i5-processor-units`
- `/products/toughbook-54-prime-with-intel-core-i7-7600u-2-80ghz`
- … 481 more in Ahrefs

### 12. Structured data has Google rich results validation error

`issue:structured-data-has-google-rich-results-validation-error` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual

- `/products/7300-0082`
- `/products/7170-0244`
- `/products/7300-0171`
- `/products/7160-0565-03`
- `/products/7300-0106`
- `/products/7300-0332`
- `/products/7160-0531-02`
- `/products/7300-0083`
- `/products/7300-0035`
- `/products/7300-0033`
- … 2 more in Ahrefs

### 13. Non-canonical page in sitemap

`issue:non-canonical-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/pages/diagnostics-for-agricultural-equipment`
- `/pages/military-laptops-buying-guide`
- `/pages/field-service-laptops-tablets`
- `/pages/diesel-truck-diagnostics`
- `/pages/government-laptops-buying-guide`
- `/pages/vehicle-laptop-mounts-for-cars-and-trucks`
- `/pages/fire-ems-laptops`
- `/pages/police-laptops-buying-guide`
- `/pages/marine-boat-diagnostics`
- `/pages/laptops-for-automotive-tuning`

### 14. Indexable page not in sitemap

`issue:indexable-page-not-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/blogs/news?page=3`
- `/blogs/news?page=2`
- `/collections`
- `/cart`

### 15. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/search?q=+cradles`
- `/pages/laptops-for-automotive-tuning`

### 16. 5XX page in sitemap

`issue:5xx-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/products/7160-1261-01`

### 17. Indexable page became non-indexable

`issue:indexable-page-became-non-indexable` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/products/7160-1261-01`

### 18. Organization schema missing or incomplete

`issue:organization-schema-missing-or-incomplete` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/`

### 19. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/collections/ram-rugged-vehicle-mounts-for-phones-tablets-and-laptops`
- `/pages/%3Ca%20href=%22https://www.dodig.mil/reports.html/Article/1118917/improvements-needed-with-tracking-and-configuring-army-commercial-mobile-devices/%22%3Ehttps://www.dodig.mil/reports.html/Article/1118917/improvements-needed-with-tracking-and-configuring-army-commercial-mobile-devices/%3C/a%3E%20`
- `/products/cf-aa6373am`

### 20. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/collections/ram-rugged-vehicle-mounts-for-phones-tablets-and-laptops`
- `/pages/%3Ca%20href=%22https://www.dodig.mil/reports.html/Article/1118917/improvements-needed-with-tracking-and-configuring-army-commercial-mobile-devices/%22%3Ehttps://www.dodig.mil/reports.html/Article/1118917/improvements-needed-with-tracking-and-configuring-army-commercial-mobile-devices/%3C/a%3E%20`
- `/products/cf-aa6373am`

### 21. Page has links to broken page  (non-indexable pages)

`issue:page-has-links-to-broken-page-nonindexable` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/pages/military-laptops-buying-guide`
- `/pages/vehicle-laptop-mounts-for-cars-and-trucks`
- `/collections/desktop-docks/products/fz-vcbn11u`

### 22. 5XX page

`issue:5xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/products/7160-1261-01`

### 23. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/products/fz-vcbn11u`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (492 pages: /search?q=+cradles, /pages/laptops-for-automotive-tuning, /products/toughbook-20-with-512gb-ssd, /products/toughbook-a3-with-4g-lte-via-verizon, …)

492 pages on mooringtech.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

**Orphan page (has no incoming internal links)  (non-indexable pages)** (490 pages: /products/toughbook-20-with-512gb-ssd, /products/toughbook-a3-with-4g-lte-via-verizon, /products/new-mk2-available-units-30-60-day-lead-time-1, /products/toughbook-33-mk2-i7-units, …)

490 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

