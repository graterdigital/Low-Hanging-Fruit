# Work orders: stg-fenceworksofgeorgia-fwstaging.kinsta.cloud

Ahrefs Site Audit project 10134365 · crawl 2026-11-04 · health 75 · 19 active issue types → 8 work orders (2 decisions, 2 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 294 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex page. |
| 2 | Orphan page (has no incoming internal links)  (non-indexable pages) | indexation-review | decide | 6 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 3 | Slow page | manual | FLAG | 92 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 4 | Pages fix-meta routed to homepage title | homepage title | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 5 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 6 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 7 | Waiting on skill `nofollow-audit` (3 issue types): Nofollow in HTML and HTTP header (293); Page has nofollow incoming internal links only  (non-indexable pages) (287); Page has nofollow outgoing internal links  (non-indexable pages) (293) | nofollow-audit | skill pending | 873 | 0 | agency | Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: nofollow set twice (meta tag and X-Robots-Tag header): staging sites do this on purpose; on a live site remove the header one. |
| 8 | Waiting on skill `indexation-review` (2 issue types): Noindex in HTML and HTTP header (293); Noindex page in sitemap (235) | indexation-review | skill pending | 528 | 0 | agency | Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |

## Per item

### 1. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex page.

- `/news/page/21/`
- `/cages-enclosures-installation-experts/`
- `/category/wooden-privacy-fence/page/2/`
- `/news/page/15/`
- `/prep-fence-fall-weather/`
- `/alpharetta-ga-fence-company-tips-for-choosing-a-residential-fence/`
- `/4-tips-wooden-fence-winter/`
- `/classic-wood-fences-atlanta-ga/`
- `/atlanta-metal-fences/`
- `/fence-building-steering-clear-mishaps/`
- … 284 more in Ahrefs

### 2. Orphan page (has no incoming internal links)  (non-indexable pages)

`issue:orphan-page-has-no-incoming-internal-links-nonindexable` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/category/athletic-facilities/`
- `/category/gates-and-entries/`
- `/editable-sections-demo-safe-to-edit/`
- `/category/farm-fences/`
- `/category/composite-fence/`
- `/category/temporary-fencing/`

### 3. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/prep-fence-fall-weather/`
- `/alpharetta-ga-fence-company-tips-for-choosing-a-residential-fence/`
- `/atlanta-metal-fences/`
- `/about-us/products-and-service-area/`
- `/right-fence-material/`
- `/how-to-paint-a-vinyl-fence/`
- `/reviews/`
- `/summer-decorate-picket-fence/`
- `/tips-winterizing-fence-fenceworks-ga/`
- `/begin-back-yard-renovation-new-fence/`
- … 82 more in Ahrefs

### 4. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-28.json

See the fix-meta report's 'Routed elsewhere' section.


### 5. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-28.json

See the fix-meta report's 'Routed elsewhere' section.


### 6. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-28.json

See the fix-meta report's 'Routed elsewhere' section.


### 7. Waiting on skill `nofollow-audit` (3 issue types): Nofollow in HTML and HTTP header (293); Page has nofollow incoming internal links only  (non-indexable pages) (287); Page has nofollow outgoing internal links  (non-indexable pages) (293)

`pending:nofollow-audit` · nofollow-audit · skill pending · decider: agency

Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: nofollow set twice (meta tag and X-Robots-Tag header): staging sites do this on purpose; on a live site remove the header one.

- `/news/page/21/`
- `/cages-enclosures-installation-experts/`
- `/category/wooden-privacy-fence/page/2/`
- `/news/page/15/`
- `/prep-fence-fall-weather/`
- `/alpharetta-ga-fence-company-tips-for-choosing-a-residential-fence/`
- `/4-tips-wooden-fence-winter/`
- `/classic-wood-fences-atlanta-ga/`
- `/atlanta-metal-fences/`
- `/fence-building-steering-clear-mishaps/`
- … 863 more in Ahrefs

### 8. Waiting on skill `indexation-review` (2 issue types): Noindex in HTML and HTTP header (293); Noindex page in sitemap (235)

`pending:indexation-review` · indexation-review · skill pending · decider: agency

Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/news/page/21/`
- `/cages-enclosures-installation-experts/`
- `/category/wooden-privacy-fence/page/2/`
- `/news/page/15/`
- `/prep-fence-fall-weather/`
- `/alpharetta-ga-fence-company-tips-for-choosing-a-residential-fence/`
- `/4-tips-wooden-fence-winter/`
- `/classic-wood-fences-atlanta-ga/`
- `/atlanta-metal-fences/`
- `/fence-building-steering-clear-mishaps/`
- … 518 more in Ahrefs

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (294 pages: /news/page/21/, /cages-enclosures-installation-experts/, /category/wooden-privacy-fence/page/2/, /news/page/15/, …)

294 pages on stg-fenceworksofgeorgia-fwstaging.kinsta.cloud are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

**Orphan page (has no incoming internal links)  (non-indexable pages)** (6 pages: /category/athletic-facilities/, /category/gates-and-entries/, /editable-sections-demo-safe-to-edit/, /category/farm-fences/, …)

6 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

