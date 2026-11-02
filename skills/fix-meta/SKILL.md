---
name: fix-meta
description: Write missing or weak SEO titles and meta descriptions on a WordPress site through the SEO plugin, with every piece of text reviewed by a human in the client's Google review sheet before it goes live. Use this whenever a triage report or Ahrefs lists "Meta description tag missing or empty", "Page and SERP titles do not match", "Title tag missing or empty", "Multiple title tags", duplicate titles or descriptions for a client site, or the user asks to fix, write, or improve titles, meta descriptions, or snippets. APPROVE tier, always: searchers read this text, so nothing is written that a human has not typed or approved.
---

# fix-meta

Titles and descriptions are the one piece of on-page text Google shows before the click, so this is the highest-traffic-impact fix in Phase 1 and also the one that is never automatic. The skill builds a prioritised queue from Ahrefs and Search Console, drafts text with a stated basis, puts it on the client's review sheet, and writes only the rows a human has approved.

## What you need

1. A client file `clients/<slug>.yaml` with `ahrefs.site_audit_project_id`, `platform.seo_plugin` (Yoast is the only writer in v1; AIOSEO sites get a queue for manual entry), `hosting.ssh_alias` and `hosting.staging_environment`, and `review.alt_sheet_id` (the client's review sheet; `python scripts/review_sheets.py setup <slug>` if missing). `ahrefs.gsc_connected: yes` makes the queue GSC-driven; without it the order falls back to Ahrefs traffic.
2. Optional per-client knobs under `meta:`: `brand_suffix` and `separator` when detection gets it wrong (the probe reports what it detected), `city` for templated bios.
3. `AHREFS_API_KEY` in `.env`; `ANTHROPIC_API_KEY` there too if `--draft` is used; the Google service account for the sheet.

## What the probe does

`python scripts/fix_meta.py <slug> --probe` reads the indexable variants of these Ahrefs issues: description missing/empty, page and SERP titles do not match, title missing/empty, multiple titles, multiple descriptions, and duplicate titles/descriptions where the project reports them (otherwise the `duplicate_*_canonical_hreflang` counts on the flagged pages). It pulls 90 days of GSC per page through the Ahrefs project, learns the site's brand suffix from a 100-title sample, then:

- **Routes archives out.** Category, tag, author, date and `/page/N/` URLs (and anything Ahrefs classes as a listing or blog index) go to `indexation-review`: one Yoast taxonomy template or a noindex covers all of them, and a per-page description on a tag archive is wasted work. Noindexed and non-200 pages are skipped for the same reason. The homepage title is proposed but never automated: it comes from Yoast's site-wide template.
- **Reads what Google did with each title** rather than treating every "SERP mismatch" as a defect. `brand dropped` (Google shows the title minus the suffix), `truncated`, `brand moved first` and `used as-is` get no action. `rewritten to H1` proposes the H1 plus the brand suffix: Google already decided the H1 describes the page better. `stale year` swaps the year to the one in the URL/H1 (and in the description, if it carries the same year). `brand typo` fixes a misspelt suffix. `glued` (two titles concatenated) proposes the H1. Anything else is `rewritten` with Google's version shown for the reviewer.
- **Orders the queue** by GSC impressions × (1 − CTR): pages Google shows most but clicks least first; then Ahrefs traffic; then page type (core > people > product > post).
- **Drafts descriptions** for pages that need one, from the page's own text (`site-audit-page-content`, about 50 Ahrefs units per page, capped by `--max-pages`, default 40). Sources, in order: a hand-written `reports/<slug>/meta-drafts.json` (keys are URL paths, values `{"title","description","basis"}`); `--draft`, one model call per page with the trimmed page text and the top GSC query; the bio template (`<Name> is a <role> at <brand> in <city>, practicing <areas>`) when the page is a person with a role line and an areas-of-practice list. A draft that cannot be made is marked `needs draft`; the reviewer writes it in the sheet.

Everything lands in `reports/<slug>/meta-<crawl>.md` (the queue, a per-page block with current/Google/H1/proposed and the basis of each draft, the no-action list with the reason, the routed list) and `meta-<crawl>.json` (what `--sheet` pushes). Read the report before pushing: a wrong brand suffix or a misread page type is fixed in the client file and the probe rerun, not in the sheet.

## The drafting standard (encoded in the probe and in `--draft`; the reviewer holds the same bar)

Tiebreaker is Google Search Central (title links, snippets), then the Ahrefs title-tag and meta-description studies and SEL's rewrite analysis.

- Titles only where Google is rewriting, or the title is missing, duplicated or defective. Describe the page, keep the H1's meaning, one brand suffix in the site's existing convention, no keyword lists, no pipe-separated city lists, no stale years. Keep what Google kept: if Google's displayed version is better, propose Google's version. Never change a title Google already uses as-is.
- Descriptions unique per page, written from the page's own text, one or two sentences that answer "what will I find here", the top GSC query worked in only when the page answers it. No claims the page does not make: no outcome promises or superlatives for a law firm, no treatment-result claims for a medical spa. Templated bios are fine when the fields are real; Google says programmatic descriptions from page data are acceptable.
- No character limits, ever. "Title too long" and "Meta description too long" are ignored on purpose; Google states no limit and rewrites snippets anyway. The skill never truncates.
- Every draft carries a `basis` (`from page text`, `templated from fields`, `model draft`, `stale year`, `rewritten to H1` ...) so the reviewer knows what to look hardest at. Model drafts are the ones to read closely; templated bios are the ones to spot-check.

## Review sheet tab `meta`

`python scripts/fix_meta.py <slug> --sheet` upserts one row per queued URL on the `meta` tab of the client's review sheet (created if missing). Columns: `url | page_type | impressions | ctr | position | top_query | current_title | serp_title | proposed_title | new_title | current_description | proposed_description | new_description | basis | status | note | updated`.

Humans edit `new_title`, `new_description`, `status` and `note` only. A rerun refreshes metrics, current values, proposals and basis and never touches those four. `status`: `pending` → `approved` (human) → `applied <date>` (script, after the live apply). Blank `new_*` at apply time means leave that field alone; `skip` in a field means the same; a row with neither field filled is ignored. Rows already `applied` are left alone by later `--sheet` runs; if the next crawl still flags the page it is a new row only once the applied row is cleared by a human.

Copy the proposal into `new_*` when it is right as it stands: the script writes what is in `new_*`, never what is in `proposed_*`.

## Running one site

```
python scripts/fix_meta.py <slug> --fix
```
Dry run on staging of every approved row. Ships `scripts/php/set_meta.php` over SSH and runs it with `wp eval-file`: resolves each URL to a post by path (so a staging hostname is fine), reports `before → after` per field and the `rendered` title/description Yoast will actually output. On a dry run `rendered` is the current state; read it to see the site's Yoast template behaviour (whether it appends the separator and brand to a literal title). A `no post` row is a URL that is not a post or page (a template-driven archive that slipped through, or a page newer than the staging copy). Log: `changes/<provider>/<slug>/<stamp>-fix-meta-staging-dry.md`.

```
python scripts/fix_meta.py <slug> --fix --apply
```
Apply on staging. Before-values of every written row are saved to `changes/<provider>/<slug>/backup/<stamp>-fix-meta-staging.json` (git-ignored), the object cache is flushed (Kinsta: the page cache too), and `rendered` now shows the new output. Open two or three of the pages on staging and view source.

```
python scripts/fix_meta.py <slug> --fix --apply --target live
```
Live. The script asks you to type the slug (`--yes` skips that for vetted unattended runs; with neither a terminal nor `--yes` it aborts). After the apply it re-fetches every written page from outside and logs the public `<title>` and description; an unchanged value minutes after the apply is the edge cache. Rows that were set become `applied <date>` on the sheet; a row that failed gets the reason in `note`.

Commit the `changes/<provider>/<slug>/*.md` logs, not the backup folder.

## Rollback

`python scripts/fix_meta.py <slug> --rollback changes/<provider>/<slug>/backup/<stamp>-fix-meta-<target>.json` (dry; add `--apply`). Restores each field to its before-value only while the field still holds exactly what the fix wrote; anything edited since is reported and left alone. An empty before-value deletes the meta row, so Yoast falls back to its template.

## Verification

- Ahrefs recrawl: "Meta description tag missing or empty" should drop by the number of real pages written (the archives stay until `indexation-review`). "Page and SERP titles do not match" is a lagging signal; Google has to recrawl and decide again, and the brand-dropped rows will keep appearing because that behaviour is Google's, not the site's.
- GSC after four weeks: CTR on the rewritten pages against the 90 days before (`gsc-page-history` through the Ahrefs project). That number is what justifies this skill; record before/after in the report.

## Scope and limits

- WordPress with Yoast, over SSH with WP-CLI. Writes `_yoast_wpseo_title` and `_yoast_wpseo_metadesc` on published posts, pages, products and public custom post types; nothing else. AIOSEO keeps per-post SEO in its own table (`wp_aioseo_posts`), so those two sites get the queue and the sheet but "manual in AIOSEO" instead of a write, until a second writer exists.
- Does not touch Yoast templates, taxonomy settings, or the homepage title (propose only), and does not noindex anything: that is `indexation-review`.
- Does not generate text without a basis, and does not apply text a human has not approved. The queue is internal; clients never see the sheet.
