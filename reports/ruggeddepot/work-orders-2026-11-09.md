# Work orders: ruggeddepot.com

Ahrefs Site Audit project 9704549 · crawl 2026-11-09 · health 96 · 45 active issue types → 26 work orders (4 decisions, 12 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Page has nofollow outgoing internal links | nofollow-audit | APPROVE (skill pending) | 8086 | 587 (top 200 of 8086) | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 2 | Category page missing ItemList schema | schema-check | FLAG | 995 | 473 (top 200 of 995) | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 3 | Slow page | manual | FLAG | 6687 | 244 (top 200 of 6687) | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 4 | Product page missing Product schema | schema-check | FLAG | 27 | 39 | agency | Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages. |
| 5 | H1 tag missing or empty | manual | FLAG | 34 | 11 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 6 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 5 | 10 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 7 | Orphan page (has no incoming internal links) | indexation-review | decide | 349 | 9 (top 200 of 349) | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 8 | 3XX page receives organic traffic | redirect-rules | APPROVE (skill pending) | 2 | 5 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 9 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 94 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 10 | Links to redirect, skipped by fix-redirect-links: no incoming internal links (sitemap or orphan entry) | manual | decide | 3 | 0 | agency | fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave. |
| 11 | Links to redirect, skipped by fix-redirect-links: target https://ruggeddepot.com/shop returned 403 on verify, expected 200 | manual | decide | 1 | 0 | agency | fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave. |
| 12 | Slow server response for AI crawlers | hosting/cache | FLAG | 557 | 0 (top 200 of 557) | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 13 | Pages fix-meta routed to [] | [] | FLAG | 4 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 14 | Low word count | manual | FLAG | 3 | 0 | client | Content call: expand, merge or noindex the page. Client decides what the page is for. |
| 15 | Page has no outgoing links | manual | FLAG | 3 | 0 | client | Content call: add relevant internal links or accept it (thank-you and utility pages are fine). |
| 16 | wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings) | manual | FLAG | 1 | 0 | agency | Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1056-fix-redirect-links-live-options.md. |
| 17 | Product images whose alt text needs a human (shared model photos, one-word titles) | fix-images | APPROVE | 296 | 0 | agency | Fill new_alt on the 'alt text' tab (rows keyed product-attachment:<id>) or in the exception CSV, then fix-images --alt-apply. |
| 18 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 117 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 19 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 16 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 20 | Noindex in HTML and HTTP header | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 21 | Page in multiple sitemaps | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 22 | X (Twitter) card missing | fix-social-tags | AUTO (skill pending) | 2 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 23 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 1 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 24 | X (Twitter) card incomplete | fix-social-tags | AUTO (skill pending) | 1 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 25 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 5 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 26 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 5 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Page has nofollow outgoing internal links

`issue:page-has-nofollow-outgoing-internal-links` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/` (137 traffic)
- `/product-category/getac/laptops-getac/` (97 traffic)
- `/product-category/getac/tablets-getac/f110/` (63 traffic)
- `/product/getac-120w-11-16v-22-32v-dc-vehicle-adapter-bare-wire-3-year-warranty-120w-for-docking-station/` (40 traffic)
- `/product-category/getac/laptops-getac/b360/` (31 traffic)
- `/product-category/getac/laptops-getac/v120/` (26 traffic)
- `/product-category/getac/tablets-getac/zx10/` (22 traffic)
- `/product-category/panasonic/` (21 traffic)
- `/product/havis-work-truck-console-package-for-2004-2025-freightliner-m2-106-112-with-bucket-seats/` (17 traffic)
- `/product-category/getac/tablets-getac/` (15 traffic)
- … 8076 more in Ahrefs

### 2. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/product-category/panasonic/laptops/toughbook-40/` (152 traffic)
- `/product-category/getac/laptops-getac/` (97 traffic)
- `/product-category/getac/tablets-getac/f110/` (63 traffic)
- `/product-category/getac/laptops-getac/b360/` (31 traffic)
- `/product-category/getac/laptops-getac/v120/` (26 traffic)
- `/product-category/panasonic/` (21 traffic)
- `/product-category/getac/tablets-getac/` (15 traffic)
- `/product-category/getac/laptops-getac/s410-laptops-getac/` (13 traffic)
- `/product-category/accessories/headsets/setcom-headsets/` (11 traffic)
- `/product-category/panasonic/2-in-1s/toughbook-g2/` (8 traffic)
- … 985 more in Ahrefs

