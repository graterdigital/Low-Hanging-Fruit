# Handoff: ai-discoverability

Status as of 2026-10-30: specified, not built. Mirror of the project doc `claude/skill-ai-discoverability.md`; update both.

## Purpose

Report and tune how a site is seen by AI search and assistant crawlers, using Ahrefs Site Audit's "AI Discoverability" category (app view: Site Audit → AI discoverability → sub-categories *Bot access* and *Machine readability*). Mostly read-and-decide: the few direct fixes are a robots.txt policy change (APPROVE) and the IndexNow toggle (APPROVE); everything else routes to another skill.

## Data available through the Ahrefs API

Issue types (`site-audit-issues`, category `AI Discoverability`), with hsfamilylaw counts from the 2026-10-08 crawl:

| Check | Importance | Sub-category | hsfamilylaw |
|---|---|---|---|
| Indexable page blocked from all AI search bots | Warning | Bot access | 0 |
| Indexable page blocked from some AI search bots | Notice | Bot access | 0 |
| Inconsistent AI training bot policy | Notice | Bot access | 0 |
| Main content requires JavaScript rendering | Warning | Machine readability | 1 (`/what-our-clients-say/`, reviews widget) |
| Slow server response for AI crawlers | Warning | Machine readability | 3 |
| Page size exceeds 2 MB crawl limit | Error | Machine readability | 0 |
| Similar AI-generated content | Warning | Machine readability | 0 |
| Changed pages not submitted to IndexNow | Notice | Machine readability | 2 |

Per-page columns (`site-audit-page-explorer`): `allowed_search_bots`, `blocked_search_bots`, `allowed_training_bots`, `blocked_training_bots`, `is_rendered`, `size_uncompressed`, `http_header_robots`, `meta_robots`, `robots_error`, `indexnow_status`, `ai_content_level`. hsfamilylaw's homepage allows all 17 AI search bots (ChatGPT-User, OAI-SearchBot, Claude-SearchBot, PerplexityBot, Applebot, DuckAssistBot, Google-Agent, ...) and all 8 training bots (GPTBot, ClaudeBot, anthropic-ai, Google-Extended, Applebot-Extended, Meta-ExternalAgent, DeepseekBot, xAI-Bot).

## Skill design

Inputs: client slug; a per-client policy block in `clients/<slug>.yaml`:

```yaml
ai:
  search_bots: allow          # allow | block   (citations and live answers in ChatGPT, Perplexity, AI Overviews, etc.)
  training_bots: allow        # allow | block   (model training; GPTBot, ClaudeBot, Google-Extended, ...)
  exceptions: []              # bot names that override the above
  indexnow: unknown           # yes | no | unknown
  policy_confirmed_by: ""     # who at the client decided, and when
```

Steps:
1. Pull the eight checks and the per-page bot columns for indexable pages (one call with `where` on indexable, select the bot columns; it's the same robots.txt for every page, so sample the homepage and a few templates rather than all URLs).
2. **Bot access.** Compare actual allow/block lists with the client policy. If the client file has no policy, stop and ask: it's a business decision (training-bot blocking trades future AI visibility for content control). Output a proposed robots.txt diff. APPROVE. Note Google's own guidance: AI Overviews and AI Mode use Googlebot; `Google-Extended` governs Gemini training and grounding, not Search; blocking Googlebot to avoid AI Overviews also removes the page from Search.
3. **Machine readability.** Route: page size > 2 MB → `fix-images`; slow response for AI crawlers → hosting/cache (FLAG; a TTFB check, not a crawl fix); JS-only main content → theme/plugin change (FLAG, with the page and the plugin named); similar AI-generated content → content phase (FLAG). IndexNow: Google ignores it, Bing/Yandex/Naver use it; Yoast and Rank Math have a one-click toggle. APPROVE, cheap.
4. **Not recommended, say so in the report:** llms.txt (Google states Search does not use it; a 300k-domain study found no citation effect), "AI-specific" schema, chunking or rewriting content "for AI." The real levers are the normal ones: indexable, snippet-eligible, content in HTML text, structured data that matches the page, Business Profile current.
5. Write `reports/<slug>/ai-discoverability-<crawl-date>.md`: policy vs. actual, proposed robots.txt diff, routed items, recommendation-against list. Update the client file's `ai:` block with what was observed.

Tier summary: robots.txt change APPROVE (only after the client decides); IndexNow APPROVE; everything else FLAG or routed.

Write path for robots.txt on WordPress: if a physical `robots.txt` exists in the web root, edit it over SSH with a backup copy in `changes/`; otherwise WordPress generates it and Yoast's file editor (or the `robots_txt` filter) owns it. Check which with `wp eval 'echo file_exists(ABSPATH."robots.txt") ? "file" : "virtual";'`.

## Verification

Ahrefs recrawl: the three bot-access checks reflect robots.txt within one crawl. For IndexNow, `indexnow_status` per page flips on the next content change.

## Open questions for the build chat

- Does the firm (and each client) want training bots blocked? Default proposal: allow search bots, decide training bots per client, never block Googlebot.
- Whether to extend the sync script's fingerprint with a robots.txt fetch so the client index shows bot policy across all 40 sites at once (cheap: one page-explorer call per site, or the public robots.txt).
- Sources to cite in the report: Google AI features doc (https://developers.google.com/search/docs/appearance/ai-features), Google AI optimization guide (https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), Google-Extended / robots meta docs, Ahrefs AI discoverability help article.
