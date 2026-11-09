# Work orders: livingyoungcenter.com

Ahrefs Site Audit project 9704535 · crawl 2026-11-05 · health 48 · 34 active issue types → 9 work orders (1 decisions, 3 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 3 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 2 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 3 | Slow page | manual | FLAG | 1 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 4 | Pages fix-meta routed to homepage title | homepage title | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 5 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 6 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 7 | Waiting on skill `fix-broken-links` (4 issue types): Page has links to broken page (91); 404 page (10); 4XX page (10); Page has links to broken page  (non-indexable pages) (5) | fix-broken-links | skill pending | 116 | 580 | agency | Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 8 | Waiting on skill `redirect-rules` (2 issue types): Canonical points to redirect (2); 3XX redirect in sitemap (3) | redirect-rules | skill pending | 5 | 0 | agency | Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 9 | Waiting on skill `indexation-review` (1 issue type): Non-canonical page in sitemap (1) | indexation-review | skill pending | 1 | 0 | agency | Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |

## Per item

### 1. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/category/med-spa/`
- `/category/blog/`
- `/category/injectables/`

### 2. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/resources/financing/`

### 3. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/blog/hrt-women-tampa-bay-guide/`

### 4. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 5. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 6. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 7. Waiting on skill `fix-broken-links` (4 issue types): Page has links to broken page (91); 404 page (10); 4XX page (10); Page has links to broken page  (non-indexable pages) (5)

`pending:fix-broken-links` · fix-broken-links · skill pending · decider: agency

Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

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
- … 106 more in Ahrefs

### 8. Waiting on skill `redirect-rules` (2 issue types): Canonical points to redirect (2); 3XX redirect in sitemap (3)

`pending:redirect-rules` · redirect-rules · skill pending · decider: agency

Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/?page_id=9288`
- `/testosterone-therapy/`
- … 3 more in Ahrefs

### 9. Waiting on skill `indexation-review` (1 issue type): Non-canonical page in sitemap (1)

`pending:indexation-review` · indexation-review · skill pending · decider: agency

Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/testosterone-therapy/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (3 pages: /category/med-spa/, /category/blog/, /category/injectables/)

3 pages on livingyoungcenter.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

## Skipped on purpose

- Indexable page not in sitemap (1): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

