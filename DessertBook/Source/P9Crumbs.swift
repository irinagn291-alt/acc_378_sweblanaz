import Foundation
import SwiftUI
import ActivityKit

func d8(_ k:String)->String { NSLocalizedString(k, comment: "") }
func q4(_ n:Int)->String {String(n)+" "+d8(n==1 ? "portion":"servings")}
func m6(_ x:[String:String])->String { let l=Bundle.main.preferredLocalizations.first ?? "en"; return x[l] ?? x[String(l.prefix(2))] ?? x["en"] ?? "" }
let p9group="group.com.dessertbook.app"
let p9ink=Color(red:0.29,green:0.17,blue:0.37)
let p9pink=Color(red:1,green:0.48,blue:0.67)
let p9paper=Color(red:1,green:0.965,blue:0.985)
let p9berry=Color(red:0.57,green:0.20,blue:0.43)

struct C8:Codable,Identifiable,Hashable {
 var id:String; var amount:Double; var unit:String; var name:[String:String]
 var n:String { m6(name) }
 var key:String { id+"|"+unit }
 func q(_ f:Double=1)->String { P4.n(amount*f)+" "+d8(unit) }
}
struct H2:Codable,Hashable { var text:[String:String]; var seconds:Int; var n:String {m6(text)} }
struct T7:Codable,Identifiable,Hashable {
 var id:String; var title:[String:String]; var intro:[String:String]; var category:String; var minutes:Int; var servings:Int; var seasons:[Int]; var allergens:[String:String]; var ingredients:[C8]; var steps:[H2]
 var n:String {m6(title)}; var sub:String {m6(intro)}
 func step(_ i:Int,_ portions:Int)->String {steps[i].n.replacingOccurrences(of:"[[half]]",with:P4.n(60*Double(portions)/Double(servings)))}
}
enum P4 {
 static var all:[T7] { guard let u=Bundle.main.url(forResource:"CrumbIndex",withExtension:"json"),let d=try? Data(contentsOf:u),let a=try? JSONDecoder().decode([T7].self,from:d) else {return []}; return a }
 static func w7(_ date:Date=Date())->Range<Date>{let start=Calendar.current.startOfDay(for:date);return start..<Calendar.current.date(byAdding:.day,value:7,to:start)!}
 static func n(_ v:Double)->String { v.formatted(.number.precision(.fractionLength(0...2))) }
 static func day(_ date:Date=Date())->Int { Calendar.current.ordinality(of:.day,in:.era,for:date) ?? 0 }
 static func daily(_ date:Date=Date())->T7? {let a=all; return a.isEmpty ? nil : a[((day(date)%a.count)+a.count)%a.count] }
 static func season(_ date:Date=Date())->Int { let m=Calendar.current.component(.month,from:date); return m<3 || m==12 ? 1 : m<6 ? 2 : m<9 ? 3 : 4 }
 static func filter(_ a:[T7],_ text:String,_ category:String,_ pantry:Set<String>)->[T7] {
  a.filter { r in let hay=([r.n,r.sub]+r.ingredients.map(\.n)).joined(separator:" "); let words=text.split(whereSeparator:{$0.isWhitespace}); return (category=="all" || (category=="seasonal" ? r.seasons.contains(season()) : r.category==category)) && pantry.isSubset(of:Set(r.ingredients.map(\.id))) && words.allSatisfy{hay.localizedStandardContains(String($0))} }
 }
 static func shopping(_ selected:[String:Int],_ a:[T7])->[C8] { var sums:[String:C8]=[:]; for r in a { guard let count=selected[r.id],count>0 else {continue}; for item in r.ingredients { var v=item; v.amount *= Double(count)/Double(r.servings); if let old=sums[v.key] {v.amount += old.amount}; sums[v.key]=v } }; return sums.values.sorted{$0.n.localizedStandardCompare($1.n) == .orderedAscending} }
}
struct E5:Codable,Hashable { var value:String; var date:Date }
struct A6:Codable,Identifiable,Hashable {var id:String; var recipe:String; var date:Date; var servings:Int; var removed:Bool=false; var edited:Date=Date()}
struct B2:Codable,Equatable {
 var recipe:String; var began:Date; var end:Date; var held:Double?=nil
 var remaining:Double { max(0,held ?? end.timeIntervalSinceNow) }
 var running:Bool {held==nil && end>Date()}
}
struct J4:Codable {
 var marks:[String:E5]=[:]; var notes:[String:E5]=[:]; var plans:[String:A6]=[:]
 mutating func merge(_ x:J4) { for (k,v) in x.marks where v.date > (marks[k]?.date ?? .distantPast) {marks[k]=v}; for (k,v) in x.notes where v.date > (notes[k]?.date ?? .distantPast) {notes[k]=v}; for (k,v) in x.plans where v.edited > (plans[k]?.edited ?? .distantPast) {plans[k]=v} }
}
struct G7:Codable {
 var yields:[String:Int]=[:]; var cloud=J4(); var cart:[String:Int]=[:]; var checked:Set<String>=[]; var progress:[String:Int]=[:]; var timer:B2?=nil; var notifyTimer=false; var weekly=false; var seasonal=false; var cloudOn=false; var account:String?=nil; var reminderIDs:[String:String]=[:]
}
struct F3:ActivityAttributes {
 struct ContentState:Codable,Hashable {var end:Date; var start:Date; var paused:Double?}
 var title:String; var recipe:String
}
struct N4:Codable {
 var timer:B2?; var plan:[A6]; var shopping:[C8]
 static var empty:N4 {N4(timer:nil,plan:[],shopping:[])}
 static func read()->N4 {guard let b=UserDefaults(suiteName:p9group)?.data(forKey:"folio.tiles"),let n=try? JSONDecoder().decode(N4.self,from:b) else{return .empty};return n}
}
