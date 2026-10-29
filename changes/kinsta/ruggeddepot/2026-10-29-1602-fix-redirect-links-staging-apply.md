# fix-redirect-links: ruggeddepot.com (staging)

Run 2026-10-29-1602 · mode **apply** · alias `ruggeddepot-staging` · provider `kinsta` · map `redirect-map-2026-10-29.json`

Install host `stg-ruggeddepot-rdstaging.kinsta.cloud`; hosts matched: `ruggeddepot.com`, `stg-ruggeddepot-rdstaging.kinsta.cloud`. Entries starting `host:` are legacy-host links moved to the current host.

Object cache flush after apply: ok (`Success: All caches were cleared. Changes usually appear globally within a few minutes.`)

## Totals (replacements per old URL)

- `https://ruggeddepot.com/repair-and-support/` → 1

## Posts changed (0)

| ID | type | title | URL | replacements | applied |
|---|---|---|---|---|---|

## Postmeta changed (1)

| meta_id | post | key | kind | replacements | applied |
|---|---|---|---|---|---|
| 498172 | 31 | blocks_9_services_links_2_link | serialized | 1 | True |

## Skipped by the map

- https://ruggeddepot.com/get-a-custom-quote/: no incoming internal links (sitemap or orphan entry); nothing in content to rewrite
- http://ruggeddepot.com/: http:// or www. host variant; expected canonical redirect
- https://ruggeddepot.com/product/panasonic-cf-339w045bm/: no incoming internal links (sitemap or orphan entry); nothing in content to rewrite
- http://www.ruggeddepot.com/: http:// or www. host variant; expected canonical redirect
- https://www.ruggeddepot.com/: http:// or www. host variant; expected canonical redirect
- https://ruggeddepot.com/our-team/: no incoming internal links (sitemap or orphan entry); nothing in content to rewrite

## wp_options still referencing old URLs (0, not changed)

None found.

## Rollback

Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.
Postmeta: previous values are in the same backup file.
