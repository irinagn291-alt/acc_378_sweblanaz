import SwiftUI
@main struct A7Folio:App {
 @StateObject private var q=Z6();@Environment(\.scenePhase) private var phase
 var body:some Scene {WindowGroup{U2().environmentObject(q).preferredColorScheme(.light).task{await q.foreground()}.onChange(of:phase){_,p in if p == .active {Task{await q.foreground()}}}}}
}
