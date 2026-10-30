# fix-redirect-links: wp_options hits for slepianfirm.com (live)

Run 2026-10-30-0956 · mode **dry** · companion to `2026-10-30-0956-fix-redirect-links-live-dry.md`. Report only: the script never edits options.

Each row is an option whose value contains an old URL (transients are excluded). `autoload` and size help tell a widget or menu setting from an analytics or cache blob, which can be ignored.

| option_name | autoload | bytes | old URL | context |
|---|---|---|---|---|
| `widget_text` | yes | 20133 | `https://www.slepianfirm.com/jeremy-trimble/` | ...uote-6">             <a href="<?php echo get_site_url(); ?>/jeremy-trimble/">               <img class="alignnone size-footer-images" ... |
| `widget_text` | yes | 20133 | `https://www.slepianfirm.com/gary-Schwartz` | ...s:4:"text";s:126:"<h4><a href="<?php echo get_site_url(); ?>/gary-Schwartz" style="width:100%;" class="btn btn-default">Read Gary's Bi... |
| `widget_text` | yes | 20133 | `https://www.slepianfirm.com/eric-slepian` | ...s:4:"text";s:125:"<h4><a href="<?php echo get_site_url(); ?>/eric-slepian" style="width:100%;" class="btn btn-default">Read Eric's Bi... |
| `widget_text` | yes | 20133 | `https://www.slepianfirm.com/keri-davis` | ...s:4:"text";s:123:"<h4><a href="<?php echo get_site_url(); ?>/keri-davis" style="width:100%;" class="btn btn-default">Read Keri's Bi... |
