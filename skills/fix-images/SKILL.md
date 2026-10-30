---
name: fix-images
description: Shrink a WordPress site's oversized images in place (same URL, same format), regenerate their thumbnails, and inventory alt-text, broken-image and redirected-image work for review. Use this whenever a triage report or Ahrefs lists "Image file size too large", "Missing alt text", "Image broken", "Image redirects", "Page has broken image" or "Page has redirected image" for a client site, or the user asks to compress, optimize, or clean up a site's images or alt tags. Weight fixes are AUTO tier; alt text and broken images are APPROVE. Always probe and dry-run on staging first.
---

# fix-images

Three different problems hide under "images" in an audit, and they need three different treatments:

| Problem | What Ahrefs calls it | Tier | What this skill does |
|---|---|---|---|
| Oversized originals (multi-MB PNGs, 4000px headshots shown at 400px) | Image file size too large | **AUTO** | Pull, compress and resize on your machine, push back under the same name, regenerate thumbnails. Nothing a visitor reads changes. |
| Images with no `alt` | Missing alt text | **APPROVE** | Find every `<img>` without alt (Ahrefs only gives per-page counts), put them in a CSV with drafted text, a human reviews, the skill writes it back. |
| Broken or redirected image sources | Image broken, Image redirects, Page has broken/redirected image | **APPROVE** | List them per page. These are re-uploads or removals, done by hand. |

Not this skill: converting to WebP/AVIF and swapping references (that is a delivery concern; a plugin or the host does it from the originals this skill shrinks), lazy-loading, `width`/`height` attributes, theme CSS images, writing the alt text itself (a human does, in the sheet).

## Why "in place, same format"

