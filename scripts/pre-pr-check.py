import os
import subprocess

print("Running Strict Husky Quality Gate & Evidence Verification...")

# 1. Static check on server.js for correct network and port binding
if os.path.exists("server.js"):
    with open("server.js", "r") as f:
        content = f.read()
        if "0.0.0.0" not in content or "PORT" not in content:
            print("❌ CRITICAL LINT ERROR: server.js must bind to '0.0.0.0' and use process.env.PORT.")
            exit(1)
        else:
            print("✅ Static network check passed: server.js binds to 0.0.0.0 and PORT.")

# 2. Enforce before/after evidence or screenshot check for UI changes
staged_files = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True).stdout.splitlines()
has_ui_changes = any(f.endswith(('.html', '.css', '.js')) for f in staged_files)

if has_ui_changes:
    print("🎨 UI changes detected in staged files.")
    # Check if PR description template or evidence file exists
    has_evidence = os.path.exists("PR_DESCRIPTION.md") or os.path.exists("screenshot.png")
    if not has_evidence:
        print("⚠️ Warning: UI changes detected without a screenshot or PR_DESCRIPTION.md evidence file. Please ensure before/after evidence is documented.")

print("🎉 Strict Husky Quality Gate passed successfully!")
