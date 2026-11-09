# Work orders: cmitsolutions.com

Ahrefs Site Audit project 9799848 · crawl 2026-11-07 · health 97 · 91 active issue types → 43 work orders (3 decisions, 25 waiting on a skill not yet built) · generated 2026-11-09

Everything here needs a human: a template edit, a hosting ticket, a content call, or a client decision. Skills handle the rest and never show up on this list. Rows and counts refresh from each crawl; a row disappears (sheet: `cleared <date>`) when the crawl no longer shows the issue. Decisions go in the sheet's `decision_or_note` as `decision: …` and `--decisions` copies them into `clients/<slug>.yaml` → `rules.decisions`.

| # | item | goes to | tier | URLs | traffic | decider | what to do |
|---|---|---|---|---|---|---|---|
| 1 | Pages hidden from Google (noindex/nofollow): confirm intent | indexation-review | decide | 959 | 0 | client | Confirm each hidden page is meant to be (legal pages, thank-you pages and press releases usually are); record the answer in rules.decisions. Ahrefs issues folded in: Nofollow page, Noindex and nofollow page, Noindex follow page, Noindex page. |
| 2 | Orphan page (has no incoming internal links) | indexation-review | decide | 395 | 0 (top 200 of 395) | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 3 | Orphan page (has no incoming internal links)  (non-indexable pages) | indexation-review | decide | 4 | 0 | client | Per page: link it from somewhere relevant, noindex it, or merge/delete it. Catalog sites (mooringtech 4.7k) need a look at how the catalog is linked first. |
| 4 | Slow page | manual | FLAG | 1627 | 0 (top 200 of 1627) | agency | Not page weight if HTML is small: run PageSpeed/WebPageTest on the top 3 by traffic and the host's APM; deep pagination = cold cache. Hosting or theme ticket. |
| 5 | H1 tag missing or empty | manual | FLAG | 801 | 0 (top 200 of 801) | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 6 | Structured data has schema.org validation error | schema-fix | FLAG | 610 | 0 (top 200 of 610) | agency | Run the top page through the Schema Markup Validator to get the failing property; hand-coded blocks in the theme (hsfamilylaw's LegalService) are a template edit. |
| 7 | H1 tag missing or empty  (non-indexable pages) | manual | FLAG | 540 | 0 (top 200 of 540) | agency | Template edit: add an <h1> to the archive/post-type template the triage names; diff goes in changes/<provider>/<slug>/ for a human to apply. |
| 8 | Multiple title tags | manual | FLAG | 383 | 0 (top 200 of 383) | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 9 | Slow server response for AI crawlers | hosting/cache | FLAG | 207 | 0 (top 200 of 207) | agency | TTFB. Check which pages: deep pagination = cold cache (raise products-per-page); single pages at 5 s+ = PHP, run the host's APM. |
| 10 | Multiple title tags  (non-indexable pages) | manual | FLAG | 184 | 0 | agency | Two things print <title>: find the second (theme header, builder, plugin) once per site and remove it; usually one setting. |
| 11 | Indexable page not in sitemap | indexation-review | APPROVE (skill pending) | 6116 | 0 (top 200 of 6116) | agency | Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin. |
| 12 | Page has nofollow incoming internal links only | nofollow-audit | APPROVE (skill pending) | 826 | 0 (top 200 of 826) | agency | Skill `nofollow-audit` is planned but not built; until then: find what adds rel=nofollow to internal links (theme, plugin, editor habit); if systematic, one fix clears thousands (ruggeddepot 8k, miuraboiler 3k) |
| 13 | Page has nofollow outgoing internal links  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 466 | 0 (top 200 of 466) | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 14 | Structured data has Google rich results validation error | schema-fix | APPROVE (skill pending) | 218 | 0 (top 200 of 218) | agency | Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual |
| 15 | Broken redirect | redirect-rules | APPROVE (skill pending) | 102 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 16 | Page has nofollow incoming internal links only  (non-indexable pages) | nofollow-audit | APPROVE (skill pending) | 60 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: find what adds rel=nofollow to internal links (theme, plugin, editor habit); if systematic, one fix clears thousands (ruggeddepot 8k, miuraboiler 3k) |
| 17 | Canonical points to redirect | redirect-rules | APPROVE (skill pending) | 20 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 18 | Canonical URL has no incoming internal links | indexation-review | APPROVE (skill pending) | 14 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 19 | Page has nofollow outgoing internal links | nofollow-audit | APPROVE (skill pending) | 13 | 0 | agency | Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting. |
| 20 | Non-canonical page in sitemap | indexation-review | APPROVE (skill pending) | 7 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 21 | 3XX redirect in sitemap | redirect-rules | APPROVE (skill pending) | 6 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 22 | Indexable page became non-indexable | indexation-review | APPROVE (skill pending) | 6 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 23 | Page in multiple sitemaps | indexation-review | APPROVE (skill pending) | 6 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 24 | Noindex page in sitemap | indexation-review | APPROVE (skill pending) | 2 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 25 | Redirect loop | redirect-rules | APPROVE (skill pending) | 2 | 0 | agency | Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions |
| 26 | Sitemap in the wrong format | indexation-review | APPROVE (skill pending) | 1 | 0 | agency | Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision |
| 27 | Open Graph tags incomplete | fix-social-tags | AUTO (skill pending) | 6177 | 0 (top 200 of 6177) | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 28 | Open Graph tags missing | fix-social-tags | AUTO (skill pending) | 1 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 29 | X (Twitter) card missing | fix-social-tags | AUTO (skill pending) | 1 | 0 | agency | Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap |
| 30 | Page has links to broken page | fix-broken-links | AUTO/APPROVE (skill pending) | 738 | 0 (top 200 of 738) | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 31 | 4XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 295 | 0 (top 200 of 295) | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 32 | 404 page | fix-broken-links | AUTO/APPROVE (skill pending) | 289 | 0 (top 200 of 289) | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 33 | Page has links to broken page  (non-indexable pages) | fix-broken-links | AUTO/APPROVE (skill pending) | 111 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 34 | Page has broken CSS | review | ? | 85 | 0 | agency | Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster) |
| 35 | CSS broken | review | ? | 27 | 0 | agency | Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster) |
| 36 | JavaScript broken | review | ? | 6 | 0 | agency | Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster) |
| 37 | Page has broken JavaScript | review | ? | 6 | 0 | agency | Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster) |
| 38 | Canonical points to 4XX | fix-broken-links | AUTO/APPROVE (skill pending) | 4 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 39 | 5XX page | fix-broken-links | AUTO/APPROVE (skill pending) | 2 | 0 | agency | Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE) |
| 40 | HTML file size too large | review | ? | 2 | 0 | agency | Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster) |
| 41 | Noindex page became indexable | review | ? | 2 | 0 | agency | Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster) |
| 42 | Non-canonical page specified as canonical one | review | ? | 1 | 0 | agency | Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster) |
| 43 | Robots.txt is not accessible | review | ? | 1 | 0 | agency | Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster) |

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