Replacing `big.png` with a smaller `big.png` keeps every URL, every `srcset`, every ACF field and every CSS reference valid, so it can run unattended. Converting to `.jpg` or `.webp` changes URLs and needs a reference rewrite plus redirects; that is a different, APPROVE-tier job and almost never needed when a WebP plugin is active. A lossy-PNG quantize (256 colours, dithered) typically cuts a photo-saved-as-PNG by 60–80% with no visible change at display size; resizing anything over 2560px on the long edge (WordPress's own `big_image_size_threshold`) does the rest.

## What you need

1. `clients/<slug>.yaml` with `hosting.ssh_alias`, `hosting.staging_environment`, `hosting.provider` and `ahrefs.site_audit_project_id`.
2. `AHREFS_API_KEY` in `.env` at the repo root.
3. On the machine that runs the script: Python with `pillow` and `pyyaml`, and **`pngquant` on PATH** (optionally `oxipng`). Without pngquant, PNGs are skipped: Pillow's 256-colour quantizer is only usable for flat graphics and visibly ruins photographs saved as PNG, which is what most oversized PNGs on client sites are (headshots, hero photos). `--allow-pillow` overrides that for a run you have looked at.
4. A fresh staging copy of live.

## Step 1: probe

```
python scripts/fix_images.py <slug> --probe
```

Reads the "Image file size too large" issue from Ahrefs, ships `scripts/php/image_inventory.php` to the site (`wp eval-file`, read-only) and writes `reports/<slug>/image-inventory-<crawl>.json` plus a readable `reports/<slug>/images-<crawl>.md`. Read the report before anything else. It answers:

- **Can the server compress?** PHP Imagick/GD, and whether `pngquant`, `cwebp`, `convert` exist there. (v1 compresses locally regardless; this is for later.)
- **Is a WebP plugin active and actually converting?** WebP Express / ShortPixel / Smush / EWWW / Imagify / Optimole state, the WebP Express config, how many `.webp` files exist, and, per oversized file, what a Chrome-like request with `Accept: image/webp` really receives on the live URL. If browsers already get a `.webp`, Ahrefs flagging the PNG is partly a crawler artifact (its crawler does not send that header): the originals still matter (they feed every conversion and thumbnail, and non-WebP clients), but the user should know the live impact is smaller than the audit implies. If the plugin is active and browsers still get the PNG, the plugin is misconfigured; fix that first, by hand.
- **Per file:** attachment ID, path on disk, bytes, dimensions, the largest registered sub-size (if the original is 4000px and the biggest sub-size is 1536px, nothing on the site shows the original), how many posts/meta/options reference it or its `-WxH` thumbnails, whether it is a featured image or sits in an ACF image field. A file referenced nowhere in the database is a theme or CSS image (e.g. a background) or unused; it still gets shrunk, since the URL doesn't change.
- **Alt text:** every `<img>` in `post_content` or non-underscore postmeta with no `alt` or `alt=""`, with page URL, post type and the tag; plus featured images whose attachment has no alt. `alt=""` on a decorative image is correct and should be left alone; the human reviewing the list decides.
- **Broken sources:** `<img src>` on this host whose file is missing from `uploads/`.

Sanity checks: the file count should match Ahrefs; every file should resolve to an attachment ID (one that doesn't is a direct upload or an `-e123456789` edited copy whose metadata lives under a different name; it is still compressed by path, but thumbnails can't be regenerated for it); the `served_to_webp_browser` column should be consistent across files.

## Step 2: dry run on staging

```
python scripts/fix_images.py <slug>
```

Pulls each oversized file over `scp` into `changes/<provider>/<slug>/backup/<stamp>-fix-images-staging/orig/`, compresses it into `new/`, and writes `changes/<provider>/<slug>/<stamp>-fix-images-staging-dry.md` with before/after bytes and the steps per file. Nothing is pushed. Open a few of the `new/` files next to their `orig/` at 100%: headshots and anything with gradients or text are the ones to look at. If one looks wrong, exclude it with `--only` on the next run or raise `--png-quality` (pngquant only, e.g. `80-95`).

Defaults: `--max-edge 2560`, `--min-gain 15` (a file that doesn't shrink by at least 15% is left alone), `--png-quality 80-98` (pngquant's floor–ceiling; visually lossless on photos, and pngquant refuses rather than going below the floor), `--jpeg-quality 82`. Flat graphics can take `--png-quality 65-85` with `--only` to target them.

**Look before you apply, every time.** Open the headshots and anything with a smooth gradient from `new/` next to `orig/` at 100%. The staging apply is not the review step; it is confirmation of a review already done. A run that was applied twice (a second pass over already-quantized files) compounds the damage, so never rerun apply on the same files without restoring first.

## Step 3: apply on staging, then live

```
python scripts/fix_images.py <slug> --apply
python scripts/fix_images.py <slug> --target live --apply        # type the slug; --yes for vetted unattended runs
```

The dry run and apply both work on the original **and every registered sub-size file** of each attachment (the 1024px `large` of a photo saved as PNG is often 1–1.5 MB by itself, and that is what pages actually load). WordPress writes resized PNGs as truecolor, so regenerating thumbnails from a quantized original would not shrink them; each sub-size file is compressed in place instead. `wp media regenerate` runs only when an original had to be resized, so the metadata and dimension-bound sub-sizes match, and the sub-sizes that produces are then compressed too.

Apply pushes the compressed files back under the same names, flushes the object cache, and tries the host's full-page/CDN purge (`wp kinsta cache purge --all` on Kinsta). Each step's result is in the log. Then load two or three affected pages on the target and check the images look right and the page weight dropped (DevTools → Network, filter Img).

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

Trigger an Ahrefs recrawl. "Image file size too large" should drop to the files kept under `--min-gain`. Record the result in the client file (`platform.image_optimization_plugin`, and a note on what the probe found) and in the skill handoff doc.

## Rollback

`backup/<stamp>-fix-images-<target>/orig/` holds every replaced file byte-for-byte, originals and sub-sizes alike. `python scripts/restore_images.py <slug> --target <t> --only <names>` (or `--all`) pushes them back, rewrites the `.webp` siblings with `--webp`, and purges caches; it defaults to the **oldest** run's backup for that target, because a later run's `orig/` is the earlier run's output, not the real original. Only if an original was resized is `wp media regenerate <id> --yes` needed afterwards.

## Scope and limits

- WordPress over SSH + WP-CLI + scp, Kinsta webroot `public`, WP Engine `sites/<install>`.
- Only files Ahrefs flags are touched. A site-wide sweep of `uploads/` is deliberate scope creep for later; Ahrefs' threshold is the agreed definition of "too large".
- PNG stays PNG, JPEG stays JPEG. GIF, SVG, AVIF, WebP originals are copied through untouched.
- Writes files and attachment metadata (via regenerate) only. Never touches `post_content`, postmeta text, options or theme files.
- `.webp` siblings are left alone unless `--purge-webp` is passed. Learned on hsfamilylaw: Kinsta's Nginx kept serving `name.png.webp` to WebP-capable browsers after WebP Express was removed, so deleting the siblings of the 26 replaced files broke exactly those 26 images (the photo looked "missing"; the file on disk was fine). After replacing an image on such a host, regenerate its sibling instead: `python scripts/regen_webp_siblings.py <slug> --target <staging|live>` (uses `cwebp` on the server and picks the naming from the existing files). The real fix is having the host remove the plugin's rewrite rules.
