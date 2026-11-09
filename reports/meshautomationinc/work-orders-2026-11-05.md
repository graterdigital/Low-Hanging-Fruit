# Work orders: meshautomationinc.com

Ahrefs Site Audit project 9704540 · crawl 2026-11-05 · health 97 · 47 active issue types → 28 work orders (5 decisions, 13 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Slow page | manual | FLAG | 185 | 232 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 2 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 113 | 211 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 3 | H1 tag missing or empty | manual | FLAG | 30 | 88 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 4 | Organization schema missing or incomplete | schema-fix | APPROVE (skill pending) | 1 | 82 | agency | Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 5 | Slow server response for AI crawlers | hosting/cache | FLAG | 10 | 62 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 6 | Product page missing Product schema | schema-check | FLAG | 28 | 13 | agency | Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages. |
| 7 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 25 | 1 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 8 | Orphan page (has no incoming internal links) | indexation-review | decide | 19 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 9 | Links to redirect, skipped by fix-redirect-links: URL has a query string | manual | decide | 15 | 0 | agency | fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave. |
| 10 | Links to redirect, skipped by fix-redirect-links: redirects to homepage | redirect-rules | decide | 7 | 0 | client | Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order. |
| 11 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 4 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 12 | Links to redirect, skipped by fix-redirect-links: no incoming internal links (sitemap or orphan entry) | manual | decide | 1 | 0 | agency | fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave. |
| 13 | Category page missing ItemList schema | schema-check | FLAG | 15 | 0 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 14 | Pages fix-meta routed to [] | [] | FLAG | 3 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 15 | Links to redirect, skipped by fix-redirect-links: pagination /page/1/ comes from the theme template, not content | manual | FLAG | 3 | 0 | agency | Theme template edit: emit the archive root for page 1 (WordPress paginate_links does by default). Diff by hand. |
| 16 | wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings) | manual | FLAG | 3 | 0 | agency | Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1052-fix-redirect-links-live-options.md. |
| 17 | CSS file size too large | manual | FLAG | 2 | 0 | agency | Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket. |
| 18 | Pages fix-meta routed to ['/categorycpt/vision/', '/category/tending/', '/product-brands/siemens/', '/categorycpt/material-handling/page/2/', '/categorycpt/palletizing/page/3/', '/brand/fanuc/', '/category/finishing/', '/made-for/boxes/', '/product-brands/mesh/', '/brand/yaskawa/', '/category/news/', '/product-category/palletizing/', '/categorycpt/additional-expertise/', '/made-for/totes/', '/categorycpt/palletizing/page/2/', '/category/vision/', '/product-brands/siemens/page/2/', '/product-brands/rockwell/', '/category/palletizing/', '/categorycpt/assembly/', '/product-brands/mesh/page/2/', '/category/assembly/', '/category/palletizing/page/2/', '/category/uncategorized/', '/brand/abb/', '/made-for/pails/', '/categorycpt/cobots/', '/categorycpt/robotic-tending/', '/made-for/bags/', '/product-brands/rockwell/page/2/', '/product-category/palletizing/page/2/'] | ['/categorycpt/vision/', '/category/tending/', '/product-brands/siemens/', '/categorycpt/material-handling/page/2/', '/categorycpt/palletizing/page/3/', '/brand/fanuc/', '/category/finishing/', '/made-for/boxes/', '/product-brands/mesh/', '/brand/yaskawa/', '/category/news/', '/product-category/palletizing/', '/categorycpt/additional-expertise/', '/made-for/totes/', '/categorycpt/palletizing/page/2/', '/category/vision/', '/product-brands/siemens/page/2/', '/product-brands/rockwell/', '/category/palletizing/', '/categorycpt/assembly/', '/product-brands/mesh/page/2/', '/category/assembly/', '/category/palletizing/page/2/', '/category/uncategorized/', '/brand/abb/', '/made-for/pails/', '/categorycpt/cobots/', '/categorycpt/robotic-tending/', '/made-for/bags/', '/product-brands/rockwell/page/2/', '/product-category/palletizing/page/2/'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 19 | Canonical URL has no incoming internal links | indexation-review | APPROVE (skill pending) | 9 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 20 | Canonical points to redirect | redirect-rules | APPROVE (skill pending) | 3 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 21 | Noindex page in sitemap | indexation-review | APPROVE (skill pending) | 2 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 22 | 302 redirect | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 23 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 24 | Noindex in HTML and HTTP header | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 25 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 1 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 26 | Page in multiple sitemaps | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 27 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 5 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 28 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 5 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/agv-cost-2026/` (68 traffic)
- `/material-handling/robotic-stacking-systems/` (42 traffic)
- `/material-handling/automated-pallet-handling/` (40 traffic)
- `/amr-cost-2026/` (19 traffic)
- `/robotic-machining-finishing/robotic-polishing/` (16 traffic)
- `/robotic-palletizing-systems/collaborative-robots/` (13 traffic)
- `/product/macpal-pallet-stacker-destacker-turnkey/` (9 traffic)
- `/robotic-palletizing-systems/` (6 traffic)
- `/automotive-manufacturing-automation/` (5 traffic)
- `/product/fanuc-robotic-palletizer-for-totes-fully-assembled/` (4 traffic)
- … 175 more in Ahrefs

### 2. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/` (82 traffic)
- `/material-handling/robotic-stacking-systems/` (42 traffic)
- `/material-handling/automated-pallet-handling/` (40 traffic)
- `/robotic-machining-finishing/robotic-polishing/` (16 traffic)
- `/robotic-palletizing-systems/collaborative-robots/` (13 traffic)
- `/robotic-palletizing-systems/` (6 traffic)
- `/automotive-manufacturing-automation/` (5 traffic)
- `/pre_eng_sol/` (3 traffic)
- `/robotic-machining-finishing/` (1 traffic)
- `/material-handling/automated-conveyor-systems/` (1 traffic)
- … 103 more in Ahrefs

### 3. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/` (82 traffic)
- `/automotive-manufacturing-automation/` (5 traffic)
- `/robotic-palletizing-systems/bottle-palletizing/` (1 traffic)
- `/medical-device-assembly-automation/`
- `/shop/`
- `/plastics-and-injection-molding/`
- `/mesh-partners/`
- `/robotic-palletizing-systems/case-packer-palletizer/`
- `/aerospace-manufacturing-automation/`
- `/process-line-controls-systems/`
- … 20 more in Ahrefs

### 4. Organization schema missing or incomplete

`issue:organization-schema-missing-or-incomplete` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (82 traffic)

### 5. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/material-handling/robotic-stacking-systems/` (42 traffic)
- `/robotic-palletizing-systems/collaborative-robots/` (13 traffic)
- `/robotic-palletizing-systems/` (6 traffic)
- `/robotic-palletizing-systems/bottle-palletizing/` (1 traffic)
- `/autonomous-mobile-robots/`
- `/blog/page/2/`
- `/pre_eng_sol/mactend/`
- `/pre_eng_sol/macgrind/`
- `/robotic-machine-tending/`
- `/robotic-machining-finishing/robotic-grinding-and-buffing/`

### 6. Product page missing Product schema

`issue:product-page-missing-product-schema` · schema-check · FLAG · decider: agency

Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages.

- `/product/macpal-pallet-stacker-destacker-turnkey/` (9 traffic)
- `/product/fanuc-robotic-palletizer-for-totes-fully-assembled/` (4 traffic)
- `/product/yaskawa-robotic-palletizer-for-boxes/`
- `/product/yaskawa-robotic-palletizer-for-totes-fully-assembled/`
- `/product/yaskawa-robotic-palletizer-for-bags/`
- `/pre_eng_sol/macpal-2/`
- `/product/abb-robotic-palletizer-for-totes-fully-assembled/`
- `/product/yaskawa-cobot-palletizer-for-boxes/`
- `/pre_eng_sol/mactend/`
- `/product/yaskawa-cobot-palletizer-for-totes/`
- … 18 more in Ahrefs

### 7. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/material-handling/automated-conveyor-systems/` (1 traffic)
- `/blog/`
- `/shop/`
- `/product-brands/siemens/`
- `/warehouse-automation-systems-vs-traditional-storage-workflows-2/`
- `/brand/fanuc/`
- `/blog/page/2/`
- `/made-for/boxes/`
- `/product-brands/mesh/`
- `/brand/yaskawa/`
- … 15 more in Ahrefs

### 8. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/category/tending/`
- `/brand/fanuc/`
- `/category/finishing/`
- `/made-for/boxes/`
- `/brand/yaskawa/`
- `/category/news/`
- `/made-for/totes/`
- `/food-and-beverage-automation-solutions/safety-considerations/`
- `/product-category/palletizing/tote-palletizing/`
- `/thank-you-pes/`
- … 9 more in Ahrefs

### 9. Links to redirect, skipped by fix-redirect-links: URL has a query string

`redirect-links:url-has-a-query-string` · manual · decide · decider: agency · source: redirect-map-2026-10-29.json

fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave.

- `/case_studies/page/1/?categorycpt=palletizing` (3 links)
- `/case_studies/page/1/?categorycpt=vision` (1 links)
- `/?categorycpt=assembly` (1 links)
- `/?categorycpt=robotic-tending` (1 links)
- `/?categorycpt=additional-expertise` (1 links)
- `/?categorycpt=material-handling` (1 links)
- `/blog/page/1/?category=palletizing` (1 links)
- `/case_studies/page/1/?categorycpt=material-handling` (1 links)
- `/?categorycpt=cobots` (1 links)
- `/?categorycpt=palletizing` (1 links)
- … 5 more in Ahrefs

### 10. Links to redirect, skipped by fix-redirect-links: redirects to homepage

`redirect-links:redirects-to-homepage` · redirect-rules · decide · decider: client · source: redirect-map-2026-10-29.json

Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order.

- `/blog/page/3/` (10 links)
- `/automated-material-handling/` (4 links)
- `/robotic-palletizing-systems/automated-guided-vehicles/` (4 links)
- `/assembly-systems/` (2 links)
- `/processing-lines/` (1 links)
- `/mesh-bag-palletizing-automation` (1 links)
- `/pre-engineered-solutions/mac-mesh-automation-cell/` (1 links)

### 11. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/my-account/lost-password/`
- `/privacy-policy/`
- `/cart/`
- `/my-account/`

### 12. Links to redirect, skipped by fix-redirect-links: no incoming internal links (sitemap or orphan entry)

`redirect-links:no-incoming-internal-links-sitemap-or-or` · manual · decide · decider: agency · source: redirect-map-2026-10-29.json

fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave.

- `/checkout/`

### 13. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/categorycpt/vision/`
- `/shop/`
- `/product-brands/siemens/`
- `/brand/fanuc/`
- `/made-for/boxes/`
- `/product-brands/mesh/`
- `/brand/yaskawa/`
- `/product-category/palletizing/`
- `/made-for/totes/`
- `/product-brands/rockwell/`
- … 5 more in Ahrefs

### 14. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `noindex`
- `non-200`
- `homepage title`

### 15. Links to redirect, skipped by fix-redirect-links: pagination /page/1/ comes from the theme template, not content

`redirect-links:pagination-page-1-comes-from-the-theme-t` · manual · FLAG · decider: agency · source: redirect-map-2026-10-29.json

Theme template edit: emit the archive root for page 1 (WordPress paginate_links does by default). Diff by hand.

- `/case_studies/page/1/` (7 links)
- `/blog/page/1/` (1 links)
- `/categorycpt/palletizing/page/1/` (1 links)

### 16. wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings)

`redirect-links:wp-options` · manual · FLAG · decider: agency · source: 2026-10-30-1052-fix-redirect-links-live-options.md

Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1052-fix-redirect-links-live-options.md.

- `clarity_collect_batch`
- `clarity_collect_batch`
- `widget_posts_widget-8_view_all`

### 17. CSS file size too large

`issue:css-file-size-too-large` · manual · FLAG · decider: agency

Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket.

- `/wp-content/cache/min/1/wp-content/themes/mesh/dist/styles/main.css?ver=1788184799`
- `/wp-content/cache/min/1/wp-includes/css/dashicons.min.css?ver=1788184799`

### 18. Pages fix-meta routed to ['/categorycpt/vision/', '/category/tending/', '/product-brands/siemens/', '/categorycpt/material-handling/page/2/', '/categorycpt/palletizing/page/3/', '/brand/fanuc/', '/category/finishing/', '/made-for/boxes/', '/product-brands/mesh/', '/brand/yaskawa/', '/category/news/', '/product-category/palletizing/', '/categorycpt/additional-expertise/', '/made-for/totes/', '/categorycpt/palletizing/page/2/', '/category/vision/', '/product-brands/siemens/page/2/', '/product-brands/rockwell/', '/category/palletizing/', '/categorycpt/assembly/', '/product-brands/mesh/page/2/', '/category/assembly/', '/category/palletizing/page/2/', '/category/uncategorized/', '/brand/abb/', '/made-for/pails/', '/categorycpt/cobots/', '/categorycpt/robotic-tending/', '/made-for/bags/', '/product-brands/rockwell/page/2/', '/product-category/palletizing/page/2/']

`fix-meta:categorycpt-vision-category-tending-prod` · ['/categorycpt/vision/', '/category/tending/', '/product-brands/siemens/', '/categorycpt/material-handling/page/2/', '/categorycpt/palletizing/page/3/', '/brand/fanuc/', '/category/finishing/', '/made-for/boxes/', '/product-brands/mesh/', '/brand/yaskawa/', '/category/news/', '/product-category/palletizing/', '/categorycpt/additional-expertise/', '/made-for/totes/', '/categorycpt/palletizing/page/2/', '/category/vision/', '/product-brands/siemens/page/2/', '/product-brands/rockwell/', '/category/palletizing/', '/categorycpt/assembly/', '/product-brands/mesh/page/2/', '/category/assembly/', '/category/palletizing/page/2/', '/category/uncategorized/', '/brand/abb/', '/made-for/pails/', '/categorycpt/cobots/', '/categorycpt/robotic-tending/', '/made-for/bags/', '/product-brands/rockwell/page/2/', '/product-category/palletizing/page/2/'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`

### 19. Canonical URL has no incoming internal links

`issue:canonical-url-has-no-incoming-internal-links` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/categorycpt/vision/`
- `/categorycpt/robotic-grinding/`
- `/categorycpt/material-handling/`
- `/categorycpt/additional-expertise/`
- `/categorycpt/palletizing/`
- `/categorycpt/assembly/`
- `/categorycpt/cobots/`
- `/categorycpt/robotic-tending/`
- `/categorycpt/amr-agv/`

### 20. Canonical points to redirect

`issue:canonical-points-to-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/case_studies/page/2/?categorycpt=vision`
- `/case_studies/page/4/?categorycpt=palletizing`
- `/case_studies/page/2/?categorycpt=robotic-tending`

### 21. Noindex page in sitemap

`issue:noindex-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/cart/`
- `/my-account/`

### 22. 302 redirect

`issue:302-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/checkout/`

### 23. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/checkout/`

### 24. Noindex in HTML and HTTP header

`issue:noindex-in-html-and-http-header` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/my-account/lost-password/`

### 25. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/cart/`

### 26. Page in multiple sitemaps

`issue:page-in-multiple-sitemaps` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/shop/`

### 27. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/warehouse-robotics-types-use-cases-system-design/`
- `/blog/page/4/`
- `/automated-material-handling/robotic-case-packers/`
- `/?page_id=4306`
- `/core/flexible-automation/assemblyjoining-methods/`

### 28. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/warehouse-robotics-types-use-cases-system-design/`
- `/blog/page/4/`
- `/automated-material-handling/robotic-case-packers/`
- `/?page_id=4306`
- `/core/flexible-automation/assemblyjoining-methods/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Orphan page (has no incoming internal links)** (19 pages: /category/tending/, /brand/fanuc/, /category/finishing/, /made-for/boxes/, …)

19 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Links to redirect, skipped by fix-redirect-links: redirects to homepage** (7 pages: /blog/page/3/, /automated-material-handling/, /robotic-palletizing-systems/automated-guided-vehicles/, /assembly-systems/, …)

7 old URLs on meshautomationinc.com currently redirect to the homepage, which loses visitors who click an old link. For each one we need the page it should go to now (or confirmation that nothing replaces it, in which case we remove the links).

**Pages hidden from Google (noindex/nofollow): confirm intent** (4 pages: /my-account/lost-password/, /privacy-policy/, /cart/, /my-account/)

4 pages on meshautomationinc.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

## Skipped on purpose

- Indexable page not in sitemap (18): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

