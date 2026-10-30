---
name: ai-discoverability
description: Report how a client site is seen by AI search and training crawlers (robots.txt bot policy, JavaScript-only content, page size, server speed, IndexNow, Ahrefs' schema notices) from Ahrefs Site Audit's "AI Discoverability" category, and apply the one direct fix, a managed robots.txt block, once the client has decided its policy. Use whenever a triage report or Ahrefs lists "blocked from AI search bots", "Inconsistent AI training bot policy", "requires JavaScript rendering", "IndexNow", or the user asks about AI visibility, GEO, llms.txt, GPTBot, ClaudeBot, or whether to block AI crawlers. Read-and-route by design; robots.txt is APPROVE, everything else is FLAG or handed to another skill.
---

# ai-discoverability

Most of what gets sold as "AI SEO" is either a normal SEO lever with a new name or does nothing measurable. This skill does three things: shows what the site's robots.txt actually does to the 25 AI crawlers Ahrefs tracks, compares that with what the client wants, and routes the machine-readability findings to the skill that owns them. Its one direct write is a managed block in robots.txt, and it never makes that change until the client has decided the policy, because blocking training bots is a business call (content control vs. being in the models' knowledge), not an SEO one.

Google's position, which the skill follows: AI Overviews and AI Mode use Googlebot and need pages that are indexed and snippet-eligible; `Google-Extended` governs Gemini training and grounding, not Search; no AI-specific file or markup is needed. Blocking Googlebot to stay out of AI Overviews removes the page from Search. The skill refuses to block Googlebot no matter what the client file says.

## What you need

1. A client file `clients/<slug>.yaml` with `ahrefs.site_audit_project_id` and an `ai:` block (the template has it):
   ```yaml
   ai:
     search_bots: allow          # allow | block   AI search/assistant crawlers (ChatGPT-User, OAI-SearchBot, Claude-SearchBot, PerplexityBot ...)
     training_bots: unknown      # allow | block   model-training crawlers (GPTBot, ClaudeBot, Google-Extended, Meta-ExternalAgent ...)
     exceptions: []              # bot names that flip the verdict above
     indexnow: unknown           # yes | no | unknown: does the site itself ping IndexNow on publish
     policy_confirmed_by: ""     # who at the client decided, and when
   ```
   `unknown` on either bots field means undecided. The skill reports but proposes nothing until both are `allow` or `block`.
2. `AHREFS_API_KEY` in `.env` at the repo root.
3. For `--probe` and `--apply-robots`: `hosting.ssh_alias` (live) and `hosting.staging_environment` filled in.

## Running one site

```
python scripts/ai_discoverability.py <slug> --probe
```
Pulls the AI Discoverability issue list, the pages behind each active check, and a traffic-sorted sample of 40 indexable HTML pages with their per-page bot columns (it is the same robots.txt for every page, so a sample is enough). Fetches the public robots.txt. `--probe` adds an SSH look at live: whether robots.txt is a physical file or WordPress's virtual one, and which IndexNow mechanism the site has. Writes:

- `reports/<slug>/ai-discoverability-<crawl-date>.md`: policy vs. actual per bot, current robots.txt, one table per active check with its route and tier, the IndexNow picture, the not-recommended list, a reconciliation of all 12 checks, sources.
- `reports/<slug>/robots-proposed-<crawl-date>.txt` only when the client policy is decided and differs from what is live.
- `ai.observed` in the client file (crawl date, blocked bots, Ahrefs IndexNow status, robots.txt kind and IndexNow plugin when probed). The policy fields above are never written by the skill.

`--cache` keeps the raw Ahrefs responses in `tmp/ahrefs-cache/<slug>/` so the report can be re-rendered for free. `--robots-file <path>` uses a saved robots.txt instead of fetching.

## Reading the report

**Section 1, bot access.** The table lists every search and training bot Ahrefs classifies, whether it is blocked on all, some, or none of the sampled pages, what the policy says, and the resulting action. "Blocked on some pages" is Ahrefs' "Inconsistent AI training bot policy": robots.txt groups that disagree, which the managed block fixes by construction. If the policy is undecided the section stops there and says what to ask the client. Default proposal: allow search bots, decide training bots per client, never block Googlebot.

**Section 2, checks with pages.** Each active check gets its route:

| Check | Route | Tier |
|---|---|---|
| Indexable page blocked from all / some AI search bots, Inconsistent AI training bot policy | this skill, managed robots.txt block | APPROVE |
| Page size exceeds 2 MB crawl limit | `fix-images` | AUTO |
| Slow server response for AI crawlers | hosting / cache (TTFB, not a crawl fix) | FLAG |
| Main content requires JavaScript rendering | theme or plugin, by hand; the report names the client-side widget plugins on the site | FLAG |
| Similar AI-generated content | content, Phase 4 | FLAG |
| Article / Category / FAQ / Organization / Product schema notices | `schema-check` | FLAG |

