---
name: fix-images
description: Resize a WordPress site's oversized images in place (same URL, same format, downscale only, never lossy compression), regenerate their thumbnails, and inventory alt-text, broken-image and redirected-image work for review. Use this whenever a triage report or Ahrefs lists "Image file size too large", "Missing alt text", "Image broken", "Image redirects", "Page has broken image" or "Page has redirected image" for a client site, or the user asks to resize, optimize, or clean up a site's images or alt tags. Resizes are AUTO tier; alt text and broken images are APPROVE. Always probe and dry-run on staging first.
---

# fix-images

Three different problems hide under "images" in an audit, and they need three different treatments:

| Problem | What Ahrefs calls it | Tier | What this skill does |
|---|---|---|---|
| Oversized originals (4000px+ files shown at 400px) | Image file size too large | **AUTO** | Pull, **downscale anything over `--max-edge`** on your machine at full quality, push back under the same name, regenerate thumbnails. Files already within the limit are not touched. No lossy compression, ever (see below). |
| Images with no `alt` | Missing alt text | **APPROVE** | Find every `<img>` without alt (Ahrefs only gives per-page counts), put them in a CSV with drafted text, a human reviews, the skill writes it back. |
| Broken or redirected image sources | Image broken, Image redirects, Page has broken/redirected image | **APPROVE** | List them per page. These are re-uploads or removals, done by hand. |

Not this skill: lossy compression of any kind (removed, see below), converting to WebP/AVIF and swapping references (that is a delivery concern; a plugin or the host CDN does it from the originals), lazy-loading, `width`/`height` attributes, theme CSS images, writing the alt text itself (a human does, in the sheet).

## No lossy compression. Resize only.

**Removed 2026-11-09.** Earlier versions quantized PNGs (Pillow 256-colour, then pngquant) and re-encoded JPEGs at q82. Pillow's quantizer visibly wrecked the hsfamilylaw attorney headshots on live (2026-10-29), they had to be restored from backup, and the client saw them. The lesson generalised: a quality setting that is "visually lossless" on one photo is not on the next, and nobody is going to eyeball 500 files per site before an apply. So the script no longer has a quality setting at all. The flags `--min-gain`, `--png-quality`, `--jpeg-quality`, `--lossless`, `--allow-pillow` are gone and the script refuses them.

What it does now, and all it does: if a flagged file's longest edge is over `--max-edge` (default 2560px, WordPress's own `big_image_size_threshold`), it is downscaled with Lanczos and saved in the same format at full quality (PNG lossless; JPEG q95 with 4:4:4 chroma, the no-visible-loss setting, because a resized JPEG has to be re-encoded). Alpha is preserved. A file already within `--max-edge` is left byte-for-byte as it was and reported as "no resize needed". Sub-size files are never touched directly: when an original is downscaled, `wp media regenerate` rebuilds them from the new original.

Consequence: a 2.5 MB headshot that is only 1800px wide stays 2.5 MB and stays on the Ahrefs list. That is the correct outcome for this skill. The levers for such files are (a) a lower `--max-edge` for a run limited with `--only` (a headshot never renders above ~1200px, so `--max-edge 1200 --only headshots` is still a plain resize), (b) the host's CDN image optimization (Kinsta/WP Engine both have one; it compresses on delivery and leaves the originals alone), or (c) the client re-exporting the photo as JPEG, which changes the URL and is a by-hand job. Say which applies in the handoff rather than tightening quality.

## Why "in place, same format"

Replacing `big.png` with a smaller `big.png` keeps every URL, every `srcset`, every ACF field and every CSS reference valid, so it can run unattended. Converting to `.jpg` or `.webp` changes URLs and needs a reference rewrite plus redirects; that is a different, APPROVE-tier job and almost never needed when the host's CDN serves WebP.

## What you need

1. `clients/<slug>.yaml` with `hosting.ssh_alias`, `hosting.staging_environment`, `hosting.provider` and `ahrefs.site_audit_project_id`.
2. `AHREFS_API_KEY` in `.env` at the repo root.
3. On the machine that runs the script: Python with `pillow` and `pyyaml`. No pngquant, oxipng or other binaries: nothing is compressed.
4. A fresh staging copy of live.

## Step 1: probe

```
python scripts/fix_images.py <slug> --probe
```

Reads the "Image file size too large" issue from Ahrefs, ships `scripts/php/image_inventory.php` to the site (`wp eval-file`, read-only) and writes `reports/<slug>/image-inventory-<crawl>.json` plus a readable `reports/<slug>/images-<crawl>.md`. Read the report before anything else. It answers:

