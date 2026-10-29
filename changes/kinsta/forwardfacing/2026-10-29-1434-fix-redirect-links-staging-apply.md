# fix-redirect-links: forwardfacing.com (staging)

Run 2026-10-29-1434 · mode **apply** · alias `forwardfacing-staging` · provider `kinsta` · map `redirect-map-2026-10-29.json`

Install host `stg-forwardfacingpodcast-stgforward.kinsta.cloud`; hosts matched: `forwardfacing.com`, `stg-forwardfacingpodcast-stgforward.kinsta.cloud`. Entries starting `host:` are legacy-host links moved to the current host.

Object cache flush after apply: ok (`Success: All caches were cleared. Changes usually appear globally within a few minutes.`)

## Totals (replacements per old URL)

- `https://forwardfacing.com/episodes` → 12
- `https://forwardfacing.com/resources/` → 3

## Posts changed (0)

| ID | type | title | URL | replacements | applied |
|---|---|---|---|---|---|

## Postmeta changed (15)

| meta_id | post | key | kind | replacements | applied |
|---|---|---|---|---|---|
| 17 | 24 | _menu_item_url | plain | 1 | True |
| 26262 | 3258 | _menu_item_url | plain | 1 | True |
| 37806 | 3778 | full_width_image_description | plain | 1 | True |
| 75129 | 9211 | recent_episodes_button | serialized | 1 | True |
| 75847 | 9239 | recent_episodes_button | serialized | 1 | True |
| 76113 | 9244 | recent_episodes_button | serialized | 1 | True |
| 76245 | 9247 | recent_episodes_button | serialized | 1 | True |
| 76374 | 9248 | recent_episodes_button | serialized | 1 | True |
| 76554 | 9255 | recent_episodes_button | serialized | 1 | True |
| 76682 | 9256 | recent_episodes_button | serialized | 1 | True |
| 76814 | 9258 | recent_episodes_button | serialized | 1 | True |
| 76944 | 9260 | recent_episodes_button | serialized | 1 | True |
| 77095 | 9264 | recent_episodes_button | serialized | 1 | True |
| 77163 | 9266 | full_width_image_description | plain | 1 | True |
| 77193 | 9267 | full_width_image_description | plain | 1 | True |

## Skipped by the map

- http://forwardfacing.com/: http:// or www. host variant; expected canonical redirect
- http://www.forwardfacing.com/: http:// or www. host variant; expected canonical redirect
- https://www.forwardfacing.com/: http:// or www. host variant; expected canonical redirect

## wp_options still referencing old URLs (1, not changed)

See `2026-10-29-1434-fix-redirect-links-staging-options.md` next to this log. Widgets, theme mods, menus and plugin settings live here and need a hand or a different skill.

## Rollback

Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.
Postmeta: previous values are in the same backup file.
