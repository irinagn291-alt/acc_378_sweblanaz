import SwiftUI
import WidgetKit
import ActivityKit
import EventKit
import UserNotifications

@MainActor final class Z6:NSObject,ObservableObject,UNUserNotificationCenterDelegate {
 @Published var v=G7(); @Published var message:String?; @Published var syncText=d8("cloud.local"); @Published var busy=false
 let recipes=P4.all
 private var queued:Task<Void,Never>?; private var pulse:Timer?
 private let disk:URL
 init(_ path:URL?=nil){disk=path ?? URL.documentsDirectory.appending(path:"FolioLocal.json");super.init();
 #if DEBUG
 if ProcessInfo.processInfo.arguments.contains("-folio-reset"){try? FileManager.default.removeItem(at:disk)}
 #endif
 if let data=try? Data(contentsOf:disk),let saved=try? JSONDecoder().decode(G7.self,from:data){v=saved};UNUserNotificationCenter.current().delegate=self; publish(); pulse=Timer.scheduledTimer(withTimeInterval:1,repeats:true){[weak self] _ in Task{@MainActor in self?.objectWillChange.send();self?.finishIfNeeded()}} }
 deinit {pulse?.invalidate()}
 var planned:[A6] {v.cloud.plans.values.filter{ !$0.removed }.sorted{$0.date<$1.date}}
 var shopping:[C8] {P4.shopping(v.cart,recipes)}
 func favorite(_ id:String)->Bool {v.cloud.marks[id]?.value=="1"}
 func star(_ id:String){v.cloud.marks[id]=E5(value:favorite(id) ? "0":"1",date:Date());save()}
 func note(_ id:String,_ s:String){v.cloud.notes[id]=E5(value:String(s.prefix(12000)),date:Date());save()}
 func save(_ sync:Bool=true){do{let b=try JSONEncoder().encode(v);try b.write(to:disk,options:.atomic)}catch{message=d8("storage.error")};publish();if sync && v.cloudOn {queued?.cancel();queued=Task{try? await Task.sleep(for:.seconds(2));guard !Task.isCancelled else{return};await self.cloud()}}}
 func publish(){let n=N4(timer:v.timer,plan:planned,shopping:shopping);if let b=try? JSONEncoder().encode(n){UserDefaults(suiteName:p9group)?.set(b,forKey:"folio.tiles")};WidgetCenter.shared.reloadAllTimelines()}
 func cart(_ r:T7,_ servings:Int){v.cart[r.id]=servings;v.checked=[];save(false)}
 func dropCart(_ id:String){v.cart[id]=nil;v.checked=[];save(false)}
 func check(_ id:String){if v.checked.contains(id){v.checked.remove(id)}else{v.checked.insert(id)};save(false)}
 func next(_ r:T7){v.progress[r.id]=min(r.steps.count,(v.progress[r.id] ?? 0)+1);save(false)}
 func previous(_ r:T7){v.progress[r.id]=max(0,(v.progress[r.id] ?? 0)-1);save(false)}
 func restart(_ r:T7){v.progress[r.id]=0;save(false)}
 func plan(_ r:T7,_ date:Date,_ servings:Int){let key=UUID().uuidString;v.cloud.plans[key]=A6(id:key,recipe:r.id,date:date,servings:servings);save()}
 func removePlan(_ id:String){v.cloud.plans[id]?.removed=true;v.cloud.plans[id]?.edited=Date();save()}
 func plannerToCart(){for p in planned where P4.w7().contains(p.date){v.cart[p.recipe,default:0] += p.servings};v.checked=[];save(false)}
 func allowNotifications() async ->Bool {
  let c=UNUserNotificationCenter.current();let s=await c.notificationSettings()
  if s.authorizationStatus == .notDetermined {do{return try await c.requestAuthorization(options:[.alert,.sound,.badge])}catch{message=d8("notification.error");return false}}
  return s.authorizationStatus == .authorized || s.authorizationStatus == .provisional
 }
 func schedule(_ id:String,_ title:String,_ body:String,_ trigger:UNNotificationTrigger) async {
  let c=UNMutableNotificationContent();c.title=title;c.body=body;c.sound = .default
  do{try await UNUserNotificationCenter.current().add(UNNotificationRequest(identifier:id,content:c,trigger:trigger))}catch{message=d8("notification.error")}
 }
 func preferences(_ week:Bool,_ season:Bool) async {
  if week || season {guard await allowNotifications() else{message=d8("notification.denied");return}}
  v.weekly=week;v.seasonal=season;let c=UNUserNotificationCenter.current();c.removePendingNotificationRequests(withIdentifiers:["folio.week","folio.spring","folio.summer","folio.autumn","folio.winter"])
  if week {await schedule("folio.week",d8("week.title"),d8("week.body"),UNCalendarNotificationTrigger(dateMatching:DateComponents(hour:10,minute:0,weekday:1),repeats:true))}
  if season {for (id,month) in [("spring",3),("summer",6),("autumn",9),("winter",12)] {await schedule("folio."+id,d8("season.title"),d8("season.body"),UNCalendarNotificationTrigger(dateMatching:DateComponents(month:month,day:1,hour:10,minute:0),repeats:true))}}
  save(false)
 }
 func start(_ r:T7,_ seconds:Int,_ notify:Bool) async {
  guard v.timer == nil else {message=d8("timer.exists");return}
  let granted=notify ? await allowNotifications():false
  if notify && !granted {message=d8("notification.denied")}
  let now=Date();v.timer=B2(recipe:r.id,began:now,end:now.addingTimeInterval(Double(max(1,min(seconds,21600)))));v.notifyTimer=granted;save(false)
  if granted,let t=v.timer{await schedule("folio.oven",d8("ready"),r.n,UNTimeIntervalNotificationTrigger(timeInterval:max(1,t.remaining),repeats:false))}
  await live(r)
 }
 func live(_ r:T7) async {
  guard let t=v.timer else{return};let state=F3.ContentState(end:t.end,start:t.began,paused:t.held)
  let content=ActivityContent(state:state,staleDate:t.held == nil ? t.end:nil)
  if let old=Activity<F3>.activities.first(where:{$0.activityState == .active || $0.activityState == .stale}) {await old.update(content)}
  else if ActivityAuthorizationInfo().areActivitiesEnabled {do{_ = try Activity.request(attributes:F3(title:r.n,recipe:r.id),content:content,pushType:nil)}catch{message=d8("live.unavailable")}}
 }
 func pause() async {
  guard var t=v.timer, let r=recipes.first(where:{$0.id==t.recipe}) else{return}
  UNUserNotificationCenter.current().removePendingNotificationRequests(withIdentifiers:["folio.oven"])
  if let held=t.held {t.began=Date();t.end=Date().addingTimeInterval(held);t.held=nil} else {guard t.remaining>0 else{return};t.held=t.remaining}
  v.timer=t;save(false)
  if t.held == nil && v.notifyTimer {await schedule("folio.oven",d8("ready"),r.n,UNTimeIntervalNotificationTrigger(timeInterval:max(1,t.remaining),repeats:false))};await live(r)
 }
 func cancel() async {v.timer=nil;save(false);UNUserNotificationCenter.current().removePendingNotificationRequests(withIdentifiers:["folio.oven"]);for a in Activity<F3>.activities {await a.end(nil,dismissalPolicy:.immediate)}}
 private var expired:Date?
 func finishIfNeeded(){guard let t=v.timer,t.held==nil,t.end<=Date(),expired != t.end else{return};expired=t.end;publish();Task{for a in Activity<F3>.activities {await a.end(ActivityContent(state:F3.ContentState(end:t.end,start:t.began,paused:nil),staleDate:nil),dismissalPolicy:.default)}}}
 func foreground() async {finishIfNeeded();if v.timer==nil {for a in Activity<F3>.activities {await a.end(nil,dismissalPolicy:.immediate)}};if v.cloudOn {await cloud()}}
 func exportReminder(_ p:A6) async {
  let e=EKEventStore()
  do {guard try await e.requestFullAccessToReminders() else {message=d8("reminder.denied");return}
   guard let calendar=e.defaultCalendarForNewReminders() else {message=d8("reminder.calendar");return}
   let r = v.reminderIDs[p.id].flatMap{e.calendarItem(withIdentifier:$0) as? EKReminder} ?? EKReminder(eventStore:e)
   r.calendar=calendar;r.title=recipes.first{$0.id==p.recipe}?.n ?? d8("bake");r.notes=d8("reminder.note");r.dueDateComponents=Calendar.current.dateComponents([.year,.month,.day,.hour,.minute],from:p.date);r.alarms=[EKAlarm(absoluteDate:p.date)];try e.save(r,commit:true);v.reminderIDs[p.id]=r.calendarItemIdentifier;save(false);message=d8("reminder.saved")
  }catch{message=d8("reminder.error")}
 }
 func setCloud(_ on:Bool) async {v.cloudOn=on;save(false);if on {await cloud()}else{syncText=d8("cloud.local")}}
 func cloud() async {}
 func preparef8d65() throws -> Data {
  let value: J4 = v.cloud
  return try JSONEncoder().encode(value)
 }
 func acceptf8d65(_ data:Data) throws {
  let incoming = try JSONDecoder().decode(J4.self, from:data)
  v.cloud.merge(incoming);save(false)
 }

 nonisolated func userNotificationCenter(_ center:UNUserNotificationCenter,willPresent notification:UNNotification) async ->UNNotificationPresentationOptions {[.banner,.sound]}
}
