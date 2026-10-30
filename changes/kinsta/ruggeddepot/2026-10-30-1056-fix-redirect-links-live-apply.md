# fix-redirect-links: ruggeddepot.com (live)

Run 2026-10-30-1056 · mode **apply** · alias `ruggeddepot` · provider `kinsta` · map `redirect-map-2026-10-29.json`

Install host `ruggeddepot.com`; hosts matched: `ruggeddepot.com`, `www.ruggeddepot.com`. Entries starting `host:` are legacy-host links moved to the current host.

Object cache flush after apply: ok (`Success: All caches were cleared. Changes usually appear globally within a few minutes.`)

## Totals (replacements per old URL)

- `https://ruggeddepot.com/product-category/getac/s410-laptops-getac/` → 4
- `https://ruggeddepot.com/product-category/getac/ux10/` → 2
- `https://ruggeddepot.com/product-category/panasonic/toughbook-55/` → 3
- `https://ruggeddepot.com/product-category/vehicle-equipment/vehicle-mounts-vehicle-equipment/` → 1

## Posts changed (0)

| ID | type | title | URL | replacements | applied |
|---|---|---|---|---|---|

## Postmeta changed (10)

| meta_id | post | key | kind | replacements | applied |
|---|---|---|---|---|---|
| 1197297 | 41821 | _wc_order_attribution_session_entry | plain | 1 | True |
| 2907610 | 49883 | blocks_0_jump_to_content_12_cards_2_link | serialized | 1 | True |
| 2907620 | 49883 | blocks_0_jump_to_content_12_cards_3_link | serialized | 1 | True |
| 2910339 | 49883 | blocks_0_jump_to_content_10_cards_2_link | serialized | 1 | True |
| 2938888 | 50071 | blocks_0_jump_to_content_9_cards_2_link | serialized | 1 | True |
| 2946054 | 50071 | blocks_0_jump_to_content_11_cards_2_link | serialized | 1 | True |
| 2946064 | 50071 | blocks_0_jump_to_content_11_cards_3_link | serialized | 1 | True |
| 4265571 | 57036 | handl_original_ref | plain | 1 | True |
| 4265578 | 57036 | organic_source | plain | 1 | True |
| 4268015 | 57058 | handl_ref | plain | 1 | True |

## Skipped by the map

- https://ruggeddepot.com/featured/: target https://ruggeddepot.com/shop returned 403 on verify, expected 200; check the redirect rule (APPROVE)
- https://ruggeddepot.com/get-a-custom-quote/: no incoming internal links (sitemap or orphan entry); nothing in content to rewrite
- http://ruggeddepot.com/: http:// or www. host variant; expected canonical redirect
- https://ruggeddepot.com/product/panasonic-cf-339w045bm/: no incoming internal links (sitemap or orphan entry); nothing in content to rewrite
- http://www.ruggeddepot.com/: http:// or www. host variant; expected canonical redirect
- https://www.ruggeddepot.com/: http:// or www. host variant; expected canonical redirect
- https://ruggeddepot.com/our-team/: no incoming internal links (sitemap or orphan entry); nothing in content to rewrite

## wp_options still referencing old URLs (1, not changed)

See `2026-10-30-1056-fix-redirect-links-live-options.md` next to this log. Widgets, theme mods, menus and plugin settings live here and need a hand or a different skill.

## Rollback

Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.
Postmeta: previous values are in the same backup file.
