# Handoff: fix-redirect-links

Status as of 2026-10-29. Read this at the start of the chat dedicated to this skill. The repo is the source of truth: github.com/graterdigital/Low-Hanging-Fruit, cloned on Greg's PC at `C:\Users\greg\Documents\Low-Hanging-Fruit`. Mirror of the project doc `claude/skill-fix-redirect-links.md`; update both.

## What the skill does

Rewrites internal links that point at redirecting URLs so they point straight at the final page. AUTO tier (changes nothing a visitor reads), but always dry-run on staging first. It does not create or edit redirect rules, and it never writes to `wp_options`.

## Where it lives

- `skills/fix-redirect-links/SKILL.md`: the procedure (how to build the redirect map from Ahrefs, what to skip, run order, rollback).
- `scripts/fix_redirect_links.py`: local runner. Reads `clients/<slug>.yaml` for SSH aliases and `hosting.provider`, ships the PHP over SSH, writes the change logs, runs `wp cache flush` after an apply. Flags: `--probe` (locate occurrences, change nothing), default dry run, `--apply`, `--target live` (asks you to type the slug), `--yes` (skips that prompt for vetted unattended runs; with no terminal and no `--yes` it aborts rather than hangs), `--webroot`.
- `scripts/php/replace_links.php`: runs inside WordPress via `wp eval-file -`. Anchored matching so `/child-support/` never matches inside `/divorce/child-support/`. Handles absolute, root-relative, JSON-escaped, and PHP-serialized (ACF link field) forms. Matches the live host, the host the install currently runs on (staging has its own domain), and `legacy_hosts` from the map. Uses `wp_update_post` so WordPress keeps a revision; postmeta is updated directly. Every mode also scans `wp_options` (anchored) and returns the hits under `options` for the report.
- `scripts/build_redirect_map.py`: builds the map from the Ahrefs API (`AHREFS_API_KEY` in `.env`), applying the SKILL.md swap/skip rules and HEAD-checking every target. Replaces the hand-made JSON; tested against the hsfamilylaw map (identical result) and setcom's rows.
- `scripts/batch_fix_redirect_links.py`: runs every client on a host through map → staging dry → staging apply (→ `--live`: live dry → live apply) with gates between steps; writes `changes/<provider>/_batch-<stamp>-...md`.
- `reports/<slug>/redirect-map-<crawl-date>.json`: per-site input. `swaps` (old → new), `skipped` (with reasons), `legacy_hosts`. The runner's `--map` now defaults to the newest one.
- `changes/<provider>/<slug>/<stamp>-fix-redirect-links-<target>-<mode>.md`: change log per run, grouped by host (`kinsta`, `wpengine`, `other`). Companion `<stamp>-fix-redirect-links-<target>-options.md`: `wp_options` rows that still contain an old URL or legacy host, with autoload flag, size and context. Report only; those are widgets, menus, theme mods and plugin settings to fix by hand. `changes/<provider>/<slug>/backup/*.json` holds full before/after content (git-ignored).

## Pilot: hsfamilylaw.com

- Map: 9 swaps from the 2026-10-08 crawl's "3XX redirect" issue, 1 legacy host (`hswlaw.wpengine.com`, the firm's previous WP Engine install, still linked from FAQ fields). Skipped: 5 old URLs that redirect to the homepage (need real targets), `/podcast/` (intentional, off-site), `/page/1/` links (theme pagination template), author archives (Yoast sitemap setting), host variants.
- Dry run on fresh staging 2026-10-29 morning: 8 posts, 55 postmeta rows, 79 replacements. Applied to staging same day, identical counts, no errors. Greg spot-checked pages and links: good. Logs in `changes/kinsta/hsfamilylaw/` (2026-10-28 and 2026-10-29 dry runs, 2026-10-29-1040 apply).
- A second staging dry run after the script changes (2026-10-29-1118) returned 0 / 0: idempotent, as expected on an already-applied copy.
- **Live applied 2026-10-29 11:30** (`2026-10-29-1130-fix-redirect-links-live-apply.md`): 8 posts, 55 postmeta rows, 79 replacements, all `applied: True`, cache flush ok, 0 `wp_options` hits. Totals: 25 legacy-host links, 18 `/contact-us` slash fixes, 15 guardian-ad-litem, 13 collaborative-divorce, 2+2 collaborative-divorce-attorney (incl. the chain), 1 each child-custody, child-support, divorce-process, mediate.
- Verified from outside right after: `/divorce/child-support/` serves fixed links. `/2026-child-support/` (post 5553, 2 replacements applied) still served the old `/child-support/` and `/child-custody/` hrefs minutes later: Kinsta edge cache; DB confirmed changed via the apply log. Re-check after the cache clears.
- That post also still links `/modifications/`, one of the 5 homepage-redirect URLs on the skipped list; first concrete item for `redirect-rules`.
- **Verified by the 2026-10-29 crawl** (same day): "Page has links to redirect" 39 → 31, "3XX redirect" 28 → 21, "Redirect chain" 1 → 0. The 31 that remain are 25 paginated archives (template `/page/1/` fix) and 6 content pages that link to skipped-list URLs: home (`/podcast/`), `/2026-child-support/` (`/modifications/`), `/understanding-roles-collaborative-divorce-team/` (pasted file path), `/family-law/`, `/co-parenting-schedules-summer-break/`, `/needs-mediation-attorneys/` (the homepage-redirect URLs). `build_redirect_map.py` run against this crawl produces 0 swaps / 21 skipped, all for the expected reasons; that map (`redirect-map-2026-10-29.json`) is the current one, so the batch reports the site as nothing to do.

