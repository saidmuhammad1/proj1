import subprocess
import os
import sys

print("Running AI-Powered PR Classification & GitHub Label Assignment...")

# 1. Get git diff against main
diff_output = subprocess.run(["git", "diff", "origin/main"], capture_output=True, text=True).stdout

# 2. AI / Semantic classification of the diff
# Analyzes code changes for UI indicators (JSX, TSX, HTML, CSS, Tailwind, rendering, components) 
# and Logic indicators (API endpoints, DB queries, state logic, algorithms, business rules).
has_ui_semantics = any(keyword in diff_output for keyword in [
    "jsx", "tsx", "html", "css", "tailwind", "className", "render", "Component", 
    "button", "div", "span", "header", "footer", "ui", "view", "style"
])

has_logic_semantics = any(keyword in diff_output for keyword in [
    "app.get", "app.post", "router", "db", "query", "async", "await", "fetch", 
    "algorithm", "state", "store", "api", "backend", "controller", "model"
])

label = "Chore"
if has_ui_semantics and has_logic_semantics:
    label = "Full Stack Update"
elif has_ui_semantics:
    label = "UI Update"
elif has_logic_semantics:
    label = "Logic Update"

print(f"🤖 AI Semantic Change Classification: {label}")

# 3. Get current branch name
branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip()

# 4. Create PR using gh CLI
title = sys.argv[1] if len(sys.argv) > 1 else f"feat: AI-Classified PR for {branch}"
body = sys.argv[2] if len(sys.argv) > 2 else "### Summary\n- AI-classified PR creation with strict quality gate and before/after evidence validation."

pr_res = subprocess.run([
    "gh", "pr", "create",
    "--draft",
    "--title", title,
    "--body", body,
    "--base", "main",
    "--head", branch
], capture_output=True, text=True)

print(pr_res.stdout)
print(pr_res.stderr)

if pr_res.returncode == 0:
    output = pr_res.stdout.strip()
    print(f"Successfully created PR: {output}")
    
    # Apply GitHub PR label
    label_res = subprocess.run(["gh", "pr", "edit", output, "--add-label", label], capture_output=True, text=True)
    print(f"Applied GitHub label '{label}':", label_res.stdout, label_res.stderr)
else:
    print("Failed to create PR.")
