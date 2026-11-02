# AI discoverability: ruggeddepot.com

Ahrefs Site Audit project 9704549 · crawl 2026-11-02 · health 96 · 40 indexable pages sampled (top by traffic) · robots.txt source: `https://ruggeddepot.com/robots.txt` (HTTP 403)

Mostly read-and-route. The only direct change this skill makes is the robots.txt policy block (APPROVE, after the client decides). Google's position, which this report follows: AI Overviews and AI Mode use Googlebot and need pages that are indexed and snippet-eligible; `Google-Extended` governs Gemini training and grounding, not Search; no AI-specific files or markup are needed.

## 1. Bot access (robots.txt)

Client policy in `clients/ruggeddepot.yaml`: search bots **allow**, training bots **allow** (decided by Grater Digital default, Greg 2026-10-30; per-client opt-out on request).

| Bot | Class | Live (sampled pages) | Policy says | Action |
|---|---|---|---|---|
| Amazonbot | search | allowed | allow | none |
| Amzn-SearchBot | search | allowed | allow | none |
| Amzn-User | search | allowed | allow | none |
| Applebot | search | allowed | allow | none |
| ChatGPT-User | search | allowed | allow | none |
| Claude-SearchBot | search | allowed | allow | none |
| Claude-User | search | allowed | allow | none |
| Claude-Web | search | allowed | allow | none |
| DuckAssistBot | search | allowed | allow | none |
| GitHubCopilotChat | search | allowed | allow | none |
| Google-Agent | search | allowed | allow | none |
| Googlebot | search | allowed | allow | none |
| MistralAI-User | search | allowed | allow | none |
| OAI-SearchBot | search | allowed | allow | none |
| Perplexity-User | search | allowed | allow | none |
| PerplexityBot | search | allowed | allow | none |
| YouBot | search | allowed | allow | none |
| Applebot-Extended | training | allowed | allow | none |
| ClaudeBot | training | allowed | allow | none |
| DeepseekBot | training | allowed | allow | none |
| GPTBot | training | allowed | allow | none |
| Google-Extended | training | allowed | allow | none |
| Meta-ExternalAgent | training | allowed | allow | none |
| anthropic-ai | training | allowed | allow | none |
| xAI-Bot | training | allowed | allow | none |

robots.txt errors reported by Ahrefs: none · Sitemap lines: none · X-Robots-Tag headers on sampled pages: none

Current robots.txt:

```
(empty or not fetched)
```

Live robots.txt already matches the client policy. Nothing to change.

## 2. Checks with pages behind them

### Article page missing Article schema (39, Notice) → schema-check · FLAG

Ahrefs' ML classed the page as an article; Yoast emits Article only for posts.

Shape of the 39 sampled: 0 paginated (`/page/N/`), 11 with any traffic (51 total), TTFB median 874 ms / max 1274 ms.