## Kinsta stage-only batch, 2026-10-29 14:33 (`changes/kinsta/_batch-2026-10-29-1433-fix-redirect-links-stage.md`)

13 client files, 8 staged, 4 nothing to do (fenceworks ×2, hsfamilylaw, ruggeddepot), nativecustomstone needs staging. Mechanics held up: no prompts, no hangs, all gates and logs behaved. Reading the results exposed three builder/matcher problems, all fixed the same afternoon, **and left miuraboiler staging corrupted**:

- **miuraboiler**: the map contained `https://miuraboiler.com/rep-locator/\` (a link typo on the site that Ahrefs reports as a redirecting URL). The matcher took the backslash as part of the path, matched the escaping backslash of JSON-encoded links (`\"/rep-locator/\"`) 30 times, and the rewrite removed it, producing invalid JSON in Elementor data. **Staging only. Restore it with `restore_changes.py` from `changes/kinsta/miuraboiler/backup/2026-10-29-1438-fix-redirect-links-staging.json`, rebuild the map (the builder now skips such URLs), then re-stage.** Then `--check-json` must report 0 invalid.
- **ruggeddepot**: `/repair-and-support/` → `/services/` (6,341 incoming links, a sitewide template link) was skipped because the HEAD verify got a 403 from the site's bot protection. Builder now trusts Ahrefs' 200 on 403/405/429/503 and notes it. Rebuild the map; expect 1 swap. The crawl really does have only 6 redirecting URLs now.
- **apply counts > dry counts** (miuraboiler 35 → 60 meta, setcomcorp 111 → 115): `wp_update_post` in the posts pass created revisions, and Elementor copies `_elementor_data` into revisions, so the meta pass then found and rewrote those copies. Harmless but wrong. The meta pass now runs first and ignores revision rows.

Other notes from the run: atlantaspecializedcare is ACF-heavy (748 meta rows for 33 swaps, chains collapsed correctly); forwardfacing's hits are all in meta (0 posts); markheardfuel (Elementor) 12p/71m applied cleanly on staging but has 16 `wp_options` hits (widgets/theme settings to fix by hand); meshautomationinc has 15 query-string redirects skipped and 7 homepage redirects for a human; setcomcorp 13 swaps incl. three menu-level slash fixes; technikpackaging's canonical host is `www`. Elementor sites staged (markheardfuel, setcomcorp, miuraboiler, meshautomationinc is ACF/Elementor?) need `--check-json` run before any of them go live.

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

- Second site: one on WP Engine (webroot `sites/<install>`, path logic exists but is untested) and one with a page builder (Elementor stores content as JSON in `_elementor_data`; the JSON-escaped rules should cover it but it has not been exercised).
- Builder-aware handling if Elementor data turns out to need it.
- `restore_changes.py` exists now; first real use is miuraboiler staging.
- Kinsta batch: stage-only run done (see above). Before live: restore + re-stage miuraboiler, rebuild ruggeddepot's map, `--check-json` on every Elementor staging, set up staging for nativecustomstone (86 swaps waiting), fix setcomcorp's live SSH port (37782 times out; staging works).
- setcomcorp live SSH alias: port 37782 timed out on 2026-10-29; get the current port from MyKinsta.
- Once a few batch cycles are clean, schedule `--live` as a task.

## Related work that is NOT this skill

- `redirect-rules` (APPROVE): give the 4 homepage-redirect URLs real targets (`/modifications/`, `/family-law/alimony-modification/`, `/mediation/mediation-faqs/`, `/collaborative-divorce-attorney/basics-collaborative-approach/`) and fix the links on the 5 pages above; the chain is already gone.
- Template fixes (theme diffs, by hand): archive `<h1>`, pagination `/page/1/`.
- `indexation-review` (APPROVE): Yoast author sitemap, thin archive noindex.
- Options cleanup (by hand, from the `-options.md` log): widgets, menus, theme settings still carrying old links.
