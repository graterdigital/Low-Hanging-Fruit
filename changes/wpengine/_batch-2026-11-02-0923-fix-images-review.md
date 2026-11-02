# fix-images review batch: wpengine

Run 2026-11-02-0923 · 21 sites · pngquant on this machine: yes

Nothing was pushed to any site. For each site marked *ready for visual check*: open `backup/.../new/` next to `orig/` at 100% (headshots and gradients first), then apply per site with `python scripts/fix_images.py <slug> --apply`, then live. Alt sheets go to Google Sheets for review, then `merge_alt_sheet.py` and `--alt-apply`.

| site | status | flagged | before MB | after MB | PNGs skipped | alt rows (A/C/B) | note |
|---|---|---|---|---|---|---|---|
| 22plasticsurgery | nothing to compress | 0 | - | - | - | written | sheet pushed |
| 22spamd | probe failed | - | - | - | - | - | Error: There has been a critical error on this website.Learn more about troubleshooting WordPress. There has been a critical error on this website. |
| aveluremedspa | nothing to compress | 0 | - | - | - | written | sheet pushed |
| blushmedspact | probe failed | - | - | - | - | - | Error: There has been a critical error on this website.Learn more about troubleshooting WordPress. There has been a critical error on this website. |
| curatemedspa | probe failed | - | - | - | - | - | Error: There has been a critical error on this website.Learn more about troubleshooting WordPress. There has been a critical error on this website. |
| dermguy | needs staging | - | - | - | - | - |  |
| destinationaesthetics | dry run failed | 1 | - | - | - | written | Could not resolve uploads dir on destinationaesthetics-staging: sheet pushed |
| esthetixmd | probe failed | - | - | - | - | - | thrown in /nas/content/live/esthetixmdstg/wp-content/plugins/wordpress-seo/src/main.php on line 25 |
| everbody | probe failed | - | - | - | - | - | thrown in /nas/content/live/everbodyprostg/wp-content/object-cache.php on line 638 |
| glomedspa | needs staging | - | - | - | - | - |  |
| h-md | dry run failed | 10 | - | - | - | written | Could not resolve uploads dir on h-md-staging: sheet pushed |
| legalatlanta | needs staging | - | - | - | - | - |  |
| livingyoungcenter | nothing to compress | 0 | - | - | - | written | sheet pushed |
| newradiancenow | nothing to compress | 0 | - | - | - | written | sheet pushed |
| nouveauspa | dry run failed | 5 | - | - | - | written | Could not resolve uploads dir on nouveauspa-staging: sheet pushed |
| purskinclinic | needs staging | - | - | - | - | - |  |
| reflectionscenter | dry run failed | 1 | - | - | - | written | Could not resolve uploads dir on reflectionscenter-staging: sheet pushed |
| skynbaratlanta | probe failed | - | - | - | - | - | Error: There has been a critical error on this website.Learn more about troubleshooting WordPress. There has been a critical error on this website. |
| synergymedaesthetics | probe failed | - | - | - | - | - | Error: There has been a critical error on this website.Learn more about troubleshooting WordPress. There has been a critical error on this website. |
| theagelesscenter | nothing to compress | 0 | - | - | - | written | sheet pushed |
| theclinique | probe failed | - | - | - | - | - | Fatal error: Cannot redeclare pmae_admin_notices() (previously declared in /nas/content/live/aesthclinnestg/wp-content/plugins/wp-all-export-csv-excel-xml-for-acf/actions/admin_notices.php:4) in /nas/ |

## Paths

**22plasticsurgery**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\22plasticsurgery\images-2026-10-29.md`



**aveluremedspa**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\aveluremedspa\images-2026-10-29.md`



**destinationaesthetics**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\destinationaesthetics\images-2026-10-29.md`



**h-md**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\h-md\images-2026-10-29.md`



**livingyoungcenter**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\livingyoungcenter\images-2026-10-29.md`



**newradiancenow**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\newradiancenow\images-2026-10-29.md`



**nouveauspa**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\nouveauspa\images-2026-10-29.md`



**reflectionscenter**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\reflectionscenter\images-2026-10-29.md`



**theagelesscenter**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\theagelesscenter\images-2026-10-29.md`



