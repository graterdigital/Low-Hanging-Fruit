# Work orders: 22plasticsurgery.com

Ahrefs Site Audit project 9704531 · crawl 2026-11-05 · health 97 · 36 active issue types → 14 work orders (1 decisions, 5 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Structured data has schema.org validation error | schema-fix | FLAG | 302 | 815 (top 200 of 302) | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 2 | Slow page | manual | FLAG | 117 | 113 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 3 | Slow server response for AI crawlers | hosting/cache | FLAG | 6 | 94 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 4 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 27 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 5 | H1 tag missing or empty | manual | FLAG | 7 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 6 | FAQ page missing FAQPage schema | schema-check | FLAG | 1 | 0 | client | FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing. |
| 7 | Pages fix-meta routed to homepage title | homepage title | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 8 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 9 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 10 | Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (126) | fix-social-tags | skill pending | 126 | 630 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 11 | Waiting on skill `schema-fix` (2 issue types): Organization schema missing or incomplete (1); Structured data has Google rich results validation error (1) | schema-fix | skill pending | 2 | 151 | agency | Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 12 | Waiting on skill `indexation-review` (2 issue types): Indexable page not in sitemap (39); Page in multiple sitemaps (1) | indexation-review | skill pending | 40 | 79 | agency | Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 13 | Waiting on skill `redirect-rules` (1 issue type): 3XX page receives organic traffic (1) | redirect-rules | skill pending | 1 | 18 | agency | Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 14 | Waiting on skill `fix-broken-links` (3 issue types): 404 page (1); 4XX page (1); Page has links to broken page (1) | fix-broken-links | skill pending | 3 | 0 | agency | Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Structured data has schema.org validation error

`issue:structured-data-has-schema-org-validation-error` · schema-fix · FLAG · decider: agency

Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit.

- `/` (151 traffic)
- `/video-resources/` (90 traffic)
- `/breast-augmentation-gone-wrong/` (74 traffic)
- `/gallery/` (68 traffic)
- `/is-it-normal-to-have-extra-skin-down-there-heres-what-you-should-know/` (63 traffic)
- `/doctor/dr-katherine-vandenberg/` (57 traffic)
- `/how-long-does-recovery-take-after-mtf-top-surgery/` (37 traffic)
- `/consultation-and-pre-op-prep/` (37 traffic)
- `/blog/` (29 traffic)
- `/get-a-jump-start-on-your-summer-body/` (23 traffic)
- … 292 more in Ahrefs

### 2. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/breast-augmentation-gone-wrong/` (74 traffic)
- `/what-is-male-breast-reduction-gynecomastia-surgery-and-how-does-it-work/` (16 traffic)
- `/how-to-get-rid-of-seroma-after-tummy-tuck-effective-tips-for-recovery/` (10 traffic)
- `/everything-you-need-to-know-about-neck-lift-surgery-lower-rhytidectomy/` (8 traffic)
- `/enhance-your-confidence-with-breast-augmentation-in-salt-lake-city/` (3 traffic)
- `/what-is-a-mini-tummy-tuck-understanding-mini-abdominoplasty/` (1 traffic)
- `/understanding-breast-augmentation-cost-types-recovery-and-more/` (1 traffic)
- `/gallery-category/facial-implants/?d=92`
- `/gallery-category/surgery-after-weight-loss-gallery/?d=104`
- `/gallery-category/renuvion/?d=92`
- … 107 more in Ahrefs

### 3. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/breast-augmentation-gone-wrong/` (74 traffic)
- `/how-to-get-rid-of-seroma-after-tummy-tuck-effective-tips-for-recovery/` (10 traffic)
- `/everything-you-need-to-know-about-neck-lift-surgery-lower-rhytidectomy/` (8 traffic)
- `/what-is-a-mini-tummy-tuck-understanding-mini-abdominoplasty/` (1 traffic)
- `/understanding-breast-augmentation-cost-types-recovery-and-more/` (1 traffic)
- `/how-to-prepare-for-breast-implant-removal-surgery/`

### 4. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/category/breast-reconstruction-surgery/`
- `/category/spa-md/`
- `/category/brow-lift/`
- `/category/mommy-makeover/`
- `/category/gender-confirming-top-surgery/`
- `/category/breast-augmentation/`
- `/category/surgery-after-weight-loss/`
- `/category/lower-blepharoplasty-surgery/`
- `/category/tummy-tuck/`
- `/category/liposuction/`
- … 17 more in Ahrefs

### 5. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/pre-op-visit-instructions/`
- `/insurance-pre-op-instructions/`
- `/form-test/`
- `/47976-2/`
- `/pre-op-phone-call-instructions/`
- `/preparing-for-your-virtual-consultation/`
- `/preparing-for-your-plastic-surgery-consultation/`

### 6. FAQ page missing FAQPage schema

`issue:faq-page-missing-faqpage-schema` · schema-check · FLAG · decider: client

FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing.

- `/rhinoplasty-faqs/`

### 7. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 8. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 9. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 10. Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (126)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/` (151 traffic)
- `/video-resources/` (90 traffic)
- `/breast-augmentation-gone-wrong/` (74 traffic)
- `/gallery/` (68 traffic)
- `/doctor/dr-katherine-vandenberg/` (57 traffic)
- `/consultation-and-pre-op-prep/` (37 traffic)
- `/blog/` (29 traffic)
- `/get-a-jump-start-on-your-summer-body/` (23 traffic)
- `/what-is-vaginal-rejuvenation-surgery-a-comprehensive-beginners-guide/` (18 traffic)
- `/renuvion/` (18 traffic)
- … 116 more in Ahrefs

### 11. Waiting on skill `schema-fix` (2 issue types): Organization schema missing or incomplete (1); Structured data has Google rich results validation error (1)

`pending:schema-fix` · schema-fix · skill pending · decider: agency

Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (151 traffic)
- … 1 more in Ahrefs

### 12. Waiting on skill `indexation-review` (2 issue types): Indexable page not in sitemap (39); Page in multiple sitemaps (1)

`pending:indexation-review` · indexation-review · skill pending · decider: agency

Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/doctor/dr-katherine-vandenberg/` (57 traffic)
- `/gallery-category/breast-lift/` (18 traffic)
- `/gallery-category/mommy-makeover/` (3 traffic)
- `/gallery-category/breast-augmentation-revision/` (1 traffic)
- `/gallery-category/blepharoplasty-gallery/`
- `/gallery-category/breast-reduction-gallery/`
- `/gallery-category/labiaplasty/`
- `/gallery-category/neck-lift/`
- `/gallery-category/tummy-tuck/`
- `/gallery-category/brachioplasty-gallery/`
- … 30 more in Ahrefs

### 13. Waiting on skill `redirect-rules` (1 issue type): 3XX page receives organic traffic (1)

`pending:redirect-rules` · redirect-rules · skill pending · decider: agency

Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/gallery` (18 traffic)

### 14. Waiting on skill `fix-broken-links` (3 issue types): 404 page (1); 4XX page (1); Page has links to broken page (1)

`pending:fix-broken-links` · fix-broken-links · skill pending · decider: agency

Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/artas-hair-restoration/`
- … 2 more in Ahrefs

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (27 pages: /category/breast-reconstruction-surgery/, /category/spa-md/, /category/brow-lift/, /category/mommy-makeover/, …)

27 pages on 22plasticsurgery.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

