from pathlib import Path
import json,re,hashlib,plistlib
p=Path(__file__).resolve().parents[1]
res=p/'DessertBook/Resources';words=json.loads((res/'Localizable.xcstrings').read_text())['strings'];a=json.loads((res/'CrumbIndex.json').read_text());langs={'en','de','fr','pt-BR'}
issues=[]
for k,v in words.items():
 if set(v['localizations'])!=langs:issues.append('Missing UI locale '+k)
for r in a:
 for field in ['title','intro','allergens']:
  if set(r[field])!=langs:issues.append('Missing recipe locale '+r['id'])
 for st in r['steps']:
  if set(st['text'])!=langs:issues.append('Missing step locale '+r['id'])
codefiles=list((p/'DessertBook/Source').glob('*.swift'))+list((p/'TimerTiles').glob('*.swift'))+list((p/'Tests').glob('*.swift'))
assert len(codefiles)==6
for f in codefiles:
 for key in re.findall(r'd8\("([a-zA-Z0-9.]+)"\)',f.read_text()):
  if key not in words:issues.append('Missing key '+key)
 for forbidden in ['/Users/',Path.home().name,'ContentView','MyApp','ViewModel']:
  if forbidden in f.read_text():issues.append('Forbidden identifier/path '+f.name+': '+forbidden)
for r in a:
 assert (res/'Assets.xcassets'/(r['id']+'.imageset')/(r['id']+'.png')).is_file()
 assert r['servings']>0 and all(i['amount']>0 for i in r['ingredients'])
proj=p/'DessertBook.xcodeproj/project.pbxproj';ids=set(re.findall(r'"([A-F0-9]{24})" = \{',proj.read_text()))
shared=[]
for other in p.parents[1].glob('*/*/*.xcodeproj/project.pbxproj'):
 if other.resolve()==proj.resolve():continue
 duplicates=ids & set(re.findall(r'\b[A-F0-9]{24}\b',other.read_text(errors='ignore')))
 if duplicates:shared.append({'project':str(other.relative_to(p.parents[2])),'ids':list(duplicates)})
if shared:issues.append('Shared object UUIDs')
for f in [p/'DessertBook/Info.plist',p/'TimerTiles/Info.plist',p/'DessertBook/Folio.entitlements',p/'TimerTiles/Tile.entitlements',res/'PrivacyInfo.xcprivacy']:plistlib.loads(f.read_bytes())
store=json.loads((p/'Store/metadata.json').read_text())
for lang in langs:
 for k,limit in [('name',30),('subtitle',30),('keywords',100)]:
  if len(store[lang][k])>limit:issues.append(f'Metadata length {lang} {k}: {len(store[lang][k])}')
banned=re.compile(r'\b(?:bet|casino|slot|jackpot|odds)\b',re.I)
for lang in langs:
 for v in [x['localizations'][lang]['stringUnit']['value'] for x in words.values()]+list(store[lang].values()):
  if banned.search(v):issues.append('Prohibited store/UI vocabulary '+lang)
report={'swiftFiles':len(codefiles),'recipes':len(a),'locales':sorted(langs),'UIKeys':len(words),'projectObjectIDs':len(ids),'duplicateUUIDs':shared,'issues':issues}
(p/'QA/static-audit.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
raise SystemExit(bool(issues))
