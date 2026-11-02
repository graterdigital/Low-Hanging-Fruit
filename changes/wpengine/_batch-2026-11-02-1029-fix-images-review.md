# fix-images review batch: wpengine

Run 2026-11-02-1029 · 21 sites · pngquant on this machine: yes

Nothing was pushed to any site. For each site marked *ready for visual check*: open `backup/.../new/` next to `orig/` at 100% (headshots and gradients first), then apply per site with `python scripts/fix_images.py <slug> --apply`, then live. Alt sheets go to Google Sheets for review, then `merge_alt_sheet.py` and `--alt-apply`.

| site | status | flagged | before MB | after MB | PNGs skipped | alt rows (A/C/B) | note |
|---|---|---|---|---|---|---|---|
| 22plasticsurgery | nothing to compress | 0 | - | - | - | written | sheet pushed |
| 22spamd | probe failed | - | - | - | - | - | urllib.error.URLError: <urlopen error _ssl.c:993: The handshake operation timed out> |
| aveluremedspa | nothing to compress | 0 | - | - | - | written | sheet pushed |
| blushmedspact | nothing to compress | 0 | - | - | - | written | sheet pushed |
| curatemedspa | nothing to compress | 0 | - | - | - | written | sheet pushed |
| dermguy | needs staging | - | - | - | - | - |  |
| destinationaesthetics | dry run failed | 1 | - | - | - | written | Could not resolve uploads dir on destinationaesthetics-staging: sheet pushed |
| esthetixmd | nothing to compress | 0 | - | - | - | written | sheet pushed |
| everbody | nothing to compress | 0 | - | - | - | written | sheet pushed |
| glomedspa | needs staging | - | - | - | - | - |  |
| h-md | dry run failed | 10 | - | - | - | written | Could not resolve uploads dir on h-md-staging: sheet pushed |
| legalatlanta | needs staging | - | - | - | - | - |  |
| livingyoungcenter | nothing to compress | 0 | - | - | - | written | sheet pushed |
| newradiancenow | nothing to compress | 0 | - | - | - | written | sheet pushed |
| nouveauspa | dry run failed | 5 | - | - | - | written | Could not resolve uploads dir on nouveauspa-staging: sheet pushed |
| purskinclinic | needs staging | - | - | - | - | - |  |
| reflectionscenter | dry run failed | 1 | - | - | - | written | Could not resolve uploads dir on reflectionscenter-staging: sheet pushed |
| skynbaratlanta | dry run failed | 1 | - | - | - | written | Could not resolve uploads dir on skynbaratlanta-staging: sheet pushed |
| synergymedaesthetics | nothing to compress | 0 | - | - | - | written | sheet pushed |
| theagelesscenter | nothing to compress | 0 | - | - | - | written | sheet pushed |
| theclinique | nothing to compress | 0 | - | - | - | written | sheet pushed |

## Paths

**22plasticsurgery**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\22plasticsurgery\images-2026-10-29.md`



**aveluremedspa**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\aveluremedspa\images-2026-10-29.md`



**blushmedspact**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\blushmedspact\images-2026-10-29.md`



**curatemedspa**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\curatemedspa\images-2026-10-29.md`



**destinationaesthetics**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\destinationaesthetics\images-2026-10-29.md`



**esthetixmd**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\esthetixmd\images-2026-10-29.md`



**everbody**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\everbody\images-2026-10-29.md`



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



**skynbaratlanta**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\skynbaratlanta\images-2026-10-29.md`



**synergymedaesthetics**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\synergymedaesthetics\images-2026-10-29.md`



**theagelesscenter**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\theagelesscenter\images-2026-10-29.md`



**theclinique**
- probe report: `C:\Users\greg\Documents\Low-Hanging-Fruit\reports\theclinique\images-2026-10-29.md`



