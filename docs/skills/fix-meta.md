# Handoff: fix-meta

Status as of 2026-11-02: specified, not built. Mirror of the project doc `claude/skill-fix-meta.md`; update both.

## Purpose

Write missing or weak SEO titles and meta descriptions through the SEO plugin, with every piece of text reviewed by a human before it goes live. APPROVE tier always (searchers read this text; the law-firm client rule `visible_copy_changes: approve` applies to all clients here). Highest traffic impact of anything in Phase 1.

## What exists to build on (do not rebuild)

- **Review loop:** `scripts/review_sheets.py` gives every client a persistent Google Sheet (`review.alt_sheet_id` in the client file, service-account auth, Drive folder "LHF Review Sheets"). `scripts/ai_discoverability.py` shows the pattern for a skill-owned tab (`push_sheet`: upsert rows, humans own `status`/`note`, scripts own the rest) and a sheet-driven `--fix` that reads rows back. Add a tab named `meta`.
- **Yoast per-post write:** `scripts/php/set_article_type.php` is the template: job JSON in a constant, `wp eval-file -` over SSH, path-based URL→post matching (works on staging hostnames), dry/apply, before/after rows. Copy it to `set_meta.php` writing `_yoast_wpseo_title` and `_yoast_wpseo_metadesc`.
- **Runner conventions:** `fix_redirect_links.py` / `fix_images.py`: `--probe`, dry default, `--apply`, `--target live`, `--yes`, change log to `changes/<provider>/<slug>/`, backup JSON of before values, `wp cache flush` after apply, `restore_changes.py` for rollback.
- **Ahrefs helpers:** `build_redirect_map.py` (`load_env`, `ahrefs()`), GSC through the Ahrefs API (`gsc-pages`, `gsc-keywords`; 0 units; 17 of 40 projects connected, `ahrefs.gsc_connected` in the client file).

## Inputs

Ahrefs Site Audit issues (`site-audit-issues` + `site-audit-page-explorer` with `issue_id`):

| Issue | issue_id | hsfamilylaw (2026-10-08) |
|---|---|---|
| Meta description tag missing or empty (indexable) | `c64d31f0-d0f4-11e7-8ed1-001e67ed4656` | 58 (41 archives/pagination, 17 real pages) |
| Page and SERP titles do not match | `d69246c2-225a-11ec-8456-06d2f2f613d8` | 28 (20 with traffic, 653 combined) |
| Title tag missing or empty, Multiple title tags, Duplicate titles, Duplicate meta descriptions | look up by name in the issues list | 0 / 0 / 0 / 0 here; present on other sites |

Page-explorer columns: `url, title, serp_title, is_page_title_used_in_serp, meta_description, h1, traffic, page_type, duplicate_title, duplicate_description_canonical_hreflang`. GSC per page: `clicks, impressions, ctr, position, top_keyword, keywords_count` (gsc-pages, last 90 days). Page text for drafting: `site-audit-page-content` with `select: page_text_md` (one call per page, ~50 units; only for pages that make the queue).

Ignore on purpose (already in site-triage's ignore list): "Title too long" and "Meta description too long". Google states no length limit. The skill never truncates to a character count; it writes what the page needs and lets Google display what it will.

## Scope rules

- **In:** indexable, non-archive pages: core pages, people/bio pages, posts, products. On hsfamilylaw that is 17 pages without a description plus the SERP-mismatch list.
- **Out, routed elsewhere:** category/tag/author archives and `/page/N/` (Yoast taxonomy templates or noindex → `indexation-review`); the homepage title when it comes from Yoast's site-wide template (`wpseo_titles` option; propose, don't automate); non-indexable pages (skip entirely; Patrick Stox's point that descriptions on noindexed pages are wasted work).
- **Queue order:** GSC impressions × (1 - CTR) first, so a page with 17,609 impressions at 0.22% CTR (`/how-much-does-a-divorce-cost-in-georgia-in-2026/`) outranks a bio with 300 impressions, which outranks any zero-impression page. Without GSC, fall back to Ahrefs `traffic`, then to page type (core > people > post).

## Drafting rules (encode these; they are the standard, not taste)

Sources: Google title links and snippet docs, Ahrefs title-tag study (76% rewritten per SEL Q1 2025; brand removal and boilerplate are the top rewrite triggers), Ahrefs meta description study.

Titles (only where Google is rewriting, or missing/duplicate):
- Describe the page, match the visible H1's meaning, one brand suffix (`| Hastings Shadmehry` style from the site's existing convention), no keyword lists, no city lists separated by pipes, no stale years (the `2026` URL whose title still says 2025 is the canonical example).
- Keep what Google kept. `serp_title` shows what Google chose to display; if Google's version is better, propose Google's version.
- Never change a title Google is already using as-is (`is_page_title_used_in_serp` true) unless it's also missing or duplicate.