| URL | traffic | JSON-LD types on page | Ahrefs page type |
|---|---|---|---|
| `/cradlepoint-r1900-review/` | 11 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Comparisons |
| `/ultimate-rugged-laptop-buying-guide/` | 10 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/what-is-cradlepoint-netcloud/` | 9 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/firstnet-frontline-t-priority-setup/` | 7 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Comparisons |
| `/government-laptops-buying-guide/` | 6 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/what-is-a-cradlepoint-router/` | 3 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/field-service-laptops-tablets/` | 1 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/police-laptops-buying-guide/` | 1 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/military-laptops-buying-guide/` | 1 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/what-is-a-mobile-data-terminal/` | 1 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/laptops-for-automotive-tuning/` | 1 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/fire-ems-laptops-old/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/fully-vs-semi-rugged-laptops-explained/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Comparisons |
| `/panasonic-toughbook-docking-station-guide/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/4x4-mimo-antenna-vehicle-router/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/ip-ratings-explained/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/public-safety-distributed-antenna-systems/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/in-vehicle-connectivity-public-safety-vehicles/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/best-rugged-laptops-2026/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Roundup |
| `/mil-std-810h-explained/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/marine-boat-diagnostics/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Roundup |
| `/diesel-truck-diagnostics/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/vehicle-wifi-public-safety/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Comparisons |
| `/diagnostics-for-agricultural-equipment/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/public-safety-network-vehicle-architecture/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/fleet-connectivity-public-safety-vehicles/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/rugged-tablet-buying-guide/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/5g-mobile-router-public-safety-vehicles/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/firstnet-public-safety-carriers/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Comparisons |
| `/repair-warranty-triage/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/vehicle-cellular-failover/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/police-mobile-data-terminals/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/what-is-a-mimo-antenna/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/vehicle-laptop-mounts-for-cars-and-trucks/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/getac-ultimate-guide-2026/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/panasonics-ultimate-care-warranty/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/panasonic-toughbook-models/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/rugged-testing/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |
| `/fire-ems/` | 0 | BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Article/Tutorial_or_Guide |

### Category page missing ItemList schema (996, Notice) → schema-check · FLAG

Archive/listing page without ItemList.

Shape of the 200 sampled: 156 paginated (`/page/N/`), 21 with any traffic (501 total), TTFB median 1378 ms / max 6178 ms (of 996 flagged; sample is the top by traffic).

| URL | traffic | JSON-LD types on page | Ahrefs page type |
|---|---|---|---|
| `/product-category/panasonic/laptops/toughbook-40/` | 154 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/getac/laptops-getac/` | 104 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/getac/tablets-getac/f110/` | 70 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/getac/laptops-getac/b360/` | 31 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/getac/laptops-getac/v120/` | 26 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/getac/tablets-getac/` | 19 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/panasonic/` | 19 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/getac/tablets-getac/ux10/` | 15 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/getac/laptops-getac/s410-laptops-getac/` | 13 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/accessories/headsets/setcom-headsets/` | 11 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/panasonic/2-in-1s/toughbook-g2/` | 8 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/cradles-docking-stations/getac-cradles-docking-stations-vehicle-equipment/` | 8 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/police-vehicle-equipment/window-guards/` | 4 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/accessories/keyboards/` | 4 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/panasonic/laptops/toughbook-56/` | 4 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/panasonic/laptops/page/7/` | 4 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/printer-mounts/` | 3 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/police-vehicle-equipment/gun-mounts/` | 1 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/police-vehicle-equipment/` | 1 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/accessories/desktop-dock/` | 1 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/panasonic/laptops/page/5/` | 1 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/accessories/page/50/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/misc-mounts/page/76/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/cradles-docking-stations/page/33/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/accessories/page/22/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/160/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/cradles-docking-stations/page/19/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/cradles-docking-stations/dell/page/3/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/page/49/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/accessories/routers/page/7/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/page/33/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/panasonic/2-in-1s/toughbook-g2/page/2/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/panasonic/laptops/page/10/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/accessories/cameras/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/getac/laptops-getac/b360/page/5/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/accessories/page/17/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/getac/tablets-getac/page/15/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/console-systems/page/14/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/accessories/page/67/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/shop/page/28/` | 0 | EntryPoint, ImageObject, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/page/11/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/pedestal-mounts/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/45/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/getac/laptops-getac/page/12/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/misc-mounts/page/15/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/getac/tablets-getac/page/3/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/docks/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/accessories/hard-drives/page/2/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/accessories/antennas/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/non-vehicle/wall-mounts/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/misc-mounts/page/25/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/material-handling/page/5/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/cradles-docking-stations/panasonic-cradles-docks/page/11/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/panasonic/page/9/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/3/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/35/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/getac/tablets-getac/k120/page/3/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/cradles-docks-vehicle-mounts-equipment/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/vehicle-equipment/cradles-docking-stations/panasonic-cradles-docks/page/2/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| `/product-category/accessories/printers-accessories/page/5/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing_Collection/Product |
| ... 140 more | | |

### Product page missing Product schema (32, Warning) → schema-check · FLAG

WooCommerce emits Product; a non-Woo product page needs the SEO plugin's schema type set.

Shape of the 32 sampled: 16 paginated (`/page/N/`), 2 with any traffic (26 total), TTFB median 1131 ms / max 1486 ms.

| URL | traffic | JSON-LD types on page | Ahrefs page type |
|---|---|---|---|
| `/product-category/getac/tablets-getac/zx10/` | 22 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product-category/panasonic/2-in-1s/toughbook-33/` | 4 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product/universal-wide-body-console-box-kit-with-locking-storage-and-cup-holder/` | 0 | BreadcrumbList, BuyAction, EntryPoint, ImageObject, ItemPage, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebPage, WebSite | /Listing/Product |
| `/product/kit-g140-dock-full-port-no-rf-bare-wire-power-adapter-7170-1285-00/` | 0 | BreadcrumbList, BuyAction, EntryPoint, ImageObject, ItemPage, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebPage, WebSite | /Listing/Product |
| `/product-category/getac/tablets-getac/f110/page/2/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product/havis-equipment-bracket-kit-for-vsx-consoles-front-tray-fits-motorola-remote-radio-xtl-1500-xtl-2500-xtl-5000-05-apx-6500-apx-7500-apx-8500-c-ebx-mot-1/` | 0 | BreadcrumbList, BuyAction, EntryPoint, ImageObject, ItemPage, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebPage, WebSite | /Listing/Product |
| `/product/toughbook-55-fz-55jz016bm/` | 0 | BreadcrumbList, BuyAction, EntryPoint, ImageObject, ItemPage, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebPage, WebSite | /Listing/Product |
| `/product/havis-docking-station-for-panasonic-toughbook-33-2-in-1-with-standard-port-replication-havis-power-supply/` | 0 | BreadcrumbList, BuyAction, EntryPoint, ImageObject, ItemPage, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebPage, WebSite | /Listing/Product |
| `/product-category/getac/tablets-getac/zx10/page/2/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product/toughbook-g3/` | 0 | BreadcrumbList, BuyAction, EntryPoint, ImageObject, ItemPage, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebPage, WebSite | /Listing/Product |
| `/product/1tb-opal-ssd-2nd-drive-quick-release-xpak-for-fz-55-mk1-mk2-mk3-universal-bay-expansion-area-2/` | 0 | BreadcrumbList, BuyAction, EntryPoint, ImageObject, ItemPage, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebPage, WebSite | /Listing/Product |
| `/product-category/panasonic/2-in-1s/toughbook-g2/page/5/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product-category/getac/laptops-getac/s410-laptops-getac/page/3/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product/fz-vzsu84a2u-fz-g1-standard-battery__trashed/` | 0 | BreadcrumbList, BuyAction, EntryPoint, ImageObject, ItemPage, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebPage, WebSite | /Listing/Product |
| `/toughbook-56/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product-category/panasonic/2-in-1s/toughbook-34/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product-category/getac/laptops-getac/s510/page/2/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product-category/getac/laptops-getac/b360/page/2/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product-category/getac/tablets-getac/page/7/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product-category/getac/laptops-getac/s410-laptops-getac/page/7/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/durabook-r12-rugged-tablet-edge-ai/` | 0 | Article, BlogPosting, BreadcrumbList, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, Person, PropertyValueSpecification, QuantitativeValue, ReadAction, SearchAction, WebPage, WebSite | /Listing/Product |
| `/product/havis-docking-station-for-getac-zx80-with-advanced-port-replication-power-cable/` | 0 | BreadcrumbList, BuyAction, EntryPoint, ImageObject, ItemPage, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebPage, WebSite | /Listing/Product |
| `/product-category/getac/laptops-getac/s410-laptops-getac/page/2/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product-category/getac/laptops-getac/s410-laptops-getac/page/6/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product-category/getac/tablets-getac/f110/page/5/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product-category/panasonic/laptops/toughbook-56/page/5/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product-category/panasonic/laptops/toughbook-56/page/4/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product/havis-5-year-enhanced-protection-plan-for-ds-gtc-1604/` | 0 | BreadcrumbList, BuyAction, EntryPoint, ImageObject, ItemPage, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebPage, WebSite | /Listing/Product |
| `/product-category/getac/tablets-getac/f110/page/4/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product/toughbook-34/` | 0 | BreadcrumbList, BuyAction, EntryPoint, ImageObject, ItemPage, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebPage, WebSite | /Listing/Product |
| `/product-category/getac/laptops-getac/s410-laptops-getac/page/5/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |
| `/product-category/panasonic/2-in-1s/toughbook-g2/page/4/` | 0 | BreadcrumbList, CollectionPage, EntryPoint, ImageObject, ListItem, MerchantReturnPolicy, Organization, PropertyValueSpecification, QuantitativeValue, SearchAction, WebSite | /Listing/Product |

