#!/bin/bash
set -u
TASK_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer
if [ -f "$TASK_ROOT/QA/ipad-exit-code.txt" ] && [ -f "$TASK_ROOT/QA/iphone-exit-code.txt" ]; then
  exit "$(cat "$TASK_ROOT/QA/ipad-exit-code.txt")"
fi
xcrun simctl boot "$GF_SIMULATOR_UDID" 2>/dev/null || true
xcrun simctl bootstatus "$GF_SIMULATOR_UDID" -b
FOLIO_ATTEMPT=1
while true; do
  xcodebuild -project "$TASK_ROOT/DessertBook.xcodeproj" -scheme DessertKitchen -configuration Debug -destination "id=$GF_SIMULATOR_UDID" -parallel-testing-enabled NO -jobs 2 -derivedDataPath "$TASK_ROOT/Artifacts/TestCompilerCache" -resultBundlePath "$TASK_ROOT/QA/iPad.xcresult" -only-testing:KitchenJourney/V8Journey/testKitchenFlowAndPersistence CODE_SIGNING_ALLOWED=NO ARCHS=arm64 test > "$TASK_ROOT/QA/ipad-tests.log" 2>&1
  TASK_RESULT=$?
  if [ "$TASK_RESULT" = "0" ] || [ "$FOLIO_ATTEMPT" -ge "3" ]; then break; fi
  mkdir -p "$TASK_ROOT/QA/iPad-attachments"
  xcrun xcresulttool export attachments --path "$TASK_ROOT/QA/iPad.xcresult" --output-path "$TASK_ROOT/QA/iPad-attachments" > "$TASK_ROOT/QA/ipad-failed-export.log" 2>&1 || true
  printf '%s\n' "$TASK_RESULT" > "$TASK_ROOT/QA/ipad-needs-review.txt"
  FOLIO_WAIT=0
  while [ ! -f "$TASK_ROOT/QA/ipad-rerun.request" ] && [ "$FOLIO_WAIT" -lt "600" ]; do
    sleep 2
    FOLIO_WAIT=$((FOLIO_WAIT + 2))
  done
  if [ ! -f "$TASK_ROOT/QA/ipad-rerun.request" ]; then break; fi
  rm -f "$TASK_ROOT/QA/ipad-rerun.request"
  mv "$TASK_ROOT/QA/iPad.xcresult" "$TASK_ROOT/QA/iPad-attempt-$FOLIO_ATTEMPT.xcresult"
  cp "$TASK_ROOT/QA/ipad-tests.log" "$TASK_ROOT/QA/ipad-attempt-$FOLIO_ATTEMPT.log"
  FOLIO_ATTEMPT=$((FOLIO_ATTEMPT + 1))
done
rm -f "$TASK_ROOT/QA/ipad-needs-review.txt"
mkdir -p "$TASK_ROOT/QA/iPad-attachments"
xcrun xcresulttool export attachments --path "$TASK_ROOT/QA/iPad.xcresult" --output-path "$TASK_ROOT/QA/iPad-attachments" > "$TASK_ROOT/QA/ipad-export.log" 2>&1 || true
xcrun simctl terminate "$GF_SIMULATOR_UDID" com.dessertbook.app 2>/dev/null || true
xcrun simctl launch "$GF_SIMULATOR_UDID" com.dessertbook.app -AppleLanguages '(en)' -AppleLocale en_US > "$TASK_ROOT/QA/ipad-launch.log" 2>&1 || true
xcrun simctl io "$GF_SIMULATOR_UDID" screenshot "$TASK_ROOT/QA/iPad-final.png" || true
printf '%s\n' "$TASK_RESULT" > "$TASK_ROOT/QA/ipad-exit-code.txt"
if [ "${FOLIO_QA_CHAINED:-0}" != "1" ] && [ ! -f "$TASK_ROOT/QA/iphone-exit-code.txt" ]; then
  xcrun simctl shutdown "$GF_SIMULATOR_UDID" 2>/dev/null || true
  FACTORY_ROOT="${GF_FACTORY_ROOT:-$(cd "$TASK_ROOT/../../../.." && pwd)}"
  FOLIO_NEXT_TEMPLATE="$(python3 "$TASK_ROOT/QA/choose_template.py" "$FACTORY_ROOT" iPhone)"
  FOLIO_QA_CHAINED=1 python3 "$FACTORY_ROOT/gf/genesis/simulator_pool.py" "$FOLIO_NEXT_TEMPLATE" bash "$TASK_ROOT/QA/phone_qa.sh" >> "$TASK_ROOT/QA/chained-pool.log" 2>&1
  FOLIO_OTHER_RESULT=$?
  if [ "$TASK_RESULT" = "0" ]; then TASK_RESULT=$FOLIO_OTHER_RESULT; fi
fi
exit "$TASK_RESULT"
