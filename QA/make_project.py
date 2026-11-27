from pathlib import Path
import json,uuid,plistlib,subprocess,re
p=Path(__file__).resolve().parents[1];res=p/'DessertBook/Resources'; assets=res/'Assets.xcassets'
def dump(path,value):path.write_bytes(plistlib.dumps(value,sort_keys=False))
assets.joinpath('Contents.json').write_text(json.dumps({'info':{'version':1,'author':'xcode'}}))
# Raster resources are already bundled; project generation never needs the image service.
for name in ['cupcake','brownie','lemon','berry','cookie','apple']:
 assert (assets/(name+'.imageset')/(name+'.png')).is_file()
assert (assets/'OvenMark.appiconset/icon.png').is_file()
base={'CFBundleDevelopmentRegion':'en','CFBundleExecutable':'$(EXECUTABLE_NAME)','CFBundleIdentifier':'$(PRODUCT_BUNDLE_IDENTIFIER)','CFBundleInfoDictionaryVersion':'6.0','CFBundleName':'$(PRODUCT_NAME)','CFBundlePackageType':'APPL','CFBundleShortVersionString':'$(MARKETING_VERSION)','CFBundleVersion':'$(CURRENT_PROJECT_VERSION)','CFBundleDisplayName':'Dessert Book','LSRequiresIPhoneOS':True,'NSSupportsLiveActivities':True,'NSRemindersUsageDescription':'Dessert Book can add a planned bake to Apple Reminders when you choose to export it.','NSRemindersFullAccessUsageDescription':'Dessert Book can add a planned bake to Apple Reminders when you choose to export it.','UIBackgroundModes':['remote-notification'],'UILaunchScreen':{},'UISupportedInterfaceOrientations':['UIInterfaceOrientationPortrait','UIInterfaceOrientationLandscapeLeft','UIInterfaceOrientationLandscapeRight'],'UISupportedInterfaceOrientations~ipad':['UIInterfaceOrientationPortrait','UIInterfaceOrientationPortraitUpsideDown','UIInterfaceOrientationLandscapeLeft','UIInterfaceOrientationLandscapeRight'],'UIApplicationSceneManifest':{'UIApplicationSupportsMultipleScenes':False},'CFBundleURLTypes':[{'CFBundleURLName':'kitchen.page','CFBundleURLSchemes':['dessertfolio']}],'ITSAppUsesNonExemptEncryption':False}
dump(p/'DessertBook/Info.plist',base)
ext={k:v for k,v in base.items() if k.startswith('CFBundle') and k not in ['CFBundleDisplayName','CFBundleURLTypes']};ext.update(CFBundlePackageType='XPC!',CFBundleDisplayName='Kitchen Pages',NSExtension={'NSExtensionPointIdentifier':'com.apple.widgetkit-extension'})
dump(p/'TimerTiles/Info.plist',ext)
dump(p/'DessertBook/Folio.entitlements',{'com.apple.security.application-groups':['group.com.dessertbook.app'],'aps-environment':'development','com.apple.developer.icloud-container-identifiers':['iCloud.com.dessertbook.app'],'com.apple.developer.icloud-services':['CloudKit']})
dump(p/'TimerTiles/Tile.entitlements',{'com.apple.security.application-groups':['group.com.dessertbook.app']})
dump(res/'PrivacyInfo.xcprivacy',{'NSPrivacyTracking':False,'NSPrivacyCollectedDataTypes':[],'NSPrivacyAccessedAPITypes':[{'NSPrivacyAccessedAPIType':'NSPrivacyAccessedAPICategoryUserDefaults','NSPrivacyAccessedAPITypeReasons':['1C8F.1']} ]})
objects={}
def new(obj):i=uuid.uuid4().hex[:24].upper();objects[i]=obj;return i
def file(path,typ):return new({'isa':'PBXFileReference','lastKnownFileType':typ,'path':path,'sourceTree':'<group>'})
core=file('DessertBook/Source/P9Crumbs.swift','sourcecode.swift');store=file('DessertBook/Source/L2Oven.swift','sourcecode.swift');ui=file('DessertBook/Source/S5Pages.swift','sourcecode.swift');main=file('DessertBook/Source/A7Folio.swift','sourcecode.swift');widget=file('TimerTiles/W4Tiles.swift','sourcecode.swift');tests=file('Tests/V8Checks.swift','sourcecode.swift')
resources=[file('DessertBook/Resources/'+f,t) for f,t in [('CrumbIndex.json','text.json'),('Localizable.xcstrings','text.json.xcstrings'),('InfoPlist.xcstrings','text.json.xcstrings'),('Assets.xcassets','folder.assetcatalog'),('PrivacyInfo.xcprivacy','text.xml')]]
infos=[file('DessertBook/Info.plist','text.plist.xml'),file('TimerTiles/Info.plist','text.plist.xml'),file('DessertBook/Folio.entitlements','text.plist.entitlements'),file('TimerTiles/Tile.entitlements','text.plist.entitlements')]
def product(name,t):return new({'isa':'PBXFileReference','explicitFileType':t,'includeInIndex':0,'path':name,'sourceTree':'BUILT_PRODUCTS_DIR'})
appProd=product('FolioKitchen.app','wrapper.application');extProd=product('KitchenPages.appex','wrapper.app-extension');unitProd=product('CrumbChecks.xctest','wrapper.cfbundle');uiProd=product('KitchenJourney.xctest','wrapper.cfbundle')
grp=new({'isa':'PBXGroup','children':[core,store,ui,main,widget,tests]+resources+infos,'sourceTree':'<group>'});products=new({'isa':'PBXGroup','children':[appProd,extProd,unitProd,uiProd],'name':'Products','sourceTree':'<group>'});objects[grp]['children'].append(products)
def phase(kind,files):return new({'isa':kind,'buildActionMask':2147483647,'files':[new({'isa':'PBXBuildFile','fileRef':f}) for f in files],'runOnlyForDeploymentPostprocessing':0})
def configs(settings):
 ids=[]
 for n in ['Debug','Release']:
  s=dict(settings)
  if n=='Debug':s.update(SWIFT_OPTIMIZATION_LEVEL='-Onone',GCC_PREPROCESSOR_DEFINITIONS=['DEBUG=1','$(inherited)'],SWIFT_ACTIVE_COMPILATION_CONDITIONS='DEBUG'+(' KITCHEN_UI' if s.get('PRODUCT_NAME')=='KitchenJourney' else ' WIDGET_QA' if s.get('PRODUCT_NAME')=='CrumbChecks' else ''))
  else:s.update(SWIFT_OPTIMIZATION_LEVEL='-O',SWIFT_COMPILATION_MODE='wholemodule',STRIP_INSTALLED_PRODUCT='YES',DEPLOYMENT_POSTPROCESSING='YES',COPY_PHASE_STRIP='YES',STRIP_STYLE='non-global',SWIFT_SERIALIZE_DEBUGGING_OPTIONS='NO',DEBUG_INFORMATION_FORMAT='',ENABLE_TESTABILITY='NO',OTHER_LDFLAGS=['$(inherited)','-Wl,-oso_prefix,$(SRCROOT)/'])
  ids.append(new({'isa':'XCBuildConfiguration','name':n,'buildSettings':s}))
 return new({'isa':'XCConfigurationList','buildConfigurations':ids,'defaultConfigurationIsVisible':0,'defaultConfigurationName':'Release'})
