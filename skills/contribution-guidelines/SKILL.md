---
name: contribution-guidelines
description: Enforce structured PR descriptions with summaries, changes, and screenshots.
version: 0.1.0
author: Saidmuhammad (saidmuhammad1), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [contribution, pr, guidelines, screenshots]
    related_skills: []
---

# Contribution Guidelines Skill

Enforce a standardized PR structure across all contributions to ensure high quality, thorough testing, and clear visual evidence.

## When to Use

- When opening or reviewing a pull request in `proj1`.
- When verifying pre-PR quality gates and visual UI states.

## PR Structure Requirements

Every pull request must include:

1. **Summary of Changes**: High-level overview of what problem was solved and why.
2. **What Changed**: Bulleted list of modified files, features added, or bugs fixed.
3. **Before & After / Visual Attachments**: Screenshots or UI recordings proving the feature works as intended and matches design requirements.
4. **Browser & Environment Testing**: Verification checkpoints across different browsers (Chromium, Firefox, Safari) and screen sizes (desktop/mobile).
5. **Quality Gate Checkpoints**: Confirmation that all tests passed and no regression was introduced.

## PR Description Template

```markdown
## Pull Request Title

### Summary of Changes
- Concise summary of the objective.

### What Changed
- File or feature A modified.
- File or feature B added.

### Browser Testing & Verification
- [x] Verified in Chromium (Desktop)
- [x] Verified responsive layouts
- [x] Automated tests passing

### App Preview / Attachments
<img src="https://raw.githubusercontent.com/saidmuhammad1/proj1/<branch>/screenshot.png" alt="App Screenshot" width="600"/>
```

## Verification

- Ensure every PR meets all 5 checklist points before merging.
