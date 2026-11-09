# Work orders: stg-fenceworksofgeorgia-fwstaging.kinsta.cloud

Ahrefs Site Audit project 10134365 · crawl 2026-11-04 · health 75 · 19 active issue types → 9 work orders (2 decisions, 4 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 294 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex page. |
| 2 | Orphan page (has no incoming internal links)  (non-indexable pages) | indexation-review | decide | 6 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 3 | Slow page | manual | FLAG | 92 | 0 | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 4 | Pages fix-meta routed to [] | [] | FLAG | 4 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 5 | Noindex in HTML and HTTP header | indexation-review | APPROVE (skill pending) | 293 | 0 (top 200 of 293) | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 6 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 293 | 0 (top 200 of 293) | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 7 | Page has nofollow incoming internal links only  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 287 | 0 (top 200 of 287) | agency | Skill `nofollow-audit` is planned but not built; until then: find what adds rel=nofollow to internal links (theme, plugin, editor habit); if systematic, one fix clears thousands (ruggeddepot 8k, miuraboiler 3k) |
| 8 | Noindex page in sitemap | indexation-review | APPROVE (skill pending) | 235 | 0 (top 200 of 235) | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 9 | Nofollow in HTML and HTTP header | review | ? | 293 | 0 (top 200 of 293) | agency | Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster) |

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

### 4. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-28.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`
- `noindex`
- `non-200`
- `homepage title`

### 5. Noindex in HTML and HTTP header

`issue:noindex-in-html-and-http-header` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

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
- … 283 more in Ahrefs

### 6. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

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
- … 283 more in Ahrefs

### 7. Page has nofollow incoming internal links only  (non-indexable pages)

`issue:page-has-nofollow-incoming-internal-links-only-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: find what adds rel=nofollow to internal links (theme, plugin, editor habit); if systematic, one fix clears thousands (ruggeddepot 8k, miuraboiler 3k)

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
- … 277 more in Ahrefs

### 8. Noindex page in sitemap

`issue:noindex-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/cages-enclosures-installation-experts/`
- `/prep-fence-fall-weather/`
- `/alpharetta-ga-fence-company-tips-for-choosing-a-residential-fence/`
- `/4-tips-wooden-fence-winter/`
- `/classic-wood-fences-atlanta-ga/`
- `/atlanta-metal-fences/`
- `/fence-building-steering-clear-mishaps/`
- `/about-us/products-and-service-area/`
- `/plan-fence-project-winter-fenceworks/`
- `/right-fence-material/`
- … 225 more in Ahrefs

### 9. Nofollow in HTML and HTTP header

`issue:nofollow-in-html-and-http-header` · review · ? · decider: agency

Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster)

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
- … 283 more in Ahrefs

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (294 pages: /news/page/21/, /cages-enclosures-installation-experts/, /category/wooden-privacy-fence/page/2/, /news/page/15/, …)

294 pages on stg-fenceworksofgeorgia-fwstaging.kinsta.cloud are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

**Orphan page (has no incoming internal links)  (non-indexable pages)** (6 pages: /category/athletic-facilities/, /category/gates-and-entries/, /editable-sections-demo-safe-to-edit/, /category/farm-fences/, …)

6 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

