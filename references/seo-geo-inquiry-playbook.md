# B2B 独立站 SEO + GEO 询盘获客全链路作战手册 (Fusion V3.2 · 十大技能 + 四阶段中枢协同版)

本手册专为 **外贸制造业、工贸一体与 OEM/ODM 出海企业通过自然搜索（SEO）与生成式引擎（GEO）获取海外采购商询盘（RFQ）** 而设计。在 [cnproduct/b2b-global-brand-site-master](https://github.com/cnproduct/b2b-global-brand-site-master) 工程底座之上，严格筛选并融合了十大开源 Agent Skills 中 **真正适合 B2B 独立站** 的核心能力，并吸收了 **`yan-skills (rankup)` + `marketingskills` + `claude-seo` 四阶段单事实源（`docs/seo/`）与 `.claude/CLAUDE.md` 总控路由协议**。

## 一、四阶段协同与唯一事实源矩阵（防多 Skill 指令打架）

如果不做明确边界划分，多个 SEO、文案与建站 Skill 在「写 TDK、写首屏文案、注入 Schema」时会出现指令冲突（例如文案 Skill 为了修辞删掉核心搜索词，或工具站 Skill 错误注入 SaaS 付费墙与 `SoftwareApplication` Schema）。

V3.2 采用 **`docs/seo/` + `content/public-facts.json` 双核唯一事实源（Single Source of Truth）** 架构，通过 `python3 scripts/seo_geo_matrix.py init-workspace` 一键生成全套协同目录与 `.claude/CLAUDE.md` 路由协议：

| 阶段 | 主导能力模块 | 核心动作（B2B 独立站专属适配） | 关键交付物（写入项目目录） |
| :--- | :--- | :--- | :--- |
| **Phase 1：选词、竞品拆解与立项** | **`yan-skills` (`rankup`) + 哥飞方法论 + `seomachine`** | 词根扩树（1 个首页核心制造商大词 + 6 大采购意图分支内页词）、SERP 前 10 名弱点拆解（是否有内页排名、DR < 30 站点占比、B2B 供应商占比 >= 60%）、Hub-and-Spoke 工程主题聚类 | `docs/seo/site-brief.md`<br>`docs/seo/keyword-matrix.json`<br>`docs/seo/topic-cluster.json` |
| **Phase 2：高转化 B2B 着陆页与询盘漏斗** | **`marketingskills` (`page-cro` + `copywriting`) + `renwork-web-design-master`** | 严格读取 `keyword-matrix.json` 的 `h1_contract`/`h2_contract` 锁定核心词；按欧美 B2B 采购标准输出 **Value Proposition（价值主张）**、**4-Step OEM/Sourcing Process（四步定制采购流程）**、**Verifiable Social Proof（可验证证书与质检证据）**、**Risk Reversal（风险逆转：NDA 保密 / 样品费抵扣大货 / AQL 验货保障）** 与 **三级商业询盘卡（取代 SaaS Paywall 付费墙）** | `docs/seo/cro-copy-deck.md`<br>`DESIGN.md`<br>反 AI 塑料感工业级 HTML/React 页面 |
| **Phase 3：代码级 SEO、多语言与 GEO 武装** | **`claude-seo` + `geo-seo-claude` + `Agentic-SEO-Skill`** | 注入同源 `Organization` + `Product` + `TechArticle` + `BreadcrumbList` JSON-LD（严禁给实体制造业套用 `SoftwareApplication`）；多语言（`en/es/pt/ja/de/fr`）按当地工业标准（DIN/ASTM/JIS）母语重研并校验双向 `hreflang` + `x-default`；编写 **134-167 词自包含 GEO 工程直答块**（`citability-score >= 85`）；同步生成 `/public/llms.txt` 与 `/public/llms-full.txt`；配置分面筛选（Faceted Nav）防爬虫陷阱 | `public/llms.txt`<br>`public/llms-full.txt`<br>`sitemap.xml`<br>全站 Clean URLs（零 `.html`）页面 |
| **Phase 4：上线体检、极速收录与三轨外链** | **`yan-skills` (`rankup` + `backlink`) + `validate_site.py`** | 上线前 9 道硬闸门体检、Anti-FOUC 样式哈希与 Cloudflare Workers 边缘防抓取滥用发布包、IndexNow API 秒级推送 + GSC/Bing Sitemap 提交、三轨外链与品牌提及（B2B 垂直目录 + LinkedIn/Medium 选型白皮书 + YouTube 验厂字幕/行业名录 Brand Mentions） | `acceptance.md`<br>`docs/seo/status-log.md`<br>`docs/seo/backlink-tracker.csv`<br>`private/backlink-ledger.json` |

## 二、十大上游 Skill 的 B2B 适用性拆解与取舍矩阵

| 上游 Skill 来源 | 采纳的 B2B 独立站核心能力 | 明确剔除的非 B2B / 干扰机制 |
| :--- | :--- | :--- |
| **1. [cnproduct/b2b-global-brand-site-master](https://github.com/cnproduct/b2b-global-brand-site-master)** | 21 行业采购蓝图、RenWork V4 21 模块事实治理、全站 Clean URLs（零 `.html` 后缀）、Anti-FOUC 样式哈希防乱码、Cloudflare Workers 默认边缘防抓取滥用、渐进式 RFQ 守护进程（`rfq_daemon.py`） | 无（作为本 Skill 的核心工程编译器与事实底座） |
| **2. [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)**（`rankup` + `backlink`） | 网站七段全生命周期交接链、SERP 弱点核验（内页排名 & DR < 30）、上线前九道证据闸门、分批平台接入（批 A 域名无关 -> 域名黑历史裁决 -> 批 B 域名相关）、7 态证据化外链台账 | 剔除 `game-opportunity`（小游戏每日找词）与纯 AdSense 流量变现逻辑 |
| **3. [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)** | B2B 首屏价值主张公式、四步 OEM 合作展示、B2B 风险逆转（NDA / 寄样抵扣 / AQL 验货）与三级商业询盘卡（索样 / 定制 BOM / 整柜报价） | **剔除 SaaS 订阅付费墙（Paywall）、Credit 算力积分包与免费试用绑卡漏斗**（B2B 严禁对规格书或产品页设付费墙） |
| **4. [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)** | 9 维技术 SEO 体检、E-E-A-T（Trust 信任度权重最高）、2026 有效 Schema.org（`Organization`/`Product`/`TechArticle`）、多语言国际化 `hreflang`（`en/es/pt/ja/de/fr` + `x-default` 互返校验） | 剔除本地门店 30-50 页地域词铺站（Local GBP Doorway）、纯工具站 `SoftwareApplication` 默认套用与已废弃的 `FAQPage`/`HowTo` 富媒体承诺 |
| **5. 哥飞官方 Skill 方法论 (`seo.web.cafe`)** | **站 -> 词 / 词 -> 站** 拆解海外 B2B 垂直同行核心询盘着陆页；**多语言严禁一键机翻**，必须按目标国工业标准（如德语 DIN、美标 ASTM、日标 JIS）重新找词；**谷歌品牌名六处对齐法则** | 剔除纯工具站 KGR 擦边流量词与 C 端单页玩具站快速弃站模式 |
| **6. [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)** | **134-167 词自包含 GEO 工程直答块**评分器（`citability-score`）、6 维复合 GEO 评分体系、站外品牌提及（Brand Mentions，AI 引用相关性为普通外链 3 倍）布局、`/public/llms.txt` 与 `/public/llms-full.txt` 同步生成 | 剔除面向代运营甲方的通用冷启动销售提案生成器（`geo-proposal`） |
| **7. [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine)** | **B2B Hub-and-Spoke 主题聚类与内链缝合流水线（`topic-cluster`）**：以核心品类页/OEM 页为 Hub，撰写材质对比、QC 检验标准、装柜优化等工程选型指南（Spoke），用精准技术锚文本向 RFQ 页导流；反 AI 腔调润色 | **剔除 Affiliate 亚马逊带货评测、Top 10 凑数软文与高密度空洞长文灌水** |
| **8. [aaron-he-zhu/aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills)** | `Survey -> Implement -> Tune -> Evaluate` 闭环、`CORE-EEAT` 内容质量闸门、`CITE` 域名权威闸门，以及 LinkedIn B2B 社媒与邮件外联协同 | 剔除 C 端网红带货打分与短期消费品促销脚本 |
| **9. [Bhanunamikaze/Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill)** | 证据优先的审计输出契约（`Finding / Evidence / Impact / Fix` + `Confirmed / Likely / Hypothesis`）、**B2B 多维参数筛选（Faceted Navigation）爬虫陷阱防护**、孤儿页（Orphan Pages）与可索引矩阵核查 | 剔除 GitHub 仓库刷星 SEO（`github_seo_report.py`） |
| **10. [cnproduct/renwork-web-design-master](https://github.com/cnproduct/renwork-web-design-master)** | 流式字阶 `clamp()`、45ch-75ch 最佳技术阅读行宽、1.8x-2.5x 标题间距比、OKLCH 色彩系统、0.5px-1px 工业感细线边框（彻底消除 AI 蓝紫渐变塑料感） | 无（已内置于 `scripts/design_math.py` 与工业级 CSS 模板） |

## 三、B2B 独立站标准项目目录架构（`init-workspace` 自动生成）

```text
my-b2b-export-site/
├── .claude/
│   └── CLAUDE.md                        # 【核心】B2B 四阶段总控路由协议与快捷指令（防多 Skill 冲突）
├── docs/
│   └── seo/                             # 【核心】SEO / GEO / CRO 共享唯一事实源中枢（Single Source of Truth）
│       ├── site-brief.md                # 企业定位、目标采购商画像、核心参数与验证证据边界
│       ├── keyword-matrix.json          # 词库矩阵（1个首页大词 + 6大采购意图分支、SERP弱点、H1/H2契约、承接Clean URL）
│       ├── topic-cluster.json           # Hub-and-Spoke 工程选型文章聚类与内链锚文本缝合表
│       ├── cro-copy-deck.md             # 经 B2B CRO 打磨的首屏价值主张、四步OEM流程、风险逆转与三级询盘卡文案
│       ├── backlink-tracker.csv         # B2B 目录外链、LinkedIn 技术文与 YouTube 品牌提及跟踪表（CSV 视图）
│       └── status-log.md                # 四阶段推进状态与 GSC / Bing / IndexNow / AI 引用复盘日志
├── private/
│   ├── knowledge-cards.json             # RenWork V4 21模块企业原子事实卡（含敏感度与公开审批标记）
│   ├── backlink-ledger.json             # 7态强校验外链台账（candidate -> ... -> indexed@<engine> -> rel_verified）
│   └── gaps.md                          # 待企业补充核实的技术参数与资质缺口清单
├── content/
│   ├── public-facts.json                # 经 sitekit.py export 严格白名单导出的公开企业事实
│   └── site.json                        # 站点编译模型
└── public/
    ├── llms.txt                         # 供 ChatGPT Search / Perplexity 抓取的 B2B 产品与能力精简导航
    ├── llms-full.txt                    # 同源公开技术规格与采购边界汇总索引
    ├── robots.txt                       # 精细分流搜索检索爬虫（OAI-SearchBot/PerplexityBot）与训练爬虫（GPTBot）
    └── sitemap.xml                      # 全量 Clean URLs（零 .html 后缀）规范站点地图
```

## 四、执行口令快捷映射（Slash Workflow）

在配置了 `.claude/CLAUDE.md` 的项目中，可直接对 Agent 发送以下三类口令触发全自动流水线：

1. **「立项/拓词 [产品方向/行业]」**：
   - 自动运行 `python3 scripts/seo_geo_matrix.py init-workspace` 与 `orchestrator.py`，生成 `docs/seo/keyword-matrix.json`、`docs/seo/topic-cluster.json`、`docs/seo/site-brief.md` 与 21 模块事实卡底座。
2. **「生成落地页 [URL/目标词]」**：
   - 先读取 `docs/seo/keyword-matrix.json` 锁定 H1/H2 词根契约 -> 结合 `docs/seo/cro-copy-deck.md` 编写 B2B 首屏价值主张、**134-167 词自包含 GEO 工程直答块**、语义化 `<table>` 规格表与三级风险逆转询盘卡 -> 注入 `Organization`/`Product`/`TechArticle` JSON-LD 与多语言 `hreflang` -> 运行 `citability-score` 确保得分 >= 85。
3. **「上线前体检」**：
   - 串联执行 `python3 scripts/validate_site.py`（检查 Clean URLs、Anti-FOUC 样式哈希、Schema 同源性、分面筛选 canonical）+ `citability-score` + Cloudflare Workers 边缘防抓取发布包生成 + IndexNow/GSC 收录清单核验，并将结果写入 `acceptance.md` 与 `docs/seo/status-log.md`。
