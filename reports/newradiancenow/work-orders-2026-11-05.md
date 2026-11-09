# Work orders: newradiancenow.com

Ahrefs Site Audit project 9704544 · crawl 2026-11-05 · health 96 · 49 active issue types → 20 work orders (1 decisions, 11 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Structured data has schema.org validation error | schema-fix | FLAG | 218 | 1199 (top 200 of 218) | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 2 | Structured data has Google rich results validation error | schema-fix | APPROVE (skill pending) | 178 | 1193 | agency | Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual |
| 3 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 12 | 30 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 4 | Indexable page not in sitemap | indexation-review | APPROVE (skill pending) | 448 | 6 (top 200 of 448) | agency | Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 5 | Category page missing ItemList schema | schema-check | FLAG | 15 | 1 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 6 | FAQ page missing FAQPage schema | schema-check | FLAG | 7 | 1 | client | FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing. |
| 7 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 36 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 8 | Multiple title tags | manual | FLAG | 6 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 9 | Slow page | manual | FLAG | 6 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 10 | H1 tag missing or empty | manual | FLAG | 4 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 11 | Pages fix-meta routed to ['/'] | ['/'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 12 | Pages fix-meta routed to ['/author/dlm_seo/', '/author/dlm_developer/page/3/', '/author/dlm_developer/page/2/', '/author/dlm_admin/', '/author/dlm_admin/', '/author/dlm_seo/', '/author/dlm_seo/page/3/', '/author/dlm_seo/page/2/', '/author/dlm_seo/page/3/', '/category/uncategorized/', '/author/dlm_seo/page/4/', '/author/dlm_developer/page/4/', '/author/dlm_developer/page/2/', '/author/dlm_developer/page/3/', '/author/dlm_developer/', '/category/uncategorized/', '/video-category/alma-accent-pixel/', '/category/uncategorized/page/2/', '/author/dlm_developer/page/4/', '/video-category/tummy-tuck/', '/category/uncategorized/page/2/', '/author/dlm_seo/page/4/', '/author/dlm_developer/', '/video-category/emsella/', '/author/dlm_seo/page/2/', '/gallery-category/coolsculpting-elite/page/3/'] | ['/author/dlm_seo/', '/author/dlm_developer/page/3/', '/author/dlm_developer/page/2/', '/author/dlm_admin/', '/author/dlm_admin/', '/author/dlm_seo/', '/author/dlm_seo/page/3/', '/author/dlm_seo/page/2/', '/author/dlm_seo/page/3/', '/category/uncategorized/', '/author/dlm_seo/page/4/', '/author/dlm_developer/page/4/', '/author/dlm_developer/page/2/', '/author/dlm_developer/page/3/', '/author/dlm_developer/', '/category/uncategorized/', '/video-category/alma-accent-pixel/', '/category/uncategorized/page/2/', '/author/dlm_developer/page/4/', '/video-category/tummy-tuck/', '/category/uncategorized/page/2/', '/author/dlm_seo/page/4/', '/author/dlm_developer/', '/video-category/emsella/', '/author/dlm_seo/page/2/', '/gallery-category/coolsculpting-elite/page/3/'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 13 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 3 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 14 | Broken redirect | redirect-rules | APPROVE (skill pending) | 2 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 15 | HTTPS to HTTP redirect | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 16 | X (Twitter) card missing | fix-social-tags | AUTO (skill pending) | 7 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 17 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 4 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 18 | Open Graph tags missing | fix-social-tags | AUTO (skill pending) | 3 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 19 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 16 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 20 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 16 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Structured data has schema.org validation error

`issue:structured-data-has-schema-org-validation-error` · schema-fix · FLAG · decider: agency

Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit.

- `/new-radiance-eye-rejuvenation/` (195 traffic)
- `/locations/palm-beach-gardens/` (148 traffic)
- `/locations/boca-raton/` (95 traffic)
- `/` (86 traffic)
- `/locations/wellington/` (77 traffic)
- `/body-sculpting-at-new-radiance-cosmetic-centers/` (71 traffic)
- `/double-chin-reduction/` (52 traffic)
- `/dermal-fillers-boca-raton-florida/` (38 traffic)
- `/exilis-ultra-360-skin-tightening/` (37 traffic)
- `/specials/` (32 traffic)
- … 208 more in Ahrefs

### 2. Structured data has Google rich results validation error

`issue:structured-data-has-google-rich-results-validation-error` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual

- `/new-radiance-eye-rejuvenation/` (195 traffic)
- `/locations/palm-beach-gardens/` (148 traffic)
- `/locations/boca-raton/` (95 traffic)
- `/` (86 traffic)
- `/locations/wellington/` (77 traffic)
- `/body-sculpting-at-new-radiance-cosmetic-centers/` (71 traffic)
- `/double-chin-reduction/` (52 traffic)
- `/dermal-fillers-boca-raton-florida/` (38 traffic)
- `/exilis-ultra-360-skin-tightening/` (37 traffic)
- `/specials/` (32 traffic)
- … 168 more in Ahrefs

### 3. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/skin-tightening/` (12 traffic)
- `/coolsculpting-elite/` (9 traffic)
- `/skin-rejuvenation/` (9 traffic)
- `/skin-care-services/`
- `/skin/`
- `/skin-tightening/`
- `/skin-care-services/`
- `/skin/`
- `/body/`
- `/coolsculpting-elite/`
- … 2 more in Ahrefs

### 4. Indexable page not in sitemap

`issue:indexable-page-not-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/locations/palm-beach-gardens/` (4 traffic)
- `/mini-facelift-vs-full-facelift-which-is-right-for-you/` (1 traffic)
- `/gallery-category/coolsculpting-elite/page/3/` (1 traffic)
- `/gallery/coolsculpting-elite-case-12/`
- `/video/coolsculpting-patient-experience/`
- `/locations/boca-raton/`
- `/experience-the-power-of-rf-microneedling-intensif-in-florida/`
- `/gallery-category/sculpsure-laser-lipo/page/4/`
- `/gallery/sculpsure-laser-lipo-case-9/`
- `/sculptra/`
- … 438 more in Ahrefs

### 5. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/gallery-category/coolsculpting-elite/page/3/` (1 traffic)
- `/gallery-category/emsculpt/page/2/`
- `/gallery-category/emsculpt/page/4/`
- `/gallery-category/sculpsure-laser-lipo/`
- `/gallery-category/coolsculpting-elite/page/4/`
- `/gallery/`
- `/gallery-category/facelift/`
- `/gallery-category/dysport/`
- `/gallery-category/skin-tightening-body-contouring/`
- `/gallery-category/emsculpt/page/5/`
- … 5 more in Ahrefs

### 6. FAQ page missing FAQPage schema

`issue:faq-page-missing-faqpage-schema` · schema-check · FLAG · decider: client

FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing.

- `/eyelid-surgery-faq-your-questions-answered/` (1 traffic)
- `/eyelid-surgery-faq-your-questions-answered/`
- `/dermal-fillers-faq-your-questions-answered/`
- `/dermal-fillers-faq-your-questions-answered/`
- `/coolsculpting-faq-your-questions-answered/`
- `/am-i-a-good-candidate-for-brow-lift/`
- `/coolsculpting-faq-your-questions-answered/`

### 7. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/category/rhinoplasty/`
- `/special/monthly-special-8/`
- `/category/face/page/2/`
- `/category/microneedling/`
- `/special-category/monthly-special/`
- `/special/free-consultation/`
- `/category/coolsculpting/`
- `/category/mommy-makeover/`
- `/category/skin/`
- … 27 more in Ahrefs

### 8. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/palm-beach-gardens?_gl=1*ibap5o*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/port-st-lucie?_gl=1*ibap5o*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/financing/`
- `/wellington?_gl=1*ibap5o*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/boca-raton?_gl=1*nb6lts*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/financing/`

### 9. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/coolsculpting-chin-treatment/`
- `/ipl-photofacial/`
- `/gallery/sculpsure-laser-lipo-case-7/`
- `/regain-confidence-with-emsella-incontinence-treatment-in-florida/`
- `/gallery/smart-liposuction-case-2/`
- `/gallery/emsculpt-case-17/`

### 10. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/palm-beach-gardens?_gl=1*ibap5o*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/port-st-lucie?_gl=1*ibap5o*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/wellington?_gl=1*ibap5o*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/boca-raton?_gl=1*nb6lts*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`

### 11. Pages fix-meta routed to ['/']

`fix-meta:` · ['/'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `homepage title`

### 12. Pages fix-meta routed to ['/author/dlm_seo/', '/author/dlm_developer/page/3/', '/author/dlm_developer/page/2/', '/author/dlm_admin/', '/author/dlm_admin/', '/author/dlm_seo/', '/author/dlm_seo/page/3/', '/author/dlm_seo/page/2/', '/author/dlm_seo/page/3/', '/category/uncategorized/', '/author/dlm_seo/page/4/', '/author/dlm_developer/page/4/', '/author/dlm_developer/page/2/', '/author/dlm_developer/page/3/', '/author/dlm_developer/', '/category/uncategorized/', '/video-category/alma-accent-pixel/', '/category/uncategorized/page/2/', '/author/dlm_developer/page/4/', '/video-category/tummy-tuck/', '/category/uncategorized/page/2/', '/author/dlm_seo/page/4/', '/author/dlm_developer/', '/video-category/emsella/', '/author/dlm_seo/page/2/', '/gallery-category/coolsculpting-elite/page/3/']

`fix-meta:author-dlm-seo-author-dlm-developer-page` · ['/author/dlm_seo/', '/author/dlm_developer/page/3/', '/author/dlm_developer/page/2/', '/author/dlm_admin/', '/author/dlm_admin/', '/author/dlm_seo/', '/author/dlm_seo/page/3/', '/author/dlm_seo/page/2/', '/author/dlm_seo/page/3/', '/category/uncategorized/', '/author/dlm_seo/page/4/', '/author/dlm_developer/page/4/', '/author/dlm_developer/page/2/', '/author/dlm_developer/page/3/', '/author/dlm_developer/', '/category/uncategorized/', '/video-category/alma-accent-pixel/', '/category/uncategorized/page/2/', '/author/dlm_developer/page/4/', '/video-category/tummy-tuck/', '/category/uncategorized/page/2/', '/author/dlm_seo/page/4/', '/author/dlm_developer/', '/video-category/emsella/', '/author/dlm_seo/page/2/', '/gallery-category/coolsculpting-elite/page/3/'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`

### 13. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/ipl-photo-facial/`
- `/hydrafacial/`
- `/membership/`

### 14. Broken redirect

`issue:broken-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/gallery-category/breast/`
- `/gallery-category/breast/`

### 15. HTTPS to HTTP redirect

`issue:https-to-http-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/`

### 16. X (Twitter) card missing

`issue:x-twitter-card-missing` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/palm-beach-gardens?_gl=1*ibap5o*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/beauty-bank`
- `/subscribe-notifications/`
- `/port-st-lucie?_gl=1*ibap5o*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/wellington?_gl=1*ibap5o*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/boca-raton?_gl=1*nb6lts*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/subscribe-notifications/`

### 17. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/palm-beach-gardens?_gl=1*ibap5o*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/port-st-lucie?_gl=1*ibap5o*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/wellington?_gl=1*ibap5o*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`
- `/boca-raton?_gl=1*nb6lts*_gcl_au*OTgxNDk1NTIwLjE3NTc5NTk5NDk.*_ga*MTQ0ODE5NTMxOS4xNzQxNzI1MDc0*_ga_TBP679T6FT*czE3NjM1NjAxOTkkbzE2MSRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDEwMTczNjExMjQ.*_ga_10D573LMBZ*czE3NjM1NjAyMDAkbzE3MiRnMSR0MTc2MzU2MjY0OCRqNTckbDAkaDA`

### 18. Open Graph tags missing

`issue:open-graph-tags-missing` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/beauty-bank`
- `/subscribe-notifications/`
- `/subscribe-notifications/`

### 19. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/?post_type=team&p=287`
- `/?post_type=team&p=280`
- `/?post_type=team&p=292`
- `/sofwave/`
- `/?post_type=team&p=292`
- `/microneedling-with-eclipse-micropen/`
- `/?post_type=team&p=289`
- `/?post_type=team&p=289`
- `/?post_type=team&p=280`
- `/sofwave/`
- … 6 more in Ahrefs

### 20. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/?post_type=team&p=287`
- `/?post_type=team&p=280`
- `/?post_type=team&p=292`
- `/sofwave/`
- `/?post_type=team&p=292`
- `/microneedling-with-eclipse-micropen/`
- `/?post_type=team&p=289`
- `/?post_type=team&p=289`
- `/?post_type=team&p=280`
- `/sofwave/`
- … 6 more in Ahrefs

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (36 pages: /category/rhinoplasty/, /special/monthly-special-8/, /category/face/page/2/, /category/microneedling/, …)

36 pages on newradiancenow.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

