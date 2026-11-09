# Work orders: 22spamd.com

Ahrefs Site Audit project 9704527 · crawl 2026-11-05 · health 99 · 22 active issue types → 8 work orders (0 decisions, 4 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Indexable page not in sitemap | indexation-review | APPROVE (skill pending) | 67 | 100 | agency | Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 2 | Page has nofollow outgoing internal links | nofollow-audit | APPROVE (skill pending) | 67 | 100 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 3 | H1 tag missing or empty | manual | FLAG | 17 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 4 | Pages fix-meta routed to [] | [] | FLAG | 4 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 5 | Slow page | manual | FLAG | 2 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 6 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 7 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 1 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 8 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 7 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |

## Per item

### 1. Indexable page not in sitemap

`issue:indexable-page-not-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

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

### 2. Page has nofollow outgoing internal links

`issue:page-has-nofollow-outgoing-internal-links` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

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

### 3. H1 tag missing or empty

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

### 4. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`
- `noindex`
- `non-200`
- `homepage title`

### 5. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/blog/`
- `/people/makayley-riding/`

### 6. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/financing/`

### 7. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/blog/2/`

### 8. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/blog/`
- `/privacy-policy/`
- `/financing/`
- `/good-faith-estimate/`
- `/financial-policies/`
- `/contact/`
- `/terms-of-use/`

