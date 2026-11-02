# Handoff: ai-discoverability

Status as of 2026-11-02: **built, v1. IndexNow plugin live on 28 WordPress sites (11 Kinsta 2026-10-30, 17 WP Engine 2026-11-02); 3 sites already on Yoast Premium. Key file confirmed served on hsfamilylaw; rerun the dry runs to record it roster-wide.** Report path tested end to end on hsfamilylaw (crawl 2026-10-29); robots.txt proposal, idempotence and unblock tested against the live file offline; `--probe` and `--apply-robots` written but not yet run against a real server. Mirror of the project doc `claude/skill-ai-discoverability.md`; update both.

Files: `skills/ai-discoverability/SKILL.md` (the procedure), `scripts/ai_discoverability.py` (report, roster, probe, robots apply), `reports/hsfamilylaw/ai-discoverability-2026-10-29.md` (first report), `ai:` block in `clients/_template.yaml` and `clients/hsfamilylaw.yaml`.

## Purpose

Report and tune how a site is seen by AI search and assistant crawlers, using Ahrefs Site Audit's "AI Discoverability" category. Read-and-route: the one direct write is a managed robots.txt block (APPROVE, only after the client decides); IndexNow is a plugin install (APPROVE); everything else is FLAG or routed to `fix-images`, `schema-check`, content, hosting.

## What the build found (changes from the spec)

