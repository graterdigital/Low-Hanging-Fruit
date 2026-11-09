# Work orders: legalatlanta.com

Ahrefs Site Audit project 9704534 · crawl 2026-11-05 · health 85 · 32 active issue types → 11 work orders (1 decisions, 3 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Structured data has schema.org validation error | schema-fix | FLAG | 150 | 197 | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 2 | Slow page | manual | FLAG | 72 | 40 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 3 | Slow server response for AI crawlers | hosting/cache | FLAG | 12 | 27 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 4 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 23 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 5 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 1 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 6 | Pages fix-meta routed to homepage title | homepage title | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 7 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 8 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 9 | Waiting on skill `fix-broken-links` (4 issue types): Page has links to broken page (161); 404 page (1); 4XX page (1); Page has links to broken page  (non-indexable pages) (12) | fix-broken-links | skill pending | 175 | 1468 | agency | Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 10 | Waiting on skill `fix-social-tags` (2 issue types): X (Twitter) card missing (2); Open Graph tags incomplete (5) | fix-social-tags | skill pending | 7 | 203 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 11 | Waiting on skill `indexation-review` (1 issue type): Indexable page not in sitemap (5) | indexation-review | skill pending | 5 | 0 | agency | Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |

## Per item

### 1. Structured data has schema.org validation error

`issue:structured-data-has-schema-org-validation-error` · schema-fix · FLAG · decider: agency

Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit.

- `/crucial-differences-between-debt-settlement-and-bankruptcy/` (50 traffic)
- `/how-much-are-repossession-fees-in-georgia/` (47 traffic)
- `/what-happens-if-your-car-gets-repossessed/` (21 traffic)
- `/what-your-auto-liability-insurance-really-covers/` (13 traffic)
- `/georgia-foreclosure-process-timeline-procedure/` (11 traffic)
- `/how-to-pass-the-means-test-for-chapter-7-bankruptcy/` (11 traffic)
- `/georgia-hb-1024-what-the-new-bankruptcy-exemption-law-means-for-homeowners-in-2026/` (10 traffic)
- `/mobile-chiropractic-care-that-keeps-recovery-on-track/` (7 traffic)
- `/is-jaywalking-illegal-in-georgia/` (7 traffic)
- `/minimal-damage-crash-risks/` (4 traffic)
- … 140 more in Ahrefs

### 2. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/how-to-pass-the-means-test-for-chapter-7-bankruptcy/` (11 traffic)
- `/gainesville-dog-bite-lawyer/` (8 traffic)
- `/mobile-chiropractic-care-that-keeps-recovery-on-track/` (7 traffic)
- `/athens-car-accident-lawyer/` (7 traffic)
- `/who-is-at-fault-in-a-sideswipe-accident/` (3 traffic)
- `/contact/morrow/` (2 traffic)
- `/how-to-file-for-chapter-7-bankruptcy/` (1 traffic)
- `/gainesville-motorcycle-accident-lawyer/` (1 traffic)
- `/morrow-dui-accident-lawyer/`
- `/blog/page/17/`
- … 62 more in Ahrefs

### 3. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/how-to-pass-the-means-test-for-chapter-7-bankruptcy/` (11 traffic)
- `/gainesville-dog-bite-lawyer/` (8 traffic)
- `/athens-car-accident-lawyer/` (7 traffic)
- `/gainesville-motorcycle-accident-lawyer/` (1 traffic)
- `/spouse-declares-bankruptcy-in-georgia/`
- `/emotional-distress-compensation-in-georgia/`
- `/gainesville-uber-accident-lawyer/`
- `/is-bankruptcy-public-record-in-georgia/`
- `/morrow-car-accident-lawyer/`
- `/bankruptcy/chapter-13/conyers-chapter-13/`
- … 2 more in Ahrefs

### 4. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/category/personal-injury/page/3/`
- `/category/bankruptcy/page/4/`
- `/category/uncategorized/page/3/`
- `/category/other/page/3/`
- `/category/bankruptcy/`
- `/category/other/`
- `/category/other/page/2/`
- `/category/wrongful-death/`
- `/category/personal-injury/page/6/`
- `/thank-you/`
- … 13 more in Ahrefs

### 5. H1 tag missing or empty  (non-indexable pages)

`issue:h1-tag-missing-or-empty-nonindexable` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/thank-you/`

### 6. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 7. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 8. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 9. Waiting on skill `fix-broken-links` (4 issue types): Page has links to broken page (161); 404 page (1); 4XX page (1); Page has links to broken page  (non-indexable pages) (12)

`pending:fix-broken-links` · fix-broken-links · skill pending · decider: agency

Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/chapter-13-calculator/` (407 traffic)
- `/athens-truck-accident-lawyer/` (225 traffic)
- `/personal-injury/sr13-form/` (106 traffic)
- `/bankruptcy/chapter-7/` (80 traffic)
- `/buford-personal-injury-lawyers/` (80 traffic)
- `/personal-injury/georgia-car-accident-lawyer/` (60 traffic)
- `/bankruptcy/chapter-13/` (58 traffic)
- `/duluth-personal-injury-lawyer/` (49 traffic)
- `/athens-dog-bite-lawyer/` (44 traffic)
- `/bankruptcy/` (44 traffic)
- … 165 more in Ahrefs

### 10. Waiting on skill `fix-social-tags` (2 issue types): X (Twitter) card missing (2); Open Graph tags incomplete (5)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/` (203 traffic)
- `/resources/`
- … 5 more in Ahrefs

### 11. Waiting on skill `indexation-review` (1 issue type): Indexable page not in sitemap (5)

`pending:indexation-review` · indexation-review · skill pending · decider: agency

Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/personal-injury/georgia-sb68-tort-reform/`
- `/personal-injury/catastrophic-injury-attorney/`
- `/personal-injury/atlanta-hit-and-run-attorney/`
- `/personal-injury/atlanta-workers-compensation-attorneys/`
- `/personal-injury/tuck-accident-attorney/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (23 pages: /category/personal-injury/page/3/, /category/bankruptcy/page/4/, /category/uncategorized/page/3/, /category/other/page/3/, …)

23 pages on legalatlanta.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

