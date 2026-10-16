#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

REPO="cnproduct/b2b-seo-geo-site-master"
DESC="面向海外询盘获取（RFQ）的 B2B 独立站 SEO + GEO 全链路建站与增长 Skill (V3.0)"

echo "==> Checking GitHub CLI authentication..."
gh auth status

echo "==> Creating repository https://github.com/${REPO} (if not already created)..."
if ! gh repo view "${REPO}" >/dev/null 2>&1; then
  gh repo create "${REPO}" --public --description "${DESC}"
fi

echo "==> Pushing main branch to https://github.com/${REPO}..."
git remote set-url origin "https://github.com/${REPO}.git" 2>/dev/null || git remote add origin "https://github.com/${REPO}.git"
git push -u origin main

echo "==> Done! Repository is live at: https://github.com/${REPO}"
