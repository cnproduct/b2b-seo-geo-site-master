# B2B SEO & GEO Site Master (`b2b-seo-geo-site-master`) · V3.1 十大技能深度融合版

**以「获取海外采购商高质量询盘（RFQ）」为唯一终点的 B2B 独立站全生命周期 Agent Skill。**

本项目以 [cnproduct/b2b-global-brand-site-master](https://github.com/cnproduct/b2b-global-brand-site-master) 为工程底座，深度融合并**按 B2B 外贸制造业/供应链独立站场景严格筛选**了十大开源 Agent Skills（剔除 SaaS 付费墙、C 端小游戏、Affiliate 软文等非 B2B 机制）：

1. **[cnproduct/b2b-global-brand-site-master](https://github.com/cnproduct/b2b-global-brand-site-master)**：21 行业采购蓝图、RenWork V4 21 模块事实治理、Clean URLs（零 `.html` 后缀）、Anti-FOUC 样式哈希防乱码、Cloudflare Workers 默认边缘防抓取滥用与渐进式 RFQ 守护进程（`rfq_daemon.py`）。
2. **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)**（`rankup` + `backlink`）：网站七段全生命周期交接链、词根扩树工作流、上线前九道硬闸门、两批平台接入（批 A 域名无关 -> 域名黑历史裁决 -> 批 B 域名相关）与 7 态证据化外链台账。
3. **[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**：B2B 首屏价值主张公式（`[真实制造能力/产品] for [目标行业/采购角色]`）、消除采购顾虑的邻近信任微文案与三级渐进式 RFQ 询盘漏斗（剔除 SaaS 订阅付费墙 Paywall）。
4. **[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)**：9 维技术 SEO 审计、E-E-A-T（Trust 信任权重最高）、2026 有效 Schema.org 规范（剔除已废弃的 `FAQPage`/`HowTo` 富媒体承诺）与多语言国际化 `hreflang`（BCP-47 + `x-default` 互返校验）。
5. **哥飞官方 Skill 方法论 (`seo.web.cafe`)**：**站 -> 词 -> 站** 拆解海外 B2B 垂直同行核心询盘页、**多语言严禁一键机翻（按目标国 DIN/ASTM 等工业标准母语重研）**、**谷歌品牌名六处一起写对齐法则**。
6. **[zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)**：**134-167 词自包含 GEO 工程直答块**评分器（`citability-score`）、6 维复合 GEO 评分体系、站外品牌提及矩阵（Brand Mentions，AI 引用相关性为普通外链 3 倍）与 AI 爬虫分级治理。
7. **[TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine)**：**B2B Hub-and-Spoke 主题聚类与内链缝合流水线（`topic-cluster`）**，围绕核心品类页与 OEM 页生成材质取舍、质检标准、装柜优化与工况选型四类深度工程指南，精准向 RFQ 页面导流（剔除 Affiliate 带货软文）。
8. **[aaron-he-zhu/aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills)**：`Survey -> Implement -> Tune -> Evaluate` 闭环及 `CORE-EEAT`（内容质量）与 `CITE`（域名权威）双审计闸门。
9. **[Bhanunamikaze/Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill)**：证据优先审计准则（`Finding / Evidence / Impact / Fix`）、**B2B 多维参数筛选（Faceted Navigation）防爬虫陷阱**与孤儿页排查。
10. **[cnproduct/renwork-web-design-master](https://github.com/cnproduct/renwork-web-design-master)**：流式字阶 `clamp()`、45ch-75ch 阅读行宽、1.8x 标题间距比、OKLCH 色彩系统与工业级细线边框（消除 AI 蓝紫渐变塑料感）。

## 一键安装

支持 Claude Code、Codex CLI、Cursor、Gemini CLI、OpenClaw 等所有兼容 `SKILL.md` 的 Agent 平台：

```bash
npx skills add cnproduct/b2b-seo-geo-site-master -g
```

或者直接克隆到你的 Agent Skills 目录：

```bash
git clone https://github.com/cnproduct/b2b-seo-geo-site-master.git ~/.claude/skills/b2b-seo-geo-site-master
```

## 七段全生命周期命令速查

### 1. Stage 1：B2B 商业词根扩树、同行拆解与 Hub-and-Spoke 主题聚类

```bash
# 生成 6 大 B2B 采购意图分支词树 + 哥飞「站->词->站」同行拆解与多语言母语重研规约
python3 scripts/seo_geo_matrix.py keyword-tree \
  --seed "stainless steel bento box" \
  --industry bento \
  --markets "US,EU,Global" \
  --out /tmp/keyword-tree.json

# 生成 B2B Hub-and-Spoke 主题聚类与内链锚文本缝合方案（2 个核心 Hub + 4 篇工程选型 Spoke）
python3 scripts/seo_geo_matrix.py topic-cluster \
  --seed "stainless steel bento box" \
  --industry bento \
  --market "North America" \
  --out /tmp/topic-cluster.json
```

### 2. Stage 2 & 3：21 模块事实底座、反 AI 味品牌设计与站点生成

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

### 3. Stage 4 & 5：GEO 可引用性评分、上线前九道硬闸门与 RFQ 守护服务

```bash
# 编译并运行预览环境（noindex）全量 SEO/GEO/Clean URLs/防乱码校验
python3 scripts/orchestrator.py --project /tmp/example-b2b-project
python3 scripts/validate_site.py /tmp/example-b2b-project/site --domain https://example.com

# 对任意 HTML 或 Markdown 页面执行 0-100 分 B2B GEO 可引用性与询盘漏斗评分（检测 134-167 词直答块、规格表、Clean URL 与 AI 套话）
python3 scripts/seo_geo_matrix.py citability-score --file /tmp/example-b2b-project/site/products.html

# 启动生产环境 RFQ 询盘接收守护服务（支持 HMAC 算术验证码、蜜罐防刷、JSON/CSV 双轨落盘与多邮箱分发）
python3 scripts/rfq_daemon.py --port 8012 --emails sales@example.com
```

### 4. Stage 6 & 7：三轨外链/品牌提及台账与 GEO 买家提问基线

```bash
# 初始化并校验 7 态外链与站外品牌提及台账（支持 batch_directory / editorial_authority / brand_mention_surface）
python3 scripts/seo_geo_matrix.py init-ledger --out /tmp/backlink-ledger.json
python3 scripts/seo_geo_matrix.py validate-ledger --file /tmp/backlink-ledger.json

# 生成覆盖 ChatGPT / Perplexity / Google AI Overviews / Bing Copilot 的 B2B 采购评测问题集与站外品牌提及清单
python3 scripts/seo_geo_matrix.py geo-prompts \
  --company "Example Manufacturing Co., Ltd." \
  --seed "stainless steel bento box" \
  --industry bento \
  --market "North America" \
  --out /tmp/geo-prompts.json
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

本项目采用 [MIT License](LICENSE) 开源。第三方资产归属与十大上游开源项目致谢详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 与 [references/seo-geo-inquiry-playbook.md](references/seo-geo-inquiry-playbook.md)。
