# AI discoverability: hsfamilylaw.com

Ahrefs Site Audit project 9704538 · crawl 2026-10-29 · health 94 · 40 indexable pages sampled (top by traffic) · robots.txt source: `https://hsfamilylaw.com/robots.txt` (HTTP 200)

Mostly read-and-route. The only direct change this skill makes is the robots.txt policy block (APPROVE, after the client decides). Google's position, which this report follows: AI Overviews and AI Mode use Googlebot and need pages that are indexed and snippet-eligible; `Google-Extended` governs Gemini training and grounding, not Search; no AI-specific files or markup are needed.

## 1. Bot access (robots.txt)

Client policy in `clients/hsfamilylaw.yaml`: search bots **allow**, training bots **unknown**.

**No decision on file.** This is a business call, so the skill stops here on bot access: allowing training bots trades content control for being in the models' knowledge; blocking them does not affect Google Search, AI Overviews, or any 'search' bot above. Default proposal: allow all search bots, decide training bots per client, never block Googlebot. Record the decision in the `ai:` block and rerun.

| Bot | Class | Live (sampled pages) | Policy says | Action |
|---|---|---|---|---|
| Amazonbot | search | allowed | undecided | - |
| Amzn-SearchBot | search | allowed | undecided | - |
| Amzn-User | search | allowed | undecided | - |
| Applebot | search | allowed | undecided | - |
| ChatGPT-User | search | allowed | undecided | - |
| Claude-SearchBot | search | allowed | undecided | - |
| Claude-User | search | allowed | undecided | - |
| Claude-Web | search | allowed | undecided | - |
| DuckAssistBot | search | allowed | undecided | - |
| GitHubCopilotChat | search | allowed | undecided | - |
| Google-Agent | search | allowed | undecided | - |
| Googlebot | search | allowed | undecided | - |
| MistralAI-User | search | allowed | undecided | - |
| OAI-SearchBot | search | allowed | undecided | - |
| Perplexity-User | search | allowed | undecided | - |
| PerplexityBot | search | allowed | undecided | - |
| YouBot | search | allowed | undecided | - |
| Applebot-Extended | training | allowed | undecided | - |
| ClaudeBot | training | allowed | undecided | - |
| DeepseekBot | training | allowed | undecided | - |
| GPTBot | training | allowed | undecided | - |
| Google-Extended | training | allowed | undecided | - |
| Meta-ExternalAgent | training | allowed | undecided | - |
| anthropic-ai | training | allowed | undecided | - |
| xAI-Bot | training | allowed | undecided | - |

robots.txt errors reported by Ahrefs: none · Sitemap lines: `https://hsfamilylaw.com/sitemap_index.xml` · X-Robots-Tag headers on sampled pages: none

Current robots.txt:

```
# START YOAST BLOCK
#  -  -  -  -  -  -  -  -  - 
User-agent: *
Disallow:

Sitemap: https://hsfamilylaw.com/sitemap_index.xml
#  -  -  -  -  -  -  -  -  - 
# END YOAST BLOCK

User-agent: axios
  Allow: /
```

## 2. Checks with pages behind them

### Article page missing Article schema (4, Notice) → schema-check · FLAG

Ahrefs' ML classed the page as an article; Yoast emits Article only for posts.

| URL | traffic | JSON-LD types on page | Ahrefs page type |
|---|---|---|---|
| `/divorce/uncontested-divorce/` | 23 | BreadcrumbList, EntryPoint, ImageObject, LegalService, ListItem, Organization, PostalAddress, PropertyValueSpecification, ReadAction, SearchAction, State, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/family-law/grandparents-rights/` | 0 | BreadcrumbList, EntryPoint, ImageObject, LegalService, ListItem, Organization, PostalAddress, PropertyValueSpecification, ReadAction, SearchAction, State, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/divorce/before-divorce/` | 0 | BreadcrumbList, EntryPoint, ImageObject, LegalService, ListItem, Organization, PostalAddress, PropertyValueSpecification, ReadAction, SearchAction, State, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/family-law/legitimation-paternity/` | 0 | BreadcrumbList, EntryPoint, ImageObject, LegalService, ListItem, Organization, PostalAddress, PropertyValueSpecification, ReadAction, SearchAction, State, WebPage, WebSite | /Article/Tutorial_or_Guide |

### FAQ page missing FAQPage schema (1, Notice) → schema-check · FLAG

FAQ rich results are gone from Google (2026-05-07); add FAQPage only if it matches visible Q&A and the client wants it for other engines.

| URL | traffic | JSON-LD types on page | Ahrefs page type |
|---|---|---|---|
| `/category/divorce-faq/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, Organization, PropertyValueSpecification, SearchAction, WebSite | /Core_Page/FAQ_Page |

### Main content requires JavaScript rendering (1, Warning) → theme/plugin (by hand) · FLAG

The plugin or widget rendering the main copy client-side needs server-side output or fallback text.

Client-side widget plugins on this site (from the client file): business-reviews-bundle, youtube-feed-pro. One of these is the usual suspect; the fix is server-rendered output or static fallback text in the template.

