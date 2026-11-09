# Handoff: fix-images

Status as of 2026-11-09 (**lossy compression removed; the script is resize-only now**; see the 2026-11-09 section first). Read this at the start of the chat dedicated to this skill. The repo is the source of truth: github.com/graterdigital/Low-Hanging-Fruit, cloned on Greg's PC at `C:\Users\greg\Documents\Low-Hanging-Fruit`. Mirror of the project doc `claude/skill-fix-images.md`; update both.

## What the skill does

Downscales oversized images **in place, same URL, same format** when their longest edge is over `--max-edge` (default 2560px), saved at full quality, then regenerates thumbnails for those attachments and purges caches. Files within the limit are not touched. **No lossy compression of any kind** (removed 2026-11-09). AUTO tier. Also inventories alt-text gaps and broken/redirected image sources for APPROVE work, but never writes alt text or content.

Decision made this chat: no format conversion and no URL swaps in this skill. WebP delivery is the plugin's/host's job; this skill shrinks the originals everything is derived from.

## Where it lives

- `skills/fix-images/SKILL.md`: procedure, tiers, defaults, rollback.
- `scripts/fix_images.py`: runner. `--probe` → `reports/<slug>/image-inventory-<crawl>.json` + `images-<crawl>.md`; default = dry run (pull + resize locally, no push); `--apply`; `--target live`; `--yes`; `--alt-csv` (review sheet, no SSH); `--alt-apply <csv>` (dry/apply/live like the rest); `--only`, `--max-edge`. (`--min-gain`, `--png-quality`, `--jpeg-quality`, `--lossless`, `--allow-pillow` were removed 2026-11-09 and the script refuses them.) Reuses `build_redirect_map.py`'s `.env`/Ahrefs helpers.
- `scripts/review_sheets.py` (2026-10-30): one persistent Google Sheet per client, id in `clients/<slug>.yaml` → `review.alt_sheet_id`; `setup / push / pull / mark-applied / status`; service account auth (docs/setup-machine.md). Batch pushes new images automatically. Replaces the hand-uploaded dated sheets; the five made by hand on 10-30 are recorded in the client files and get upgraded in place on first `push`. **2026-11-09: every `status` column on the review sheets (alt text, ai discoverability, meta, work orders) is a strict dropdown; allowed values live in `STATUS_VALUES` in review_sheets.py, `dropdowns --all` retrofits; run on all 31 sheets the same day. Alt tab gained an `applied` date column (status is bare `applied`).**
- `scripts/php/apply_alt.php`: writes alt from the reviewed CSV (featured → `_wp_attachment_image_alt`; inline → attribute replace/insert on the matching `<img>` by src path, host-agnostic). Regex unit-tested locally; not yet run on a site.
- `scripts/php/image_inventory.php`: read-only, runs via `wp eval-file`. Server tools, optimizer-plugin state (WebP Express config + converted-file counts), per-file facts (attachment ID, dims, sub-sizes, references, featured/ACF use), `<img>`-without-alt scan over post_content + postmeta, missing-file scan.
- Logs: `changes/<provider>/<slug>/<stamp>-fix-images-<target>-<dry|apply>.md`; originals in `backup/<stamp>-fix-images-<target>/orig/`, resized copies in `new/` (git-ignored).

Resizing runs on Greg's PC (needs `pip install pillow` only; no binaries).

## 2026-11-09: lossy compression removed

Greg's call after the hsfamilylaw headshots: "the image compression is too strong and resulted in client-visible overly compressed images. Remove that step and strictly resize as applicable." Done in `fix_images.py`:

