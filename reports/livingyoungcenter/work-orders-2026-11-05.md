# Work orders: livingyoungcenter.com

Ahrefs Site Audit project 9704535 · crawl 2026-11-05 · health 48 · 34 active issue types → 11 work orders (1 decisions, 7 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 91 | 580 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 2 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 3 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 3 | Pages fix-meta routed to [] | [] | FLAG | 4 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 4 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 5 | Slow page | manual | FLAG | 1 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 6 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 3 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 7 | Canonical points to redirect | redirect-rules | APPROVE (skill pending) | 2 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 8 | Non-canonical page in sitemap | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 9 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 10 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 10 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 10 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 11 | Page has links to broken page  (non-indexable pages) | fix-broken-links | AUTO/APPROVE (skill pending) | 5 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/` (217 traffic)
- `/wellness-health/lipolean/` (123 traffic)
- `/blog/lip-filler-in-tampa-the-complete-guide/` (53 traffic)
- `/tampa-bay-med-spa/best-med-spa-in-st-pete/` (41 traffic)
- `/tampa-bay-med-spa/best-med-spa-odessa/` (29 traffic)
- `/non-surgical-nose-job/` (24 traffic)
- `/blog/how-many-units-of-botox/` (17 traffic)
- `/acne-scar-treatment/` (13 traffic)
- `/wellness-health/peptide-therapy/` (13 traffic)
- `/blog/peptide-therapy-tampa-guide/` (11 traffic)
- … 81 more in Ahrefs

### 2. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/category/med-spa/`
- `/category/blog/`
- `/category/injectables/`

### 3. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`
- `noindex`
- `non-200`
- `homepage title`

### 4. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/resources/financing/`

### 5. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/blog/hrt-women-tampa-bay-guide/`

### 6. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/wellness-health/specialty-testing/multiple-autoimmune-reactivity-screen/`
- `/medical-spa/`
- `/wellness-health/specialty-testing/heavy-metal-testing/`

### 7. Canonical points to redirect

`issue:canonical-points-to-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/?page_id=9288`
- `/testosterone-therapy/`

### 8. Non-canonical page in sitemap

`issue:non-canonical-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/testosterone-therapy/`

### 9. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/locations/seminole/`
- `/seminole/`
- `/st-petersburg/`
- `/medical-spa/dermal-fillers/brands/radiesse/`
- `/financing/`
- `/medical-spa/dermal-fillers/treatment-areas/`
- `/odessa/`
- `/black-friday-specials-2025/`
- `/medical-spa/dermal-fillers/brands/lip-augmentation/`
- `/medical-spa/dermal-fillers/brands/rha-fillers/`

### 10. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/locations/seminole/`
- `/seminole/`
- `/st-petersburg/`
- `/medical-spa/dermal-fillers/brands/radiesse/`
- `/financing/`
- `/medical-spa/dermal-fillers/treatment-areas/`
- `/odessa/`
- `/black-friday-specials-2025/`
- `/medical-spa/dermal-fillers/brands/lip-augmentation/`
- `/medical-spa/dermal-fillers/brands/rha-fillers/`

### 11. Page has links to broken page  (non-indexable pages)

`issue:page-has-links-to-broken-page-nonindexable` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/category/med-spa/`
- `/category/blog/`
- `/?page_id=9288`
- `/testosterone-therapy/`
- `/category/injectables/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (3 pages: /category/med-spa/, /category/blog/, /category/injectables/)

3 pages on livingyoungcenter.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

## Skipped on purpose

- Indexable page not in sitemap (1): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