| URL | traffic | rendered? |
|---|---|---|
| `/what-our-clients-say/` | 0 | True |

### Organization schema missing or incomplete (1, Notice) → schema-check · FLAG

Usually the homepage; the SEO plugin's Organization settings (name, logo, sameAs) fill it.

| URL | traffic | JSON-LD types on page | Ahrefs page type |
|---|---|---|---|
| `/` | 199 | BreadcrumbList, EntryPoint, ImageObject, LegalService, ListItem, Organization, PostalAddress, PropertyValueSpecification, ReadAction, SearchAction, State, WebPage, WebSite | /Core_Page/Homepage |

Schema notes: these are Ahrefs' notices against its own page classification, not Google requirements. Google says no special structured data is needed to appear in AI features; the rule that matters is that any schema on the page describes what is visibly on the page. Organization schema is worth completing (name, logo, sameAs) through the SEO plugin. FAQPage no longer earns rich results in Google. Hand the list to `schema-check` with the existing validation-error work.

## 3. IndexNow (APPROVE)

Google ignores IndexNow; Bing, Yandex, Naver and Seznam use it, and Bing's index feeds ChatGPT search and Copilot. Two separate things can submit URLs, and Ahrefs only reports on the first:

- **Ahrefs auto-submission** (Site Audit → Crawl settings → IndexNow): status on sampled pages `Indexnow_off` ×40. `Indexnow_off` means the crawl setting is off. Turning it on needs an IndexNow key file hosted at the site root and a project boost that includes the feature; then Ahrefs submits changed, new, redirected and removed pages after each crawl.
- **The site pinging on publish**: Yoast SEO Premium (built in, on by default; not in free Yoast), Rank Math's Instant Indexing plugin, AIOSEO's IndexNow addon, or Microsoft's free `indexnow` plugin on anything else. This is the one that matters for fresh content, and Ahrefs cannot see it. Probe over SSH (hsfamilylaw): no IndexNow plugin active; `wpseo.enable_index_now` = 1.

Client file says `ai.indexnow: no`. Recommended for the roster: Microsoft's `indexnow` plugin on free-Yoast sites (one key file, no settings), and the SEO plugin's own integration where it exists. Record the choice in `ai.indexnow` once it is live.

Probe also found robots.txt served as **file** on live.

## 4. Not recommended, on purpose

- **llms.txt**: Google Search does not read it, and large-scale studies have found no citation effect. Skip it; if a client insists, it is harmless but does nothing measurable.
- **"AI-specific" schema or hidden content for AI**: Google needs none and treats hidden text as spam. Keep copy in the HTML as text; make schema match the page.
- **Blocking Googlebot to stay out of AI Overviews**: removes the page from Search. Use `nosnippet`/`max-snippet` on a page if a client truly wants no AI preview, and expect it to cost regular snippets too.
- **Chunking or rewriting content "for AI"**: the levers are the usual ones: indexable, snippet-eligible, fast, text in HTML, accurate schema, Business Profile current.

## 5. Reconciliation

AI Discoverability issue types in this crawl: 12 · with URLs: 4 · zero: 8

| Check | Importance | URLs | Route |
|---|---|---|---|
| Article page missing Article schema | Notice | 4 | schema-check (FLAG) |
| Category page missing ItemList schema | Notice | 0 | schema-check (FLAG) |
| FAQ page missing FAQPage schema | Notice | 1 | schema-check (FLAG) |
| Inconsistent AI training bot policy | Notice | 0 | ai-discoverability (APPROVE) |
| Indexable page blocked from all AI search bots | Warning | 0 | ai-discoverability (APPROVE) |
| Indexable page blocked from some AI search bots | Notice | 0 | ai-discoverability (APPROVE) |
| Main content requires JavaScript rendering | Warning | 1 | theme/plugin (by hand) (FLAG) |
| Organization schema missing or incomplete | Notice | 1 | schema-check (FLAG) |
| Page size exceeds 2 MB crawl limit | Error | 0 | fix-images (AUTO) |
| Product page missing Product schema | Warning | 0 | schema-check (FLAG) |
| Similar AI-generated content | Warning | 0 | content (Phase 4) (FLAG) |
| Slow server response for AI crawlers | Warning | 0 | hosting/cache (FLAG) |

## 6. Client file

`clients/hsfamilylaw.yaml` → `ai.observed` was updated by this run (crawl, robots.txt kind if probed, blocked bots, IndexNow status). The policy fields (`search_bots`, `training_bots`, `exceptions`, `policy_confirmed_by`) are yours; the skill never writes them.

## Sources

- Google: AI features and your website https://developers.google.com/search/docs/appearance/ai-features
- Google: AI optimization guide https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google: robots meta tag / Google-Extended https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers
- Ahrefs: AI Discoverability in Site Audit (feature announcement, Sept 2026) https://ahrefs.com/blog/new-features-september-2026/
- Ahrefs: IndexNow in Site Audit https://help.ahrefs.com/en/articles/9317209-how-to-submit-pages-to-indexnow-within-site-audit
- Yoast: IndexNow is a Premium feature https://yoast.com/yoast-seo-june-28-2022/
- IndexNow https://www.indexnow.org/
