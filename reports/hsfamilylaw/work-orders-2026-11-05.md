# Work orders: hsfamilylaw.com

Ahrefs Site Audit project 9704538 · crawl 2026-11-05 · health 97 · 27 active issue types → 10 work orders (3 decisions, 2 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Structured data has schema.org validation error | schema-fix | FLAG | 43 | 335 | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 2 | Organization schema missing or incomplete | schema-fix | APPROVE (skill pending) | 1 | 164 | agency | Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 3 | Links to redirect, skipped by fix-redirect-links: redirects to homepage | redirect-rules | decide | 4 | 0 | client | Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order. |
| 4 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 3 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page. |
| 5 | Links to redirect, skipped by fix-redirect-links: redirects off-site to forwardfacing.com | manual | decide | 1 | 0 | client | Confirm the off-site redirect is meant; if yes, nothing to do. |
| 6 | Links to redirect, skipped by fix-redirect-links: pagination /page/1/ comes from the theme template, not content | manual | FLAG | 7 | 0 | agency | Theme template edit: emit the archive root for page 1 (WordPress paginate_links does by default). Diff by hand. |
| 7 | Main content requires JavaScript rendering | theme/plugin (by hand) | FLAG | 1 | 0 | agency | Find the widget rendering the main copy client-side (reviews/feed plugin) and give it server-side output or fallback text. |
| 8 | Links to redirect, skipped by fix-redirect-links: author archive | indexation-review | APPROVE | 5 | 0 | agency | Yoast > Search Appearance > Archives: disable author archives (or the author sitemap); one setting removes them all. |
| 9 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 2 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 10 | Links to redirect, skipped by fix-redirect-links: looks like a pasted file path (one post's broken image) | fix-images | APPROVE | 1 | 0 | agency | Re-upload the post's image to the media library and replace the src by hand (fix-images lists it as a broken/redirected image). |

## Per item

### 1. Structured data has schema.org validation error

`issue:structured-data-has-schema-org-validation-error` · schema-fix · FLAG · decider: agency

Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit.

- `/` (164 traffic)
- `/divorce/property-debt-division/` (50 traffic)
- `/family-law/separation-agreements/` (46 traffic)
- `/divorce/uncontested-divorce/` (23 traffic)
- `/firm/elizabeth-findley/` (17 traffic)
- `/divorce/high-asset-divorce/` (16 traffic)
- `/firm/mali-shadmehry/` (11 traffic)
- `/firm/` (7 traffic)
- `/firm/madison-alexander/` (1 traffic)
- `/divorce/lgbtq-divorce/`
- … 33 more in Ahrefs

### 2. Organization schema missing or incomplete

`issue:organization-schema-missing-or-incomplete` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (164 traffic)

### 3. Links to redirect, skipped by fix-redirect-links: redirects to homepage

`redirect-links:redirects-to-homepage` · redirect-rules · decide · decider: client · source: redirect-map-2026-10-29.json

Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order.

- `/collaborative-divorce-attorney/basics-collaborative-approach/` (1 links)
- `/family-law/alimony-modification/` (1 links)
- `/mediation/mediation-faqs/` (1 links)
- `/modifications/` (1 links)

### 4. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page.

- `/terms/`
- `/privacy-policy/`
- `/andrea-hastings-top-one-percent/`

### 5. Links to redirect, skipped by fix-redirect-links: redirects off-site to forwardfacing.com

`redirect-links:redirects-off-site-to-forwardfacing-com` · manual · decide · decider: client · source: redirect-map-2026-10-29.json

Confirm the off-site redirect is meant; if yes, nothing to do.

- `/podcast/` (1 links)

### 6. Links to redirect, skipped by fix-redirect-links: pagination /page/1/ comes from the theme template, not content

`redirect-links:pagination-page-1-comes-from-the-theme-t` · manual · FLAG · decider: agency · source: redirect-map-2026-10-29.json

Theme template edit: emit the archive root for page 1 (WordPress paginate_links does by default). Diff by hand.

- `/blog/page/1/` (12 links)
- `/category/collaborative-divorce/page/1/` (4 links)
- `/category/families/page/1/` (4 links)
- `/category/uncategorized/page/1/` (2 links)
- `/category/divorce-faq/page/1/` (1 links)
- `/category/divorce/page/1/` (1 links)
- `/category/firm-news/page/1/` (1 links)

### 7. Main content requires JavaScript rendering

`issue:main-content-requires-javascript-rendering` · theme/plugin (by hand) · FLAG · decider: agency

Find the widget rendering the main copy client-side (reviews/feed plugin) and give it server-side output or fallback text.

- `/what-our-clients-say/`

### 8. Links to redirect, skipped by fix-redirect-links: author archive

`redirect-links:author-archive` · indexation-review · APPROVE · decider: agency · source: redirect-map-2026-10-29.json

Yoast > Search Appearance > Archives: disable author archives (or the author sitemap); one setting removes them all.

- `/author/content/`
- `/author/haleyburklowkz0p/`
- `/author/joegraterdigital-com/`
- `/author/tatelyngraterdigital-com/`
- `/author/tatelyninteractivesearchmarketing-com/`

### 9. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/terms/`
- `/privacy-policy/`

### 10. Links to redirect, skipped by fix-redirect-links: looks like a pasted file path (one post's broken image)

`redirect-links:looks-like-a-pasted-file-path-one-post-s` · fix-images · APPROVE · decider: agency · source: redirect-map-2026-10-29.json

Re-upload the post's image to the media library and replace the src by hand (fix-images lists it as a broken/redirected image).

- `/understanding-roles-collaborative-divorce-team/Collaborative%20Divorce%20Team%20Hastings%20Shadmehry` (1 links)

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Links to redirect, skipped by fix-redirect-links: redirects to homepage** (4 pages: /collaborative-divorce-attorney/basics-collaborative-approach/, /family-law/alimony-modification/, /mediation/mediation-faqs/, /modifications/)

4 old URLs on hsfamilylaw.com currently redirect to the homepage, which loses visitors who click an old link. For each one we need the page it should go to now (or confirmation that nothing replaces it, in which case we remove the links).

**Pages hidden from Google (noindex/nofollow): confirm intent** (3 pages: /terms/, /privacy-policy/, /andrea-hastings-top-one-percent/)

3 pages on hsfamilylaw.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

**Links to redirect, skipped by fix-redirect-links: redirects off-site to forwardfacing.com** (1 page: /podcast/)

One link on hsfamilylaw.com (/podcast/) sends visitors to another website. If that is intended, say so and we leave it; if not, tell us where it should go.

## Skipped on purpose

- Indexable page not in sitemap (12): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