- `compress()` is gone, replaced by `resize_only()`: Lanczos downscale when the longest edge is over `--max-edge`, saved as PNG lossless (alpha kept) or JPEG q95 4:4:4 (a resized JPEG has to be re-encoded; that is the no-visible-loss setting). Otherwise the file is not written at all and the row says `kept (no resize needed)`.
- Sub-size files are no longer pulled or rewritten. When an original is downscaled, `wp media regenerate` rebuilds them from it; otherwise nothing on the server changes.
- No quality flags exist. `--min-gain`, `--png-quality`, `--jpeg-quality`, `--lossless`, `--allow-pillow` make the script exit with a message. Applying twice is harmless now.
- `batch_fix_images.py` reports "over max-edge" per site instead of MB saved by compression; sites whose flagged files are all within the limit are marked *flagged but within max-edge (nothing to resize)*.
- SKILL.md has a "No lossy compression. Resize only." section with what to recommend instead for heavy-but-not-huge files: a lower `--max-edge` with `--only` (still a plain resize), the host CDN's image optimization (Kinsta/WPE compress on delivery, originals untouched), or the client re-exporting as JPEG (URL change, by hand).

What this means for the existing flagged files: hsfamilylaw's 12 headshots (1.5–2.8 MB, under 2560px) stay on the Ahrefs list; Kinsta CDN optimization is already on there, so browsers get a compressed copy anyway. The Kinsta/WPE batch dry runs from 10-29 and 11-02 were produced by the old compression code and must not be applied; rerun the dry runs with the new script before any apply. The 15 hsfamilylaw graphics already compressed on live 10-29 are left as they are (Greg said they look fine); restore with `restore_images.py hsfamilylaw --target live --only <names> --webp` if that changes.

Staging on hsfamilylaw still had the posterised headshots as of 11-02 (the 11-03 restore fix below addressed the cause; rerun `python scripts/restore_images.py hsfamilylaw --target staging --all --webp` and check `/firm/mali-shadmehry/` on staging).

## 2026-11-03: staging restore that did nothing, and `--lossless`

- Greg ran `restore_images.py hsfamilylaw --target staging --all --webp` on 11-02 and staging still showed the posterised headshots. Cause: the 10-30 "oldest run" default picked `2026-10-29-1443-fix-images-staging`, which is the **dry run**; its `result.json` rows say `would replace`, and the restore only accepted `replaced`, so it matched 0 files, pushed nothing, flushed caches and wrote a "Restored 0" log. Fixed: dry-run rows are restorable (their `orig/` is the same server pull), the picker takes the oldest run that has rows, 0 matches is an error, and every pushed file is size-checked on the server. Live was never affected (its restore on 10-29 used `--result` on the 15:03 apply).
- `fix_images.py --lossless`: oxipng/optipng for PNG, jpegoptim for JPEG, no pngquant, no Pillow quantizer, `--min-gain` 3. `--max-edge` still resizes first (Lanczos, then lossless re-pack); on its own the re-pack is a 5–25% shave, with `--max-edge 1200` the headshots should land ~60% smaller. Sub-sizes are regenerated from the resized original on apply and then re-packed the same way. Uses pyoxipng/oxipng when present, else Pillow's lossless writer; pyoxipng has no wheel for Greg's Windows ARM64 Python, so Pillow is what runs there.

## Where things stand (2026-10-30 12:50)

