# Work orders: miuraboiler.com

Ahrefs Site Audit project 9704539 · crawl 2026-11-05 · health 99 · 68 active issue types → 28 work orders (8 decisions, 6 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | AI crawler policy (robots.txt): client decision | ai-discoverability | decide | 453 | 2096 (top 200 of 453) | client | Set the client's ai: policy (allow/block search bots, allow/block training bots), then ai-discoverability applies the managed robots.txt block. Ahrefs issues folded in: Inconsistent AI training bot policy, Indexable page blocked from some AI search bots. |
| 2 | Structured data has schema.org validation error | schema-fix | FLAG | 2934 | 2079 (top 200 of 2934) | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 3 | H1 tag missing or empty | manual | FLAG | 37 | 577 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 4 | Slow page | manual | FLAG | 1754 | 285 (top 200 of 1754) | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 5 | Category page missing ItemList schema | schema-check | FLAG | 2 | 78 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 6 | Product page missing Product schema | schema-check | FLAG | 18 | 54 | agency | Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages. |
| 7 | Slow server response for AI crawlers | hosting/cache | FLAG | 9 | 3 | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 8 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 5511 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page. |
| 9 | Links to redirect, skipped by fix-redirect-links: URL has a query string | manual | decide | 170 | 0 | agency | fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave. |
| 10 | Links to redirect, skipped by fix-redirect-links: redirects off-site to storage.pardot.com | manual | decide | 13 | 0 | client | Confirm the off-site redirect is meant; if yes, nothing to do. |
| 11 | Links to redirect, skipped by fix-redirect-links: final target returns 404, not 200 | manual | decide | 9 | 0 | agency | fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave. |
| 12 | Links to redirect, skipped by fix-redirect-links: redirects to homepage | redirect-rules | decide | 5 | 0 | client | Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order. |
| 13 | Links to redirect, skipped by fix-redirect-links: no incoming internal links (sitemap or orphan entry) | manual | decide | 2 | 0 | agency | fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave. |
| 14 | Links to redirect, skipped by fix-redirect-links: path contains a backslash, quote, space or angle bracket | manual | decide | 1 | 0 | agency | fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave. |
| 15 | wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings) | manual | FLAG | 124 | 0 | agency | Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1053-fix-redirect-links-live-options.md. |
| 16 | Multiple title tags | manual | FLAG | 5 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 17 | FAQ page missing FAQPage schema | schema-check | FLAG | 2 | 0 | client | FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing. |
| 18 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 2 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 19 | Pages fix-meta routed to homepage title | homepage title | FLAG | 1 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 20 | 500 page | manual | FLAG | 1 | 0 | agency | Server error on request: open the URL, read the host's PHP error log for that path. Hosting ticket if it is not a plugin fatal. |
| 21 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 22 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 23 | Waiting on skill `schema-fix` (2 issue types): Structured data has Google rich results validation error (2919); Organization schema missing or incomplete (1) | schema-fix | skill pending | 2920 | 2079 | agency | Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual |
| 24 | Waiting on skill `fix-broken-links` (5 issue types): Page has links to broken page (10); 404 page (11); 4XX page (11); 5XX page (1); Page has links to broken page  (non-indexable pages) (7) | fix-broken-links | skill pending | 40 | 536 | agency | Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 25 | Waiting on skill `indexation-review` (3 issue types): Indexable page not in sitemap (47); Canonical URL has no incoming internal links (1); 5XX page in sitemap (1) | indexation-review | skill pending | 49 | 17 | agency | Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 26 | Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (47) | fix-social-tags | skill pending | 47 | 17 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 27 | Waiting on skill `nofollow-audit` (2 issue types): Page has nofollow outgoing internal links  (non-indexable pages) (3088); Page has nofollow outgoing internal links (2) | nofollow-audit | skill pending | 3090 | 0 | agency | Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 28 | Waiting on skill `redirect-rules` (5 issue types): Canonical from HTTP to HTTPS (1); Canonical points to redirect (4); 302 redirect (13); Broken redirect (9); 3XX redirect in sitemap (3) | redirect-rules | skill pending | 30 | 0 | agency | Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |

