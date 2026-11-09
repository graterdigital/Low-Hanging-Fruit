# Work orders: curatemedspa.com

Ahrefs Site Audit project 9704524 · crawl 2026-11-05 · health 99 · 35 active issue types → 16 work orders (1 decisions, 9 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Organization schema missing or incomplete | schema-fix | APPROVE (skill pending) | 1 | 128 | agency | Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 2 | Slow page | manual | FLAG | 10 | 68 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 3 | Page has nofollow outgoing internal links | nofollow-audit | APPROVE (skill pending) | 9 | 61 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 4 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 11 | 21 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 5 | Slow server response for AI crawlers | hosting/cache | FLAG | 2 | 6 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 6 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 1 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 7 | H1 tag missing or empty | manual | FLAG | 6 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 8 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 2 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 9 | Pages fix-meta routed to ['/'] | ['/'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 10 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 11 | Canonical from HTTP to HTTPS | redirect-rules | APPROVE (skill pending) | 7 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 12 | 302 redirect | redirect-rules | APPROVE (skill pending) | 5 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 13 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 2 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 14 | HTTPS to HTTP redirect | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 15 | Indexable page not in sitemap | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 16 | X (Twitter) card missing | fix-social-tags | AUTO (skill pending) | 1 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |

## Per item

### 1. Organization schema missing or incomplete

`issue:organization-schema-missing-or-incomplete` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (128 traffic)

### 2. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/dermal-fillers/` (61 traffic)
- `/iv-hydration-therapy/` (6 traffic)
- `/dermal-fillers-vs-botox-guide/` (1 traffic)
- `/services/vitamin-injections/`
- `/home-2/`
- `/laser-hair-removal-chattanooga-winter/`
- `/skin-tightening-2025/`
- `/sculptra/`
- `/anti-aging-2025/`
- `/botox/`

### 3. Page has nofollow outgoing internal links

`issue:page-has-nofollow-outgoing-internal-links` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/dermal-fillers/` (61 traffic)
- `/privacy-policy/`
- `/blog/`
- `/services/vitamin-injections/`
- `/services/cooltone/`
- `/services/dermal-fillers/`
- `/services/pdo-threads/`
- `/services/iv-therapy/`
- `/pdo-threads/`

### 4. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/locations/murfreesboro/` (13 traffic)
- `/treatment-for-excessive-sweating-in-2025/` (5 traffic)
- `/locations/nashville/` (3 traffic)
- `/privacy-policy/`
- `/locations/ooltewah/`
- `/blog/`
- `/financing/`
- `/the-reserve`
- `/locations/knoxville/`
- `/terms-conditions/`
- … 1 more in Ahrefs

### 5. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/iv-hydration-therapy/` (6 traffic)
- `/skin-tightening-2025/`

### 6. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/tag/weekly-newsletter/`

### 7. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/locations/ooltewah/`
- `/services/pdo-threads/`
- `/locations/knoxville/`
- `/terms-conditions/`
- `/pdo-threads/`
- `/locations/chattanooga/`

### 8. H1 tag missing or empty  (non-indexable pages)

`issue:h1-tag-missing-or-empty-nonindexable` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/terms-conditions/`
- `/tag/weekly-newsletter/`

### 9. Pages fix-meta routed to ['/']

`fix-meta:` · ['/'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `homepage title`

### 10. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/financing/`

### 11. Canonical from HTTP to HTTPS

`issue:canonical-from-http-to-https` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/dermal-fillers/`
- `/contact/`
- `/injectable-services/`
- `/privacy-policy/`
- `/sculptra/`
- `/botox/`
- `/terms-conditions/`

### 12. 302 redirect

`issue:302-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/the-reserve/button/kGsxVn6q2byOry4L6MmhemRaCrG7ManT`
- `/the-reserve/button/lzcaWCTg8PzTOmn61hzMK7NRlzRUwn8s`
- `/the-reserve/button/dxlw6rQl2S3ys4HISh7cz8sSTh4rPfEL`
- `/the-reserve/button/Xrgf82x5KKylCzDZXia51t2t7Mbry1Ci`
- `/the-reserve/button/kSFwFAqmAAx8vxHUhFgU4bDCV5z1AkyD`

### 13. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/dermal-fillers/`
- `/privacy-policy/`

### 14. HTTPS to HTTP redirect

`issue:https-to-http-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/injectable-services/?utm_source=chatgpt.com`

### 15. Indexable page not in sitemap

`issue:indexable-page-not-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/the-reserve`

### 16. X (Twitter) card missing

`issue:x-twitter-card-missing` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/the-reserve`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (1 page: /tag/weekly-newsletter/)

1 page on curatemedspa.com is set so Google does not index it (or does not follow its links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

