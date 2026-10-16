# B2B SEO & GEO Site Master (`b2b-seo-geo-site-master`) · V3.2 四阶段中枢协同与十大技能融合版

**以「获取海外采购商高质量询盘（RFQ）」为唯一终点的 B2B 独立站全生命周期 Agent Skill。**

本项目以 [cnproduct/b2b-global-brand-site-master](https://github.com/cnproduct/b2b-global-brand-site-master) 为工程底座，采用 **`docs/seo/` + `content/public-facts.json` 双核唯一事实源（Single Source of Truth）** 与 **`.claude/CLAUDE.md` 四阶段总控路由协议**，深度融合并按 **B2B 外贸制造业/供应链独立站** 场景严格筛选了十大开源 Agent Skills（剔除 SaaS 付费墙、C 端小游戏、Affiliate 软文等非 B2B 机制）：

| 阶段 | 主导能力模块 | 核心动作（B2B 独立站专属适配） | 关键交付物（写入项目目录） |
| :--- | :--- | :--- | :--- |
| **Phase 1：选词、竞品拆解与立项** | **`yan-skills` (`rankup`) + 哥飞方法论 + `seomachine`** | 1 个首页制造商核心大词 + 6 大采购意图分支词根扩树、SERP 前 10 名弱点核验（内页排名 & DR < 30 站点占比）、Hub-and-Spoke 工程选型主题聚类 | `docs/seo/site-brief.md`<br>`docs/seo/keyword-matrix.json`<br>`docs/seo/topic-cluster.json` |
| **Phase 2：高转化 B2B 着陆页与询盘漏斗** | **`marketingskills` (`page-cro` + `copywriting`) + `renwork-web-design-master`** | 严格遵守 `keyword-matrix.json` 的 H1/H2 词根契约；输出 B2B 首屏价值主张、四步 OEM 定制流程、可验证质检背书、**B2B 风险逆转（NDA 保密 / 样品费抵扣大货 / AQL 验货）** 与 **三级商业询盘卡（取代 SaaS Paywall 付费墙）** | `docs/seo/cro-copy-deck.md`<br>`DESIGN.md`<br>反 AI 塑料感工业级页面源码 |
| **Phase 3：代码级 SEO、多语言与 GEO 武装** | **`claude-seo` + `geo-seo-claude` + `Agentic-SEO-Skill`** | 注入同源 `Organization` + `Product` + `TechArticle` + `BreadcrumbList` JSON-LD；多语言（`en/es/pt/ja/de/fr`）按目标国工业标准（DIN/ASTM/JIS）母语重研并校验双向 `hreflang` + `x-default`；编写 **134-167 词自包含 GEO 工程直答块**（`citability-score >= 85`）；生成 `/public/llms.txt` 与 `/public/llms-full.txt`；分面筛选防爬虫陷阱 | `public/llms.txt`<br>`public/llms-full.txt`<br>`sitemap.xml`<br>全站 Clean URLs（零 `.html`）页面 |
| **Phase 4：上线体检、极速收录与三轨外链** | **`yan-skills` (`rankup` + `backlink`) + `validate_site.py`** | 上线前 9 道硬闸门体检、Anti-FOUC 样式哈希与 Cloudflare Workers 边缘防抓取滥用发布包、IndexNow 秒级推送 + GSC/Bing Sitemap 提交、三轨外链与站外品牌提及（B2B 目录 + LinkedIn/Medium 选型白皮书 + YouTube 验厂字幕 Brand Mentions） | `acceptance.md`<br>`docs/seo/status-log.md`<br>`docs/seo/backlink-tracker.csv`<br>`private/backlink-ledger.json` |

## 一键安装

支持 Claude Code、Codex CLI、Cursor、Gemini CLI、OpenClaw 等所有兼容 `SKILL.md` 的 Agent 平台：

```bash
npx skills add cnproduct/b2b-seo-geo-site-master -g
```

或者直接克隆到你的 Agent Skills 目录：

```bash
git clone https://github.com/cnproduct/b2b-seo-geo-site-master.git ~/.claude/skills/b2b-seo-geo-site-master
```

## 四阶段全栈命令速查

### Phase 1：一键初始化 B2B 项目与 `docs/seo/` 唯一事实源中枢

```bash
# 1. 查看内置的 21 个外贸 B2B 垂直行业蓝图并初始化 21 模块事实底座
python3 scripts/sitekit.py industries
python3 scripts/orchestrator.py \
  --name "Example Manufacturing Co., Ltd." \
  --intro "We manufacture custom stainless steel bento boxes and insulated food containers for OEM brands." \
  --industry bento \
  --out /tmp/example-b2b-project

# 2. 一键生成 docs/seo/ 数据中枢（site-brief.md、keyword-matrix.json、topic-cluster.json、cro-copy-deck.md、backlink-tracker.csv、status-log.md）、public/llms.txt + llms-full.txt 以及 .claude/CLAUDE.md 路由协议
python3 scripts/seo_geo_matrix.py init-workspace \
  --project /tmp/example-b2b-project \
  --company "Example Manufacturing Co., Ltd." \
  --seed "stainless steel bento box" \
  --industry bento \
  --markets "US,DE,Global"
```

### Phase 2 & 3：B2B 页面生成、工程数学计算与 0-100 分 GEO 可引用性评分

```bash
# WCAG 对比度、流式字阶 clamp、20GP/40GP/40HQ 整柜装载核算
python3 scripts/design_math.py contrast '#1e293b' '#ffffff'
python3 scripts/design_math.py fluid 36 60 360 1440
python3 scripts/design_math.py container --length 540 --width 380 --height 420 --weight 14.5 --pcs 24

# 编译站点并对任意 HTML 或 Markdown 页面执行 0-100 分 B2B GEO 可引用性与询盘漏斗评分
python3 scripts/orchestrator.py --project /tmp/example-b2b-project
python3 scripts/seo_geo_matrix.py citability-score --file /tmp/example-b2b-project/site/products.html
```

### Phase 4：上线前九道硬闸门验收、RFQ 守护服务与 7 态外链台账

```bash
# 预览与发布候选全量 SEO/GEO/Clean URLs/防乱码校验
python3 scripts/validate_site.py /tmp/example-b2b-project/site --domain https://example.com

# 启动生产环境 RFQ 询盘接收守护服务（支持 HMAC 算术验证码、蜜罐防刷、JSON/CSV 双轨落盘与多邮箱分发）
python3 scripts/rfq_daemon.py --port 8012 --emails sales@example.com

# 初始化并校验 7 态外链与站外品牌提及台账
python3 scripts/seo_geo_matrix.py init-ledger --out /tmp/example-b2b-project/private/backlink-ledger.json
python3 scripts/seo_geo_matrix.py validate-ledger --file /tmp/example-b2b-project/private/backlink-ledger.json
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
