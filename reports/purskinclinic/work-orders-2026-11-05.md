# Work orders: purskinclinic.com

Ahrefs Site Audit project 9704546 · crawl 2026-11-05 · health 92 · 5 active issue types → 4 work orders (0 decisions, 3 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | HTTPS to HTTP redirect | redirect-rules | APPROVE (skill pending) | 2 | 316 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 2 | 3XX page receives organic traffic | redirect-rules | APPROVE (skill pending) | 1 | 316 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 3 | Indexable page became non-indexable | indexation-review | APPROVE (skill pending) | 1 | 316 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 4 | Pages fix-meta routed to [] | [] | FLAG | 4 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |

## Per item

### 1. HTTPS to HTTP redirect

`issue:https-to-http-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/` (316 traffic)
- `/robots.txt`

### 2. 3XX page receives organic traffic

`issue:3xx-page-receives-organic-traffic` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/` (316 traffic)

### 3. Indexable page became non-indexable

`issue:indexable-page-became-non-indexable` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/` (316 traffic)

### 4. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`
- `noindex`
- `non-200`
- `homepage title`