### 3. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/product-category/getac/laptops-getac/` (97 traffic)
- `/product/getac-120w-11-16v-22-32v-dc-vehicle-adapter-bare-wire-3-year-warranty-120w-for-docking-station/` (40 traffic)
- `/product-category/panasonic/2-in-1s/toughbook-33/` (17 traffic)
- `/product/havis-work-truck-console-package-for-2004-2025-freightliner-m2-106-112-with-bucket-seats/` (17 traffic)
- `/product-category/getac/tablets-getac/` (15 traffic)
- `/product-category/accessories/headsets/setcom-headsets/` (11 traffic)
- `/product-category/panasonic/2-in-1s/toughbook-g2/` (8 traffic)
- `/product-category/getac/tablets-getac/ux10/` (8 traffic)
- `/toughbook-vehicle-mounting-options/` (4 traffic)
- `/product-category/vehicle-equipment/vehicle-mounts-equipment/printer-mounts/` (3 traffic)
- … 6677 more in Ahrefs

### 4. Product page missing Product schema

`issue:product-page-missing-product-schema` · schema-check · FLAG · decider: agency

Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages.

- `/product-category/getac/tablets-getac/zx10/` (22 traffic)
- `/product-category/panasonic/2-in-1s/toughbook-33/` (17 traffic)
- `/product/gamber-johnson-7170-0601-tabcruzer-mini-wall-mount-kit/`
- `/product/gamber-johnson-7160-0847-external-cup-holder/`
- `/product-category/getac/tablets-getac/f110/page/2/`
- `/product-category/getac/tablets-getac/zx10/page/2/`
- `/product/toughbook-g3/`
- `/product-category/panasonic/2-in-1s/toughbook-g2/page/5/`
- `/product-category/getac/laptops-getac/s410-laptops-getac/page/3/`
- `/product/brother-printer-dt-paper-lb3660-001/`
- … 17 more in Ahrefs

### 5. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/why-are-toughbook-computers-so-expensive/` (5 traffic)
- `/toughbook-vehicle-mounting-options/` (4 traffic)
- `/panasonic-toughbook-warranty-guide/` (2 traffic)
- `/getac-b360x-b360x-pro-edge-ai-rugged-laptops/`
- `/getac-rugged-devices-now-certified-on-t-mobiles-high-speed-5g-network/`
- `/4-ways-investing-in-technology-can-improve-recruitment-for-fire-ems-and-rescue/`
- `/product/gamber-johnson-7170-0601-tabcruzer-mini-wall-mount-kit/`
- `/the-ultimate-guide-to-getac-rugged-laptops-2025-comprehensive-model-comparison/`
- `/how-tough-is-the-toughbook-55/`
- `/how-much-do-rugged-laptops-tablets-cost-in-2025/`
- … 24 more in Ahrefs

### 6. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/ultimate-rugged-laptop-buying-guide/` (10 traffic)
- `/product/gamber-johnson-7160-1425-overhead-guard-cab-mount/`
- `/toughbook-vehicle-mounting-options-2/`
- `/diagnostics-for-agricultural-equipment/`
- `/fire-ems/`

