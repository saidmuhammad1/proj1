import os
import subprocess
import sys

print("🛡️ Running Strict Lifecycle Quality Gate & Evidence Validation...")

# 1. Verify Git Diff is Non-Empty (Ensure changes actually happened)
diff_check = subprocess.run(["git", "diff", "--stat"], capture_output=True, text=True)
staged_check = subprocess.run(["git", "diff", "--cached", "--stat"], capture_output=True, text=True)

if not diff_check.stdout.strip() and not staged_check.stdout.strip():
    print("❌ ERROR: Quality gate failed! No code or UI changes detected in the workspace.")
    print("   Workflow order: 1) Take Before Snapshot -> 2) Make Changes -> 3) Take After Snapshot -> 4) Commit & PR.")
    sys.exit(1)

print("✅ Verified: Code/UI changes detected in diff.")

# 2. Strict Before & After Evidence Verification
has_before = os.path.exists("before.png") and os.path.getsize("before.png") > 0
has_after = os.path.exists("after.png") and os.path.getsize("after.png") > 0

if not (has_before and has_after):
    print("❌ ERROR: Strict Evidence Failure! UI changes require both 'before.png' (pre-change) and 'after.png' (post-change).")
    if not has_before:
        print("   • missing 'before.png' captured before code edits.")
    if not has_after:
        print("   • missing 'after.png' captured after code edits.")
    sys.exit(1)

print("✅ Verified: Both 'before.png' and 'after.png' evidence snapshots are present.")

# 3. Static Server Binding Check
if os.path.exists("server.js"):
    with open("server.js", "r") as f:
        content = f.read()
        if "0.0.0.0" not in content or "PORT" not in content:
            print("❌ CRITICAL LINT ERROR: server.js must bind to '0.0.0.0' and use process.env.PORT.")
            sys.exit(1)

# 4. PR Description Validation
if not os.path.exists("PR_DESCRIPTION.md"):
    print("❌ ERROR: PR_DESCRIPTION.md is missing!")
    sys.exit(1)

with open("PR_DESCRIPTION.md", "r") as f:
    pr_text = f.read().lower()

if "before.png" not in pr_text or "after.png" not in pr_text:
    print("❌ ERROR: PR_DESCRIPTION.md must reference both before.png and after.png!")
    sys.exit(1)

print("=== 🎉 Strict Lifecycle Quality Gate Passed Successfully! ===")
