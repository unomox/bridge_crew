#!/usr/bin/env bash
set -euo pipefail

echo "Running markdownlint..."
markdownlint "**/*.md" "!node_modules/**" || true

echo "Running yamllint..."
yamllint . || true

echo "Running hadolint..."
if command -v hadolint >/dev/null 2>&1; then
  find . -type f \( -iname "Dockerfile" -o -name "*Dockerfile*" -o -name "Dockerfile.*" \) -print0 | \
    xargs -0 -r -I{} sh -c 'echo "Linting {}"; hadolint "{}" || true'
fi

echo "Running actionlint..."
if command -v actionlint >/dev/null 2>&1; then
  actionlint || true
fi

echo "Linting complete"

