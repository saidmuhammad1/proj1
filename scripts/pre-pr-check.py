import os
import subprocess

print("🛡️ Running Strict Quality Gate & Evidence Validation...")

staged_files = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True).stdout.splitlines()

has_ui = any(f.endswith(('.html', '.css', '.svg', '.jsx', '.tsx')) for f in staged_files)
has_logic = any(f.endswith(('.js', '.ts', '.json')) for f in staged_files)

badge = "[Chore]"
if has_ui and has_logic:
    badge = "[Full Stack Update]"
elif has_ui:
    badge = "[UI Update]"
elif has_logic:
    badge = "[Logic Update]"

print(f"📌 Change Classification: {badge}")

# 1. Static Network Check
if os.path.exists("server.js"):
    with open("server.js", "r") as f:
        content = f.read()
        if "0.0.0.0" not in content or "PORT" not in content:
            print("❌ CRITICAL LINT ERROR: server.js must bind to '0.0.0.0' and use process.env.PORT.")
            exit(1)

# 2. Strict Before & After Screenshot Enforcement for UI Changes (MANDATORY 2 IMAGES)
if has_ui:
    print("🎨 UI Modifications detected in commit/push.")
    
    before_exists = os.path.exists("before.png") and os.path.getsize("before.png") > 0
    after_exists = os.path.exists("after.png") and os.path.getsize("after.png") > 0
    
    if not (before_exists and after_exists):
        print("\n" + "="*70)
        print("❌ CRITICAL QUALITY GATE FAILURE: UI CHANGES STRICTLY REQUIRE 2 VALID IMAGES!")
        print("="*70)
        print("You must provide both 'before.png' and 'after.png' with valid image data:")
        if not before_exists:
            print("  • ❌ before.png (Missing or empty)")
        else:
            print("  • ✅ before.png (Verified)")
        if not after_exists:
            print("  • ❌ after.png (Missing or empty)")
        else:
            print("  • ✅ after.png (Verified)")
        print("\nPlease ensure both before.png and after.png are placed in the root")
        print("and staged via 'git add before.png after.png' before committing or pushing.")
        print("="*70 + "\n")
        exit(1)
    else:
        print("📸 Verified: Both 'before.png' and 'after.png' are present and valid.")

print(f"✅ Quality Gate Passed successfully for {badge}!")
