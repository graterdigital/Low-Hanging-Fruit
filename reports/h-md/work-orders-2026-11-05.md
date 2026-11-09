# Work orders: h-md.com

Ahrefs Site Audit project 9704536 · crawl 2026-11-05 · health 98 · 29 active issue types → 14 work orders (0 decisions, 7 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Page has nofollow outgoing internal links | nofollow-audit | APPROVE (skill pending) | 227 | 477 (top 200 of 227) | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 2 | Organization schema missing or incomplete | schema-fix | APPROVE (skill pending) | 1 | 312 | agency | Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 3 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 54 | 9 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 4 | H1 tag missing or empty | manual | FLAG | 35 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 5 | Slow page | manual | FLAG | 12 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 6 | Slow server response for AI crawlers | hosting/cache | FLAG | 8 | 0 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 7 | Pages fix-meta routed to [] | [] | FLAG | 3 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 8 | Product page missing Product schema | schema-check | FLAG | 3 | 0 | agency | Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages. |
| 9 | Pages fix-meta routed to ['/category/blog/page/4', '/category/blog/page/12', '/category/blog', '/position/injectors/page/2', '/category/blog/page/5', '/services/page/3', '/category/blog/page/6', '/category/blog/page/2', '/services/page/2', '/category/blog/page/9', '/category/blog/page/11', '/category/blog/page/3', '/category/blog/page/7', '/category/blog/page/10', '/category/blog/page/13', '/category/blog/page/8'] | ['/category/blog/page/4', '/category/blog/page/12', '/category/blog', '/position/injectors/page/2', '/category/blog/page/5', '/services/page/3', '/category/blog/page/6', '/category/blog/page/2', '/services/page/2', '/category/blog/page/9', '/category/blog/page/11', '/category/blog/page/3', '/category/blog/page/7', '/category/blog/page/10', '/category/blog/page/13', '/category/blog/page/8'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 10 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 11 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 3 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 12 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 1 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 13 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 1 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 14 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 1 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Page has nofollow outgoing internal links

`issue:page-has-nofollow-outgoing-internal-links` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

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

### 2. Organization schema missing or incomplete

`issue:organization-schema-missing-or-incomplete` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (312 traffic)

### 3. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

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

### 4. H1 tag missing or empty

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

### 5. Slow page

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

### 6. Slow server response for AI crawlers

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

### 7. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `noindex`
- `non-200`
- `homepage title`

### 8. Product page missing Product schema

`issue:product-page-missing-product-schema` · schema-check · FLAG · decider: agency

Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages.

- `/say-goodbye-fine-lines-wrinkles-radiesse-okc`
- `/treat-dynamic-wrinkles-botox-cosmetic`
- `/botox-oklahoma-city-candidate`

### 9. Pages fix-meta routed to ['/category/blog/page/4', '/category/blog/page/12', '/category/blog', '/position/injectors/page/2', '/category/blog/page/5', '/services/page/3', '/category/blog/page/6', '/category/blog/page/2', '/services/page/2', '/category/blog/page/9', '/category/blog/page/11', '/category/blog/page/3', '/category/blog/page/7', '/category/blog/page/10', '/category/blog/page/13', '/category/blog/page/8']

`fix-meta:category-blog-page-4-category-blog-page-` · ['/category/blog/page/4', '/category/blog/page/12', '/category/blog', '/position/injectors/page/2', '/category/blog/page/5', '/services/page/3', '/category/blog/page/6', '/category/blog/page/2', '/services/page/2', '/category/blog/page/9', '/category/blog/page/11', '/category/blog/page/3', '/category/blog/page/7', '/category/blog/page/10', '/category/blog/page/13', '/category/blog/page/8'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`

### 10. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/financing`

### 11. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/service_type/laser-procedures`
- `/service_type/medical-aesthetics`
- `/service_type/injectables`

### 12. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/health-optimization/`

### 13. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/health-optimization/`

### 14. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/improve-overall-wellness-bioidentical-hormones-oklahoma-city`

## Skipped on purpose

- Indexable page not in sitemap (15): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

