#!/usr/bin/env python3
"""Rewrite internal links that point at redirecting URLs so they point at the final page.

    python scripts/fix_redirect_links.py <slug> --map <redirect-map.json>              # dry run on staging
    python scripts/fix_redirect_links.py <slug> --map <redirect-map.json> --apply      # apply on staging
    python scripts/fix_redirect_links.py <slug> --map <redirect-map.json> --target live --apply

Reads clients/<slug>.yaml for the SSH aliases, ships scripts/php/replace_links.php to the site over SSH
with `wp eval-file`, and writes a change log to changes/<provider>/<slug>/ (provider from the client file:
kinsta, wpengine, ...). Dry run is the default; every apply also saves the full before/after content of
each changed post to changes/<provider>/<slug>/backup/ (git-ignored) and flushes the object cache.
A second, report-only log lists wp_options rows that still contain an old URL; the script never edits options.
Live applies ask you to type the slug unless --yes is given.
"""
import argparse, json, re, subprocess, sys, datetime, urllib.request, urllib.parse, urllib.error, html
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SKIP_PLUGINS = "handl-utm-grabber-v3"   # prints PHP warnings under CLI; harmless but noisy

def run_remote(alias, mode, host, swaps, webroot="public", legacy_hosts=None):
    job = json.dumps({"mode": mode, "host": host, "swaps": swaps, "legacy_hosts": legacy_hosts or []})
    php = (HERE / "php" / "replace_links.php").read_text(encoding="utf-8")
    # Prepend the job as a constant so the PHP file itself stays generic.
    payload = "<?php define('REPLACE_LINKS_JOB', " + json.dumps(job) + "); ?>" + php
    cmd = ["ssh", alias, f"cd {webroot} && wp --skip-plugins={SKIP_PLUGINS} eval-file -"]
    r = subprocess.run(cmd, input=payload.encode("utf-8"), capture_output=True)
    out = r.stdout.decode("utf-8", "replace")
    if "===JSON===" not in out:
        sys.exit(f"Remote run failed.\nstdout:\n{out[-2000:]}\nstderr:\n{r.stderr.decode('utf-8','replace')[-2000:]}")
    return json.loads(out.split("===JSON===", 1)[1].strip())

def flush_cache(alias, webroot="public"):
    """wp cache flush after an apply: postmeta is written straight to the table, so a persistent object
    cache (Kinsta's Redis, WP Engine's) would otherwise keep serving the old ACF values."""
    r = subprocess.run(["ssh", alias, f"cd {webroot} && wp --skip-plugins={SKIP_PLUGINS} cache flush"], capture_output=True)
    msg = (r.stdout.decode("utf-8", "replace") + r.stderr.decode("utf-8", "replace")).strip().splitlines()
    return (r.returncode == 0, msg[-1] if msg else "")

UA = "Mozilla/5.0 (compatible; GraterDigital-LHF/1.0; +https://graterdigital.com)"

def _fetch(url, method="GET", follow=False, timeout=20):
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k): return None
    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(NoRedirect)
    try:
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
        with opener.open(req, timeout=timeout) as r:
            return r.status, (r.read().decode("utf-8", "replace") if method == "GET" else ""), r.headers.get("Location", "")
    except urllib.error.HTTPError as e:
        return e.code, "", e.headers.get("Location", "") if e.headers else ""
    except Exception as e:
        return f"error: {type(e).__name__}", "", ""

