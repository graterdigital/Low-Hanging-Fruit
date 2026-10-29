#!/usr/bin/env python3
"""Build reports/<slug>/redirect-map-<crawl-date>.json from the Ahrefs Site Audit "3XX redirect" issue.

    python scripts/build_redirect_map.py <slug>                # build (verifies each target with a HEAD request)
    python scripts/build_redirect_map.py <slug> --no-verify    # trust Ahrefs' final_redirect_code, skip the HEAD requests
    python scripts/build_redirect_map.py <slug> --print        # also dump the map to stdout

Needs AHREFS_API_KEY in the environment or in a .env file at the repo root (KEY=value lines; .env is git-ignored).
Reads clients/<slug>.yaml for ahrefs.site_audit_project_id and domain. Applies the swap/skip rules from
skills/fix-redirect-links/SKILL.md; every skipped URL carries its reason so the change log can show it.
Legacy hosts are not discoverable from Ahrefs (they only show up in content); add them by hand or from a --probe run,
and they are preserved when an existing map for the same crawl is rebuilt.
"""
import argparse, json, os, re, sys, datetime, urllib.request, urllib.parse, urllib.error
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
API = "https://api.ahrefs.com/v3"
ISSUE_NAME = "3XX redirect"
SELECT = "url,http_code,redirect,redirect_code,final_redirect,final_redirect_code,incoming_all_links,nr_redirect_chain_urls"
UA = "Mozilla/5.0 (compatible; GraterDigital-LHF/1.0; +https://graterdigital.com)"

def load_env():
    """Read KEY=value lines from .env at the repo root. Tolerates the BOM and UTF-16 that PowerShell's Set-Content can write."""
    f = ROOT / ".env"
    if not f.exists(): return
    raw = f.read_bytes()
    text = raw.decode("utf-16") if raw[:2] in (b"\xff\xfe", b"\xfe\xff") else raw.decode("utf-8-sig", "replace")
    lines = [l.strip().lstrip("\ufeff") for l in text.splitlines() if l.strip() and not l.strip().startswith("#")]
    for line in lines:
        if "=" in line:
            k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    # A file that is nothing but the key itself (no KEY= prefix) is taken as the Ahrefs key.
    if len(lines) == 1 and "=" not in lines[0] and " " not in lines[0]:
        os.environ.setdefault("AHREFS_API_KEY", lines[0].strip('"').strip("'"))

def ahrefs(path, **params):
    key = os.environ.get("AHREFS_API_KEY")
    if not key: sys.exit("AHREFS_API_KEY not set (environment or .env at the repo root).")
    url = f"{API}/{path}?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {key}", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        sys.exit(f"Ahrefs API {e.code} on {path}: {e.read().decode('utf-8', 'replace')[:500]}")

def head_status(url):
    """Status of a HEAD request without following redirects; falls back to GET for servers that reject HEAD."""
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k): return None
    opener = urllib.request.build_opener(NoRedirect)
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
            with opener.open(req, timeout=15) as r: return r.status
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 501): continue
            return e.code
        except Exception as e:
            return f"error: {type(e).__name__}"
    return None

def norm_host(h): return re.sub(r"^www\.", "", (h or "").lower())

