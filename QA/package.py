from pathlib import Path
import zipfile,hashlib,json
p=Path(__file__).resolve().parents[1]
a=p/'Artifacts';a.mkdir(exist_ok=True)
folders=['DessertBook','TimerTiles','Tests','DessertBook.xcodeproj','Store']
items=[p/'REPORT.md']
for folder in folders:
 items.extend(f for f in (p/folder).rglob('*') if f.is_file() and not any(x in f.parts for x in ['xcuserdata','.DS_Store']))
items.extend(f for f in (p/'QA').iterdir() if f.suffix in ['.py','.sh'] or f.name=='static-audit.json')
with zipfile.ZipFile(a/'DessertBook-source.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in items:z.write(f,Path('DessertBook')/f.relative_to(p))
manifest={f.relative_to(p).as_posix():hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(items)}
(a/'source-manifest.json').write_text(json.dumps(manifest,indent=2))
print('Packaged',len(items),'files')
