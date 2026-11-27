Implementation notes · 15 November 2026

The product has one app target, a required WidgetKit extension, and two development-only test targets. WidgetKit requires an extension; the one-app-target rule therefore does not remove that extension. Shared models and ActivityAttributes are compiled into both products. [Apple: Creating a widget extension](https://developer.apple.com/documentation/widgetkit/creating-a-widget-extension).

Timers use persisted absolute deadlines and system Text(timerInterval:countsDown:). ActivityKit does not use push updates. Timer selection is capped at six hours; a Live Activity has an Apple-imposed active lifetime of up to eight hours, which pausing does not extend. Local timer state persists after the system ends an Activity. WidgetKit decides the precise delivery time of timeline entries; the countdown itself does not require per-second reloads. [Apple: Live Activities](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities), [Apple: Timeline](https://developer.apple.com/documentation/widgetkit/timeline).

Deployment starts at iOS 17.4. Reminders export uses requestFullAccessToReminders, NSRemindersFullAccessUsageDescription and the requested legacy fallback key. Both permission descriptions are localized in InfoPlist.xcstrings. [Apple: Accessing the event store](https://developer.apple.com/documentation/eventkit/accessing-the-event-store).

CloudKit uses container iCloud.com.dessertbook.app and its user-private database. The FolioEnvelope record has a payload Bytes field; deploy this schema to Production when preparing distribution. Notes, favorite markers and plan entries carry edit timestamps; deletions remain as tombstones. Server-record conflicts merge and retry up to three times. Payload is limited to 900 KB with an explicit local-saving message above that limit. Private database storage counts against the user’s iCloud quota; quota failures receive specific instructions. No recipe API is used. [Apple: privateCloudDatabase](https://developer.apple.com/documentation/cloudkit/ckcontainer/privateclouddatabase), [Apple: quotaExceeded](https://developer.apple.com/documentation/cloudkit/ckerror/quotaexceeded).

App Group group.com.dessertbook.app shares only this product’s widget state. Its UserDefaults privacy reason is 1C8F.1. Push entitlement and remote-notification background mode are declared as required by the brief; there is no APNs server or registration-dependent feature. All alerts are local. [Apple: Required reason API](https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacyaccessedapitypes/nsprivacyaccessedapitype).

The honey age note was checked against [CDC prevention guidance](https://www.cdc.gov/botulism/prevention/). Recipes were authored for this product; no published cookbook text was copied. Serving pictures are generated illustrations. Software QA does not constitute a physical kitchen test.

Build with the shared DessertKitchen scheme. QA/release.sh creates the unsigned archive, removes debug symbol-table paths using Apple strip -S and runs the full archive audit. QA/phone_qa.sh or QA/ipad_qa.sh must run under the factory simulator_pool helper. They reuse completed results; move the corresponding xcresult and exit-code files before a fresh run. Set GF_FACTORY_ROOT when the project is outside its original factory layout. No named simulator is required.

Source brief SHA-256: c407e5e64754fcb46c858cfbdba4df4c192f1e33c52ade6141232a6e8c03dbf0

Canonical README SHA-256: f0134d4bc1eab47d1b8d3e37be06fc510be0744a7dc17b95e258885e08ef7e93
