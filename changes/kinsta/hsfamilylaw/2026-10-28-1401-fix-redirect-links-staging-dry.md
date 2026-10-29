# fix-redirect-links: hsfamilylaw.com (staging)

Run 2026-10-28-1401 · mode **dry** · alias `hsfamilylaw-staging` · map `redirect-map-2026-10-08.json`

## Totals (replacements per old URL)

- `https://hsfamilylaw.com/collaborative-divorce-attorney/` → 2
- `https://hsfamilylaw.com/collaborative-divorce-attorney/the-process/` → 2
- `https://hsfamilylaw.com/contact-us` → 1
- `https://hsfamilylaw.com/divorce/divorce-process/` → 1
- `https://hsfamilylaw.com/mediation/mediate/` → 1

## Posts changed (7)

| ID | type | title | URL | replacements | applied |
|---|---|---|---|---|---|
| 2244 | post | What are the Benefits of a Collaborative Divorce? | https://stg-hastingsshadmehry-hsfamilystg.kinsta.cloud/alpharetta-collaborative-divorce/ | 1 | - |
| 2477 | post | The Difference Between Collaboration and Mediation | https://stg-hastingsshadmehry-hsfamilystg.kinsta.cloud/difference-collaboration-mediation-attorneys/ | 1 | - |
| 2492 | post | Choosing a Judge or a Mediation Attorney for Divor | https://stg-hastingsshadmehry-hsfamilystg.kinsta.cloud/whether-choose-judge-mediation-attorney-divorce/ | 1 | - |
| 2551 | post | How Long Does it Take to Get Divorce in Georgia? | https://stg-hastingsshadmehry-hsfamilystg.kinsta.cloud/long-take-get-divorce-georgia/ | 1 | - |
| 2619 | post | Understanding the Roles of the Collaborative Divor | https://stg-hastingsshadmehry-hsfamilystg.kinsta.cloud/understanding-roles-collaborative-divorce-team/ | 1 | - |
| 2633 | post | How Collaborative Divorce Helps Children Cope | https://stg-hastingsshadmehry-hsfamilystg.kinsta.cloud/how-collaborative-divorce-helps-children-cope/ | 1 | - |
| 2660 | post | Avoiding Disputes in Family Law Matters | https://stg-hastingsshadmehry-hsfamilystg.kinsta.cloud/avoiding-disputes-in-family-law-matters/ | 1 | - |

## Postmeta changed (0)

| meta_id | post | key | replacements | note |
|---|---|---|---|---|

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

## Rollback

Posts: WordPress kept a revision of each changed post (Posts → edit → Revisions), and the exact before/after content is in `backup/` next to this log.
Postmeta: previous values are in the same backup file.
