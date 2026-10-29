# Batch fix-redirect-links: kinsta (stage only)

Run 2026-10-29-1612 · 2 site(s) · tolerance 25%

| site | status | swaps | staging p/m/r | live p/m/r | notes |
|---|---|---|---|---|---|
| miuraboiler | **staged** | 28 | 2p/10m/17r | - | map redirect-map-2026-10-22.json: 28 swaps, 217 skipped<br>27 swap(s) had no hits on staging (theme/builder/already fixed): https://miuraboiler.com/reps/premium-mechanical-and-automation-inc/rep-locator, https://miuraboiler.com/reps/thermal-product-solutions/rep-locator, https://miuraboiler.com/reps/atlanta-southeast-branch/rep-locator ...<br>elementor json ok (188 rows) |
| ruggeddepot | **staged** | 25 | 0p/52m/72r | - | map redirect-map-2026-10-29.json: 25 swaps, 7 skipped<br>12 swap(s) had no hits on staging (theme/builder/already fixed): https://ruggeddepot.com/all-getac-models/handhelds-all-getac-models/, https://ruggeddepot.com/all-getac-models/2-in-1s-all-getac-models/, https://ruggeddepot.com/all-getac-models/laptops-all-getac-models/ ...<br>1 wp_options row(s) still reference old URLs; see the -options.md log<br>elementor json ok (3 rows) |

## Logs

- miuraboiler: `changes\kinsta\miuraboiler\2026-10-29-1613-fix-redirect-links-staging-dry.md`, `changes\kinsta\miuraboiler\2026-10-29-1613-fix-redirect-links-staging-apply.md`
- ruggeddepot: `changes\kinsta\ruggeddepot\2026-10-29-1615-fix-redirect-links-staging-dry.md`, `changes\kinsta\ruggeddepot\2026-10-29-1616-fix-redirect-links-staging-apply.md`

p/m/r = posts changed / postmeta rows changed / link replacements. Sites that stopped at a gate did not go further; their logs say why.
