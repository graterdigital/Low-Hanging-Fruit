# Work orders: slepianfirm.com

Ahrefs Site Audit project 9704553 · crawl 2026-11-05 · health 92 · 31 active issue types → 12 work orders (2 decisions, 4 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 68 | 215 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 2 | H1 tag missing or empty | manual | FLAG | 2 | 148 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 3 | Organization schema missing or incomplete | schema-fix | APPROVE (skill pending) | 1 | 148 | agency | Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 4 | X (Twitter) card missing | fix-social-tags | AUTO (skill pending) | 6 | 148 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 5 | Orphan page (has no incoming internal links) | indexation-review | decide | 9 | 1 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 6 | FAQ page missing FAQPage schema | schema-check | FLAG | 3 | 1 | client | FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing. |
| 7 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 84 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page. |
| 8 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 88 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 9 | Pages fix-meta routed to [] | [] | FLAG | 4 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 10 | wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings) | manual | FLAG | 4 | 0 | agency | Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-0957-fix-redirect-links-live-options.md. |
| 11 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 1 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 12 | Links to redirect, skipped by fix-redirect-links: author archive | indexation-review | APPROVE | 1 | 0 | agency | Yoast > Search Appearance > Archives: disable author archives (or the author sitemap); one setting removes them all. |

## Per item

### 1. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/` (148 traffic)
- `/personal-injury-attorney/` (34 traffic)
- `/real-estate-attorney/closing-checklist-for-lenders-and-mortgage-brokers/` (10 traffic)
- `/real-estate-attorney/closing-checklist-for-the-agent/` (5 traffic)
- `/landlord-tenant-attorney/` (5 traffic)
- `/real-estate-attorney/closing-checklist-for-sellers/` (3 traffic)
- `/gary-schwartz/` (3 traffic)
- `/real-estate-attorney-represent-buyer-seller/` (2 traffic)
- `/civil-litigation-vs-small-claims/` (2 traffic)
- `/contact-us/` (1 traffic)
- … 58 more in Ahrefs

### 2. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/` (148 traffic)
- `/news/`

### 3. Organization schema missing or incomplete

`issue:organization-schema-missing-or-incomplete` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (148 traffic)

### 4. X (Twitter) card missing

`issue:x-twitter-card-missing` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/` (148 traffic)
- `/sitemap/`
- `/reviews/`
- `/real-estate-attorney/title-order-request/`
- `/news/`
- `/what-our-clients-say/`

### 5. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/estate-faqs/` (1 traffic)
- `/sitemap/`
- `/reviews/`
- `/samuel-johnson/`
- `/builders-and-developers/`
- `/information-about-closing/`
- `/canon-g-snow/`
- `/terms-of-use/`
- `/emily-client-feedback/`

### 6. FAQ page missing FAQPage schema

`issue:faq-page-missing-faqpage-schema` · schema-check · FLAG · decider: client

FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing.

- `/estate-faqs/` (1 traffic)
- `/real-estate-attorney/closing-faqs/`
- `/sitemap/`

### 7. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Noindex follow page, Noindex page.

- `/tag/buy-sell-agreement-ga/`
- `/category/blog/page/3/`
- `/category/family-law/`
- `/tag/divorce/`
- `/tag/juvenile-criminal-defense/`
- `/tag/divorce-court/`
- `/tag/dispute-resolution/`
- `/tag/filing-for-divorce/`
- `/tag/ga-drivers-license/`
- `/category/blog/page/4/`
- … 74 more in Ahrefs

### 8. H1 tag missing or empty  (non-indexable pages)

`issue:h1-tag-missing-or-empty-nonindexable` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/tag/buy-sell-agreement-ga/`
- `/category/blog/page/3/`
- `/news/page/3/`
- `/category/family-law/`
- `/tag/divorce/`
- `/tag/juvenile-criminal-defense/`
- `/tag/divorce-court/`
- `/tag/dispute-resolution/`
- `/tag/filing-for-divorce/`
- `/tag/ga-drivers-license/`
- … 78 more in Ahrefs

### 9. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`
- `noindex`
- `non-200`
- `homepage title`

### 10. wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings)

`redirect-links:wp-options` · manual · FLAG · decider: agency · source: 2026-10-30-0957-fix-redirect-links-live-options.md

Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-0957-fix-redirect-links-live-options.md.

- `widget_text`
- `widget_text`
- `widget_text`
- `widget_text`

### 11. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/prepare-mediation-ga/`

### 12. Links to redirect, skipped by fix-redirect-links: author archive

`redirect-links:author-archive` · indexation-review · APPROVE · decider: agency · source: redirect-map-2026-10-29.json

Yoast > Search Appearance > Archives: disable author archives (or the author sitemap); one setting removes them all.

- `/author/ismuser/` (149 links)

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Orphan page (has no incoming internal links)** (9 pages: /estate-faqs/, /sitemap/, /reviews/, /samuel-johnson/, …)

9 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Pages hidden from Google (noindex/nofollow): confirm intent** (84 pages: /tag/buy-sell-agreement-ga/, /category/blog/page/3/, /category/family-law/, /tag/divorce/, …)

84 pages on slepianfirm.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