### 4. Slow page

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

### 5. H1 tag missing or empty

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

### 6. Structured data has schema.org validation error

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

### 7. H1 tag missing or empty  (non-indexable pages)

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

### 8. Multiple title tags

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

### 9. Slow server response for AI crawlers

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

### 10. Multiple title tags  (non-indexable pages)

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

### 11. Indexable page not in sitemap

`issue:indexable-page-not-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: If every URL is /page/N/ pagination, Yoast leaves those out by design: nothing to do (work-orders skips that case). Otherwise a sitemap setting in the SEO plugin.

- `/lasvegas-nv-1206/blog/law-firm-it-support-in-las-vegas-your-fractional-it-department/`
- `/wilmington-nc-1168/`
- `/powellspoint-nc-1156/contact-us/`
- `/stcharles-mo-1093/blog/`
- `/sanantonio-tx-1120/blog/mac-malware-turns-icloud-calendars-into-a-data-theft-trap/`
- `/boise-id-1183/it-infrastructure-for-manufacturing/`
- `/oakpark-il-1005/blog/finance-firms-face-new-phishing-techniques-heres-how-to-stay-ahead/`
- `/miami-fl-1208/compliance/`
- `/greenville-sc-1006/business-data-compliance-greenville/`
- `/everett-wa-1158/managed-it-solutions-for-defense-contractors-in-everett-wa/`
- … 6106 more in Ahrefs

### 12. Page has nofollow incoming internal links only

`issue:page-has-nofollow-incoming-internal-links-only` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: find what adds rel=nofollow to internal links (theme, plugin, editor habit); if systematic, one fix clears thousands (ruggeddepot 8k, miuraboiler 3k)

- `/it-solutions-support-from-cmit-solutions-of-erie-transforms-mental-health-agencys-technology/`
- `/how-consumer-grade-video-chat-paved-way-for-cmit-impression/`
- `/southlake-tx-1197/blog/three-reasons-why-your-small-business-should-invest-in-it-help-desk-support/`
- `/microsoft-rolls-out-new-cybersecurity-protections/`
- `/philadelphia-pa-1200/blog/copilot-webinar/`
- `/tampa-fl-1078/blog/what-is-it-help-desk-support/`
- `/plymouth-mn-1102/blog/excel-just-gave-cells-a-major-upgrade/`
- `/ready-to-take-your-business-to-the-next-level/`
- `/austin-tx-1128/blog/why-retailers-are-rethinking-point-of-sale-security-after-a-rise-in-breaches/`
- `/clearlake-tx-1106/blog/ready-to-take-your-business-to-the-next-level/`
- … 816 more in Ahrefs

### 13. Page has nofollow outgoing internal links  (non-indexable pages)

`issue:page-has-nofollow-outgoing-internal-links-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

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
- … 456 more in Ahrefs

