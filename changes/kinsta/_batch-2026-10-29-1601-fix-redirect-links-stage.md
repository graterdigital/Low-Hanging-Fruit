# Batch fix-redirect-links: kinsta (stage only)

Run 2026-10-29-1601 · 2 site(s) · tolerance 25%

| site | status | swaps | staging p/m/r | live p/m/r | notes |
|---|---|---|---|---|---|
| miuraboiler | **staged** | 28 | 85p/2m/112r | - | map redirect-map-2026-10-22.json: 28 swaps, 203 skipped<br>23 swap(s) had no hits on staging (theme/builder/already fixed): https://miuraboiler.com/reps/premium-mechanical-and-automation-inc/rep-locator, https://miuraboiler.com/reps/thermal-product-solutions/rep-locator, https://miuraboiler.com/reps/atlanta-southeast-branch/rep-locator ...<br>elementor json ok (188 rows) |
| ruggeddepot | **staged** | 1 | 0p/1m/1r | - | map redirect-map-2026-10-29.json: 1 swaps, 6 skipped<br>elementor json ok (3 rows) |

## Logs

- miuraboiler: `changes\kinsta\miuraboiler\2026-10-29-1601-fix-redirect-links-staging-dry.md`, `changes\kinsta\miuraboiler\2026-10-29-1602-fix-redirect-links-staging-apply.md`
- ruggeddepot: `changes\kinsta\ruggeddepot\2026-10-29-1602-fix-redirect-links-staging-dry.md`, `changes\kinsta\ruggeddepot\2026-10-29-1602-fix-redirect-links-staging-apply.md`

p/m/r = posts changed / postmeta rows changed / link replacements. Sites that stopped at a gate did not go further; their logs say why.
