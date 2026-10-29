# Handoff: fix-images

Status as of 2026-10-29 (evening). Read this at the start of the chat dedicated to this skill. The repo is the source of truth: github.com/graterdigital/Low-Hanging-Fruit, cloned on Greg's PC at `C:\Users\greg\Documents\Low-Hanging-Fruit`. Mirror of the project doc `claude/skill-fix-images.md`; update both.

## What the skill does

Shrinks oversized images **in place, same URL, same format** (resize over 2560px long edge, lossy-PNG quantize / JPEG re-encode), regenerates thumbnails for those attachments, purges stale WebP conversions and caches. AUTO tier. Also inventories alt-text gaps and broken/redirected image sources for APPROVE work, but never writes alt text or content.

Decision made this chat: no format conversion and no URL swaps in this skill. WebP delivery is the plugin's/host's job; this skill shrinks the originals everything is derived from.

## Where it lives

- `skills/fix-images/SKILL.md`: procedure, tiers, defaults, rollback.
- `scripts/fix_images.py`: runner. `--probe` → `reports/<slug>/image-inventory-<crawl>.json` + `images-<crawl>.md`; default = dry run (pull + compress locally, no push); `--apply`; `--target live`; `--yes`; `--only`, `--max-edge`, `--min-gain`, `--png-quality`, `--jpeg-quality`. Reuses `build_redirect_map.py`'s `.env`/Ahrefs helpers.
- `scripts/php/image_inventory.php`: read-only, runs via `wp eval-file`. Server tools, optimizer-plugin state (WebP Express config + converted-file counts), per-file facts (attachment ID, dims, sub-sizes, references, featured/ACF use), `<img>`-without-alt scan over post_content + postmeta, missing-file scan.
- Logs: `changes/<provider>/<slug>/<stamp>-fix-images-<target>-<dry|apply>.md`; originals in `backup/<stamp>-fix-images-<target>/orig/`, compressed in `new/` (git-ignored).

Compression runs on Greg's PC (needs `pip install pillow`; `pngquant` + `oxipng` on PATH are better but optional and the log records which was used). Live-tested on hsfamilylaw 2026-10-29 with the Pillow path only (no pngquant on Greg's PC yet).

## Pilot: hsfamilylaw.com (Ahrefs crawl 2026-10-29) — DONE on live

- 26 PNGs flagged, 53 MB of originals; with their sub-sizes, **102 MB on disk → 26 MB** after the run (26 originals + 108 sub-size files, all replaced, none under the 15% floor). Blog/practice-area graphics and the site-wide `HS-BG-Image.png` dropped 82–89%; attorney headshots (transparent backgrounds → Pillow's octree quantizer) dropped 55–69%.
- Probe findings that shaped the skill: the 1024px `large` sub-sizes were 0.9–1.6 MB each and are what pages actually load (originals are referenced through ACF image fields and featured images); WordPress regenerates PNG thumbs as truecolor, so the skill now compresses every sub-size file in place and only regenerates when an original was resized (none were; max was 1920px).
- Run log: probe 14:25 → staging dry 14:43 → staging apply 14:52 → **live apply 15:03** (`changes/kinsta/hsfamilylaw/2026-10-29-1503-fix-images-live-apply.md`). Object cache flush ok; `wp kinsta cache purge --all` works on Kinsta and is logged. 138 stray `.webp` files for these images removed on live (142 on staging).
- WebP Express was active and had produced 2,464 `.webp` files but served none of them (Kinsta is Nginx; its `.htaccess` rules do nothing there and it wasn't in Alter-HTML mode). Greg removed the plugin and enabled **Kinsta CDN lossy image optimization** at the server level the same afternoon. ~1,880 stray `.webp` siblings remain elsewhere in `uploads/`; harmless, sweep later.
- Alt text scan (111 rows) agrees with Ahrefs: Tier A (alt attribute absent, published) = 5 rows = Ahrefs' 5 pages. Tier B 42 (`alt=""` inline), Tier C 59 (featured images with empty attachment alt), Tier D 4 (drafts). Broken srcs: 0. All still open; see `reports/hsfamilylaw/images-2026-10-29.md`.
- Still to do here: a recrawl to confirm "Image file size too large" clears; a fresh `--probe` to confirm Kinsta's CDN now serves WebP to browsers; visual spot-check of the headshots at 100% (not done before apply).

## Open items

- pngquant on Greg's PC: headshots would likely go from ~60% to 70–80% reduction and with less banding risk; rerun `--target live --apply` after installing (idempotent enough: already-quantized files just shrink a bit more or stay under the floor).
- `alt-text-apply`: write-back from an edited CSV (featured image → `_wp_attachment_image_alt`; inline → attribute insert into the exact tag in post_content/postmeta). Same dry/apply/log contract.
- Thumbnail regeneration for files with no attachment ID (edited `-eNNNN` copies, direct uploads): compressed by path, thumbs untouched. See what the probe finds.
- Batch runner across a host, like `batch_fix_redirect_links.py`, once two sites are clean.
- Elementor/WPBakery sites: image references in builder JSON are not an issue for this skill (URLs don't change), but the alt scan only reads `<img>` tags; builder widgets keep alt in their JSON. Extend the scan when the first builder site runs.
- Server-side compression (Imagick/pngquant on the host) if the local round-trip proves slow on sites with hundreds of files.
