# Work orders: everbody.com

Ahrefs Site Audit project 9704532 · crawl 2026-11-05 · health 99 · 21 active issue types → 10 work orders (1 decisions, 3 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | FAQ page missing FAQPage schema | schema-check | FLAG | 1 | 2 | client | FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing. |
| 2 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 11 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 3 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 11 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 4 | H1 tag missing or empty | manual | FLAG | 1 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 5 | Pages fix-meta routed to homepage title | homepage title | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 6 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 7 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 8 | Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (26) | fix-social-tags | skill pending | 26 | 1165 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 9 | Waiting on skill `redirect-rules` (1 issue type): 3XX page receives organic traffic (1) | redirect-rules | skill pending | 1 | 2 | agency | Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 10 | Waiting on skill `indexation-review` (1 issue type): Indexable page not in sitemap (1) | indexation-review | skill pending | 1 | 0 | agency | Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |

## Per item

### 1. FAQ page missing FAQPage schema

`issue:faq-page-missing-faqpage-schema` · schema-check · FLAG · decider: client

FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing.

- `/faq/` (2 traffic)

### 2. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/area/connecticut/`
- `/area/texas/`
- `/treatment-category/facials/`
- `/treatment-category/lasers-light/`
- `/treatment-category/body/`
- `/area/maryland/`
- `/area/new-york-city/`
- `/treatment-category/hair/`
- `/treatment-category/peels/`
- `/treatment-category/injectables/`
- … 1 more in Ahrefs

### 3. H1 tag missing or empty  (non-indexable pages)

`issue:h1-tag-missing-or-empty-nonindexable` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/area/connecticut/`
- `/area/texas/`
- `/treatment-category/facials/`
- `/treatment-category/lasers-light/`
- `/treatment-category/body/`
- `/area/maryland/`
- `/area/new-york-city/`
- `/treatment-category/hair/`
- `/treatment-category/peels/`
- `/treatment-category/injectables/`
- … 1 more in Ahrefs

### 4. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/model-release/`

### 5. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 6. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 7. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 8. Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (26)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/` (1061 traffic)
- `/locations/` (59 traffic)
- `/treatment/` (33 traffic)
- `/locations/greenwich-village/` (4 traffic)
- `/providers/` (3 traffic)
- `/locations/south-windsor/` (2 traffic)
- `/faq/` (2 traffic)
- `/financing/` (1 traffic)
- `/press/`
- `/locations/gaithersburg/`
- … 16 more in Ahrefs

### 9. Waiting on skill `redirect-rules` (1 issue type): 3XX page receives organic traffic (1)

`pending:redirect-rules` · redirect-rules · skill pending · decider: agency

Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/locations` (2 traffic)

### 10. Waiting on skill `indexation-review` (1 issue type): Indexable page not in sitemap (1)

`pending:indexation-review` · indexation-review · skill pending · decider: agency

Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/press/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (11 pages: /area/connecticut/, /area/texas/, /treatment-category/facials/, /treatment-category/lasers-light/, …)

11 pages on everbody.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

