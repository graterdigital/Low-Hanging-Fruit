# Handoff: work-orders

Status as of 2026-11-09: **built, v1.1** (sheet now carries the whole report: `client_brief` column + `work orders summary` tab). `scripts/work_orders.py` + `skills/work-orders/SKILL.md`. Tested offline on hsfamilylaw (crawl 2026-11-03, health 97): 27 active issue types → 10 work orders (3 client decisions). The sheet upsert, `cleared` stamping and the decisions write-back were exercised against a mocked sheet; the first real `--sheet` run is Greg's, on his PC (needs the service-account key). Mirror of the project doc `claude/skill-work-orders.md`; update both. Process definition is in `docs/issue-routing.md` §3.

## Purpose

Collect every item that needs a human (manual fixes, client decisions, skill-routed exceptions) into one "work orders" tab per client review sheet plus a roster view, fed from the latest Ahrefs crawl through `routes.yaml`, auto-cleared on the next crawl.

## What was built

- `scripts/work_orders.py <slug> [--cache] [--sheet] [--decisions]`, `--all`, `--roster [--sheet]`. Report `reports/<slug>/work-orders-<crawl>.md` + `.json`; roster `reports/_roster/work-orders-<date>.md`. Cache in its own folder `tmp/ahrefs-cache/<slug>/work-orders/` and every Ahrefs call pinned to `date=<crawl>` (2026-11-09: Greg's first real run picked up ai_discoverability's stale `issues.json` from 10-29 while the page calls hit the current crawl → blank example columns and health 94 on a crawl that was already 97).
- `routes.yaml` now carries `what_to_do` and `decider` on the six `manual` entries, on the twelve AI-discoverability checks (with a per-check `route` and `tier`, moved out of `ai_discoverability.py`, which now reads them from routes.yaml so there is one copy), on the schema rows, and `tier: decide` on the intent rows (noindex ×3, nofollow page, orphan page, the three bot-policy checks). The header of routes.yaml documents the fields and the work-order rule.
- Rule (in the script, no list of its own): handler `manual` → always; tier `FLAG` or `decide` → yes; handler still `proposed` in `handlers:` → "skill pending" row, drops off when the skill is built; `review`/unmapped → classify; plus routed-out items from fix-redirect-links (skipped list by reason via `SKIP_REASONS`, wp_options log), fix-images (product-alt exceptions), fix-meta (routed rows), and any `*-workorders.json` a skill writes.
- Two merges that matter: the four noindex/nofollow issues fold into one "Pages hidden from Google: confirm intent" row (one client question, not four); "Indexable page not in sitemap" / "OG URL not matching canonical" are skipped when every URL is `/page/N/` (Yoast by design, as the hsfamilylaw triage parked them).
- Client briefs: one paragraph per `decider: client` row in the report (hidden pages, homepage-redirect targets, off-site link, bot policy, orphans have specific text; the rest get a generic paragraph from `what_to_do`).
- Decisions: sheet row `done` + note `decision: …` → `rules.decisions` in the client file (text edit, comments kept, as `"<date> <id>: <text>"`); rows with a recorded decision are left off every later run until the line is deleted.
- Sheet tab `work orders` (16 columns incl. `client_brief`, humans own owner/status/decision_or_note); tab `work orders summary` rebuilt each run with the crawl header, skipped-on-purpose, decisions on file and a run history, so the sheet is the single place for all fix data (Greg's call 2026-11-09). A tab made with the old 15-column header is extended in place, `cleared <date>` when an issue leaves the crawl, un-cleared if it returns. Agency sheet: tabs `work orders` and `by client`, rebuilt each run, id from `clients/_agency.yaml` → `review.agency_sheet_id` (file not created yet; Greg makes the blank sheet "LHF work orders" in the shared folder first).

## Fleet run 2026-11-09 (Greg, `--all --sheet`): 41 clients, crawls 11-04..11-09

638 rows across 38 clients before the fixes below; 312 were per-issue "skill pending" rows (now collapsed to one per skill per client and sorted last), 13 unclassified (`review`) issue types (all 13 classified in routes.yaml the same day), and fix-meta's routed dict was mis-parsed (`Pages fix-meta routed to []`; fixed). Ranking by traffic at stake: reflectionscenter 38.6k (health 14: 2.1k pages with broken links, 2.1k with schema validation errors, 1.3k incomplete OG), miuraboiler 10.5k (bot policy decision 453 pages, 2.9k schema pages), newradiancenow 2.4k, legalatlanta 1.9k, 22plasticsurgery 1.9k, ruggeddepot 1.4k. Roster-wide, what people can do today: schema.org validation errors (14 clients, 20k traffic, almost always one hand-coded block per theme), slow pages (28 clients, 11k URLs), H1 missing (24 clients, template edits). What is waiting on skills, by traffic: fix-broken-links 18k, fix-social-tags 12.8k, schema-fix 6.8k, nofollow-audit 1.7k — that is the build order the data argues for. 10 clients still have no review sheet (list in `review_sheets.py` output); the agency sheet (`clients/_agency.yaml`) is not created yet. Re-running `--all --sheet` after this commit will clear the old per-issue pending rows and add the collapsed ones (one-time churn).

## hsfamilylaw, crawl 2026-11-03 (health 97)

The crawl already shows fix-meta's work (description missing 59 → 13, all archives) and the archive template fixes (H1 missing and orphan pages are gone). What is left for a human, by traffic at stake: the hand-coded LegalService schema block (43 pages, 335 traffic, FLAG: validator first), Organization schema (skill pending, 164), four homepage-redirect URLs that need real targets (client decision, first `redirect-rules` input), confirm `/terms/`, `/privacy-policy/`, `/andrea-hastings-top-one-percent/` are meant to be hidden (client), the `/podcast/` off-site link (client), `/page/1/` pagination template (7 archives, diff by hand), the client-side reviews widget on `/what-our-clients-say/`, Yoast author archives (one setting), nofollow on the two legal pages (fine; skill pending), and the pasted image path on `/understanding-roles-collaborative-divorce-team/`.

## Next, in order

1. First real `--sheet` run done 2026-11-09 (sheet 15clsGl0RA5BRuYQFyiWzxxy_kVcrXcdH5P5Lt9QdSKU, tabs `work orders` + `work orders summary`), against the stale 10-29 crawl; the rerun on the current crawl clears the four rows that no longer exist (orphan, H1, 3XX in sitemap, FAQ). Next: set status/owner on a couple of rows, put `decision: …` on one, `--decisions`, check `clients/hsfamilylaw.yaml`.
2. Create the blank "LHF work orders" sheet in the LHF Review Sheets folder, add `clients/_agency.yaml` with `review: {agency_sheet_id: <id>}`, then `--all --cache --sheet` and `--roster --sheet`.
3. Read the roster output across the 40 projects: the point of the first run is to see whether "skill pending" rows swamp it (cmitsolutions, ruggeddepot) and whether the `review` (unclassified) rows are worth classifying now.
4. Wire into the weekly cycle (`ai_discoverability_cycle.py` or a sibling) after the Monday crawls.

## Open items

- Skills should write `*-workorders.json` for their human items; today the script parses fix-redirect-links' map and options log, fix-images' exception CSV and fix-meta's JSON.
- `traffic_at_stake` is Ahrefs organic traffic summed over the top 200 flagged pages; GSC impressions where connected would be better for ordering.
- Brief text per issue could live in routes.yaml next to `what_to_do`; today the specific briefs are in `brief_for()`.
- Template diffs are the finding skill's job (site-triage names them; nothing writes them yet); the work order should link the diff once one exists.
- `review_sheets.py status` does not count this tab or the `meta` tab.