**Done**
- hsfamilylaw: 15 graphics compressed on live; 11 headshots restored to originals; 95 alt texts applied live; WebP Express removed, Kinsta CDN optimisation on; theme untouched.
- ruggeddepot: 7,481 product alts written on **staging** by the title rule (`--product-alt`); theme gallery patch (`scripts/php/patch_ruggeddepot_gallery_alt.php`) applied on staging and verified (the `#` is gone). **Live still pending** for both: `python scripts/fix_images.py ruggeddepot --product-alt --target live --apply`, then scp + `wp eval-file` the patch on the live alias, then commit logs. 296-attachment exception CSV (shared model photos, one-word titles) awaits a human.
- Review batch (`batch_fix_images.py --provider kinsta`, 2026-10-29): probes, staging dry runs and alt CSVs for 11 sites; summary `changes/kinsta/_batch-2026-10-29-1655-fix-images-review.md`. Compression dry runs ready for a visual check (nothing pushed): atlantaspecializedcare 149→28 MB, markheardfuel 32→7, miuraboiler 45→21, meshautomationinc 40→21, setcomcorp 30→12, forwardfacing 12→7. slepianfirm's 27 flagged files are bare uploads with no attachment record (needs a path-only mode, not built).
- Google review sheets: service account `lhf-review-sheets@overwatch-site-monitoring.iam.gserviceaccount.com`, key at `secrets/google-service-account.json`, Drive folder `1IOL3yiztXBmERkbfEbUA8NVYDSl-jHfG` ("LHF Review Sheets", owned by overwatch@, shared with greg@ and the service account). Eleven blank sheets `<slug> review` created in it. `setup`+`push` succeeded for atlantaspecializedcare (76 rows), fenceworksofga (127), forwardfacing (66, all prefilled by rule), hsfamilylaw (3), markheardfuel (9); the Sheets API 60-reads/min quota stopped the rest. Retry added (`4398a25`).

**Next, in order**
1. Rerun on Greg's PC: `foreach ($s in "meshautomationinc","miuraboiler","setcomcorp","slepianfirm","technikpackaging","ruggeddepot") { python scripts/review_sheets.py setup $s; python scripts/review_sheets.py push $s }` then `status`, commit `clients/`.
2. ruggeddepot live (product-alt apply + theme patch), see above.
3. Greg (or overwatch@) fills `new_alt` in the sheets; then per site `review_sheets.py pull <slug>` → `fix_images.py <slug> --alt-apply <csv>` dry → `--apply` → `--target live --apply` → `review_sheets.py mark-applied <slug>`. forwardfacing can skip review (rule-filled).
4. Resize applies, per site, after a **fresh** dry run with the resize-only script (old dry runs are compression output, discard them): `fix_images.py <slug>` → look at `new/` vs `orig/` → `--apply` → `--target live --apply`. A `batch_apply_images.py` with a `--reviewed <slugs>` gate is designed but not built.
5. Delete the five hand-made sheets in greg@'s Drive (dated "alt text review 2026-10-29/30"); their ids were retired from the client files. Rotate the service-account key that was pasted into chat (Cloud Console → service account → Keys → delete `ae5a2fd2…`; the live key is `9a12a0ed…`).
6. Kinsta ticket: remove WebP Express Nginx rules on hsfamilylaw (both environments).

## What went wrong on 2026-10-29

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

- Alt drafts without seeing the image are the weak spot: a vision pass (fetch each image, describe it) would make the sheet near-final. Needs the images reachable from wherever the pass runs.
- Thumbnail regeneration for files with no attachment ID (edited `-eNNNN` copies, direct uploads): compressed by path, thumbs untouched. See what the probe finds.
- `scripts/batch_fix_images.py --provider kinsta`: review-only batch (probe → staging dry run → alt sheet per site, nothing pushed), summary in `changes/kinsta/_batch-<stamp>-fix-images-review.md`. Built 2026-10-29 evening, first run pending. Applies stay per site after the visual check.
- Elementor/WPBakery sites: image references in builder JSON are not an issue for this skill (URLs don't change), but the alt scan only reads `<img>` tags; builder widgets keep alt in their JSON. Extend the scan when the first builder site runs.

## Theme gotcha found on ruggeddepot (2026-10-30)

The product-alt run wrote 7,671 alts correctly, but the custom theme (`ruggeddepotoverhaul`, `inc/woo-custom.php`) renders the product gallery with a hardcoded `alt="#"` and never reads the attachment. Fixed with `scripts/php/patch_ruggeddepot_gallery_alt.php` (run via `wp eval-file` on staging then live; backs up the original; keeps the attachment ID in the map and prints the attachment alt, falling back to the product name). General lesson for the skill: after any alt apply, curl one page and grep the `<img>` tags; data in the database is not the same as alt in the HTML. The probe should do that check automatically (open item).