def classify(row, site_host):
    """Return ("swap", note) or ("skip", reason) for one page-explorer row."""
    url = row["url"]; final = row.get("final_redirect") or row.get("redirect") or ""
    u = urllib.parse.urlsplit(url); f = urllib.parse.urlsplit(final)
    path = u.path or "/"
    if not final:
        return "skip", "Ahrefs reports no redirect target"
    if re.search(r"[\\\"'<>\s]", u.path + (f.path or "")):
        return "skip", "path contains a backslash, quote, space or angle bracket; a typo in a link that cannot be matched safely. Fix that link by hand (APPROVE)"
    if norm_host(f.netloc) != site_host:
        return "skip", f"redirects off-site to {f.netloc}; usually intentional, leave"
    if u.query:
        return "skip", "URL has a query string; parameter redirects are handled by the app, not content links"
    if re.search(r"/page/1/?$", path):
        return "skip", "pagination /page/1/ comes from the theme template, not content; fix in the template"
    if re.match(r"^/author/", path):
        return "skip", "author archive; disable author archives or the author sitemap in the SEO plugin"
    if re.search(r"%20|\s|_files/", url):
        return "skip", "looks like a pasted file path (one post's broken image); fix the post by hand (APPROVE)"
    if norm_host(u.netloc) == site_host and (u.scheme == "http" or u.netloc.lower().startswith("www.")) and (f.path or "/") == path:
        return "skip", "http:// or www. host variant; expected canonical redirect"
    if (f.path or "/") == "/" and not f.query:
        if re.match(r"^/\d{4}/\d{2}(/\d{2})?/?$", path):
            return "skip", "date archive redirecting to the homepage; not a content link"
        return "skip", "redirects to homepage; needs a real target or removal (APPROVE)"
    if row.get("final_redirect_code") not in (200, None):
        return "skip", f"final target returns {row.get('final_redirect_code')}, not 200; fix the redirect rule first (APPROVE)"
    if row.get("incoming_all_links", 1) == 0:
        return "skip", "no incoming internal links (sitemap or orphan entry); nothing in content to rewrite"
    notes = []
    if (row.get("nr_redirect_chain_urls") or 1) > 1: notes.append(f"{row['nr_redirect_chain_urls']}-hop chain collapsed to its final page")
    if (f.path or "/") == path + "/": notes.append("missing trailing slash")
    if path.rstrip("/") and (f.path or "/").rstrip("/") and path.startswith((f.path or "/").rstrip("/") + "/") and len(f.path.rstrip("/").split("/")) < len(path.rstrip("/").split("/")):
        notes.append("redirects up to its parent page; check the parent covers the old content")
    return "swap", "; ".join(notes)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--no-verify", action="store_true", help="skip the HEAD check of each swap target")
    ap.add_argument("--print", action="store_true", dest="dump")
    args = ap.parse_args()
    load_env()

    client = yaml.safe_load((ROOT / "clients" / f"{args.slug}.yaml").read_text(encoding="utf-8"))
    pid = (client.get("ahrefs") or {}).get("site_audit_project_id")
    if not pid or str(pid) == "unknown": sys.exit(f"clients/{args.slug}.yaml has no ahrefs.site_audit_project_id")
    site_host = norm_host(client["domain"])
    home = (client.get("canonical_host") or f"https://{client['domain']}").rstrip("/")

    proj = ahrefs("site-audit/projects", project_id=pid)
    hs = (proj.get("healthscores") or [{}])[0]
    crawl_date = (hs.get("date") or "")[:10] or datetime.date.today().isoformat()
    if hs.get("status") not in (None, "Completed"):
        print(f"Note: latest crawl status is {hs.get('status')}; data is from the last completed crawl.")

    issues = ahrefs("site-audit/issues", project_id=pid).get("issues", [])
    issue = next((i for i in issues if i["name"] == ISSUE_NAME), None)
    if not issue: sys.exit(f"Issue '{ISSUE_NAME}' not found for project {pid}")

    rows, offset = [], 0
    while True:
        page = ahrefs("site-audit/page-explorer", project_id=pid, issue_id=issue["issue_id"], select=SELECT,
                      order_by="incoming_all_links:desc", limit=1000, offset=offset).get("pages", [])
        rows += page
        if len(page) < 1000: break
        offset += 1000

    swaps, skipped, verify_fail = [], [], 0
    for r in rows:
        kind, note = classify(r, site_host)
        if kind == "skip":
            skipped.append({"old": r["url"], "reason": note, "links": r.get("incoming_all_links")}); continue
        new = r["final_redirect"]
        if not args.no_verify:
            st = head_status(new)
            if st in (403, 405, 429, 503) and r.get("final_redirect_code") == 200:
                # A firewall or bot filter answered the script, not the page. Ahrefs saw 200 from the target; trust that.
                note = (note + "; " if note else "") + f"verify got {st} (bot protection); trusting Ahrefs' 200"
            elif st != 200:
                verify_fail += 1
                skipped.append({"old": r["url"], "reason": f"target {new} returned {st} on verify, expected 200; check the redirect rule (APPROVE)", "links": r.get("incoming_all_links")}); continue
        s = {"old": r["url"], "new": new, "links": r.get("incoming_all_links")}
        if note: s["note"] = note
        swaps.append(s)

    # Longest old path first so the anchored matcher sees the most specific rule first (it is anchored anyway; this is belt and braces).
    swaps.sort(key=lambda s: (-len(urllib.parse.urlsplit(s["old"]).path), s["old"]))

    outdir = ROOT / "reports" / args.slug; outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / f"redirect-map-{crawl_date}.json"
    legacy, prev_notes = [], None
    if out.exists():
        try:
            prev = json.loads(out.read_text(encoding="utf-8")); legacy = prev.get("legacy_hosts") or []; prev_notes = prev.get("notes")
        except Exception: pass
    m = {"site": client["domain"], "source": f"Ahrefs Site Audit project {pid}, crawl {crawl_date}, issue '{ISSUE_NAME}' via build_redirect_map.py",
         "generated": datetime.date.today().isoformat(), "verified": not args.no_verify,
         "counts": {"rows": len(rows), "swaps": len(swaps), "skipped": len(skipped), "verify_failed": verify_fail},
         "swaps": swaps, "skipped": skipped, "legacy_hosts": legacy}
    if prev_notes: m["notes"] = prev_notes
    out.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    sitewide = [s for s in swaps if (s.get("links") or 0) >= max(20, 0.8 * (hs.get("total") or 0))]
    print(f"{client['domain']}: crawl {crawl_date}, {len(rows)} redirecting URLs -> {len(swaps)} swaps, {len(skipped)} skipped" + (f" ({verify_fail} failed verify)" if verify_fail else ""))
    if sitewide: print(f"  {len(sitewide)} swap(s) are linked from nearly every page (menu/footer/template): " + ", ".join(urllib.parse.urlsplit(s['old']).path for s in sitewide[:5]))
    by = {}
    for s in skipped: by[s["reason"].split(";")[0]] = by.get(s["reason"].split(";")[0], 0) + 1
    for k, v in sorted(by.items(), key=lambda kv: -kv[1]): print(f"  skip {v:3}  {k}")
    print(f"Map: {out}")
    if args.dump: print(json.dumps(m, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