### 14. Structured data has Google rich results validation error

`issue:structured-data-has-google-rich-results-validation-error` · schema-fix · APPROVE (skill pending) · decider: agency

Skill `schema-fix` is planned but not built; until then: Organization from client file (name, logo, sameAs) via the SEO plugin; validation errors diagnosed per site, hand-coded blocks go manual

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

### 15. Broken redirect

`issue:broken-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/corporate/blog/7-reasons-why-you-should-take-disaster-preparedness-seriously`
- `/services/cloud/cloud-storage/`
- `/corporate/blog/9-reasons-why-quickbooks-still-rules-accounting-world-even-cloud-takes-over`
- `/location-directory/cmit-solutions-of-bellevue-kirkland-and-redmond/`
- `/corporate/blog/how-recognize-and-avoid-pdf-based-malware`
- `/corporate/blog/what-can-changing-face-microsoft-office-do-you`
- `/corporate/blog/five-password-management-tools-and-why-you-need-use-them`
- `/cmit-solutions-of-seattle-downtown/proactive-it-services/`
- `/local-weekly-tips/hacking-for-gold/`
- `/corporate/blog/top-10-reasons-why-hipaa-compliance-should-matter-you`
- … 92 more in Ahrefs

### 16. Page has nofollow incoming internal links only  (non-indexable pages)

`issue:page-has-nofollow-incoming-internal-links-only-nonindexable` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: find what adds rel=nofollow to internal links (theme, plugin, editor habit); if systematic, one fix clears thousands (ruggeddepot 8k, miuraboiler 3k)

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
- … 50 more in Ahrefs

### 17. Canonical points to redirect

`issue:canonical-points-to-redirect` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

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
- … 10 more in Ahrefs

### 18. Canonical URL has no incoming internal links

