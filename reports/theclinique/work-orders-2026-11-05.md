# Work orders: theclinique.com

Ahrefs Site Audit project 9704556 · crawl 2026-11-05 · health 98 · 45 active issue types → 17 work orders (1 decisions, 11 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Organization schema missing or incomplete | schema-fix | APPROVE (skill pending) | 1 | 164 | agency | Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 2 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 8 | 164 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 3 | Page has nofollow outgoing internal links | nofollow-audit | APPROVE (skill pending) | 11 | 3 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 4 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 273 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex follow page, Noindex page. |
| 5 | Slow server response for AI crawlers | hosting/cache | FLAG | 4 | 0 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 6 | Pages fix-meta routed to ['/'] | ['/'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 7 | FAQ page missing FAQPage schema | schema-check | FLAG | 1 | 0 | client | FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing. |
| 8 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 9 | Product page missing Product schema | schema-check | FLAG | 1 | 0 | agency | Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages. |
| 10 | Indexable page not in sitemap | indexation-review | APPROVE (skill pending) | 265 | 0 (top 200 of 265) | agency | Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 11 | Broken redirect | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 12 | Indexable page became non-indexable | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 13 | Open Graph tags missing | fix-social-tags | AUTO (skill pending) | 1 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 14 | X (Twitter) card missing | fix-social-tags | AUTO (skill pending) | 1 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 15 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 8 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 16 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 8 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 17 | Canonical points to 4XX | fix-broken-links | AUTO/APPROVE (skill pending) | 1 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Organization schema missing or incomplete

`issue:organization-schema-missing-or-incomplete` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (164 traffic)

### 2. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/` (164 traffic)
- `/about/`
- `/conditions/facial-concerns/wrinkle-reduction/`
- `/conditions/facial-concerns/jowls/`
- `/conditions/body-concerns/stretch-marks/`
- `/blog/exploring-the-top-treatment-areas-for-botox-dysport/`
- `/conditions/skin-concerns/`
- `/conditions/facial-concerns/`

### 3. Page has nofollow outgoing internal links

`issue:page-has-nofollow-outgoing-internal-links` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/privacy-policy/` (3 traffic)
- `/blog/everything-you-need-to-know-about-laser-tattoo-removal/`
- `/santa-rosa-beach-promotions/`
- `/blog/are-superficial-chemical-peels-obsolete-the-spectra-laser-peel-hollywood-peel-might-make-that-happen/`
- `/open-house/`
- `/face/injectables/dermal-fillers/skinvive-by-juvederm/`
- `/about/our-office/`
- `/face/injectables/injectable-butt-lift/`
- `/blog/dont-forget-the-hands-and-decollete-when-thinking-about-your-cosmetic-refinements/`
- `/open-house-social-media/`
- … 1 more in Ahrefs

### 4. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex follow page, Noindex page.

- `/face/injectables/dermal-fillers/skinvive-by-juvederm/`
- `/face/injectables/injectable-butt-lift/`
- `/gallery-parkland/1223-2/`
- `/gallery-parkland/1499-2/`
- `/gallery-parkland/254725-2/`
- `/gallery/chemicalpeels2/`
- `/gallery-parkland/1372-2/`
- `/gallery-parkland/924-2/`
- `/gallery-parkland/1407-2/`
- `/gallery/lips-8/`
- … 263 more in Ahrefs

### 5. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/gallery-category-parkland/advatx-laser/page/2/`
- `/gallery-category/skin/page/3/`
- `/gallery-category/tixel/page/2/`
- `/gallery-category-parkland/coolsculpting/page/12/`

### 6. Pages fix-meta routed to ['/']

`fix-meta:` · ['/'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `homepage title`

### 7. FAQ page missing FAQPage schema

`issue:faq-page-missing-faqpage-schema` · schema-check · FLAG · decider: client

FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing.

- `/blog/commonly-asked-questions-about-lip-filler-problems/`

### 8. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/financing/`

### 9. Product page missing Product schema

`issue:product-page-missing-product-schema` · schema-check · FLAG · decider: agency

Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages.

- `/face/injectables/hylenex/`

### 10. Indexable page not in sitemap

`issue:indexable-page-not-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/gallery-category-parkland/face/page/2/`
- `/gallery-category/injectables-dermal-fillers/page/14/`
- `/gallery-category-parkland/face/page/10/`
- `/gallery-category-cooper-city/injectables-dermal-fillers/page/8/`
- `/gallery-category/genius-infini/page/8/`
- `/gallery-category-cooper-city/non-surgical-face-lift/page/2/`
- `/gallery-category/genius-infini/page/5/`
- `/gallery-category-cooper-city/non-surgical-face-lift/page/3/`
- `/gallery-category-parkland/butt-lift/page/3/`
- `/gallery-category/injectables-dermal-fillers/page/15/`
- … 255 more in Ahrefs

### 11. Broken redirect

`issue:broken-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/medspa-south-florida/facial-body-treatments/venus-legacy/`

### 12. Indexable page became non-indexable

`issue:indexable-page-became-non-indexable` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/about/out-of-town-clients/`

### 13. Open Graph tags missing

`issue:open-graph-tags-missing` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/subscribe-notifications/`

### 14. X (Twitter) card missing

`issue:x-twitter-card-missing` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/subscribe-notifications/`

### 15. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/about/financing/`
- `/cooper-city-home-page/`
- `/face/lasers/advatx/`
- `/conditions/skin-concerns/melasma/`
- `/conditions/facial-concerns/pigmented-lesions/`
- `/team/sandy-weiner/`
- `/face/skin/ellacor/`
- `/body/venus-legacy-rf/`

### 16. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/about/financing/`
- `/cooper-city-home-page/`
- `/face/lasers/advatx/`
- `/conditions/skin-concerns/melasma/`
- `/conditions/facial-concerns/pigmented-lesions/`
- `/team/sandy-weiner/`
- `/face/skin/ellacor/`
- `/body/venus-legacy-rf/`

### 17. Canonical points to 4XX

`issue:canonical-points-to-4xx` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/team/alicia-budda/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (273 pages: /face/injectables/dermal-fillers/skinvive-by-juvederm/, /face/injectables/injectable-butt-lift/, /gallery-parkland/1223-2/, /gallery-parkland/1499-2/, …)

273 pages on theclinique.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