### 7. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/product/havis-100-watt-ac-power-supply-used-with-ds-dell-900-1100-series-docking-stations-lps-181/` (9 traffic)
- `/product/havis-3-5%E2%80%B3-heavy-duty-telescoping-pole-c-hdm-207/`
- `/product/havis-self-checkout-printer-enclosure/`
- `/product/havis-flexipole-compact-counter-mount-locking-stand-for-payment-terminals/`
- `/product/havis-rear-partition-for-2015-2025-ford-transit-low-roof-130%E2%80%B3-wb-window-van-p-rear-4/`
- `/product/havis-dual-ball-mount-with-1-50%E2%80%B3-knob-style-long-housing-two-long-vesa-75-plates-dbm-1150-kl-0404/`
- `/product/havis-power-cable-for-havis-rugged-communications-hub-ds-da-317/`
- `/product/havis-premium-tablet-pedestal-mount-package-for-2018-2024-chevrolet-equinox-gmc-terrain-pkg-psm-3004-t/`
- `/product/havis-forklift-pillar-mount-swivel-arm-for-keyboards-with-6%E2%80%B3-base-mh-arm-0600/`
- `/product/havis-docking-station-for-getac-zx70-tablet-with-jae-connector-dual-pass-thru-antenna-connections-ds-gtc-711-2/`
- … 339 more in Ahrefs

### 8. 3XX page receives organic traffic

`issue:3xx-page-receives-organic-traffic` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/product-category/getac/tablets-getac/a140/` (3 traffic)
- `/product-category/panasonic/toughbook-40/` (2 traffic)

### 9. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/shop/product_brand-gamber-johnson-3-or-havis/page/33/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/259/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/28/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/264/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/22/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/16/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/25/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/236/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/40/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/261/`
- … 84 more in Ahrefs

### 10. Links to redirect, skipped by fix-redirect-links: no incoming internal links (sitemap or orphan entry)

`redirect-links:no-incoming-internal-links-sitemap-or-or` · manual · decide · decider: agency · source: redirect-map-2026-10-29.json

fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave.

- `/get-a-custom-quote/`
- `/product/panasonic-cf-339w045bm/`
- `/our-team/`

### 11. Links to redirect, skipped by fix-redirect-links: target https://ruggeddepot.com/shop returned 403 on verify, expected 200

`redirect-links:target-https-ruggeddepot-com-shop-return` · manual · decide · decider: agency · source: redirect-map-2026-10-29.json

fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave.

- `/featured/` (4 links)

### 12. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/product/gamber-johnson-7300-0373-04/`
- `/product-category/vehicle-equipment/cradles-docking-stations/page/33/`
- `/product/getac-s510ad-sx172aqxsqxx/`
- `/product/gamber-johnson-7300-0597-00/`
- `/product-category/vehicle-equipment/page/49/`
- `/product-category/vehicle-equipment/page/33/`
- `/product/getac-f110g7-fta724ja1dxx/`
- `/product/gamber-johnson-7300-0600-00/`
- `/product-category/getac/tablets-getac/page/15/`
- `/product/havis-premium-tablet-pedestal-mount-package-for-2018-2024-chevrolet-equinox-gmc-terrain-pkg-psm-3004-t/`
- … 547 more in Ahrefs

### 13. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-11-03.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`
- `noindex`
- `non-200`
- `homepage title`

### 14. Low word count

`issue:low-word-count` · manual · FLAG · decider: client

Content call: expand, merge or noindex the page. Client decides what the page is for.

- `/product/gamber-johnson-7170-0601-tabcruzer-mini-wall-mount-kit/`
- `/product/gamber-johnson-7160-0847-external-cup-holder/`
- `/product/brother-printer-dt-paper-lb3660-001/`

### 15. Page has no outgoing links

`issue:page-has-no-outgoing-links` · manual · FLAG · decider: client

Content call: add relevant internal links or accept it (thank-you and utility pages are fine).

- `/product/gamber-johnson-7170-0601-tabcruzer-mini-wall-mount-kit/`
- `/product/gamber-johnson-7160-0847-external-cup-holder/`
- `/product/brother-printer-dt-paper-lb3660-001/`

### 16. wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings)

`redirect-links:wp-options` · manual · FLAG · decider: agency · source: 2026-10-30-1056-fix-redirect-links-live-options.md

Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1056-fix-redirect-links-live-options.md.