The five schema checks are Ahrefs' notices against its own page classification, not Google requirements. Google says no special structured data is needed for AI features; what matters is that schema on the page describes what is visibly on it. Organization schema is worth completing (name, logo, sameAs) through the SEO plugin. FAQPage stopped earning rich results in Google on 2026-05-07.

**Section 3, IndexNow.** Two separate mechanisms, and Ahrefs only reports on the first:
- Ahrefs' own auto-submission (Site Audit → Crawl settings → IndexNow; needs an IndexNow key file at the site root and a project boost). `Indexnow_off` in the per-page `indexnow_status` column means this setting is off. It is not a statement about the site.
- The site pinging IndexNow on publish, which is the one that matters for fresh content. Yoast SEO Premium has it built in (free Yoast does not); Rank Math has the Instant Indexing plugin; AIOSEO has an addon; Microsoft's free `indexnow` plugin works everywhere else. `--probe` checks the active plugin list for these. Google ignores IndexNow; Bing, Yandex, Naver and Seznam use it, and Bing's index feeds ChatGPT search and Copilot. Installing the plugin is APPROVE (a plugin install on a client site); record the result in `ai.indexnow`.

**Section 4, not recommended.** llms.txt (Google Search does not read it; large-scale studies found no citation effect), "AI-specific" schema or hidden text, blocking Googlebot to avoid AI Overviews, rewriting content "for AI". Say so in client conversations; the real levers are indexable, snippet-eligible, fast, text in HTML, accurate schema, Business Profile current.

## Applying the robots.txt policy

Only after the client has decided, the `ai:` block records it with `policy_confirmed_by`, and the report has produced a proposed file.

```
python scripts/ai_discoverability.py <slug> --apply-robots
```
Dry run on staging: shows whether staging serves a physical `robots.txt` or WordPress's virtual one (`do_robots()`), and the diff. Nothing is written.

```
python scripts/ai_discoverability.py <slug> --apply-robots --apply
```
Writes the file on staging, backs up the previous content (file or virtual output) to `changes/<provider>/<slug>/backup/`, flushes the cache, logs to `changes/<provider>/<slug>/<stamp>-ai-discoverability-staging-robots-apply.md`. Open `https://<staging>/robots.txt` and read it.

```
python scripts/ai_discoverability.py <slug> --apply-robots --target live --apply
```
Same on live; type the slug to confirm, or `--yes` for vetted unattended runs. The script re-fetches the public robots.txt afterwards and says whether it matches yet (an edge cache can lag). Commit the change log, not the backup folder.

How the proposed file is built: the current text is kept as is, any existing group that only addresses AI bots is removed, and one managed block between marker comments disallows the bots the policy blocks. Allowed bots get no group of their own on purpose: robots.txt groups do not inherit, so a bot with its own group ignores the `User-agent: *` rules, and the safest way to allow a bot is to give it no group. Rerunning replaces the managed block instead of stacking rules; switching the policy back to allow removes the block and leaves the rest of the file untouched.

Virtual robots.txt: WordPress and Yoast generate robots.txt when no file exists in the web root. Writing a physical file takes over from then on, and the proposed file carries the generated content (including Yoast's `Sitemap:` line) as static text. Yoast's file editor will edit that same file afterwards. To go back to virtual, delete the file.

Not WordPress, or `rules.do_not_touch` lists `robots.txt`: the script stops; hand over the proposed file.

## Running the roster

```
python scripts/ai_discoverability.py --all
```
One page-explorer call per client with an Ahrefs project (top 5 live pages), writes `docs/ai-bot-policy.md`: a table of policy vs. blocked bots vs. Ahrefs IndexNow status per site. Cheap way to see which sites block anything today (most block nothing, because nobody set a policy) and which client files still say `unknown`.

## After

- Recrawl: the three bot-access checks reflect the new robots.txt on the next crawl. `ai.observed` updates on the next report run.
- Hand the routed items on: the 2 MB pages to `fix-images`, schema notices to `schema-check`, the JS-rendered page and the slow pages to whoever owns the theme and the hosting.
- If the client chose to block training bots, tell them what it does and does not do: it keeps the named crawlers from fetching pages for training, it does not remove content already in any model, and it has no effect on Google Search, AI Overviews, or any search bot.

## Scope and limits

- Reads the Ahrefs API and the public robots.txt. Writes only `robots.txt` on the target (and the client file's `ai.observed`). Never touches `User-agent: *` rules, sitemap lines, or any non-AI group.
- Ahrefs classifies the bots; the skill's universe is whatever `allowed_*` and `blocked_*` columns return, with a fallback list for a site Ahrefs has never crawled. A new bot appears automatically once Ahrefs tracks it.
- Bot access is only robots.txt. A WAF or CDN rule (Cloudflare's AI bot blocking, for instance) blocks crawlers without any robots.txt trace; if Ahrefs reports nothing blocked but the client says bots are blocked, look there.
- `--probe` and `--apply-robots` are WordPress over SSH with WP-CLI, Kinsta web root `public`, WP Engine `sites/<install>` (picked from `hosting.provider`).