`issue:canonical-url-has-no-incoming-internal-links` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/oakpark-il-1005/industries-legal/`
- `/oakpark-il-1005/industries-healthcare/`
- `/lp/franchise/`
- `/oakpark-il-1005/industries-non-profit/`
- `/oakpark-il-1005/industries-education/`
- `/oakpark-il-1005/industries-government/`
- `/oakpark-il-1005/industries-construction/`
- `/frederick-md-1072/lp/productivity-applications/`
- `/oakpark-il-1005/industries-real-estate/`
- `/oakpark-il-1005/industries-engineering/`
- … 4 more in Ahrefs

### 19. Page has nofollow outgoing internal links

`issue:page-has-nofollow-outgoing-internal-links` · nofollow-audit · APPROVE (skill pending) · decider: agency

Skill `nofollow-audit` is planned but not built; until then: Find what adds rel=nofollow (theme/plugin option vs editor habit). Two legal pages = fine; thousands = one setting.

- `/how-to-prevent-password-resets/`
- `/why-cmit-solutions-new-automatic-patch-management-for-adobe-java-itunes-and-firefox-is-critical-for-small-business/`
- `/ocala-fl-1255/blog/exciting-news-cmit-solutions-opens-in-ocala-fl-bringing-expert-it-support-to-the-heart-of-north-central-florida/`
- `/go-multimedia-with-windows-live-writer/`
- `/should-you-store-your-medical-records-on-the-cloud-a-10-point-checklist/`
- `/use-email-signatures-to-ensure-people-have-your-contact-info/`
- `/the-snipping-tool-captures-screen-shots-in-a-snap-2/`
- `/pdfs-and-protected-mode/`
- `/what-does-any-to-any-mean/`
- `/austin-tx-1079/`
- … 3 more in Ahrefs

### 20. Non-canonical page in sitemap

`issue:non-canonical-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/lp/it-budget-review/`
- `/the-ai-assistant-on-your-keychain-is-still-an-endpoint/`
- `/webinars/it-budget-season-series-part-ii-three-places-your-2027-ai-budget-needs-to-go/`
- `/lp/it-budget/`
- `/lp/find-your-it-model/`
- `/ai-just-beat-12-cpas-at-month-end-close-what-it-actually-means/`
- `/lp/scenthound/`

### 21. 3XX redirect in sitemap

`issue:3xx-redirect-in-sitemap` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/industries/hotel-it-support/`
- `/network-security/`
- `/video-cherry-hill-cpa-firm-stays-secure-with-reliable-and-proactive-it-support/`
- `/industries/hospitality/`
- `/industries/hospitality-networking-solutions/`
- `/industries/finance-and-insurance/`

### 22. Indexable page became non-indexable

`issue:indexable-page-became-non-indexable` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/statesville-nc-1218/resources/`
- `/erie-pa-1030/about/`
- `/folsom-ca-1233/`
- `/raleigh-nc-1248/resources/`
- `/denver-co-1228/managed-it-services/`
- `/greenville-sc-1006/tools-and-calculators/`

### 23. Page in multiple sitemaps

`issue:page-in-multiple-sitemaps` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/the-snipping-tool-captures-screen-shots-in-a-snap/`
- `/how-powerful-is-video-as-a-promotional-tool/`
- `/case-study/when-the-midnight-it-call-gets-answered/`
- `/the-snipping-tool-captures-screen-shots-in-a-snap-2/`
- `/case-study/public-safety-cybersecurity-how-cmit-solutions-helps-madison-fire-department-protect-critical-operations/`
- `/use-ctrlk-to-add-hyperlinks-in-gmail-messages/`

### 24. Noindex page in sitemap

`issue:noindex-page-in-sitemap` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/category/featured/`
- `/category/uncategorized/`

### 25. Redirect loop

`issue:redirect-loop` · redirect-rules · APPROVE (skill pending) · decider: agency

Skill `redirect-rules` is planned but not built; until then: fix the rule itself in the redirect plugin: collapse chains, 302→301, retarget loops and homepage dumps, chase 404s that still get impressions

- `/stcharles-mo-1093/why-cmit/`
- `/siliconvalley-ca-1019/why-cmit/`

### 26. Sitemap in the wrong format

`issue:sitemap-in-the-wrong-format` · indexation-review · APPROVE (skill pending) · decider: agency

Skill `indexation-review` is planned but not built; until then: SEO-plugin sitemap and index settings; noindex is usually intent, so confirm before changing; orphans get a link/noindex/merge decision

- `/sitemap.rss`

### 27. Open Graph tags incomplete

`issue:open-graph-tags-incomplete` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

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
- … 6167 more in Ahrefs

### 28. Open Graph tags missing

`issue:open-graph-tags-missing` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/bellevue-wa-1140/blog/author/dstewart/`

