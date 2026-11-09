# Work orders: cmitsolutions.com

Ahrefs Site Audit project 9799848 · crawl 2026-11-07 · health 97 · 91 active issue types → 23 work orders (4 decisions, 6 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 959 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page. |
| 2 | Orphan page (has no incoming internal links) | indexation-review | decide | 395 | 0 (top 200 of 395) | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 3 | Orphan page (has no incoming internal links)  (non-indexable pages) | indexation-review | decide | 4 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 4 | Noindex page became indexable | indexation-review | decide | 2 | 0 | client | Pages that were noindexed last crawl are now indexable: confirm it was deliberate (a plugin update or a theme switch can reset it). |
| 5 | Slow page | manual | FLAG | 1627 | 0 (top 200 of 1627) | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 6 | H1 tag missing or empty | manual | FLAG | 801 | 0 (top 200 of 801) | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 7 | Structured data has schema.org validation error | schema-fix | FLAG | 610 | 0 (top 200 of 610) | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 8 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 540 | 0 (top 200 of 540) | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 9 | Multiple title tags | manual | FLAG | 383 | 0 (top 200 of 383) | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 10 | Slow server response for AI crawlers | hosting/cache | FLAG | 207 | 0 (top 200 of 207) | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 11 | Multiple title tags  (non-indexable pages) | manual | FLAG | 184 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 12 | Page has broken CSS | manual | FLAG | 85 | 0 | agency | A stylesheet the page loads 404s or errors: usually a plugin removed without cleaning its enqueue, or a CDN path. Find the URL in the page source, fix the enqueue or re-add the file. |
| 13 | CSS broken | manual | FLAG | 27 | 0 | agency | The CSS file itself returns an error; same fix as 'Page has broken CSS' (one file, many pages). |
| 14 | JavaScript broken | manual | FLAG | 6 | 0 | agency | The script file itself returns an error; same fix as 'Page has broken JavaScript'. |
| 15 | Page has broken JavaScript | manual | FLAG | 6 | 0 | agency | A script the page loads 404s or errors: plugin remnant or CDN path. Fix the enqueue; check the console on one page. |
| 16 | HTML file size too large | manual | FLAG | 2 | 0 | agency | HTML over Ahrefs' size threshold: inline CSS/JS from a builder or an embedded data blob. Usually one template; check what inflates it. |
| 17 | Robots.txt is not accessible | manual | FLAG | 1 | 0 | agency | robots.txt returned an error during the crawl: check it loads now (host block, WAF, or a plugin serving it). Transient if it loads. |
| 18 | Waiting on skill `fix-social-tags` (3 issue types): Open Graph tags incomplete (6177); Open Graph tags missing (1); X (Twitter) card missing (1) | fix-social-tags | skill pending | 6179 | 0 | agency | Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 19 | Waiting on skill `indexation-review` (8 issue types): Indexable page became non-indexable (6); Non-canonical page specified as canonical one (1); Canonical URL has no incoming internal links (14); Indexable page not in sitemap (6116); Noindex page in sitemap (2); Non-canonical page in sitemap (7); Page in multiple sitemaps (6); Sitemap in the wrong format (1) | indexation-review | skill pending | 6153 | 0 | agency | Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 20 | Waiting on skill `fix-broken-links` (6 issue types): Canonical points to 4XX (4); 404 page (289); 4XX page (295); 5XX page (2); Page has links to broken page  (non-indexable pages) (111); Page has links to broken page (738) | fix-broken-links | skill pending | 1439 | 0 | agency | Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 21 | Waiting on skill `nofollow-audit` (4 issue types): Page has nofollow incoming internal links only  (non-indexable pages) (60); Page has nofollow incoming internal links only (826); Page has nofollow outgoing internal links  (non-indexable pages) (466); Page has nofollow outgoing internal links (13) | nofollow-audit | skill pending | 1365 | 0 | agency | Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: find what adds rel=nofollow to internal links (theme, plugin, editor habit); if systematic, one fix clears thousands (ruggeddepot 8k, miuraboiler 3k) |
| 22 | Waiting on skill `schema-fix` (1 issue type): Structured data has Google rich results validation error (218) | schema-fix | skill pending | 218 | 0 | agency | Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual |
| 23 | Waiting on skill `redirect-rules` (4 issue types): Canonical points to redirect (20); Broken redirect (102); Redirect loop (2); 3XX redirect in sitemap (6) | redirect-rules | skill pending | 130 | 0 | agency | Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |

## Per item

### 1. Pages hidden from Google (noindex/nofollow): confirm intent

`issue:hidden-pages-confirm-intent` · indexation-review · decide · decider: client

Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page.

- `/houston-tx-1192/resources/page/2/`
- `/tempe-az-1141/blog/category/blogs/page/2/`
- `/sanmateo-ca-1060/managed-it-services-in-san-carlos/page/2/`
- `/stlouis-mo-1042/resources/page/2/`
- `/boston-ma-1089/blog/page/3/`
- `/westchester-ny-1180/resources/page/2/`
- `/upper-east-side-ny-1258/resources/page/2/`
- `/tampa-fl-1078/resources/page/2/`
- `/plymouth-mn-1102/blog/page/2/`
- `/boston-ma-1020/blog/page/3/`
- … 949 more in Ahrefs

### 2. Orphan page (has no incoming internal links)

`issue:orphan-page-has-no-incoming-internal-links` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/the-big-takeaway-any-company-can-be-attacked/`
- `/cmit-solutions-targets-br-n-o/`
- `/test/`
- `/newly-detected-malware-could-have-far-reaching-impacts/`
- `/lp/it-services-for-anyone/`
- `/lp/responsive-support/`
- `/top-10-strategies-for-maximizing-microsoft-office-productivity-and-efficiency/`
- `/end-of-support-is-coming-for-microsoft-windows-server-2008/`
- `/2014-holiday-shopping-statistics-mean-push-toward-mobility/`
- `/how-safe-is-your-smartphone/`
- … 385 more in Ahrefs

### 3. Orphan page (has no incoming internal links)  (non-indexable pages)

`issue:orphan-page-has-no-incoming-internal-links-nonindexable` · indexation-review · decide · decider: client

Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first.

- `/lp/it-budget-review/`
- `/lp/it-budget/`
- `/lp/find-your-it-model/`
- `/lp/scenthound/`

### 4. Noindex page became indexable

`issue:noindex-page-became-indexable` · indexation-review · decide · decider: client

Pages that were noindexed last crawl are now indexable: confirm it was deliberate (a plugin update or a theme switch can reset it).

- `/dallas-tx-1036/client-reviews/`
- `/shenandoah-va-1096/blog/category/it-strategy-infrastructure/`

### 5. Slow page

`issue:slow-page` · manual · FLAG · decider: agency

Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket.

- `/it-solutions-support-from-cmit-solutions-of-erie-transforms-mental-health-agencys-technology/`
- `/how-consumer-grade-video-chat-paved-way-for-cmit-impression/`
- `/jumpstart-your-daily-routine-by-organizing-your-desktop/`
- `/microsoft-rolls-out-new-cybersecurity-protections/`
- `/the-big-takeaway-any-company-can-be-attacked/`
- `/ready-to-take-your-business-to-the-next-level/`
- `/cmit-solutions-targets-br-n-o/`
- `/industries/hipaa-compliant-it-services/`
- `/the-washington-business-journal-spotlights-cmit-solutions-area-developer/`
- `/ffiec-compliance/`
- … 1617 more in Ahrefs

### 6. H1 tag missing or empty

`issue:h1-tag-missing-or-empty` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/powellspoint-nc-1156/contact-us/`
- `/stcharles-mo-1093/blog/`
- `/phoenix-az-1256/blog/`
- `/chicago-il-1221/blog/category/local-it/`
- `/dallas-tx-1036/client-reviews/`
- `/dayton-south-oh-1226/blog/`
- `/glendale-az-1136/cybersecurity-services/`
- `/miami-fl-1208/blog/`
- `/newbrunswick-nj-1187/contact-us/`
- `/atlanta-east-ga-1216/blog/`
- … 791 more in Ahrefs

### 7. Structured data has schema.org validation error

`issue:structured-data-has-schema-org-validation-error` · schema-fix · FLAG · decider: agency

Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit.

- `/it-solutions-support-from-cmit-solutions-of-erie-transforms-mental-health-agencys-technology/`
- `/how-consumer-grade-video-chat-paved-way-for-cmit-impression/`
- `/jumpstart-your-daily-routine-by-organizing-your-desktop/`
- `/the-big-takeaway-any-company-can-be-attacked/`
- `/cmit-solutions-targets-br-n-o/`
- `/bowie-md-1050/resources/`
- `/the-washington-business-journal-spotlights-cmit-solutions-area-developer/`
- `/mobile-device-security-critical-especially-wake-samsung-galaxy-note-7-issues/`
- `/3-ways-to-protect-yourself-from-the-2016-tide-of-ransomware/`
- `/pittsburgh-pa-1035/blog/why-you-need-it-services/`
- … 600 more in Ahrefs

### 8. H1 tag missing or empty  (non-indexable pages)

`issue:h1-tag-missing-or-empty-nonindexable` · manual · FLAG · decider: agency

Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply.

- `/tempe-az-1141/blog/category/blogs/page/2/`
- `/sanmateo-ca-1060/managed-it-services-in-san-carlos/page/2/`
- `/boston-ma-1089/blog/page/3/`
- `/austin-tx-1079/client-reviews/`
- `/novasouth-va-1254/blog/category/ransomware-recovery/`
- `/plymouth-mn-1102/blog/page/2/`
- `/cleveland-oh-1188/blog/category/cloud-storage/`
- `/boston-ma-1020/blog/page/3/`
- `/idahofalls-id-1207/blog/page/2/`
- `/plano-tx-1190/lp/free-cybersecurity-risk-assessment/`
- … 530 more in Ahrefs

### 9. Multiple title tags

`issue:multiple-title-tags` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/boise-id-1183/it-infrastructure-for-manufacturing/`
- `/miami-fl-1208/compliance/`
- `/greenville-sc-1006/business-data-compliance-greenville/`
- `/brandon-lakeland-fl-1222/compliance/`
- `/birmingham-al-1149/unified-communications/`
- `/dallas-tx-1036/client-reviews/`
- `/greenville-sc-1006/manufacturing-firm/`
- `/sanmarcos-tx-1047/contact-us/`
- `/birmingham-al-1149/about/`
- `/miami-fl-1208/blog/`
- … 373 more in Ahrefs

### 10. Slow server response for AI crawlers

`issue:slow-server-response-for-ai-crawlers` · hosting/cache · FLAG · decider: agency

TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM.

- `/jumpstart-your-daily-routine-by-organizing-your-desktop/`
- `/microsoft-rolls-out-new-cybersecurity-protections/`
- `/glendale-ca-1236/network-management/`
- `/lp/it-services-for-anyone/`
- `/top-managed-it-services-for-accounting-firms/`
- `/5-fun-facts-about-cybersecurity/`
- `/cmit-solutions-connect-live-annual-conference-charts-the-course-for-the-brands-five-year-vision/`
- `/mobile-device-security-critical-especially-wake-samsung-galaxy-note-7-issues/`
- `/austin-tx-1052/it-services-procurement/`
- `/lp/network-security/`
- … 197 more in Ahrefs

### 11. Multiple title tags  (non-indexable pages)

`issue:multiple-title-tags-nonindexable` · manual · FLAG · decider: agency

Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting.

- `/austin-tx-1128/contact-us/?tab=retail&service=it-support`
- `/oakpark-il-1005/it-service/compliance/?utm_source=direct&utm_medium=direct`
- `/austin-tx-1128/contact-us/?tab=education&service=it-support`
- `/austin-tx-1128/contact-us/?tab=finance&service=data-backup`
- `/oakpark-il-1005/Industries-accounting/`
- `/austin-tx-1128/contact-us/?tab=education&service=data-backup`
- `/austin-tx-1128/contact-us/?tab=manufacturing&service=unified-communications`
- `/oakpark-il-1005/Industries-government/?utm_source=direct&utm_medium=direct`
- `/austin-tx-1128/contact-us/?tab=healthcare&service=productivity-applications`
- `/boston-ma-1020/it_self_assessment/`
- … 174 more in Ahrefs

### 12. Page has broken CSS

`issue:page-has-broken-css` · manual · FLAG · decider: agency

A stylesheet the page loads 404s or errors: usually a plugin removed without cleaning its enqueue, or a CDN path. Find the URL in the page source, fix the enqueue or re-add the file.

- `/concord-ca-1107/it-guidance/`
- `/miami-fl-1208/hospitality/`
- `/concord-ca-1107/cybersecurity/`
- `/kenosha-wi-1018/it-self-assessment/`
- `/charleston-sc-1165/industries-manufacturing/`
- `/boston-ma-1020/it_self_assessment/`
- `/miami-fl-1208/healthcare/`
- `/charleston-sc-1165/industries-engineering/`
- `/livermore-ca-1203/`
- `/charleston-sc-1165/ai-insights/`
- … 75 more in Ahrefs

### 13. CSS broken

`issue:css-broken` · manual · FLAG · decider: agency

The CSS file itself returns an error; same fix as 'Page has broken CSS' (one file, many pages).

- `/long-beach-ca-1217/it-self-assessment/styles.css`
- `/brandon-lakeland-fl-1222/construction/styles.css`
- `/boston-ma-1020/it_self_assessment/styles.css`
- `/brandon-lakeland-fl-1222/healthcare/styles.css`
- `/siliconvalley-ca-1019/assets/fontawesome/all.min.css`
- `/boston-ma-1020/wp-content/cache/min/48/ajax/libs/font-awesome/6.5.2/css/fontawesome.min.css?ver=1712633913`
- `/miami-fl-1208/healthcare/styles.css`
- `/birmingham-al-1149/it-self-assessment/styles.css`
- `/fortmyers-fl-1214/CMIT%20Solutions%20of%20Plano%20%E2%80%94%20Services_files/avenir-lt-pro`
- `/cincinnati-oh-1088/it-self-assessment/styles.css`
- … 17 more in Ahrefs

### 14. JavaScript broken

`issue:javascript-broken` · manual · FLAG · decider: agency

The script file itself returns an error; same fix as 'Page has broken JavaScript'.

- `/dallas-tx-1036/ai-services/form-handler.js`
- `/dallas-tx-1036/it-support-cpa-firms-dallas/form-handler.js`
- `/dallas-tx-1036/it-service-cybersecurity/form-handler.js`
- `/dallas-tx-1036/cybersecurity-dallas-businesses/form-handler.js`
- `/dallas-tx-1036/microsoft-365/form-handler.js`
- `/dallas-tx-1036/technology-snapshot/form-handler.js`

### 15. Page has broken JavaScript

`issue:page-has-broken-javascript` · manual · FLAG · decider: agency

A script the page loads 404s or errors: plugin remnant or CDN path. Fix the enqueue; check the console on one page.

- `/dallas-tx-1036/it-service-cybersecurity/`
- `/dallas-tx-1036/it-support-cpa-firms-dallas/`
- `/dallas-tx-1036/ai-services/`
- `/dallas-tx-1036/cybersecurity-dallas-businesses/`
- `/dallas-tx-1036/technology-snapshot/`
- `/dallas-tx-1036/microsoft-365/`

### 16. HTML file size too large

`issue:html-file-size-too-large` · manual · FLAG · decider: agency

HTML over Ahrefs' size threshold: inline CSS/JS from a builder or an embedded data blob. Usually one template; check what inflates it.

- `/long-beach-ca-1217/about/`
- `/bothell-wa-1091/about/`

### 17. Robots.txt is not accessible

`issue:robots-txt-is-not-accessible` · manual · FLAG · decider: agency

robots.txt returned an error during the crawl: check it loads now (host block, WAF, or a plugin serving it). Transient if it loads.

- `/robots.txt`

### 18. Waiting on skill `fix-social-tags` (3 issue types): Open Graph tags incomplete (6177); Open Graph tags missing (1); X (Twitter) card missing (1)

`pending:fix-social-tags` · fix-social-tags · skill pending · decider: agency

Nothing by hand unless urgent: `fix-social-tags` is queued in the plan and this row disappears when it ships. Until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/wilmington-nc-1168/`
- `/powellspoint-nc-1156/contact-us/`
- `/stcharles-mo-1093/blog/`
- `/sanantonio-tx-1120/blog/mac-malware-turns-icloud-calendars-into-a-data-theft-trap/`
- `/it-solutions-support-from-cmit-solutions-of-erie-transforms-mental-health-agencys-technology/`
- `/boise-id-1183/it-infrastructure-for-manufacturing/`
- `/oakpark-il-1005/blog/finance-firms-face-new-phishing-techniques-heres-how-to-stay-ahead/`
- `/greenville-sc-1006/business-data-compliance-greenville/`
- `/everett-wa-1158/managed-it-solutions-for-defense-contractors-in-everett-wa/`
- `/how-consumer-grade-video-chat-paved-way-for-cmit-impression/`
- … 6169 more in Ahrefs

### 19. Waiting on skill `indexation-review` (8 issue types): Indexable page became non-indexable (6); Non-canonical page specified as canonical one (1); Canonical URL has no incoming internal links (14); Indexable page not in sitemap (6116); Noindex page in sitemap (2); Non-canonical page in sitemap (7); Page in multiple sitemaps (6); Sitemap in the wrong format (1)

`pending:indexation-review` · indexation-review · skill pending · decider: agency

Nothing by hand unless urgent: `indexation-review` is queued in the plan and this row disappears when it ships. Until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/statesville-nc-1218/resources/`
- `/erie-pa-1030/about/`
- `/folsom-ca-1233/`
- `/raleigh-nc-1248/resources/`
- `/denver-co-1228/managed-it-services/`
- `/greenville-sc-1006/tools-and-calculators/`
- … 6147 more in Ahrefs

### 20. Waiting on skill `fix-broken-links` (6 issue types): Canonical points to 4XX (4); 404 page (289); 4XX page (295); 5XX page (2); Page has links to broken page  (non-indexable pages) (111); Page has links to broken page (738)

`pending:fix-broken-links` · fix-broken-links · skill pending · decider: agency

Nothing by hand unless urgent: `fix-broken-links` is queued in the plan and this row disappears when it ships. Until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/greenville-sc-1006/cmit-business-risk/`
- `/boston-ma-1020/accounting-firm/`
- `/alexandria-va-1247/blog/how-can-managed-it-services-in-alexandria-va-protect-and-scale-your-business/`
- `/alexandria-va-1247/blog/why-is-cmit-solutions-alexandria-the-go-to-network-security-company-in-alexandria-va-for-your-business/`
- … 1435 more in Ahrefs

### 21. Waiting on skill `nofollow-audit` (4 issue types): Page has nofollow incoming internal links only  (non-indexable pages) (60); Page has nofollow incoming internal links only (826); Page has nofollow outgoing internal links  (non-indexable pages) (466); Page has nofollow outgoing internal links (13)

`pending:nofollow-audit` · nofollow-audit · skill pending · decider: agency

Nothing by hand unless urgent: `nofollow-audit` is queued in the plan and this row disappears when it ships. Until then: find what adds rel=nofollow to internal links (theme, plugin, editor habit); if systematic, one fix clears thousands (ruggeddepot 8k, miuraboiler 3k)

- `/category/quick-tips/page/41/`
- `/richardson-tx-1049/blog/should-you-ban-ai-on-fridays/`
- `/roanoke-va-1017/blog/category/local-it/page/3/`
- `/category/in-the-news/page/4/`
- `/newyork-ny-1095/blog/why-your-old-antivirus-wont-cut-it/`
- `/category/quick-tips/page/8/`
- `/category/case-studies/page/4/`
- `/richardson-tx-1049/blog/is-data-security-your-top-priority/`
- `/richardson-tx-1049/blog/how-to-stop-ai-projects-stalling/`
- `/category/cybersecurity/page/5/`
- … 1355 more in Ahrefs

### 22. Waiting on skill `schema-fix` (1 issue type): Structured data has Google rich results validation error (218)

`pending:schema-fix` · schema-fix · skill pending · decider: agency

Nothing by hand unless urgent: `schema-fix` is queued in the plan and this row disappears when it ships. Until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual

- `/oakpark-il-1005/blog/finance-firms-face-new-phishing-techniques-heres-how-to-stay-ahead/`
- `/bothell-wa-1091/blog/wi-fi-7-and-the-future-of-business-connectivity-what-smbs-need-to-know/`
- `/kenosha-wi-1018/blog/data-backup-disaster-recovery-the-silent-lifeline-of-southeast-wisconsin-businesses/`
- `/des-moines-ia-1210/blog/the-ceos-guide-to-vciso-in-des-moines-why-mid-sized-businesses-are-making-the-switch-in-2026/`
- `/charleston-sc-1165/blog/windows-11-for-business-unlocking-new-levels-of-productivity-and-security/`
- `/birmingham-al-1149/blog/what-happens-when-your-business-it-systems-go-down-the-real-cost-of-downtime/`
- `/austin-tx-1052/blog/your-office-manager-is-not-your-it-department-and-that-is-nobodys-fault/`
- `/bothell-wa-1091/blog/how-cyber-insurance-requirements-are-changing-business-it-strategies-in-2026/`
- `/sanmarcos-tx-1047/blog/client-spotlight-how-the-faust-hotel-stopped-firefighting-it/`
- `/kenosha-wi-1018/blog/remote-work-is-permanent-is-your-it-infrastructure-built-to-support-it-securely/`
- … 208 more in Ahrefs

### 23. Waiting on skill `redirect-rules` (4 issue types): Canonical points to redirect (20); Broken redirect (102); Redirect loop (2); 3XX redirect in sitemap (6)

`pending:redirect-rules` · redirect-rules · skill pending · decider: agency

Nothing by hand unless urgent: `redirect-rules` is queued in the plan and this row disappears when it ships. Until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/sanantonio-tx-1098/managed-it-services-san-antonio/`
- `/boston-ma-1020/cybersecurity/`
- `/burlington-nj-1230/lp/unified-communications/`
- `/boston-ma-1020/industry/`
- `/boston-ma-1020/compliance/`
- `/burlington-nj-1230/lp/it-service-package/`
- `/burlington-nj-1230/lp/it-support-service-in-burlington-area/`
- `/burlington-nj-1230/lp/cybersecurity-service-in-gurlington-area/`
- `/burlington-nj-1230/lp/need-productivity-applications-in-burlington-area/`
- `/novasouth-va-1254/network-management/`
- … 120 more in Ahrefs

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (959 pages: /houston-tx-1192/resources/page/2/, /tempe-az-1141/blog/category/blogs/page/2/, /sanmateo-ca-1060/managed-it-services-in-san-carlos/page/2/, /stlouis-mo-1042/resources/page/2/, …)

959 pages on cmitsolutions.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

**Orphan page (has no incoming internal links)** (395 pages: /the-big-takeaway-any-company-can-be-attacked/, /cmit-solutions-targets-br-n-o/, /test/, /newly-detected-malware-could-have-far-reaching-impacts/, …)

395 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Orphan page (has no incoming internal links)  (non-indexable pages)** (4 pages: /lp/it-budget-review/, /lp/it-budget/, /lp/find-your-it-model/, /lp/scenthound/)

4 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Noindex page became indexable** (2 pages: /dallas-tx-1036/client-reviews/, /shenandoah-va-1096/blog/category/it-strategy-infrastructure/)

2 pages on cmitsolutions.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

