# Handoff: fix-images

Status as of 2026-10-29 (afternoon). Read this at the start of the chat dedicated to this skill. The repo is the source of truth: github.com/graterdigital/Low-Hanging-Fruit, cloned on Greg's PC at `C:\Users\greg\Documents\Low-Hanging-Fruit`. Mirror of the project doc `claude/skill-fix-images.md`; update both.

## What the skill does

Shrinks oversized images **in place, same URL, same format** (resize over 2560px long edge, lossy-PNG quantize / JPEG re-encode), regenerates thumbnails for those attachments, purges stale WebP conversions and caches. AUTO tier. Also inventories alt-text gaps and broken/redirected image sources for APPROVE work, but never writes alt text or content.

Decision made this chat: no format conversion and no URL swaps in this skill. WebP delivery is the plugin's/host's job; this skill shrinks the originals everything is derived from.

## Where it lives

- `skills/fix-images/SKILL.md`: procedure, tiers, defaults, rollback.
- `scripts/fix_images.py`: runner. `--probe` → `reports/<slug>/image-inventory-<crawl>.json` + `images-<crawl>.md`; default = dry run (pull + compress locally, no push); `--apply`; `--target live`; `--yes`; `--only`, `--max-edge`, `--min-gain`, `--png-quality`, `--jpeg-quality`. Reuses `build_redirect_map.py`'s `.env`/Ahrefs helpers.
- `scripts/php/image_inventory.php`: read-only, runs via `wp eval-file`. Server tools, optimizer-plugin state (WebP Express config + converted-file counts), per-file facts (attachment ID, dims, sub-sizes, references, featured/ACF use), `<img>`-without-alt scan over post_content + postmeta, missing-file scan.
- Logs: `changes/<provider>/<slug>/<stamp>-fix-images-<target>-<dry|apply>.md`; originals in `backup/<stamp>-fix-images-<target>/orig/`, compressed in `new/` (git-ignored).

Compression runs on Greg's PC (needs `pip install pillow`; `pngquant` + `oxipng` on PATH are better but optional and the log records which was used). Tested here only on synthetic PNGs (opaque and alpha): resize + quantize work, transparency survives.

## Pilot: hsfamilylaw.com (Ahrefs crawl 2026-10-29)

- 26 PNGs flagged, ~55 MB total, 1.0–3.5 MB each. 11 attorney headshots (2026/04, 08, 09), 12 blog/practice-area graphics (2025/03, 2026/06), `2025/04/HS-BG-Image.png` 1.59 MB on **160** pages, `2026/02/forward-facing-phone-graphic.png` (new since Oct 8), `2025/02/Areas-of-Practice-Experience-Picture.png`.
- Other image issues: Missing alt text 5 pages, Image broken 1, Image redirects 4 + Page has redirected image 1 (the pasted `/isle-of-dogs/` post), HTTPS→HTTP image 0.
- **Open question the probe answers first:** `wp plugin list` on 2026-10-28 showed WebP Express and Enable Media Replace active, but the client file still says `image_optimization_plugin: none-detected` and Ahrefs crawled PNGs. Either WebP Express serves `.webp` to browsers (then the live impact is smaller than the audit says, and the originals are still worth shrinking) or it isn't converting (fix the config by hand first).
- Nothing run on the site yet. Next: `--probe` on staging, read `reports/hsfamilylaw/images-2026-10-29.md`, dry run, eyeball `new/` vs `orig/` for the headshots, apply on staging, then live.

## Open items

- `alt-text-apply`: write-back from an edited CSV (featured image → `_wp_attachment_image_alt`; inline → attribute insert into the exact tag in post_content/postmeta). Same dry/apply/log contract.
- Thumbnail regeneration for files with no attachment ID (edited `-eNNNN` copies, direct uploads): compressed by path, thumbs untouched. See what the probe finds.
- Batch runner across a host, like `batch_fix_redirect_links.py`, once two sites are clean.
- Elementor/WPBakery sites: image references in builder JSON are not an issue for this skill (URLs don't change), but the alt scan only reads `<img>` tags; builder widgets keep alt in their JSON. Extend the scan when the first builder site runs.
- Server-side compression (Imagick/pngquant on the host) if the local round-trip proves slow on sites with hundreds of files.
- Kinsta CDN: `wp kinsta cache purge --all` is attempted and logged; confirm it exists on this install.
