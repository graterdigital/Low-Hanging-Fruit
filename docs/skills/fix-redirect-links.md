# Handoff: fix-redirect-links

Status as of 2026-10-30. Read this at the start of the chat dedicated to this skill. The repo is the source of truth: github.com/graterdigital/Low-Hanging-Fruit, cloned on Greg's PC at `C:\Users\greg\Documents\Low-Hanging-Fruit`. Mirror of the project doc `claude/skill-fix-redirect-links.md`; update both.

## What the skill does

Rewrites internal links that point at redirecting URLs so they point straight at the final page. AUTO tier (changes nothing a visitor reads), but always dry-run on staging first. It does not create or edit redirect rules, and it never writes to `wp_options`.

## Where it lives

- `skills/fix-redirect-links/SKILL.md`: the procedure (how to build the redirect map from Ahrefs, what to skip, run order, rollback).
- `scripts/fix_redirect_links.py`: local runner. Reads `clients/<slug>.yaml` for SSH aliases and `hosting.provider`, ships the PHP over SSH, writes the change logs, runs `wp cache flush` after an apply. Flags: `--probe` (locate occurrences, change nothing), default dry run, `--apply`, `--target live` (asks you to type the slug), `--yes` (skips that prompt for vetted unattended runs; with no terminal and no `--yes` it aborts rather than hangs), `--webroot`.
- Post-apply link check (2026-10-30): every changed page is fetched and every internal link on it HEAD-checked; `-linkcheck.md` next to the log; the batch stops a site when a swap target is not 200. `--check-links` runs it alone. Menu rows are labelled `menu` in the log; whole-value URLs keep `#fragment`/`?query`.
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

## Kinsta live batch, 2026-10-30

After the stage-only run and its fixes (below), live went in three groups with `--live --no-stage --no-map`, two sites first, then five, then miuraboiler and setcomcorp singly. **9 of 11 Kinsta sites are done**:

| site | live p/m/r | notes |
|---|---|---|
| hsfamilylaw | 8/55/79 (10-29) | verified by recrawl |
| slepianfirm | 9/0/19 | staging is a rebuild, not a copy: `staging_is_copy_of_live: false` in the client file now; live dry run was the only gate |
| technikpackaging | 31/0/34 | |
| atlantaspecializedcare | 5/60/96 | staging said 748 meta rows: revision copies counted by the old code; the meta-first/no-revisions pass gives the true number |
| forwardfacing | 0/3/3 | |
| markheardfuel | 12/6/18 | Elementor; check-json on staging 0 invalid |
| meshautomationinc | 21/59/114 | |
| ruggeddepot | 0/44/64 | the 6,341-link `/repair-and-support/` swap vanished from the 10-29/30 crawl before we reached it; current map has 25 swaps |
| miuraboiler | 75/23/102 | Elementor; staging was stale (17 hits), live is the real number; run live check-json after apply |
| setcomcorp | 10/9/43 | live SSH needs the running machine's IP on the environment's allowlist (MyKinsta → Security); Elementor, run live check-json |

Re-run needed on the Elementor sites (markheardfuel, setcomcorp, miuraboiler, ruggeddepot, meshautomationinc) after the plain-JSON fix of 2026-10-30 (`--live --no-stage --no-map` is fine: the maps are current and the sites are idempotent). Left on Kinsta: **nativecustomstone** (86 swaps in the map, no staging; create one or run live-only with `--allow-no-staging` after reading the map). Options logs with real hits to hand over: markheardfuel (16 rows), setcomcorp (7), meshautomationinc (3), technikpackaging (2), forwardfacing, ruggeddepot (1 each): widgets/menus/theme settings carrying old links.

Verify next week: Ahrefs recrawls each project on its schedule; compare "Page has links to redirect" and "3XX redirect" against the 10-22/10-29 baselines in the first batch summary.

## Elementor re-run and the ACF-options finding, 2026-10-30 10:52

After the plain-JSON fix: miuraboiler 149p/126m/2,653 replacements (2,652 of them `www.`→bare host moves), setcomcorp 1p/7m/12r, ruggeddepot 0p/10m/10r, meshautomationinc clean, markheardfuel only 1 move. All Elementor JSON valid on live. markheardfuel's 15 remaining old links turned out to be **ACF options-page fields** (`options_proudly_serving_repeater_*_link`: the footer service-area list), the one storage form the script was told never to write. Since ACF options are client-edited content exactly like ACF postmeta, the matcher now rewrites `options_*` rows with the same serialized walk, backup, JSON guard and restore; all other `wp_options` rows stay report-only. **Re-run markheardfuel live** to pick them up; expect ~15 ACF option rows. miuraboiler's "LINK CHECK FAILED" after that run was the edge cache still serving old HTML; re-run `--check-links` after a few minutes.

## Late 2026-10-30: ACF options, GSC, onboarding

- markheardfuel's 15 footer/CTA links were ACF options-page fields; the 10:52 live run rewrote them (backup has 11 `proudly_serving` rows + 4 others), the apply log's ACF section didn't print (cosmetic, parked). Site verified correct. Options report now 1 row (shortcode plugin memory).
- GSC columns in the map (`gsc_clicks_90d`, `gsc_impressions_90d`, pulled through the Ahrefs project when `gsc_connected: yes`) order the skipped list; hsfamilylaw: 107 GSC pages, 0 skipped URLs with impressions.
- Answer to "new site = add to Ahrefs and run?": nearly. Still needs a client file; `new_client.py <domain>` is the next build so that becomes true (plan.md). Then `redirect-rules` (APPROVE, GSC-driven) for the homepage-redirect leftovers.

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
- nativecustomstone: staging or live-only run (86 swaps).
- Hand over the options logs listed above.
- Next host: WP Engine (22 client files, webroot `sites/<install>` untested). Same rhythm: stage-only batch, read the summary, live.
- Gate gap found 2026-10-30: `--live --no-stage` has no staging counts to compare against, so the live/staging mismatch gate is silent in that mode. Acceptable while a human reads the table; before scheduling, make the batch read the latest staging dry-run log for the comparison.
- Once a few batch cycles are clean, schedule `--live` as a task.

## Related work that is NOT this skill

- `redirect-rules` (APPROVE): give the 4 homepage-redirect URLs real targets (`/modifications/`, `/family-law/alimony-modification/`, `/mediation/mediation-faqs/`, `/collaborative-divorce-attorney/basics-collaborative-approach/`) and fix the links on the 5 pages above; the chain is already gone.
- Template fixes (theme diffs, by hand): archive `<h1>`, pagination `/page/1/`.
- `indexation-review` (APPROVE): Yoast author sitemap, thin archive noindex.
- Options cleanup (by hand, from the `-options.md` log): widgets, menus, theme settings still carrying old links.
