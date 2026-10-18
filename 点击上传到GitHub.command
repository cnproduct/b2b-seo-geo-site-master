#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

REPO="cnproduct/b2b-seo-geo-site-master"
DESC="面向海外询盘获取（RFQ）的 B2B 独立站 SEO + GEO 全链路建站与增长总控 Skill (V3.2)"

echo "=========================================================="
echo "  正在为您创建并推送 https://github.com/${REPO}"
echo "=========================================================="

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

echo "1. 检查 GitHub CLI (gh) 登录状态..."
gh auth status

echo "2. 在 github.com/cnproduct 下创建仓库 b2b-seo-geo-site-master..."
if ! gh repo view "${REPO}" >/dev/null 2>&1; then
  gh repo create "${REPO}" --public --description "${DESC}"
else
  echo "   仓库已存在，直接准备推送更新..."
fi

echo "3. 推送本地 main 分支代码到 GitHub..."
git remote set-url origin "https://github.com/${REPO}.git" 2>/dev/null || git remote add origin "https://github.com/${REPO}.git"
git push -u origin main

echo ""
echo "✅ 推送成功！现在可以在浏览器打开："
echo "   https://github.com/${REPO}"
open "https://github.com/${REPO}" 2>/dev/null || true