common={'SDKROOT':'iphoneos','IPHONEOS_DEPLOYMENT_TARGET':'17.4','SWIFT_VERSION':'5.0','TARGETED_DEVICE_FAMILY':'1,2','MARKETING_VERSION':'1.3.2','CURRENT_PROJECT_VERSION':'17','CODE_SIGN_STYLE':'Automatic','ENABLE_USER_SCRIPT_SANDBOXING':'YES','CLANG_ENABLE_MODULES':'YES','SWIFT_EMIT_LOC_STRINGS':'NO','SUPPORTS_MACCATALYST':'NO','SUPPORTS_MAC_DESIGNED_FOR_IPHONE_IPAD':'NO','SUPPORTS_XR_DESIGNED_FOR_IPHONE_IPAD':'NO','DEBUG_INFORMATION_FORMAT':'dwarf','GCC_C_LANGUAGE_STANDARD':'gnu17'}
projid=new({'isa':'PBXProject'});appId=new({'isa':'PBXNativeTarget'});extId=new({'isa':'PBXNativeTarget'});unitId=new({'isa':'PBXNativeTarget'});uiId=new({'isa':'PBXNativeTarget'})
def dep(target):
 proxy=new({'isa':'PBXContainerItemProxy','containerPortal':projid,'proxyType':1,'remoteGlobalIDString':target,'remoteInfo':'KitchenProduct'})
 return new({'isa':'PBXTargetDependency','target':target,'targetProxy':proxy})
