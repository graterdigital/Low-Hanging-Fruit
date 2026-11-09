# Work orders: nouveauspa.com

Ahrefs Site Audit project 9704547 · crawl 2026-11-05 · health 79 · 45 active issue types → 21 work orders (1 decisions, 15 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Structured data has schema.org validation error | schema-fix | FLAG | 174 | 286 | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 2 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 156 | 286 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 3 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 64 | 194 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 4 | H1 tag missing or empty | manual | FLAG | 2 | 177 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 5 | Structured data has Google rich results validation error | schema-fix | APPROVE (skill pending) | 16 | 3 | agency | Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual |
| 6 | Page has nofollow outgoing internal links | nofollow-audit | APPROVE (skill pending) | 9 | 3 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 7 | Indexable page not in sitemap | indexation-review | APPROVE (skill pending) | 25 | 1 | agency | Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 8 | X (Twitter) card incomplete | fix-social-tags | AUTO (skill pending) | 15 | 1 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 9 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 11 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 10 | Slow page | manual | FLAG | 15 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 11 | Pages fix-meta routed to [] | [] | FLAG | 4 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 12 | Category page missing ItemList schema | schema-check | FLAG | 1 | 0 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 13 | Broken redirect | redirect-rules | APPROVE (skill pending) | 10 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 14 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 3 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 15 | Noindex page in sitemap | indexation-review | APPROVE (skill pending) | 2 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 16 | 302 redirect | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 17 | Noindex in HTML and HTTP header | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 18 | Page in multiple sitemaps | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 19 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 23 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 20 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 23 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 21 | Page has links to broken page  (non-indexable pages) | fix-broken-links | AUTO/APPROVE (skill pending) | 18 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Structured data has schema.org validation error

`issue:structured-data-has-schema-org-validation-error` · schema-fix · FLAG · decider: agency

Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit.

- `/` (177 traffic)
- `/shop/skin/signature-skin-treatments/microdermabrasion/` (42 traffic)
- `/acne-scar-treatment-in-2025-lasers-rf-microneedling-fillers/` (24 traffic)
- `/day-spa/` (14 traffic)
- `/product-category/hair-and-nails/manicures/` (6 traffic)
- `/product-category/day-spa/body-treatments/` (5 traffic)
- `/shop/hair-and-nails/manicures/shellac-manicure/` (3 traffic)
- `/shop/day-spa/hydro-spa/steamy-wonder/` (2 traffic)
- `/the-power-of-deep-pore-cleansing-in-kennewick-wa/` (2 traffic)
- `/product-category/skin/facials/` (2 traffic)
- … 164 more in Ahrefs

### 2. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/` (177 traffic)
- `/shop/skin/signature-skin-treatments/microdermabrasion/` (42 traffic)
- `/acne-scar-treatment-in-2025-lasers-rf-microneedling-fillers/` (24 traffic)
- `/day-spa/` (14 traffic)
- `/product-category/hair-and-nails/manicures/` (6 traffic)
- `/product-category/day-spa/body-treatments/` (5 traffic)
- `/shop/hair-and-nails/manicures/shellac-manicure/` (3 traffic)
- `/shop/day-spa/hydro-spa/steamy-wonder/` (2 traffic)
- `/the-power-of-deep-pore-cleansing-in-kennewick-wa/` (2 traffic)
- `/product-category/skin/facials/` (2 traffic)
- … 146 more in Ahrefs

### 3. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/` (177 traffic)
- `/product-category/hair-and-nails/manicures/` (6 traffic)
- `/product-category/day-spa/body-treatments/` (5 traffic)
- `/product-category/skin/facials/` (2 traffic)
- `/product-category/hair-and-nails/pedicures/` (2 traffic)
- `/team/brenda-petry/` (1 traffic)
- `/medspa-1/` (1 traffic)
- `/store/page/3/`
- `/product-category/day-spa/page/2/`
- `/store/page/5/`
- … 54 more in Ahrefs

### 4. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/` (177 traffic)
- `/shop/day-spa/b36714c11a32134e943c3754470c79bc/`

### 5. Structured data has Google rich results validation error

`issue:structured-data-has-google-rich-results-validation-error` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual

- `/shop/day-spa/spa-days/the-detox-day/` (1 traffic)
- `/shop/day-spa/spa-days/mother-to-be-spa-day/` (1 traffic)
- `/shop/day-spa/spa-days/sweet-16-spa-day-teens-13-18/` (1 traffic)
- `/shop/day-spa/waxing/brow-chin/`
- `/shop/day-spa/spa-days/decadent-delight/`
- `/shop/hair-and-nails/hair/root-touch-up/`
- `/shop/day-spa/waxing/brow-lip/`
- `/shop/day-spa/spa-days/express-yourself/`
- `/shop/day-spa/spa-days/couples-retreat/`
- `/shop/day-spa/spa-days/nouveau-spa-day/`
- … 6 more in Ahrefs

### 6. Page has nofollow outgoing internal links

`issue:page-has-nofollow-outgoing-internal-links` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/shop/day-spa/spa-days/the-detox-day/` (1 traffic)
- `/shop/day-spa/spa-days/mother-to-be-spa-day/` (1 traffic)
- `/shop/day-spa/spa-days/sweet-16-spa-day-teens-13-18/` (1 traffic)
- `/shop/day-spa/spa-days/decadent-delight/`
- `/shop/day-spa/spa-days/express-yourself/`
- `/shop/day-spa/spa-days/couples-retreat/`
- `/shop/day-spa/spa-days/nouveau-spa-day/`
- `/shop/day-spa/spa-days/just-for-men-the-gentlemans-escape/`
- `/shop/day-spa/spa-days/the-ultimate-spa-day/`

### 7. Indexable page not in sitemap

`issue:indexable-page-not-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/team/brenda-petry/` (1 traffic)
- `/store/page/3/`
- `/product-category/day-spa/page/2/`
- `/store/page/5/`
- `/team/joelle-filbrun/`
- `/team/casandra-hudon/`
- `/team/jenni-devoir/`
- `/store/page/4/`
- `/product-category/day-spa/page/3/`
- `/product-category/day-spa/page/4/`
- … 15 more in Ahrefs

### 8. X (Twitter) card incomplete

`issue:x-twitter-card-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/team/brenda-petry/` (1 traffic)
- `/team/joelle-filbrun/`
- `/team/casandra-hudon/`
- `/team/jenni-devoir/`
- `/team/tony-arteaga/`
- `/team/kassen-chamberlain/`
- `/team/michelle-mason/`
- `/team/tayler-morales/`
- `/team/annina-monville/`
- `/team/samantha-olson/`
- … 5 more in Ahrefs

### 9. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/category/spa-days/`
- `/category/facials/`
- `/category/hydro-spa/`
- `/category/dlm-faq/`
- `/my-account/`
- `/my-account/lost-password/`
- `/cart/`
- `/category/skin-rejuvenation/`
- `/category/plastic-surgery/`
- `/category/body-treatments/`
- … 1 more in Ahrefs

### 10. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/get-summer-ready-at-nouveau-day-spa-with-the-mineral-mud-detox-treatment/`
- `/product-category/day-spa/page/2/`
- `/store/page/5/`
- `/store/page/4/`
- `/shop/day-spa/waxing/brow-lip/`
- `/injectables-fillers/`
- `/category/hydro-spa/`
- `/category/dlm-faq/`
- `/team/annina-monville/`
- `/product-category/day-spa/waxing/`
- … 5 more in Ahrefs

### 11. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`
- `noindex`
- `non-200`
- `homepage title`

### 12. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/shop/hair-and-nails/hair/gloss/`

### 13. Broken redirect

`issue:broken-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/product/enzyme-firming-facial/`
- `/product/cupping-massage/`
- `/product/nouveau-stone-massage/`
- `/product/diamond-glow/`
- `/product/deep-pore-cleansing-treatment/`
- `/product/vichy-waterfall-experience/`
- `/product/photo-rejuvenation-lumilift-lumifacial/`
- `/product/nouveau-stone-therapy/`
- `/?post_type=product&p=12729&preview=true`
- `/product/hot-oil-tandem-massage/`

### 14. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/medspa/`
- `/checkout/`
- `/shop/day-spa/for-men/the-gentlemans-escape/`

### 15. Noindex page in sitemap

`issue:noindex-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/my-account/`
- `/cart/`

### 16. 302 redirect

`issue:302-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/checkout/`

### 17. Noindex in HTML and HTTP header

`issue:noindex-in-html-and-http-header` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/my-account/lost-password/`

### 18. Page in multiple sitemaps

`issue:page-in-multiple-sitemaps` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/store/`

### 19. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/shop/skin/facials/teen-facial/`
- `/shop/day-spa/massage-therapy/lymphatic-body-massage/`
- `/shop/medspa/massage-therapy/nouveau-stone-therapy/`
- `/shop/day-spa/massage-therapy/cupping-massage/`
- `/shop/skin/facials/enzyme-firming-facial/`
- `/shop/medspa/massage-therapy/cupping-massage/`
- `/shop/medspa/massage-therapy/lymphatic-body-massage/`
- `/?page_id=344`
- `/shop/day-spa/hydro-spa/vichy-waterfall-experience/`
- `/shop/day-spa/massage-therapy/nouveau-stone-massage/`
- … 13 more in Ahrefs

### 20. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/shop/skin/facials/teen-facial/`
- `/shop/day-spa/massage-therapy/lymphatic-body-massage/`
- `/shop/medspa/massage-therapy/nouveau-stone-therapy/`
- `/shop/day-spa/massage-therapy/cupping-massage/`
- `/shop/skin/facials/enzyme-firming-facial/`
- `/shop/medspa/massage-therapy/cupping-massage/`
- `/shop/medspa/massage-therapy/lymphatic-body-massage/`
- `/?page_id=344`
- `/shop/day-spa/hydro-spa/vichy-waterfall-experience/`
- `/shop/day-spa/massage-therapy/nouveau-stone-massage/`
- … 13 more in Ahrefs

### 21. Page has links to broken page  (non-indexable pages)

`issue:page-has-links-to-broken-page-nonindexable` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/category/spa-days/`
- `/product-category/medspa/waxing/`
- `/product-category/medspa/hydro-spa/`
- `/category/facials/`
- `/category/hydro-spa/`
- `/category/dlm-faq/`
- `/my-account/`
- `/my-account/lost-password/`
- `/product-category/spa-days/`
- `/product-category/medspa/spa-days/`
- … 8 more in Ahrefs

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (11 pages: /category/spa-days/, /category/facials/, /category/hydro-spa/, /category/dlm-faq/, …)

11 pages on nouveauspa.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

