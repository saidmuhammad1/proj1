import os
import subprocess
import time
import urllib.request

print("🛡️ [Husky AI QA & Puppeteer Test Gate] Starting real application execution & screenshot test...")

# 1. Static Network & Port Binding Check
if os.path.exists("server.js"):
    with open("server.js", "r") as f:
        content = f.read()
        if "0.0.0.0" not in content or "PORT" not in content:
            print("❌ CRITICAL LINT ERROR: server.js must bind to '0.0.0.0' and use process.env.PORT.")
            exit(1)
        else:
            print("✅ Static network check passed: server.js binds to 0.0.0.0 and PORT.")

# 2. Real Application Execution & Automated Puppeteer Screenshot Test
print("🚀 Launching local Express test server...")
server_proc = subprocess.Popen(["node", "server.js"], env={**os.environ, "PORT": "3002"})

# Wait for server readiness
server_ready = False
for _ in range(10):
    try:
        with urllib.request.urlopen("http://localhost:3002/api/status") as resp:
            if resp.status == 200:
                server_ready = True
                break
    except Exception:
        time.sleep(0.5)

if not server_ready:
    print("❌ CRITICAL QA FAILURE: Local Express server failed to start or respond on port 3002.")
    server_proc.terminate()
    exit(1)

print("✅ Local server running successfully on port 3002. Running Puppeteer visual verification...")

# Run Puppeteer screenshot capture script
puppeteer_test_script = """
import puppeteer from 'puppeteer';

(async () => {
    try {
        const browser = await puppeteer.launch({
            headless: true,
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        const page = await browser.newPage();
        await page.setViewport({ width: 1280, height: 800 });
        await page.goto('http://localhost:3002', { waitUntil: 'networkidle0' });
        await page.screenshot({ path: 'after.png', fullPage: true });
        await browser.close();
        console.log('REAL_PUPPETEER_SUCCESS');
    } catch (err) {
        console.error('Puppeteer error:', err);
        process.exit(1);
    }
})();
"""

test_js_path = "scripts/run-puppeteer.mjs"
with open(test_js_path, "w") as f:
    f.write(puppeteer_test_script)

test_res = subprocess.run(["node", test_js_path], capture_output=True, text=True)
server_proc.terminate()

if test_res.returncode != 0 or "REAL_PUPPETEER_SUCCESS" not in test_res.stdout:
    print("❌ CRITICAL QA FAILURE: Puppeteer failed to capture live screenshot.")
    print("Stderr:", test_res.stderr)
    exit(1)

print("📸 Real application screenshot successfully captured via Puppeteer (`after.png`)!")
print("🎉 Strict Husky QA Gate passed successfully!")
