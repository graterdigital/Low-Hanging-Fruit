# Work orders: synergymedaesthetics.com

Ahrefs Site Audit project 9704552 · crawl 2026-11-05 · health 97 · 29 active issue types → 15 work orders (0 decisions, 11 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Page has nofollow outgoing internal links | nofollow-audit | APPROVE (skill pending) | 73 | 339 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 2 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 43 | 82 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 3 | Organization schema missing or incomplete | schema-fix | APPROVE (skill pending) | 1 | 70 | agency | Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 4 | Slow page | manual | FLAG | 10 | 7 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 5 | Canonical points to redirect | redirect-rules | APPROVE (skill pending) | 4 | 7 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 6 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 4 | 7 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 7 | Pages fix-meta routed to [] | [] | FLAG | 3 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 8 | Pages fix-meta routed to ['/treatments/page/2/'] | ['/treatments/page/2/'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 9 | Slow server response for AI crawlers | hosting/cache | FLAG | 1 | 0 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 10 | Non-canonical page in sitemap | indexation-review | APPROVE (skill pending) | 3 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 11 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 2 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 12 | Redirect loop | redirect-rules | APPROVE (skill pending) | 2 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 13 | Broken redirect | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 14 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 1 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 15 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 1 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Page has nofollow outgoing internal links

`issue:page-has-nofollow-outgoing-internal-links` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/location/kennewick/` (154 traffic)
- `/location/yakima/` (81 traffic)
- `/` (70 traffic)
- `/contact/kennewick-location/` (15 traffic)
- `/blog/` (12 traffic)
- `/hair-body/laser-hair-removal/` (6 traffic)
- `/contact/yakima-location/` (1 traffic)
- `/faqs/how-often-can-i-receive-a-coolpeel-treatment/`
- `/faqs/does-the-suction-applicator-leave-marks/`
- `/hair-body/sculptra-butt-lift/`
- … 63 more in Ahrefs

### 2. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/` (70 traffic)
- `/blog/` (12 traffic)
- `/faqs/how-often-can-i-receive-a-coolpeel-treatment/`
- `/faqs/does-the-suction-applicator-leave-marks/`
- `/about/meet-our-team/`
- `/faqs/how-long-is-the-treatment/`
- `/faqs/are-there-any-side-effects-of-botox/`
- `/treatments/page/2/`
- `/faqs/are-there-any-side-effects-associated-with-injectables/`
- `/faqs/is-there-any-downtime-after-facials-prf-treatments-or-synergy-lift-treatments/`
- … 33 more in Ahrefs

### 3. Organization schema missing or incomplete

`issue:organization-schema-missing-or-incomplete` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (70 traffic)

### 4. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/face/` (7 traffic)
- `/faqs/does-the-suction-applicator-leave-marks/`
- `/about/meet-our-team/`
- `/treatments/page/2/`
- `/injectables/wrinkle-relaxers/`
- `/faqs/what-are-the-potential-side-effects-of-dysport/`
- `/skin/`
- `/hair-body/`
- `/treatments/`
- `/injectables/fillers-injectables/`

### 5. Canonical points to redirect

`issue:canonical-points-to-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/face/` (7 traffic)
- `/skin/`
- `/hair-body/`
- `/injectables/`

### 6. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/face/` (7 traffic)
- `/skin/`
- `/hair-body/`
- `/injectables/`

### 7. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `noindex`
- `non-200`
- `homepage title`

### 8. Pages fix-meta routed to ['/treatments/page/2/']

`fix-meta:treatments-page-2` · ['/treatments/page/2/'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`

### 9. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/faqs/does-the-suction-applicator-leave-marks/`

### 10. Non-canonical page in sitemap

`issue:non-canonical-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/skin/`
- `/hair-body/`
- `/injectables/`

### 11. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/meet-rene-your-expert-injector-in-eastern-washington/`
- `/skin-care-basics-simple-but-necessary/`

### 12. Redirect loop

`issue:redirect-loop` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/meet-rene-your-expert-injector-in-eastern-washington/`
- `/skin-care-basics-simple-but-necessary/`

### 13. Broken redirect

`issue:broken-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/category/gallery/`

### 14. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/category/home/`

### 15. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/category/home/`

## Skipped on purpose

- Indexable page not in sitemap (1): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

