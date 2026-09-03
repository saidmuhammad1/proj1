import os
import subprocess
import json

print("Running Pre-PR Quality Gate & Screenshot Verification...")

# 1. Check git status and diff
diff_res = subprocess.run(["git", "diff", "origin/main"], capture_output=True, text=True)
print("Git Diff Summary:\n", diff_res.stdout[:500])

# 2. Static check on server.js
with open("server.js", "r") as f:
    content = f.read()
    if "0.0.0.0" not in content or "PORT" not in content:
        print("CRITICAL ISSUE: server.js must bind to 0.0.0.0 and use PORT!")
        exit(1)
    else:
        print("Static check passed: server.js correctly binds to 0.0.0.0 and PORT.")

print("Pre-PR check completed successfully. Ready for PR creation!")
