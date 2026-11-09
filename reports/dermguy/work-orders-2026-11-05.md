# Work orders: dermguy.com

Ahrefs Site Audit project 9704523 · crawl 2026-11-05 · health 99 · 32 active issue types → 15 work orders (1 decisions, 6 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 97 | 288 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 2 | H1 tag missing or empty | manual | FLAG | 16 | 38 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 3 | Slow page | manual | FLAG | 21 | 2 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 4 | Slow server response for AI crawlers | hosting/cache | FLAG | 5 | 1 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 5 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 27 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 6 | Structured data has schema.org validation error | schema-fix | FLAG | 4 | 0 | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 7 | Pages fix-meta routed to [] | [] | FLAG | 3 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 8 | Pages fix-meta routed to ['/category/uncategorized/', '/category/consultation/', '/category/tv-spots/', '/category/testimonials/'] | ['/category/uncategorized/', '/category/consultation/', '/category/tv-spots/', '/category/testimonials/'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 9 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 10 | Product page missing Product schema | schema-check | FLAG | 1 | 0 | agency | Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages. |
| 11 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 4 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 12 | Indexable page not in sitemap | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 13 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 3 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 14 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 1 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 15 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 1 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/device-vbeam-perfecta-laser/` (122 traffic)
- `/` (37 traffic)
- `/gentlemax/` (28 traffic)
- `/red-stretch-marks/` (16 traffic)
- `/picoway/` (15 traffic)
- `/vbeam-prima-laser/` (14 traffic)
- `/picoway-laser/` (10 traffic)
- `/laser-tattoo-removal/` (8 traffic)
- `/neck-redness-poc/` (7 traffic)
- `/cherry-spider-angiomas/` (7 traffic)
- … 87 more in Ahrefs

### 2. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/` (37 traffic)
- `/dr-kachiu-c-lee-m-d/` (1 traffic)
- `/aesthetic-nurses/`
- `/sample-page/`
- `/cart/`
- `/mission-statement/`
- `/anti-covid-measures/`
- `/checkout/`
- `/vascular-rejuvenating-lasers/`
- `/all-conditions/`
- … 6 more in Ahrefs

### 3. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/lightsheer/` (1 traffic)
- `/acne/` (1 traffic)
- `/testimonials/`
- `/sample-page/`
- `/portfolio-filter/fillerx/page/2/`
- `/red-leg-veins-spider-veins/`
- `/revlite/`
- `/tv-spots/`
- `/fillers/`
- `/portfolio-filter/wrinkles-sun-damage/`
- … 11 more in Ahrefs

### 4. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/acne/` (1 traffic)
- `/tv-spots/`
- `/fillers/`
- `/picosure-laser-what-it-treats/`
- `/consultation/`

### 5. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/portfolio-filter/facial-veins-rosacea/page/4/`
- `/portfolio-filter/red-stretch-marks/`
- `/portfolio-filter/facial-veins-rosacea/page/3/`
- `/portfolio-filter/fat-reduction-coolsculpting/`
- `/portfolio-filter/fillerx/page/2/`
- `/portfolio-filter/melasma/`
- `/portfolio-filter/tattoo-laser-removal/page/3/`
- `/portfolio-filter/tattoo-laser-removal/`
- `/portfolio-filter/neck-redness-poc/`
- `/portfolio-filter/facial-veins-rosacea/page/2/`
- … 17 more in Ahrefs

### 6. Structured data has schema.org validation error

`issue:structured-data-has-schema-org-validation-error` · schema-fix · FLAG · decider: agency

Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit.

- `/botox-neuromodulators/`
- `/treatments/`
- `/conditions/`
- `/treatments-bk/`

### 7. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `noindex`
- `non-200`
- `homepage title`

### 8. Pages fix-meta routed to ['/category/uncategorized/', '/category/consultation/', '/category/tv-spots/', '/category/testimonials/']

`fix-meta:category-uncategorized-category-consulta` · ['/category/uncategorized/', '/category/consultation/', '/category/tv-spots/', '/category/testimonials/'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`

### 9. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/financing/`

### 10. Product page missing Product schema

`issue:product-page-missing-product-schema` · schema-check · FLAG · decider: agency

Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages.

- `/gentlemax-pro-plus-laser/`

### 11. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/before-after-old/`
- `/all-treatments/`
- `/videos/`
- `/rejuvenating-scar-treatment-devices/`

### 12. Indexable page not in sitemap

`issue:indexable-page-not-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/picosure-laser-what-it-treats/`

### 13. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/privacy-policy-2/`
- `/good-faith-estimate/`
- `/policy/`

### 14. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/cdn-cgi/l/email-protection`

### 15. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/cdn-cgi/l/email-protection`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (27 pages: /portfolio-filter/facial-veins-rosacea/page/4/, /portfolio-filter/red-stretch-marks/, /portfolio-filter/facial-veins-rosacea/page/3/, /portfolio-filter/fat-reduction-coolsculpting/, …)

27 pages on dermguy.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

