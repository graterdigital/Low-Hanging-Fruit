# Work orders: fenceworksofga.com

Ahrefs Site Audit project 9799850 · crawl 2026-11-05 · health 98 · 19 active issue types → 8 work orders (2 decisions, 2 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Orphan page (has no incoming internal links) | indexation-review | decide | 5 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 2 | Links to redirect, skipped by fix-redirect-links: redirects to homepage | redirect-rules | decide | 1 | 0 | client | Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order. |
| 3 | Category page missing ItemList schema | schema-check | FLAG | 2 | 0 | agency | Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave. |
| 4 | Pages fix-meta routed to homepage title | homepage title | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 5 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 6 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 7 | Waiting on skill `schema-fix` (1 issue type): Organization schema missing or incomplete (1) | schema-fix | skill pending | 1 | 679 | agency | Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file). |
| 8 | Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (36) | fix-social-tags | skill pending | 36 | 0 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |

## Per item

### 1. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/category/gates-and-entries/`
- `/category/temporary-fencing/`
- `/category/farm-fences/`
- `/category/composite-fence/`
- `/category/athletic-facilities/`

### 2. Links to redirect, skipped by fix-redirect-links: redirects to homepage

`redirect-links:redirects-to-homepage` · redirect-rules · decide · decider: client · source: redirect-map-2026-10-29.json

Each old URL needs a real redirect target (redirect-rules) or the link removed; GSC impressions decide the order.

- `/` (1 links)

### 3. Category page missing ItemList schema

`issue:category-page-missing-itemlist-schema` · schema-check · FLAG · decider: agency

Ahrefs preference, not a Google feature. Optional: ItemList via wpseo_schema_graph filter. Usually leave.

- `/category/picket-fence/`
- `/category/farm-fences/`

### 4. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 5. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 6. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 7. Waiting on skill `schema-fix` (1 issue type): Organization schema missing or incomplete (1)

`pending:schema-fix` · schema-fix · skill pending · decider: agency

Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Fill Organization in the SEO plugin: name, logo, sameAs, contact (schema-fix will do this from the client file).

- `/` (679 traffic)

### 8. Waiting on skill `fix-social-tags` (1 issue type): Open Graph tags incomplete (36)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/category/chain-link-fence/`
- `/category/wooden-privacy-fence/page/11/`
- `/category/wooden-privacy-fence/page/17/`
- `/category/ranch-rail-split-rail-fence/`
- `/category/wooden-privacy-fence/page/4/`
- `/category/picket-fence/`
- `/category/chain-link-fence/page/2/`
- `/category/wooden-privacy-fence/page/7/`
- `/category/wooden-privacy-fence/page/10/`
- `/category/wooden-privacy-fence/page/16/`
- … 26 more in Ahrefs

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Orphan page (has no incoming internal links)** (5 pages: /category/gates-and-entries/, /category/temporary-fencing/, /category/farm-fences/, /category/composite-fence/, …)

5 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Links to redirect, skipped by fix-redirect-links: redirects to homepage** (1 page: /)

1 old URL on fenceworksofga.com currently redirect to the homepage, which loses visitors who click an old link. For each one we need the page it should go to now (or confirmation that nothing replaces it, in which case we remove the links).

## Skipped on purpose

- Indexable page not in sitemap (43): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

