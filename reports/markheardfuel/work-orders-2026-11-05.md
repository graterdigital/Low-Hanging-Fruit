# Work orders: markheardfuel.com

Ahrefs Site Audit project 9799849 · crawl 2026-11-05 · health 90 · 34 active issue types → 15 work orders (3 decisions, 7 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 31 | 20 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 2 | Orphan page (has no incoming internal links) | indexation-review | decide | 6 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 3 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 1 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex page. |
| 4 | Links to redirect, skipped by fix-redirect-links: URL has a query string | manual | decide | 1 | 0 | agency | fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave. |
| 5 | CSS file size too large | manual | FLAG | 5 | 0 | agency | Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket. |
| 6 | FAQ page missing FAQPage schema | schema-check | FLAG | 5 | 0 | client | FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing. |
| 7 | Pages fix-meta routed to [] | [] | FLAG | 3 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 8 | Pages fix-meta routed to ['/blog', '/blog/cache'] | ['/blog', '/blog/cache'] | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 9 | wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings) | manual | FLAG | 1 | 0 | agency | Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1103-fix-redirect-links-live-options.md. |
| 10 | Page has nofollow outgoing internal links | nofollow-audit | APPROVE (skill pending) | 2 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 11 | Organization schema missing or incomplete | schema-fix | APPROVE (skill pending) | 1 | 0 | agency | Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 12 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 1 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 13 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 6 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 14 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 2 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 15 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 2 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/service-areas/gainesville-ga-propane` (18 traffic)
- `/service-areas/jasper-ga-propane` (2 traffic)
- `/thank-you-refill`
- `/service-areas/dawsonville-ga-propane`
- `/services/new-account-setup`
- `/services`
- `/blog/cache-5`
- `/services/pay-bill`
- `/blog/cache-4`
- `/blog`
- … 21 more in Ahrefs

### 2. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/thank-you-refill`
- `/services`
- `/thank-you-new-service`
- `/thank-you`
- `/service-areas`
- `/local-propane-service`

### 3. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex page.

- `/privacy-policy`

### 4. Links to redirect, skipped by fix-redirect-links: URL has a query string

`redirect-links:url-has-a-query-string` · manual · decide · decider: agency · source: redirect-map-2026-10-29.json

fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave.

- `/?utm_campaign=gmb` (2 links)

### 5. CSS file size too large

`issue:css-file-size-too-large` · manual · FLAG · decider: agency

Builder/theme CSS; minify or defer via the cache/optimizer plugin. Hosting or theme ticket.

- `/wp-content/cache/min/1/wp-content/plugins/widget-google-reviews/assets/7.2/css/public-main.css?ver=1793235247`
- `/wp-content/cache/min/1/wp-content/themes/markheard/assets/css/custom.css?ver=1793235247`
- `/wp-content/cache/min/1/wp-includes/css/dashicons.min.css?ver=1793235364`
- `/wp-content/cache/min/1/wp-content/themes/markheard/assets/css/foundation.css?ver=1793235247`
- `/wp-content/cache/min/1/wp-content/plugins/business-reviews-bundle/assets/2.1.1/css/public-main.css?ver=1793235247`

### 6. FAQ page missing FAQPage schema

`issue:faq-page-missing-faqpage-schema` · schema-check · FLAG · decider: client

FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing.

- `/faqs/propane-safety-faqs`
- `/faqs/underground-propane-tanks`
- `/faqs/why-choose-propane`
- `/faqs`
- `/faqs/ordering-information`

### 7. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `noindex`
- `non-200`
- `homepage title`

### 8. Pages fix-meta routed to ['/blog', '/blog/cache']

`fix-meta:blog-blog-cache` · ['/blog', '/blog/cache'] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`

### 9. wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings)

`redirect-links:wp-options` · manual · FLAG · decider: agency · source: 2026-10-30-1103-fix-redirect-links-live-options.md

Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1103-fix-redirect-links-live-options.md.

- `su_presets_button`

### 10. Page has nofollow outgoing internal links

`issue:page-has-nofollow-outgoing-internal-links` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/local-propane-service`
- `/`

### 11. Organization schema missing or incomplete

`issue:organization-schema-missing-or-incomplete` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/`

### 12. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/privacy-policy`

### 13. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/thank-you-refill`
- `/services`
- `/thank-you-new-service`
- `/thank-you`
- `/faqs`
- `/`

### 14. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/submit-service-request/`
- `/why-choose-propane/`

### 15. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/submit-service-request/`
- `/why-choose-propane/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Orphan page (has no incoming internal links)** (6 pages: /thank-you-refill, /services, /thank-you-new-service, /thank-you, …)

6 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Pages hidden from Google (noindex/nofollow): confirm intent** (1 page: /privacy-policy)

1 page on markheardfuel.com is set so Google does not index it (or does not follow its links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

