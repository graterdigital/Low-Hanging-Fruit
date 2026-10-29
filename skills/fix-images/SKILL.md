---
name: fix-images
description: Shrink a WordPress site's oversized images in place (same URL, same format), regenerate their thumbnails, and inventory alt-text, broken-image and redirected-image work for review. Use this whenever a triage report or Ahrefs lists "Image file size too large", "Missing alt text", "Image broken", "Image redirects", "Page has broken image" or "Page has redirected image" for a client site, or the user asks to compress, optimize, or clean up a site's images or alt tags. Weight fixes are AUTO tier; alt text and broken images are APPROVE. Always probe and dry-run on staging first.
---

# fix-images

Three different problems hide under "images" in an audit, and they need three different treatments:

| Problem | What Ahrefs calls it | Tier | What this skill does |
|---|---|---|---|
| Oversized originals (multi-MB PNGs, 4000px headshots shown at 400px) | Image file size too large | **AUTO** | Pull, compress and resize on your machine, push back under the same name, regenerate thumbnails. Nothing a visitor reads changes. |
| Images with no `alt` | Missing alt text | **APPROVE** | Find every `<img>` without alt (Ahrefs only gives per-page counts) and list them with page, source and context. A human writes the text. |
| Broken or redirected image sources | Image broken, Image redirects, Page has broken/redirected image | **APPROVE** | List them per page. These are re-uploads or removals, done by hand. |

Not this skill: converting to WebP/AVIF and swapping references (that is a delivery concern; a plugin or the host does it from the originals this skill shrinks), lazy-loading, `width`/`height` attributes, theme CSS images.

## Why "in place, same format"

Replacing `big.png` with a smaller `big.png` keeps every URL, every `srcset`, every ACF field and every CSS reference valid, so it can run unattended. Converting to `.jpg` or `.webp` changes URLs and needs a reference rewrite plus redirects; that is a different, APPROVE-tier job and almost never needed when a WebP plugin is active. A lossy-PNG quantize (256 colours, dithered) typically cuts a photo-saved-as-PNG by 60–80% with no visible change at display size; resizing anything over 2560px on the long edge (WordPress's own `big_image_size_threshold`) does the rest.

## What you need

1. `clients/<slug>.yaml` with `hosting.ssh_alias`, `hosting.staging_environment`, `hosting.provider` and `ahrefs.site_audit_project_id`.
2. `AHREFS_API_KEY` in `.env` at the repo root.
3. On the machine that runs the script: Python with `pillow` and `pyyaml`; optionally `pngquant` and `oxipng` on PATH (better PNG results than Pillow's quantizer; the log records which was used).
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

Defaults: `--max-edge 2560`, `--min-gain 15` (a file that doesn't shrink by at least 15% is left alone), `--png-quality 65-85`, `--jpeg-quality 82`.

## Step 3: apply on staging, then live

```
python scripts/fix_images.py <slug> --apply
python scripts/fix_images.py <slug> --target live --apply        # type the slug; --yes for vetted unattended runs
```

The dry run and apply both work on the original **and every registered sub-size file** of each attachment (the 1024px `large` of a photo saved as PNG is often 1–1.5 MB by itself, and that is what pages actually load). WordPress writes resized PNGs as truecolor, so regenerating thumbnails from a quantized original would not shrink them; each sub-size file is compressed in place instead. `wp media regenerate` runs only when an original had to be resized, so the metadata and dimension-bound sub-sizes match, and the sub-sizes that produces are then compressed too.

Apply pushes the compressed files back under the same names, deletes any stale WebP Express conversions of those files (the plugin remakes them on the next request), flushes the object cache, and tries the host's full-page/CDN purge (`wp kinsta cache purge --all` on Kinsta). Each step's result is in the log. Then load two or three affected pages on the target and check the images look right and the page weight dropped (DevTools → Network, filter Img).

Commit the `changes/<provider>/<slug>/*.md` logs; the `backup/` folders stay local.

## Step 4: hand back the APPROVE work

From the probe report:
- **Alt text list** → the user (or a content person) fills in text per row. Writing it back is `alt-text-apply` (not built yet): `_wp_attachment_image_alt` for featured images, and an attribute insert into the exact `<img>` tag for inline ones, under the usual dry/apply/log contract.
- **Broken and redirected images** → per page, by hand: re-upload the file, replace the `src`, add alt.
- **Delivery** → if no WebP plugin is active, recommend one (or Kinsta's/WP Engine's built-in conversion). Not installed by this skill.

## After

Trigger an Ahrefs recrawl. "Image file size too large" should drop to the files kept under `--min-gain`. Record the result in the client file (`platform.image_optimization_plugin`, and a note on what the probe found) and in the skill handoff doc.

## Rollback

`backup/<stamp>-fix-images-<target>/orig/` holds every replaced file byte-for-byte, originals and sub-sizes alike. Restore one with `scp` to the remote path shown in the log table. Only if an original was resized is `wp media regenerate <id> --yes` needed afterwards.

## Scope and limits

- WordPress over SSH + WP-CLI + scp, Kinsta webroot `public`, WP Engine `sites/<install>`.
- Only files Ahrefs flags are touched. A site-wide sweep of `uploads/` is deliberate scope creep for later; Ahrefs' threshold is the agreed definition of "too large".
- PNG stays PNG, JPEG stays JPEG. GIF, SVG, AVIF, WebP originals are copied through untouched.
- Writes files and attachment metadata (via regenerate) only. Never touches `post_content`, postmeta text, options or theme files.
- Every `.webp` sibling removed is one WebP Express made from a file this run replaced; nothing else in `webp-express/` is touched.
