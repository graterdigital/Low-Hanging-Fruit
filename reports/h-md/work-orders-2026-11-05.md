# Work orders: h-md.com

Ahrefs Site Audit project 9704536 · crawl 2026-11-05 · health 98 · 29 active issue types → 13 work orders (0 decisions, 5 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | H1 tag missing or empty | manual | FLAG | 35 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 2 | Slow page | manual | FLAG | 12 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 3 | Slow server response for AI crawlers | hosting/cache | FLAG | 8 | 0 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 4 | Product page missing Product schema | schema-check | FLAG | 3 | 0 | agency | Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages. |
| 5 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 6 | Pages fix-meta routed to homepage title | homepage title | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 7 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 8 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 9 | Waiting on skill `nofollow-audit` (1 issue type): Page has nofollow outgoing internal links (227) | nofollow-audit | skill pending | 227 | 477 | agency | Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 10 | Waiting on skill `schema-fix` (1 issue type): Organization schema missing or incomplete (1) | schema-fix | skill pending | 1 | 312 | agency | Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 11 | Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (54) | fix-social-tags | skill pending | 54 | 9 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 12 | Waiting on skill `fix-broken-links` (3 issue types): 404 page (1); 4XX page (1); Page has links to broken page (1) | fix-broken-links | skill pending | 3 | 0 | agency | Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 13 | Waiting on skill `redirect-rules` (1 issue type): 3XX redirect in sitemap (3) | redirect-rules | skill pending | 3 | 0 | agency | Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |

## Per item

### 1. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/category/blog/page/4`
- `/specialty/le`
- `/specialty/master-injector`
- `/category/blog/page/12`
- `/specialty/aprn`
- `/team_locations/okc`
- `/category/blog`
- `/specialty/pa-c`
- `/position/injectors/page/2`
- `/position/aestheticians-and-administrative-staff`
- … 25 more in Ahrefs

### 2. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/consider-liposuction-neck-okc`
- `/smooth-signs-aging-botox`
- `/say-goodbye-fine-lines-wrinkles-radiesse-okc`
- `/5-simple-ways-to-manage-female-incontinence-this-summer`
- `/tired-thinning-hair-learn-hair-restoration-okc`
- `/refresh-skin-microneedling`
- `/get-summer-ready-laser-hair-removal-oklahoma-city`
- `/botox-oklahoma-city-candidate`
- `/enjoy-lasting-results-laser-hair-removal-oklahoma-city`
- `/get-smoother-skin-laser-hair-removal-okc`
- … 2 more in Ahrefs

### 3. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/say-goodbye-fine-lines-wrinkles-radiesse-okc`
- `/tired-thinning-hair-learn-hair-restoration-okc`
- `/refresh-skin-microneedling`
- `/get-summer-ready-laser-hair-removal-oklahoma-city`
- `/botox-oklahoma-city-candidate`
- `/get-smoother-skin-laser-hair-removal-okc`
- `/volumize-with-juvederm-in-oklahoma-city`
- `/consider-xeomin-okc`

### 4. Product page missing Product schema

`issue:product-page-missing-product-schema` · schema-check · FLAG · decider: agency

Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages.

- `/say-goodbye-fine-lines-wrinkles-radiesse-okc`
- `/treat-dynamic-wrinkles-botox-cosmetic`
- `/botox-oklahoma-city-candidate`

### 5. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/financing`

### 6. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 7. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 8. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 9. Waiting on skill `nofollow-audit` (1 issue type): Page has nofollow outgoing internal links (227)

`pending:nofollow-audit` · nofollow-audit · skill pending · decider: agency

Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/` (312 traffic)
- `/services/dermal-fillers` (106 traffic)
- `/services/dysport` (25 traffic)
- `/services/coolsculpting-elite` (17 traffic)
- `/our-locations/tulsa` (6 traffic)
- `/injectables` (5 traffic)
- `/our_team/aunisty-moore` (2 traffic)
- `/about/our-team` (1 traffic)
- `/our-locations/okc` (1 traffic)
- `/contact-us` (1 traffic)
- … 217 more in Ahrefs

### 10. Waiting on skill `schema-fix` (1 issue type): Organization schema missing or incomplete (1)

`pending:schema-fix` · schema-fix · skill pending · decider: agency

Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (312 traffic)

### 11. Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (54)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/our-locations/tulsa` (6 traffic)
- `/about/our-team` (1 traffic)
- `/our-locations/okc` (1 traffic)
- `/contact-us` (1 traffic)
- `/before_after/5`
- `/financing`
- `/category/blog/page/4`
- `/specialty/le`
- `/specialty/master-injector`
- `/category/blog/page/12`
- … 44 more in Ahrefs

### 12. Waiting on skill `fix-broken-links` (3 issue types): 404 page (1); 4XX page (1); Page has links to broken page (1)

`pending:fix-broken-links` · fix-broken-links · skill pending · decider: agency

Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/health-optimization/`
- … 2 more in Ahrefs

### 13. Waiting on skill `redirect-rules` (1 issue type): 3XX redirect in sitemap (3)

`pending:redirect-rules` · redirect-rules · skill pending · decider: agency

Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/service_type/laser-procedures`
- `/service_type/medical-aesthetics`
- `/service_type/injectables`

## Skipped on purpose

- Indexable page not in sitemap (15): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