## Per item

### 1. AI crawler policy (robots.txt): client decision

`issue:ai-bot-policy-decide` · ai-discoverability · decide · decider: client

Set the client's ai: policy (allow/block search bots, allow/block training bots), then ai-discoverability applies the managed robots.txt block. Ahrefs issues folded in: Inconsistent AI training bot policy, Indexable page blocked from some AI search bots.

- `/steam-boilers-101/` (631 traffic)
- `/` (536 traffic)
- `/low-pressure-steam-vs-high-pressure-steam/` (148 traffic)
- `/products-category/steam-boilers/` (70 traffic)
- `/how-do-modular-boilers-work/` (45 traffic)
- `/how-to-find-the-most-efficient-industrial-steam-boiler/` (43 traffic)
- `/how-are-steam-boilers-used-in-hospitals/` (40 traffic)
- `/difference-between-water-tube-boiler-and-a-fire-tube-boiler/` (40 traffic)
- `/what-is-a-boiler-turndown-ratio/` (39 traffic)
- `/products/feedwater-tanks/` (38 traffic)
- … 443 more in Ahrefs

### 2. Structured data has schema.org validation error

`issue:structured-data-has-schema-org-validation-error` · schema-fix · FLAG · decider: agency

Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit.

- `/steam-boilers-101/` (631 traffic)
- `/` (536 traffic)
- `/low-pressure-steam-vs-high-pressure-steam/` (148 traffic)
- `/products-category/steam-boilers/` (70 traffic)
- `/how-do-modular-boilers-work/` (45 traffic)
- `/how-to-find-the-most-efficient-industrial-steam-boiler/` (43 traffic)
- `/how-are-steam-boilers-used-in-hospitals/` (40 traffic)
- `/difference-between-water-tube-boiler-and-a-fire-tube-boiler/` (40 traffic)
- `/what-is-a-boiler-turndown-ratio/` (39 traffic)
- `/products/feedwater-tanks/` (38 traffic)
- … 2924 more in Ahrefs

### 3. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/` (536 traffic)
- `/difference-between-water-tube-boiler-and-a-fire-tube-boiler/` (40 traffic)
- `/another-sucessful-mac-technical-training-in-rockmart/` (1 traffic)
- `/resources/emissions/`
- `/miura-warranty/`
- `/understanding-and-complying-with-evolving-steam-boiler-emissions-regulations/`
- `/miura-hosts-successful-open-house-at-rockmart-headquarters/`
- `/tip-top-chooses-miura/`
- `/miuras-4th-annual-first-responders-appreciation-day-event/`
- `/steam-boiler-safety-in-an-age-of-public-health-concerns/`
- … 27 more in Ahrefs

### 4. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/how-do-modular-boilers-work/` (45 traffic)
- `/how-to-find-the-most-efficient-industrial-steam-boiler/` (43 traffic)
- `/what-is-a-boiler-turndown-ratio/` (39 traffic)
- `/products/feedwater-tanks/` (38 traffic)
- `/how-are-water-softeners-used-in-steam-boilers/` (30 traffic)
- `/how-boiler-economizers-reduce-energy-consumption/` (26 traffic)
- `/the-basics-of-industrial-steam-boiler-systems/` (19 traffic)
- `/what-is-thermal-shock-and-how-do-you-prevent-it/` (10 traffic)
- `/scale-build-up-in-industrial-steam-boilers-what-it-is-and-how-to-prevent-it/` (7 traffic)
- `/category/videos/general/` (7 traffic)
- … 1744 more in Ahrefs

### 5. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/products-category/steam-boilers/` (70 traffic)
- `/products-category/all/` (8 traffic)

### 6. Product page missing Product schema

`issue:product-page-missing-product-schema` · schema-check · FLAG · decider: agency

Check whether these are quote-only products (no price = no Offer, schema adds nothing) or misclassified category pages.

