# fix-images: slepianfirm.com (staging)

Run 2026-10-29-1714 · mode **dry** · alias `slepianfirm-staging` · provider `kinsta` · inventory `image-inventory-2026-10-29.json` · max edge 2560px · min gain 15% · PNG 80-98 · JPEG q82

Tools: pngquant yes, oxipng no, optipng no, jpegoptim no

**0 KB → 0 KB** across 0 files (0 would be replaced).

| file | kind | attachment | before | after | gain | steps | action |
|---|---|---|---|---|---|---|---|

## Rollback

Originals are in `backup/2026-10-29-1714-fix-images-staging/orig/`. To restore one: `scp backup/.../orig/<name> slepianfirm-staging:<remote path from the table>` then `wp media regenerate <id> --yes`.

## Not done by this run

Alt text and broken/redirected images are in the probe report (`reports/<slug>/images-<crawl>.md`) and are APPROVE-tier, per page.
