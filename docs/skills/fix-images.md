# Handoff: fix-images

Status as of 2026-10-29 (late evening). Read this at the start of the chat dedicated to this skill. The repo is the source of truth: github.com/graterdigital/Low-Hanging-Fruit, cloned on Greg's PC at `C:\Users\greg\Documents\Low-Hanging-Fruit`. Mirror of the project doc `claude/skill-fix-images.md`; update both.

## What the skill does

Shrinks oversized images **in place, same URL, same format** (resize over 2560px long edge, lossy-PNG quantize / JPEG re-encode), regenerates thumbnails for those attachments, purges stale WebP conversions and caches. AUTO tier. Also inventories alt-text gaps and broken/redirected image sources for APPROVE work, but never writes alt text or content.

Decision made this chat: no format conversion and no URL swaps in this skill. WebP delivery is the plugin's/host's job; this skill shrinks the originals everything is derived from.

## Where it lives

- `skills/fix-images/SKILL.md`: procedure, tiers, defaults, rollback.
- `scripts/fix_images.py`: runner. `--probe` → `reports/<slug>/image-inventory-<crawl>.json` + `images-<crawl>.md`; default = dry run (pull + compress locally, no push); `--apply`; `--target live`; `--yes`; `--alt-csv` (review sheet, no SSH); `--alt-apply <csv>` (dry/apply/live like the rest); `--only`, `--max-edge`, `--min-gain`, `--png-quality`, `--jpeg-quality`. Reuses `build_redirect_map.py`'s `.env`/Ahrefs helpers.
- `scripts/php/apply_alt.php`: writes alt from the reviewed CSV (featured → `_wp_attachment_image_alt`; inline → attribute replace/insert on the matching `<img>` by src path, host-agnostic). Regex unit-tested locally; not yet run on a site.
- `scripts/php/image_inventory.php`: read-only, runs via `wp eval-file`. Server tools, optimizer-plugin state (WebP Express config + converted-file counts), per-file facts (attachment ID, dims, sub-sizes, references, featured/ACF use), `<img>`-without-alt scan over post_content + postmeta, missing-file scan.
- Logs: `changes/<provider>/<slug>/<stamp>-fix-images-<target>-<dry|apply>.md`; originals in `backup/<stamp>-fix-images-<target>/orig/`, compressed in `new/` (git-ignored).

Compression runs on Greg's PC (needs `pip install pillow`; `pngquant` + `oxipng` on PATH are better but optional and the log records which was used). Live-tested on hsfamilylaw 2026-10-29 with the Pillow path only (no pngquant on Greg's PC yet).

## What went wrong on 2026-10-29 (read this first)

1. **Pillow's quantizer wrecked the headshots.** The 11 attorney photos are photographs saved as PNG with smooth gradient backgrounds; 256-colour quantization with dithering made them look awful at full size. Nobody looked at `new/` vs `orig/` before the staging or live apply, and Greg then ran a second live apply (15:36) after installing pngquant, which quantized the already-quantized files. Fixed by `restore_images.py` from the 15:03 live backup (the true originals), 55 files, plus fresh `.webp` siblings. Skill now: PNGs are skipped unless pngquant is on PATH (`--allow-pillow` overrides), default `--png-quality 80-98`, and SKILL.md says the visual check is mandatory before any apply.
2. **Deleting `.webp` siblings blanked the images.** Kinsta's Nginx still serves `name.webp` to WebP-capable browsers after WebP Express is removed (naming: `photo.webp`, not `photo.png.webp`). The run deleted the siblings of exactly the 26 replaced files, so exactly those 26 went blank on staging (files on disk were fine). Skill now: deletion is opt-in (`--purge-webp`); `regen_webp_siblings.py` recreates siblings with `cwebp` on the server. Ask Kinsta to remove the WebP Express rules on both environments.
3. **Restore picked the wrong backup once.** Newest-run default pointed at the 15:36 run whose `orig/` was already-compressed. Now defaults to the oldest run; `--result` overrides.
4. Windows: one ssh argument with 134 commands exceeds the command-line limit; long batches are piped to `bash -s`.

## Pilot: hsfamilylaw.com (Ahrefs crawl 2026-10-29) — applied, headshots restored

