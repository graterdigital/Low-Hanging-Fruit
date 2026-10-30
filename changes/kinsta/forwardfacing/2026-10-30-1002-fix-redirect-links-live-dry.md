# fix-redirect-links: forwardfacing.com (live)

Run 2026-10-30-1002 · mode **dry** · alias `forwardfacing` · provider `kinsta` · map `redirect-map-2026-10-29.json`

Install host `forwardfacing.com`; hosts matched: `forwardfacing.com`. Entries starting `host:` are legacy-host links moved to the current host.

## Totals (replacements per old URL)

- `https://forwardfacing.com/episodes` → 2
- `https://forwardfacing.com/resources/` → 1

## Posts changed (0)

| ID | type | title | URL | replacements | applied |
|---|---|---|---|---|---|

## Postmeta changed (3)

| meta_id | post | key | kind | replacements | applied |
|---|---|---|---|---|---|
| 17 | 24 | _menu_item_url | plain | 1 | - |
| 26262 | 3258 | _menu_item_url | plain | 1 | - |
| 37806 | 3778 | full_width_image_description | plain | 1 | - |

## Skipped by the map

- http://forwardfacing.com/: http:// or www. host variant; expected canonical redirect
- http://www.forwardfacing.com/: http:// or www. host variant; expected canonical redirect
- https://www.forwardfacing.com/: http:// or www. host variant; expected canonical redirect

## wp_options still referencing old URLs (1, not changed)

See `2026-10-30-1002-fix-redirect-links-live-options.md` next to this log. Widgets, theme mods, menus and plugin settings live here and need a hand or a different skill.

## Rollback

Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.
Postmeta: previous values are in the same backup file.
