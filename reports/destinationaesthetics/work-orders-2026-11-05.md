# Work orders: destinationaesthetics.com

Ahrefs Site Audit project 9704522 · crawl 2026-11-05 · health 97 · 37 active issue types → 12 work orders (1 decisions, 4 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Slow page | manual | FLAG | 34 | 204 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 2 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 133 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 3 | H1 tag missing or empty | manual | FLAG | 7 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 4 | FAQ page missing FAQPage schema | schema-check | FLAG | 2 | 0 | client | FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing. |
| 5 | Pages fix-meta routed to homepage title | homepage title | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 6 | Multiple title tags | manual | FLAG | 1 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 7 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 8 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 9 | Waiting on skill `schema-fix` (1 issue type): Organization schema missing or incomplete (1) | schema-fix | skill pending | 1 | 563 | agency | Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 10 | Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (45) | fix-social-tags | skill pending | 45 | 486 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 11 | Waiting on skill `fix-broken-links` (3 issue types): 404 page (7); 4XX page (7); Page has links to broken page (10) | fix-broken-links | skill pending | 24 | 0 | agency | Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 12 | Waiting on skill `redirect-rules` (1 issue type): 3XX redirect in sitemap (1) | redirect-rules | skill pending | 1 | 0 | agency | Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |

## Per item

### 1. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/location/elk-grove/` (87 traffic)
- `/services/skin/microneedling/` (73 traffic)
- `/services/` (24 traffic)
- `/services/body/coolsculpting-elite/` (20 traffic)
- `/location/el-dorado-hills/page/4/`
- `/location/napa/page/3/`
- `/location/folsom/page/3/`
- `/service/page/2/`
- `/services/face/skinvive-by-juvederm/`
- `/gallery/case-66/`
- … 24 more in Ahrefs

### 2. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/gallery/case-184/`
- `/gallery/case-224/`
- `/about/our-team/joanna-c/`
- `/gallery/case-192/`
- `/about/our-team/terra-k/`
- `/about/our-team/shawna-c/`
- `/gallery/case-75/`
- `/gallery/case-120/`
- `/about/our-team/ian-c/`
- `/about/our-team/isabella-m/`
- … 123 more in Ahrefs

### 3. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/service/page/2/`
- `/service/`
- `/good-faith-estimate/`
- `/service/page/4/`
- `/additional-california-privacy-disclosures/`
- `/service/page/3/`
- `/privacy-policy/`

### 4. FAQ page missing FAQPage schema

`issue:faq-page-missing-faqpage-schema` · schema-check · FLAG · decider: client

FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing.

- `/blog/chin-and-jawline-fillers-questions-answers/`
- `/blog/faq-what-are-the-differences-between-different-juvederm-fillers/`

### 5. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `/`

### 6. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/financing/`

### 7. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 8. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 9. Waiting on skill `schema-fix` (1 issue type): Organization schema missing or incomplete (1)

`pending:schema-fix` · schema-fix · skill pending · decider: agency

Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (563 traffic)

### 10. Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (45)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/location/sacramento/` (133 traffic)
- `/location/roseville/` (102 traffic)
- `/location/elk-grove/` (87 traffic)
- `/location/el-dorado-hills/` (64 traffic)
- `/location/folsom/` (27 traffic)
- `/services/` (24 traffic)
- `/location/napa/` (19 traffic)
- `/about/reviews/` (16 traffic)
- `/about/dadifference/` (11 traffic)
- `/choose-a-location/` (3 traffic)
- … 35 more in Ahrefs

### 11. Waiting on skill `fix-broken-links` (3 issue types): 404 page (7); 4XX page (7); Page has links to broken page (10)

`pending:fix-broken-links` · fix-broken-links · skill pending · decider: agency

Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/collections/moisturize-hydrate`
- `/contact-us/`
- `/search?q=retinoin`
- `/search?q=retinoin&options%5Bprefix%5D=last`
- `/collections/cleanse-exfoliate`
- `/cosmetic-laser/`
- `/payment-plans/`
- … 17 more in Ahrefs

### 12. Waiting on skill `redirect-rules` (1 issue type): 3XX redirect in sitemap (1)

`pending:redirect-rules` · redirect-rules · skill pending · decider: agency

Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/about/procedure-financing/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (133 pages: /gallery/case-184/, /gallery/case-224/, /about/our-team/joanna-c/, /gallery/case-192/, …)

133 pages on destinationaesthetics.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

## Skipped on purpose

- Indexable page not in sitemap (24): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

