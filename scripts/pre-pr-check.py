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

# 2. Strict Before & After Screenshot Enforcement for UI Changes
if has_ui:
    print("🎨 UI Modifications detected in commit/push.")
    has_before = os.path.exists("before.png")
    has_after = os.path.exists("after.png")
    
    if not (has_before and has_after):
        print("\n" + "="*70)
        print("❌ QUALITY GATE BLOCKED: UI CHANGES REQUIRE BEFORE & AFTER EVIDENCE!")
        print("="*70)
        print("Missing required screenshot files in the repository root:")
        if not has_before:
            print("  • ❌ before.png (Missing)")
        else:
            print("  • ✅ before.png (Found)")
        if not has_after:
            print("  • ❌ after.png (Missing)")
        else:
            print("  • ✅ after.png (Found)")
        print("\nPlease place both 'before.png' and 'after.png' in the root directory")
        print("and run 'git add before.png after.png' before committing or pushing.")
        print("="*70 + "\n")
        exit(1)
    else:
        print("📸 Verified: Both 'before.png' and 'after.png' are present.")

print(f"✅ Quality Gate Passed successfully for {badge}!")
