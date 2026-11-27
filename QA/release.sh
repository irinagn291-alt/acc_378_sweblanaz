#!/bin/bash
set -euo pipefail
TASK_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer
xcodebuild -project "$TASK_ROOT/DessertBook.xcodeproj" -scheme DessertKitchen -configuration Release -destination 'generic/platform=iOS' -jobs 2 -derivedDataPath "$TASK_ROOT/Artifacts/DeviceCache" -archivePath "$TASK_ROOT/Artifacts/DessertBook.xcarchive" CODE_SIGNING_ALLOWED=NO 'OTHER_SWIFT_FLAGS=-debug-prefix-map $(SRCROOT)=.' archive > "$TASK_ROOT/QA/device-build.log" 2>&1
xcrun strip -S "$TASK_ROOT/Artifacts/DessertBook.xcarchive/Products/Applications/FolioKitchen.app/FolioKitchen"
xcrun strip -S "$TASK_ROOT/Artifacts/DessertBook.xcarchive/Products/Applications/FolioKitchen.app/PlugIns/KitchenPages.appex/KitchenPages"
python3 "$TASK_ROOT/QA/archive_audit.py"
