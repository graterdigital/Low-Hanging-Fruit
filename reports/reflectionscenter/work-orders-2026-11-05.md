# Work orders: reflectionscenter.com

Ahrefs Site Audit project 9704548 · crawl 2026-11-05 · health 14 · 63 active issue types → 29 work orders (2 decisions, 15 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 2052 | 14951 (top 200 of 2052) | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 2 | Structured data has schema.org validation error | schema-fix | FLAG | 2133 | 14903 (top 200 of 2133) | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 3 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 1324 | 8315 (top 200 of 1324) | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 4 | Indexable page not in sitemap | indexation-review | APPROVE (skill pending) | 312 | 116 (top 200 of 312) | agency | Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 5 | Slow page | manual | FLAG | 29 | 87 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 6 | Category page missing ItemList schema | schema-check | FLAG | 9 | 76 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 7 | Slow server response for AI crawlers | hosting/cache | FLAG | 14 | 74 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 8 | X (Twitter) card incomplete | fix-social-tags | AUTO (skill pending) | 186 | 61 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 9 | 3XX page receives organic traffic | redirect-rules | APPROVE (skill pending) | 2 | 54 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 10 | FAQ page missing FAQPage schema | schema-check | FLAG | 3 | 1 | client | FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing. |
| 11 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 72 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page. |
| 12 | Orphan page (has no incoming internal links) | indexation-review | decide | 2 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 13 | H1 tag missing or empty | manual | FLAG | 4 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 14 | Low word count | manual | FLAG | 3 | 0 | client | Content call: expand, merge or noindex the page. Client decides what the page is for. |
| 15 | Page has no outgoing links | manual | FLAG | 3 | 0 | client | Content call: add relevant internal links or accept it (thank-you and utility pages are fine). |
| 16 | Pages fix-meta routed to ['/'] | ['/'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 17 | Pages fix-meta routed to ['/before-after-photos-new-jersey/q-switched-lasers/', '/before-after-photos-new-jersey/q-switched-yag/'] | ['/before-after-photos-new-jersey/q-switched-lasers/', '/before-after-photos-new-jersey/q-switched-yag/'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 18 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 19 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 50 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 20 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 22 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 21 | Page has nofollow outgoing internal links | nofollow-audit | APPROVE (skill pending) | 6 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 22 | Page in multiple sitemaps | indexation-review | APPROVE (skill pending) | 5 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 23 | Broken redirect | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 24 | Open Graph tags missing | fix-social-tags | AUTO (skill pending) | 3 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 25 | X (Twitter) card missing | fix-social-tags | AUTO (skill pending) | 3 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 26 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 88 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 27 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 88 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 28 | Page has links to broken page  (non-indexable pages) | fix-broken-links | AUTO/APPROVE (skill pending) | 82 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 29 | Duplicate pages without canonical | review | ? | 41 | 0 | agency | Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster) |

## Per item

### 1. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/before-after-photos-new-jersey/rf-microneedling/` (3206 traffic)
- `/new-jersey-medical-spa-conditions/face/rosacea/` (1177 traffic)
- `/how-many-syringes-of-filler-do-i-need/` (746 traffic)
- `/gallery/juvederm-lip-filler-for-very-thin-lips/` (488 traffic)
- `/before-after-photos-new-jersey/sebaceous-hyperplasia/` (471 traffic)
- `/before-after-photos-new-jersey/laser-liposuction/` (457 traffic)
- `/` (455 traffic)
- `/plasma-pen-dangers-and-alternative-treatments/` (346 traffic)
- `/new-jersey-medical-spa/botox-fillers/botox-for-the-nasal-tip/` (284 traffic)
- `/botox-for-tmj/` (273 traffic)
- … 2042 more in Ahrefs

### 2. Structured data has schema.org validation error

`issue:structured-data-has-schema-org-validation-error` · schema-fix · FLAG · decider: agency

Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit.

- `/before-after-photos-new-jersey/rf-microneedling/` (3206 traffic)
- `/new-jersey-medical-spa-conditions/face/rosacea/` (1177 traffic)
- `/how-many-syringes-of-filler-do-i-need/` (746 traffic)
- `/gallery/juvederm-lip-filler-for-very-thin-lips/` (488 traffic)
- `/before-after-photos-new-jersey/sebaceous-hyperplasia/` (471 traffic)
- `/before-after-photos-new-jersey/laser-liposuction/` (457 traffic)
- `/` (455 traffic)
- `/plasma-pen-dangers-and-alternative-treatments/` (346 traffic)
- `/new-jersey-medical-spa/botox-fillers/botox-for-the-nasal-tip/` (284 traffic)
- `/botox-for-tmj/` (273 traffic)
- … 2123 more in Ahrefs

### 3. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/before-after-photos-new-jersey/rf-microneedling/` (3206 traffic)
- `/gallery/juvederm-lip-filler-for-very-thin-lips/` (488 traffic)
- `/before-after-photos-new-jersey/sebaceous-hyperplasia/` (471 traffic)
- `/before-after-photos-new-jersey/laser-liposuction/` (457 traffic)
- `/new-jersey-medical-spa-conditions/face/melasma-treatment/` (264 traffic)
- `/gallery/botox-injection-nasal-tip-lift/` (230 traffic)
- `/new-jersey-medical-spa-technologies/dermal-fillers/collagen-stimulating-injections/` (153 traffic)
- `/new-jersey-medical-spa/botox-fillers/fat-dissolving-injections/` (136 traffic)
- `/new-jersey-medical-spa/body/stretch-mark/` (121 traffic)
- `/before-after-photos-new-jersey/sofwave/` (111 traffic)
- … 1314 more in Ahrefs

### 4. Indexable page not in sitemap

`issue:indexable-page-not-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/monthly-promos` (51 traffic)
- `/patient-stories/they-always-make-me-look-so-beautiful/` (27 traffic)
- `/patient-stories/rebecca-acne-treatment-patient/` (14 traffic)
- `/patient-stories/you-guys-at-reflections-are-so-wonderful/` (11 traffic)
- `/patient-stories/removing-tattooed-freckles-that-turned-out-too-dark-unnatural/` (8 traffic)
- `/apple-stem-cells-the-next-anti-aging-phenomena/` (4 traffic)
- `/patient-stories/lasers-skincare-didnt-work-for-my-melasma-until-i-tried-tranexamic-acid-txa-pills/` (1 traffic)
- `/patient-stories/show-stopping-results-from-acne-scar-surgery/`
- `/patient-stories/coolsculpting-review-i-threw-out-my-spanx/`
- `/before-after-photos-new-jersey/ideal-eyes-undereye/`
- … 302 more in Ahrefs

### 5. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/gallery/marionette-lines-around-mouth-filler-results-for-woman-in-her-late-60s/` (45 traffic)
- `/new-jersey-medical-spa-technologies/body-sculpting-fat-reduction/coolsculpting/` (23 traffic)
- `/new-jersey-medical-spa/surgical/lower-facelift/` (9 traffic)
- `/about/our-locations/bridgewater-twp-nj/` (4 traffic)
- `/gallery/botox-for-under-eye-wrinkles-frown-lines/` (4 traffic)
- `/about/our-locations/livingston-nj/` (2 traffic)
- `/people-look-into-laser-tattoo-removal-to-expand-career-opportunities/`
- `/new-jersey-medical-spa-conditions/face/jowls-jawline-sag/`
- `/gallery/under-eye-wrinkles-treated-with-botox-injections/`
- `/about/dollars-sense/rewards-plus/`
- … 19 more in Ahrefs

### 6. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/before-after-photos-new-jersey/q-switched-lasers/` (40 traffic)
- `/before-after-photos-new-jersey/q-switched-yag/` (36 traffic)
- `/new-jersey-medical-spa/face/defenage-skincare-products/`
- `/before-after-photos-new-jersey/sebacia/`
- `/before-after-photos-new-jersey/qwo/`
- `/before-after-photos-new-jersey/belotero/`
- `/before-after-photos-new-jersey/refyne/`
- `/before-after-photos-new-jersey/q-switched-ruby-laser/`
- `/before-after-photos-new-jersey/arms/`

### 7. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/gallery/marionette-lines-around-mouth-filler-results-for-woman-in-her-late-60s/` (45 traffic)
- `/new-jersey-medical-spa-technologies/body-sculpting-fat-reduction/coolsculpting/` (23 traffic)
- `/about/our-locations/bridgewater-twp-nj/` (4 traffic)
- `/about/our-locations/livingston-nj/` (2 traffic)
- `/people-look-into-laser-tattoo-removal-to-expand-career-opportunities/`
- `/new-jersey-medical-spa-conditions/face/jowls-jawline-sag/`
- `/about/dollars-sense/rewards-plus/`
- `/new-jersey-medical-spa-conditions/face/hair-loss-thinning-hair/`
- `/prepare-for-summers-leg-baring-fashions-with-laser-hair-removal/`
- `/five-hottest-medical-spa-treatments-right-now/`
- … 4 more in Ahrefs

### 8. X (Twitter) card incomplete

`issue:x-twitter-card-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/patient-stories/they-always-make-me-look-so-beautiful/` (27 traffic)
- `/patient-stories/rebecca-acne-treatment-patient/` (14 traffic)
- `/patient-stories/you-guys-at-reflections-are-so-wonderful/` (11 traffic)
- `/patient-stories/removing-tattooed-freckles-that-turned-out-too-dark-unnatural/` (8 traffic)
- `/patient-stories/lasers-skincare-didnt-work-for-my-melasma-until-i-tried-tranexamic-acid-txa-pills/` (1 traffic)
- `/patient-stories/show-stopping-results-from-acne-scar-surgery/`
- `/patient-stories/coolsculpting-review-i-threw-out-my-spanx/`
- `/patient-stories/its-really-something-to-do-for-me-my-experience-with-fillers-at-74/`
- `/patient-stories/looking-forward-to-my-laser-lipo-procedure-for-under-my-chin/`
- `/patient-stories/i-regained-my-confidence/`
- … 176 more in Ahrefs

### 9. 3XX page receives organic traffic

`issue:3xx-page-receives-organic-traffic` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/gallery` (43 traffic)
- `/gallery-category/lip-filler/` (11 traffic)

### 10. FAQ page missing FAQPage schema

`issue:faq-page-missing-faqpage-schema` · schema-check · FLAG · decider: client

FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing.

- `/restylane-faq-your-questions-answered/` (1 traffic)
- `/microneedling-faq-your-questions-answered/`
- `/kybella-faq-your-questions-answered/`

### 11. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page.

- `/review-us/leave-us-a-review-sl/`
- `/review-us/leave-us-a-review-sh/`
- `/review-us/leave-us-a-review-jc/`
- `/thank-you-2/`
- `/review-us/leave-us-a-review-al/`
- `/thank-you-3/`
- `/review-us/leave-us-a-review-ap/`
- `/review-us/leave-us-a-review-chasin/`
- `/review-us/leave-us-a-review-ms/`
- `/review-us/leave-us-a-review-ellern/`
- … 62 more in Ahrefs

### 12. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/author/dlm_seo/`
- `/sitemap/`

### 13. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/kybella-double-chin-fat-reduction/`
- `/news/connecting-cosmetic-surgery-mental-health-with-dr-mitchell-chasin/`
- `/gallery/1cc-silk-for-under-eyes-filler-results/`
- `/schedule-free-consultation/`

### 14. Low word count

`issue:low-word-count` · manual · FLAG · decider: client

Content call: expand, merge or noindex the page. Client decides what the page is for.

- `/kybella-double-chin-fat-reduction/`
- `/news/connecting-cosmetic-surgery-mental-health-with-dr-mitchell-chasin/`
- `/gallery/1cc-silk-for-under-eyes-filler-results/`

### 15. Page has no outgoing links

`issue:page-has-no-outgoing-links` · manual · FLAG · decider: client

Content call: add relevant internal links or accept it (thank-you and utility pages are fine).

- `/kybella-double-chin-fat-reduction/`
- `/news/connecting-cosmetic-surgery-mental-health-with-dr-mitchell-chasin/`
- `/gallery/1cc-silk-for-under-eyes-filler-results/`

### 16. Pages fix-meta routed to ['/']

`fix-meta:` · ['/'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `homepage title`

### 17. Pages fix-meta routed to ['/before-after-photos-new-jersey/q-switched-lasers/', '/before-after-photos-new-jersey/q-switched-yag/']

`fix-meta:before-after-photos-new-jersey-q-switche` · ['/before-after-photos-new-jersey/q-switched-lasers/', '/before-after-photos-new-jersey/q-switched-yag/'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`

### 18. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/about/dollars-sense/financing-options/`

### 19. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/yes-you-still-have-time-to-look-your-best-for-high-school-reunions/`
- `/beauty-may-not-be-skin-deep-after-all/`
- `/turn-your-frown-upside-down-consider-a-cosmetic-procedure-to-boost-youthfulness-and-self-esteem/`
- `/a-surprisingly-good-use-for-nicotine/`
- `/what-is-a-varicose-vein-anyway/`
- `/americans-shape-up-with-the-help-of-laser-liposuction/`
- `/rapidtat-laser-tattoo-removal-procedure/`
- `/about/privacy-policy/`
- `/ultherapy-ultrasound-skin-tightening-treatment/`
- `/laser-lipo-post-pregnancy-is-this-the-new-tummy-tuck/`
- … 40 more in Ahrefs

### 20. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/review-us/leave-us-a-review-sl/`
- `/review-us/leave-us-a-review-sh/`
- `/review-us/leave-us-a-review-jc/`
- `/thank-you-2/`
- `/review-us/leave-us-a-review-al/`
- `/thank-you-3/`
- `/review-us/leave-us-a-review-ap/`
- `/review-us/leave-us-a-review-chasin/`
- `/review-us/leave-us-a-review-ms/`
- `/review-us/leave-us-a-review-ellern/`
- … 12 more in Ahrefs

### 21. Page has nofollow outgoing internal links

`issue:page-has-nofollow-outgoing-internal-links` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/botox-for-mens-forehead-treatment-guide/`
- `/restylane-defyne-in-millburn-nj/`
- `/restylane-kysse-in-west-orange-nj/`
- `/restylane-refyne-in-millburn-nj/`
- `/microneedling-faq-your-questions-answered/`
- `/everything-you-need-to-know-about-botox/`

### 22. Page in multiple sitemaps

`issue:page-in-multiple-sitemaps` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/restylane-kysse-in-west-orange-nj/`
- `/botox-is-now-a-treatment-option-for-canadians-who-experience-chronic-migraines/`
- `/botox-injections-are-best-left-to-trained-professionals-doctors-say/`
- `/botox-or-fillers-may-be-perfect-complement-to-cosmetic-dental-procedures/`
- `/restylane-kysse-in-millburn-nj/`

### 23. Broken redirect

`issue:broken-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/laser-hair-removal-hurt-much/`

### 24. Open Graph tags missing

`issue:open-graph-tags-missing` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/kybella-double-chin-fat-reduction/`
- `/news/connecting-cosmetic-surgery-mental-health-with-dr-mitchell-chasin/`
- `/gallery/1cc-silk-for-under-eyes-filler-results/`

### 25. X (Twitter) card missing

`issue:x-twitter-card-missing` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/kybella-double-chin-fat-reduction/`
- `/news/connecting-cosmetic-surgery-mental-health-with-dr-mitchell-chasin/`
- `/gallery/1cc-silk-for-under-eyes-filler-results/`

### 26. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/?post_type=gallery&p=2937`
- `/?post_type=gallery&p=3245`
- `/?post_type=gallery&p=3906`
- `/?post_type=gallery&p=9174`
- `/?post_type=gallery&p=3755`
- `/?post_type=gallery&p=3829`
- `/?page_id=979`
- `/?post_type=gallery&p=9223`
- `/?post_type=gallery&p=3501`
- `/new-jersey-medical-spa/botox-fillershttps://www.reflectionscenter.com/new-jersey-medical-spa/botox-fillers/botox-for-the-nasal-tip/`
- … 78 more in Ahrefs

### 27. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/?post_type=gallery&p=2937`
- `/?post_type=gallery&p=3245`
- `/?post_type=gallery&p=3906`
- `/?post_type=gallery&p=9174`
- `/?post_type=gallery&p=3755`
- `/?post_type=gallery&p=3829`
- `/?page_id=979`
- `/?post_type=gallery&p=9223`
- `/?post_type=gallery&p=3501`
- `/new-jersey-medical-spa/botox-fillershttps://www.reflectionscenter.com/new-jersey-medical-spa/botox-fillers/botox-for-the-nasal-tip/`
- … 78 more in Ahrefs

### 28. Page has links to broken page  (non-indexable pages)

`issue:page-has-links-to-broken-page-nonindexable` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/tag/volume/`
- `/about/in-the-media/page/6/`
- `/about/in-the-media/page/4/`
- `/category/microneedling/`
- `/tag/aging-lips/`
- `/review-us/leave-us-a-review-sl/`
- `/tag/aging/`
- `/tag/anti-aging/page/2/`
- `/tag/wrinkles/page/3/`
- `/category/laser-hair-removal/`
- … 72 more in Ahrefs

### 29. Duplicate pages without canonical

`issue:duplicate-pages-without-canonical` · review · ? · decider: agency

Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster)

- `/about/news/tv/page/11/`
- `/about/news/print/page/11/`
- `/kybella-double-chin-fat-reduction/`
- `/about/news/print/page/9/`
- `/before-after-photos-new-jersey/Thread-Lifts/`
- `/about/news/online/page/7/`
- `/about/news/tv/page/9/`
- `/about/news/tv/page/20/`
- `/about/news/online/page/8/`
- `/about/news/tv/page/16/`
- … 31 more in Ahrefs

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (72 pages: /review-us/leave-us-a-review-sl/, /review-us/leave-us-a-review-sh/, /review-us/leave-us-a-review-jc/, /thank-you-2/, …)

72 pages on reflectionscenter.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

**Orphan page (has no incoming internal links)** (2 pages: /author/dlm_seo/, /sitemap/)

2 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

