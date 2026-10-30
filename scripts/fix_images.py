#!/usr/bin/env python3
"""Shrink oversized images in place (same URL, same format), and inventory alt-text and broken-image work.

    python scripts/fix_images.py <slug> --probe                 # inventory: server tools, WebP serving, file facts, alt/broken scan
    python scripts/fix_images.py <slug>                         # dry run on staging: pull files, compress locally, report before/after
    python scripts/fix_images.py <slug> --apply                 # push the compressed files to staging, regenerate thumbnails, flush caches
    python scripts/fix_images.py <slug> --target live --apply   # same on live (asks you to type the slug; --yes skips)

Inputs: clients/<slug>.yaml (SSH aliases, provider, domain) and the Ahrefs Site Audit "Image file size too large" issue
(AHREFS_API_KEY in .env), cached in reports/<slug>/image-inventory-<crawl-date>.json after --probe (--inventory to pick one).
Compression runs on this machine: pngquant + oxipng/optipng when on PATH, else Pillow; JPEGs are re-encoded with Pillow.
    python scripts/fix_images.py <slug> --alt-csv                  # review sheet of every image without alt, with drafted suggestions
    python scripts/fix_images.py <slug> --alt-apply <csv>           # dry run of the reviewed sheet on staging; add --apply / --target live as above

Anything longer than --max-edge pixels (default 2560, WordPress's own big-image threshold) is resized first.
A file is only replaced when the result is at least --min-gain percent smaller (default 15). Originals are kept in
changes/<provider>/<slug>/backup/ (git-ignored). Alt text and broken images are reported, never written, by this script.
"""
import argparse, csv, json, re, shutil, subprocess, sys, datetime, os, urllib.request, urllib.error
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from build_redirect_map import load_env, ahrefs, UA   # same Ahrefs plumbing; keeps one copy of the .env reader

ISSUE_ID = "c64d8113-d0f4-11e7-8ed1-001e67ed4656"   # Ahrefs "Image file size too large"
SKIP_PLUGINS = "handl-utm-grabber-v3"
UA_WEBP = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"