- 26 PNGs flagged, 53 MB of originals; with their sub-sizes, **102 MB on disk → 26 MB** after the run (26 originals + 108 sub-size files, all replaced, none under the 15% floor). Blog/practice-area graphics and the site-wide `HS-BG-Image.png` dropped 82–89%; attorney headshots (transparent backgrounds → Pillow's octree quantizer) dropped 55–69%.
- Probe findings that shaped the skill: the 1024px `large` sub-sizes were 0.9–1.6 MB each and are what pages actually load (originals are referenced through ACF image fields and featured images); WordPress regenerates PNG thumbs as truecolor, so the skill now compresses every sub-size file in place and only regenerates when an original was resized (none were; max was 1920px).
- Run log: probe 14:25 → staging dry 14:43 → staging apply 14:52 → **live apply 15:03** (`changes/kinsta/hsfamilylaw/2026-10-29-1503-fix-images-live-apply.md`). Object cache flush ok; `wp kinsta cache purge --all` works on Kinsta and is logged. 138 stray `.webp` files for these images removed on live (142 on staging).
- WebP Express was active and had produced 2,464 `.webp` files but served none of them (Kinsta is Nginx; its `.htaccess` rules do nothing there and it wasn't in Alter-HTML mode). Greg removed the plugin and enabled **Kinsta CDN lossy image optimization** at the server level the same afternoon. ~1,880 stray `.webp` siblings remain elsewhere in `uploads/`; harmless, sweep later.
- Alt text scan (111 rows) agrees with Ahrefs: Tier A (alt attribute absent, published) = 5 rows = Ahrefs' 5 pages. Tier C 59 (featured images with empty attachment alt), Tier B 34 (`alt=""` inline), Tier D 13 (drafts/private). Broken srcs: 0. **Review sheet written: `changes/kinsta/hsfamilylaw/2026-10-29-1533-fix-images-alt.csv`, 94 rows prefilled** (13 headshots from the bio titles; the rest drafted from post topics without seeing the pictures, flagged as such; 3 pasted tracking pixels on `/isle-of-dogs/` and `decor-logo.svg` left blank). Review copy in Google Drive: "hsfamilylaw alt text review 2026-10-29" (Sheets file id `1j6bX79mViQOnblkOgDAhUmcW4lLrFpoanVgka1NN3gU`, 98 rows, Tier D left out, live page links). When Greg is done: export as CSV (Drive `download_file_content` with `text/csv`), `python scripts/merge_alt_sheet.py changes/kinsta/hsfamilylaw/2026-10-29-1533-fix-images-alt.csv <export>`, commit, then `--alt-apply` dry → staging → live. Not yet run. (A second, empty sheet with the same name exists from a failed first upload; Greg can delete it.)
- Current state of live: 15 graphics (practice-area images, `HS-BG-Image`, phone graphic, areas-of-practice picture) are the compressed versions and look fine so far (Greg to confirm); 11 headshots are back to originals (2–3 MB PNGs) with `.webp` siblings at q85, so WebP browsers still get a small file. Staging restore of the headshots pending at time of writing.
- Still to do: staging headshot restore; decide whether to recompress headshots with pngquant `--png-quality 85-98` after a real visual check, or leave them; Ahrefs recrawl; fresh `--probe` for WebP serving; Kinsta ticket for the Nginx rules; **alt text applied to staging and live 2026-10-29 ~16:50** (95 rows: 5 Tier A, 59 featured images, 31 inline `alt=""`), spot-checked good on live.

## Open items

- pngquant on Greg's PC: headshots would likely go from ~60% to 70–80% reduction and with less banding risk; rerun `--target live --apply` after installing (idempotent enough: already-quantized files just shrink a bit more or stay under the floor).
- Alt drafts without seeing the image are the weak spot: a vision pass (fetch each image, describe it) would make the sheet near-final. Needs the images reachable from wherever the pass runs.
- Thumbnail regeneration for files with no attachment ID (edited `-eNNNN` copies, direct uploads): compressed by path, thumbs untouched. See what the probe finds.
- `scripts/batch_fix_images.py --provider kinsta`: review-only batch (probe → staging dry run → alt sheet per site, nothing pushed), summary in `changes/kinsta/_batch-<stamp>-fix-images-review.md`. Built 2026-10-29 evening, first run pending. Applies stay per site after the visual check.
- Elementor/WPBakery sites: image references in builder JSON are not an issue for this skill (URLs don't change), but the alt scan only reads `<img>` tags; builder widgets keep alt in their JSON. Extend the scan when the first builder site runs.
- Server-side compression (Imagick/pngquant on the host) if the local round-trip proves slow on sites with hundreds of files.

## Theme gotcha found on ruggeddepot (2026-10-30)

The product-alt run wrote 7,671 alts correctly, but the custom theme (`ruggeddepotoverhaul`, `inc/woo-custom.php`) renders the product gallery with a hardcoded `alt="#"` and never reads the attachment. Fixed with `scripts/php/patch_ruggeddepot_gallery_alt.php` (run via `wp eval-file` on staging then live; backs up the original; keeps the attachment ID in the map and prints the attachment alt, falling back to the product name). General lesson for the skill: after any alt apply, curl one page and grep the `<img>` tags; data in the database is not the same as alt in the HTML. The probe should do that check automatically (open item).