- `/products/feedwater-tanks/` (38 traffic)
- `/lx-series-steam-boiler/` (10 traffic)
- `/products/chemical-treatment/` (4 traffic)
- `/products/deaerator-tanks/` (2 traffic)
- `/products/bl-boiler-controller/`
- `/products/colormetry-hardness-detection-system/`
- `/products/miura-online-maintenance-mom/`
- `/5ppm/`
- `/products/bp-panel/`
- `/products/ro-systems/`
- … 8 more in Ahrefs

### 7. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/products/deaerator-tanks/` (2 traffic)
- `/industries/food-beverage/` (1 traffic)
- `/powering-precision-how-miura-americas-advanced-steam-technologies-are-transforming-semiconductor-manufacturing/`
- `/5ppm/`
- `/february-2026-newsletter/`
- `/boiler-maintenance/`
- `/february-2025-newsletter/`
- `/specifications/boilermate/`
- `/may-2024-newsletter/`

### 8. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page.

- `/events/category/trade-shows/list/?tribe-bar-date=2026-10-23&outlook-ical=1`
- `/events/list/?tribe-bar-date=2026-06-09&eventDisplay=past&ical=1`
- `/page/2/?post_type=tribe_events&eventDisplay=day&eventDate=2026-10-13&ical=1`
- `/events/list/page/2/?tribe-bar-date=2027-01-23&ical=1`
- `/events/category/trade-shows/list/?tribe-bar-date=2026-06-26&ical=1`
- `/events/category/trade-shows/day/2026-06-07/?ical=1`
- `/events/list/?tribe-bar-date=2027-02-06&eventDisplay=past&ical=1`
- `/events/category/trade-shows/day/2026-08-11/?outlook-ical=1`
- `/events/list/?tribe-bar-date=2026-04-23&eventDisplay=past&ical=1`
- `/events/list/?tribe-bar-date=2026-10-07&eventDisplay=past&ical=1`
- … 5501 more in Ahrefs

### 9. Links to redirect, skipped by fix-redirect-links: URL has a query string

`redirect-links:url-has-a-query-string` · manual · decide · decider: agency · source: redirect-map-2026-10-22.json

fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave.

- `/?post_type=tribe_events&eventDisplay=day&paged=2` (3 links)
- `/?post_type=tribe_events&eventDisplay=day&paged=2&eventDate=2027-02-01` (2 links)
- `/?post_type=tribe_events&eventDisplay=day&paged=2&eventDate=2026-07-04` (2 links)
- `/?post_type=tribe_events&eventDisplay=day&paged=2&eventDate=2026-06-17` (2 links)
- `/?post_type=tribe_events&eventDisplay=day&paged=2&eventDate=2027-01-01` (2 links)
- `/?post_type=tribe_events&eventDisplay=day&paged=2&eventDate=2026-10-25` (2 links)
- `/?post_type=tribe_events&eventDisplay=day&paged=2&eventDate=2026-04-22` (2 links)
- `/?post_type=tribe_events&eventDisplay=day&paged=2&eventDate=2026-09-15` (2 links)
- `/?post_type=tribe_events&eventDisplay=day&paged=2&eventDate=2026-07-03` (2 links)
- `/?post_type=tribe_events&eventDisplay=day&paged=2&eventDate=2026-11-06` (2 links)
- … 160 more in Ahrefs

### 10. Links to redirect, skipped by fix-redirect-links: redirects off-site to storage.pardot.com

`redirect-links:redirects-off-site-to-storage-pardot-com` · manual · decide · decider: client · source: redirect-map-2026-10-22.json

Confirm the off-site redirect is meant; if yes, nothing to do.