- **Server tools:** PHP Imagick/GD, and whether `cwebp`, `convert` exist there (`cwebp` matters for `regen_webp_siblings.py`).
- **Is a WebP plugin active and actually converting?** WebP Express / ShortPixel / Smush / EWWW / Imagify / Optimole state, the WebP Express config, how many `.webp` files exist, and, per oversized file, what a Chrome-like request with `Accept: image/webp` really receives on the live URL. If browsers already get a `.webp`, Ahrefs flagging the PNG is partly a crawler artifact (its crawler does not send that header): the originals still matter (they feed every conversion and thumbnail, and non-WebP clients), but the user should know the live impact is smaller than the audit implies. If the plugin is active and browsers still get the PNG, the plugin is misconfigured; fix that first, by hand.
- **Per file:** attachment ID, path on disk, bytes, dimensions, the largest registered sub-size (if the original is 4000px and the biggest sub-size is 1536px, nothing on the site shows the original), how many posts/meta/options reference it or its `-WxH` thumbnails, whether it is a featured image or sits in an ACF image field. A file referenced nowhere in the database is a theme or CSS image (e.g. a background) or unused; it is still resized if over the limit, since the URL doesn't change. **Dimensions are the column that matters now:** a flagged file within `--max-edge` will not change, and the report should say so up front.
- **Alt text:** every `<img>` in `post_content` or non-underscore postmeta with no `alt` or `alt=""`, with page URL, post type and the tag; plus featured images whose attachment has no alt. `alt=""` on a decorative image is correct and should be left alone; the human reviewing the list decides.
- **Broken sources:** `<img src>` on this host whose file is missing from `uploads/`.

Sanity checks: the file count should match Ahrefs; every file should resolve to an attachment ID (one that doesn't is a direct upload or an `-e123456789` edited copy whose metadata lives under a different name; it is still resized by path, but thumbnails can't be regenerated for it); the `served_to_webp_browser` column should be consistent across files.

## Step 2: dry run on staging

```
python scripts/fix_images.py <slug>
```

Pulls each flagged file over `scp` into `changes/<provider>/<slug>/backup/<stamp>-fix-images-staging/orig/`, writes a downscaled copy into `new/` for the ones over `--max-edge`, and writes `changes/<provider>/<slug>/<stamp>-fix-images-staging-dry.md` with dimensions, before/after bytes and the action per file (`would replace` or `kept (no resize needed)`). Nothing is pushed. Often most or all rows are "kept": that means the site's problem is weight-per-pixel, not pixel count, and this skill has nothing to do there (see "No lossy compression" above for what to recommend instead).

Options: `--max-edge N` (default 2560) and `--only a,b` (substrings of the path) to resize a specific group harder, e.g. `--only headshot,attorney --max-edge 1200`. Still look at `new/` next to `orig/` for a couple of files: a downscale is safe, but a wrong `--max-edge` on a hero image that really is shown at 2400px wide is a visible softening. Applying twice is harmless (a file already at the limit is left alone), unlike the old compression.

## Step 3: apply on staging, then live

```
python scripts/fix_images.py <slug> --apply
python scripts/fix_images.py <slug> --target live --apply        # type the slug; --yes for vetted unattended runs
```

Apply pushes the downscaled originals back under the same names and runs `wp media regenerate <id> --yes` for each one, so attachment metadata and every dimension-bound sub-size match the new original. Sub-size files of untouched originals are not changed.

Apply then flushes the object cache, and tries the host's full-page/CDN purge (`wp kinsta cache purge --all` on Kinsta). Each step's result is in the log. Then load two or three affected pages on the target and check the images look right and the page weight dropped (DevTools → Network, filter Img).

Commit the `changes/<provider>/<slug>/*.md` logs; the `backup/` folders stay local.

## Step 4: alt text (APPROVE, from a reviewed sheet)

```
python scripts/fix_images.py <slug> --alt-csv
```

No SSH; builds `changes/<provider>/<slug>/<stamp>-fix-images-alt.csv` from the inventory, one row per image without alt, sorted by tier: **A** alt attribute absent on a published page (what Ahrefs counts), **C** featured images whose attachment has no alt (one attachment field fixes every use), **B** `alt=""` inline on published pages (valid-decorative by HTML rules, usually just unfilled), **D** unpublished (left blank, never applied). `new_alt` is prefilled only for attorney/staff headshots (name + role, the one case the rule gets right); every other row carries a draft in `suggestion` and an empty `new_alt`, so nothing gets applied unless a person accepted or rewrote it. The drafts are written from the page topic and file name, not from seeing the picture, so the review is real work, not a rubber stamp: open the page, look at the image, fix the text. Blank `new_alt` to skip a row. Review happens in the client's persistent Google Sheet (`review.alt_sheet_id` in the client file; `python scripts/review_sheets.py setup <slug> --share <emails>` creates it once, as a service account, see docs/setup-machine.md). `review_sheets.py push <slug>` appends only images the sheet has not seen (the batch does this automatically); a human fills `new_alt` (or writes `skip`); `review_sheets.py pull <slug>` merges decisions into the repo CSV and marks the rows merged; after the apply, `review_sheets.py mark-applied <slug>` stamps them. The sheet is one row per distinct image (size variants collapsed, decorative files left out), and a decision fans out to every occurrence. `merge_alt_sheet.py` still works for a hand-exported CSV. Leave decorative images (logos, icons, divider art) blank. Alt text is short, describes what the picture shows, and never starts with "image of"; no keyword stuffing.