- `wcstripe_cache_live_account_data`

### 17. Product images whose alt text needs a human (shared model photos, one-word titles)

`fix-images:product-alt-exceptions` · fix-images · APPROVE · decider: agency · source: 2026-10-30-1149-fix-images-product-alt-exceptions.csv

Fill new_alt on the 'alt text' tab (rows keyed product-attachment:<id>) or in the exception CSV, then fix-images --alt-apply.

- `Image_20230205_123244_131.png` (294 products)
- `fz-55-stylus-insert-5.jpg` (137 products)
- `fz-55-front-left-dvd-5.jpg` (137 products)
- `fz-55-flat-5.jpg` (137 products)
- `fz-55-fingerprint-5.jpg` (137 products)
- `fz-55-closed-stand-5.jpg` (137 products)
- `fz-55-bottom-stand-5.jpg` (137 products)
- `fz-55-back-right-5.jpg` (137 products)
- `fz-55-back-ports-out-5.jpg` (137 products)
- `fz-55-back-left-5.jpg` (137 products)
- … 286 more in Ahrefs

### 18. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/shop/product_brand-gamber-johnson-3-or-havis/page/33/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/259/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/28/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/264/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/22/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/16/`
- `/shop/product_brand-gamber-johnson-3-or-havis/page/25/`
- `/product-category/getac/b360/?orderby=price_asc`
- `/product-category/getac/laptops-getac/s410-laptops-getac/page/2/?orderby=price_asc`
- `/product-category/getac/b360/page/3/?orderby=price_asc`
- … 107 more in Ahrefs

### 19. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/featured/`
- `/get-a-custom-quote/`
- `/all-getac-models/`
- `/all-getac-models/handhelds-all-getac-models/`
- `/all-getac-models/tablets-all-getac-models/`
- `/product/panasonic-cf-339w045bm/`
- `/toughbooks/laptops/`
- `/all-getac-models/laptops-all-getac-models/`
- `/ems/`
- `/toughbook-55/`
- … 6 more in Ahrefs

### 20. Noindex in HTML and HTTP header

`issue:noindex-in-html-and-http-header` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/my-account/lost-password/`

### 21. Page in multiple sitemaps

`issue:page-in-multiple-sitemaps` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/shop/`

### 22. X (Twitter) card missing

`issue:x-twitter-card-missing` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/product/toughbook-g3/`
- `/product/toughbook-34/`

### 23. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/product/60295/`

### 24. X (Twitter) card incomplete

`issue:x-twitter-card-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/product/60295/`

### 25. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/products`
- `/product-category/getac/a140/?orderby=price_asc`
- `/firstnet-built-with-att/`
- `/product-category/accessories/docking-stations/`
- `/product-category/accessories/cradles/`

### 26. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/products`
- `/product-category/getac/a140/?orderby=price_asc`
- `/firstnet-built-with-att/`
- `/product-category/accessories/docking-stations/`
- `/product-category/accessories/cradles/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Orphan page (has no incoming internal links)** (349 pages: /product/havis-100-watt-ac-power-supply-used-with-ds-dell-900-1100-series-docking-stations-lps-181/, /product/havis-3-5%E2%80%B3-heavy-duty-telescoping-pole-c-hdm-207/, /product/havis-self-checkout-printer-enclosure/, /product/havis-flexipole-compact-counter-mount-locking-stand-for-payment-terminals/, …)

349 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Pages hidden from Google (noindex/nofollow): confirm intent** (94 pages: /shop/product_brand-gamber-johnson-3-or-havis/page/33/, /shop/product_brand-gamber-johnson-3-or-havis/page/259/, /shop/product_brand-gamber-johnson-3-or-havis/page/28/, /shop/product_brand-gamber-johnson-3-or-havis/page/264/, …)

94 pages on ruggeddepot.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

## Skipped on purpose

- Indexable page not in sitemap (943): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