- `/l/312261/2026-02-12/nz6c1/312261/1770913004YCaBk8Nt/Reverse_Osmosis_Press_Release.jpg` (1 links)
- `/l/312261/2026-05-15/p2flq/312261/1778859194Aakd9mTw/Beige_Minimalist_Mood_Photo_Collage.jpg` (1 links)
- `/l/312261/2025-12-10/nxg4x/312261/1765380118nVrbchaw/Learn_more_button.jpg` (1 links)
- `/l/312261/2026-02-12/nz6jt/312261/1770923602QuPBdhk2/FEB2026_NewsletterHeader.jpg` (1 links)
- `/l/312261/2026-02-12/nz6cj/312261/1770915986Aw96zpzh/BP_Panel_Live.jpg` (1 links)
- `/l/312261/2026-02-12/nz6cx/312261/1770916670DOOP6yQQ/F_B_Blog_Header.jpg` (1 links)
- `/l/312261/2026-02-12/nz6cq/312261/1770916394duDvbmY7/Scale_Blog_Header.jpeg` (1 links)
- `/l/312261/2026-02-12/nz6ct/312261/1770916642mPpY3CJO/Open_House_Outlook_Email_Header.png` (1 links)
- `/l/312261/2026-05-15/p2fr4/312261/1778870855FH836MUe/MAY2026_NewsletterHeader.jpg` (1 links)
- `/l/312261/2026-05-15/p2fm1/312261/1778861444gS6FgI9E/2026_06_Open_House_Registration_Card_Part1.jpg` (1 links)
- … 3 more in Ahrefs

### 11. Links to redirect, skipped by fix-redirect-links: final target returns 404, not 200

`redirect-links:final-target-returns-404-not-200` · manual · decide · decider: agency · source: redirect-map-2026-10-22.json

fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave.

- `/tag/lx/` (296 links)
- `/august-2026-newsletter/{{Unsubscribe}}` (1 links)
- `/may-2026-newsletter/{{Unsubscribe}}` (1 links)
- `/august-2026-newsletter/{{{EmailPreferenceCenter}}}` (1 links)
- `/february-2026-newsletter/{{{EmailPreferenceCenter}}}` (1 links)
- `/november-2025-newsletter/{{Unsubscribe}}` (1 links)
- `/may-2026-newsletter/{{{EmailPreferenceCenter}}}` (1 links)
- `/february-2026-newsletter/{{Unsubscribe}}` (1 links)
- `/november-2025-newsletter/{{{EmailPreferenceCenter}}}` (1 links)

### 12. Links to redirect, skipped by fix-redirect-links: redirects to homepage

`redirect-links:redirects-to-homepage` · redirect-rules · decide · decider: client · source: redirect-map-2026-10-22.json

Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order.

- `/events-old/pack-expo-international-nov-3-6-2/` (2497 links)
- `/events-old/imc-december-16-19-2/` (2497 links)
- `/events-old/ahr-feb-10-12-2/` (2497 links)
- `/events-old/adi-2025-craft-distillers-conference/` (2497 links)
- `/reps-category/usvi/` (3 links)

### 13. Links to redirect, skipped by fix-redirect-links: no incoming internal links (sitemap or orphan entry)

`redirect-links:no-incoming-internal-links-sitemap-or-or` · manual · decide · decider: agency · source: redirect-map-2026-10-22.json

fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave.

- `/august-2024-newsletter/`
- `/product-listings/`

### 14. Links to redirect, skipped by fix-redirect-links: path contains a backslash, quote, space or angle bracket

`redirect-links:path-contains-a-backslash-quote-space-or` · manual · decide · decider: agency · source: redirect-map-2026-10-22.json

fix-redirect-links skipped these; read the reason and decide: redirect rule, link edit by hand, or leave.

- `/rep-locator/\` (1 links)

### 15. wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings)

`redirect-links:wp-options` · manual · FLAG · decider: agency · source: 2026-10-30-1053-fix-redirect-links-live-options.md

Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1053-fix-redirect-links-live-options.md.

- `widget_media_image`
- `usr_map`
- `wpseo_taxonomy_meta`
- `wpmdb_state_5c7c34743e6c7`
- `wpmdb_state_5c7da3e3a72c9`
- `wpmdb_state_5c7da6f09858e`
- `wpmdb_state_5c7fc93e73ba4`
- `wpmdb_state_5c8050cea11f7`
- `wpmdb_state_5c81202f48e54`
- `wpmdb_state_5c813059e7d16`
- … 114 more in Ahrefs

### 16. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/may-2026-newsletter/`
- `/august-2025-newsletter/`
- `/november-2025-newsletter/`
- `/august-2026-newsletter/`
- `/february-2026-newsletter/`

