# fix-images (product alt from title): ruggeddepot.com (staging)

Run 2026-10-30-0940 · mode **apply** · alias `ruggeddepot-staging` · provider `kinsta` · install host `stg-ruggeddepot-rdstaging.kinsta.cloud`

4915 products, 18437 images. 6909 alts written (6909 confirmed), 0 already set on the attachment, 11528 shared or kept.

Full list: `2026-10-30-0940-fix-images-product-alt-staging-apply.csv`. Rule: featured = product title; gallery = title + view word from the file name or 'view N'; variation = title + attributes. Existing alts are never overwritten. Attachments used by more than 5 products are placeholders or brand images and are listed in the `-exceptions.csv` for a human instead.

Sample:

- featured  `7160-1132-0220Semi-Truck20Pivot20Mount202inch20ext` → Gamber-Johnson Zirkona Pivot Arm with 4" Extension and AMPs Plate (7160-1132-02)
- featured  `7170-0674-00-dock-only-2.jpg` → KIT: Samsung Galaxy Tab ACTIVE2 Dual USB Dock W/MP205 Connector (7160-1368-30) And AC Power Supply (#17794).
- gallery   `7170-0765-31_TA3-2.jpg` → KIT: Samsung Galaxy Tab ACTIVE2 Dual USB Dock W/MP205 Connector (7160-1368-30) And AC Power Supply (#17794). - view 2
- gallery   `samsung-galaxy-tab-active2-dock-backside_1-1-2.jpg` → KIT: Samsung Galaxy Tab ACTIVE2 Dual USB Dock W/MP205 Connector (7160-1368-30) And AC Power Supply (#17794). - view 3
- gallery   `samsung-galaxy-tab-active2-dock-top_1-1-2.jpg` → KIT: Samsung Galaxy Tab ACTIVE2 Dual USB Dock W/MP205 Connector (7160-1368-30) And AC Power Supply (#17794). - top view
- gallery   `samsung-galaxy-tab-active2-dock-side-2_1-1-2.jpg` → KIT: Samsung Galaxy Tab ACTIVE2 Dual USB Dock W/MP205 Connector (7160-1368-30) And AC Power Supply (#17794). - side view
- featured  `7170-0680-00-2.jpg` → Samsung Galaxy Tab ACTIVE2 Dual USB Docking Station With 12-32V Isolated Power Adapter
- gallery   `SamsungTA3_MP205_PowerAdapter-1-2.jpg` → Samsung Galaxy Tab ACTIVE2 Dual USB Docking Station With 12-32V Isolated Power Adapter - view 2
- gallery   `7160-102920Samsung20Galaxy20TabActive220docking20s` → Samsung Galaxy Tab ACTIVE2 Dual USB Docking Station With 12-32V Isolated Power Adapter - view 3
- gallery   `samsung-galaxy-tab-active2-dock-backside_2-2.jpg` → Samsung Galaxy Tab ACTIVE2 Dual USB Docking Station With 12-32V Isolated Power Adapter - docked
- gallery   `samsung-galaxy-tab-active2-dock-side-2_2-2.jpg` → Samsung Galaxy Tab ACTIVE2 Dual USB Docking Station With 12-32V Isolated Power Adapter - docked, side view
- featured  `7170-0680-00_1-2.jpg` → Samsung Galaxy Tab ACTIVE2 Dual USB Docking Station With 70-110V Isolated Poweradapter
- gallery   `SamsungTA3_MP205_PowerAdapter-2-2.jpg` → Samsung Galaxy Tab ACTIVE2 Dual USB Docking Station With 70-110V Isolated Poweradapter - view 2
- gallery   `samsung-galaxy-tab-active2-dock-backside_4-2.jpg` → Samsung Galaxy Tab ACTIVE2 Dual USB Docking Station With 70-110V Isolated Poweradapter - docked
- gallery   `samsung-galaxy-tab-active2-dock-top_3-2.jpg` → Samsung Galaxy Tab ACTIVE2 Dual USB Docking Station With 70-110V Isolated Poweradapter - docked, top view
- gallery   `samsung-galaxy-tab-active2-dock-side-2_4-2.jpg` → Samsung Galaxy Tab ACTIVE2 Dual USB Docking Station With 70-110V Isolated Poweradapter - docked, side view
- featured  `download-50.png` → Havis Premium Tablet Vehicle Dock (dual pass) for TOUGHBOOK G2, TOUGHBOOK G1
- featured  `CF-VNT002U-Panasonic-Tether.png` → Panasonic Tether for TOUGHBOOK 33, TOUGHBOOK 31, TOUGHBOOK 20, TOUGHBOOK A3
- featured  `download-12.png` → Panasonic CF-LNDBRK120 Mounting Bracket
- featured  `CF-LNDMLDC90-LIND-Vehicle-Adapter-90W-MIL-STD-461F` → Panasonic CF-LNDMLDC90 DC Converter - 90 W Output Power - MIL-STD-461F
- featured  `CF-LNDDC80-LIND-Vehicle-Adapter-80W-2.png` → Panasonic LIND Vehicle Adapter (80W)
- featured  `7160-0368_0_0-1.jpg` → Gamber-johnson Forklift Mount Forklift Roof Mount
- gallery   `Overhead-guard-mount-dell-latitude-12-tablet_0-1.j` → Gamber-johnson Forklift Mount Forklift Roof Mount - view 2
- gallery   `7160-0368_overhead-guard-intermec_0-1.jpg` → Gamber-johnson Forklift Mount Forklift Roof Mount - view 3
- gallery   `7160-0368-panasonic-cf19-forklift_0-1.jpg` → Gamber-johnson Forklift Mount Forklift Roof Mount - view 4

Object cache flush: (True, 'Success: The cache was flushed.\nSuccess: All caches were cleared. Changes usually appear globally within a few minutes.')

## Rollback

Every attachment in the list had an empty `_wp_attachment_image_alt`; clearing it restores the previous state. `backup/` holds the full result.
