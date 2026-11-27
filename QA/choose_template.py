from pathlib import Path
import sys,runpy
factory=Path(sys.argv[1]);kind=sys.argv[2]
data=runpy.run_path(str(factory/'gf/genesis/simulator_pool.py'))['inventory']()
rows=[d for group in data['devices'].values() for d in group if not d['name'].startswith('GF isolated ') and d['name'].startswith(kind)]
preferred=[d for d in rows if ('13-inch' in d['name'] if kind=='iPad' else 'Pro' in d['name'])]
if not rows:raise SystemExit('No available '+kind+' simulator template')
print((preferred or rows)[0]['udid'])
