# Work orders: atlantaspecializedcare.com

Ahrefs Site Audit project 9704530 · crawl 2026-11-05 · health 90 · 40 active issue types → 16 work orders (4 decisions, 5 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Orphan page (has no incoming internal links) | indexation-review | decide | 5 | 11 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 2 | Links to redirect, skipped by fix-redirect-links: redirects to homepage | redirect-rules | decide | 2 | 0 | client | Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order. |
| 3 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 1 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex page. |
| 4 | Robots.txt rules disallow to crawl | indexation-review | decide | 1 | 0 | client | robots.txt blocks pages Ahrefs found linked: confirm the block is intended (admin, cart, search) or lift it. |
| 5 | CSS file size too large | manual | FLAG | 5 | 0 | agency | Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket. |
| 6 | Links to redirect, skipped by fix-redirect-links: pagination /page/1/ comes from the theme template, not content | manual | FLAG | 5 | 0 | agency | Theme template edit: emit the archive root for page 1 (WordPress paginate_links does by default). Diff by hand. |
| 7 | FAQ page missing FAQPage schema | schema-check | FLAG | 2 | 0 | client | FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing. |
| 8 | H1 tag missing or empty | manual | FLAG | 1 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 9 | Pages fix-meta routed to homepage title | homepage title | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 10 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 11 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 12 | Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (88) | fix-social-tags | skill pending | 88 | 433 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 13 | Waiting on skill `fix-broken-links` (3 issue types): Page has links to broken page (8); 404 page (8); 4XX page (8) | fix-broken-links | skill pending | 24 | 118 | agency | Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 14 | Waiting on skill `schema-fix` (1 issue type): Organization schema missing or incomplete (1) | schema-fix | skill pending | 1 | 6 | agency | Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 15 | Waiting on skill `indexation-review` (1 issue type): 4XX page in sitemap (3) | indexation-review | skill pending | 3 | 0 | agency | Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 16 | Waiting on skill `nofollow-audit` (1 issue type): Page has nofollow outgoing internal links  (non-indexable pages) (1) | nofollow-audit | skill pending | 1 | 0 | agency | Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |

## Per item

### 1. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/team/erin-mills/` (11 traffic)
- `/team/delaney-banzhof/`
- `/thank-you-appointment/`
- `/thank-you-contact/`
- `/therapy-no-insurance/`

### 2. Links to redirect, skipped by fix-redirect-links: redirects to homepage

`redirect-links:redirects-to-homepage` · redirect-rules · decide · decider: client · source: redirect-map-2026-10-29.json

Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order.

- `/workplace-consultation/` (1 links)
- `/therapies/workplace-consultation/` (1 links)

### 3. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex page.

- `/privacy-policy/`

### 4. Robots.txt rules disallow to crawl

`issue:robots-txt-rules-disallow-to-crawl` · indexation-review · decide · decider: client

robots.txt blocks pages Ahrefs found linked: confirm the block is intended (admin, cart, search) or lift it.

- `/robots.txt`

### 5. CSS file size too large

`issue:css-file-size-too-large` · manual · FLAG · decider: agency

Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket.

- `/wp-content/cache/min/1/wp-content/plugins/business-reviews-bundle/assets/2.1.1/css/public-main.css?ver=1793289595`
- `/wp-content/cache/min/1/wp-content/plugins/gravityforms/assets/css/dist/gravity-forms-theme-framework.min.css?ver=1793290068`
- `/wp-content/cache/min/1/wp-includes/css/dashicons.min.css?ver=1793289595`
- `/wp-content/cache/min/1/wp-content/themes/atlantaspecializedcare/assets/css/custom.css?ver=1793289595`
- `/wp-content/cache/min/1/wp-content/themes/atlantaspecializedcare/assets/css/foundation.css?ver=1793289595`

### 6. Links to redirect, skipped by fix-redirect-links: pagination /page/1/ comes from the theme template, not content

`redirect-links:pagination-page-1-comes-from-the-theme-t` · manual · FLAG · decider: agency · source: redirect-map-2026-10-29.json

Theme template edit: emit the archive root for page 1 (WordPress paginate_links does by default). Diff by hand.

- `/blog/page/1/` (8 links)
- `/category/counseling/page/1/` (2 links)
- `/category/mental-health/page/1/` (1 links)
- `/category/depression/page/1/` (1 links)
- `/category/anxiety/page/1/` (1 links)

### 7. FAQ page missing FAQPage schema

`issue:faq-page-missing-faqpage-schema` · schema-check · FLAG · decider: client

FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing.

- `/cache/`
- `/payment-and-insurance-information/`

### 8. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/rapid-access-assessments/`

### 9. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 10. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 11. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 12. Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (88)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/therapies/erp-therapy/` (113 traffic)
- `/our-expertise/neurodiversity/autism/` (111 traffic)
- `/therapies/grief-counseling/` (60 traffic)
- `/our-expertise/executive-functioning/` (39 traffic)
- `/blog/page/7/` (21 traffic)
- `/therapies/group-therapy/` (18 traffic)
- `/therapies/cbt-therapy/` (14 traffic)
- `/therapies/chronic-illness-acquired-disability/` (13 traffic)
- `/therapies/psychodynamic-therapy/` (9 traffic)
- `/home/mental-health-superbill/` (9 traffic)
- … 78 more in Ahrefs

### 13. Waiting on skill `fix-broken-links` (3 issue types): Page has links to broken page (8); 404 page (8); 4XX page (8)

`pending:fix-broken-links` · fix-broken-links · skill pending · decider: agency

Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/our-expertise/neurodiversity/autism/` (111 traffic)
- `/` (6 traffic)
- `/therapies/dbt-therapy/` (1 traffic)
- `/teen-mental-health-expert-help-in-atlanta/`
- `/therapies/lgbtq-counseling/`
- `/our-expertise/neurodiversity/adhd/`
- `/confronting-unresolved-issues-from-your-past-midlife-is-a-natural-time-of-reflection/`
- `/our-expertise/`
- … 16 more in Ahrefs

### 14. Waiting on skill `schema-fix` (1 issue type): Organization schema missing or incomplete (1)

`pending:schema-fix` · schema-fix · skill pending · decider: agency

Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (6 traffic)

### 15. Waiting on skill `indexation-review` (1 issue type): 4XX page in sitemap (3)

`pending:indexation-review` · indexation-review · skill pending · decider: agency

Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/author/graterdev/`
- `/author/joegraterdigital-com/`
- `/author/tatelyninteractivesearchmarketing-com/`

### 16. Waiting on skill `nofollow-audit` (1 issue type): Page has nofollow outgoing internal links  (non-indexable pages) (1)

`pending:nofollow-audit` · nofollow-audit · skill pending · decider: agency

Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/privacy-policy/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Orphan page (has no incoming internal links)** (5 pages: /team/erin-mills/, /team/delaney-banzhof/, /thank-you-appointment/, /thank-you-contact/, …)

5 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Links to redirect, skipped by fix-redirect-links: redirects to homepage** (2 pages: /workplace-consultation/, /therapies/workplace-consultation/)

2 old URLs on atlantaspecializedcare.com currently redirect to the homepage, which loses visitors who click an old link. For each one we need the page it should go to now (or confirmation that nothing replaces it, in which case we remove the links).

**Pages hidden from Google (noindex/nofollow): confirm intent** (1 page: /privacy-policy/)

1 page on atlantaspecializedcare.com is set so Google does not index it (or does not follow its links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

**Robots.txt rules disallow to crawl** (1 page: /robots.txt)

Atlanta Specialized Care: robots.txt blocks pages Ahrefs found linked: confirm the block is intended (admin, cart, search) or lift it. (1 page affected.) Our recommendation is in the sheet; reply with your call and we will do the rest.

## Skipped on purpose

- Indexable page not in sitemap (13): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

