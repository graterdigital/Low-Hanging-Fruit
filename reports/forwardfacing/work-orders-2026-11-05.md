# Work orders: forwardfacing.com

Ahrefs Site Audit project 9704533 · crawl 2026-11-05 · health 95 · 29 active issue types → 11 work orders (4 decisions, 4 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Inconsistent AI training bot policy | ai-discoverability | decide | 72 | 0 | client | robots.txt groups disagree; the managed block replaces them (skill). |
| 2 | Indexable page blocked from some AI search bots | ai-discoverability | decide | 72 | 0 | client | Set the client's ai: policy, then apply the managed robots.txt block (skill). |
| 3 | Orphan page (has no incoming internal links) | indexation-review | decide | 4 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 4 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 1 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex page. |
| 5 | Pages fix-meta routed to [] | [] | FLAG | 4 | 0 | agency | See the fix-meta report's 'Routed elsewhere' section. |
| 6 | H1 tag missing or empty | manual | FLAG | 1 | 0 | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 7 | wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings) | manual | FLAG | 1 | 0 | agency | Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1002-fix-redirect-links-live-options.md. |
| 8 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 1 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 9 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 2 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 10 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 2 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 11 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 2 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |

## Per item

### 1. Inconsistent AI training bot policy

`issue:inconsistent-ai-training-bot-policy` · ai-discoverability · decide · decider: client

robots.txt groups disagree; the managed block replaces them (skill).

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

### 2. Indexable page blocked from some AI search bots

`issue:indexable-page-blocked-from-some-ai-search-bots` · ai-discoverability · decide · decider: client

Set the client's ai: policy, then apply the managed robots.txt block (skill).

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

### 3. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/youtube-feed-cron/`
- `/host/mali-shadmehry/`
- `/podcast-guest/`
- `/host/andee-hastings/`

### 4. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex page.

- `/privacy-policy/`

### 5. Pages fix-meta routed to []

`fix-meta:` · [] · FLAG · decider: agency · source: meta-2026-10-29.json

See the fix-meta report's 'Routed elsewhere' section.

- `archive`
- `noindex`
- `non-200`
- `homepage title`

### 6. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/youtube-feed-cron/`

### 7. wp_options rows still carrying old URLs (widgets, menus, theme/plugin settings)

`redirect-links:wp-options` · manual · FLAG · decider: agency · source: 2026-10-30-1002-fix-redirect-links-live-options.md

Fix by hand in the admin (Appearance > Widgets/Menus, theme and plugin settings); list in 2026-10-30-1002-fix-redirect-links-live-options.md.

- `options_copyright`

### 8. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/privacy-policy/`

### 9. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/author/developer/`
- `/cdn-cgi/l/email-protection`

### 10. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/author/developer/`
- `/cdn-cgi/l/email-protection`

### 11. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/host/mali-shadmehry/`
- `/host/andee-hastings/`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Inconsistent AI training bot policy** (72 pages: /episodes/why-great-employees-struggle-in-the-wrong-role-fractional-integrator-nicole-mennicke-episode-113/, /episodes/meet-the-wolf-pack-family-law-stalwart-elizabeth-findley-episode-65/, /episodes/winning-family-law-firm-secrets-divorce-faqs-episode-20/, /episodes/handling-pet-custody-in-divorce-episode-22/, …)

Some AI crawlers are blocked from forwardfacing.com. Allowing AI search bots (ChatGPT, Perplexity, Claude search) lets those tools cite the site in their answers; allowing training bots (GPTBot, ClaudeBot, Google-Extended) puts the content into future models. Our default is allow both; blocking training bots does not affect Google Search. Tell us if you want training bots blocked and we will set it.

**Indexable page blocked from some AI search bots** (72 pages: /episodes/why-great-employees-struggle-in-the-wrong-role-fractional-integrator-nicole-mennicke-episode-113/, /episodes/meet-the-wolf-pack-family-law-stalwart-elizabeth-findley-episode-65/, /episodes/winning-family-law-firm-secrets-divorce-faqs-episode-20/, /episodes/handling-pet-custody-in-divorce-episode-22/, …)

Some AI crawlers are blocked from forwardfacing.com. Allowing AI search bots (ChatGPT, Perplexity, Claude search) lets those tools cite the site in their answers; allowing training bots (GPTBot, ClaudeBot, Google-Extended) puts the content into future models. Our default is allow both; blocking training bots does not affect Google Search. Tell us if you want training bots blocked and we will set it.

**Orphan page (has no incoming internal links)** (4 pages: /youtube-feed-cron/, /host/mali-shadmehry/, /podcast-guest/, /host/andee-hastings/)

4 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Pages hidden from Google (noindex/nofollow): confirm intent** (1 page: /privacy-policy/)

1 page on forwardfacing.com is set so Google does not index it (or does not follow its links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

## Skipped on purpose

- Indexable page not in sitemap (5): all URLs are /page/N/ pagination: Yoast leaves them out of the sitemap and sets og:url to page 1 by design

