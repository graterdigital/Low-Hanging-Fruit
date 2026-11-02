# Handoff: work-orders

Status as of 2026-11-02: specified, not built. Mirror of the project doc `claude/skill-work-orders.md`; update both. Process definition is in `docs/issue-routing.md` §3; this is the build spec.

## Purpose

Collect every item that needs a human (manual fixes, client decisions, skill-routed exceptions) into one "work orders" tab per client review sheet plus a roster view, fed from the latest Ahrefs crawl through `routes.yaml`, auto-cleared on the next crawl.

## Build on

- `routes.yaml`: handler per issue type. Add `what_to_do` and `decider` fields to the `manual` entries as they get written (the AI-discoverability `WHAT_TO_DO` dict is the model; move it into routes.yaml so there is one copy).
- `scripts/review_sheets.py` (`gc`, `sheet_for`) and `ai_discoverability.py::push_sheet` for the upsert pattern (script owns metrics, humans own status/note, `cleared <date>` when gone).
- `build_redirect_map.py` Ahrefs helpers; `Api` cache class in `ai_discoverability.py`.
- Skill outputs that already list human items: fix-redirect-links `skipped` + `-options.md`; fix-images exception CSVs; ai-discoverability routed rows; site-triage "Not examined" section; fix-meta's out-of-scope list.

## Script

`scripts/work_orders.py <slug> [--sheet] [--roster] [--all]`

1. Pull `site-audit-issues` for the client; keep `crawled > 0`; map each to `routes.yaml`.
2. Rows for: handler `manual`; any `decide` tier; routed-out items from skill reports in `reports/<slug>/` and `changes/<provider>/<slug>/` (parse the skipped/exception sections; each skill should also emit a small `*-workorders.json` going forward so parsing isn't needed).
3. For each row pull up to 10 example URLs with `traffic` (page-explorer, one call per issue) and sum traffic as `traffic_at_stake`.
4. Upsert to the `work orders` tab: key = issue name (or `skill:item` for routed items). Never overwrite `owner`, `status`, `decision_or_note`. Set `cleared <date>` when an issue is no longer active and status isn't already done.
5. `--roster`: one tab `work orders` on the agency sheet (new client file key `review.agency_sheet_id` in `clients/_agency.yaml`), all open rows across clients sorted by traffic_at_stake, plus a per-client count table.
6. Decisions: when `status` is `done` and `decision_or_note` starts with `decision:`, write the decision into the client file (`rules.decisions:` list with date) so skills can read it.

## Columns

`id | issue | handler | tier | urls_affected | traffic_at_stake | what_to_do | decider | owner | status | decision_or_note | opened | updated | cleared`

## Open questions

- Agency sheet location (same Drive folder, named "LHF work orders").
- Whether a weekly cycle script (`ai_discoverability_cycle.py` exists as a model) should run work-orders across the roster after each crawl.
- Email brief generation for `decider: client` rows: template per issue in routes.yaml, filled with the client's name and URLs.
