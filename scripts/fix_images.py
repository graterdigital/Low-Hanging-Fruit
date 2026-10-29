#!/usr/bin/env python3
"""Shrink oversized images in place (same URL, same format), and inventory alt-text and broken-image work.

    python scripts/fix_images.py <slug> --probe                 # inventory: server tools, WebP serving, file facts, alt/broken scan
    python scripts/fix_images.py <slug>                         # dry run on staging: pull files, compress locally, report before/after
    python scripts/fix_images.py <slug> --apply                 # push the compressed files to staging, regenerate thumbnails, flush caches
    python scripts/fix_images.py <slug> --target live --apply   # same on live (asks you to type the slug; --yes skips)

Inputs: clients/<slug>.yaml (SSH aliases, provider, domain) and the Ahrefs Site Audit "Image file size too large" issue
(AHREFS_API_KEY in .env), cached in reports/<slug>/image-inventory-<crawl-date>.json after --probe (--inventory to pick one).
Compression runs on this machine: pngquant + oxipng/optipng when on PATH, else Pillow; JPEGs are re-encoded with Pillow.
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

def compress(src: Path, dst: Path, max_edge: int, png_quality="65-85", jpeg_quality=82):
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
    ap.add_argument("--png-quality", default="65-85")
    ap.add_argument("--jpeg-quality", type=int, default=82)
    ap.add_argument("--only", help="comma-separated substrings; process only files whose path contains one")
    ap.add_argument("--webroot", default="public")
    ap.add_argument("--yes", action="store_true")
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
        row["steps"] = compress(local_o, local_n, max_edge, args.png_quality, args.jpeg_quality)
        row["after"] = local_n.stat().st_size
        gain = 100 * (1 - row["after"] / row["before"]) if row["before"] else 0
        row["gain_pct"] = round(gain, 1)
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
        if stems and inv.get("webp", {}).get("webp-express") == "active":
            finds = " ".join(f"-path '*/{s}*.webp' -o" for s in stems).rstrip(" -o")
            code, out, err = ssh(alias, f"cd {args.webroot} && find wp-content/webp-express wp-content/uploads \\( {finds} \\) -type f -print -delete 2>/dev/null | wc -l")
            webp_purge = out.strip()
            print(f"Removed {webp_purge} stale .webp conversions (WebP Express regenerates them on request)")
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
