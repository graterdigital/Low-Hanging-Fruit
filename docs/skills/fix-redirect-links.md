# Handoff: fix-redirect-links

Status as of 2026-10-29. Mirror of the project doc `claude/skill-fix-redirect-links.md`; update both.

## What the skill does

Rewrites internal links that point at redirecting URLs so they point straight at the final page. AUTO tier (changes nothing a visitor reads), but always dry-run on staging first. It does not create or edit redirect rules.

## Where it lives

- `skills/fix-redirect-links/SKILL.md`: the procedure.
- `scripts/fix_redirect_links.py`: local runner. Flags: `--probe`, default dry run, `--apply`, `--target live`.
- `scripts/php/replace_links.php`: runs inside WordPress via `wp eval-file -`. Anchored matching; absolute, relative, JSON-escaped and serialized forms; live, current and legacy hosts.
- `reports/<slug>/redirect-map-<crawl-date>.json`: per-site input (`swaps`, `skipped`, `legacy_hosts`).
- `changes/<slug>/`: change logs per run; `backup/` holds full before/after (git-ignored).

## Pilot: hsfamilylaw.com

- 9 swaps + 1 legacy host (`hswlaw.wpengine.com`). Skipped: 5 homepage redirects, `/podcast/`, `/page/1/` (template), author archives (Yoast), host variants.
- Staging 2026-10-29: dry run and apply both 8 posts, 55 postmeta rows, 79 replacements, no errors. Spot-checked good.
- Live: pending. `python scripts\fix_redirect_links.py hsfamilylaw --map reports\hsfamilylaw\redirect-map-2026-10-08.json --target live --apply`, then commit `changes/`.
- Verify: Ahrefs recrawl; "Page has links to redirect" should fall from 39 to about 24 (the paginated archives, a template fix).

## Learned the hard way

1. Kinsta staging rewrites absolute URLs to the staging domain.
2. ACF Pro + classic editor: links live in postmeta, often serialized.
3. `wp eval-file` runs the file inside a function; declare shared state `global`.
4. PHP's empty array is a JSON list.
5. Rebuilt staging = new host key on the same port (`ssh-keygen -R "[ip]:port"`).
6. Probe first on every new site.

## Open items

- Live run + recrawl on hsfamilylaw.
- Test on a WP Engine site and on an Elementor site.
- Bulk restore script from backup JSON.
- Let the skill build the redirect map from Ahrefs itself.
