#!/usr/bin/env bash
set -uo pipefail

cd "$(dirname "$0")"
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

REPO_OWNER="cnproduct"
REPO_NAME="b2b-seo-geo-site-master"
REPO="${REPO_OWNER}/${REPO_NAME}"
DESC="面向海外询盘获取（RFQ）的 B2B 独立站 SEO + GEO 全链路建站与增长总控 Skill (V3.2)"

echo "=========================================================="
echo "  正在为您创建并推送 https://github.com/${REPO}"
echo "=========================================================="
echo ""

TOKEN="${GH_TOKEN:-${GITHUB_TOKEN:-}}"

if [ -z "${TOKEN}" ]; then
  if gh auth status -h github.com >/dev/null 2>&1; then
    echo "✅ 检测到本机 GitHub CLI 已处于有效登录状态。"
    TOKEN="$(gh auth token -h github.com 2>/dev/null || true)"
  else
    echo "⚠️  检测到本机钥匙串 (Keyring) 中的旧 GitHub 凭证已过期失效。"
    echo ""
    echo "请选择认证方式："
    echo "  • 直接粘贴您的 GitHub Token (github_pat_... 或 ghp_...) 后按回车；"
    echo "  • 或者不输入内容、直接按回车键，将自动打开浏览器进行 GitHub 网页授权登录。"
    echo ""
    printf "👉 请粘贴 Token（或直接按回车打开浏览器登录）: "
    read -r INPUT_TOKEN
    INPUT_TOKEN="$(echo "${INPUT_TOKEN}" | tr -d '[:space:]')"

    if [ -n "${INPUT_TOKEN}" ]; then
      TOKEN="${INPUT_TOKEN}"
    else
      echo ""
      echo "==> 正在启动浏览器进行 GitHub 授权登录..."
      gh auth login -h github.com -p https -w
      TOKEN="$(gh auth token -h github.com 2>/dev/null || true)"
    fi
  fi
fi

echo ""
echo "==> 1. 正在检查或创建远端仓库 https://github.com/${REPO} ..."

if [ -n "${TOKEN}" ]; then
  PAYLOAD=$(printf '{"name":"%s","description":"%s","private":false,"has_issues":true,"has_projects":true,"has_wiki":true}' "${REPO_NAME}" "${DESC}")
  HTTP_CODE=$(curl -sS -o /tmp/gh_create_repo.json -w "%{http_code}" \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer ${TOKEN}" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    https://api.github.com/user/repos \
    -d "${PAYLOAD}" || echo "000")

  if [ "${HTTP_CODE}" = "201" ]; then
    echo "✅ 已成功创建新仓库: https://github.com/${REPO}"
  elif [ "${HTTP_CODE}" = "422" ]; then
    echo "ℹ️  仓库 https://github.com/${REPO} 已存在，直接准备推送代码..."
  else
    ORG_CODE=$(curl -sS -o /tmp/gh_create_org_repo.json -w "%{http_code}" \
      -H "Accept: application/vnd.github+json" \
      -H "Authorization: Bearer ${TOKEN}" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      "https://api.github.com/orgs/${REPO_OWNER}/repos" \
      -d "${PAYLOAD}" || echo "000")
    if [ "${ORG_CODE}" = "201" ] || [ "${ORG_CODE}" = "422" ]; then
      echo "✅ 组织仓库 https://github.com/${REPO} 已就绪。"
    else
      echo "⚠️  API 建仓返回状态码 (user=${HTTP_CODE}, org=${ORG_CODE})，详情如下："
      cat /tmp/gh_create_repo.json 2>/dev/null || true
      echo ""
      echo "   提示：如果您的 Fine-grained Token 未勾选 Administration (Read and write) 权限，无法通过 API 自动新建空仓库。"
      echo "   您可以先在浏览器打开 https://github.com/new 手动创建一个名为 ${REPO_NAME} 的空仓库，脚本将继续为您推送代码。"
    fi
  fi

  echo ""
  echo "==> 2. 正在推送本地 main 分支到 GitHub（绕过失效的本机 Keyring）..."
  git remote set-url origin "https://github.com/${REPO}.git" 2>/dev/null || git remote add origin "https://github.com/${REPO}.git"
  if git -c credential.helper= push -u "https://x-access-token:${TOKEN}@github.com/${REPO}.git" main:main; then
    rm -f /tmp/gh_create_repo.json /tmp/gh_create_org_repo.json
    echo ""
    echo "🎉 推送成功！正在为您在浏览器打开仓库页面："
    echo "   https://github.com/${REPO}"
    open "https://github.com/${REPO}" 2>/dev/null || true
    exit 0
  else
    echo ""
    echo "❌ 推送失败。请确认："
    echo "   1. https://github.com/${REPO} 仓库已存在（若不存在，请点击 https://github.com/new 创建名为 ${REPO_NAME} 的空仓库）；"
    echo "   2. 您的 Token 具备 Contents (Read and write) 权限。"
    exit 1
  fi
else
  if ! gh repo view "${REPO}" >/dev/null 2>&1; then
    gh repo create "${REPO}" --public --description "${DESC}"
  fi
  git remote set-url origin "https://github.com/${REPO}.git" 2>/dev/null || git remote add origin "https://github.com/${REPO}.git"
  git push -u origin main
  echo ""
  echo "🎉 推送成功！正在为您在浏览器打开仓库页面："
  echo "   https://github.com/${REPO}"
  open "https://github.com/${REPO}" 2>/dev/null || true
fi
