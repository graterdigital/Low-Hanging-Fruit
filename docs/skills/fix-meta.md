# Handoff: fix-meta

Status as of 2026-11-02 (afternoon): **built, v1. Probe run on hsfamilylaw against the 2026-10-29 crawl; 22-row queue with drafts in `reports/hsfamilylaw/meta-2026-10-29.md`. Nothing pushed to the sheet, nothing written to the site.** `--sheet`, `--fix` and `--rollback` are written to the existing patterns but have not been run against a real sheet or server yet; the PHP is lint-clean but untested in WordPress. Mirror of the project doc `claude/skill-fix-meta.md`; update both.

## Purpose

Write missing or weak SEO titles and meta descriptions through the SEO plugin, with every piece of text reviewed by a human before it goes live. APPROVE tier always (searchers read this text; the law-firm client rule `visible_copy_changes: approve` applies to all clients here). Highest traffic impact of anything in Phase 1.

## Files

- `skills/fix-meta/SKILL.md`: the procedure, the drafting standard, run order, rollback.
- `scripts/fix_meta.py`: `--probe [--draft] [--max-pages N] [--cache]`, `--sheet`, `--fix [--apply] [--target live] [--yes]`, `--rollback <backup.json> [--apply]`. Reuses `build_redirect_map` (`load_env`, `ahrefs`, `wpengine_webroot`) and `review_sheets.gc`. Cache dir `tmp/ahrefs-cache/<slug>/` (same `Api` class as ai_discoverability).
- `scripts/php/set_meta.php`: Yoast writer, `wp eval-file -` with `META_JOB`; path-based URL→post lookup (copied from set_article_type); `before/after` per field; `rendered_title`/`rendered_description` from `YoastSEO()->meta->for_post()` (dry = current, apply = new, so the log shows whether Yoast adds its template suffix to a literal title); rebuilds the post's indexable after an apply; prints after `===JSON===`.
- `reports/<slug>/meta-<crawl>.md` + `.json` (queue; the JSON is what `--sheet` pushes), `reports/<slug>/meta-drafts.json` (hand drafts, keyed by path).
- Logs `changes/<provider>/<slug>/<stamp>-fix-meta-<target>-<dry|apply>.md`, backups `backup/<stamp>-fix-meta-<target>.json`, rollback logs `-rollback-<mode>.md`. Rollback lives in fix_meta.py (same pattern as `--rollback-article`), not in `restore_changes.py`; two meta keys did not justify extending the links restore.

## What the build found (changes from the spec)

- **Issue ids are read by name**, not hard-coded: this project has no "Duplicate titles"/"Duplicate meta descriptions" issues at all; duplicates come from the `duplicate_*_canonical_hreflang` columns on flagged pages instead. Indexable variants only (`is_indexable` true).
- **GSC `ctr` from the Ahrefs API is a percentage** (1.7475 = 1.75 %), not a fraction. Queue score is `impressions × (1 − ctr/100)`.
- **Most "Page and SERP titles do not match" rows are not defects.** On hsfamilylaw 15 of 25 are Google dropping the ` - Hastings Shadmehry` suffix, plus the homepage where Google leads with the brand. The probe classifies each row (`brand dropped`, `truncated`, `brand moved first`, `used as-is` = no action; `rewritten to H1`, `stale year`, `brand typo`, `glued`, `rewritten` = propose). Only 6 titles get a proposal here.
- **The brand suffix is ` - Hastings Shadmehry` (hyphen), not `|`** as the spec guessed; detected from a 100-title sample (most common tail after the last separator, ≥3 occurrences). Override with `meta.brand_suffix` / `meta.separator` in the client file. Three posts use `|` instead; left alone.
- **Page text needs trimming**: Ahrefs' `page_text_md` carries the whole nav, the reviews widget and the footer. `main_text()` starts at the first H1 and stops at Reviews/Testimonials/Let's Get Started/Contact Us/Useful Links-style headings. Bios on this site have a role line right under the H1 and an "Areas of Practice" list, which the bio template reads.
- **Drafts need a human or a model.** The build chat drafted all 18 descriptions and 7 titles by hand from the live pages into `reports/hsfamilylaw/meta-drafts.json`; the probe merges that file first, then `--draft` (Anthropic API, `ANTHROPIC_API_KEY` in `.env`, model `LHF_DRAFT_MODEL`, default `claude-sonnet-5-5`), then the bio template. `--draft` is written but has not been run (no key on the build machine).
- **Stale year also hits the description**: `/how-much-does-a-divorce-cost-in-georgia-in-2026/` says 2025 in both; the probe swaps the year in the existing description automatically and the hand draft rewrote it anyway.

## hsfamilylaw queue (crawl 2026-10-29, GSC 2026-08-03 → 2026-11-01)

79 flagged URLs → 22 to write, 15 no action, 42 archives routed to `indexation-review`. Top of the queue by impressions × (1 − CTR): the 2026 divorce-cost post (16,107 impressions, 0.17 % CTR, stale 2025 in title and description), `/2026-child-support/` (Google shows the H1, drops "Updates & Info"), `/divorce/property-debt-division/` (suffix typo "Hasting"), then the six core pages and eleven bios without a description. Two more title fixes: `/mediation-attorneys-make-divorce-easier/` and `/divorce-mediation-helps-children/` (Google uses the H1), `/resource-links/` (two titles glued together). Rhonda Smith's bio is the only one whose title has no role; the hand draft adds "Senior Attorney".

## Next, in order

1. On Greg's PC: `python scripts\fix_meta.py hsfamilylaw --probe --cache` (real API; expect the same 22 rows, plus page text pulled for the drafts' `text_chars`). Then `--sheet` to create the `meta` tab and push the 22 rows.
2. Greg reviews in the sheet: copy a proposal into `new_*` where it is right, edit where not, `status` → `approved`.
3. `--fix` (staging dry): check `no post` rows and the `rendered` column (does Yoast append the brand to a literal title on this site?). Then `--fix --apply` on staging, view source on two pages, then `--fix --apply --target live`.
4. First real run of `--rollback` on staging against the staging backup, to prove it.
5. Ahrefs recrawl: "Meta description missing" 59 → 42 (archives remain). GSC CTR check after four weeks on the rewritten pages.
6. Second site on Yoast with a different builder (markheardfuel or setcomcorp, Elementor) to see whether bios/templates generalise; then an AIOSEO site (cmitsolutions) to decide whether a `wp_aioseo_posts` writer is worth it.

## Open items

- `--draft` untested end to end; first run with `--max-pages 3` on a site without hand drafts.
- `indexation-review` is now the gating skill for the 42 archive rows (Yoast taxonomy description template or noindex); the homepage title (Google leads with the brand) is a Yoast template decision, not a per-page write.
- Yoast templates as FLAG output (one change covers many pages) not built; the report routes archives but does not propose a template string.
- Sheet rows marked `applied` are skipped by later `--sheet` runs; a human clears them if the page needs another pass.
- `review_sheets.py status` does not count the `meta` tab yet.
