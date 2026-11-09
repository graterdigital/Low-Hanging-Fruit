# Work orders: technikpackaging.com

Ahrefs Site Audit project 9704554 · crawl 2026-11-05 · health 90 · 46 active issue types → 26 work orders (3 decisions, 14 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 103 | 53 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 2 | Organization schema missing or incomplete | schema-fix | APPROVE (skill pending) | 1 | 37 | agency | Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 3 | Category page missing ItemList schema | schema-check | FLAG | 34 | 16 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 4 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 44 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page. |
| 5 | Orphan page (has no incoming internal links) | indexation-review | decide | 2 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 6 | Links to redirect, skipped by fix-redirect-links: no incoming internal links (sitemap or orphan entry) | manual | decide | 1 | 0 | agency | fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave. |
| 7 | Structured data has schema.org validation error | schema-fix | FLAG | 52 | 0 | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 8 | Product page missing Product schema | schema-check | FLAG | 4 | 0 | agency | Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages. |
| 9 | Pages fix-meta routed to [] | [] | FLAG | 3 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 10 | CSS file size too large | manual | FLAG | 3 | 0 | agency | Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket. |
| 11 | Links to redirect, skipped by fix-redirect-links: pagination /page/1/ comes from the theme template, not content | manual | FLAG | 2 | 0 | agency | Theme template edit: emit the archive root for page 1 (WordPress paginate_links does by default). Diff by hand. |
| 12 | wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings) | manual | FLAG | 2 | 0 | agency | Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-0957-fix-redirect-links-live-options.md. |
| 13 | Pages fix-meta routed to ['/product-category/custom-solutions/', '/category/uncategorized/', '/category/news/page/7/', '/cache-2/', '/news/page/4/', '/cache-3/', '/category/news/page/3/', '/news/page/5/', '/news/page/7/', '/product-category/uncategorized/', '/category/news/page/6/', '/category/snack-foods/', '/news/', '/shop/page/4/', '/category/dried-foods/', '/news/page/3/', '/product-category/packaging-equipment/cup-pod-fill-seal-machines/', '/news/page/8/', '/category/news/page/2/', '/news/page/2/', '/cache/', '/category/vertical-baggers/', '/shop/', '/category/news/page/5/', '/news/page/6/', '/category/industrial/', '/category/news/', '/category/pharmaceutical/', '/shop/page/2/', '/category/news/page/4/', '/shop/page/3/', '/product-category/industries/condiments/', '/product-category/packaging-equipment/automatic-bottling-lines/'] | ['/product-category/custom-solutions/', '/category/uncategorized/', '/category/news/page/7/', '/cache-2/', '/news/page/4/', '/cache-3/', '/category/news/page/3/', '/news/page/5/', '/news/page/7/', '/product-category/uncategorized/', '/category/news/page/6/', '/category/snack-foods/', '/news/', '/shop/page/4/', '/category/dried-foods/', '/news/page/3/', '/product-category/packaging-equipment/cup-pod-fill-seal-machines/', '/news/page/8/', '/category/news/page/2/', '/news/page/2/', '/cache/', '/category/vertical-baggers/', '/shop/', '/category/news/page/5/', '/news/page/6/', '/category/industrial/', '/category/news/', '/category/pharmaceutical/', '/shop/page/2/', '/category/news/page/4/', '/shop/page/3/', '/product-category/industries/condiments/', '/product-category/packaging-equipment/automatic-bottling-lines/'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 14 | Slow page | manual | FLAG | 1 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 15 | Noindex page in sitemap | indexation-review | APPROVE (skill pending) | 2 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 16 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 2 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 17 | 302 redirect | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 18 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 19 | 4XX page in sitemap | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 20 | Noindex in HTML and HTTP header | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 21 | Page has nofollow outgoing internal links | nofollow-audit | APPROVE (skill pending) | 1 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 22 | Page in multiple sitemaps | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 23 | Structured data has Google rich results validation error | schema-fix | APPROVE (skill pending) | 1 | 0 | agency | Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual |
| 24 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 7 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 25 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 7 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 26 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 5 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/` (37 traffic)
- `/product-category/custom-solutions/` (9 traffic)
- `/product-category/industries/condiments/` (4 traffic)
- `/product-category/packaging-equipment/automatic-bottling-lines/` (3 traffic)
- `/category/uncategorized/`
- `/product-category/industries/dry-foods/`
- `/product-category/industries/industrial/page/4/`
- `/contact-us/`
- `/product-category/industries/candy-packaging-equipment/`
- `/product-category/industries/liquids/`
- … 93 more in Ahrefs

### 2. Organization schema missing or incomplete

`issue:organization-schema-missing-or-incomplete` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (37 traffic)

### 3. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/product-category/custom-solutions/` (9 traffic)
- `/product-category/industries/condiments/` (4 traffic)
- `/product-category/packaging-equipment/automatic-bottling-lines/` (3 traffic)
- `/product-category/industries/dry-foods/`
- `/product-category/industries/candy-packaging-equipment/`
- `/product-category/industries/liquids/`
- `/product-category/packaging-equipment/stick-packers/`
- `/product-category/industries/pet-foods/`
- `/product-category/industries/frozen-foods/`
- `/cache-2/`
- … 24 more in Ahrefs

### 4. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page.

- `/privacy-policy/`
- `/terms-conditions/`
- `/2016/05/`
- `/cart/`
- `/2018/08/`
- `/2018/05/`
- `/2018/12/`
- `/my-account/`
- `/2017/04/`
- `/2017/09/`
- … 34 more in Ahrefs

### 5. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/product-category/uncategorized/`
- `/vertical-baggers-2/`

### 6. Links to redirect, skipped by fix-redirect-links: no incoming internal links (sitemap or orphan entry)

`redirect-links:no-incoming-internal-links-sitemap-or-or` · manual · decide · decider: agency · source: redirect-map-2026-10-29.json

fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave.

- `/checkout/`

### 7. Structured data has schema.org validation error

`issue:structured-data-has-schema-org-validation-error` · schema-fix · FLAG · decider: agency

Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit.

- `/product/triapex-hv2/`
- `/product/triapex-lds/`
- `/product/jw-ccm-av-tray-former/`
- `/product/dienst-hk-ii-n/`
- `/product/pegasus-premade-bag-filling-and-sealing-machine/`
- `/product/triapex-dr2a/`
- `/product/dienst-dls-i-iii/`
- `/product/dienst-hk-ii-a/`
- `/product/triapex-ds1b/`
- `/product/triapex-vxnd/`
- … 42 more in Ahrefs

### 8. Product page missing Product schema

`issue:product-page-missing-product-schema` · schema-check · FLAG · decider: agency

Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages.

- `/featured-product-spotlight-jw-ccm-mv/`
- `/featured-product-spotlight-triapex-hu/`
- `/featured-product-spotlight-triapex-hu-2/`
- `/featured-product-spotlight-jw-ccm-mv-2/`

### 9. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `noindex`
- `non-200`
- `homepage title`

### 10. CSS file size too large

`issue:css-file-size-too-large` · manual · FLAG · decider: agency

Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket.

- `/wp-content/cache/min/1/wp-content/themes/technikpackag/assets/css/custom.css?ver=1784556209`
- `/wp-content/cache/min/1/wp-includes/css/dashicons.min.css?ver=1784556209`
- `/wp-content/cache/min/1/wp-content/themes/technikpackag/assets/css/foundation.css?ver=1784556209`

### 11. Links to redirect, skipped by fix-redirect-links: pagination /page/1/ comes from the theme template, not content

`redirect-links:pagination-page-1-comes-from-the-theme-t` · manual · FLAG · decider: agency · source: redirect-map-2026-10-29.json

Theme template edit: emit the archive root for page 1 (WordPress paginate_links does by default). Diff by hand.

- `/news/page/1/` (7 links)
- `/category/news/page/1/` (6 links)

### 12. wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings)

`redirect-links:wp-options` · manual · FLAG · decider: agency · source: 2026-10-30-0957-fix-redirect-links-live-options.md

Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-0957-fix-redirect-links-live-options.md.

- `clarity_collect_batch`
- `options_text_under`

### 13. Pages fix-meta routed to ['/product-category/custom-solutions/', '/category/uncategorized/', '/category/news/page/7/', '/cache-2/', '/news/page/4/', '/cache-3/', '/category/news/page/3/', '/news/page/5/', '/news/page/7/', '/product-category/uncategorized/', '/category/news/page/6/', '/category/snack-foods/', '/news/', '/shop/page/4/', '/category/dried-foods/', '/news/page/3/', '/product-category/packaging-equipment/cup-pod-fill-seal-machines/', '/news/page/8/', '/category/news/page/2/', '/news/page/2/', '/cache/', '/category/vertical-baggers/', '/shop/', '/category/news/page/5/', '/news/page/6/', '/category/industrial/', '/category/news/', '/category/pharmaceutical/', '/shop/page/2/', '/category/news/page/4/', '/shop/page/3/', '/product-category/industries/condiments/', '/product-category/packaging-equipment/automatic-bottling-lines/']

`fix-meta:product-category-custom-solutions-catego` · ['/product-category/custom-solutions/', '/category/uncategorized/', '/category/news/page/7/', '/cache-2/', '/news/page/4/', '/cache-3/', '/category/news/page/3/', '/news/page/5/', '/news/page/7/', '/product-category/uncategorized/', '/category/news/page/6/', '/category/snack-foods/', '/news/', '/shop/page/4/', '/category/dried-foods/', '/news/page/3/', '/product-category/packaging-equipment/cup-pod-fill-seal-machines/', '/news/page/8/', '/category/news/page/2/', '/news/page/2/', '/cache/', '/category/vertical-baggers/', '/shop/', '/category/news/page/5/', '/news/page/6/', '/category/industrial/', '/category/news/', '/category/pharmaceutical/', '/shop/page/2/', '/category/news/page/4/', '/shop/page/3/', '/product-category/industries/condiments/', '/product-category/packaging-equipment/automatic-bottling-lines/'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`

### 14. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/category/news/page/4/`

### 15. Noindex page in sitemap

`issue:noindex-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/cart/`
- `/my-account/`

### 16. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/privacy-policy/`
- `/terms-conditions/`

### 17. 302 redirect

`issue:302-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/checkout/`

### 18. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/checkout/`

### 19. 4XX page in sitemap

`issue:4xx-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/author/tatelyngraterdigital-com/`

### 20. Noindex in HTML and HTTP header

`issue:noindex-in-html-and-http-header` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/my-account/lost-password/`

### 21. Page has nofollow outgoing internal links

`issue:page-has-nofollow-outgoing-internal-links` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/featured-product-spotlight-jw-ccm-mv-2/`

### 22. Page in multiple sitemaps

`issue:page-in-multiple-sitemaps` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/shop/`

### 23. Structured data has Google rich results validation error

`issue:structured-data-has-google-rich-results-validation-error` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual

- `/terms-conditions/`

### 24. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/product/triapex-hv2d-premium-recloseable-top-bagger/`
- `/author/tatelyngraterdigital-com/`
- `/product-category/stick-pack/`
- `/product-category/bottling-lines/`
- `/product/pick-place-systems/`
- `/product-category/pharmaceutical/`
- `/product-category/stickpack-machines-sachet/`

### 25. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/product/triapex-hv2d-premium-recloseable-top-bagger/`
- `/author/tatelyngraterdigital-com/`
- `/product-category/stick-pack/`
- `/product-category/bottling-lines/`
- `/product/pick-place-systems/`
- `/product-category/pharmaceutical/`
- `/product-category/stickpack-machines-sachet/`

### 26. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/industries-that-benefit-most-from-automated-packaging-machinery-2/`
- `/automated-packing-equipment/`
- `/stick-packers-cater-consumers-move/`
- `/considering-automating-your-product-packing-technik-packaging-machinery-offers-custom-solutions/`
- `/automating-product-packing-custom-solutions/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (44 pages: /privacy-policy/, /terms-conditions/, /2016/05/, /cart/, …)

44 pages on technikpackaging.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

**Orphan page (has no incoming internal links)** (2 pages: /product-category/uncategorized/, /vertical-baggers-2/)

2 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

## Skipped on purpose

- Indexable page not in sitemap (44): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

