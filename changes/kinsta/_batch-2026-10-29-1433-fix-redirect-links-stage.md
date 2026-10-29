# Batch fix-redirect-links: kinsta (stage only)

Run 2026-10-29-1433 · 13 site(s) · tolerance 25%

| site | status | swaps | staging p/m/r | live p/m/r | notes |
|---|---|---|---|---|---|
| atlantaspecializedcare | **staged** | 33 | 5p/748m/1129r | - | map redirect-map-2026-10-29.json: 33 swaps, 10 skipped<br>1 swap(s) had no hits on staging (theme/builder/already fixed): https://atlantaspecializedcare.com/blog |
| fenceworks-staging | **nothing to do** | 0 | - | - | map redirect-map-2026-10-28.json: 0 swaps, 3 skipped |
| fenceworksofga | **nothing to do** | 0 | - | - | map redirect-map-2026-10-29.json: 0 swaps, 3 skipped |
| forwardfacing | **staged** | 3 | 0p/15m/15r | - | map redirect-map-2026-10-29.json: 3 swaps, 3 skipped<br>1 swap(s) had no hits on staging (theme/builder/already fixed): https://forwardfacing.com/terms-of-service<br>1 wp_options row(s) still reference old URLs; see the -options.md log |
| hsfamilylaw | **nothing to do** | 0 | - | - | map redirect-map-2026-10-29.json: 0 swaps, 21 skipped |
| markheardfuel | **staged** | 19 | 12p/71m/83r | - | map redirect-map-2026-10-29.json: 19 swaps, 4 skipped<br>13 swap(s) had no hits on staging (theme/builder/already fixed): https://markheardfuel.com/service-areas/cumming-ga-propane-company/, https://markheardfuel.com/service-areas/dawsonville-ga-propane/, https://markheardfuel.com/service-areas/gainesville-ga-propane/ ...<br>16 wp_options row(s) still reference old URLs; see the -options.md log |
| meshautomationinc | **staged** | 41 | 19p/70m/126r | - | map redirect-map-2026-10-29.json: 41 swaps, 29 skipped<br>7 swap(s) had no hits on staging (theme/builder/already fixed): https://meshautomationinc.com/warehouse-automation-systems-vs-traditional-storage-workflows/, https://meshautomationinc.com/other-services/factory-service-and-support/, https://meshautomationinc.com/categorycpt/robotic-tending/page/2/ ...<br>3 wp_options row(s) still reference old URLs; see the -options.md log |
| miuraboiler | **staged** | 29 | 85p/60m/188r | - | map redirect-map-2026-10-22.json: 29 swaps, 101 skipped<br>23 swap(s) had no hits on staging (theme/builder/already fixed): https://miuraboiler.com/reps/premium-mechanical-and-automation-inc/rep-locator, https://miuraboiler.com/reps/thermal-product-solutions/rep-locator, https://miuraboiler.com/reps/atlanta-southeast-branch/rep-locator ... |
| nativecustomstone | **needs staging** | 86 | - | - | map redirect-map-2026-10-29.json: 86 swaps, 20 skipped |
| ruggeddepot | **nothing to do** | 0 | - | - | map redirect-map-2026-10-29.json: 0 swaps, 6 skipped |
| setcomcorp | **staged** | 13 | 10p/115m/254r | - | map redirect-map-2026-10-28.json: 13 swaps, 14 skipped<br>2 swap(s) had no hits on staging (theme/builder/already fixed): https://setcomcorp.com/wwett-2025-show, https://setcomcorp.com/shop<br>7 wp_options row(s) still reference old URLs; see the -options.md log |
| slepianfirm | **staged** | 32 | 3p/92m/103r | - | map redirect-map-2026-10-29.json: 32 swaps, 2 skipped<br>26 swap(s) had no hits on staging (theme/builder/already fixed): https://www.slepianfirm.com/peachtree-city-real-estate-attorney/closing-checklist-for-lenders-and-mortgage-brokers/, https://www.slepianfirm.com/peachtree-city-real-estate-attorney/closing-checklist-for-the-agent/, https://www.slepianfirm.com/peachtree-city-real-estate-attorney/glossary-of-closing-terminology/ ... |
| technikpackaging | **staged** | 6 | 31p/1m/35r | - | map redirect-map-2026-10-29.json: 6 swaps, 4 skipped<br>2 wp_options row(s) still reference old URLs; see the -options.md log |

## Logs

- atlantaspecializedcare: `changes\kinsta\atlantaspecializedcare\2026-10-29-1433-fix-redirect-links-staging-dry.md`, `changes\kinsta\atlantaspecializedcare\2026-10-29-1433-fix-redirect-links-staging-apply.md`
- forwardfacing: `changes\kinsta\forwardfacing\2026-10-29-1434-fix-redirect-links-staging-dry.md`, `changes\kinsta\forwardfacing\2026-10-29-1434-fix-redirect-links-staging-apply.md`
- markheardfuel: `changes\kinsta\markheardfuel\2026-10-29-1434-fix-redirect-links-staging-dry.md`, `changes\kinsta\markheardfuel\2026-10-29-1434-fix-redirect-links-staging-apply.md`
- meshautomationinc: `changes\kinsta\meshautomationinc\2026-10-29-1436-fix-redirect-links-staging-dry.md`, `changes\kinsta\meshautomationinc\2026-10-29-1436-fix-redirect-links-staging-apply.md`
- miuraboiler: `changes\kinsta\miuraboiler\2026-10-29-1437-fix-redirect-links-staging-dry.md`, `changes\kinsta\miuraboiler\2026-10-29-1438-fix-redirect-links-staging-apply.md`
- setcomcorp: `changes\kinsta\setcomcorp\2026-10-29-1440-fix-redirect-links-staging-dry.md`, `changes\kinsta\setcomcorp\2026-10-29-1441-fix-redirect-links-staging-apply.md`
- slepianfirm: `changes\kinsta\slepianfirm\2026-10-29-1441-fix-redirect-links-staging-dry.md`, `changes\kinsta\slepianfirm\2026-10-29-1441-fix-redirect-links-staging-apply.md`
- technikpackaging: `changes\kinsta\technikpackaging\2026-10-29-1441-fix-redirect-links-staging-dry.md`, `changes\kinsta\technikpackaging\2026-10-29-1442-fix-redirect-links-staging-apply.md`

p/m/r = posts changed / postmeta rows changed / link replacements. Sites that stopped at a gate did not go further; their logs say why.
