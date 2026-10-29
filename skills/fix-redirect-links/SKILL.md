---
name: fix-redirect-links
description: Rewrite a WordPress site's internal links that point at redirecting URLs so they point straight at the final page, with a dry run, a change log, and rollback. Use this whenever a triage report or Ahrefs lists "Page has links to redirect", "3XX redirect", or "Redirect chain" for a client site, or the user asks to clean up, fix, or update old or redirecting internal links. AUTO tier: safe to apply without copy review, but always run on staging first.
---

# fix-redirect-links

Internal links that go through a redirect waste a hop on every click and crawl, and the old URLs tend to break when someone later deletes the redirect rule. The fix is to point each link at the page it ends up on anyway. Nothing a visitor reads changes, which is why this is the AUTO tier and the first fix to run on a new site.

## What you need

1. A client file `clients/<slug>.yaml` with `hosting.ssh_alias` (live) and `hosting.staging_environment` (staging) filled in. If they say `unknown`, run `scripts/ssh_config_sync.py` first or ask for the aliases.
2. A redirect map: `reports/<slug>/redirect-map-<crawl-date>.json`. If there isn't one, build it (next section).
3. A staging environment that is a recent copy of live. If the user hasn't refreshed it, say so before running; a stale staging proves little.

## Building the redirect map

Pull the "3XX redirect" issue for the Ahrefs Site Audit project with `site-audit-page-explorer`, `select: url,http_code,redirect,redirect_code,final_redirect,final_redirect_code,incoming_all_links,nr_redirect_chain_urls`. The `final_redirect` column is the destination after following any chain. Then sort every row into **swaps** or **skipped**:

Swap when the final URL is on the same site, returns 200, and is a specific page. Use `final_redirect` as `new`, never the first hop, so chains collapse in one step.

Skip, with the reason written into the map, when:
- the final URL is the homepage. Someone picked "send it home" because the page was deleted; the link needs a real target or removal, which is a human decision (APPROVE).
- the final URL is on another domain. Usually intentional.
- the old URL is `.../page/1/`. That comes from the theme's pagination template, not content. Fixing it in content would be undone on the next render.
- the old URL is an author archive or similar sitemap entry with zero incoming links. Fix the SEO plugin setting instead.
- it's an `http://` or `www.` variant of the site itself. Those redirects are supposed to exist.
- the old URL looks like a pasted file path (spaces, `%20`, `_files/`). A broken image on one post; fix by hand.

Save the map as JSON with `site`, `source`, `generated`, `swaps` (`old`, `new`, optional `note`), `skipped` (`old` or `pattern`, `reason`) and, when the probe finds them, `legacy_hosts`: old hostnames (a previous host's URL, an old domain) still linked from content. Links on a legacy host are moved to the current host with the same path. The skipped list goes into the change log so nobody wonders why those links were left alone.

## Running it

Everything happens through `scripts/fix_redirect_links.py`, which ships `scripts/php/replace_links.php` to the site over SSH and runs it inside WordPress with `wp eval-file`. The PHP does anchored matching: a URL is replaced only when it is a complete link target (between quotes or parentheses), so `/child-support/` never matches inside `/divorce/child-support/`, and `/contact-us` never matches `/contact-us/`. Absolute and root-relative links are both handled; relative links stay relative.

Staging copies run on their own domain and the host rewrites every absolute link to it, so the matcher accepts the live domain, whatever host the install currently runs on, and the legacy hosts, and a rewritten link keeps the host it had. Serialized postmeta (ACF link and URL fields, WYSIWYG fields inside repeaters) is unserialized, walked, rewritten, and reserialized.

Logs land in `changes/<provider>/<slug>/` (provider from the client file: `kinsta`, `wpengine`, `other`). Every run writes two files: the change log, and a companion `-options.md` listing any `wp_options` rows that still contain an old URL. Options are never edited; that list is for a human. Widgets, theme mods, Customizer settings, and plugin configs live there, and a swap that shows zero hits in posts and meta but turns up in the options log is a link to fix by hand.

Run in this order, and stop at any step that looks wrong. Start with `--probe` on a new site: it lists where each old URL actually appears and reveals legacy hosts and storage forms (ACF fields, builder data) the dry run would otherwise miss.

```
python scripts/fix_redirect_links.py <slug> --map reports/<slug>/redirect-map-<date>.json
```
Dry run on staging. Prints how many posts and meta rows would change, per-URL totals, and how many options rows reference old URLs, and writes `changes/<provider>/<slug>/<stamp>-fix-redirect-links-staging-dry.md` plus the `-options.md` companion. Read both. Sanity checks: the post count should be in the same ballpark as Ahrefs' "Page has links to redirect" count for non-template pages (template-driven pages like paginated archives won't appear, which is expected); every swap in the map should have hits somewhere, and a swap with no hits in posts, meta, or options means the link lives in a theme file or a builder blob the script doesn't read.

```
python scripts/fix_redirect_links.py <slug> --map ... --apply
```
Apply on staging. WordPress keeps a revision of each changed post, the full before/after of everything is saved to `changes/<provider>/<slug>/backup/` (git-ignored, since it's client content), and the script runs `wp cache flush` afterwards because postmeta is written straight to the table and a persistent object cache would otherwise keep serving the old values. Then open two or three of the changed pages on staging and click the fixed links.

```
python scripts/fix_redirect_links.py <slug> --map ... --target live --apply
```
Apply on live. The script asks you to type the slug to confirm; `--yes` skips that for vetted, unattended runs, and a run with neither a terminal nor `--yes` aborts rather than hanging. Same logs, backup, and cache flush.

Then commit the `changes/<provider>/<slug>/*.md` logs (not the backup folder).

## After

- Ask the user to trigger a recrawl in Ahrefs, or wait for the scheduled one. The "Page has links to redirect" count should drop by roughly the number of posts changed; what's left is template-driven and belongs to the template fix.
- Hand back the skipped list as a short to-do: the homepage-redirect URLs each need a decision.
- Hand over the `-options.md` log too: each row is a widget, menu, theme setting, or plugin option still carrying an old link, to be fixed in wp-admin by hand.
- Page builders: WPBakery shortcodes live in `post_content` and are handled. Elementor keeps its layout as a JSON string in `_elementor_data` postmeta; the JSON-escaped matching should cover it but has not been exercised on a real Elementor site yet, so on the first one, probe, dry-run, and inspect the diff in the backup before applying.

## Rollback

Per post: Posts → edit → Revisions → restore the one before the run. In bulk: the backup JSON has `before` content for every changed post and meta row; `wp post update <id> --post_content=<file>` restores one, or ask for a restore script. Never rerun the fix "in reverse" by swapping new for old; the anchored matching makes that unsafe.

## Scope and limits

- WordPress only, over SSH with WP-CLI. Kinsta's web root is `public`; WP Engine's is `sites/<install>` (the script picks that from `hosting.provider`).
- Touches `post_content` of all non-revision posts and postmeta values, plain or serialized. Reads `wp_options` for the companion report but never writes it. Does not touch theme files or anything outside the database.
- Does not create, edit, or delete redirect rules. Chains are handled by pointing links at the final URL; the rule cleanup in Redirection (or whatever plugin holds the rules) is a separate, APPROVE-tier step.
