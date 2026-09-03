import os
import subprocess

print("Running Advanced Husky Quality Gate & Strict Labeling/Evidence Check...")

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

# Automatically prepend badge label to commit message if editing commit msg
commit_msg_path = ".git/COMMIT_EDITMSG"
if os.path.exists(commit_msg_path):
    with open(commit_msg_path, "r") as f:
        msg = f.read().strip()
    if msg and not msg.startswith("["):
        new_msg = f"{badge} {msg}"
        with open(commit_msg_path, "w") as f:
            f.write(new_msg)
        print(f"🏷️ Automatically prepended label to commit message: '{new_msg}'")

# 1. Static network check
if os.path.exists("server.js"):
    with open("server.js", "r") as f:
        content = f.read()
        if "0.0.0.0" not in content or "PORT" not in content:
            print("❌ CRITICAL LINT ERROR: server.js must bind to '0.0.0.0' and use process.env.PORT.")
            exit(1)
        else:
            print("✅ Static network check passed: server.js binds to 0.0.0.0 and PORT.")

# 2. Strict Before & After Screenshot Enforcement (Require BOTH before.png AND after.png)
if has_ui:
    print("🎨 UI Changes detected. Verifying BOTH before.png and after.png...")
    
    # Check staged files or working directory for before.png and after.png
    has_before = os.path.exists("before.png") or any("before" in f.lower() for f in staged_files)
    has_after = os.path.exists("after.png") or any("after" in f.lower() for f in staged_files)
    
    if not (has_before and has_after):
        print("❌ CRITICAL QUALITY GATE FAILURE: UI changes STRICTLY require BOTH 'before.png' AND 'after.png' images to be provided. Only 1 or 0 found.")
        exit(1)
    else:
        print("📸 Both 'before.png' and 'after.png' evidence verified successfully!")

print(f"🎉 Quality Gate passed with tag {badge}!")