copyFile=new({'isa':'PBXBuildFile','fileRef':extProd,'settings':{'ATTRIBUTES':['RemoveHeadersOnCopy','CodeSignOnCopy']}})
copy=new({'isa':'PBXCopyFilesBuildPhase','buildActionMask':2147483647,'dstPath':'','dstSubfolderSpec':13,'files':[copyFile],'name':'Embed Kitchen Pages','runOnlyForDeploymentPostprocessing':0})
for tid,name,pid,bundle,src,rs,extra,deps,typ in [
(appId,'FolioKitchen',appProd,'com.dessertbook.app',[main,core,store,ui],resources,{'INFOPLIST_FILE':'DessertBook/Info.plist','CODE_SIGN_ENTITLEMENTS':'DessertBook/Folio.entitlements','ASSETCATALOG_COMPILER_APPICON_NAME':'OvenMark','LD_RUNPATH_SEARCH_PATHS':['$(inherited)','@executable_path/Frameworks']},[dep(extId)],'com.apple.product-type.application'),
(extId,'KitchenPages',extProd,'com.dessertbook.app.pages',[widget,core],[r for r in resources if r!=resources[2]],{'INFOPLIST_FILE':'TimerTiles/Info.plist','CODE_SIGN_ENTITLEMENTS':'TimerTiles/Tile.entitlements','APPLICATION_EXTENSION_API_ONLY':'YES','SKIP_INSTALL':'YES','LD_RUNPATH_SEARCH_PATHS':['$(inherited)','@executable_path/Frameworks','@executable_path/../../Frameworks']},[],'com.apple.product-type.app-extension'),
(unitId,'CrumbChecks',unitProd,'com.dessertbook.app.checks',[tests,widget],[],{'GENERATE_INFOPLIST_FILE':'YES','SWIFT_ACTIVE_COMPILATION_CONDITIONS':'WIDGET_QA','TEST_HOST':'$(BUILT_PRODUCTS_DIR)/FolioKitchen.app/$(BUNDLE_EXECUTABLE_FOLDER_PATH)/FolioKitchen','BUNDLE_LOADER':'$(TEST_HOST)','ENABLE_TESTABILITY':'YES'},[dep(appId)],'com.apple.product-type.bundle.unit-test'),
(uiId,'KitchenJourney',uiProd,'com.dessertbook.app.journey',[tests],[],{'GENERATE_INFOPLIST_FILE':'YES','SWIFT_ACTIVE_COMPILATION_CONDITIONS':'KITCHEN_UI','TEST_TARGET_NAME':'FolioKitchen'},[dep(appId)],'com.apple.product-type.bundle.ui-testing')]:
 s=dict(common,PRODUCT_NAME=name,PRODUCT_BUNDLE_IDENTIFIER=bundle,**extra)
 if tid==appId:s['ENABLE_TESTABILITY']='YES'
 phases=[phase('PBXSourcesBuildPhase',src),phase('PBXFrameworksBuildPhase',[]),phase('PBXResourcesBuildPhase',rs)]+([copy] if tid==appId else [])
 objects[tid].update(buildConfigurationList=configs(s),buildPhases=phases,buildRules=[],dependencies=deps,name=name,productName=name,productReference=pid,productType=typ)
