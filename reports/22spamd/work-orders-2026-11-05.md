# Work orders: 22spamd.com

Ahrefs Site Audit project 9704527 · crawl 2026-11-05 · health 99 · 22 active issue types → 9 work orders (0 decisions, 3 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | H1 tag missing or empty | manual | FLAG | 17 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 2 | Slow page | manual | FLAG | 2 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 3 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 4 | Pages fix-meta routed to homepage title | homepage title | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 5 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 6 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 7 | Waiting on skill `nofollow-audit` (2 issue types): Page has nofollow outgoing internal links (67); Page has nofollow outgoing internal links  (non-indexable pages) (1) | nofollow-audit | skill pending | 68 | 100 | agency | Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 8 | Waiting on skill `indexation-review` (1 issue type): Indexable page not in sitemap (67) | indexation-review | skill pending | 67 | 100 | agency | Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 9 | Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (7) | fix-social-tags | skill pending | 7 | 0 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |

## Per item

### 1. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/people/lola-ramirez/`
- `/people/jamie-mcdonald/`
- `/people/hailey-brazier/`
- `/people/sumer-christensen/`
- `/people/brandi-salway/`
- `/people/kelsee-hyde/`
- `/people/mari-english/`
- `/people/jamie-johnson/`
- `/people/masha-melnik/`
- `/people/allie-sweat/`
- … 7 more in Ahrefs

### 2. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/blog/`
- `/people/makayley-riding/`

### 3. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/financing/`

### 4. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 5. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 6. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 7. Waiting on skill `nofollow-audit` (2 issue types): Page has nofollow outgoing internal links (67); Page has nofollow outgoing internal links  (non-indexable pages) (1)

`pending:nofollow-audit` · nofollow-audit · skill pending · decider: agency

Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/` (91 traffic)
- `/service/pixel-laser-skin-resurfacing/` (6 traffic)
- `/about-us/` (1 traffic)
- `/service/dermaplaning/` (1 traffic)
- `/membership/` (1 traffic)
- `/service/pixel-precision-skin-renewal/`
- `/people/lola-ramirez/`
- `/service/coolsculpting-elite/`
- `/high-tech-beauty-suite/`
- `/people/jamie-mcdonald/`
- … 58 more in Ahrefs

### 8. Waiting on skill `indexation-review` (1 issue type): Indexable page not in sitemap (67)

`pending:indexation-review` · indexation-review · skill pending · decider: agency

Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/` (91 traffic)
- `/service/pixel-laser-skin-resurfacing/` (6 traffic)
- `/about-us/` (1 traffic)
- `/service/dermaplaning/` (1 traffic)
- `/membership/` (1 traffic)
- `/service/pixel-precision-skin-renewal/`
- `/people/lola-ramirez/`
- `/service/coolsculpting-elite/`
- `/high-tech-beauty-suite/`
- `/people/jamie-mcdonald/`
- … 57 more in Ahrefs

### 9. Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (7)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/blog/`
- `/privacy-policy/`
- `/financing/`
- `/good-faith-estimate/`
- `/financial-policies/`
- `/contact/`
- `/terms-of-use/`