def check_links(pages, site_host, swaps, legacy_hosts=()):
    """Fetch each page, HEAD every unique internal link on it (no redirects followed), and report non-200s.
    Links whose path is one of the swap targets are flagged separately so a bad swap stands out."""
    site_host = re.sub(r"^www\.", "", site_host.lower())
    # Exact paths: a slash-only swap (/about -> /about/) must not collapse old and new into one key.
    new_paths = {urllib.parse.urlsplit(s["new"]).path or "/" for s in swaps}
    old_paths = {urllib.parse.urlsplit(s["old"]).path or "/" for s in swaps}
    def internal(href, base):
        href = html.unescape(href.strip())
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")): return None
        u = urllib.parse.urljoin(base, href); s = urllib.parse.urlsplit(u)
        if s.scheme not in ("http", "https"): return None
        h = re.sub(r"^www\.", "", s.netloc.lower())
        if h != site_host and h not in {re.sub(r"^www\.", "", l.lower()) for l in legacy_hosts}: return None
        return urllib.parse.urlunsplit((s.scheme, s.netloc, s.path or "/", s.query, ""))
    page_results, links = {}, {}
    def do_page(url):
        st, body, _ = _fetch(url, "GET", follow=True)
        found = set()
        if isinstance(st, int) and st == 200:
            for href in re.findall(r"""<a\s[^>]*?href\s*=\s*["']([^"']+)["']""", body, flags=re.I):
                u = internal(href, url)
                if u: found.add(u)
        return url, st, found
    with ThreadPoolExecutor(max_workers=6) as ex:
        for url, st, found in ex.map(do_page, pages):
            page_results[url] = st
            for u in found: links.setdefault(u, set()).add(url)
    def do_link(u):
        st, _, loc = _fetch(u, "HEAD")
        if st in (403, 405, 501): st, _, loc = _fetch(u, "GET")
        return u, st, loc
    link_results = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        for u, st, loc in ex.map(do_link, sorted(links)): link_results[u] = (st, loc)
    bad = []
    for u, (st, loc) in sorted(link_results.items()):
        if st == 200: continue
        if st in (401, 403, 429, 503) or isinstance(st, str): continue   # firewall/rate limit answered, not the page; the builder already trusted Ahrefs here
        path = urllib.parse.urlsplit(u).path or "/"
        bad.append({"url": u, "status": st, "location": loc, "on_pages": sorted(links[u]),
                    "is_swap_target": path in new_paths, "is_old_url": path in old_paths and path not in new_paths})
    return {"pages": page_results, "links_checked": len(link_results), "bad": bad}

