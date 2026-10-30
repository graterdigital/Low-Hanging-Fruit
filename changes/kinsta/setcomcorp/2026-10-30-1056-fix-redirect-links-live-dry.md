# fix-redirect-links: setcomcorp.com (live)

Run 2026-10-30-1056 · mode **dry** · alias `setcomcorp` · provider `kinsta` · map `redirect-map-2026-10-28.json`

Install host `setcomcorp.com`; hosts matched: `setcomcorp.com`, `www.setcomcorp.com`. Entries starting `host:` are legacy-host links moved to the current host.

## Totals (replacements per old URL)

- `host:www.setcomcorp.com` → 2
- `https://setcomcorp.com/2025-police-motorcycle-training-events/` → 1
- `https://setcomcorp.com/industry/drilling` → 3
- `https://setcomcorp.com/industry/drone-operations` → 3
- `https://setcomcorp.com/portable-radio-adapter-cables` → 1
- `https://setcomcorp.com/products/accessories/headset-strap-extension` → 1
- `https://setcomcorp.com/radio-designator-list` → 1

## Posts changed (1)

| ID | type | title | URL | replacements | applied |
|---|---|---|---|---|---|
| 1504 | page | Privacy | https://setcomcorp.com/privacy/ | 1 | - |

## Postmeta changed (7)

| meta_id | post | key | kind | replacements | applied |
|---|---|---|---|---|---|
| 22007 | 97 | _elementor_data | json | 2 | - |
| 10898 | 1260 | _elementor_data | json | 2 | - |
| 13444 | 1504 | _elementor_data | json | 1 | - |
| 14305 | 1606 | _elementor_data | json | 1 | - |
| 27376 | 3243 | _elementor_data | json | 2 | - |
| 47463 | 5104 | _elementor_data | json | 1 | - |
| 48458 | 5187 | _elementor_data | json | 2 | - |

## Skipped by the map

- https://setcomcorp.com/2026/10/21/: date archive redirecting to the homepage; not a content link
- https://setcomcorp.com/2026/06/22/: date archive redirecting to the homepage; not a content link
- https://setcomcorp.com/2026/06/04/: date archive redirecting to the homepage; not a content link
- https://setcomcorp.com/2026/05/04/: date archive redirecting to the homepage; not a content link
- https://www.setcomcorp.com/: http:// or www. host variant; expected canonical redirect
- https://setcomcorp.com/2026/10/07/: date archive redirecting to the homepage; not a content link
- https://setcomcorp.com/2026/05/18/: date archive redirecting to the homepage; not a content link
- https://setcomcorp.com/2026/01/09/: date archive redirecting to the homepage; not a content link
- https://setcomcorp.com/2026/01/28/: date archive redirecting to the homepage; not a content link
- https://setcomcorp.com/2026/09/10/: date archive redirecting to the homepage; not a content link
- https://setcomcorp.com/2026/09/24/: date archive redirecting to the homepage; not a content link
- https://setcomcorp.com/2026/10/16/: date archive redirecting to the homepage; not a content link
- http://setcomcorp.com/: http:// or www. host variant; expected canonical redirect
- http://www.setcomcorp.com/: http:// or www. host variant; expected canonical redirect

## wp_options still referencing old URLs (7, not changed)

See `2026-10-30-1056-fix-redirect-links-live-options.md` next to this log. Widgets, theme mods, menus and plugin settings live here and need a hand or a different skill.

## Rollback

Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.
Postmeta: previous values are in the same backup file.