### 17. FAQ page missing FAQPage schema

`issue:faq-page-missing-faqpage-schema` · schema-check · FLAG · decider: client

FAQ rich results are gone from Google (2026-05). Add only if visible Q&A exists and the client wants it for Bing.

- `/category/faq/`
- `/resources/faq/`

### 18. H1 tag missing or empty  (non-indexable pages)

`issue:h1-tag-missing-or-empty-nonindexable` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/efficiency-calculator/`
- `/qsx-quote/`

### 19. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `/`

### 20. 500 page

`issue:500-page` · manual · FLAG · decider: agency

Server error on request: open the URL, read the host's PHP error log for that path. Hosting ticket if it is not a plugin fatal.

- `/products/`

### 21. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 22. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 23. Waiting on skill `schema-fix` (2 issue types): Structured data has Google rich results validation error (2919); Organization schema missing or incomplete (1)

`pending:schema-fix` · schema-fix · skill pending · decider: agency

Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual

- `/steam-boilers-101/` (631 traffic)
- `/` (536 traffic)
- `/low-pressure-steam-vs-high-pressure-steam/` (148 traffic)
- `/products-category/steam-boilers/` (70 traffic)
- `/how-do-modular-boilers-work/` (45 traffic)
- `/how-to-find-the-most-efficient-industrial-steam-boiler/` (43 traffic)
- `/how-are-steam-boilers-used-in-hospitals/` (40 traffic)
- `/difference-between-water-tube-boiler-and-a-fire-tube-boiler/` (40 traffic)
- `/what-is-a-boiler-turndown-ratio/` (39 traffic)
- `/products/feedwater-tanks/` (38 traffic)
- … 2910 more in Ahrefs

### 24. Waiting on skill `fix-broken-links` (5 issue types): Page has links to broken page (10); 404 page (11); 4XX page (11); 5XX page (1); Page has links to broken page  (non-indexable pages) (7)

`pending:fix-broken-links` · fix-broken-links · skill pending · decider: agency

Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/` (536 traffic)
- `/miura-warranty/`
- `/miura-america-honored-with-2026-trsa-community-service-award/`
- `/privacy-policy/`
- `/contact/`
- `/how-pressure-simulations-benefit-steam-generation-efficiency/`
- `/miura-donates-ppe-to-medical-centers-assisted-living-facilities/`
- `/fast-boiler-delivery-avoid-winter-downtime/`
- `/november-2025-newsletter/`
- `/7-easy-steps-to-getting-an-emergency-steam-boiler/`
- … 30 more in Ahrefs

### 25. Waiting on skill `indexation-review` (3 issue types): Indexable page not in sitemap (47); Canonical URL has no incoming internal links (1); 5XX page in sitemap (1)

`pending:indexation-review` · indexation-review · skill pending · decider: agency

Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/tag/modular-water-tube-boilers/` (11 traffic)
- `/tag/industrial-laundry/` (5 traffic)
- `/tag/boiler-maintenance-safety/` (1 traffic)
- `/tag/trap-energy/`
- `/tag/miura/`
- `/tag/rental-boilers/`
- `/tag/miura-technician/`
- `/tag/show/`
- `/reps/boiler-masters-inc/`
- `/tag/industrial-boiler-rentals/`
- … 39 more in Ahrefs

### 26. Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (47)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/tag/modular-water-tube-boilers/` (11 traffic)
- `/tag/industrial-laundry/` (5 traffic)
- `/tag/boiler-maintenance-safety/` (1 traffic)
- `/tag/trap-energy/`
- `/tag/miura/`
- `/tag/rental-boilers/`
- `/tag/miura-technician/`
- `/tag/show/`
- `/category/videos/miscellaneous/`
- `/reps/boiler-masters-inc/`
- … 37 more in Ahrefs

