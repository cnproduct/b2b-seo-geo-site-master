# B2B 独立站 SEO + GEO 询盘获客全链路作战手册 (Fusion V3.1 · 十大技能深度融合版)

本手册专为 **外贸制造业、工贸一体与 OEM/ODM 出海企业通过自然搜索（SEO）与生成式引擎（GEO）获取海外采购商询盘（RFQ）** 而设计。在 [cnproduct/b2b-global-brand-site-master](https://github.com/cnproduct/b2b-global-brand-site-master) 工程底座之上，严格筛选并融合了十大开源 Agent Skills 中 **真正适合 B2B 独立站** 的核心能力，同时剔除了 SaaS 付费墙（Paywall）、C 端小游戏日更、Affiliate 联盟客软文等不适用机制。

## 一、十大上游 Skill 的 B2B 适用性拆解与取舍矩阵

| 上游 Skill 来源 | 采纳的 B2B 独立站核心能力 | 明确剔除的非 B2B / 干扰机制 |
| :--- | :--- | :--- |
| **1. [cnproduct/b2b-global-brand-site-master](https://github.com/cnproduct/b2b-global-brand-site-master)** | 21 行业采购蓝图、RenWork V4 21 模块事实治理、全站 Clean URLs（零 `.html` 后缀）、Anti-FOUC 样式哈希防乱码、Cloudflare Workers 默认边缘防抓取滥用、渐进式 RFQ 守护进程（`rfq_daemon.py`） | 无（作为本 Skill 的核心工程编译器与事实底座） |
| **2. [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)**（`rankup` + `backlink`） | 网站七段全生命周期交接链、词根扩树工作流、上线前九道证据闸门、分批平台接入（批 A 域名无关 -> 域名黑历史裁决 -> 批 B 域名相关）、7 态证据化外链台账 | 剔除 `game-opportunity`（小游戏每日找词）与纯 AdSense 流量变现逻辑 |
| **3. [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)** | B2B 首屏价值主张公式（`[真实制造能力/产品] for [目标行业/采购角色]`）、消除买家犹豫的邻近信任微文案、三级渐进式 RFQ 转化漏斗 | **剔除 SaaS 订阅付费墙（Paywall）、免费试用绑卡漏斗与 C 端冲动消费倒计时**（B2B 严禁对规格书或产品页设付费墙） |
| **4. [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)** | 9 维技术 SEO 体检、E-E-A-T（Trust 信任度权重最高）、2026 有效 Schema.org（`Organization`/`Product`/`TechArticle`）、多语言国际化 `hreflang`（BCP-47 + `x-default` 互返校验） | 剔除本地门店 30-50 页地域词铺站（Local GBP Doorway）与已废弃的 `FAQPage`/`HowTo` 富媒体承诺 |
| **5. 哥飞官方 Skill 方法论 (`seo.web.cafe`)** | **站 -> 词 / 词 -> 站** 拆解海外 B2B 垂直同行核心询盘着陆页；**多语言严禁一键机翻**，必须按目标国工业标准（如德语 DIN、美标 ASTM）重新找词；**谷歌品牌名六处对齐法则** | 剔除纯工具站 KGR 擦边流量词与 C 端单页玩具站快速弃站模式 |
| **6. [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)** | **134-167 词自包含 GEO 工程直答块**评分器（`citability-score`）、6 维复合 GEO 评分体系、站外品牌提及（Brand Mentions，AI 引用相关性为普通外链 3 倍）布局、Markdown 内容协商与 `llms.txt` | 剔除面向代运营甲方的通用冷启动销售提案生成器（`geo-proposal`）与纯 SaaS Schema |
| **7. [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine)** | **B2B Hub-and-Spoke 主题聚类与内链缝合流水线（`topic-cluster`）**：以核心品类页/OEM 页为 Hub，撰写材质对比、QC 检验标准、装柜优化等工程选型指南（Spoke），用精准技术锚文本向 RFQ 页导流；反 AI 腔调润色 | **剔除 Affiliate 亚马逊带货评测、Top 10 凑数软文与高密度空洞长文灌水** |
| **8. [aaron-he-zhu/aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills)** | `Survey -> Implement -> Tune -> Evaluate` 闭环、`CORE-EEAT` 内容质量闸门、`CITE` 域名权威闸门，以及 LinkedIn B2B 社媒与邮件外联协同 | 剔除 C 端网红带货打分与短期消费品促销脚本 |
| **9. [Bhanunamikaze/Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill)** | 证据优先的审计输出契约（`Finding / Evidence / Impact / Fix` + `Confirmed / Likely / Hypothesis`）、**B2B 多维参数筛选（Faceted Navigation）爬虫陷阱防护**、孤儿页（Orphan Pages）与可索引矩阵核查 | 剔除 GitHub 仓库刷星 SEO（`github_seo_report.py`） |
| **10. [cnproduct/renwork-web-design-master](https://github.com/cnproduct/renwork-web-design-master)** | 流式字阶 `clamp()`、45ch-75ch 最佳技术阅读行宽、1.8x-2.5x 标题间距比、OKLCH 色彩系统、0.5px-1px 工业感细线边框（彻底消除 AI 蓝紫渐变塑料感） | 无（已内置于 `scripts/design_math.py` 与工业级 CSS 模板） |

## 二、七段全生命周期交接链（以「有效询盘」为唯一终点）

| 阶段 | 名称 | 核心可执行命令 / 动作 | 出口判据与交付物（交给下一段） |
| :--- | :--- | :--- | :--- |
| **Stage 1** | **B2B 商业意图词根扩树与同行拆解** | 运行 `scripts/seo_geo_matrix.py keyword-tree` 扩展 6 大 B2B 采购分支；执行哥飞「站 -> 词 -> 站」同行着陆页拆解；规划 `topic-cluster` 主题聚类与内链缝合图谱 | 产出经 SERP 意图核实的 **B2B 词根树、多语言母语词表与 Hub-and-Spoke 内链蓝图** |
| **Stage 2** | **事实盘点与 21 模块知识底座** | 运行 `scripts/orchestrator.py` 初始化项目；将公司简介、证书、测试报告、规格表拆解为原子知识卡（`private/knowledge-cards.json`），严格区分「已验证企业事实」与「行业通用常识」 | 产出通过 `sitekit.py export` 白名单过滤的 **`content/public-facts.json`** 与内部资料缺口表 `private/gaps.md` |
| **Stage 3** | **反 AI 味工业设计、采购版式与三级 RFQ** | 生成 `DESIGN.md` 与流式字阶/OKLCH Tokens；按行业选定四种采购版式；落实谷歌品牌名六处对齐；实现 Clean URLs 页面、分面筛选防爬虫陷阱、装柜计算器与三级 RFQ 通道 | 产出零占位符、零 AI 套话、带 SHA-256 样式防缓存穿透与防御性隐藏抽屉的 **可运行静态源码与边缘防护包** |
| **Stage 4** | **上线前 SEO / GEO 九道硬闸门（预览域 `noindex`）** | 在预览环境运行 `scripts/validate_site.py` 与 `scripts/seo_geo_matrix.py citability-score`：核验 134-167 词自包含工程直答块、语义规格表、Clean URLs、唯一 TDK/H1、同源 JSON-LD、多语言 `hreflang` 互返与 RFQ 回执 | 产出复合 GEO 评分 >= 85 分且九门全绿的 **`acceptance.md` 封板声明** |
| **Stage 5** | **两批平台接入与正式放开索引** | **批 A（域名无关）**：配置 GA4、Microsoft Clarity（监控 RFQ 表单流失热力图）、CF Web Analytics 与 `rfq_daemon.py` -> **域名黑历史裁决** -> **绑定正式域名** -> **批 B（域名相关）**：IndexNow 密钥校验并推送、GSC 与 Bing Webmaster 验证及提交 `sitemap.xml` -> 执行 `--release` 放开索引 | 产出线上实测可达、防护生效且已提交搜索平台的 **正式生产站点** |
| **Stage 6** | **B2B 双线外链与站外品牌提及（Brand Mentions）** | 运行 `scripts/seo_geo_matrix.py init-ledger` 建立台账；三轨推进：Track A（B2B 垂直目录）、Track B（LinkedIn/Medium 选型对比技术文）、Track C（YouTube 验厂/质检视频字幕与行业名录品牌提及） | 产出经过 `candidate -> qualified -> filled -> submitted -> public -> indexed@<engine> -> rel_verified` 逐级核验的 **`backlink-ledger.json`** |
| **Stage 7** | **询盘归因、GEO 跨平台监测与记忆库迭代** | 运行 `scripts/seo_geo_matrix.py geo-prompts` 建立采购问题基线；结合 GSC 生成式 AI 报告、Bing AI Performance 与真实 RFQ 入库记录，将有效询盘归因回具体词根与页面 | 原地修订项目记忆 Wiki，触发下一棵高转化产品词根树 |

## 三、B2B 专属关键工程细则

### 1. 哥飞 B2B 同行拆解与六处品牌名对齐法则
- **站 -> 词 -> 站（Competitor Teardown）**：选定 3-5 家海外本土 B2B 制造商或头部进口商独立站，提取其自然流量前 20% 的产品分类页与技术指南页词根，再用该词根反查 SERP 前 10 名，确认至少 60% 结果为 B2B 供应商/规格页而非亚马逊/eBay 零售页。
- **多语言母语重研（Native Industrial Nomenclature）**：小语种建站严禁直接机翻英文关键词。必须按目标市场工业标准重新采词（如德国市场检索 DIN/EN 标准词根，北美市场检索 ASTM/ANSI/FDA 词根），并配置自指 canonical 与双向互返 `hreflang`（含 `x-default`）。
- **谷歌品牌名六处一起写**：在首页 `<title>` 尾部、`WebSite` JSON-LD 的 `name`/`alternateName`、`<meta property="og:site_name">`、页头 Logo `alt` 属性、首屏主标题旁身份说明、页脚版权声明六处保持品牌名称完全一致，让谷歌搜索结果直接显示企业品牌名而非裸域名。

### 2. `geo-seo-claude` 134-167 词自包含工程直答块与跨平台差异
- **134-167 词黄金直答窗口**：研究显示被 AI 引擎高频引用的段落集中在 **134-167 词**。在每个分类页、产品页和工程选型文章首屏下方，必须提供一个不依赖上下文即可独立成意的事实段落，包含：核心产品定义、材质/公差/工况范围、实测认证标准与定制边界。
- **ChatGPT / Perplexity vs Google AI Overviews 双轨适配**：仅约 11% 的域名能同时被 ChatGPT 和 Google AIO 引用。Google AIO 依赖经典搜索索引与页面 Schema；而 ChatGPT Search 与 Perplexity 极度依赖 **站外品牌提及（Brand Mentions 权重相关性为普通外链的 3 倍）**。因此必须将同一套经核实的企业技术参数同步分发至 LinkedIn 企业专栏、YouTube 生产线与质检视频说明及行业垂直名录。

### 3. `seomachine` B2B Hub-and-Spoke 主题聚类与内链缝合
- 拒绝无转化价值的行业新闻灌水。每做一个核心品类（Hub：`/products` 与 `/oem-odm`），配套生成 4 篇深度工程选型文章（Spoke）：
  1. **材质与规格取舍指南**（如 `304 vs 316 Stainless Steel for Bulk Sourcing`）
  2. **B2B 质量检验与批次追溯清单**（如 `AQL Inspection & Lab Testing Checklist`）
  3. **外箱包装与 20GP/40HQ 装柜优化指南**（内链直通 `/calculator` 装柜计算器）
  4. **特定行业工况选型应用笔记**（内链直通 `/solutions` 与 `/oem-odm`）
- 每篇 Spoke 文章必须在首屏前 200 词内用描述性技术锚文本链回对应 Hub 页，并在文末参数表下方直接挂载预填上下文的 Tier 1 / Tier 2 询盘入口。

### 4. `Agentic-SEO-Skill` B2B 分面筛选防爬虫陷阱（Faceted Navigation Guard）
- B2B 工业品常含多维参数筛选（材质、厚度、口径、认证）。严禁让动态筛选参数（如 `?grade=304&finish=brushed`）生成可索引 URL 导致爬虫预算耗尽与重复内容惩罚。
- 所有动态筛选状态默认保持客户端过滤或将 `<link rel="canonical">` 指向主分类 Clean URL；仅当某一细分属性组合具备真实独立的海外采购搜索量时，才将其升级为独立的静态 Clean URL 专题页。
