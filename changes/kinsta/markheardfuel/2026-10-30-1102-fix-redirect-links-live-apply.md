# fix-redirect-links: markheardfuel.com (live)

Run 2026-10-30-1102 · mode **apply** · alias `markheardfuel` · provider `kinsta` · map `redirect-map-2026-10-29.json`

Install host `markheardfuel.com`; hosts matched: `markheardfuel.com`, `www.markheardfuel.com`. Entries starting `host:` are legacy-host links moved to the current host.

Object cache flush after apply: ok (`Success: All caches were cleared. Changes usually appear globally within a few minutes.`)

## Totals (replacements per old URL)

- `https://markheardfuel.com/contact/` → 1
- `https://markheardfuel.com/faqs/propane-safety-faqs/` → 1
- `https://markheardfuel.com/privacy-policy/` → 1
- `https://markheardfuel.com/service-areas/alpharetta-ga-propane/` → 1
- `https://markheardfuel.com/service-areas/buford-ga-propane/` → 1
- `https://markheardfuel.com/service-areas/canton-ga-propane/` → 1
- `https://markheardfuel.com/service-areas/cumming-ga-propane-company/` → 1
- `https://markheardfuel.com/service-areas/dahlonega-ga-propane/` → 1
- `https://markheardfuel.com/service-areas/dawsonville-ga-propane/` → 1
- `https://markheardfuel.com/service-areas/gainesville-ga-propane/` → 1
- `https://markheardfuel.com/service-areas/jasper-ga-propane/` → 1
- `https://markheardfuel.com/service-areas/johns-creek-ga-propane/` → 1
- `https://markheardfuel.com/service-areas/milton-ga-propane/` → 1
- `https://markheardfuel.com/service-areas/roswell-ga-propane/` → 1
- `https://markheardfuel.com/services/new-account-setup/` → 1

## Posts changed (0)

| ID | type | title | URL | replacements | applied |
|---|---|---|---|---|---|

## Postmeta changed (0)

| meta_id | post | key | kind | replacements | applied |
|---|---|---|---|---|---|

## Skipped by the map

- http://www.markheardfuel.com/?utm_campaign=gmb: URL has a query string; parameter redirects are handled by the app, not content links
- https://www.markheardfuel.com/: http:// or www. host variant; expected canonical redirect
- http://www.markheardfuel.com/: http:// or www. host variant; expected canonical redirect
- http://markheardfuel.com/: http:// or www. host variant; expected canonical redirect

## ACF options-page fields changed (15)

| option_id | option_name | kind | replacements | applied |
|---|---|---|---|---|
| 244 | options_go_guarantee_link | serialized | 1 | True |
| 246 | options_go_guarantee_second_text | plain | 1 | True |
| 271 | options_privacy_policy_link | serialized | 1 | True |
| 279 | options_proudly_serving_repeater_0_link | serialized | 1 | True |
| 281 | options_proudly_serving_repeater_1_link | serialized | 1 | True |
| 299 | options_proudly_serving_repeater_10_link | serialized | 1 | True |
| 283 | options_proudly_serving_repeater_2_link | serialized | 1 | True |
| 285 | options_proudly_serving_repeater_3_link | serialized | 1 | True |
| 287 | options_proudly_serving_repeater_4_link | serialized | 1 | True |
| 289 | options_proudly_serving_repeater_5_link | serialized | 1 | True |
| 291 | options_proudly_serving_repeater_6_link | serialized | 1 | True |
| 293 | options_proudly_serving_repeater_7_link | serialized | 1 | True |
| 295 | options_proudly_serving_repeater_8_link | serialized | 1 | True |
| 297 | options_proudly_serving_repeater_9_link | serialized | 1 | True |
| 429 | options_safety_link | serialized | 1 | True |

## wp_options still referencing old URLs (1, not changed)

See `2026-10-30-1102-fix-redirect-links-live-options.md` next to this log. Widgets, theme mods, menus and plugin settings live here and need a hand or a different skill.

## Rollback

Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.
Postmeta and ACF options-page rows: previous values are in the same backup file; `scripts/restore_changes.py` restores all three.
