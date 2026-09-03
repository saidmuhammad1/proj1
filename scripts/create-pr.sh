#!/bin/bash
set -e
echo "=== Strict Pre-PR Validation Gate ==="
python3 scripts/pre-pr-check.py

if [ ! -f "PR_DESCRIPTION.md" ]; then
    echo "❌ Error: PR_DESCRIPTION.md is required to create a PR per contribution guidelines."
    exit 1
fi

TITLE="${1:-feat: new update following contribution guidelines}"

echo "✅ Validation passed. Creating Pull Request..."
gh pr create --title "$TITLE" --body-file PR_DESCRIPTION.md
echo "=== Pull Request Created Successfully! ==="
