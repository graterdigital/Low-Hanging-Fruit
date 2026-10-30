# fix-redirect-links: markheardfuel.com (live)

Run 2026-10-30-1052 · mode **apply** · alias `markheardfuel` · provider `kinsta` · map `redirect-map-2026-10-29.json`

Install host `markheardfuel.com`; hosts matched: `markheardfuel.com`, `www.markheardfuel.com`. Entries starting `host:` are legacy-host links moved to the current host.

Object cache flush after apply: ok (`Success: All caches were cleared. Changes usually appear globally within a few minutes.`)

## Totals (replacements per old URL)

- `host:www.markheardfuel.com` → 1

## Posts changed (1)

| ID | type | title | URL | replacements | applied |
|---|---|---|---|---|---|
| 955 | brb_collection | Mark Heard Fuel Co | https://markheardfuel.com/blog/brb_collection/955 | 1 | True |

## Postmeta changed (0)

| meta_id | post | key | kind | replacements | applied |
|---|---|---|---|---|---|

## Skipped by the map

- http://www.markheardfuel.com/?utm_campaign=gmb: URL has a query string; parameter redirects are handled by the app, not content links
- https://www.markheardfuel.com/: http:// or www. host variant; expected canonical redirect
- http://www.markheardfuel.com/: http:// or www. host variant; expected canonical redirect
- http://markheardfuel.com/: http:// or www. host variant; expected canonical redirect

## wp_options still referencing old URLs (16, not changed)

See `2026-10-30-1052-fix-redirect-links-live-options.md` next to this log. Widgets, theme mods, menus and plugin settings live here and need a hand or a different skill.

## Rollback

Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.
Postmeta: previous values are in the same backup file.
