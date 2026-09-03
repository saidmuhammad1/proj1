import subprocess
import os
import sys

print("Running Automated PR Creator with GitHub Label Assignment...")

# 1. Determine change type from git diff against main
diff_files = subprocess.run(["git", "diff", "--name-only", "origin/main"], capture_output=True, text=True).stdout.splitlines()

has_ui = any(f.endswith(('.html', '.css', '.svg')) for f in diff_files)
has_logic = any(f.endswith(('.js', '.ts', '.json')) for f in diff_files)

label = "Chore"
if has_ui and has_logic:
    label = "Full Stack Update"
elif has_ui:
    label = "UI Update"
elif has_logic:
    label = "Logic Update"

print(f"Assigned GitHub PR Label: {label}")

# 2. Get current branch name
branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip()

# 3. Create PR using gh CLI
title = sys.argv[1] if len(sys.argv) > 1 else f"feat: Automated PR for {branch}"
body = sys.argv[2] if len(sys.argv) > 2 else "### Summary\n- Automated PR creation with quality gate validation."

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
    # Extract PR number or URL and add label
    output = pr_res.stdout.strip()
    print(f"Successfully created PR: {output}")
    
    # Apply GitHub PR label
    label_res = subprocess.run(["gh", "pr", "edit", output, "--add-label", label], capture_output=True, text=True)
    print(f"Applied GitHub label '{label}':", label_res.stdout, label_res.stderr)
else:
    print("Failed to create PR.")
