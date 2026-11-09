# Work orders: nativecustomstone.com

Ahrefs Site Audit project 9704543 · crawl 2026-11-05 · health 88 · 63 active issue types → 33 work orders (5 decisions, 17 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Page has nofollow outgoing internal links | nofollow-audit | APPROVE (skill pending) | 161 | 42 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 2 | Indexable page not in sitemap | indexation-review | APPROVE (skill pending) | 87 | 35 | agency | Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 3 | Organization schema missing or incomplete | schema-fix | APPROVE (skill pending) | 1 | 34 | agency | Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 4 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 407 | 2 (top 200 of 407) | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 5 | Indexable page became non-indexable | indexation-review | APPROVE (skill pending) | 52 | 2 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 6 | Canonical from HTTPS to HTTP | review | ? | 142 | 2 | agency | Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster) |
| 7 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 9 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 8 | Orphan page (has no incoming internal links) | indexation-review | decide | 9 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 9 | Orphan page (has no incoming internal links)  (non-indexable pages) | indexation-review | decide | 4 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 10 | Links to redirect, skipped by fix-redirect-links: date archive redirecting to the homepage | redirect-rules | decide | 2 | 0 | client | Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order. |
| 11 | Links to redirect, skipped by fix-redirect-links: no incoming internal links (sitemap or orphan entry) | manual | decide | 1 | 0 | agency | fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave. |
| 12 | Slow page | manual | FLAG | 179 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 13 | H1 tag missing or empty | manual | FLAG | 39 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 14 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 20 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 15 | Links to redirect, skipped by fix-redirect-links: pagination /page/1/ comes from the theme template, not content | manual | FLAG | 15 | 0 | agency | Theme template edit: emit the archive root for page 1 (WordPress paginate_links does by default). Diff by hand. |
| 16 | CSS file size too large | manual | FLAG | 4 | 0 | agency | Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket. |
| 17 | Pages fix-meta routed to [] | [] | FLAG | 3 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 18 | Pages fix-meta routed to ['/category/custom-stone-bathroom/', '/category/manufactured-stone/page/3/', '/category/custom-stone-fireplace/page/2/', '/category/faux-stone-veneer/', '/category/maintenance-and-installation/page/3/', '/category/faux-stone-paneling/', '/category/manufactured-stone-fireplace/', '/category/tips-and-tricks/', '/category/custom-stone-kitchen/', '/category/maintenance-and-installation/diy/', '/category/installation-and-care/', '/category/stone/', '/category/go-stone-panels/', '/category/go-stone-panels/page/2/', '/category/go-brick-brick-veneer/', '/category/uncategorized/', '/category/adhered-stone-veneer/', '/category/manufactured-stone/', '/category/maintenance-and-installation/', '/category/panel/', '/category/faux-stone-paneling/page/2/', '/category/maintenance-and-installation/diy/page/2/', '/category/custom-stone-accents/', '/category/custom-stone-fireplace/', '/category/general/', '/category/maintenance-and-installation/diy/page/3/', '/category/maintenance-and-installation/tips-and-advice/page/2/', '/category/custom-stone-kitchen/page/2/', '/category/faux-stone-veneer/page/2/', '/category/faux-stone-veneer/page/3/', '/category/maintenance-and-installation/page/5/', '/category/maintenance-and-installation/page/4/', '/category/manufactured-stone2/', '/stone/', '/category/maintenance-and-installation/tips-and-advice/', '/category/uncategorized/page/2/', '/category/maintenance-and-installation/page/2/', '/category/manufactured-stone/page/2/', '/category/manufactured-stone/page/4/'] | ['/category/custom-stone-bathroom/', '/category/manufactured-stone/page/3/', '/category/custom-stone-fireplace/page/2/', '/category/faux-stone-veneer/', '/category/maintenance-and-installation/page/3/', '/category/faux-stone-paneling/', '/category/manufactured-stone-fireplace/', '/category/tips-and-tricks/', '/category/custom-stone-kitchen/', '/category/maintenance-and-installation/diy/', '/category/installation-and-care/', '/category/stone/', '/category/go-stone-panels/', '/category/go-stone-panels/page/2/', '/category/go-brick-brick-veneer/', '/category/uncategorized/', '/category/adhered-stone-veneer/', '/category/manufactured-stone/', '/category/maintenance-and-installation/', '/category/panel/', '/category/faux-stone-paneling/page/2/', '/category/maintenance-and-installation/diy/page/2/', '/category/custom-stone-accents/', '/category/custom-stone-fireplace/', '/category/general/', '/category/maintenance-and-installation/diy/page/3/', '/category/maintenance-and-installation/tips-and-advice/page/2/', '/category/custom-stone-kitchen/page/2/', '/category/faux-stone-veneer/page/2/', '/category/faux-stone-veneer/page/3/', '/category/maintenance-and-installation/page/5/', '/category/maintenance-and-installation/page/4/', '/category/manufactured-stone2/', '/stone/', '/category/maintenance-and-installation/tips-and-advice/', '/category/uncategorized/page/2/', '/category/maintenance-and-installation/page/2/', '/category/manufactured-stone/page/2/', '/category/manufactured-stone/page/4/'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 19 | Category page missing ItemList schema | schema-check | FLAG | 1 | 0 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 20 | Product page missing Product schema | schema-check | FLAG | 1 | 0 | agency | Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages. |
| 21 | Canonical from HTTP to HTTPS | redirect-rules | APPROVE (skill pending) | 147 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 22 | Non-canonical page in sitemap | indexation-review | APPROVE (skill pending) | 60 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 23 | Canonical URL has no incoming internal links | indexation-review | APPROVE (skill pending) | 8 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 24 | Noindex page in sitemap | indexation-review | APPROVE (skill pending) | 2 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 25 | Links to redirect, skipped by fix-redirect-links: author archive | indexation-review | APPROVE | 2 | 0 | agency | Yoast > Search Appearance > Archives: disable author archives (or the author sitemap); one setting removes them all. |
| 26 | 302 redirect | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 27 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 28 | HTTPS to HTTP redirect | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 29 | Page in multiple sitemaps | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 30 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 2 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 31 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 2 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 32 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 1 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 33 | Page has links to broken page  (non-indexable pages) | fix-broken-links | AUTO/APPROVE (skill pending) | 1 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Page has nofollow outgoing internal links

`issue:page-has-nofollow-outgoing-internal-links` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/` (34 traffic)
- `/castle-rock/` (7 traffic)
- `/rubble-stone/` (1 traffic)
- `/roi-when-using-manufactured-stone/`
- `/check-out-how-this-diyer-used-go-stone-to-bring-the-outdoors-in/`
- `/how-to-create-a-backyard-firepit-with-manufactured-stone/`
- `/see-native-custom-stones-customfit-panels-on-food-networks-the-kitchen/`
- `/how-to-use-native-custom-stones-go-stone-as-a-decorating-tool/`
- `/stone-veneer-panels-can-be-a-weekend-project/`
- `/native-custom-stone-partners-with-builddirect-to-distribute-products/`
- … 151 more in Ahrefs

### 2. Indexable page not in sitemap

`issue:indexable-page-not-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/` (34 traffic)
- `/rubble-stone/` (1 traffic)
- `/roi-when-using-manufactured-stone/`
- `/how-to-create-a-backyard-firepit-with-manufactured-stone/`
- `/stone-veneer-panels-can-be-a-weekend-project/`
- `/category/manufactured-stone/page/3/`
- `/product/go-stone-single-electric-box-accent/`
- `/how-to-avoid-weather-damage-to-manufactured-stone-veneer/`
- `/why-you-should-use-stack-stone-veneer-for-your-outdoor-kitchen/`
- `/blog/page/7/`
- … 77 more in Ahrefs

### 3. Organization schema missing or incomplete

`issue:organization-schema-missing-or-incomplete` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (34 traffic)

### 4. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/ledge-stone/` (2 traffic)
- `/product/stack-stone-sample-board/`
- `/roi-when-using-manufactured-stone/5/`
- `/this-article-could-change-your-mind-about-manufactured-stone/`
- `/use-native-custom-stones-go-brick-for-a-magnificent-makeover/8/`
- `/bigger-in-real-life-fireplace-installation-using-go-stone/8/`
- `/use-go-stone-for-indoor-custom-stone-work/`
- `/the-importance-of-sealing-your-manufactured-stone-veneer/`
- `/why-should-you-choose-manufactured-stone-over-natural-stone/`
- `/go-brick-and-go-stone-for-diy-projects/2/`
- … 397 more in Ahrefs

### 5. Indexable page became non-indexable

`issue:indexable-page-became-non-indexable` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/ledge-stone/` (2 traffic)
- `/the-importance-of-sealing-your-manufactured-stone-veneer/`
- `/why-should-you-choose-manufactured-stone-over-natural-stone/`
- `/how-to-create-a-beautiful-custom-stone-patio/`
- `/warranty/`
- `/go-brick-and-go-stone-for-diy-projects/`
- `/how-to-care-for-a-cultured-stone-fireplace/`
- `/go-diy-with-go-stone-manufactured-stone-for-interior-walls/`
- `/go-brick-veneer/`
- `/category/go-brick-brick-veneer/`
- … 42 more in Ahrefs

### 6. Canonical from HTTPS to HTTP

`issue:canonical-from-https-to-http` · review · ? · decider: agency

Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster)

- `/ledge-stone/` (2 traffic)
- `/this-article-could-change-your-mind-about-manufactured-stone/`
- `/use-native-custom-stones-go-brick-for-a-magnificent-makeover/8/`
- `/bigger-in-real-life-fireplace-installation-using-go-stone/8/`
- `/use-go-stone-for-indoor-custom-stone-work/`
- `/use-native-custom-stones-go-brick-for-a-magnificent-makeover/9/`
- `/the-beauty-of-river-rock-stone-veneer/`
- `/custom-stone-for-kitchens-bathrooms/`
- `/choosing-the-right-manufactured-stone-fireplace-veneer/`
- `/the-advantages-of-faux-stone-paneling/`
- … 132 more in Ahrefs

### 7. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/privacy-policy/`
- `/cart/`
- `/my-account/lost-password/`
- `/tag/custom-stone/page/3/`
- `/my-account/`
- `/tag/custom-stone/page/2/`
- `/tag/custom-stone/`
- … 2 more in Ahrefs

### 8. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/category/custom-stone-bathroom/`
- `/category/manufactured-stone-fireplace/`
- `/category/installation-and-care/`
- `/category/adhered-stone-veneer/`
- `/leed-projects/`
- `/category/panel/`
- `/category/custom-stone-accents/`
- `/category/general/`
- `/category/manufactured-stone2/`

### 9. Orphan page (has no incoming internal links)  (non-indexable pages)

`issue:orphan-page-has-no-incoming-internal-links-nonindexable` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/warranty/`
- `/category/go-brick-brick-veneer/`
- `/category/stone/`
- `/category/tips-and-tricks/`

### 10. Links to redirect, skipped by fix-redirect-links: date archive redirecting to the homepage

`redirect-links:date-archive-redirecting-to-the-homepage` · redirect-rules · decide · decider: client · source: redirect-map-2026-10-29.json

Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order.

- `/2020/02/15/` (1 links)
- `/2020/02/15/` (1 links)

### 11. Links to redirect, skipped by fix-redirect-links: no incoming internal links (sitemap or orphan entry)

`redirect-links:no-incoming-internal-links-sitemap-or-or` · manual · decide · decider: agency · source: redirect-map-2026-10-29.json

fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave.

- `/checkout/`

### 12. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/roi-when-using-manufactured-stone/`
- `/the-importance-of-sealing-your-manufactured-stone-veneer/`
- `/why-should-you-choose-manufactured-stone-over-natural-stone/`
- `/stone-veneer-panels-can-be-a-weekend-project/`
- `/how-to-create-a-beautiful-custom-stone-patio/`
- `/the-beauty-of-river-rock-stone-veneer/`
- `/the-advantages-of-using-go-stone-panels-for-your-home/3/`
- `/roi-when-using-manufactured-stone/3/`
- `/how-to-install-diy-stone-panels-go-stone-the-easy-way/8/`
- `/the-benefits-of-manufactured-vs-natural-stone/2/`
- … 169 more in Ahrefs

### 13. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/category/custom-stone-bathroom/`
- `/category/manufactured-stone/page/3/`
- `/category/custom-stone-fireplace/page/2/`
- `/category/faux-stone-veneer/`
- `/category/maintenance-and-installation/page/3/`
- `/category/faux-stone-paneling/`
- `/category/manufactured-stone-fireplace/`
- `/category/tips-and-tricks/`
- `/category/custom-stone-kitchen/`
- `/category/maintenance-and-installation/diy/`
- … 29 more in Ahrefs

### 14. H1 tag missing or empty  (non-indexable pages)

`issue:h1-tag-missing-or-empty-nonindexable` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/category/maintenance-and-installation/`
- `/category/go-brick-brick-veneer/`
- `/category/stone/`
- `/category/go-stone-panels/`
- `/category/maintenance-and-installation/tips-and-advice/page/2/`
- `/category/maintenance-and-installation/page/5/`
- `/category/maintenance-and-installation/page/4/`
- `/lunch-learn-program/`
- `/category/custom-stone-kitchen/`
- `/my-account/lost-password/`
- … 10 more in Ahrefs

### 15. Links to redirect, skipped by fix-redirect-links: pagination /page/1/ comes from the theme template, not content

`redirect-links:pagination-page-1-comes-from-the-theme-t` · manual · FLAG · decider: agency · source: redirect-map-2026-10-29.json

Theme template edit: emit the archive root for page 1 (WordPress paginate_links does by default). Diff by hand.

- `/category/maintenance-and-installation/page/1/` (4 links)
- `/category/maintenance-and-installation/page/1/` (4 links)
- `/category/manufactured-stone/page/1/` (3 links)
- `/category/maintenance-and-installation/diy/page/1/` (2 links)
- `/tag/custom-stone/page/1/` (2 links)
- `/category/faux-stone-veneer/page/1/` (2 links)
- `/category/faux-stone-paneling/page/1/` (1 links)
- `/category/go-stone-panels/page/1/` (1 links)
- `/category/custom-stone-fireplace/page/1/` (1 links)
- `/category/custom-stone-kitchen/page/1/` (1 links)
- … 5 more in Ahrefs

### 16. CSS file size too large

`issue:css-file-size-too-large` · manual · FLAG · decider: agency

Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket.

- `/wp-content/cache/min/1/wp-content/themes/nativecustomstone/assets/css/foundation.css?ver=1793270021`
- `/wp-content/cache/min/1/wp-content/plugins/gravityforms/assets/css/dist/gravity-forms-theme-framework.min.css?ver=1793270021`
- `/wp-content/cache/min/1/wp-content/themes/nativecustomstone/assets/css/foundation.css?ver=1793270021`
- `/wp-content/cache/min/1/wp-content/plugins/gravityforms/assets/css/dist/gravity-forms-theme-framework.min.css?ver=1793270021`

### 17. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `noindex`
- `non-200`
- `homepage title`

### 18. Pages fix-meta routed to ['/category/custom-stone-bathroom/', '/category/manufactured-stone/page/3/', '/category/custom-stone-fireplace/page/2/', '/category/faux-stone-veneer/', '/category/maintenance-and-installation/page/3/', '/category/faux-stone-paneling/', '/category/manufactured-stone-fireplace/', '/category/tips-and-tricks/', '/category/custom-stone-kitchen/', '/category/maintenance-and-installation/diy/', '/category/installation-and-care/', '/category/stone/', '/category/go-stone-panels/', '/category/go-stone-panels/page/2/', '/category/go-brick-brick-veneer/', '/category/uncategorized/', '/category/adhered-stone-veneer/', '/category/manufactured-stone/', '/category/maintenance-and-installation/', '/category/panel/', '/category/faux-stone-paneling/page/2/', '/category/maintenance-and-installation/diy/page/2/', '/category/custom-stone-accents/', '/category/custom-stone-fireplace/', '/category/general/', '/category/maintenance-and-installation/diy/page/3/', '/category/maintenance-and-installation/tips-and-advice/page/2/', '/category/custom-stone-kitchen/page/2/', '/category/faux-stone-veneer/page/2/', '/category/faux-stone-veneer/page/3/', '/category/maintenance-and-installation/page/5/', '/category/maintenance-and-installation/page/4/', '/category/manufactured-stone2/', '/stone/', '/category/maintenance-and-installation/tips-and-advice/', '/category/uncategorized/page/2/', '/category/maintenance-and-installation/page/2/', '/category/manufactured-stone/page/2/', '/category/manufactured-stone/page/4/']

`fix-meta:category-custom-stone-bathroom-category-` · ['/category/custom-stone-bathroom/', '/category/manufactured-stone/page/3/', '/category/custom-stone-fireplace/page/2/', '/category/faux-stone-veneer/', '/category/maintenance-and-installation/page/3/', '/category/faux-stone-paneling/', '/category/manufactured-stone-fireplace/', '/category/tips-and-tricks/', '/category/custom-stone-kitchen/', '/category/maintenance-and-installation/diy/', '/category/installation-and-care/', '/category/stone/', '/category/go-stone-panels/', '/category/go-stone-panels/page/2/', '/category/go-brick-brick-veneer/', '/category/uncategorized/', '/category/adhered-stone-veneer/', '/category/manufactured-stone/', '/category/maintenance-and-installation/', '/category/panel/', '/category/faux-stone-paneling/page/2/', '/category/maintenance-and-installation/diy/page/2/', '/category/custom-stone-accents/', '/category/custom-stone-fireplace/', '/category/general/', '/category/maintenance-and-installation/diy/page/3/', '/category/maintenance-and-installation/tips-and-advice/page/2/', '/category/custom-stone-kitchen/page/2/', '/category/faux-stone-veneer/page/2/', '/category/faux-stone-veneer/page/3/', '/category/maintenance-and-installation/page/5/', '/category/maintenance-and-installation/page/4/', '/category/manufactured-stone2/', '/stone/', '/category/maintenance-and-installation/tips-and-advice/', '/category/uncategorized/page/2/', '/category/maintenance-and-installation/page/2/', '/category/manufactured-stone/page/2/', '/category/manufactured-stone/page/4/'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`

### 19. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/stone/`

### 20. Product page missing Product schema

`issue:product-page-missing-product-schema` · schema-check · FLAG · decider: agency

Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages.

- `/product/double-light-switch-box-accent/`

### 21. Canonical from HTTP to HTTPS

`issue:canonical-from-http-to-https` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/product/stack-stone-sample-board/`
- `/the-importance-of-sealing-your-manufactured-stone-veneer/`
- `/why-should-you-choose-manufactured-stone-over-natural-stone/`
- `/go-brick-and-go-stone-for-diy-projects/2/`
- `/how-to-create-a-beautiful-custom-stone-patio/`
- `/the-advantages-of-using-go-stone-panels-for-your-home/3/`
- `/roi-when-using-manufactured-stone/4/`
- `/how-to-install-diy-stone-panels-go-stone-the-easy-way/8/`
- `/warranty/`
- `/roi-when-using-manufactured-stone/5/`
- … 137 more in Ahrefs

### 22. Non-canonical page in sitemap

`issue:non-canonical-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/product/stack-stone-sample-board/`
- `/the-importance-of-sealing-your-manufactured-stone-veneer/`
- `/why-should-you-choose-manufactured-stone-over-natural-stone/`
- `/how-to-create-a-beautiful-custom-stone-patio/`
- `/warranty/`
- `/go-brick-and-go-stone-for-diy-projects/`
- `/blog/`
- `/category/maintenance-and-installation/`
- `/how-to-care-for-a-cultured-stone-fireplace/`
- `/`
- … 50 more in Ahrefs

### 23. Canonical URL has no incoming internal links

`issue:canonical-url-has-no-incoming-internal-links` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/category/tips-and-tricks/`
- `/category/custom-stone-kitchen/`
- `/warranty/`
- `/category/stone/`
- `/category/go-stone-panels/`
- `/category/go-brick-brick-veneer/`
- `/category/maintenance-and-installation/`
- `/category/maintenance-and-installation/tips-and-advice/`

### 24. Noindex page in sitemap

`issue:noindex-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/cart/`
- `/my-account/`

### 25. Links to redirect, skipped by fix-redirect-links: author archive

`redirect-links:author-archive` · indexation-review · APPROVE · decider: agency · source: redirect-map-2026-10-29.json

Yoast > Search Appearance > Archives: disable author archives (or the author sitemap); one setting removes them all.

- `/author/welcome/` (39 links)
- `/author/welcome/` (18 links)

### 26. 302 redirect

`issue:302-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/checkout/`

### 27. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/checkout/`

### 28. HTTPS to HTTP redirect

`issue:https-to-http-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/wp-content/uploads/2015/01/Go-Stone_New-Brochure_12-19-13.pdf`

### 29. Page in multiple sitemaps

`issue:page-in-multiple-sitemaps` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/shop/`

### 30. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/wp-content/uploads/2015/09/customfit-fn-thekitchen.jpg`
- `/stone/page/2/`

### 31. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/wp-content/uploads/2015/09/customfit-fn-thekitchen.jpg`
- `/stone/page/2/`

### 32. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/see-native-custom-stones-customfit-panels-on-food-networks-the-kitchen/`

### 33. Page has links to broken page  (non-indexable pages)

`issue:page-has-links-to-broken-page-nonindexable` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/see-native-custom-stones-customfit-panels-on-food-networks-the-kitchen/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (9 pages: /privacy-policy/, /cart/, /my-account/lost-password/, /tag/custom-stone/page/3/, …)

9 pages on nativecustomstone.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

**Orphan page (has no incoming internal links)** (9 pages: /category/custom-stone-bathroom/, /category/manufactured-stone-fireplace/, /category/installation-and-care/, /category/adhered-stone-veneer/, …)

9 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Orphan page (has no incoming internal links)  (non-indexable pages)** (4 pages: /warranty/, /category/go-brick-brick-veneer/, /category/stone/, /category/tips-and-tricks/)

4 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Links to redirect, skipped by fix-redirect-links: date archive redirecting to the homepage** (2 pages: /2020/02/15/, /2020/02/15/)

2 old URLs on nativecustomstone.com currently redirect to the homepage, which loses visitors who click an old link. For each one we need the page it should go to now (or confirmation that nothing replaces it, in which case we remove the links).

