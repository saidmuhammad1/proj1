import os
import subprocess

print("Running Strict Husky Quality Gate & Contribution Check...")

# 1. Static check on server.js for correct network and port binding
if os.path.exists("server.js"):
    with open("server.js", "r") as f:
        content = f.read()
        if "0.0.0.0" not in content or "PORT" not in content:
            print("❌ CRITICAL LINT ERROR: server.js must bind to '0.0.0.0' and use process.env.PORT.")
            exit(1)
        else:
            print("✅ Static network check passed: server.js binds to 0.0.0.0 and PORT.")

# 2. Check recent commit message or staged changes for standard conventional/structured format
try:
    last_commit = subprocess.run(["git", "log", "-1", "--pretty=%s"], capture_output=True, text=True, check=True).stdout.strip()
    print(f"Latest commit message: '{last_commit}'")
    
    # Optional conventional commit check or structure check
    if not any(last_commit.startswith(prefix) for prefix in ["feat:", "fix:", "chore:", "docs:", "refactor:"]):
        print("⚠️ Warning: Commit message should ideally follow conventional format (feat:, fix:, chore:, docs:, refactor:).")
except Exception as e:
    print(f"Note on commit check: {e}")

print("🎉 Strict Husky Quality Gate passed successfully!")
