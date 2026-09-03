---
name: contribution-guidelines
description: "Enforce strict pre-PR lifecycle: before snapshot, changes, after snapshot, PR."
version: 0.5.0
author: Saidmuhammad (saidmuhammad1), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [contribution, pr, guidelines, lifecycle, screenshots]
    related_skills: [requesting-code-review]
---

# Strict Contribution Guidelines & Lifecycle Skill

Strict workflow rule for all changes and pull requests:
1. **Before Snapshot**: Capture `before.png` of the running application *before* any code or UI modifications are made.
2. **Code Changes**: Apply the requested code or UI changes.
3. **Diff Verification**: Verify `git diff` is non-empty. If no changes exist, fail immediately.
4. **After Snapshot**: Capture `after.png` of the running application *after* code and UI modifications are completed.
5. **PR Description**: Write `PR_DESCRIPTION.md` embedding both `before.png` and `after.png`.
6. **Quality Gate & PR**: Run `python3 scripts/pre-pr-check.py` and `npm run pr`.
