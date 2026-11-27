from pathlib import Path
import plistlib,json
p=Path(__file__).resolve().parents[1];a=p/'Artifacts/DessertBook.xcarchive';issues=[];count=0
for f in a.rglob('*'):
 if not f.is_file():continue
 count+=1;data=f.read_bytes()
 if b'/Users/' in data or Path.home().name.encode() in data:issues.append(f.relative_to(a).as_posix())
app=a/'Products/Applications/FolioKitchen.app'
for lang in ['en','de','fr','pt-BR']:
 x=plistlib.loads((app/(lang+'.lproj/InfoPlist.strings')).read_bytes());assert x['NSRemindersFullAccessUsageDescription'] and x['NSRemindersUsageDescription']
r={'archiveFilesScanned':count,'localizedPrivacyKeys':4,'machinePaths':issues};(p/'QA/archive-full-scan.json').write_text(json.dumps(r,indent=2));print(json.dumps(r));raise SystemExit(bool(issues))