### 29. X (Twitter) card missing

`issue:x-twitter-card-missing` · fix-social-tags · AUTO (skill pending) · decider: agency

Skill `fix-social-tags` is planned but not built; until then: one SEO-plugin setting per site: default social image and X cards on; roster-wide, cheap

- `/bellevue-wa-1140/blog/author/dstewart/`

### 30. Page has links to broken page

`issue:page-has-links-to-broken-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/boise-id-1183/it-infrastructure-for-manufacturing/`
- `/miami-fl-1208/compliance/`
- `/greenville-sc-1006/business-data-compliance-greenville/`
- `/how-consumer-grade-video-chat-paved-way-for-cmit-impression/`
- `/philadelphia-pa-1200/blog/ransomware/`
- `/brandon-lakeland-fl-1222/compliance/`
- `/birmingham-al-1149/unified-communications/`
- `/philadelphia-pa-1200/blog/copilot-webinar/`
- `/sanmarcos-tx-1047/contact-us/`
- `/charleston-sc-1165/blog/how-to-identify-business-processes-ready-for-ai-automation/`
- … 728 more in Ahrefs

### 31. 4XX page

`issue:4xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/blog/top-10-reasons-why-windows-81-worth-upgrade`
- `/wp-content/uploads/2012/04/phisher.jpg`
- `/what-is-spoofing-in-cyber-security/+18003992648`
- `/cincinnati-oh-1088/industry/`
- `/services/hardware-purchasing/`
- `/blog/why-strong-network-security-must-wake-shellshock-bug`
- `/charleston-sc-1165/?page_id=4`
- `/birmingham-al-1149/accessibility/`
- `/wp-content/uploads/2015/02/iStock_000029894058Large_0.jpg`
- `/blog/your-small-business-prepared-natural-disaster`
- … 285 more in Ahrefs

### 32. 404 page

`issue:404-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/blog/top-10-reasons-why-windows-81-worth-upgrade`
- `/wp-content/uploads/2012/04/phisher.jpg`
- `/what-is-spoofing-in-cyber-security/+18003992648`
- `/cincinnati-oh-1088/industry/`
- `/services/hardware-purchasing/`
- `/blog/why-strong-network-security-must-wake-shellshock-bug`
- `/charleston-sc-1165/?page_id=4`
- `/birmingham-al-1149/accessibility/`
- `/wp-content/uploads/2015/02/iStock_000029894058Large_0.jpg`
- `/blog/your-small-business-prepared-natural-disaster`
- … 279 more in Ahrefs

### 33. Page has links to broken page  (non-indexable pages)

`issue:page-has-links-to-broken-page-nonindexable` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/oakpark-il-1005/it-service/compliance/?utm_source=direct&utm_medium=direct`
- `/oakpark-il-1005/Industries-accounting/`
- `/austin-tx-1052/client-reviews/`
- `/lasvegas-nv-1206/blog/category/local-it/page/10/`
- `/oakpark-il-1005/Industries-government/?utm_source=direct&utm_medium=direct`
- `/lasvegas-nv-1206/blog/page/2/`
- `/miami-fl-1208/blog/page/2/`
- `/chicago-il-1223/blog/page/3/`
- `/oakpark-il-1005/it-service/productivity-applications/?utm_source=direct&utm_medium=direct`
- `/birmingham-al-1149/cybersecurity-birmingham//`
- … 101 more in Ahrefs

### 34. Page has broken CSS

`issue:page-has-broken-css` · review · ? · decider: agency

Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster)

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

### 35. CSS broken

`issue:css-broken` · review · ? · decider: agency

Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster)

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

### 36. JavaScript broken

`issue:javascript-broken` · review · ? · decider: agency

Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster)

