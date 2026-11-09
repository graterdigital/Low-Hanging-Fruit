# fix-images: hsfamilylaw.com (staging)

Run 2026-11-09-0830 · mode **dry** · alias `hsfamilylaw-staging` · provider `kinsta` · inventory `image-inventory-2026-10-29.json` · **RESIZE ONLY** (Lanczos downscale over 2560px, saved at full quality; no lossy compression)

**16.82 MB → 16.82 MB** across 12 files (0 would be replaced).

| file | kind | attachment | before | after | gain | steps | action |
|---|---|---|---|---|---|---|---|
| `2026/04/andrea-dyer-hastings-family-law-and-divorce-attorney.png` | original | 6161 | 1.79 MB | 1.79 MB | 0.0% | 1200x1200 within 2560px, no resize needed | kept (no resize needed) |
| `2026/04/mali-shadmehry-family-law-and-divorce-attorney.png` | original | 6168 | 1.65 MB | 1.65 MB | 0.0% | 1200x1200 within 2560px, no resize needed | kept (no resize needed) |
| `2026/04/cathy-cooper-family-law-and-divorce-attorney.png` | original | 6179 | 1.51 MB | 1.51 MB | 0.0% | 1200x1200 within 2560px, no resize needed | kept (no resize needed) |
| `2026/04/lily-lutton-family-law-and-divorce-attorney.png` | original | 6180 | 1.56 MB | 1.56 MB | 0.0% | 1200x1200 within 2560px, no resize needed | kept (no resize needed) |
| `2026/04/nicole-crites-family-law-and-divorce-attorney.png` | original | 6188 | 1.36 MB | 1.36 MB | 0.0% | 1200x1200 within 2560px, no resize needed | kept (no resize needed) |
| `2026/04/sarah-price-family-law-and-divorce-attorney-1-e1781711488599.png` | original | 6197 | 1.27 MB | 1.27 MB | 0.0% | 1200x1200 within 2560px, no resize needed | kept (no resize needed) |
| `2026/04/lisa-malas-family-law-and-divorce-attorney.png` | original | 6174 | 1.30 MB | 1.30 MB | 0.0% | 1200x1200 within 2560px, no resize needed | kept (no resize needed) |
| `2026/04/elizabeth-findley-family-law-and-divorce-attorney.png` | original | 6177 | 1.26 MB | 1.26 MB | 0.0% | 1200x1200 within 2560px, no resize needed | kept (no resize needed) |
| `2026/04/madison-alexander-family-law-and-divorce-attorney.png` | original | 6190 | 1.30 MB | 1.30 MB | 0.0% | 1200x1200 within 2560px, no resize needed | kept (no resize needed) |
| `2026/09/Jordan-Alexis-Fox-Attorney-Hastings-Shadmehry.png` | original | 6512 | 1.35 MB | 1.35 MB | 0.0% | 1200x1200 within 2560px, no resize needed | kept (no resize needed) |
| `2026/08/rhonda-smith-attorney-hastings-shadmehry-1.png` | original | 6471 | 1.24 MB | 1.24 MB | 0.0% | 1200x1200 within 2560px, no resize needed | kept (no resize needed) |
| `2026/08/Kristy-Seidenberg-Hastings-Shadmehry-1.png` | original | 6484 | 1.25 MB | 1.25 MB | 0.0% | 1200x1200 within 2560px, no resize needed | kept (no resize needed) |

## Rollback

Originals are in `backup/2026-11-09-0830-fix-images-staging/orig/`. To restore one: `scp backup/.../orig/<name> hsfamilylaw-staging:<remote path from the table>` then `wp media regenerate <id> --yes`.

## Not done by this run

Alt text and broken/redirected images are in the probe report (`reports/<slug>/images-<crawl>.md`) and are APPROVE-tier, per page.