### Slow server response for AI crawlers (525, Warning) → hosting/cache · FLAG

TTFB, not a crawl fix; check server cache and the host's APM.

Shape of the 200 sampled: 115 paginated (`/page/N/`), 0 with any traffic (0 total), TTFB median 2373 ms / max 11102 ms (of 525 flagged; sample is the top by traffic).

| URL | traffic | TTFB ms | load ms |
|---|---|---|---|
| `/product-category/accessories/page/50/` | 0 | 1861 | 1870 |
| `/product/panasonic-ha-55lvdlt0l/` | 0 | 2418 | 2441 |
| `/product-category/accessories/page/22/` | 0 | 1961 | 1974 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/160/` | 0 | 2594 | 2604 |
| `/product-category/vehicle-equipment/cradles-docking-stations/page/19/` | 0 | 2048 | 2060 |
| `/product/durabook-s14g3-s4k1q3dlabcx-4ystd/` | 0 | 10509 | 10533 |
| `/product/havis-docking-station-for-panasonic-toughbook-33-2-in-1-laptop-with-advanced-port-replication-dual-pass-thru-antenna-connections-with-lind-power-supply-ds-pan-1112-2/` | 0 | 2057 | 2083 |
| `/product-category/vehicle-equipment/page/49/` | 0 | 4483 | 4485 |
| `/product/gamber-johnson-7160-1385-multi-function-pivot-mount-2-extension-amps-mounting-plate-with-back-plate/` | 0 | 2004 | 2028 |
| `/product-category/vehicle-equipment/page/33/` | 0 | 4842 | 4859 |
| `/product/durabook-z14hg-z4l5r4jaabxx/` | 0 | 2447 | 2467 |
| `/product/toughbook-33-cf-33tz044am__trashed/` | 0 | 1925 | 2258 |
| `/product/panasonic-cf-33yz013bm/` | 0 | 3045 | 3159 |
| `/product-category/vehicle-equipment/page/11/` | 0 | 3599 | 3608 |
| `/product/havis-lite-tablet-vehicle-dock-no-pass-for-cf-33-and-cf-33-with-5g-2/` | 0 | 1956 | 1978 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/45/` | 0 | 2167 | 2179 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/misc-mounts/page/15/` | 0 | 2304 | 2316 |
| `/product/setcom-25-0733/` | 0 | 1901 | 1926 |
| `/product-category/panasonic/page/9/` | 0 | 2020 | 2031 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/3/` | 0 | 2666 | 2676 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/35/` | 0 | 2096 | 2111 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/173/` | 0 | 2361 | 2374 |
| `/product/toughbook-33-cf-33yz-0sbm/` | 0 | 3900 | 3925 |
| `/product/panasonic-cf-339w01ebm/` | 0 | 1850 | 2071 |
| `/product/panasonic-fz-g2nz00lbm/` | 0 | 4487 | 4797 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/167/` | 0 | 2439 | 2451 |
| `/product/durabook-s14g3-s4k1q2deabcx-4ystd/` | 0 | 9646 | 9648 |
| `/product/durabook-s14g3-s4k1q4aaabcx/` | 0 | 11102 | 11127 |
| `/product/toughbook-55-fz-55dv467am__trashed/` | 0 | 2558 | 2694 |
| `/product-category/vehicle-equipment/page/249/` | 0 | 4141 | 4161 |
| `/product/panasonic-fz-g2pz01hbm/` | 0 | 2534 | 2695 |
| `/shop/page/31/` | 0 | 5934 | 5947 |
| `/product-category/vehicle-equipment/page/247/` | 0 | 6178 | 6190 |
| `/product/panasonic-cf-338z01abm/` | 0 | 2405 | 3397 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/48/` | 0 | 2867 | 2880 |
| `/product/gamber-johnson-7170-0833-00-panasonic-toughbook-a3-tablet-cradle-no-rf-with-lind-90w-auto-power-adapter/` | 0 | 2667 | 2689 |
| `/product/durabook-u11-u1h1q3djahax/` | 0 | 4423 | 4451 |
| `/product/toughbook-g2-fz-g2nz-10bm/` | 0 | 2242 | 2848 |
| `/product-category/vehicle-equipment/page/268/` | 0 | 3689 | 3700 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/49/` | 0 | 2484 | 2495 |
| `/product/toughbook-33-cf-33yz-0pbm/` | 0 | 2113 | 2713 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/42/` | 0 | 2141 | 2159 |
| `/product-category/vehicle-equipment/page/265/` | 0 | 3678 | 3692 |
| `/product/panasonic-fz-g2nz009bm/` | 0 | 2745 | 3208 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/142/` | 0 | 2006 | 2018 |
| `/product-category/vehicle-equipment/cradles-docking-stations/page/17/` | 0 | 2001 | 2010 |
| `/product/panasonic-fz-g2pz-0mbm/` | 0 | 2116 | 2383 |
| `/product/durabook-u11-u1h1q3dcabxx/` | 0 | 6475 | 6499 |
| `/shop/page/448/` | 0 | 2214 | 2220 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/151/` | 0 | 2179 | 2197 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/19/` | 0 | 2706 | 2718 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/misc-mounts/page/40/` | 0 | 2049 | 2055 |
| `/product-category/vehicle-equipment/page/237/` | 0 | 4000 | 4010 |
| `/product-category/accessories/page/58/` | 0 | 1939 | 1950 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/misc-mounts/page/59/` | 0 | 1869 | 1883 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/misc-mounts/page/33/` | 0 | 1864 | 1878 |
| `/product/gamber-johnson-7170-0832-02-panasonic-toughbook-a3-tablet-docking-station-dual-rf-with-lind-90w-auto-power-adapter/` | 0 | 2301 | 2325 |
| `/product-category/vehicle-equipment/vehicle-mounts-equipment/page/135/` | 0 | 2323 | 2333 |
| `/product/durabook-s14g3-s4k1q3deabcx-4ystd/` | 0 | 2434 | 2459 |
| `/product-category/vehicle-equipment/page/259/` | 0 | 5390 | 5403 |
| ... 140 more | | |

