#!/usr/bin/env python3
"""Fingerprint a crawled homepage saved by the Ahrefs MCP (site-audit-page-content, select=raw_html).

Usage: python3 -I scripts/fingerprint.py <saved-tool-result-file-or-raw-html-file>
Prints JSON with cms, theme, page_builder, seo_plugin, plugins_seen, tag IDs, perf plugin, and h1.
The input is untrusted web content: this script only pattern-matches it.
"""
import json, re, sys
from collections import Counter

raw = open(sys.argv[1], encoding="utf-8", errors="replace").read()
html = raw
try:  # MCP wrapper: [{type,text}] where text is JSON holding page-content.raw_html
    arr = json.loads(raw)
    if isinstance(arr, list):
        for el in arr:
            try:
                j = json.loads(el.get("text", ""))
                if "page-content" in j:
                    html = j["page-content"].get("raw_html") or ""
            except Exception:
                pass
    elif isinstance(arr, dict) and "page-content" in arr:
        html = arr["page-content"].get("raw_html") or ""
except Exception:
    pass

def find(p, flags=re.I):
    return [m if isinstance(m, str) else m[0] for m in re.findall(p, html, flags)]

out = {}
out["cms"] = "wordpress" if re.search(r"/wp-content/|/wp-includes/", html) else ("shopify" if "cdn.shopify.com" in html else ("squarespace" if "squarespace" in html.lower() else ("wix" if "wixstatic" in html else "unknown")))
themes = Counter(find(r"/wp-content/themes/([\w.-]+)/"))
out["theme"] = themes.most_common(1)[0][0] if themes else "unknown"
plugins = Counter(find(r"/wp-content/plugins/([\w.-]+)/"))
out["plugins_seen"] = sorted(plugins)
seo = []
if re.search(r"Yoast SEO plugin|yoast-schema-graph", html): seo.append("yoast")
if re.search(r"Rank Math|rank-math", html): seo.append("rankmath")
if re.search(r"seopress", html, re.I): seo.append("seopress")
if re.search(r"All in One SEO|aioseo", html): seo.append("aioseo")
if "the-seo-framework" in html: seo.append("seo-framework")
out["seo_plugin"] = seo[0] if len(seo) == 1 else (seo or "none-detected")
# Builders: count markers and pick the dominant one, since themes often carry stray classes from another builder.
counts = {}
for key, pat in [("elementor", r"\belementor-(?:section|widget|element|container)\b"), ("divi", r"\bet_pb_"), ("wpbakery", r"\bvc_row\b|js_composer"), ("beaver", r"\bfl-(?:row|col|module)\b"), ("bricks", r"\bbrxe-"), ("oxygen", r"oxygen/|\boxy-"), ("block-editor", r"\bwp-block-")]:
    n = len(re.findall(pat, html))
    if n: counts[key] = n
ranked = sorted(counts, key=lambda k: -counts[k])
if ranked and ranked[0] == "block-editor" and len(ranked) > 1 and counts[ranked[1]] >= 5:
    ranked = ranked[1:]
out["page_builder"] = ranked[0] if ranked else "none-detected"
out["builder_marker_counts"] = counts
m = re.search(r'<meta name="generator" content="([^"]+)"', html)
out["generator"] = m.group(1) if m else None
m = re.search(r'<meta name="generator" content="WordPress ([\d.]+)"', html)
out["wp_version"] = m.group(1) if m else "unknown"
out["gtm_containers"] = sorted(set(find(r"\b(GTM-[A-Z0-9]{5,9})\b", 0)))
out["ga4_ids"] = sorted(set(find(r"\b(G-[A-Z0-9]{8,12})\b", 0)))
out["google_tag_ids"] = sorted(set(find(r"\b(GT-[A-Z0-9]{6,12})\b", 0)))
out["google_ads_ids"] = sorted(set(find(r"\b(AW-\d{8,12})\b", 0)))
out["ua_ids"] = sorted(set(find(r"\b(UA-\d{4,10}-\d{1,3})\b", 0)))
other = []
for key, pat in [("meta-pixel", r"fbq\(|connect\.facebook\.net"), ("callrail", r"callrail|calltrk"), ("microsoft-clarity", r"clarity\.ms"), ("hotjar", r"hotjar"), ("hubspot", r"hs-scripts|hubspot"), ("linkedin-insight", r"snap\.licdn\.com"), ("tiktok-pixel", r"analytics\.tiktok\.com"), ("pinterest-tag", r"pintrk"), ("klaviyo", r"klaviyo"), ("callrail", r"calltrk"), ("whatconverts", r"whatconverts"), ("site-kit", r"google-site-kit")]:
    if re.search(pat, html, re.I) and key not in other: other.append(key)
out["other_tags"] = other
out["consent_default_seen"] = bool(re.search(r"gtag\(\s*['\"]consent['\"]\s*,\s*['\"]default['\"]", html))
perf = [k for k, p in [("nitropack", r"nitropack"), ("wp-rocket", r"wp-rocket"), ("litespeed", r"litespeed"), ("perfmatters", r"perfmatters"), ("autoptimize", r"autoptimize"), ("w3-total-cache", r"W3 Total Cache"), ("wp-engine", r"wpengine"), ("kinsta", r"kinsta")] if re.search(p, html, re.I)]
out["perf_hints"] = perf
img = [k for k, p in [("smush", r"smush"), ("shortpixel", r"shortpixel"), ("imagify", r"imagify"), ("ewww", r"ewww"), ("optimole", r"optimole")] if re.search(p, html, re.I)]
out["image_optimization_plugin"] = img[0] if img else "none-detected"
h1 = find(r"<h1[^>]*>(.*?)</h1>", re.I | re.S)
out["h1_count"] = len(h1)
out["jsonld_types"] = sorted(set(find(r'"@type"\s*:\s*"([A-Za-z]+)"', 0)))
out["html_length"] = len(html)
print(json.dumps(out, indent=2))