# ---------------------------------------------------------------- remote helpers
def ssh(alias, cmd, inp=None):
    r = subprocess.run(["ssh", alias, cmd], input=inp, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace"), r.stderr.decode("utf-8", "replace")

def wp(alias, webroot, args):
    return ssh(alias, f"cd {webroot} && wp --skip-plugins={SKIP_PLUGINS} {args}")

def run_inventory(alias, webroot, host, urls):
    job = json.dumps({"mode": "inventory", "host": host, "urls": urls})
    php = (HERE / "php" / "image_inventory.php").read_text(encoding="utf-8")
    payload = ("<?php define('IMAGE_INVENTORY_JOB', " + json.dumps(job) + "); ?>" + php).encode("utf-8")
    code, out, err = ssh(alias, f"cd {webroot} && wp --skip-plugins={SKIP_PLUGINS} eval-file -", payload)
    if "===JSON===" not in out:
        sys.exit(f"Remote inventory failed.\nstdout:\n{out[-2000:]}\nstderr:\n{err[-2000:]}")
    return json.loads(out.split("===JSON===", 1)[1].strip())

def scp(src, dst):
    r = subprocess.run(["scp", "-q", src, dst], capture_output=True)
    return r.returncode == 0, r.stderr.decode("utf-8", "replace").strip()

# ---------------------------------------------------------------- Ahrefs + WebP check
def oversized_from_ahrefs(project_id):
    data = ahrefs("site-audit/page-explorer", project_id=project_id, issue_id=ISSUE_ID,
                  select="url,size,content_type,incoming_all_links,http_code", order_by="size:desc", limit=500)
    rows = data.get("pages", [])
    hs = (ahrefs("site-audit/projects", project_id=project_id).get("healthscores") or [{}])[0]
    crawl = (hs.get("date") or "")[:10] or datetime.date.today().isoformat()
    return rows, crawl

def webp_served(url):
    """What a browser that accepts WebP actually gets for this URL: (status, content-type, bytes)."""
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": UA_WEBP, "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            ct = r.headers.get("Content-Type", ""); n = r.headers.get("Content-Length")
            if n is None: n = len(r.read())
            return r.status, ct, int(n)
    except urllib.error.HTTPError as e:
        return e.code, "", 0
    except Exception as e:
        return 0, str(e)[:80], 0

# ---------------------------------------------------------------- local compression
def have(bin_): return shutil.which(bin_) is not None

def compress(src: Path, dst: Path, max_edge: int, png_quality="80-98", jpeg_quality=82, allow_pillow=False):
    """Write a smaller version of src to dst. Returns a list of steps taken. Same format, same name."""
    from PIL import Image
    steps = []
    ext = src.suffix.lower()
    im = Image.open(src); im.load()
    w, h = im.size
    work = src
    if max(w, h) > max_edge:
        scale = max_edge / max(w, h)
        im = im.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
        steps.append(f"resized {w}x{h} -> {im.size[0]}x{im.size[1]}")
        tmp = dst.with_suffix(".resized" + ext)
        if ext == ".png": im.save(tmp, "PNG", optimize=True)
        else: im.save(tmp, "JPEG", quality=95, subsampling=0)
        work = tmp
    if ext == ".png":
        if have("pngquant"):
            r = subprocess.run(["pngquant", "--quality", png_quality, "--speed", "1", "--strip", "--force", "--output", str(dst), str(work)], capture_output=True)
            if r.returncode == 0: steps.append("pngquant " + png_quality)
            elif r.returncode == 99: shutil.copyfile(work, dst); steps.append("pngquant: quality floor not met, kept pixels")
            else: sys.exit("pngquant failed: " + r.stderr.decode("utf-8", "replace"))
        elif not allow_pillow:
            shutil.copyfile(src, dst); steps.append("SKIPPED: pngquant not on PATH and --allow-pillow not set")
            if work != src: Path(work).unlink(missing_ok=True)
            return steps
        else:
            im2 = Image.open(work); im2.load()
            has_alpha = im2.mode in ("RGBA", "LA") or (im2.mode == "P" and "transparency" in im2.info)
            method = Image.Quantize.FASTOCTREE if has_alpha else Image.Quantize.MEDIANCUT
            q = im2.convert("RGBA" if has_alpha else "RGB").quantize(colors=256, method=method, dither=Image.Dither.FLOYDSTEINBERG)
            q.save(dst, "PNG", optimize=True); steps.append("Pillow quantize 256 colors")
        for opt, args in (("oxipng", ["oxipng", "-o", "4", "--strip", "safe", "-q", str(dst)]), ("optipng", ["optipng", "-o2", "-quiet", str(dst)])):
            if have(opt): subprocess.run(args, capture_output=True); steps.append(opt); break
    elif ext in (".jpg", ".jpeg"):
        im2 = Image.open(work); im2.load()
        if im2.mode not in ("RGB", "L"): im2 = im2.convert("RGB")
        im2.save(dst, "JPEG", quality=jpeg_quality, optimize=True, progressive=True)
        steps.append(f"JPEG q{jpeg_quality} progressive")
        if have("jpegoptim"): subprocess.run(["jpegoptim", "--strip-all", "-q", str(dst)], capture_output=True); steps.append("jpegoptim")
    else:
        shutil.copyfile(work, dst); steps.append("unsupported type, copied")
    if work != src: Path(work).unlink(missing_ok=True)
    return steps


# ---------------------------------------------------------------- alt text
BRAND_TOKENS = {"waggoner", "hastings", "shadmehry", "hs", "hsfamilylaw", "family", "law", "blog", "featured", "image", "img", "scaled",
                "stock", "photo", "shutterstock", "pexels", "unsplash", "istock", "edit", "final", "copy", "new", "web", "small", "large", "thumb"}

def alt_tier(a):
    url = a.get("page_url") or ""
    if a.get("post_status") not in (None, "publish") or "?p=" in url or "?page_id=" in url: return "D"
    if a["where"].startswith("featured_image"): return "C"
    return "A" if (a["alt"] is None or (a["alt"].strip() and junk_alt(a["alt"]))) else "B"

def suggest_alt(a, firm):
    """A first draft from the page title and the file name. Humans fix it; headshots and generic names are flagged."""
    src = a.get("src") or ""; title = (a.get("title") or "").strip(" –-|")
    name = re.sub(r"\.\w+$", "", src.rsplit("/", 1)[-1])
    name = re.sub(r"-\d+x\d+$", "", name); name = re.sub(r"-e\d{10,}$", "", name)
    words = [w for w in re.split(r"[-_\s]+", name.lower()) if w and not re.fullmatch(r"\d+|[a-z]\d+|[a-z0-9]{8,}", w)]
    meaningful = [w for w in words if w not in BRAND_TOKENS]
    if "/firm/" in (a.get("page_url") or ""):
        return f"{title}, family law and divorce attorney at {firm}", "headshot"
    if src.endswith(".svg") or "logo" in name.lower() or "icon" in name.lower():
        return "", "logo/icon: leave decorative (empty alt) unless it is the only brand mention; skipped"
    if not re.search(r"\.(jpe?g|png|webp|gif|avif)$", src, re.I):
        return "", "not an image file name (pasted page junk?); remove the tag by hand, skipped"
    if len(meaningful) >= 2 and not any(w.startswith("featured") for w in words):
        phrase = " ".join(meaningful).replace("vs ", "versus ").replace("coparenting", "co-parenting")
        return phrase[0].upper() + phrase[1:], "from file name; check it describes the picture"
    return f"Illustration for the article {title}" if title else "", "generic file name: describe the actual picture"

NON_PUBLIC_TYPES = {"revision", "attachment", "nav_menu_item", "elementor_library", "tablepress_table", "acf-field", "acf-field-group",
                    "wp_block", "wp_template", "wp_template_part", "wp_global_styles", "wp_navigation", "customize_changeset", "oembed_cache",
                    "shop_order", "shop_coupon", "product_variation", "wpcf7_contact_form", "slider", "popup", "scheduled-action"}

def alt_csv(args, inv, cdir, stamp, firm):
    rows = []
    for i, a in enumerate(inv["alt"]):
        if (a.get("post_type") or "") in NON_PUBLIC_TYPES: continue   # older inventories include these; newer probes filter server-side
        tier = alt_tier(a)
        m = re.search(r"\(attachment (\d+)\)", a["where"])
        where = "featured_image" if m else a["where"]
        sug, note = suggest_alt(a, firm)
        reliable = note == "headshot"
        rows.append({"id": f"r{i+1}", "tier": tier, "post_id": a["post_id"], "page_url": a.get("page_url") or "", "title": a.get("title") or "",
                     "where": where, "attachment_id": m.group(1) if m else "", "src": a.get("src") or "",
                     "current_alt": "" if a["alt"] is None else "(empty)",
                     "new_alt": sug if (tier != "D" and reliable) else "",
                     "suggestion": sug if tier != "D" else "",
                     "note": note if tier != "D" else "unpublished; skipped"})
    order = {"A": 0, "C": 1, "B": 2, "D": 3}
    rows.sort(key=lambda r: (order[r["tier"]], r["page_url"], r["where"]))
    # One review decision per distinct image: occurrences of the same file (any size variant) share an image_key, and the
    # review sheet carries one row per key; merge_alt_sheet.py fans the decision back out to every occurrence.
    for r in rows: r["image_key"] = image_key(r["src"])
    out = cdir / f"{stamp}-fix-images-alt.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    # the review sheet
    groups = {}
    for r in rows:
        if r["tier"] == "D": continue
        g = groups.setdefault(r["image_key"], {"image_key": r["image_key"], "tier": r["tier"], "uses": 0, "pages": set(), "example_page": r["page_url"], "image": r["src"].rsplit("/", 1)[-1],
                                               "src": r["src"], "current_alt": r["current_alt"], "suggestion": r["suggestion"], "new_alt": r["new_alt"], "note": r["note"]})
        g["uses"] += 1; g["pages"].add(r["page_url"])
        if order[r["tier"]] < order[g["tier"]]: g["tier"] = r["tier"]
    deco = [g for g in groups.values() if decorative(g["image"])]
    review = [g for g in groups.values() if not decorative(g["image"])]
    review.sort(key=lambda g: (order[g["tier"]], -g["uses"], g["example_page"]))
    rpath = cdir / f"{stamp}-fix-images-alt-review.csv"
    with rpath.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(["image_key", "tier", "uses", "on_pages", "example_page", "image", "current_alt", "suggestion", "new_alt", "note"])
        for g in review: w.writerow([g["image_key"], g["tier"], g["uses"], len(g["pages"]), g["example_page"], g["image"], g["current_alt"], g["suggestion"], g["new_alt"], g["note"]])
    counts = {t: len([r for r in rows if r["tier"] == t]) for t in "ACBD"}
    print(f"{len(rows)} occurrences -> {out.name}\n  A {counts['A']} alt absent · C {counts['C']} featured images · B {counts['B']} empty alt inline · D {counts['D']} unpublished (skipped)")
    print(f"  review sheet: {len(review)} distinct images -> {rpath.name}" + (f" ({len(deco)} decorative files left out: " + ", ".join(sorted({g['image'] for g in deco})[:4]) + ")" if deco else ""))
    print(f"  {len([g for g in review if g['new_alt']])} prefilled (headshots); the rest carry a draft in `suggestion`")
    print("Review the sheet, merge with scripts/merge_alt_sheet.py, then: python scripts/fix_images.py <slug> --alt-apply " + out.name)
    return out

def image_key(src):
    """Stem that unites size variants: /2019/05/foo-300x200.jpg and /2019/05/foo.jpg -> 2019/05/foo"""
    path = re.sub(r"^(?:https?:)?//[^/]+", "", (src or "").split("?")[0])
    path = re.sub(r"^.*?/uploads/", "", path)
    path = re.sub(r"\.\w+$", "", path); path = re.sub(r"-\d+x\d+$", "", path); path = re.sub(r"-scaled$", "", path)
    return path or (src or "")

DECORATIVE = re.compile(r"^(avatar|icon|icons|spacer|pixel|blank|divider|separator|bullet|arrow|placeholder|loader|spinner|bg|pattern|decor|ornament)([-_.]|\d|$)|[-_](icon|avatar|spacer|divider|spinner|loader|bg)(-\d+x\d+)?\.\w+$|\.svg$", re.I)
def decorative(filename):
    return bool(DECORATIVE.search(filename or ""))

# ---------------------------------------------------------------- WooCommerce product alt rule
VIEW_WORDS = {"front": "front view", "back": "back view", "rear": "rear view", "side": "side view", "top": "top view", "bottom": "underside",
              "left": "left side", "right": "right side", "angle": "angled view", "angled": "angled view", "detail": "detail", "closeup": "close-up",
              "close-up": "close-up", "ports": "ports", "port": "ports", "keyboard": "keyboard", "screen": "screen", "display": "display",
              "open": "open", "closed": "closed", "dock": "docked", "docked": "docked", "mount": "mounted", "mounted": "mounted", "vehicle": "in vehicle",
              "lifestyle": "in use", "use": "in use", "inuse": "in use", "box": "packaging", "packaging": "packaging", "kit": "kit contents",
              "accessories": "accessories", "cable": "cable", "charger": "charger", "stylus": "stylus", "case": "case", "strap": "strap"}

KEEP_CAPS = {"USB", "LTE", "RF", "GPS", "VESA", "LED", "HD", "DC", "AC", "IP", "NFC", "GJ", "GPIO", "HDMI", "VGA", "DVI", "SSD", "HDD", "RAM", "CPU", "LCD", "OEM", "SKU", "KIT", "NO", "OS", "PC", "TV", "UHF", "VHF", "FM", "AM", "PSU", "UPS", "POS", "ID", "US", "UK", "EU"}
SHARED_LIMIT = 50  # an attachment used by more than this many products is a placeholder, brand image or a whole model line's photo set, not one product's photo
JUNK_ALT = re.compile(r"^(?:[\W_]+|\d+|image|img|photo|picture|pic|untitled|n/?a|none|null|alt|logo|placeholder|(?:img|image|dsc|photo|pic|screenshot)[_ -]?\d+|[\w-]*\d[\w-]*_\d+)$", re.I)

def junk_alt(a):
    """An alt that carries no information: '#', '-', a bare number or SKU, a file stem, 'image', a single character."""
    a = (a or "").strip()
    if not a: return True
    if len(a) <= 2 or JUNK_ALT.match(a) or re.search(r"\.(jpe?g|png|gif|webp|avif|svg)$", a, re.I): return True
    return False   # an attachment used by more than this many products is a placeholder/brand image, not a product photo

def clean_title(t):
    t = re.sub(r"\s*\|.*$", "", t)   # drop a "| SKU" or "| Brand" tail
    t = re.sub(r"\s+", " ", t).strip()
    # Shouting titles ("SAMSUNG GALAXY TAB ACTIVE2 DUAL USB DOCK") read badly in a screen reader; title-case them but keep
    # tokens that are model codes or units (contain digits, or are short all-caps like USB, AMPS, KIT) as they are.
    letters = [c for c in t if c.isalpha()]
    if letters and sum(c.isupper() for c in letters) / len(letters) > 0.8:
        def fix(w):
            core = re.sub(r"[^A-Za-z0-9]", "", w)
            if any(ch.isdigit() for ch in core) or core in KEEP_CAPS: return w
            return w.capitalize()
        t = " ".join(fix(w) for w in t.split(" "))
    return t

def view_suffix(filename, title):
    """A short, honest suffix from the file name: 'ports', 'side view', 'docked'. Nothing if the name says nothing."""
    name = re.sub(r"\.\w+$", "", filename); name = re.sub(r"-\d+x\d+$", "", name); name = re.sub(r"-e\d{10,}$", "", name)
    words = [w for w in re.split(r"[-_\s]+", name.lower()) if w]
    title_words = set(re.split(r"[^a-z0-9]+", title.lower()))
    hits = [VIEW_WORDS[w] for w in words if w in VIEW_WORDS and w not in title_words]
    seen = []; [seen.append(h) for h in hits if h not in seen]
    return ", ".join(seen[:2])

def product_alt_rows(inv):
    """One row per product image needing alt. Alt = cleaned product title (+ view suffix / 'view N' / variation attributes).
    Already-set alts are kept. An attachment used by more than SHARED_LIMIT products is a placeholder or brand image and is
    NOT named after a product: it goes on the exception list with a blank new_alt. An attachment shared by a few products
    (SKU variants of one model) gets the alt from the first product that uses it, which is fine when the names match."""
    use, titles = {}, {}
    for pr in inv.get("products", []):
        for im in pr["images"]:
            use.setdefault(im["attachment_id"], set()).add(pr["id"])
            titles.setdefault(im["attachment_id"], []).append(clean_title(pr["title"]))

    def shared_name(aid, title):
        """For an image several SKU variants share, the name they have in common ('Panasonic SSD 2nd Drive ... FZ-55'),
        built from the longest common word prefix and suffix of their titles; falls back to this product's title."""
        ts = [t for t in titles.get(aid, []) if t]
        if len(set(ts)) <= 1: return title
        ws = [t.split() for t in ts]
        pre = os.path.commonprefix(ws); suf = os.path.commonprefix([w[::-1] for w in ws])[::-1]
        if len(pre) + len(suf) >= len(min(ws, key=len)): suf = []
        name = " ".join(pre + suf).strip(" -:,/(")
        return name if len(name.split()) >= 3 else title
    rows, seen = [], {}
    for pr in inv.get("products", []):
        title = clean_title(pr["title"])
        if not title: continue
        n_gal = 0
        for im in pr["images"]:
            aid = im["attachment_id"]
            if im["role"] == "gallery": n_gal += 1
            base = {"product_id": pr["id"], "product": title, "url": pr["url"], "attachment_id": aid, "role": im["role"], "file": im["file"], "shared_by": len(use[aid])}
            cur = (im.get("alt") or "").strip()
            if cur and not junk_alt(cur) and len(cur.split()) > 1:
                rows.append({**base, "new_alt": "", "note": "already set, kept: " + cur[:60]}); continue
            prefix = f"replaces junk alt {cur[:30]!r}: " if cur else ""
            if len(use[aid]) > SHARED_LIMIT:
                rows.append({**base, "new_alt": "", "note": f"EXCEPTION: used by {len(use[aid])} products, likely a placeholder, brand image or shared model photo; set its alt by hand"}); continue
            if len(title.split()) < 2:
                rows.append({**base, "new_alt": "", "note": f"EXCEPTION: product title is a single word ({title}); not enough to describe the image"}); continue
            if aid in seen:
                rows.append({**base, "new_alt": "", "note": f"shared image, alt set via product {seen[aid]}"}); continue
            suffix = view_suffix(im["file"], title)
            if len(use[aid]) > 1: title = shared_name(aid, title)
            if im["role"] == "featured": alt = title
            elif im["role"] == "gallery": alt = f"{title} - {suffix or f'view {n_gal + 1}'}"
            else: alt = f"{title} - {im.get('variation') or suffix or 'variation'}"
            seen[aid] = pr["id"]
            if len(alt) > 125: alt = alt[:125].rsplit(" ", 1)[0]
            rows.append({**base, "new_alt": alt, "note": prefix})
    return rows

def product_alt(args, inv, alias, provider, host, cdir, stamp):
    rows = product_alt_rows(inv)
    todo = [r for r in rows if r["new_alt"]]
    mode = "apply" if args.apply else "dry"
    print(f"{mode.upper()} product alt on {args.target} ({alias}): {len(inv.get('products', []))} products, {len(rows)} images, {len(todo)} to set, {len(rows) - len(todo)} kept/shared")
    if not todo: print("nothing to do"); return
    if args.target == "live" and args.apply: confirm_live(args.slug, len(todo), alias, args.yes)
    sheet = cdir / f"{stamp}-fix-images-product-alt-{args.target}-{mode}.csv"
    with sheet.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    res = {"results": [], "home_host": ""}
    if True:   # dry runs go to the server too, so "already set" and missing attachments are reported from live data
        job_rows = [{"id": f"p{i}", "where": "featured_image", "post_id": r["product_id"], "attachment_id": r["attachment_id"], "src_path": "", "new_alt": r["new_alt"]} for i, r in enumerate(todo)]
        php = (HERE / "php" / "apply_alt.php").read_text(encoding="utf-8")
        for chunk in range(0, len(job_rows), 500):   # keep each eval-file payload modest
            payload = ("<?php define('APPLY_ALT_JOB', " + json.dumps(json.dumps({"mode": mode, "rows": job_rows[chunk:chunk + 500]})) + "); ?>" + php).encode("utf-8")
            code, out, err = ssh(alias, f"cd {args.webroot} && wp --skip-plugins={SKIP_PLUGINS} eval-file -", payload)
            if "===JSON===" not in out: sys.exit(f"Remote run failed.\nstdout:\n{out[-2000:]}\nstderr:\n{err[-2000:]}")
            part = json.loads(out.split("===JSON===", 1)[1].strip()); res["results"] += part["results"]; res["home_host"] = part["home_host"]
    written = len([x for x in res["results"] if x.get("applied")]); already = len([x for x in res["results"] if x.get("note", "").startswith("already")])
    exc = [r for r in rows if r["note"].startswith("EXCEPTION")]
    by_att = {}
    for r in exc: by_att.setdefault(r["attachment_id"], {"file": r["file"], "n": r["shared_by"], "titles": set(), "reason": r["note"]})["titles"].add(r["product"])
    exc_att = sorted(by_att.items(), key=lambda kv: -kv[1]["n"])
    if exc_att:
        epath = cdir / f"{stamp}-fix-images-product-alt-exceptions.csv"
        with epath.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh); w.writerow(["attachment_id", "file", "used_by_products", "example_products", "suggestion", "new_alt", "reason"])
            for a, d in exc_att:
                name = re.sub(r"\.\w+$", "", d["file"]); name = re.sub(r"-\d+x\d+$|-scaled|_?\d+x\d+", "", name)
                words = [x for x in re.split(r"[-_\s.]+", name) if x and not re.fullmatch(r"\d+", x)]
                common = os.path.commonprefix([t.lower() for t in d["titles"]]).strip(" -:,|") if len(d["titles"]) > 1 else next(iter(d["titles"]))
                sug = (common.title() + " - " if common and len(common) > 3 else "") + " ".join(words).replace("  ", " ")
                w.writerow([a, d["file"], d["n"], " | ".join(sorted(d["titles"])[:3]), sug[:125], "", d["reason"].replace("EXCEPTION: ", "")])
        print(f"  {len(exc_att)} shared attachments (covering {len(exc)} product slots) need a hand-written alt: {epath.name}")
    flush = None
    if mode == "apply":
        c, o, e = wp(alias, args.webroot, "cache flush"); flush = (c == 0, (o + e).strip())
    log = [f"# fix-images (product alt from title): {host} ({args.target})", "", f"Run {stamp} · mode **{mode}** · alias `{alias}` · provider `{provider}` · install host `{res['home_host']}`", "",
           f"{len(inv.get('products', []))} products, {len(rows)} images. {len(todo)} alts {'written' if mode == 'apply' else 'would be written'}" + (f" ({written} confirmed)" if mode == "apply" else "") + f", {already} already set on the attachment, {len(rows) - len(todo) - already} shared or kept.", "",
           f"Full list: `{sheet.name}`. Rule: featured = product title; gallery = title + view word from the file name or 'view N'; variation = title + attributes. Existing alts are never overwritten. Attachments used by more than {SHARED_LIMIT} products are placeholders or brand images and are listed in the `-exceptions.csv` for a human instead.", "",
           "Sample:", ""] + [f"- {r['role']:9} `{r['file'][:50]}` → {r['new_alt']}" for r in todo[:25]]
    if flush is not None: log += ["", f"Object cache flush: {flush}"]
    log += ["", "## Rollback", "", "Every attachment in the list had an empty `_wp_attachment_image_alt`; clearing it restores the previous state. `backup/` holds the full result."]
    lpath = cdir / f"{stamp}-fix-images-product-alt-{args.target}-{mode}.md"; lpath.write_text("\n".join(log) + "\n", encoding="utf-8")
    if mode == "apply":
        bdir = cdir / "backup"; bdir.mkdir(exist_ok=True); (bdir / f"{stamp}-fix-images-product-alt-{args.target}.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    for r in todo[:15]: print(f"  {r['role']:9} {r['file'][:45]:45} -> {r['new_alt']}")
    if len(todo) > 15: print(f"  ... {len(todo) - 15} more in {sheet.name}")
    print(f"\nLog: {lpath}")

def alt_apply(args, alias, provider, host, cdir, stamp):
    rows = list(csv.DictReader(Path(args.alt_apply).open(encoding="utf-8-sig")))
    todo = [r for r in rows if (r.get("new_alt") or "").strip() and r["tier"] != "D"]
    mode = "apply" if args.apply else "dry"
    print(f"{mode.upper()} alt text on {args.target} ({alias}): {len(todo)} of {len(rows)} rows have new_alt")
    if args.target == "live" and args.apply: confirm_live(args.slug, len(todo), alias, args.yes)
    job_rows = [{"id": r["id"], "where": r["where"], "post_id": int(r["post_id"]), "attachment_id": int(r["attachment_id"] or 0),
                 "src_path": re.sub(r"^(?:https?:)?//[^/]+", "", r["src"].split("?")[0]), "new_alt": r["new_alt"].strip()} for r in todo]
    php = (HERE / "php" / "apply_alt.php").read_text(encoding="utf-8")
    payload = ("<?php define('APPLY_ALT_JOB', " + json.dumps(json.dumps({"mode": mode, "rows": job_rows})) + "); ?>" + php).encode("utf-8")
    code, out, err = ssh(alias, f"cd {args.webroot} && wp --skip-plugins={SKIP_PLUGINS} eval-file -", payload)
    if "===JSON===" not in out: sys.exit(f"Remote run failed.\nstdout:\n{out[-2000:]}\nstderr:\n{err[-2000:]}")
    res = json.loads(out.split("===JSON===", 1)[1].strip())
    by = {r["id"]: r for r in todo}
    flush = None
    if mode == "apply":
        c, o, e = wp(alias, args.webroot, "cache flush"); flush = (c == 0, (o + e).strip())
    n_change = len([x for x in res["results"] if x["changes"] and not x["note"].startswith("already")])
    log = [f"# fix-images (alt text): {host} ({args.target})", "", f"Run {stamp} · mode **{mode}** · alias `{alias}` · provider `{provider}` · sheet `{Path(args.alt_apply).name}` · install host `{res['home_host']}`", "",
           f"{len(todo)} rows submitted, {n_change} would change" if mode == "dry" else f"{len(todo)} rows submitted, {len([x for x in res['results'] if x['applied']])} written", "",
           "| row | tier | page | where | src | new alt | result |", "|---|---|---|---|---|---|---|"]
    for x in res["results"]:
        r = by[x["id"]]; status = x["note"] or (("written" if x["applied"] else "FAILED") if mode == "apply" else f"{len(x['changes'])} tag(s) would change")
        log.append(f"| {x['id']} | {r['tier']} | {r['page_url'].replace('https://','')} | {r['where']} | `{r['src'].rsplit('/',1)[-1][:50]}` | {r['new_alt'].replace('|', '/')} | {status} |")
        print(f"  {x['id']:5} {r['tier']} {r['where'][:28]:28} {r['src'].rsplit('/',1)[-1][:45]:45} {status}")
    if flush is not None: log += ["", f"Object cache flush: {flush}"]
    log += ["", "## Rollback", "", "post_content rows: WordPress kept a revision of each changed post. featured_image and postmeta rows: previous values are in `backup/` next to this log."]
    lpath = cdir / f"{stamp}-fix-images-alt-{args.target}-{mode}.md"; lpath.write_text("\n".join(log) + "\n", encoding="utf-8")
    if mode == "apply":
        bdir = cdir / "backup"; bdir.mkdir(exist_ok=True); (bdir / f"{stamp}-fix-images-alt-{args.target}.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nLog: {lpath}")

# ---------------------------------------------------------------- main
def confirm_live(slug, n, alias, yes):
    if yes: print(f"APPLY {n} image replacements on LIVE ({alias}) — confirmed by --yes"); return
    if not sys.stdin.isatty(): sys.exit("Live apply needs a terminal to confirm, or pass --yes.")
    print(f"About to REPLACE {n} image files on LIVE ({alias}). Type the slug to confirm: ", end="", flush=True)
    if input().strip() != slug: sys.exit("aborted")

def fmt(n): return "-" if n is None else (f"{n/1048576:.2f} MB" if n >= 1048576 else f"{n/1024:.0f} KB")

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--probe", action="store_true", help="inventory only; writes reports/<slug>/image-inventory-<date>.json and images-<date>.md")
    ap.add_argument("--inventory", help="inventory JSON to use; default: newest reports/<slug>/image-inventory-*.json")
    ap.add_argument("--target", choices=["staging", "live"], default="staging")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--max-edge", type=int, default=2560)
    ap.add_argument("--min-gain", type=int, default=15, help="percent; smaller gains leave the file alone")
    ap.add_argument("--png-quality", default="80-98", help="pngquant min-max; 80-98 is visually lossless on photos, 65-85 is fine for flat graphics")
    ap.add_argument("--jpeg-quality", type=int, default=82)
    ap.add_argument("--only", help="comma-separated substrings; process only files whose path contains one")
    ap.add_argument("--webroot", default="public")
    ap.add_argument("--yes", action="store_true")
    ap.add_argument("--allow-pillow", action="store_true", help="let Pillow's 256-colour quantizer handle PNGs when pngquant is missing. OFF by default: it visibly damages photos (hsfamilylaw headshots, 2026-10-29)")
    ap.add_argument("--purge-webp", action="store_true", help="also delete .webp siblings of replaced files. OFF by default: on Kinsta (and any host where WebP rewrite rules outlive the plugin) a missing .webp breaks the image")
    ap.add_argument("--alt-csv", action="store_true", help="write changes/<provider>/<slug>/<stamp>-fix-images-alt.csv from the inventory for review (no SSH)")
    ap.add_argument("--product-alt", action="store_true", help="WooCommerce: set empty product image alts from the product title (featured, gallery, variations); dry unless --apply")
    ap.add_argument("--alt-apply", metavar="CSV", help="write the reviewed alt CSV back to the site (dry unless --apply)")
    args = ap.parse_args(argv)
    load_env()

    client = yaml.safe_load((ROOT / "clients" / f"{args.slug}.yaml").read_text(encoding="utf-8"))
    hosting = client.get("hosting", {})
    alias = hosting.get("ssh_alias") if args.target == "live" else hosting.get("staging_environment")
    if not alias or alias in ("unknown", "none"): sys.exit(f"No {args.target} SSH alias in clients/{args.slug}.yaml.")
    alias = alias.split(",")[0].strip()
    provider = str(hosting.get("provider") or "other").strip().lower() or "other"
    if provider in ("unknown", "none"): provider = "other"
    if provider == "wpengine" and args.webroot == "public": args.webroot = f"sites/{alias}"
    host = client["domain"]
    canon = client.get("canonical_host") or f"https://{host}"
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    rdir = ROOT / "reports" / args.slug; rdir.mkdir(parents=True, exist_ok=True)
    cdir = ROOT / "changes" / provider / args.slug; cdir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------ probe
    if args.probe:
        pid = client["ahrefs"]["site_audit_project_id"]
        rows, crawl = oversized_from_ahrefs(pid)
        urls = [r["url"] for r in rows]
        print(f"Ahrefs: {len(rows)} oversized images in crawl {crawl}; running inventory on {args.target} ({alias})")
        inv = run_inventory(alias, args.webroot, host, urls)
        by_url = {r["url"]: r for r in rows}
        for f in inv["files"]:
            f["ahrefs"] = {k: by_url.get(f["url"], {}).get(k) for k in ("size", "incoming_all_links", "content_type")}
            st, ct, n = webp_served(f["url"]); f["served_to_webp_browser"] = {"status": st, "content_type": ct, "bytes": n}
        inv.update({"slug": args.slug, "crawl": crawl, "target": args.target, "generated": stamp})
        jpath = rdir / f"image-inventory-{crawl}.json"
        jpath.write_text(json.dumps(inv, indent=1, ensure_ascii=False), encoding="utf-8")

        env, wb = inv["env"], inv["webp"]
        md = [f"# Image inventory: {host} ({args.target})", "", f"Crawl {crawl} · probe {stamp} · alias `{alias}` · install host `{inv['home_host']}`", ""]
        md += ["## Server", "", f"- PHP {env['php']}, Imagick: {env['imagick'] or 'no'}, GD: {env['gd'] or 'no'} (WebP {'yes' if env['gd_webp'] else 'no'})",
               "- Binaries: " + ", ".join(f"{k}: {'yes' if v else 'no'}" for k, v in env["bin"].items()),
               f"- Registered sizes: " + ", ".join(f"{k} {v['width']}x{v['height']}{'c' if v.get('crop') else ''}" for k, v in env["registered_sizes"].items()),
               "", "## Optimizer plugins", ""] + [f"- {k}: {v}" for k, v in wb.items() if not isinstance(v, (dict, list))]
        if isinstance(wb.get("webp-express-config"), dict): md += ["- WebP Express config: `" + json.dumps(wb["webp-express-config"]) + "`"]
        if isinstance(wb.get("webp-express-converted-files"), dict): md += [f"- WebP Express converted files: {wb['webp-express-converted-files']}"]
        md += ["", "## Oversized files", "", "| file | attachment | bytes | dims | largest sub-size | refs (content/meta/options/thumbs) | featured | ACF | browser w/ WebP gets |", "|---|---|---|---|---|---|---|---|---|"]
        total = 0
        for f in inv["files"]:
            total += f["bytes"] or 0
            big = max(f["sizes"].items(), key=lambda kv: (kv[1]["w"] or 0)) if f["sizes"] else None
            s = f["served_to_webp_browser"]; r = f["refs"]
            md.append(f"| `{f['path']}` | {f['attachment_id'] or '-'} | {fmt(f['bytes'])} | {f['width']}x{f['height']} | {big[0] + ' ' + str(big[1]['w']) + 'px ' + fmt(big[1]['bytes']) if big else '-'} | "
                      f"{r['post_content']}/{r['postmeta']}/{r['options']}/{r['thumbnail_refs']} | {f.get('is_featured_image_of', 0)} | {f.get('in_acf_image_fields', 0)} | {s['status']} {s['content_type']} {fmt(s['bytes'])} |")
        md += ["", f"Total on disk: {fmt(total)} across {len(inv['files'])} files.", ""]
        noref = [f["path"] for f in inv["files"] if sum(f["refs"].values()) == 0 and not f.get("is_featured_image_of") and not f.get("in_acf_image_fields")]
        if noref: md += ["Referenced nowhere in the database (theme file or CSS, or unused): " + ", ".join(f"`{p}`" for p in noref), ""]
        tiers = {"A": "alt attribute absent, published page (this is what Ahrefs counts)", "B": "alt=\"\" inline, published (decorative per HTML; usually just never filled in)",
                 "C": "featured image whose attachment has no alt (theme outputs alt=\"\"; fix once on the attachment)", "D": "not published (drafts, private): ignore"}
        md += [f"## Images without alt text ({len(inv['alt'])})", ""]
        for t, label in tiers.items():
            rows = [a for a in inv["alt"] if a.get("tier", "A" if a["alt"] is None else "B") == t]
            md += [f"### Tier {t}: {label} ({len(rows)})", ""]
            if not rows: md += ["none", ""]; continue
            md += ["| page | type | where | src | alt |", "|---|---|---|---|---|"]
            for a in rows: md.append(f"| {a.get('page_url') or a['post_id']} | {a.get('post_type')} | {a['where']} | `{(a['src'] or '')[-70:]}` | {'missing' if a['alt'] is None else 'empty'} |")
            md.append("")
        md += ["", f"## Broken image sources on this host ({len(inv['broken'])})", ""] + [f"- {b.get('page_url')} · {b['where']} · `{b['src']}`" for b in inv["broken"]]
        (rdir / f"images-{crawl}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
        print("\n".join(md[:14])); print(f"\n{len(inv['files'])} files, {fmt(total)}; {len(inv['alt'])} img without alt; {len(inv['broken'])} broken srcs")
        print(f"\nInventory: {jpath}\nReport:    {rdir / f'images-{crawl}.md'}")
        return

    if args.alt_csv or args.alt_apply or args.product_alt:
        if args.product_alt:
            inv_path = Path(args.inventory) if args.inventory else (sorted(rdir.glob("image-inventory-*.json")) or [None])[-1]
            if not inv_path: sys.exit(f"No inventory for {args.slug}; run with --probe first.")
            inv = json.loads(inv_path.read_text(encoding="utf-8"))
            if "products" not in inv: sys.exit("inventory predates the product scan; rerun --probe")
            product_alt(args, inv, alias, provider, host, cdir, stamp)
        elif args.alt_csv:
            inv_path = Path(args.inventory) if args.inventory else (sorted(rdir.glob("image-inventory-*.json")) or [None])[-1]
            if not inv_path: sys.exit(f"No inventory for {args.slug}; run with --probe first.")
            alt_csv(args, json.loads(inv_path.read_text(encoding="utf-8")), cdir, stamp, client.get("name") or host)
        else:
            alt_apply(args, alias, provider, host, cdir, stamp)
        return

    # ------------------------------------------------------------ dry / apply
    try:
        import PIL  # noqa
    except ImportError:
        sys.exit("pip install pillow  (and optionally put pngquant + oxipng on PATH for better PNG results)")
    inv_path = Path(args.inventory) if args.inventory else (sorted(rdir.glob("image-inventory-*.json")) or [None])[-1]
    if not inv_path: sys.exit(f"No inventory for {args.slug}; run with --probe first.")
    inv = json.loads(inv_path.read_text(encoding="utf-8"))
    files = [f for f in inv["files"] if f.get("file")]
    if args.only: files = [f for f in files if any(s in f["path"] for s in args.only.split(","))]
    if args.target != inv.get("target"):
        print(f"note: inventory was taken on {inv.get('target')}; file paths are re-resolved on {args.target} by relative upload path")
    mode = "apply" if args.apply else "dry"
    print(f"{mode.upper()} on {args.target} ({alias}): {len(files)} files, max edge {args.max_edge}px, min gain {args.min_gain}%")
    if args.target == "live" and args.apply: confirm_live(args.slug, len(files), alias, args.yes)

    bdir = cdir / "backup" / f"{stamp}-fix-images-{args.target}"; (bdir / "orig").mkdir(parents=True); (bdir / "new").mkdir()
    # remote uploads root for this target (staging has a different absolute path than live)
    code, out, _ = wp(alias, args.webroot, "eval 'echo wp_upload_dir()[\"basedir\"];'")
    remote_base = out.strip()
    if code != 0 or not remote_base.startswith("/"): sys.exit(f"Could not resolve uploads dir on {alias}: {out} ")
    results = []
    def process(rel, attachment_id, kind, max_edge):
        """Pull one remote file, compress it locally, push it back on apply. Returns the result row."""
        remote = f"{remote_base}/{rel}"
        local_o = bdir / "orig" / Path(rel).name; local_n = bdir / "new" / Path(rel).name
        row = {"path": rel, "kind": kind, "attachment_id": attachment_id, "remote": remote, "before": None, "after": None, "steps": [], "action": None, "gain_pct": None}
        ok, err = scp(f"{alias}:{remote}", str(local_o))
        if not ok: row["action"] = f"PULL FAILED: {err}"; print(f"  !! {rel}: pull failed {err}"); return row
        row["before"] = local_o.stat().st_size
        row["steps"] = compress(local_o, local_n, max_edge, args.png_quality, args.jpeg_quality, args.allow_pillow)
        row["after"] = local_n.stat().st_size
        gain = 100 * (1 - row["after"] / row["before"]) if row["before"] else 0
        row["gain_pct"] = round(gain, 1)
        if any(st.startswith("SKIPPED") for st in row["steps"]): row["action"] = "skipped (no pngquant)"; print(f"  -- {rel}: skipped, pngquant not on PATH"); return row
        if gain < args.min_gain: row["action"] = "kept (gain below threshold)"; print(f"  -- {rel}: {fmt(row['before'])} -> {fmt(row['after'])} ({gain:.0f}%), kept"); return row
        if mode == "apply":
            ok, err = scp(str(local_n), f"{alias}:{remote}")
            row["action"] = "replaced" if ok else f"PUSH FAILED: {err}"
        else:
            row["action"] = "would replace"
        print(f"  {'OK' if 'FAIL' not in row['action'] else '!!'} {rel}: {fmt(row['before'])} -> {fmt(row['after'])} ({gain:.0f}%) {'; '.join(row['steps'])}")
        return row

    regenerated = {}
    for f in files:
        rel = re.sub(r"^.*?/uploads/", "", f["path"])
        row = process(rel, f.get("attachment_id"), "original", args.max_edge)
        results.append(row)
        if "FAILED" in (row["action"] or ""): continue
        sizes = f.get("sizes") or {}
        # Sub-sizes are what pages actually load (the 1024px "large" of a photo-PNG can be 1.5 MB on its own).
        # WordPress saves resized PNGs as truecolor, so regenerating from a quantized original would NOT shrink them:
        # compress each existing sub-size file in place too. If the original was resized, regenerate first so the
        # metadata and any dimension-bound sub-sizes match, then compress whatever files that produced.
        if any(st.startswith("resized") for st in row["steps"]) and row["action"] == "replaced" and f.get("attachment_id"):
            code, out, err = wp(alias, args.webroot, f"media regenerate {f['attachment_id']} --yes")
            regenerated[f["attachment_id"]] = (code == 0, (out + err).strip().splitlines()[-1:])
            code, out, err = wp(alias, args.webroot, f"post meta get {f['attachment_id']} _wp_attachment_metadata --format=json")
            try: sizes = json.loads(out).get("sizes", {}) if code == 0 else sizes
            except json.JSONDecodeError: pass
        seen = set()
        for name, sz in sizes.items():
            fn = sz.get("file") if isinstance(sz, dict) else None
            if not fn:  # inventory rows only carry w/h/bytes; derive the WordPress name
                fn = re.sub(r"(\.\w+)$", f"-{sz['w']}x{sz['h']}\\1", Path(rel).name)
            if fn in seen: continue
            seen.add(fn)
            results.append(process(str(Path(rel).parent / fn).replace("\\", "/"), f.get("attachment_id"), f"sub-size {name}", 10 ** 6))

    regen = regenerated or None; flush = cdn = webp_purge = None
    if mode == "apply":
        # stale WebP Express conversions of the replaced originals and their thumbnails
        stems = sorted({re.sub(r"\.\w+$", "", r["path"]) for r in results if r["action"] == "replaced" and r["kind"] == "original"})
        if stems and args.purge_webp:
            finds = " ".join(f"-path '*/{s}*.webp' -o" for s in stems).rstrip(" -o")
            code, out, err = ssh(alias, f"cd {args.webroot} && find wp-content/webp-express wp-content/uploads \\( {finds} \\) -type f -print -delete 2>/dev/null | wc -l")
            webp_purge = out.strip()
            print(f"Removed {webp_purge} .webp siblings (--purge-webp)")
        elif stems:
            webp_purge = "skipped (not requested; see --purge-webp). If a WebP plugin or host rule serves .webp siblings, regenerate them with scripts/regen_webp_siblings.py"
        code, out, err = wp(alias, args.webroot, "cache flush"); flush = (code == 0, (out + err).strip())
        code, out, err = wp(alias, args.webroot, "kinsta cache purge --all" if provider == "kinsta" else "page-cache flush") ; cdn = (code == 0, (out + err).strip()[-120:])
        print(f"Object cache flush: {'ok' if flush[0] else 'FAILED'}; host/CDN cache purge: {'ok' if cdn[0] else 'not available'} {cdn[1]}")

    before = sum(r["before"] or 0 for r in results); after = sum((r["after"] if r["action"] in ("replaced", "would replace") else r["before"]) or 0 for r in results)
    log = [f"# fix-images: {host} ({args.target})", "", f"Run {stamp} · mode **{mode}** · alias `{alias}` · provider `{provider}` · inventory `{inv_path.name}` · max edge {args.max_edge}px · min gain {args.min_gain}% · PNG {args.png_quality} · JPEG q{args.jpeg_quality}", "",
           f"Tools: pngquant {'yes' if have('pngquant') else 'no (Pillow quantize)'}, oxipng {'yes' if have('oxipng') else 'no'}, optipng {'yes' if have('optipng') else 'no'}, jpegoptim {'yes' if have('jpegoptim') else 'no'}", "",
           f"**{fmt(before)} → {fmt(after)}** across {len(results)} files ({len([r for r in results if r['action'] in ('replaced','would replace')])} {'replaced' if mode=='apply' else 'would be replaced'}).", "",
           "| file | kind | attachment | before | after | gain | steps | action |", "|---|---|---|---|---|---|---|---|"]
    for r in results: log.append(f"| `{r['path']}` | {r['kind']} | {r['attachment_id'] or '-'} | {fmt(r['before'])} | {fmt(r['after'])} | {r.get('gain_pct') if r.get('gain_pct') is not None else '-'}% | {'; '.join(r['steps'])} | {r['action']} |")
    if mode == "apply":
        log += ["", f"Thumbnails regenerated (only where the original was resized): {regen}", f"Stale .webp removed: {webp_purge}", f"Object cache flush: {flush}", f"Host/CDN purge: {cdn}"]
    log += ["", "## Rollback", "", f"Originals are in `backup/{bdir.name}/orig/`. To restore one: `scp backup/.../orig/<name> {alias}:<remote path from the table>` then `wp media regenerate <id> --yes`.",
            "", "## Not done by this run", "", "Alt text and broken/redirected images are in the probe report (`reports/<slug>/images-<crawl>.md`) and are APPROVE-tier, per page."]
    lpath = cdir / f"{stamp}-fix-images-{args.target}-{mode}.md"
    lpath.write_text("\n".join(log) + "\n", encoding="utf-8")
    (bdir / "result.json").write_text(json.dumps(results, indent=1), encoding="utf-8")
    n_o = len([r for r in results if r["kind"] == "original"]); n_s = len(results) - n_o
    print(f"\n{fmt(before)} -> {fmt(after)} across {n_o} originals + {n_s} sub-size files\nLog: {lpath}\nFiles: {bdir}")

if __name__ == "__main__":
    main()
