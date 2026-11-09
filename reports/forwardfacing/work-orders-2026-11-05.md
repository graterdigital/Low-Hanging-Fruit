# Work orders: forwardfacing.com

Ahrefs Site Audit project 9704533 · crawl 2026-11-05 · health 95 · 29 active issue types → 10 work orders (3 decisions, 2 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | AI crawler policy (robots.txt): client decision | ai-discoverability | decide | 72 | 0 | client | Set the client's ai: policy (allow/block search bots, allow/block training bots), then ai-discoverability applies the managed robots.txt block. Ahrefs issues folded in: Inconsistent AI training bot policy, Indexable page blocked from some AI search bots. |
| 2 | Orphan page (has no incoming internal links) | indexation-review | decide | 4 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 3 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 1 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex page. |
| 4 | H1 tag missing or empty | manual | FLAG | 1 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 5 | wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings) | manual | FLAG | 1 | 0 | agency | Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1002-fix-redirect-links-live-options.md. |
| 6 | Pages fix-meta routed to homepage title | homepage title | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 7 | Pages fix-meta routed to noindex | noindex | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 8 | Pages fix-meta routed to non-200 | non-200 | FLAG | 0 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 9 | Waiting on skill `fix-broken-links` (3 issue types): 404 page (2); 4XX page (2); Page has links to broken page (2) | fix-broken-links | skill pending | 6 | 0 | agency | Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 10 | Waiting on skill `nofollow-audit` (1 issue type): Page has nofollow outgoing internal links  (non-indexable pages) (1) | nofollow-audit | skill pending | 1 | 0 | agency | Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |

## Per item

### 1. AI crawler policy (robots.txt): client decision

`issue:ai-bot-policy-decide` · ai-discoverability · decide · decider: client

Set the client's ai: policy (allow/block search bots, allow/block training bots), then ai-discoverability applies the managed robots.txt block. Ahrefs issues folded in: Inconsistent AI training bot policy, Indexable page blocked from some AI search bots.

- `/episodes/why-great-employees-struggle-in-the-wrong-role-fractional-integrator-nicole-mennicke-episode-113/`
- `/episodes/meet-the-wolf-pack-family-law-stalwart-elizabeth-findley-episode-65/`
- `/episodes/winning-family-law-firm-secrets-divorce-faqs-episode-20/`
- `/episodes/handling-pet-custody-in-divorce-episode-22/`
- `/episodes/resilience-perspective-life-after-cancer-cdre-jill-heineck-episode-112/`
- `/episodes/meet-the-partners-andee-hastings-and-her-passion-for-family-law-episode-52/`
- `/episodes/meet-the-partners-mali-shadmehry-family-law-attorney-and-trailblazer-episode-53/`
- `/episodes/the-art-of-dog-rescue-with-jason-flatt-forward-facing-102/`
- `/episodes/meet-the-wolf-pack-family-law-attorney-lisa-malas-episode-39/`
- `/episodes/when-to-file-for-divorce-timing-strategy-impact-episode-51/`
- … 62 more in Ahrefs

### 2. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/youtube-feed-cron/`
- `/host/mali-shadmehry/`
- `/podcast-guest/`
- `/host/andee-hastings/`

### 3. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex page.

- `/privacy-policy/`

### 4. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/youtube-feed-cron/`

### 5. wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings)

`redirect-links:wp-options` · manual · FLAG · decider: agency · source: 2026-10-30-1002-fix-redirect-links-live-options.md

Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1002-fix-redirect-links-live-options.md.

- `options_copyright`

### 6. Pages fix-meta routed to homepage title

`fix-meta:homepage-title` · homepage title · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 7. Pages fix-meta routed to noindex

`fix-meta:noindex` · noindex · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 8. Pages fix-meta routed to non-200

`fix-meta:non-200` · non-200 · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.


### 9. Waiting on skill `fix-broken-links` (3 issue types): 404 page (2); 4XX page (2); Page has links to broken page (2)

`pending:fix-broken-links` · fix-broken-links · skill pending · decider: agency

Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/author/developer/`
- `/cdn-cgi/l/email-protection`
- … 4 more in Ahrefs

### 10. Waiting on skill `nofollow-audit` (1 issue type): Page has nofollow outgoing internal links  (non-indexable pages) (1)

`pending:nofollow-audit` · nofollow-audit · skill pending · decider: agency

Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/privacy-policy/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**AI crawler policy (robots.txt): client decision** (72 pages: /episodes/why-great-employees-struggle-in-the-wrong-role-fractional-integrator-nicole-mennicke-episode-113/, /episodes/meet-the-wolf-pack-family-law-stalwart-elizabeth-findley-episode-65/, /episodes/winning-family-law-firm-secrets-divorce-faqs-episode-20/, /episodes/handling-pet-custody-in-divorce-episode-22/, …)

Some AI crawlers are blocked from forwardfacing.com. Allowing AI search bots (ChatGPT, Perplexity, Claude search) lets those tools cite the site in their answers; allowing training bots (GPTBot, ClaudeBot, Google-Extended) puts the content into future models. Our default is allow both; blocking training bots does not affect Google Search. Tell us if you want training bots blocked and we will set it.

**Orphan page (has no incoming internal links)** (4 pages: /youtube-feed-cron/, /host/mali-shadmehry/, /podcast-guest/, /host/andee-hastings/)

4 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Pages hidden from Google (noindex/nofollow): confirm intent** (1 page: /privacy-policy/)

1 page on forwardfacing.com is set so Google does not index it (or does not follow its links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

## Skipped on purpose

- Indexable page not in sitemap (5): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

