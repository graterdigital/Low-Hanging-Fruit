# Work orders: glomedspa.com

Ahrefs Site Audit project 9704537 · crawl 2026-11-05 · health 96 · 35 active issue types → 12 work orders (1 decisions, 3 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | H1 tag missing or empty | manual | FLAG | 13 | 3 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 2 | Slow page | manual | FLAG | 5 | 1 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 3 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 6 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex page. |
| 4 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 6 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 5 | FAQ page missing FAQPage schema | schema-check | FLAG | 1 | 0 | client | FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing. |
| 6 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 7 | Pages fix-meta routed to homepage title | homepage title | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 8 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 9 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 10 | Waiting on skill `fix-social-tags` (2 issue types): Open Graph tags missing (10); X (Twitter) card missing (10) | fix-social-tags | skill pending | 20 | 0 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 11 | Waiting on skill `nofollow-audit` (2 issue types): Page has nofollow incoming internal links only  (non-indexable pages) (4); Page has nofollow outgoing internal links  (non-indexable pages) (6) | nofollow-audit | skill pending | 10 | 0 | agency | Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: find what adds rel=nofollow to internal links (theme, plugin, editor habit); if systematic, one fix clears thousands (ruggeddepot 8k, miuraboiler 3k) |
| 12 | Waiting on skill `indexation-review` (2 issue types): Indexable page not in sitemap (2); Sitemap in the wrong format (1) | indexation-review | skill pending | 3 | 0 | agency | Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |

## Per item

### 1. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/contact-us/` (2 traffic)
- `/resurfx/` (1 traffic)
- `/category/injectables/`
- `/author/infoeagleeyemarketinginc-com/`
- `/category/skin/`
- `/category/pdo-threads/`
- `/category/blog/`
- `/category/dlm-faq/`
- `/pdo-threads/`
- `/category/chemical-peels/`
- … 3 more in Ahrefs

### 2. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/resurfx/` (1 traffic)
- `/kybella/`
- `/neurotoxins/`
- `/smoothglo/`
- `/semaglutide-weight-loss/`

### 3. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex page.

- `/author/infoeagleeyemarketinginc-com/page/3/`
- `/category/blog/page/3/`
- `/author/infoeagleeyemarketinginc-com/page/2/`
- `/author/infoeagleeyemarketinginc-com/page/5/`
- `/category/blog/page/2/`
- `/author/infoeagleeyemarketinginc-com/page/4/`

### 4. H1 tag missing or empty  (non-indexable pages)

`issue:h1-tag-missing-or-empty-nonindexable` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/author/infoeagleeyemarketinginc-com/page/3/`
- `/category/blog/page/3/`
- `/author/infoeagleeyemarketinginc-com/page/2/`
- `/author/infoeagleeyemarketinginc-com/page/5/`
- `/category/blog/page/2/`
- `/author/infoeagleeyemarketinginc-com/page/4/`

### 5. FAQ page missing FAQPage schema

`issue:faq-page-missing-faqpage-schema` · schema-check · FLAG · decider: client

FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing.

- `/answers-to-common-questions-about-skinvive-by-juvederm/`

### 6. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/financing/`

### 7. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 8. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 9. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 10. Waiting on skill `fix-social-tags` (2 issue types): Open Graph tags missing (10); X (Twitter) card missing (10)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/category/injectables/`
- `/author/infoeagleeyemarketinginc-com/`
- `/category/skin/`
- `/category/pdo-threads/`
- `/category/blog/`
- `/category/dlm-faq/`
- `/category/chemical-peels/`
- `/author/devgraterdigital-com/`
- `/category/lasers/`
- `/category/microneedling/`
- … 10 more in Ahrefs

### 11. Waiting on skill `nofollow-audit` (2 issue types): Page has nofollow incoming internal links only  (non-indexable pages) (4); Page has nofollow outgoing internal links  (non-indexable pages) (6)

`pending:nofollow-audit` · nofollow-audit · skill pending · decider: agency

Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: find what adds rel=nofollow to internal links (theme, plugin, editor habit); if systematic, one fix clears thousands (ruggeddepot 8k, miuraboiler 3k)

- `/author/infoeagleeyemarketinginc-com/page/3/`
- `/category/blog/page/3/`
- `/author/infoeagleeyemarketinginc-com/page/5/`
- `/author/infoeagleeyemarketinginc-com/page/4/`
- … 6 more in Ahrefs

### 12. Waiting on skill `indexation-review` (2 issue types): Indexable page not in sitemap (2); Sitemap in the wrong format (1)

`pending:indexation-review` · indexation-review · skill pending · decider: agency

Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/author/infoeagleeyemarketinginc-com/`
- `/author/devgraterdigital-com/`
- … 1 more in Ahrefs

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (6 pages: /author/infoeagleeyemarketinginc-com/page/3/, /category/blog/page/3/, /author/infoeagleeyemarketinginc-com/page/2/, /author/infoeagleeyemarketinginc-com/page/5/, …)

6 pages on glomedspa.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

