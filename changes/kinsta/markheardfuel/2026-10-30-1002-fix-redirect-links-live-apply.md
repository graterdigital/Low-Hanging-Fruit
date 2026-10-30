# fix-redirect-links: markheardfuel.com (live)

Run 2026-10-30-1002 · mode **apply** · alias `markheardfuel` · provider `kinsta` · map `redirect-map-2026-10-29.json`

Install host `markheardfuel.com`; hosts matched: `markheardfuel.com`. Entries starting `host:` are legacy-host links moved to the current host.

Object cache flush after apply: ok (`Success: All caches were cleared. Changes usually appear globally within a few minutes.`)

## Totals (replacements per old URL)

- `https://markheardfuel.com/about/` → 1
- `https://markheardfuel.com/contact/` → 3
- `https://markheardfuel.com/faqs/why-choose-propane/` → 1
- `https://markheardfuel.com/services/new-account-setup/` → 2
- `https://markheardfuel.com/services/order-a-refill/` → 1
- `https://markheardfuel.com/services/signup-for-new-service/` → 10

## Posts changed (12)

| ID | type | title | URL | replacements | applied |
|---|---|---|---|---|---|
| 605 | page | Milton, GA Propane Company | https://markheardfuel.com/service-areas/milton-ga-propane | 1 | True |
| 343 | page | Alpharetta, GA Propane Company | https://markheardfuel.com/service-areas/alpharetta-ga-propane | 1 | True |
| 345 | page | Buford, GA Propane Company | https://markheardfuel.com/service-areas/buford-ga-propane | 1 | True |
| 607 | page | Canton, GA Propane Company | https://markheardfuel.com/service-areas/canton-ga-propane | 1 | True |
| 347 | page | Cumming, GA Propane Company | https://markheardfuel.com/service-areas/cumming-ga-propane-company | 1 | True |
| 608 | page | Dahlonega GA, Propane Company | https://markheardfuel.com/service-areas/dahlonega-ga-propane | 1 | True |
| 359 | page | Dawsonville GA, Propane Company | https://markheardfuel.com/service-areas/dawsonville-ga-propane | 1 | True |
| 609 | page | Gainesville, GA Propane Company | https://markheardfuel.com/service-areas/gainesville-ga-propane | 1 | True |
| 361 | page | Jasper, GA Propane Company | https://markheardfuel.com/service-areas/jasper-ga-propane | 1 | True |
| 610 | page | John's Creek, GA Propane Company | https://markheardfuel.com/service-areas/johns-creek-ga-propane | 1 | True |
| 663 | page | Keep Full Propane Autofill Service | https://markheardfuel.com/keep-full | 1 | True |
| 989 | post | What To Do If You Smell Propane Gas In Your House? | https://markheardfuel.com/blog/propane-gas-smell-actions | 1 | True |

## Postmeta changed (6)

| meta_id | post | key | kind | replacements | applied |
|---|---|---|---|---|---|
| 511 | 2 | about_us_link | serialized | 1 | True |
| 639 | 2 | faq_text | plain | 1 | True |
| 283 | 20 | services_page_child_link | serialized | 1 | True |
| 2628 | 27 | faq_child_repeater_0_text | plain | 1 | True |
| 7278 | 663 | _elementor_data | json | 1 | True |
| 214 | 99 | ext_link | serialized | 1 | True |

## Skipped by the map

- http://www.markheardfuel.com/?utm_campaign=gmb: URL has a query string; parameter redirects are handled by the app, not content links
- https://www.markheardfuel.com/: http:// or www. host variant; expected canonical redirect
- http://www.markheardfuel.com/: http:// or www. host variant; expected canonical redirect
- http://markheardfuel.com/: http:// or www. host variant; expected canonical redirect

## wp_options still referencing old URLs (16, not changed)

See `2026-10-30-1002-fix-redirect-links-live-options.md` next to this log. Widgets, theme mods, menus and plugin settings live here and need a hand or a different skill.

## Rollback

Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.
Postmeta: previous values are in the same backup file.