Schema notes: these are Ahrefs' notices against its own page classification, not Google requirements. Google says no special structured data is needed to appear in AI features; the rule that matters is that any schema on the page describes what is visibly on the page. Organization schema is worth completing (name, logo, sameAs) through the SEO plugin. FAQPage no longer earns rich results in Google. Hand the list to `schema-check` with the existing validation-error work.

## 3. IndexNow (APPROVE)

Google ignores IndexNow; Bing, Yandex, Naver and Seznam use it, and Bing's index feeds ChatGPT search and Copilot. Two separate things can submit URLs, and Ahrefs only reports on the first:

- **Ahrefs auto-submission** (Site Audit → Crawl settings → IndexNow): status on sampled pages `Indexnow_not_changed` ×29, `Indexnow_success` ×11. `Indexnow_off` means the crawl setting is off. Turning it on needs an IndexNow key file hosted at the site root and a project boost that includes the feature; then Ahrefs submits changed, new, redirected and removed pages after each crawl.
- **The site pinging on publish**: Yoast SEO Premium (built in, on by default; not in free Yoast), Rank Math's Instant Indexing plugin, AIOSEO's IndexNow addon, or Microsoft's free `indexnow` plugin on anything else. This is the one that matters for fresh content, and Ahrefs cannot see it. Not probed (run with `--probe` to check the plugin list over SSH).

