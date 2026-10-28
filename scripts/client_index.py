#!/usr/bin/env python3
"""Rebuild docs/client-index.md from clients/*.yaml. Run from the repo root."""
import glob, datetime, yaml
rows=[]
for f in sorted(glob.glob('clients/*.yaml')):
    if f.endswith('_template.yaml'): continue
    d=yaml.safe_load(open(f)); p=d.get('platform',{}); t=d.get('tracking',{}); a=d.get('ahrefs',{})
    rows.append((d['slug'],d.get('vertical'),p.get('cms'),p.get('page_builder'),p.get('seo_plugin'),str(t.get('gtm_container')),str(t.get('ga4_measurement_id')),a.get('gsc_connected'),d.get('hosting',{}).get('provider')))
lines=["# Client index","",f"Generated {datetime.date.today()} from `clients/*.yaml`. Regenerate with `python3 scripts/client_index.py`.","","| slug | vertical | cms | builder | seo | gtm | ga4 | gsc in ahrefs | host |","|---|---|---|---|---|---|---|---|---|"]
for r in rows: lines.append("| "+" | ".join(str(x) for x in r)+" |")
open('docs/client-index.md','w').write("\n".join(lines)+"\n")
print(len(rows),"sites indexed")
