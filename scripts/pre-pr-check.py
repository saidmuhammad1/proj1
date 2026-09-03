import os
import subprocess

print("Running Advanced Husky Quality Gate & Classification...")

# Get staged files
staged_files = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True).stdout.splitlines()

has_ui = any(f.endswith(('.html', '.css', '.svg')) for f in staged_files)
has_logic = any(f.endswith(('.js', '.ts', '.json')) for f in staged_files)

badge = ""
if has_ui and has_logic:
    badge = "[Full Stack Update]"
elif has_ui:
    badge = "[UI Update]"
elif has_logic:
    badge = "[Logic Update]"
else:
    badge = "[Chore]"

print(f"Detected Change Classification: {badge}")

# 1. Static check on server.js for correct network and port binding
if os.path.exists("server.js"):
    with open("server.js", "r") as f:
        content = f.read()
        if "0.0.0.0" not in content or "PORT" not in content:
            print("❌ CRITICAL LINT ERROR: server.js must bind to '0.0.0.0' and use process.env.PORT.")
            exit(1)
        else:
            print("✅ Static network check passed: server.js binds to 0.0.0.0 and PORT.")

# 2. Strict Before/After Screenshot Enforcement for UI Changes
if has_ui:
    print("🎨 UI Changes detected.")
    # Check for screenshot image evidence
    has_screenshot = os.path.exists("screenshot.png") or any(f.endswith(('.png', '.jpg', '.jpeg')) for f in staged_files)
    if not has_screenshot:
        print("❌ CRITICAL QUALITY GATE FAILURE: UI changes require before/after screenshot images (e.g., screenshot.png) to be attached/staged before proceeding.")
        exit(1)
    else:
        print("📸 Screenshot evidence verified successfully for UI changes.")

print(f"🎉 Quality Gate passed with tag {badge}!")
