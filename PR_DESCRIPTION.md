## Pull Request: Strict Lifecycle & Evidence Enforcement

### Summary of Changes
- Enforced strict pre-change `before.png` -> code edits -> diff check -> `after.png` lifecycle workflow.
- Updated pre-pr validation scripts and gitignore rules.

### What Changed
- `scripts/pre-pr-check.py`: Enforces non-empty diff and mandatory before/after snapshots.
- `.gitignore`: Ignored binary image cache files.

### Browser Testing & Checkpoints
- [x] Verified in Chromium
- [x] Strict lifecycle quality gate passed

### App Preview / Before & After Images

**Before:**
<img src="https://raw.githubusercontent.com/saidmuhammad1/proj1/main/before.png" alt="Before" width="600"/>

**After:**
<img src="https://raw.githubusercontent.com/saidmuhammad1/proj1/main/after.png" alt="After" width="600"/>
