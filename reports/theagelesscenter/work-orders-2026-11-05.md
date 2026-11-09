# Work orders: theagelesscenter.com

Ahrefs Site Audit project 9704555 · crawl 2026-11-05 · health 98 · 31 active issue types → 9 work orders (1 decisions, 3 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | X (Twitter) card missing | fix-social-tags | AUTO (skill pending) | 14 | 96 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 2 | Slow page | manual | FLAG | 10 | 35 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 3 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 24 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page. |
| 4 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 18 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 5 | Pages fix-meta routed to [] | [] | FLAG | 4 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 6 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 7 | Structured data has schema.org validation error | schema-fix | FLAG | 1 | 0 | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 8 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 5 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 9 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 2 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |

## Per item

### 1. X (Twitter) card missing

`issue:x-twitter-card-missing` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/` (96 traffic)
- `/blog/page/3/`
- `/blog/page/7/`
- `/blog/page/5/`
- `/special-juvederm-affordable-2/`
- `/blog/page/6/`
- `/atlanta-cosmetic-filler-promotions/`
- `/affordable-juvederm-promotion/`
- `/blog/page/2/`
- `/blog/`
- … 4 more in Ahrefs

### 2. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/blog/can-you-treat-laugh-lines-with-botox/` (34 traffic)
- `/contact-us/` (1 traffic)
- `/atlanta-botox-promotion/`
- `/galleries/`
- `/blog/fda-approved-atlanta-botox-services-for-a-youthful-appearance/`
- `/blog/page/7/`
- `/category/xeomin/`
- `/blog/regain-your-radiance-with-radiesse/`
- `/blog/page/2/`
- `/category/skin-care/`

### 3. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page.

- `/shipping-policy/`
- `/terms-and-conditions/`
- `/privacy-policy/`
- `/return-policy/`
- `/gfe/`
- `/galleries/`
- `/category/featured/`
- `/category/botox/page/2/`
- `/category/uncategorized/page/3/`
- `/category/skin-treatments/`
- … 14 more in Ahrefs

### 4. H1 tag missing or empty  (non-indexable pages)

`issue:h1-tag-missing-or-empty-nonindexable` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/category/featured/`
- `/category/botox/page/2/`
- `/category/uncategorized/page/3/`
- `/category/skin-treatments/`
- `/category/xeomin/`
- `/category/facial-rejuvenation/`
- `/category/services/`
- `/category/dermal-fillers/page/2/`
- `/category/radiesse/`
- `/category/uncategorized/`
- … 8 more in Ahrefs

### 5. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`
- `noindex`
- `non-200`
- `homepage title`

### 6. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/financing/`

### 7. Structured data has schema.org validation error

`issue:structured-data-has-schema-org-validation-error` · schema-fix · FLAG · decider: agency

Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit.

- `/what-our-patients-say/`

### 8. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/shipping-policy/`
- `/terms-and-conditions/`
- `/privacy-policy/`
- `/return-policy/`
- `/gfe/`

### 9. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/current-specials/`
- `/checkout/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (24 pages: /shipping-policy/, /terms-and-conditions/, /privacy-policy/, /return-policy/, …)

24 pages on theagelesscenter.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

## Skipped on purpose

- Indexable page not in sitemap (7): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

