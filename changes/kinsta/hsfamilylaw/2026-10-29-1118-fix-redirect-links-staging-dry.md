# fix-redirect-links: hsfamilylaw.com (staging)

Run 2026-10-29-1118 · mode **dry** · alias `hsfamilylaw-staging` · provider `kinsta` · map `redirect-map-2026-10-08.json`

Install host `stg-hastingsshadmehry-hsfamilystg.kinsta.cloud`; hosts matched: `hsfamilylaw.com`, `stg-hastingsshadmehry-hsfamilystg.kinsta.cloud`, `hswlaw.wpengine.com`. Entries starting `host:` are legacy-host links moved to the current host.

## Totals (replacements per old URL)


## Posts changed (0)

| ID | type | title | URL | replacements | applied |
|---|---|---|---|---|---|

## Postmeta changed (0)

| meta_id | post | key | kind | replacements | applied |
|---|---|---|---|---|---|

## Skipped by the map

- https://hsfamilylaw.com/collaborative-divorce-attorney/basics-collaborative-approach/: redirects to homepage; needs a real target (APPROVE)
- https://hsfamilylaw.com/family-law/alimony-modification/: redirects to homepage; needs a real target (APPROVE)
- https://hsfamilylaw.com/modifications/: redirects to homepage; needs a real target (APPROVE)
- https://hsfamilylaw.com/mediation/mediation-faqs/: redirects to homepage; needs a real target (APPROVE)
- https://hsfamilylaw.com/understanding-roles-collaborative-divorce-team/Collaborative%20Divorce%20Team%20Hastings%20Shadmehry: broken image path on one post; fix the post by hand (APPROVE)
- https://hsfamilylaw.com/podcast/: redirects off-site to forwardfacing.com; intentional, leave
- */page/1/: theme pagination template emits /page/1/; fix in the template, not in content
- /author/*: in the Yoast author sitemap, not in content; disable author archives in Yoast
- http:// and www. host variants: expected canonical redirects

## wp_options still referencing old URLs (1, not changed)

See `2026-10-29-1118-fix-redirect-links-staging-options.md` next to this log. Widgets, theme mods, menus and plugin settings live here and need a hand or a different skill.

## Rollback

Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.
Postmeta: previous values are in the same backup file.
