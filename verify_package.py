#!/usr/bin/env python3
"""Read-only integrity check for Q-Quality Work development handoff."""
import json
from pathlib import Path

r=Path(__file__).resolve().parent
m=json.loads((r/'WORK_SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
sat=json.loads((r/'data/sat_2025.json').read_text(encoding='utf-8'))
handbook=json.loads((r/'data/full_handbook_2025.json').read_text(encoding='utf-8'))
docs=json.loads((r/'data/document_2025_index.json').read_text(encoding='utf-8'))
actual={
 'chapters':len(sat['chapters']),
 'standards':len(sat['standards']),
 'eocs':sum(len(s['eocs']) for s in sat['standards']),
 'gsr':len(sat['gsr']),
 'provisional_items':len(sat['provisional']['items']),
 'document_eocs':len(docs['items']),
 'full_handbook_standard_details':len(handbook),
 'full_page_images':len(list((r/'assets/pages_full').glob('*.webp'))),
 'provisional_page_images':len(list((r/'assets/pages_pro').glob('*.webp'))),
}
failed=[]
for key,v in m['counts'].items():
 ok=actual[key]==v
 print(('OK  ' if ok else 'FAIL')+f' {key}: {actual[key]} (expected {v})')
 if not ok:failed.append(key)
for name in ['index.html','sat.html','achievement.html','handbook.html','app.js','style.css','data.js','assets/GAHAR_Full_2025_Original_SAT.xlsx','assets/GAHAR_Full_2025_EN.pdf','assets/GAHAR_Provisional_2025_AR.pdf']:
 ok=(r/name).is_file()
 print(('OK  ' if ok else 'FAIL')+' required file '+name)
 if not ok:failed.append(name)
if failed: raise SystemExit('Check failed: '+', '.join(failed))
print('PASS: Static package structure and counts. UI and storage still require browser tests.')