### 27. Waiting on skill `nofollow-audit` (2 issue types): Page has nofollow outgoing internal links  (non-indexable pages) (3088); Page has nofollow outgoing internal links (2)

`pending:nofollow-audit` · nofollow-audit · skill pending · decider: agency

Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/events/category/trade-shows/list/?tribe-bar-date=2026-05-25`
- `/events/category/trade-shows/list/?tribe-bar-date=2027-01-27&eventDisplay=past`
- `/events/2026-03-24/`
- `/events/category/trade-shows/day/2026-08-27/`
- `/events/list/page/2/?tribe-bar-date=2026-03-18&eventDisplay=past`
- `/events/list/?tribe-bar-date=2027-02-08&eventDisplay=past`
- `/page/2/?post_type=tribe_events&eventDisplay=day&eventDate=2026-06-26`
- `/events/list/?tribe-bar-date=2027-02-16`
- `/events/category/trade-shows/day/2027-02-01/`
- `/events/list/?tribe-bar-date=2026-06-29`
- … 3080 more in Ahrefs

### 28. Waiting on skill `redirect-rules` (5 issue types): Canonical from HTTP to HTTPS (1); Canonical points to redirect (4); 302 redirect (13); Broken redirect (9); 3XX redirect in sitemap (3)

`pending:redirect-rules` · redirect-rules · skill pending · decider: agency

Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/products/ro-systems/`
- … 29 more in Ahrefs

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**AI crawler policy (robots.txt): client decision** (453 pages: /steam-boilers-101/, /, /low-pressure-steam-vs-high-pressure-steam/, /products-category/steam-boilers/, …)

Some AI crawlers are blocked from miuraboiler.com. Allowing AI search bots (ChatGPT, Perplexity, Claude search) lets those tools cite the site in their answers; allowing training bots (GPTBot, ClaudeBot, Google-Extended) puts the content into future models. Our default is allow both; blocking training bots does not affect Google Search. Tell us if you want training bots blocked and we will set it.

**Pages hidden from Google (noindex/nofollow): confirm intent** (5511 pages: /events/category/trade-shows/list/?tribe-bar-date=2026-10-23&outlook-ical=1, /events/list/?tribe-bar-date=2026-06-09&eventDisplay=past&ical=1, /page/2/?post_type=tribe_events&eventDisplay=day&eventDate=2026-10-13&ical=1, /events/list/page/2/?tribe-bar-date=2027-01-23&ical=1, …)

5511 pages on miuraboiler.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

**Links to redirect, skipped by fix-redirect-links: redirects off-site to storage.pardot.com** (13 pages: /l/312261/2026-02-12/nz6c1/312261/1770913004YCaBk8Nt/Reverse_Osmosis_Press_Release.jpg, /l/312261/2026-05-15/p2flq/312261/1778859194Aakd9mTw/Beige_Minimalist_Mood_Photo_Collage.jpg, /l/312261/2025-12-10/nxg4x/312261/1765380118nVrbchaw/Learn_more_button.jpg, /l/312261/2026-02-12/nz6jt/312261/1770923602QuPBdhk2/FEB2026_NewsletterHeader.jpg, …)

One link on miuraboiler.com (/l/312261/2026-02-12/nz6c1/312261/1770913004YCaBk8Nt/Reverse_Osmosis_Press_Release.jpg) sends visitors to another website. If that is intended, say so and we leave it; if not, tell us where it should go.

**Links to redirect, skipped by fix-redirect-links: redirects to homepage** (5 pages: /events-old/pack-expo-international-nov-3-6-2/, /events-old/imc-december-16-19-2/, /events-old/ahr-feb-10-12-2/, /events-old/adi-2025-craft-distillers-conference/, …)

5 old URLs on miuraboiler.com currently redirect to the homepage, which loses visitors who click an old link. For each one we need the page it should go to now (or confirmation that nothing replaces it, in which case we remove the links).