```
python scripts/fix_images.py <slug> --alt-apply changes/<provider>/<slug>/<stamp>-fix-images-alt.csv
python scripts/fix_images.py <slug> --alt-apply <csv> --apply
python scripts/fix_images.py <slug> --alt-apply <csv> --target live --apply
```

Ships `scripts/php/apply_alt.php` with the rows that have `new_alt`. Featured images: `_wp_attachment_image_alt` on the attachment. Inline: every `<img>` in that post (or that ACF meta row) whose `src` path matches gets `alt="..."` (replaced if present, inserted after `<img` if not); the host part of `src` is ignored, so a sheet built on staging applies to live. `wp_update_post` keeps a revision. Log: `<stamp>-fix-images-alt-<target>-<dry|apply>.md`; previous values in `backup/`. A dry run that reports "no <img> with that src found" means the content changed since the probe or the alt was already set; re-probe.

The scan covers public post types only (revisions, Elementor templates, TablePress tables and the like are skipped), which is what keeps the sheet reviewable.

### WooCommerce products: alt from the title, no sheet

A store's product images are the bulk of its missing alts (ruggeddepot: 3,517 of 3,604) and the right text is mechanical, so they are AUTO:

```
python scripts/fix_images.py <slug> --product-alt                    # dry: lists every product image and the alt it would get
python scripts/fix_images.py <slug> --product-alt --apply            # staging
python scripts/fix_images.py <slug> --product-alt --target live --apply
```

Rule: featured image = product title (a `| Brand` tail dropped); gallery images = title + a view word taken from the file name (`-ports`, `-side`, `-docked`, `-in-vehicle`…) or `view N` when the name says nothing; variation images = title + the variation attributes. An alt already on the attachment is never overwritten. An attachment shared by several products is set once, for the first product that uses it, and the others are listed as shared. The full product → image → alt list is written as a CSV next to the log for a skim before `--apply`.

Broken and redirected images (pasted web pages, dead thumbnails) are not alt work: the sheet marks them "remove by hand" and leaves `new_alt` blank.

If no WebP delivery exists on the site, say so in the handoff; on Kinsta, turn on CDN image optimization in MyKinsta rather than installing a plugin (WebP Express's rewrite rules do nothing on Nginx).

## After

Trigger an Ahrefs recrawl. "Image file size too large" drops only by the files that were actually downscaled; everything reported "no resize needed" stays flagged, and the handoff should list those with the recommended non-script fix (CDN optimization, or a client re-export). Record the result in the client file (`platform.image_optimization_plugin`, and a note on what the probe found) and in the skill handoff doc.

## Rollback

`scripts/restore_images.py <slug> --target <staging|live> --all|--only <names> [--webp]` pushes the `orig/` copies back from the **oldest** backup for that target (a later run's `orig/` is an earlier run's output). Dry runs count: they pull the same files, their rows just say `would replace`. The script verifies each file's byte size on the server afterwards and exits non-zero when nothing matched instead of flushing caches over nothing.

`backup/<stamp>-fix-images-<target>/orig/` holds every replaced file byte-for-byte, originals and sub-sizes alike. `python scripts/restore_images.py <slug> --target <t> --only <names>` (or `--all`) pushes them back, rewrites the `.webp` siblings with `--webp`, and purges caches; it defaults to the **oldest** run's backup for that target, because a later run's `orig/` is the earlier run's output, not the real original. After a restore, run `wp media regenerate <id> --yes` for each restored attachment so the sub-sizes match the original again.

## Scope and limits

- WordPress over SSH + WP-CLI + scp, Kinsta webroot `public`, WP Engine `sites/<install>`.
- Only files Ahrefs flags are touched. A site-wide sweep of `uploads/` is deliberate scope creep for later; Ahrefs' threshold is the agreed definition of "too large".
- PNG stays PNG, JPEG stays JPEG, full quality, alpha preserved. GIF, SVG, AVIF, WebP originals are never changed, even when over `--max-edge`.
- No lossy compression. There is no flag to turn it back on; if someone wants it, that is a new, separately reviewed skill, not an option here.
- Writes files and attachment metadata (via regenerate) only. Never touches `post_content`, postmeta text, options or theme files.
- `.webp` siblings are left alone unless `--purge-webp` is passed. Learned on hsfamilylaw: Kinsta's Nginx kept serving `name.png.webp` to WebP-capable browsers after WebP Express was removed, so deleting the siblings of the 26 replaced files broke exactly those 26 images (the photo looked "missing"; the file on disk was fine). After replacing an image on such a host, regenerate its sibling instead: `python scripts/regen_webp_siblings.py <slug> --target <staging|live>` (uses `cwebp` on the server and picks the naming from the existing files). The real fix is having the host remove the plugin's rewrite rules.