- `/dallas-tx-1036/ai-services/form-handler.js`
- `/dallas-tx-1036/it-support-cpa-firms-dallas/form-handler.js`
- `/dallas-tx-1036/it-service-cybersecurity/form-handler.js`
- `/dallas-tx-1036/cybersecurity-dallas-businesses/form-handler.js`
- `/dallas-tx-1036/microsoft-365/form-handler.js`
- `/dallas-tx-1036/technology-snapshot/form-handler.js`

### 37. Page has broken JavaScript

`issue:page-has-broken-javascript` · review · ? · decider: agency

Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster)

- `/dallas-tx-1036/it-service-cybersecurity/`
- `/dallas-tx-1036/it-support-cpa-firms-dallas/`
- `/dallas-tx-1036/ai-services/`
- `/dallas-tx-1036/cybersecurity-dallas-businesses/`
- `/dallas-tx-1036/technology-snapshot/`
- `/dallas-tx-1036/microsoft-365/`

### 38. Canonical points to 4XX

`issue:canonical-points-to-4xx` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/greenville-sc-1006/cmit-business-risk/`
- `/boston-ma-1020/accounting-firm/`
- `/alexandria-va-1247/blog/how-can-managed-it-services-in-alexandria-va-protect-and-scale-your-business/`
- `/alexandria-va-1247/blog/why-is-cmit-solutions-alexandria-the-go-to-network-security-company-in-alexandria-va-for-your-business/`

### 39. 5XX page

`issue:5xx-page` · fix-broken-links · AUTO/APPROVE (skill pending) · decider: agency

Skill `fix-broken-links` is planned but not built; until then: sibling of fix-redirect-links: 404 target with an obvious replacement → rewrite (AUTO); otherwise unlink or pick a target (APPROVE)

- `/erie-pa-1030/about/`
- `/erie-pa-1030/partners-and-certifications/`

### 40. HTML file size too large

`issue:html-file-size-too-large` · review · ? · decider: agency

Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster)

- `/long-beach-ca-1217/about/`
- `/bothell-wa-1091/about/`

### 41. Noindex page became indexable

`issue:noindex-page-became-indexable` · review · ? · decider: agency

Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster)

- `/dallas-tx-1036/client-reviews/`
- `/shenandoah-va-1096/blog/category/it-strategy-infrastructure/`

### 42. Non-canonical page specified as canonical one

`issue:non-canonical-page-specified-as-canonical-one` · review · ? · decider: agency

Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster)

- `/boston-ma-1020/accounting-firm/`

### 43. Robots.txt is not accessible

`issue:robots-txt-is-not-accessible` · review · ? · decider: agency

Not classified in routes.yaml yet: decide the handler and tier there (note: not yet classified; rare on this roster)

- `/robots.txt`

## Client briefs

One paragraph per client decision, ready to paste into an email. Agency decisions are in the table above.

**Pages hidden from Google (noindex/nofollow): confirm intent** (959 pages: /houston-tx-1192/resources/page/2/, /tempe-az-1141/blog/category/blogs/page/2/, /sanmateo-ca-1060/managed-it-services-in-san-carlos/page/2/, /stlouis-mo-1042/resources/page/2/, …)

959 pages on cmitsolutions.com are set so Google does not index them (or does not follow their links). That is normal for legal pages, thank-you pages and press releases, so we expect this is deliberate. Two options: (a) leave them hidden, which we recommend if they are not pages you want people to find in Google; (b) tell us which ones should be visible and we will switch them on. We will not change anything until you confirm.

**Orphan page (has no incoming internal links)** (395 pages: /the-big-takeaway-any-company-can-be-attacked/, /cmit-solutions-targets-br-n-o/, /test/, /newly-detected-malware-could-have-far-reaching-impacts/, …)

395 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

**Orphan page (has no incoming internal links)  (non-indexable pages)** (4 pages: /lp/it-budget-review/, /lp/it-budget/, /lp/find-your-it-model/, /lp/scenthound/)

4 pages on the site are not linked from any other page, so visitors and Google only find them through the sitemap. For each one: link to it from a relevant page, hide it from search, or remove it. Tell us which pages still matter and we will handle the rest.