objects[projid].update(attributes={'BuildIndependentTargetsInParallel':'YES','LastUpgradeCheck':'2720','ORGANIZATIONNAME':'Meringue Folio Atelier','TargetAttributes':{appId:{'SystemCapabilities':{'com.apple.ApplicationGroups.iOS':{'enabled':1},'com.apple.Push':{'enabled':1},'com.apple.iCloud':{'enabled':1}}}}},buildConfigurationList=configs({'CLANG_ENABLE_OBJC_ARC':'YES','SWIFT_VERSION':'5.0','IPHONEOS_DEPLOYMENT_TARGET':'17.4','SDKROOT':'iphoneos'}),compatibilityVersion='Xcode 14.0',developmentRegion='en',hasScannedForEncodings=0,knownRegions=['en','de','fr','pt-BR','Base'],mainGroup=grp,productRefGroup=products,projectDirPath='',projectRoot='',targets=[appId,extId,unitId,uiId])
def q(x):return json.dumps(str(x))
def ser(x,depth=0):
 if isinstance(x,dict):return '{\n'+''.join('\t'*(depth+1)+q(k)+' = '+ser(v,depth+1)+';\n' for k,v in x.items())+'\t'*depth+'}'
 if isinstance(x,list):return '( '+', '.join(ser(v,depth) for v in x)+' )'
 return str(x) if isinstance(x,int) else q(x)
proj=p/'DessertBook.xcodeproj';proj.mkdir(exist_ok=True);proj.joinpath('project.pbxproj').write_text('// !$*UTF8*$!\n'+ser({'archiveVersion':1,'classes':{},'objectVersion':56,'objects':objects,'rootObject':projid})+'\n')
schemes=proj/'xcshareddata/xcschemes';schemes.mkdir(parents=True,exist_ok=True)
def ref(t,n):return f'<BuildableReference BuildableIdentifier="primary" BlueprintIdentifier="{t}" BuildableName="{n}.app" BlueprintName="{n}" ReferencedContainer="container:DessertBook.xcodeproj"/>'
scheme=f'''<?xml version="1.0" encoding="UTF-8"?><Scheme LastUpgradeVersion="2720" version="1.7"><BuildAction parallelizeBuildables="YES" buildImplicitDependencies="YES"><BuildActionEntries><BuildActionEntry buildForTesting="YES" buildForRunning="YES" buildForProfiling="YES" buildForArchiving="YES" buildForAnalyzing="YES">{ref(appId,'FolioKitchen')}</BuildActionEntry></BuildActionEntries></BuildAction><TestAction buildConfiguration="Debug" selectedDebuggerIdentifier="Xcode.DebuggerFoundation.Debugger.LLDB" selectedLauncherIdentifier="Xcode.IDEFoundation.Launcher.LLDB" shouldUseLaunchSchemeArgsEnv="YES"><Testables>'''
for t,n in [(unitId,'CrumbChecks'),(uiId,'KitchenJourney')]:scheme+=f'<TestableReference skipped="NO"><BuildableReference BuildableIdentifier="primary" BlueprintIdentifier="{t}" BuildableName="{n}.xctest" BlueprintName="{n}" ReferencedContainer="container:DessertBook.xcodeproj"/></TestableReference>'
scheme+=f'''</Testables></TestAction><LaunchAction buildConfiguration="Debug" selectedDebuggerIdentifier="Xcode.DebuggerFoundation.Debugger.LLDB" selectedLauncherIdentifier="Xcode.IDEFoundation.Launcher.LLDB" launchStyle="0" useCustomWorkingDirectory="NO" ignoresPersistentStateOnLaunch="NO" debugDocumentVersioning="YES" debugServiceExtension="internal" allowLocationSimulation="NO"><BuildableProductRunnable runnableDebuggingMode="0">{ref(appId,'FolioKitchen')}</BuildableProductRunnable></LaunchAction><ProfileAction buildConfiguration="Release" shouldUseLaunchSchemeArgsEnv="YES" savedToolIdentifier="" useCustomWorkingDirectory="NO" debugDocumentVersioning="YES"><BuildableProductRunnable runnableDebuggingMode="0">{ref(appId,'FolioKitchen')}</BuildableProductRunnable></ProfileAction><AnalyzeAction buildConfiguration="Debug"/><ArchiveAction buildConfiguration="Release" revealArchiveInOrganizer="YES"/></Scheme>'''
schemes.joinpath('DessertKitchen.xcscheme').write_text(scheme)
# No machine-specific paths are retained in the project or generation helper.
print('Created project with',len(objects),'fresh object IDs')
