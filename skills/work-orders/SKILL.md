---
name: work-orders
description: Collect everything on a client site that needs a human (theme/template edits, hosting tickets, content calls, client decisions, and the exceptions other skills routed out) into one "work orders" list per client plus a roster view, fed from the latest Ahrefs Site Audit crawl through routes.yaml and auto-cleared on the next crawl. Use this when the user asks what is left to do by hand on a site, what needs a client decision, for the manual backlog across the roster, to write a client brief for a decision, or to record a decision so skills stop asking. Read-only against the site; writes reports, a Google Sheet tab, and `rules.decisions` in the client file.
---

# work-orders

Skills fix what is mechanical. Everything else used to live in chat: the triage's "needs a human" section, the fix-redirect-links skipped list, a FLAG row in a report nobody reopened. This skill collects all of it in one place per client, keeps it current against each crawl, and turns client decisions into client-file facts.

## What you need

1. `clients/<slug>.yaml` with `ahrefs.site_audit_project_id`; `review.alt_sheet_id` for the sheet tab (`python scripts/review_sheets.py setup <slug>` if missing). The roster sheet needs `clients/_agency.yaml` with `review.agency_sheet_id` (a blank sheet named "LHF work orders" in the shared Drive folder).
2. `AHREFS_API_KEY` in `.env`; the Google service account for the sheet commands.
3. `routes.yaml` up to date. It is the only list this skill reads; there is no routing table in the script.

## What becomes a work order

Decided entirely by `routes.yaml`, per Ahrefs issue type:

- handler `manual` → always (template edits, hosting tickets, content calls). These entries carry `what_to_do` and `decider`.
- tier `FLAG` → diagnose first; tier `decide` → a choice, not a task (noindex intent, bot policy, orphan pages, where a dead URL should go). `decide` rows have a `decider: agency | client`; client rows get a one-paragraph brief in the report.
- handler is a skill whose status in the `handlers:` map is still `proposed` → "skill pending": real work nobody is doing yet. These drop off the list the day the skill's status changes to `built`, so the backlog stays honest.
- handler `review` or an issue id not in routes.yaml → "classify this in routes.yaml".
- Items a built skill routed to a human: fix-redirect-links `skipped` (grouped by reason, each reason mapped to a handler in `SKIP_REASONS`; host-variant redirects are expected and make no row), its `-options.md` wp_options hits, fix-images product-alt exception CSVs, fix-meta's routed rows, and any `*-workorders.json` a skill writes next to its report (format in the script docstring; new skills should write that instead of relying on the parser).

Never on the list: `ignore`, `monitor`, and anything a built or specified skill handles. Two automatic skips: "Indexable page not in sitemap" / "Open Graph URL not matching canonical" when every URL is `/page/N/` (Yoast by design), and the four noindex/nofollow issues, which are folded into one "Pages hidden from Google: confirm intent" row because the client answers one question, not four.

Rows whose id has a decision in the client file's `rules.decisions` are left off until someone deletes that line.

## Run

```
python scripts/work_orders.py <slug> [--cache]        # reports/<slug>/work-orders-<crawl>.md + .json
python scripts/work_orders.py <slug> --sheet           # + upsert the "work orders" tab on the client's review sheet
python scripts/work_orders.py <slug> --decisions       # copy done rows' "decision: …" notes into clients/<slug>.yaml → rules.decisions
python scripts/work_orders.py --all [--sheet]          # every client with an Ahrefs project
python scripts/work_orders.py --roster [--sheet]       # reports/_roster/work-orders-<date>.md (+ agency sheet) from the newest per-client JSONs
```

Cost: one `site-audit-issues` call per client plus one page-explorer call (≤200 URLs, `url,traffic`) per work-order issue, so 5 to 15 calls per site. `--cache` reuses responses in `tmp/ahrefs-cache/<slug>/`.

## Report

`reports/<slug>/work-orders-<crawl>.md`: a table ordered by traffic at stake, then tier (decide before FLAG before APPROVE), then URL count; a per-item section with up to 10 example URLs; **Client briefs** (one paragraph per client decision, ready to paste into an email; agency decisions stay in the table); skipped-on-purpose; decisions already on file. The `.json` beside it feeds the roster.

## Sheet tab `work orders`

Columns: `id | issue | handler | tier | urls_affected | traffic_at_stake | what_to_do | example_urls | decider | owner | status | decision_or_note | opened | updated | cleared | client_brief`. `client_brief` is the paste-ready paragraph for client decisions (same text as the report's Client briefs section).

Humans edit `owner`, `status`, `decision_or_note` only. `status`: `open` → `needs decision` → `in progress` → `done` / `won't fix`. Every run refreshes counts, traffic, what-to-do and examples and never touches the three human columns. A row whose issue is gone from the crawl gets `cleared <date>`; if it returns, `cleared` is blanked and the row is live again with its old status.

`--decisions`: a row with `status` done/won't fix and `decision_or_note` starting `decision:` is appended to `rules.decisions` in the client file as `"<date> <id>: <text>"` (text edit, comments preserved). Skills read `rules.decisions` before asking the same question; this skill drops the row.

## Sheet tab `work orders summary`

Rebuilt on every `--sheet` run so the sheet carries the whole report, not only the rows: site and crawl header (health, active issue types, work-order and decision counts, traffic at stake), how-to-use line, skipped-on-purpose items with the reason, decisions on file from the client file, and a run history (one line per run, kept across rebuilds). The `.md` report stays the version-controlled copy; the sheet is where people work.

## Roster

`--roster` reads the newest `work-orders-*.json` per client (run the clients first, or `--all`), writes `reports/_roster/work-orders-<date>.md` (per-client counts and traffic at stake, then every item by traffic) and with `--sheet` rebuilds the `work orders` and `by client` tabs on the agency sheet. The agency tabs are rebuilt from scratch each run; per-client tabs are where status lives.

## Template fixes and briefs

A template edit (archive `<h1>`, `/page/1/` pagination, hand-coded schema) gets a diff file in `changes/<provider>/<slug>/` written by whichever skill found it, and the work order points at it; this skill does not write diffs. Client briefs are generated for the common decision types (hidden pages, homepage redirects, off-site links, bot policy, orphans); other client rows get a generic paragraph from `what_to_do`, which is the signal to add a specific brief to `brief_for()`.

## Verification

The next crawl: a cleared row is the proof the fix worked. A `done` row that is not cleared on the next crawl means the fix did not take (or Ahrefs has not recrawled yet; check the crawl date in the report header).

## Open items

- Skills should emit `*-workorders.json` for their human items instead of this script parsing their reports (fix-redirect-links skipped list and options log, fix-images exceptions, fix-meta routed rows are parsed today).
- Weekly cycle: add a work-orders pass to `ai_discoverability_cycle.py` (or a sibling) after each crawl: `--all --sheet` then `--roster --sheet`, commit the reports.
- Email brief generation beyond the built-in types; per-issue brief text could live in routes.yaml.
- `traffic_at_stake` is Ahrefs estimated organic traffic summed over the flagged pages (top 200); GSC impressions would be the better number where the project has GSC connected.
