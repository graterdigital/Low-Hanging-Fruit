# Work orders: setcomcorp.com

Ahrefs Site Audit project 10610051 · crawl 2026-11-04 · health 94 · 42 active issue types → 23 work orders (5 decisions, 9 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Inconsistent AI training bot policy | ai-discoverability | decide | 113 | 265 | client | robots.txt groups disagree; the managed block replaces them (skill). |
| 2 | Indexable page blocked from some AI search bots | ai-discoverability | decide | 113 | 265 | client | Set the client's ai: policy, then apply the managed robots.txt block (skill). |
| 3 | Slow page | manual | FLAG | 156 | 250 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 4 | H1 tag missing or empty | manual | FLAG | 68 | 24 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 5 | Product page missing Product schema | schema-check | FLAG | 30 | 11 | agency | Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages. |
| 6 | Category page missing ItemList schema | schema-check | FLAG | 4 | 6 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 7 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 51 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 8 | Orphan page (has no incoming internal links) | indexation-review | decide | 25 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 9 | Links to redirect, skipped by fix-redirect-links: date archive redirecting to the homepage | redirect-rules | decide | 11 | 0 | client | Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order. |
| 10 | Slow server response for AI crawlers | hosting/cache | FLAG | 12 | 0 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 11 | wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings) | manual | FLAG | 7 | 0 | agency | Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1056-fix-redirect-links-live-options.md. |
| 12 | Pages fix-meta routed to [] | [] | FLAG | 3 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 13 | Pages fix-meta routed to ['/products/', '/2026-police-motorcycle-training-events/', '/blog/', '/products/accessories/', '/blog/page/2/', '/shop/page/2/', '/dealers/', '/shop/page/3/'] | ['/products/', '/2026-police-motorcycle-training-events/', '/blog/', '/products/accessories/', '/blog/page/2/', '/shop/page/2/', '/dealers/', '/shop/page/3/'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 14 | CSS file size too large | manual | FLAG | 1 | 0 | agency | Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket. |
| 15 | Indexable page not in sitemap | indexation-review | APPROVE (skill pending) | 4 | 0 | agency | Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 16 | Noindex page in sitemap | indexation-review | APPROVE (skill pending) | 4 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 17 | Structured data has Google rich results validation error | schema-fix | APPROVE (skill pending) | 2 | 0 | agency | Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual |
| 18 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 19 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 3 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 20 | X (Twitter) card incomplete | fix-social-tags | AUTO (skill pending) | 3 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 21 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 14 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 22 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 10 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 23 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 9 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Inconsistent AI training bot policy

`issue:inconsistent-ai-training-bot-policy` · ai-discoverability · decide · decider: client

robots.txt groups disagree; the managed block replaces them (skill).

- `/` (222 traffic)
- `/industry/police-motor/` (9 traffic)
- `/police-motorcycle-rodeo-course-maps/` (8 traffic)
- `/products/headsets/5b-headset/` (7 traffic)
- `/products/` (6 traffic)
- `/industry/fire/` (4 traffic)
- `/products/systems/900-max/` (3 traffic)
- `/support/` (3 traffic)
- `/2026-police-motorcycle-training-events/` (2 traffic)
- `/products/headsets/liberatormax-fire/` (1 traffic)
- … 103 more in Ahrefs

### 2. Indexable page blocked from some AI search bots

`issue:indexable-page-blocked-from-some-ai-search-bots` · ai-discoverability · decide · decider: client

Set the client's ai: policy, then apply the managed robots.txt block (skill).

- `/` (222 traffic)
- `/industry/police-motor/` (9 traffic)
- `/police-motorcycle-rodeo-course-maps/` (8 traffic)
- `/products/headsets/5b-headset/` (7 traffic)
- `/products/` (6 traffic)
- `/industry/fire/` (4 traffic)
- `/products/systems/900-max/` (3 traffic)
- `/support/` (3 traffic)
- `/2026-police-motorcycle-training-events/` (2 traffic)
- `/products/headsets/liberatormax-fire/` (1 traffic)
- … 103 more in Ahrefs

### 3. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/` (222 traffic)
- `/industry/police-motor/` (9 traffic)
- `/products/headsets/5b-headset/` (7 traffic)
- `/products/` (6 traffic)
- `/products/systems/900-max/` (3 traffic)
- `/2026-police-motorcycle-training-events/` (2 traffic)
- `/products/headsets/liberatormax-fire/` (1 traffic)
- `/portable-radio-adapter-cables/`
- `/product/right-side-slide-in-snap-plate/`
- `/industry/arff/`
- … 146 more in Ahrefs

### 4. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/police-motorcycle-rodeo-course-maps/` (8 traffic)
- `/products/` (6 traffic)
- `/industry/fire/` (4 traffic)
- `/support/` (3 traffic)
- `/2026-police-motorcycle-training-events/` (2 traffic)
- `/products/headsets/liberatormax-fire/` (1 traffic)
- `/portable-radio-adapter-cables/`
- `/industry/arff/`
- `/contact-thanks/`
- `/quote/`
- … 58 more in Ahrefs

### 5. Product page missing Product schema

`issue:product-page-missing-product-schema` · schema-check · FLAG · decider: agency

Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages.

- `/products/headsets/5b-headset/` (7 traffic)
- `/products/systems/900-max/` (3 traffic)
- `/products/headsets/liberatormax-fire/` (1 traffic)
- `/products/accessories/radio-routing-controller/`
- `/products/accessories/radio-cables/`
- `/products/police-motor/`
- `/products/accessories/vented-headset-cup/`
- `/products/police-motor/half-shell-helmet-kit/`
- `/products/accessories/clip-on-liberator-max/`
- `/industry/police-motor-tatelyn-test/`
- … 20 more in Ahrefs

### 6. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/products/` (6 traffic)
- `/portable-radio-adapter-cables/`
- `/products/accessories/`
- `/radio-designator-list/`

### 7. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/product/right-side-slide-in-snap-plate/`
- `/product/outer-acoustical-pad-for-cs-style-headsets/`
- `/tag/nascar/`
- `/product/left-side-slide-in-snap-plate/`
- `/tag/fire-department-communications/`
- `/product/inner-acoustical-pad-for-cs-style-headsets/`
- `/tag/travis-county-esd-12/`
- `/tag/agricultural-research/`
- `/tag/setcom/`
- `/tag/communication/`
- … 41 more in Ahrefs

### 8. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/contact-thanks/`
- `/thanks-for-requesting-a-quote/`
- `/products/police-motor/`
- `/industry/fire-rescue-boat/`
- `/industry/police-boat/`
- `/2023-police-motorcycle-training-events/`
- `/industry/incident-command/`
- `/industry/work-boats/`
- `/products/accessories/`
- `/industry/snow-plows/`
- … 15 more in Ahrefs

### 9. Links to redirect, skipped by fix-redirect-links: date archive redirecting to the homepage

`redirect-links:date-archive-redirecting-to-the-homepage` · redirect-rules · decide · decider: client · source: redirect-map-2026-10-28.json

Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order.

- `/2026/10/21/` (2 links)
- `/2026/06/22/` (1 links)
- `/2026/06/04/` (1 links)
- `/2026/05/04/` (1 links)
- `/2026/10/07/` (1 links)
- `/2026/05/18/` (1 links)
- `/2026/01/09/` (1 links)
- `/2026/01/28/` (1 links)
- `/2026/09/10/` (1 links)
- `/2026/09/24/` (1 links)
- … 1 more in Ahrefs

### 10. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/products/accessories/radio-cables/`
- `/warranty/`
- `/industry/drone-operations/`
- `/blog/page/2/`
- `/products/headsets/6b-headset/`
- `/products/headsets/8b-headset/`
- `/industry/towing/`
- `/products/accessories/headset-strap-extension/`
- `/shop/page/2/`
- `/products/police-motor/wired-cable-kit-portable-only/`
- … 2 more in Ahrefs

### 11. wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings)

`redirect-links:wp-options` · manual · FLAG · decider: agency · source: 2026-10-30-1056-fix-redirect-links-live-options.md

Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1056-fix-redirect-links-live-options.md.

- `clarity_collect_batch`
- `clarity_collect_batch`
- `monsterinsights_report_data_overview`
- `clarity_collect_batch`
- `clarity_collect_batch`
- `ywraq_return_to_shop_url`
- `ywraq_return_to_shop_after_sent_the_request_url`

### 12. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-28.json

See the fix-meta report's 'Routed elsewhere' section.

- `noindex`
- `non-200`
- `homepage title`

### 13. Pages fix-meta routed to ['/products/', '/2026-police-motorcycle-training-events/', '/blog/', '/products/accessories/', '/blog/page/2/', '/shop/page/2/', '/dealers/', '/shop/page/3/']

`fix-meta:products-2026-police-motorcycle-training` · ['/products/', '/2026-police-motorcycle-training-events/', '/blog/', '/products/accessories/', '/blog/page/2/', '/shop/page/2/', '/dealers/', '/shop/page/3/'] · FLAG · decider: agency · source: meta-2026-10-28.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`

### 14. CSS file size too large

`issue:css-file-size-too-large` · manual · FLAG · decider: agency

Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket.

- `/wp-content/cache/min/1/wp-includes/css/dashicons.min.css?ver=1793160607`

### 15. Indexable page not in sitemap

`issue:indexable-page-not-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/blog/page/2/`
- `/shop/page/2/`
- `/shop/`
- `/shop/page/3/`

### 16. Noindex page in sitemap

`issue:noindex-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/product-category/wired-headset-system/`
- `/product-category/liberatormax-wireless-accessories/`
- `/product-category/liberatormax-wireless-consumables/`
- `/product-category/police-motor-system/`

### 17. Structured data has Google rich results validation error

`issue:structured-data-has-google-rich-results-validation-error` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual

- `/product/overhead-support-strap-13/`
- `/product/overhead-support-strap-19/`

### 18. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/2025-police-motorcycle-training-events/`

### 19. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/shop/page/2/`
- `/shop/`
- `/shop/page/3/`

### 20. X (Twitter) card incomplete

`issue:x-twitter-card-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/shop/page/2/`
- `/shop/`
- `/shop/page/3/`

### 21. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/products/950-977-vehicle-intercom-system/`
- `/products/single-person-wireless-intercom-system/`
- `/index.php?gf-download=2026%2F02%2FPeach-State-Flyer.png&form-id=6&field-id=25&hash=4ab0857e2222251b41a49f1730466f49d28da8cdac162551daeb478e5400ddc6`
- `/index.php?gf-download=2025%2F12%2FIMG_9072.png&form-id=6&field-id=25&hash=c901944ab0f4dacfc0b482539b3c52cf2e66b8e82cc5565ee557f5c13b243ebd`
- `/index.php?gf-download=2026%2F01%2F2026-Panther-Prowl-Motorcycle-Rodeo-Motorman-Tribute-Flier-final.pdf&form-id=6&field-id=25&hash=254803182fee7d35de1eef6ea0e70b4bd238d82d937bd3b9b51e8188f7861cf9`
- `/index.php?gf-download=2025%2F11%2F2026-Bold-City-flyer.png&form-id=6&field-id=25&hash=7aadf87557860352a8918a5505287aa887ceeb2d5dc7b8364a0059732dd68693`
- `/products/systems/1310-2/`
- `/index.php?gf-download=2025%2F12%2FSMART-2026-FLYER.pdf&form-id=6&field-id=25&hash=d94ce7a0ce6cd9501e8dbf3ab9893e2ce68d2f597d35ec658ed2cd26b02f8ba0`
- `/fire-multi-user-wireless-intercom-headset-system.html`
- `/products/liberatormax%F0%9F%94%A5/`
- … 4 more in Ahrefs

### 22. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/solutions/`
- `/2023-police-motorcycle-training-events/`
- `/industry/incident-command/`
- `/blog/page/2/`
- `/industry/wildland-brush-truck/`
- `/industry/crane/`
- `/products/headsets/liberatormax/`
- `/industry/drilling/`
- `/industry/construction/`
- `/industry/commercial-fishing/`

### 23. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/products/950-977-vehicle-intercom-system/`
- `/products/single-person-wireless-intercom-system/`
- `/products/systems/1310-2/`
- `/fire-multi-user-wireless-intercom-headset-system.html`
- `/products/liberatormax%F0%9F%94%A5/`
- `/products/liberatormax-headset/`
- `/products/police-motor/liberator-wireless/`
- `/blog/page/3/`
- `/2024-police-motorcycle-training-events/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Inconsistent AI training bot policy** (113 pages: /, /industry/police-motor/, /police-motorcycle-rodeo-course-maps/, /products/headsets/5b-headset/, …)

Some AI crawlers are blocked from setcomcorp.com. Allowing AI search bots (ChatGPT, Perplexity, Claude search) lets those tools cite the site in their answers; allowing training bots (GPTBot, ClaudeBot, Google-Extended) puts the content into future models. Our default is allow both; blocking training bots does not affect Google Search. Tell us if you want training bots blocked and we will set it.

**Indexable page blocked from some AI search bots** (113 pages: /, /industry/police-motor/, /police-motorcycle-rodeo-course-maps/, /products/headsets/5b-headset/, …)

Some AI crawlers are blocked from setcomcorp.com. Allowing AI search bots (ChatGPT, Perplexity, Claude search) lets those tools cite the site in their answers; allowing training bots (GPTBot, ClaudeBot, Google-Extended) puts the content into future models. Our default is allow both; blocking training bots does not affect Google Search. Tell us if you want training bots blocked and we will set it.

**Pages hidden from Google (noindex/nofollow): confirm intent** (51 pages: /product/right-side-slide-in-snap-plate/, /product/outer-acoustical-pad-for-cs-style-headsets/, /tag/nascar/, /product/left-side-slide-in-snap-plate/, …)

51 pages on setcomcorp.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

**Orphan page (has no incoming internal links)** (25 pages: /contact-thanks/, /thanks-for-requesting-a-quote/, /products/police-motor/, /industry/fire-rescue-boat/, …)

25 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Links to redirect, skipped by fix-redirect-links: date archive redirecting to the homepage** (11 pages: /2026/10/21/, /2026/06/22/, /2026/06/04/, /2026/05/04/, …)

11 old URLs on setcomcorp.com currently redirect to the homepage, which loses visitors who click an old link. For each one we need the page it should go to now (or confirmation that nothing replaces it, in which case we remove the links).

