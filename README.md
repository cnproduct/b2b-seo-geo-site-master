# B2B SEO & GEO Site Master (`b2b-seo-geo-site-master`) · V3.0

**以「获取海外采购商高质量询盘（RFQ）」为唯一终点的 B2B 独立站全生命周期 Agent Skill。**

本项目将 [cnproduct/b2b-global-brand-site-master](https://github.com/cnproduct/b2b-global-brand-site-master) 的 **21 行业采购蓝图、21 模块事实治理底座、Clean URLs、Anti-FOUC 防乱码机制与 Cloudflare Workers 默认边缘防护**，与开源社区最顶流的五大建站与增长 Skill 深度融合：

- **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)**（`rankup` + `backlink`）：吸收网站七段全生命周期交接链、词根扩树工作流、上线前九道硬闸门、两批平台接入（批 A 域名无关 -> 域名黑历史裁决 -> 批 B 域名相关）与 7 态证据化外链台账（`candidate -> qualified -> filled -> submitted -> public -> indexed@<engine> -> rel_verified`）。
- **[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)**：吸收 9 维技术 SEO 审计、E-E-A-T（Who/How/Why，Trust 权重最高）准则、130-170 词自包含 GEO 工程直答块、语义化参数表、2026 最新 Schema.org 规范（剔除已废弃的 `FAQPage`/`HowTo` 富媒体承诺）与 AI 搜索爬虫分级治理（区分 `OAI-SearchBot` / `PerplexityBot` 与训练爬虫 `GPTBot`）。
- **[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**：吸收 B2B 转化率优化（CRO）与三级渐进式 RFQ 询盘漏斗（Tier 1 快速索样与规格书、Tier 2 OEM/ODM 定制 BOM 拆解、Tier 3 20GP/40HQ 整柜核算与阶梯报价）。
- **[aaron-he-zhu/aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills)**：吸收 `Survey -> Implement -> Tune -> Evaluate` 闭环及 `CORE-EEAT`（内容质量）与 `CITE`（域名权威）双审计闸门。
- **[flaqai/backlink_skills](https://github.com/flaqai/backlink_skills)**：吸收双线外链挖掘矩阵（B2B 垂直目录批量通道 + LinkedIn/Medium 行业权威对比评测通道）与验证优先队列纪律。

## 一键安装

支持 Claude Code、Codex CLI、Cursor、Gemini CLI 等所有兼容 `SKILL.md` 的 Agent 平台：

```bash
npx skills add cnproduct/b2b-seo-geo-site-master -g
```

或者直接克隆到你的 Agent Skills 目录：

```bash
git clone https://github.com/cnproduct/b2b-seo-geo-site-master.git ~/.claude/skills/b2b-seo-geo-site-master
```

## 七段全生命周期命令速查

### 1. Stage 1：B2B 商业意图词根扩树与 GEO 采购问题基线

```bash
# 生成 6 大 B2B 采购意图分支词树（OEM/ODM、制造商核验、批发装柜、技术参数、行业应用、对比选型）
python3 scripts/seo_geo_matrix.py keyword-tree \
  --seed "stainless steel bento box" \
  --industry bento \
  --markets "US,EU,Global" \
  --out /tmp/keyword-tree.json

# 生成覆盖 ChatGPT / Perplexity / Google AI Overviews / Bing Copilot 的 B2B 采购评测问题集
python3 scripts/seo_geo_matrix.py geo-prompts \
  --company "Example Manufacturing Co., Ltd." \
  --seed "stainless steel bento box" \
  --industry bento \
  --market "North America" \
  --out /tmp/geo-prompts.json
```

### 2. Stage 2 & 3：21 模块事实底座、品牌设计与站点生成

```bash
# 查看内置的 21 个外贸 B2B 垂直行业蓝图
python3 scripts/sitekit.py industries

# 从公司简介与 Logo 初始化隔离项目（生成 21 模块知识卡、品牌取色与初始 6 页 noindex 草稿）
python3 scripts/orchestrator.py \
  --name "Example Manufacturing Co., Ltd." \
  --intro "We manufacture custom stainless steel bento boxes and insulated food containers for OEM brands." \
  --industry bento \
  --out /tmp/example-b2b-project

# 常用工程计算工具（WCAG 对比度、流式字阶 clamp、20GP/40GP/40HQ 整柜装载核算）
python3 scripts/design_math.py contrast '#1e293b' '#ffffff'
python3 scripts/design_math.py fluid 36 60 360 1440
python3 scripts/design_math.py container --length 540 --width 380 --height 420 --weight 14.5 --pcs 24
```

### 3. Stage 4 & 5：上线前九道硬闸门验收、RFQ 守护进程与正式发布包

```bash
# 编译并运行预览环境（noindex）全量 SEO/GEO/Clean URLs/防乱码校验
python3 scripts/orchestrator.py --project /tmp/example-b2b-project
python3 scripts/validate_site.py /tmp/example-b2b-project/site --domain https://example.com

# 生成正式发布候选（需先完成企业身份、联系方式与公开事实卡核准）
python3 scripts/orchestrator.py --project /tmp/example-b2b-project --release
python3 scripts/validate_site.py /tmp/example-b2b-project/site --release --domain https://example.com

# 启动生产环境 RFQ 询盘接收守护服务（支持 HMAC 算术验证码、蜜罐防刷、JSON/CSV 双轨落盘与多邮箱分发）
python3 scripts/rfq_daemon.py --port 8012 --emails sales@example.com
```

### 4. Stage 6：7 态证据化 B2B 外链台账管理

```bash
# 初始化并校验 7 态外链台账（candidate -> qualified -> filled -> submitted -> public -> indexed@<engine> -> rel_verified）
python3 scripts/seo_geo_matrix.py init-ledger --out /tmp/backlink-ledger.json
python3 scripts/seo_geo_matrix.py validate-ledger --file /tmp/backlink-ledger.json
```

## 自动化自检与回归测试

```bash
python3 scripts/seo_geo_matrix.py self-test
python3 scripts/sitekit.py self-test
python3 scripts/design_math.py self-test
python3 tests/check_pipeline.py
python3 tests/check_validator.py
node tests/check_estimator.mjs
node tests/check_inquiry.mjs
node tests/check_protection.mjs
```

## 许可证与致谢

本项目采用 [MIT License](LICENSE) 开源。第三方资产归属与上游开源项目致谢详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 与 [references/seo-geo-inquiry-playbook.md](references/seo-geo-inquiry-playbook.md)。
