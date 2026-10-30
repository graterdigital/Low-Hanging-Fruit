# fix-redirect-links: setcomcorp.com (live)

Run 2026-10-30-1029 · mode **apply** · alias `setcomcorp` · provider `kinsta` · map `redirect-map-2026-10-28.json`

Install host `setcomcorp.com`; hosts matched: `setcomcorp.com`. Entries starting `host:` are legacy-host links moved to the current host.

Object cache flush after apply: ok (`PHP Warning:  Constant WP_CACHE already defined in phar:///usr/local/bin/wp/vendor/wp-cli/wp-cli/php/WP_CLI/Runner.php(1334) : eval()'d code on line 24`)

## Totals (replacements per old URL)

- `https://setcomcorp.com/2025-police-motorcycle-training-events/` → 4
- `https://setcomcorp.com/about` → 2
- `https://setcomcorp.com/dealers` → 2
- `https://setcomcorp.com/industry/drilling` → 10
- `https://setcomcorp.com/industry/drone-operations` → 10
- `https://setcomcorp.com/police-motorcycle-rodeo-course-maps` → 2
- `https://setcomcorp.com/portable-radio-adapter-cables` → 2
- `https://setcomcorp.com/products/accessories/headset-strap-extension` → 4
- `https://setcomcorp.com/products/systems/1600/` → 2
- `https://setcomcorp.com/radio-designator-list` → 2
- `https://setcomcorp.com/warranty` → 3

## Posts changed (10)

| ID | type | title | URL | replacements | applied |
|---|---|---|---|---|---|
| 291 | elementor_library | Main Header | https://setcomcorp.com/?elementor_library=elementor-header-291 | 2 | True |
| 335 | elementor_library | Setcom Footer | https://setcomcorp.com/?elementor_library=setcom-footer | 3 | True |
| 3243 | elementor_library | Grid Layout (Industry / Products) | https://setcomcorp.com/?elementor_library=grid-layout-industry-products | 4 | True |
| 97 | page | Industry | https://setcomcorp.com/industry/ | 4 | True |
| 1229 | page | LiberatorMAX | https://setcomcorp.com/products/headsets/liberatormax/ | 1 | True |
| 1260 | page | Radio Cables | https://setcomcorp.com/products/accessories/radio-cables/ | 2 | True |
| 3093 | page | Incident Command | https://setcomcorp.com/industry/incident-command/ | 1 | True |
| 5104 | page | Come See Us At World of Concrete | https://setcomcorp.com/come-see-us-at-world-of-concrete/ | 2 | True |
| 5187 | page | Territories Page | https://setcomcorp.com/territories/ | 4 | True |
| 1606 | post | Police Motorcycle Rodeo Course Maps | https://setcomcorp.com/police-motorcycle-rodeo-course-maps/ | 1 | True |

## Postmeta changed (9)

| meta_id | post | key | kind | replacements | applied |
|---|---|---|---|---|---|
| 2444 | 335 | _elementor_data | json | 3 | True |
| 79663 | 97 | _elementor_element_cache | json | 4 | True |
| 10593 | 1229 | _elementor_data | json | 1 | True |
| 79570 | 1229 | _elementor_element_cache | json | 1 | True |
| 79612 | 1260 | _elementor_element_cache | json | 2 | True |
| 26094 | 3093 | _elementor_data | json | 1 | True |
| 79717 | 5104 | _elementor_element_cache | json | 2 | True |
| 79834 | 5187 | _elementor_element_cache | json | 4 | True |
| 79585 | 1606 | _elementor_element_cache | json | 1 | True |

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

See `2026-10-30-1029-fix-redirect-links-live-options.md` next to this log. Widgets, theme mods, menus and plugin settings live here and need a hand or a different skill.

## Rollback

Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.
Postmeta: previous values are in the same backup file.
