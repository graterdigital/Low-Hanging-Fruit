# fix-redirect-links: markheardfuel.com (live)

Run 2026-10-30-1103 · mode **dry** · alias `markheardfuel` · provider `kinsta` · map `redirect-map-2026-10-29.json`

Install host `markheardfuel.com`; hosts matched: `markheardfuel.com`, `www.markheardfuel.com`. Entries starting `host:` are legacy-host links moved to the current host.

## Totals (replacements per old URL)


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

## ACF options-page fields changed (0)

| option_id | option_name | kind | replacements | applied |
|---|---|---|---|---|

## wp_options still referencing old URLs (1, not changed)

See `2026-10-30-1103-fix-redirect-links-live-options.md` next to this log. Widgets, theme mods, menus and plugin settings live here and need a hand or a different skill.

## Rollback

Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.
Postmeta and ACF options-page rows: previous values are in the same backup file; `scripts/restore_changes.py` restores all three.