Descriptions:
- Unique per page, written from the page's own text (`page_text_md`), one or two sentences that answer "what will I find here", including the top GSC query naturally when there is one. Programmatic generation from page data is explicitly fine per Google; templated bios ("<Name> is a <role> at <firm> in <city> practicing <areas>") are acceptable if the fields are real.
- No claims the page doesn't make. For a law firm, no outcome promises; for medical spas, no treatment-result claims. Draft from what's on the page, nothing more.
- Mark every draft with how it was made (`from page text`, `templated from fields`, `from GSC query`) so the reviewer knows what to look hardest at.

## Review sheet tab `meta`

Columns: `url | page_type | impressions | ctr | position | top_query | current_title | serp_title | proposed_title | new_title | current_description | proposed_description | new_description | basis | status | note | updated`

Humans edit `new_title`, `new_description`, `status`, `note` only. `status`: `pending` → `approved` (human) → `applied <date>` (script). Blank `new_*` at apply time means "leave that field alone"; `skip` leaves the row alone. Re-running `--sheet` refreshes metrics and current values, never overwrites `new_*`.

## Write path

- **Yoast (31 sites):** postmeta `_yoast_wpseo_title`, `_yoast_wpseo_metadesc` via `set_meta.php` (`update_post_meta`; Yoast reads them directly, no cache beyond page cache → `wp cache flush`). Verify by fetching the page and checking `<title>` and `<meta name="description">` after apply; Yoast may append the separator/brand from its template if the literal title lacks it, so confirm the rendered form in the dry run's report.
- **AIOSEO (cmitsolutions, glomedspa):** AIOSEO stores per-post SEO in its own table `wp_aioseo_posts` (`title`, `description` columns), not postmeta. Out of scope for v1; the skill reports these two as "manual in AIOSEO" until a second PHP writer exists.
- **Products (WooCommerce):** same Yoast meta on the product post. Title/description templates in Yoast often cover products adequately; include only products that Ahrefs flags.
- **Backup:** before values per post in `changes/<provider>/<slug>/<stamp>-fix-meta-<target>.json`; rollback through `restore_changes.py` (extend it to understand meta rows if it doesn't already).

## Run order

```
python scripts\fix_meta.py <slug> --probe                 # queue + drafts → reports/<slug>/meta-<crawl>.md, nothing written anywhere else
python scripts\fix_meta.py <slug> --sheet                 # push drafts to the "meta" tab
   (human reviews in the sheet)
python scripts\fix_meta.py <slug> --fix                   # dry run from approved rows, on staging
python scripts\fix_meta.py <slug> --fix --apply           # staging
python scripts\fix_meta.py <slug> --fix --apply --target live
```

## Verification

- Ahrefs recrawl: "Meta description missing" should drop by the number of real pages written (archives remain until `indexation-review`); "Page and SERP titles do not match" is a lagging signal, since Google has to recrawl and decide again.
- GSC after 4 weeks: CTR on the rewritten pages vs. the 90 days before, via `gsc-page-history`. That is the number that justifies this skill; record before/after in the report.

## Open questions for the build chat

- Brand suffix convention per client: read it from the current titles (most common suffix) or set `meta.brand_suffix` in the client file? Suggest: detect, write to the client file, let Greg correct.
- Where drafts come from: the build chat drafting them itself from `page_text_md` is fine for 17 pages; across 40 sites it needs a batched drafting step (one model call per page with the page text and the GSC query), which the probe can do and cache in the report.
- Whether to let the skill propose Yoast *templates* for post types/taxonomies (one change covers many pages) in addition to per-page writes. Likely yes, as FLAG output in the report.