def write_linkcheck_log(outdir, base, host, target, res, skipped=None):
    bad = res["bad"]; pages_bad = {u: s for u, s in res["pages"].items() if s != 200}
    unverifiable = {u: s for u, s in pages_bad.items() if s in (401, 403, 429, 503) or isinstance(s, str)}
    pages_bad = {u: s for u, s in pages_bad.items() if u not in unverifiable}
    lines = [f"# fix-redirect-links: link check for {host} ({target})", "",
             f"{len(res['pages'])} published changed page(s) fetched, {res['links_checked']} unique internal link(s) HEAD-checked without following redirects. Anything not 200 is listed.", ""]
    if skipped: lines += [f"{len(skipped)} changed post(s) not checked because they are not published pages (drafts, private, templates, menu items): " + ", ".join(f"{k} ({v})" for k, v in list(skipped.items())[:12]) + (" ..." if len(skipped) > 12 else ""), ""]
    if unverifiable: lines += ["## Changed pages the checker could not fetch (firewall or rate limit answered, not the page)", ""] + [f"- {u}: {s}" for u, s in unverifiable.items()] + [""]
    if pages_bad: lines += ["## Changed published pages that did not return 200", ""] + [f"- {u}: {s}" for u, s in pages_bad.items()] + [""]
    sw = [b for b in bad if b["is_swap_target"]]; ol = [b for b in bad if b["is_old_url"] and not b["is_swap_target"]]; other = [b for b in bad if not b["is_swap_target"] and not b["is_old_url"]]
    def table(rows):
        out = ["| link | status | redirects to | on pages |", "|---|---|---|---|"]
        for b in rows: out.append(f"| {b['url']} | {b['status']} | {b['location'] or ''} | {len(b['on_pages'])}: {', '.join(b['on_pages'][:3])}{' ...' if len(b['on_pages']) > 3 else ''} |")
        return out
    lines += [f"## Swap targets not returning 200 ({len(sw)})", "", "A fixed link that does not resolve to 200 means the map's `new` URL is wrong or the target changed. Stop and look." if sw else "None."] + (table(sw) if sw else []) + [""]
    lines += [f"## Old URLs still linked ({len(ol)})", "", "Links the rewrite did not reach: theme files, builder blobs it does not read, or links rendered by a plugin." if ol else "None."] + (table(ol) if ol else []) + [""]
    lines += [f"## Other internal links not returning 200 ({len(other)})", "", "Pre-existing redirects and broken links on the same pages; not caused by this run, listed for the next fix." if other else "None."] + (table(other) if other else [])
    (outdir / f"{base}-linkcheck.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(sw), len(ol), len(other), len(pages_bad)

def confirm_live(slug, n, alias, yes):
    if yes:
        print(f"APPLY {n} link swaps on LIVE ({alias}) — confirmed by --yes"); return
    if not sys.stdin.isatty():
        sys.exit("Live apply needs a terminal to confirm, or pass --yes.")
    print(f"About to APPLY {n} link swaps on LIVE ({alias}). Type the slug to confirm: ", end="", flush=True)
    if input().strip() != slug: sys.exit("aborted")

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--map", help="redirect map JSON; default: newest reports/<slug>/redirect-map-*.json")
    ap.add_argument("--target", choices=["staging", "live"], default="staging")
    ap.add_argument("--apply", action="store_true", help="write changes; default is dry run")
    ap.add_argument("--probe", action="store_true", help="locate every raw occurrence of each old URL (posts, meta, options) and stop; changes nothing")
    ap.add_argument("--webroot", default="public", help="path to WordPress relative to the SSH login dir (Kinsta: public; WP Engine: sites/<install>)")
    ap.add_argument("--check-links", action="store_true", dest="checklinks", help="fetch the pages changed by the latest apply log on this target and HEAD-check every internal link; writes a -linkcheck.md")
    ap.add_argument("--no-link-check", action="store_true", help="skip the automatic link check after an apply")
    ap.add_argument("--check-json", action="store_true", dest="checkjson", help="validate every _elementor_data row on the target and stop; changes nothing")
    ap.add_argument("--yes", action="store_true", help="skip the type-the-slug confirmation on a live apply (for vetted, unattended runs)")
    args = ap.parse_args(argv)
    return run(args)

def latest_map(slug):
    maps = sorted((ROOT / "reports" / slug).glob("redirect-map-*.json"))
    return maps[-1] if maps else None

def run(args):
    """Runs one target/mode and returns the remote result dict (with 'log' and 'options_log' paths added), or None for probe."""
    if not args.map:
        args.map = latest_map(args.slug)
        if not args.map: sys.exit(f"No redirect map for {args.slug}; run scripts/build_redirect_map.py {args.slug} first.")
    client = yaml.safe_load((ROOT / "clients" / f"{args.slug}.yaml").read_text(encoding="utf-8"))
    hosting = client.get("hosting", {})
    alias = hosting.get("ssh_alias") if args.target == "live" else hosting.get("staging_environment")
    if not alias or alias in ("unknown", "none"):
        sys.exit(f"No {args.target} SSH alias in clients/{args.slug}.yaml (hosting.{'ssh_alias' if args.target=='live' else 'staging_environment'}). Run scripts/ssh_config_sync.py first.")
    alias = alias.split(",")[0].strip()
    provider = str(hosting.get("provider") or "other").strip().lower()
    if provider in ("", "unknown", "none"): provider = "other"
    if provider == "wpengine" and args.webroot == "public":
        args.webroot = f"sites/{alias}"
    host = client["domain"]
    m = json.loads(Path(args.map).read_text(encoding="utf-8"))
    swaps = m["swaps"]
    # On LIVE, the non-canonical host variant (www. vs bare) is treated as a legacy host so links on it are moved
    # to the canonical host: the path was already right, but every such link still costs a redirect hop.
    # Staging keeps hosts as found (its own host is never the canonical one).
    legacy_hosts = list(m.get("legacy_hosts") or [])
    canon = urllib.parse.urlsplit(client.get("canonical_host") or f"https://{host}").netloc.lower()
    if args.target == "live" and canon:
        variant = canon[4:] if canon.startswith("www.") else "www." + canon
        if variant not in legacy_hosts: legacy_hosts.append(variant)
    m["legacy_hosts"] = legacy_hosts
    if args.target == "live" and args.apply:
        confirm_live(args.slug, len(swaps), alias, args.yes)

    if getattr(args, "checklinks", False):
        bdir = ROOT / "changes" / provider / args.slug / "backup"
        backups = sorted(bdir.glob(f"*-fix-redirect-links-{args.target}.json")) if bdir.exists() else []
        if not backups: sys.exit(f"No apply backup for {args.slug} on {args.target}; the link check needs the list of changed pages.")
        b = json.loads(backups[-1].read_text(encoding="utf-8"))
        pages = b.get("check_urls") or sorted({p["url"] for p in b.get("posts", []) if p.get("url")})
        res = check_links(pages, host, swaps, m.get("legacy_hosts") or [])
        outdir = ROOT / "changes" / provider / args.slug; outdir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
        sw, ol, other, pb = write_linkcheck_log(outdir, f"{stamp}-fix-redirect-links-{args.target}", host, args.target, res, b.get("check_skipped"))
        print(f"LINK CHECK on {args.target}: {len(pages)} pages, {res['links_checked']} links; {sw} swap target(s) not 200, {ol} old URL(s) still linked, {other} other non-200, {pb} page(s) not 200")
        print(f"Log: {outdir / (stamp + '-fix-redirect-links-' + args.target + '-linkcheck.md')}")
        return {"posts": [], "meta": [], "totals": {}, "errors": sw + pb, "linkcheck": (sw, ol, other, pb), "log": None, "options_log": None}

    if getattr(args, "checkjson", False):
        res = run_remote(alias, "checkjson", host, [], args.webroot, [])
        bad = res["invalid"]
        print(f"CHECK-JSON on {args.target} ({alias}): {res['checked']} _elementor_data rows, {len(bad)} invalid")
        for b in bad: print(f"   post {b['post_id']} ({b['type']}/{b['status']}) {b['title'][:50]}  {b['url']}  [{b['error']}]")
        res["log"] = None; res["options_log"] = None; res["errors"] = len(bad); res["posts"] = []; res["meta"] = []; res["totals"] = {}
        return res

    if args.probe:
        res = run_remote(alias, "probe", host, swaps, args.webroot, m.get("legacy_hosts"))
        print(f"Install runs on {res['home_host']}; matching hosts: {', '.join(res['hosts'])}")
        occ = res["occurrences"]
        print(f"PROBE on {args.target} ({alias}): {len(occ)} occurrences")
        by = {}
        for o in occ: by.setdefault(o["old"], []).append(o)
        for s_ in swaps:
            items = by.get(s_["old"], [])
            print(f"\n== {s_['old']}  ({len(items)} found)")
            for o in items: print(f"   {o['where']}\n      ...{o['ctx'].replace(chr(10),' ')}...")
        return None

    mode = "apply" if args.apply else "dry"
    print(f"{mode.upper()} on {args.target} ({alias}), {len(swaps)} swap rules, webroot {args.webroot}")
    res = run_remote(alias, mode, host, swaps, args.webroot, m.get("legacy_hosts"))
    print(f"Install runs on {res['home_host']}; matching hosts: {', '.join(res['hosts'])}")

    if not isinstance(res.get("totals"), dict): res["totals"] = {}   # PHP encodes an empty array as []
    flushed = None
    if mode == "apply":
        flushed = flush_cache(alias, args.webroot)
        print(f"Cache flush: {'ok' if flushed[0] else 'FAILED'} {flushed[1]}")
    stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    outdir = ROOT / "changes" / provider / args.slug; outdir.mkdir(parents=True, exist_ok=True)
    base = f"{stamp}-fix-redirect-links-{args.target}"
    log = [f"# fix-redirect-links: {host} ({args.target})", "", f"Run {stamp} · mode **{mode}** · alias `{alias}` · provider `{provider}` · map `{Path(args.map).name}`", ""]
    log += [f"Install host `{res['home_host']}`; hosts matched: {', '.join('`'+h+'`' for h in res['hosts'])}. Entries starting `host:` are legacy-host links moved to the current host.", ""]
    if flushed is not None:
        log += [f"Object cache flush after apply: {'ok' if flushed[0] else 'FAILED'}" + (f" (`{flushed[1]}`)" if flushed[1] else ""), ""]
    log += ["## Totals (replacements per old URL)", ""] + [f"- `{k}` → {v}" for k, v in sorted(res["totals"].items())] + [""]
    log += [f"## Posts changed ({len(res['posts'])})", "", "| ID | type | title | URL | replacements | applied |", "|---|---|---|---|---|---|"]
    for p in res["posts"]:
        log.append(f"| {p['id']} | {p['type']} | {p['title'][:50]} | {p['url']} | {sum(p['hits'].values())} | {p.get('applied', '-')} |")
    log += ["", f"## Postmeta changed ({len(res['meta'])})", "", "| meta_id | post | key | kind | replacements | applied |", "|---|---|---|---|---|---|"]
    for mm in res["meta"]:
        log.append(f"| {mm['meta_id']} | {mm['post_id']} | {mm['key']} | {mm.get('kind','')}{' (menu: ' + str(mm.get('title',''))[:30] + ')' if mm.get('kind') == 'menu' else ''} | {sum(mm['hits'].values())} | {mm.get('applied', '-')} |")
    log += ["", "## Skipped by the map", ""] + [f"- {s.get('old') or s.get('pattern')}: {s['reason']}" for s in m.get("skipped", [])]
    refused = res.get("refused") or []; guarded = res.get("json_guarded") or []
    if refused: log += ["## Swaps refused by the matcher (unsafe characters)", ""] + [f"- `{r['old']}`: {r['reason']}" for r in refused] + [""]
    if guarded:
        log += [f"## Rewrites blocked by the JSON guard ({len(guarded)})", "", "These meta values are valid JSON and the rewrite would have broken them. Nothing was written; the swap rule or the matcher needs a look.", "",
                "| meta_id | post | key | hits |", "|---|---|---|---|"] + [f"| {g['meta_id']} | {g['post_id']} | {g['key']} | {sum(g['hits'].values())} |" for g in guarded] + [""]
    opts = res.get("options") or []
    log += ["", f"## wp_options still referencing old URLs ({len(opts)}, not changed)", "",
            f"See `{base}-options.md` next to this log. Widgets, theme mods, menus and plugin settings live here and need a hand or a different skill." if opts else "None found."]
    log += ["", "## Rollback", "", "Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.",
            "Postmeta: previous values are in the same backup file."]
    main_log = outdir / f"{base}-{mode}.md"
    main_log.write_text("\n".join(log) + "\n", encoding="utf-8")

    # Secondary, report-only log: wp_options rows that contain an old path or legacy host.
    olog = [f"# fix-redirect-links: wp_options hits for {host} ({args.target})", "",
            f"Run {stamp} · mode **{mode}** · companion to `{main_log.name}`. Report only: the script never edits options.", "",
            "Each row is an option whose value contains an old URL (transients are excluded). `autoload` and size help tell a widget or menu setting from an analytics or cache blob, which can be ignored.", ""]
    if opts:
        olog += ["| option_name | autoload | bytes | old URL | context |", "|---|---|---|---|---|"]
        for o in opts:
            ctx = o["ctx"].replace("\n", " ").replace("|", "\\|")
            olog.append(f"| `{o['option_name']}` | {o['autoload']} | {o['size']} | `{o['old']}` | ...{ctx}... |")
    else:
        olog.append("No option values reference any of the old URLs or legacy hosts.")
    (outdir / f"{base}-options.md").write_text("\n".join(olog) + "\n", encoding="utf-8")

    if mode == "apply":
        bdir = outdir / "backup"; bdir.mkdir(exist_ok=True)
        (bdir / f"{base}.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    res["linkcheck"] = None
    if mode == "apply" and not getattr(args, "no_link_check", False) and res.get("check_urls"):
        lc = check_links(res["check_urls"], host, swaps, m.get("legacy_hosts") or [])
        sw, ol, other, pb = write_linkcheck_log(outdir, base, host, args.target, lc, res.get("check_skipped"))
        res["linkcheck"] = (sw, ol, other, pb)
        print(f"Link check: {len(res['check_urls'])} pages, {lc['links_checked']} links; {sw} swap target(s) not 200, {ol} old URL(s) still linked, {other} other non-200, {pb} page(s) not 200  -> {base}-linkcheck.md")

    print(f"\n{len(res['posts'])} posts, {len(res['meta'])} meta rows would change" if mode == "dry" else f"\n{len(res['posts'])} posts, {len(res['meta'])} meta rows changed")
    for k, v in sorted(res["totals"].items()): print(f"  {v:3}  {k}")
    print(f"  {len(opts)} wp_options rows still reference old URLs (not changed; see the -options.md log)")
    if refused: print(f"  {len(refused)} swap(s) REFUSED for unsafe characters: " + ", ".join(r['old'] for r in refused))
    if guarded: print(f"  {len(guarded)} meta row(s) BLOCKED by the JSON guard; see log")
    print(f"\nLog: {main_log}\nOptions log: {outdir / (base + '-options.md')}")
    errs = [p for p in res["posts"] if str(p.get("applied", "")).startswith("ERROR")]
    if errs: print(f"\n{len(errs)} posts failed to save; see log.")
    res["log"] = str(main_log); res["options_log"] = str(outdir / (base + "-options.md")); res["errors"] = len(errs)
    res["flushed"] = None if flushed is None else bool(flushed[0]); res["alias"] = alias; res["provider"] = provider
    res["guarded"] = len(guarded); res["refused_n"] = len(refused)
    return res

if __name__ == "__main__":
    main()
