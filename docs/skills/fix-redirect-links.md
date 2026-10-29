# Handoff: fix-redirect-links

Status as of 2026-10-29. Read this at the start of the chat dedicated to this skill. The repo is the source of truth: github.com/graterdigital/Low-Hanging-Fruit, cloned on Greg's PC at `C:\Users\greg\Documents\Low-Hanging-Fruit`. Mirror of the project doc `claude/skill-fix-redirect-links.md`; update both.

## What the skill does

Rewrites internal links that point at redirecting URLs so they point straight at the final page. AUTO tier (changes nothing a visitor reads), but always dry-run on staging first. It does not create or edit redirect rules, and it never writes to `wp_options`.

## Where it lives

- `skills/fix-redirect-links/SKILL.md`: the procedure (how to build the redirect map from Ahrefs, what to skip, run order, rollback).
- `scripts/fix_redirect_links.py`: local runner. Reads `clients/<slug>.yaml` for SSH aliases and `hosting.provider`, ships the PHP over SSH, writes the change logs, runs `wp cache flush` after an apply. Flags: `--probe` (locate occurrences, change nothing), default dry run, `--apply`, `--target live` (asks you to type the slug), `--yes` (skips that prompt for vetted unattended runs; with no terminal and no `--yes` it aborts rather than hangs), `--webroot`.
- `scripts/php/replace_links.php`: runs inside WordPress via `wp eval-file -`. Anchored matching so `/child-support/` never matches inside `/divorce/child-support/`. Handles absolute, root-relative, JSON-escaped, and PHP-serialized (ACF link field) forms. Matches the live host, the host the install currently runs on (staging has its own domain), and `legacy_hosts` from the map. Uses `wp_update_post` so WordPress keeps a revision; postmeta is updated directly. Every mode also scans `wp_options` (anchored) and returns the hits under `options` for the report.
- `reports/<slug>/redirect-map-<crawl-date>.json`: per-site input. `swaps` (old → new), `skipped` (with reasons), `legacy_hosts`.
- `changes/<provider>/<slug>/<stamp>-fix-redirect-links-<target>-<mode>.md`: change log per run, grouped by host (`kinsta`, `wpengine`, `other`). Companion `<stamp>-fix-redirect-links-<target>-options.md`: `wp_options` rows that still contain an old URL or legacy host, with autoload flag, size and context. Report only; those are widgets, menus, theme mods and plugin settings to fix by hand. `changes/<provider>/<slug>/backup/*.json` holds full before/after content (git-ignored).

## Pilot: hsfamilylaw.com

- Map: 9 swaps from the 2026-10-08 crawl's "3XX redirect" issue, 1 legacy host (`hswlaw.wpengine.com`, the firm's previous WP Engine install, still linked from FAQ fields). Skipped: 5 old URLs that redirect to the homepage (need real targets), `/podcast/` (intentional, off-site), `/page/1/` links (theme pagination template), author archives (Yoast sitemap setting), host variants.
- Dry run on fresh staging 2026-10-29 morning: 8 posts, 55 postmeta rows, 79 replacements. Applied to staging same day, identical counts, no errors. Greg spot-checked pages and links: good. Those logs were written under the old `changes/hsfamilylaw/` path and are uncommitted on Greg's PC; move them to `changes/kinsta/hsfamilylaw/` before committing.
- The script changed after that run (log layout, cache flush, options scan, `--yes`), so re-run the staging dry run once before live: `python scripts\fix_redirect_links.py hsfamilylaw --map reports\hsfamilylaw\redirect-map-2026-10-08.json`. Counts should match the morning (8 / 55 / 79); read the new `-options.md` too.
- Live run: pending. `python scripts\fix_redirect_links.py hsfamilylaw --map reports\hsfamilylaw\redirect-map-2026-10-08.json --target live --apply`, then commit `changes/`.
- After live: trigger an Ahrefs recrawl; "Page has links to redirect" should drop from 39 to roughly the 24 paginated archives, which belong to the template fix.

## Things learned the hard way (already encoded in the script)

1. Kinsta rewrites every absolute URL to the staging domain when it builds staging, so a matcher that only knows the live domain finds half the links.
2. This site uses ACF Pro with the classic editor: most links live in postmeta, as WYSIWYG HTML or serialized link arrays, not in post_content.
3. `wp eval-file` includes the file inside a function, so top-level variables must be declared `global` or helper functions see nothing.
4. PHP encodes an empty array as a JSON list; the runner tolerates that.
5. A rebuilt Kinsta staging gets a new host key on the same port; `ssh-keygen -R "[ip]:port"` clears the warning.
6. Per-site probe before dry run. It found the legacy host and the storage forms the first dry run missed.
7. The probe/options find-regex originally rejected any word character before the path, which blocked `hsfamilylaw.com/contact-us` as well as `/divorce/contact-us`, so the probe only ever saw root-relative links. Now `find_re()` allows an optional `scheme://host` prefix and rejects a trailing `/`, so `/contact-us` no longer matches its own fixed form `/contact-us/`. Transients are excluded from the options report.
8. Postmeta is written straight to the table, so a persistent object cache (Kinsta Redis, WP Engine) keeps serving old ACF values until `wp cache flush`. The runner flushes after every apply and records the result in the log.

## Open items for this skill

- Re-run staging dry run, then live on hsfamilylaw, then verify with a recrawl.
- Second site: one on WP Engine (webroot `sites/<install>`, path logic exists but is untested) and one with a page builder (Elementor stores content as JSON in `_elementor_data`; the JSON-escaped rules should cover it but it has not been exercised).
- Builder-aware handling if Elementor data turns out to need it.
- A restore script for bulk rollback from the backup JSON (today: per-post revisions, or ask for one).
- Consider having the skill build the redirect map itself from Ahrefs instead of a hand-made JSON; the rules for swap vs. skip are already written in SKILL.md.
- Once a few live runs are clean, schedule it with `--yes`.

## Related work that is NOT this skill

- `redirect-rules` (APPROVE): fix the 5 homepage-redirect URLs and collapse chains in the Redirection plugin.
- Template fixes (theme diffs, by hand): archive `<h1>`, pagination `/page/1/`.
- `indexation-review` (APPROVE): Yoast author sitemap, thin archive noindex.
- Options cleanup (by hand, from the `-options.md` log): widgets, menus, theme settings still carrying old links.
