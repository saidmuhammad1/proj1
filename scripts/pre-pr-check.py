import os
import subprocess

print("Running Advanced Husky Quality Gate & Strict Before/After Check...")

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

# 1. Static network check
if os.path.exists("server.js"):
    with open("server.js", "r") as f:
        content = f.read()
        if "0.0.0.0" not in content or "PORT" not in content:
            print("❌ CRITICAL LINT ERROR: server.js must bind to '0.0.0.0' and use process.env.PORT.")
            exit(1)
        else:
            print("✅ Static network check passed: server.js binds to 0.0.0.0 and PORT.")

# 2. Strict Before & After Screenshot Enforcement for UI Changes (Requires 2 images: before.png and after.png)
if has_ui:
    print("🎨 UI Changes detected. Verifying Before & After screenshot evidence...")
    
    has_before = os.path.exists("before.png") or any("before" in f.lower() and f.endswith(('.png', '.jpg', '.jpeg')) for f in staged_files)
    has_after = os.path.exists("after.png") or any("after" in f.lower() and f.endswith(('.png', '.jpg', '.jpeg')) for f in staged_files)
    
    if not (has_before and has_after):
        print("❌ CRITICAL QUALITY GATE FAILURE: UI changes require BOTH 'before.png' and 'after.png' screenshot images to be staged/provided.")
        exit(1)
    else:
        print("📸 Both 'before.png' and 'after.png' evidence verified successfully!")

print(f"🎉 Quality Gate passed with tag {badge}!")
