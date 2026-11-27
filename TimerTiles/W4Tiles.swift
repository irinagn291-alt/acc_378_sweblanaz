import SwiftUI
import WidgetKit
import ActivityKit
#if WIDGET_QA
@testable import FolioKitchen
#endif

struct R3:TimelineEntry {var date:Date;var state:N4;var recipe:T7?}
struct W5:TimelineProvider {
 func placeholder(in context:Context)->R3{R3(date:Date(),state:.empty,recipe:P4.daily())}
 func getSnapshot(in context:Context,completion:@escaping(R3)->Void){completion(R3(date:Date(),state:N4.read(),recipe:P4.daily()))}
 func getTimeline(in context:Context,completion:@escaping(Timeline<R3>)->Void){
  let n=N4.read(),now=Date();var dates=[now]
  for d in 1...7{if let day=Calendar.current.date(byAdding:.day,value:d,to:Calendar.current.startOfDay(for:now)){dates.append(day)}}
  if let t=n.timer,t.held==nil,t.end>now {dates.append(t.end)}
  completion(Timeline(entries:dates.sorted().map{R3(date:$0,state:n,recipe:P4.daily($0))},policy:.after(now.addingTimeInterval(3600))))
 }
}
struct U9:View {
 let t:B2?;var date=Date()
 var body:some View {
  if let t {HStack{Image(systemName:"timer");if let held=t.held{Text(d8("paused")+" · "+String(Int(held)/60)+" "+d8("min"))}else if t.end>date {Text(timerInterval:t.began...t.end,countsDown:true).monospacedDigit()}else{Text(d8("ready"))}}.font(.headline)}else{Label(d8("timer.none"),systemImage:"oven").font(.caption)}
 }
}
struct D9:View {
 @Environment(\.widgetFamily) private var systemFamily;let e:R3;var forced:WidgetFamily?=nil
 var family:WidgetFamily{forced ?? systemFamily}
 var lock:Bool{family == .accessoryInline || family == .accessoryCircular || family == .accessoryRectangular}
 var route:String{if family == .systemLarge{return "dessertfolio://planner"};if lock || (family == .systemMedium && e.state.timer != nil){return "dessertfolio://timer"};return "dessertfolio://recipe?id="+(e.recipe?.id ?? "")}
 var body:some View {
  Group{switch family {
  case .accessoryInline: U9(t:e.state.timer,date:e.date)
  case .accessoryCircular: VStack(spacing:2){Image(systemName:e.state.timer?.held == nil ? "timer":"pause.fill");if let t=e.state.timer {if let held=t.held {Text(String(Int(ceil(held/60)))+" "+d8("min")).font(.caption2)}else if t.end>e.date{Text(timerInterval:t.began...t.end,countsDown:true).font(.caption2).minimumScaleFactor(0.5)}else{Image(systemName:"checkmark")}}else{Text(d8("timer.short")).font(.caption2)}}
  case .accessoryRectangular: VStack(alignment:.leading){Text(d8("oven")).font(.caption);U9(t:e.state.timer,date:e.date)}
  case .systemSmall: if let r=e.recipe {VStack(alignment:.leading,spacing:6){Image(r.id).resizable().scaledToFill().frame(maxWidth:.infinity).frame(height:82).clipped().clipShape(RoundedRectangle(cornerRadius:10));Text(d8("daily").uppercased()).font(.system(size:9,weight:.bold)).foregroundStyle(p9berry);Text(r.n).font(.system(.subheadline,design:.serif,weight:.semibold)).lineLimit(2)}}
  case .systemMedium: HStack(spacing:14){if let r=e.recipe {Image(r.id).resizable().scaledToFill().frame(width:105).clipped().clipShape(RoundedRectangle(cornerRadius:12));VStack(alignment:.leading,spacing:8){Text(d8("daily").uppercased()).font(.caption2.weight(.bold)).foregroundStyle(p9berry);Text(r.n).font(.system(.headline,design:.serif));Divider();U9(t:e.state.timer,date:e.date)}}}
  default: VStack(alignment:.leading,spacing:8){Text(d8("widget.week")).font(.system(.title2,design:.serif,weight:.semibold));let plan=e.state.plan.filter{!$0.removed && P4.w7(e.date).contains($0.date)};if plan.isEmpty{Text(d8("widget.plan.empty")).font(.caption).foregroundStyle(.secondary)}else{ForEach(Array(plan.prefix(4))){p in if let r=P4.all.first(where:{$0.id==p.recipe}){HStack{Image(r.id).resizable().scaledToFill().frame(width:30,height:30).clipShape(RoundedRectangle(cornerRadius:7));Text(r.n).font(.subheadline).lineLimit(1);Spacer();Text(p.date,format:.dateTime.weekday(.abbreviated)).font(.caption).foregroundStyle(p9berry)}}}}
   Divider();U9(t:e.state.timer,date:e.date);Text(d8("shopping")).font(.caption.weight(.bold));if e.state.shopping.isEmpty{Text(d8("widget.shopping.empty")).font(.caption).foregroundStyle(.secondary)}else{Text(e.state.shopping.prefix(4).map{$0.n+" "+$0.q()}.joined(separator:" · ")).font(.caption).lineLimit(3)};Spacer(minLength:0)}
  }}.foregroundStyle(lock ? Color.primary:p9ink).containerBackground(for:.widget){p9paper}.widgetURL(URL(string:route))
 }
}
struct K4:Widget {
 var body:some WidgetConfiguration {StaticConfiguration(kind:"FolioKitchenTiles",provider:W5()){D9(e:$0)}.configurationDisplayName(d8("widget.name")).description(d8("widget.description")).supportedFamilies([.systemSmall,.systemMedium,.systemLarge,.accessoryInline,.accessoryCircular,.accessoryRectangular])}
}
struct A3:Widget {
 var body:some WidgetConfiguration {
  ActivityConfiguration(for:F3.self){context in
   HStack{Image(systemName:"oven.fill").font(.title);VStack(alignment:.leading,spacing:5){Text(context.attributes.title).font(.headline);Text(d8((context.isStale || (context.state.paused==nil && context.state.end<=Date())) ? "ready":context.state.paused==nil ? "oven":"paused")).font(.caption)};Spacer();Z3(s:context.state).font(.title2.weight(.bold)).frame(maxWidth:130)}.padding(18).foregroundStyle(p9ink).activityBackgroundTint(p9paper).activitySystemActionForegroundColor(p9ink).widgetURL(URL(string:"dessertfolio://timer"))
  }dynamicIsland:{context in
   DynamicIsland{DynamicIslandExpandedRegion(.leading){Image(systemName:"oven.fill").foregroundStyle(p9pink)};DynamicIslandExpandedRegion(.trailing){Z3(s:context.state).frame(width:100)};DynamicIslandExpandedRegion(.bottom){Text(context.attributes.title).font(.headline)}}compactLeading:{Image(systemName:"timer").foregroundStyle(p9pink)}compactTrailing:{Z3(s:context.state).frame(width:58).font(.caption2)}minimal:{Image(systemName:"timer").foregroundStyle(p9pink)}.widgetURL(URL(string:"dessertfolio://timer")).keylineTint(p9pink)
  }
 }
}
struct Z3:View {var s:F3.ContentState
 var body:some View {if let p=s.paused {Text("\(Int(p)/60):\(String(format:"%02d",Int(p)%60))").monospacedDigit()}else{Text(timerInterval:s.start...s.end,countsDown:true).monospacedDigit()}}
}
#if !WIDGET_QA
@main struct W4Tiles:WidgetBundle {var body:some Widget{K4();A3()}}
#endif
