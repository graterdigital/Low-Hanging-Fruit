# fix-images: forwardfacing.com (staging)

Run 2026-10-29-1702 · mode **dry** · alias `forwardfacing-staging` · provider `kinsta` · inventory `image-inventory-2026-10-29.json` · max edge 2560px · min gain 15% · PNG 80-98 · JPEG q82

Tools: pngquant yes, oxipng no, optipng no, jpegoptim no

**11.76 MB → 7.36 MB** across 12 files (7 would be replaced).

| file | kind | attachment | before | after | gain | steps | action |
|---|---|---|---|---|---|---|---|
| `2026/01/what-makes-us-unique-forward-facing-pod.png` | original | 9259 | 3.31 MB | 1.25 MB | 62.2% | pngquant 80-98 | would replace |
| `2026/01/what-makes-us-unique-forward-facing-pod-400x291.png` | sub-size medium | 9259 | 158 KB | 59 KB | 62.4% | pngquant 80-98 | would replace |
| `2026/01/what-makes-us-unique-forward-facing-pod-1024x745.png` | sub-size large | 9259 | 937 KB | 346 KB | 63.1% | pngquant 80-98 | would replace |
| `2026/01/what-makes-us-unique-forward-facing-pod-150x150.png` | sub-size thumbnail | 9259 | 38 KB | 15 KB | 59.8% | pngquant 80-98 | would replace |
| `2026/01/what-makes-us-unique-forward-facing-pod-768x559.png` | sub-size medium_large | 9259 | 537 KB | 198 KB | 63.1% | pngquant 80-98 | would replace |
| `2026/01/what-makes-us-unique-forward-facing-pod-1536x1117.png` | sub-size 1536x1536 | 9259 | 1.99 MB | 780 KB | 61.7% | pngquant 80-98 | would replace |
| `2026/01/andee-and-mali-facing-forward-podcast.png` | original | 9254 | 1.81 MB | 1.81 MB | 0.0% | pngquant: quality floor not met, kept pixels | kept (gain below threshold) |
| `2026/01/andee-and-mali-facing-forward-podcast-400x225.png` | sub-size medium | 9254 | 145 KB | 55 KB | 62.1% | pngquant 80-98 | would replace |
| `2026/01/andee-and-mali-facing-forward-podcast-1024x576.png` | sub-size large | 9254 | 808 KB | 808 KB | 0.0% | pngquant: quality floor not met, kept pixels | kept (gain below threshold) |
| `2026/01/andee-and-mali-facing-forward-podcast-150x150.png` | sub-size thumbnail | 9254 | 42 KB | 42 KB | 0.0% | pngquant: quality floor not met, kept pixels | kept (gain below threshold) |
| `2026/01/andee-and-mali-facing-forward-podcast-768x432.png` | sub-size medium_large | 9254 | 482 KB | 482 KB | 0.0% | pngquant: quality floor not met, kept pixels | kept (gain below threshold) |
| `2026/01/andee-and-mali-facing-forward-podcast-1536x864.png` | sub-size 1536x1536 | 9254 | 1.57 MB | 1.57 MB | 0.0% | pngquant: quality floor not met, kept pixels | kept (gain below threshold) |

## Rollback

Originals are in `backup/2026-10-29-1702-fix-images-staging/orig/`. To restore one: `scp backup/.../orig/<name> forwardfacing-staging:<remote path from the table>` then `wp media regenerate <id> --yes`.

## Not done by this run

Alt text and broken/redirected images are in the probe report (`reports/<slug>/images-<crawl>.md`) and are APPROVE-tier, per page.
