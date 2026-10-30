# Batch fix-redirect-links: kinsta (live)

Run 2026-10-30-1052 · 5 site(s) · tolerance 25%

| site | status | swaps | staging p/m/r | live p/m/r | notes |
|---|---|---|---|---|---|
| markheardfuel | **live applied** | 19 | - | 1p/0m/1r | map redirect-map-2026-10-29.json: 19 swaps, 4 skipped<br>link check ok; 15 old URL(s) still linked, 2 other non-200 (pre-existing) |
| meshautomationinc | **live already clean** | 41 | - | 0 hits | map redirect-map-2026-10-29.json: 41 swaps, 29 skipped |
| miuraboiler | **live applied; LINK CHECK FAILED** | 28 | - | 149p/126m/2653r | map redirect-map-2026-10-22.json: 28 swaps, 217 skipped<br>link check: 8 swap target(s) not 200, 2 changed page(s) not 200; see -linkcheck.md and consider restore_changes.py |
| ruggeddepot | **live applied** | 25 | - | 0p/10m/10r | map redirect-map-2026-10-29.json: 25 swaps, 7 skipped<br>link check ok |
| setcomcorp | **live applied** | 13 | - | 1p/7m/12r | map redirect-map-2026-10-28.json: 13 swaps, 14 skipped<br>link check ok; 3 old URL(s) still linked, 2 other non-200 (pre-existing) |

## Logs

- markheardfuel: `changes\kinsta\markheardfuel\2026-10-30-1052-fix-redirect-links-live-dry.md`, `changes\kinsta\markheardfuel\2026-10-30-1052-fix-redirect-links-live-apply.md`
- meshautomationinc: `changes\kinsta\meshautomationinc\2026-10-30-1052-fix-redirect-links-live-dry.md`
- miuraboiler: `changes\kinsta\miuraboiler\2026-10-30-1053-fix-redirect-links-live-dry.md`, `changes\kinsta\miuraboiler\2026-10-30-1053-fix-redirect-links-live-apply.md`
- ruggeddepot: `changes\kinsta\ruggeddepot\2026-10-30-1055-fix-redirect-links-live-dry.md`, `changes\kinsta\ruggeddepot\2026-10-30-1056-fix-redirect-links-live-apply.md`
- setcomcorp: `changes\kinsta\setcomcorp\2026-10-30-1056-fix-redirect-links-live-dry.md`, `changes\kinsta\setcomcorp\2026-10-30-1056-fix-redirect-links-live-apply.md`

p/m/r = posts changed / postmeta rows changed / link replacements. Sites that stopped at a gate did not go further; their logs say why.