Client file says `ai.indexnow: unknown`. Recommended for the roster: Microsoft's `indexnow` plugin on free-Yoast sites (one key file, no settings), and the SEO plugin's own integration where it exists. Record the choice in `ai.indexnow` once it is live.

## 4. Not recommended, on purpose

- **llms.txt**: Google Search does not read it, and large-scale studies have found no citation effect. Skip it; if a client insists, it is harmless but does nothing measurable.
- **"AI-specific" schema or hidden content for AI**: Google needs none and treats hidden text as spam. Keep copy in the HTML as text; make schema match the page.
- **Blocking Googlebot to stay out of AI Overviews**: removes the page from Search. Use `nosnippet`/`max-snippet` on a page if a client truly wants no AI preview, and expect it to cost regular snippets too.
- **Chunking or rewriting content "for AI"**: the levers are the usual ones: indexable, snippet-eligible, fast, text in HTML, accurate schema, Business Profile current.

## 5. Reconciliation

AI Discoverability issue types in this crawl: 13 · with URLs: 4 · zero: 9

| Check | Importance | URLs | Route |
|---|---|---|---|
| Article page missing Article schema | Notice | 39 | schema-check (FLAG) |
| Category page missing ItemList schema | Notice | 996 | schema-check (FLAG) |
| Changed pages not submitted to IndexNow | Notice | 0 | human (FLAG) |
| FAQ page missing FAQPage schema | Notice | 0 | schema-check (FLAG) |
| Inconsistent AI training bot policy | Notice | 0 | ai-discoverability (APPROVE) |
| Indexable page blocked from all AI search bots | Warning | 0 | ai-discoverability (APPROVE) |
| Indexable page blocked from some AI search bots | Notice | 0 | ai-discoverability (APPROVE) |
| Main content requires JavaScript rendering | Warning | 0 | theme/plugin (by hand) (FLAG) |
| Organization schema missing or incomplete | Notice | 0 | schema-check (FLAG) |
| Page size exceeds 2 MB crawl limit | Error | 0 | fix-images (AUTO) |
| Product page missing Product schema | Warning | 32 | schema-check (FLAG) |
| Similar AI-generated content | Warning | 0 | content (Phase 4) (FLAG) |
| Slow server response for AI crawlers | Warning | 525 | hosting/cache (FLAG) |

## 6. Client file

`clients/ruggeddepot.yaml` → `ai.observed` was updated by this run (crawl, robots.txt kind if probed, blocked bots, IndexNow status). The policy fields (`search_bots`, `training_bots`, `exceptions`, `policy_confirmed_by`) are yours; the skill never writes them.

## Sources

- Google: AI features and your website https://developers.google.com/search/docs/appearance/ai-features
- Google: AI optimization guide https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google: robots meta tag / Google-Extended https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers
- Ahrefs: AI Discoverability in Site Audit (feature announcement, Sept 2026) https://ahrefs.com/blog/new-features-september-2026/
- Ahrefs: IndexNow in Site Audit https://help.ahrefs.com/en/articles/9317209-how-to-submit-pages-to-indexnow-within-site-audit
- Yoast: IndexNow is a Premium feature https://yoast.com/yoast-seo-june-28-2022/
- IndexNow https://www.indexnow.org/
