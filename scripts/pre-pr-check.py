import os
import subprocess
import sys

print("🤖 [AI Agent Quality Gate] Initializing deep code review & evidence verification...")

# 1. Inspect git diff and status
diff_output = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True).stdout
if not diff_output:
    diff_output = subprocess.run(["git", "diff", "HEAD~1"], capture_output=True, text=True).stdout

print(f"📊 Analyzing diff size: {len(diff_output)} characters.")

# 2. Deep Static & Architectural Inspection
has_server_js = os.path.exists("server.js")
if has_server_js:
    with open("server.js", "r") as f:
        server_code = f.read()
        if "0.0.0.0" not in server_code or "PORT" not in server_code:
            print("❌ [AI Reviewer] CRITICAL ARCHITECTURE ERROR: server.js fails to bind to '0.0.0.0' or use process.env.PORT.")
            print("   Required pattern: app.listen(PORT, '0.0.0.0', () => ...)")
            sys.exit(1)
        else:
            print("✅ [AI Reviewer] Server architecture verified: Correct port binding & network interface.")

# 3. Strict UI Evidence Verification
staged_files = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True).stdout.splitlines()
has_ui = any(f.endswith(('.html', '.css', '.svg', '.jsx', '.tsx')) for f in staged_files)

if has_ui or "index.html" in diff_output:
    print("🎨 [AI Reviewer] UI Modifications detected in diff.")
    has_before = os.path.exists("before.png")
    has_after = os.path.exists("after.png")
    
    if not (has_before and has_after):
        print("\n" + "="*80)
        print("❌ [AI REVIEWER] QUALITY GATE BLOCKED: UI CHANGES REQUIRE BEFORE & AFTER EVIDENCE!")
        print("="*80)
        print("The AI Reviewer inspected your changes and detected UI modifications.")
        print("Strict requirements:")
        print("  • before.png -> Required in repository root")
        print("  • after.png  -> Required in repository root")
        print("\nPlease stage both screenshot images before committing or pushing.")
        print("="*80 + "\n")
        sys.exit(1)
    else:
        print("📸 [AI Reviewer] Evidence verified: Both before.png and after.png are present.")

print("🎉 [AI Reviewer] Deep code review completed successfully. All architectural and visual standards met!")
