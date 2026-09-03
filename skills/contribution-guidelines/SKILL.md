---
name: contribution-guidelines
description: "Enforce programmatic PR title and description format."
version: 0.3.0
author: Saidmuhammad (saidmuhammad1), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [contribution, pr, guidelines, pre-push, validation]
    related_skills: [requesting-code-review]
---

# Contribution Guidelines & PR Description Skill

Strict workflow rule: **When creating a Pull Request**, the AI agent MUST programmatically set the PR title and description directly using `gh pr create --title "<title>" --body "<body_content>"` (or update via `gh pr edit`), adhering strictly to the required structure below.

## Mandatory PR Description Structure

Every PR must be created with:
1. **Title**: Clear, descriptive title following conventional commits (`feat: ...`, `fix: ...`).
2. **Summary of Changes**: High-level objective.
3. **What Changed**: Specific file and logic modifications.
4. **Browser Testing & Checkpoints**: Verification steps and test results.
5. **App Preview**: Screenshot image (`screenshot.png`).

## Canonical Command

```bash
gh pr create --title "feat: <description>" --body "## Summary of Changes
- ...

### What Changed
- ...

### Browser Testing & Checkpoints
- [x] Tested in Chromium
- [x] Automated pre-push check passed

### App Preview
<img src=\"https://raw.githubusercontent.com/saidmuhammad1/proj1/<branch>/screenshot.png\" alt=\"App Screenshot\" width=\"600\"/>"
```