- **The category now has 12 checks, not 8.** Five schema notices were added by Ahrefs (Article, Category/ItemList, FAQPage, Organization, Product), all routed to `schema-check` as FLAG. "Changed pages not submitted to IndexNow" is gone from the issue list.
- **`indexnow_status` is about Ahrefs, not the site.** It reports Ahrefs' own auto-submission (Site Audit → Crawl settings → IndexNow, needs a key file at the site root plus a project boost). `Indexnow_off` = that setting is off. The site's own pinging on publish is invisible to Ahrefs; `--probe` checks the plugin list over SSH instead. And Yoast's IndexNow integration is **Premium only**, so the "one-click toggle" in the spec does not exist on the free-Yoast majority of the roster. Recommendation: Microsoft's free `indexnow` plugin there.
- **Page sample must filter on `is_html` and `page_is_noindex`**, not just `http_code = 200`: images, CSS and JS carry the bot columns too and crowd a traffic-sorted sample.
- Live robots.txt on hsfamilylaw is Yoast's virtual output (`User-agent: *` / `Disallow:` / Sitemap) plus a hand-added `User-agent: axios / Allow: /` group. All 17 search bots and 8 training bots allowed on every sampled page. Nothing blocked anywhere.
- hsfamilylaw active checks on 2026-10-29: Article schema ×4 (service pages Ahrefs' ML classes as guides), FAQPage ×1 (`/category/divorce-faq/`), Organization ×1 (homepage), JS-rendered main content ×1 (`/what-our-clients-say/`; `business-reviews-bundle` or `youtube-feed-pro` is the widget). Slow-server and 2 MB checks are now at zero (fix-images and the WebP Express removal did that).

## Script surface

```
python scripts/ai_discoverability.py <slug> [--probe] [--cache] [--robots-file path] [--no-client-write]
python scripts/ai_discoverability.py <slug> --apply-robots [--apply] [--target live] [--yes] [--webroot public]
python scripts/ai_discoverability.py --all [--cache]          -> docs/ai-bot-policy.md
```

Design points worth keeping: bot universe comes from Ahrefs' `allowed_*`/`blocked_*` columns (fallback lists only for never-crawled sites); allowed bots get no robots group (groups do not inherit); blocked bots sit in one managed block between markers so reruns replace instead of stack; Googlebot is never blocked regardless of the client file; `rules.do_not_touch: [robots.txt]` stops the apply; the client file's policy fields are never written by the script, only `ai.observed`.

## Verification

Ahrefs recrawl: the three bot-access checks reflect robots.txt within one crawl. IndexNow: Bing Webmaster Tools shows submissions; Ahrefs' column only changes if Ahrefs' own auto-submission is turned on.

## Roster findings (first `--all` run, 2026-10-30)

- forwardfacing, miuraboiler, setcomcorp carry an identical hand-added block list: Amazonbot + Claude-Web (search) and Applebot-Extended, ClaudeBot, GPTBot, Google-Extended, Meta-ExternalAgent, anthropic-ai (training). Nobody recorded a decision; find who added it and either record `training_bots: block` with `policy_confirmed_by`, or replace it with the managed block.
- ruggeddepot is the one project with Ahrefs IndexNow auto-submission on (`Indexnow_success`); the other 35 crawled projects are off.
- hsfamilylaw probe: robots.txt is a physical file on live; no IndexNow plugin; free Yoast's `enable_index_now` flag is set but inert.
- Five client files have no crawl data (backto30, fenceworks-staging, liftaesthetics, purskinclinic, sjklawfirm).

## Decisions 2026-10-30

- Bot policy: agency default allow / allow written into all 41 client files with `policy_confirmed_by: "Grater Digital default, Greg 2026-10-30; per-client opt-out on request"`. The three pre-blocked sites (forwardfacing, miuraboiler, setcomcorp) carry a NOTE comment; the skill will propose removing their block, which needs a decision before apply.
- IndexNow: Microsoft's `indexnow` plugin everywhere; Ahrefs auto-submission not used (too expensive). `--install-indexnow --provider <host> [--apply] [--yes]` does the roster; one-site form takes a slug.

## IndexNow rollout log

- 2026-10-30 Kinsta: Microsoft `indexnow` plugin installed + activated on atlantaspecializedcare, fenceworksofga, forwardfacing, hsfamilylaw, markheardfuel, meshautomationinc, miuraboiler, nativecustomstone, setcomcorp, slepianfirm, technikpackaging. ruggeddepot already had Yoast SEO Premium (IndexNow built in). Key-file verification did not run on that pass (the option lookup was too narrow); the dry run now re-checks it and records `ai.observed.indexnow_key_served`.
- 2026-10-30 WP Engine: every site FAILED with `cd: sites/<slug>: No such file or directory`. Cause: WP Engine's root is `/sites/<install>` where install is the environment name, not our slug. Fixed in `build_redirect_map.wpengine_webroot()` (reads the install name from `ssh -G <alias>`), used by ai_discoverability, fix_redirect_links and fix_images, so the WP Engine batches for those skills were about to hit the same wall. blushmedspact already has Yoast Premium. The dry run also used to report "no IndexNow mechanism" when the `cd` failed; it now reports the error.
- 2026-11-02 WP Engine rerun with the web-root fix: installed on 22plasticsurgery, 22spamd, aveluremedspa, curatemedspa, destinationaesthetics, esthetixmd, everbody, glomedspa, h-md, newradiancenow, nouveauspa, purskinclinic, reflectionscenter, skynbaratlanta, synergymedaesthetics, theagelesscenter, theclinique. blushmedspact and livingyoungcenter already on Yoast Premium. Skipped: backto30 (static), dermguy and legalatlanta (no SSH alias).
- Key-file check: Microsoft's plugin stores the key **base64-encoded** in `indexnow-admin_api_key` (`indexnow-is_valid_api_key` = 2 once validated). hsfamilylaw: decoded key served at `/<key>.txt` on 2026-11-02, no rewrite flush needed. `confirm_key` now decodes base64; the dry run records `ai.observed.indexnow_key_served: yes` per site.
- Yoast and IndexNow: only Yoast SEO **Premium** pings IndexNow (ruggeddepot, blushmedspact on this roster). Free Yoast has the `enable_index_now` option but no code behind it; that is why the Microsoft plugin goes on the free-Yoast sites.

## Open items

- Rerun `--install-indexnow --provider wpengine` (dry, then `--apply --yes`) with the web-root fix; rerun the Kinsta dry run to confirm key files are served. ruggeddepot: turn Ahrefs auto-submission off in that project's crawl settings.
- forwardfacing / miuraboiler / setcomcorp: find out who added the block list; keep (record `training_bots: block`) or let the skill replace it.
- First real `--probe` and `--apply-robots` run (staging first). The virtual→file handover carries Yoast's Sitemap line as static text; confirm Yoast's file editor then shows that file.
- `--all` roster run once the API key is on the machine, to see whether any of the 40 sites blocks anything today.
- Sample size: the hsfamilylaw report used 25 pages (built from cached MCP pulls); the script default is 40.
- Sources used by the report: Google AI features (https://developers.google.com/search/docs/appearance/ai-features), Google AI optimization guide (https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), Google crawlers / Google-Extended (https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers), Ahrefs Sept 2026 features post (https://ahrefs.com/blog/new-features-september-2026/), Ahrefs IndexNow help (https://help.ahrefs.com/en/articles/9317209-how-to-submit-pages-to-indexnow-within-site-audit), Yoast IndexNow (https://yoast.com/yoast-seo-june-28-2022/).
