# B2B 独立站 SEO + GEO 询盘获客全链路作战手册 (Fusion V3.0)

本手册将六大开源 Agent Skills 的核心工程与增长方法论融为一体，专为 **B2B 制造与外贸出海企业通过自然搜索（SEO）与生成式引擎（GEO）获取精准海外采购询盘（RFQ）** 而设计：

1. **[cnproduct/b2b-global-brand-site-master](https://github.com/cnproduct/b2b-global-brand-site-master)**：21 行业采购蓝图、RenWork V4 21 模块事实治理、Clean URLs（零 `.html` 后缀）、Anti-FOUC 防乱码样式穿透、Cloudflare Workers 默认边缘防抓取滥用与渐进式 RFQ 守护进程。
2. **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)**（`rankup` + `backlink`）：网站七段全生命周期交接链、词根扩树工作流、上线前九行证据闸门、分批平台接入（批 A 域名无关 -> 域名黑历史裁决 -> 批 B 域名相关）、项目长期记忆 Wiki 机制，以及 7 态证据化外链台账。
3. **[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)**：9 维技术 SEO 深度体检、E-E-A-T（Who/How/Why 且 Trust 权重最高）评分、有效 Schema.org 校验（剔除已停用的 FAQPage/HowTo 富媒体预期）、130-170 词自包含可引用技术段落与 Lighthouse Agentic Browsing 就绪度。
4. **[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**：B2B 转化率优化（CRO）、首屏价值主张公式、三级询盘漏斗（索样 / 定制 BOM / 整柜报价）与消除买家犹豫的微文案布局。
5. **[aaron-he-zhu/aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills)**：`Survey -> Implement -> Tune -> Evaluate` 闭环、`CORE-EEAT` 内容质量闸门与 `CITE` 域名权威闸门。
6. **[flaqai/backlink_skills](https://github.com/flaqai/backlink_skills)**：双线外链挖掘矩阵（批量目录通道 vs 行业权威编辑通道）、验证优先队列纪律与 LinkedIn / Medium 多平台 B2B 权威文章分发。

## 一、七段全生命周期交接链（以「有效询盘」为唯一终点）

每一段都有明确的输入、出口判据与交给下一段的交付物。任何上游清单（如目标词树或已核实知识卡）发生修改，必须先检索下游引用位置并同步更新。

| 阶段 | 名称 | 核心动作 | 出口判据与交付物（交给下一段） |
| :--- | :--- | :--- | :--- |
| **Stage 1** | **B2B 商业意图选词与词根扩树** | 运行 `scripts/seo_geo_matrix.py keyword-tree` 将核心产品词扩展为 6 大 B2B 采购分支（OEM/ODM、制造商核验、批发装柜、材质参数、行业应用、对比选型），剔除零售/DIY 词；核查真实 SERP 买家意图 | 产出经 SERP 验证的 **B2B 词根树与页面映射表**，每个词绑定目标 URL、买家阶段与对应 RFQ 等级 |
| **Stage 2** | **事实盘点与 21 模块知识底座** | 运行 `scripts/orchestrator.py` 初始化项目；将公司简介、证书、测试报告、规格表拆解为原子知识卡（`private/knowledge-cards.json`），严格区分「已验证企业事实」与「行业通用常识」 | 产出通过 `sitekit.py export` 严格白名单过滤的 **`content/public-facts.json`** 与内部资料缺口表 `private/gaps.md` |
| **Stage 3** | **品牌设计、采购版式与三级 RFQ 实现** | 生成 `DESIGN.md` 与语义 CSS Tokens；按行业选定四种采购版式之一；实现 Clean URLs 页面、真实规格表、装柜估算器（`sourcing_estimator.js`）及带产品上下文预填的三级 RFQ 通道 | 产出零占位符、零虚构参数、带 SHA-256 样式防缓存穿透与防御性隐藏抽屉的 **可运行静态源码与边缘防护包** |
| **Stage 4** | **上线前 SEO / GEO 九道硬闸门（预览域 `noindex`）** | 在预览环境（保持 `noindex`）逐项运行 `scripts/validate_site.py` 与九行闸门核验：站点身份、Clean URLs 与 sitemap 一致性、全站唯一 TDK/H1、事实同源 JSON-LD、GEO 可引用段落与规格表、CWV 性能与 RFQ 端到端回执 | 产出全绿通过的 **`acceptance.md` 封板声明**；未过闸严禁绑定正式域名或放开索引 |
| **Stage 5** | **两批平台接入与正式放开索引** | **批 A（域名无关）**：配置 GA4、Microsoft Clarity（监控 RFQ 表单流失热力图）、Cloudflare Web Analytics 与 `rfq_daemon.py` 接收端 -> **域名黑历史裁决**（Wayback Machine 与安全记录核查） -> **绑定正式域名** -> **批 B（域名相关）**：IndexNow 密钥校验并推送、GSC 与 Bing Webmaster 验证及提交 `sitemap.xml` -> 执行 `--release` 放开索引 | 产出线上实测可达、防护生效且已提交搜索平台的 **正式生产站点** |
| **Stage 6** | **B2B 双线外链投放与 7 态台账验证** | 运行 `scripts/seo_geo_matrix.py init-ledger` 建立外链台账；双轨推进 B2B 垂直目录提交（Track A）与 LinkedIn 技术白皮书/Medium 选型对比评测（Track B） | 产出经过 `candidate -> qualified -> filled -> submitted -> public -> indexed@<engine> -> rel_verified` 逐级核验的 **`backlink-ledger.json`** |
| **Stage 7** | **询盘归因、GEO 引用监测与记忆库迭代** | 运行 `scripts/seo_geo_matrix.py geo-prompts` 建立采购问题基线；结合 GSC 生成式 AI 报告、Bing AI Performance 与真实 RFQ 入库记录，将有效询盘归因回具体词根与页面 | 原地修订项目记忆 Wiki，触发下一棵高转化产品词根树 |

## 二、三级 B2B 询盘转化漏斗（CRO & RFQ Engineering）

海外 B2B 采购商在不同决策阶段对表单阻力的容忍度截然不同。根据页面意图配置三级渐进式转化入口：

1. **Tier 1：低阻力快速索样与规格书下载（针对产品详情页 / 技术规格页）**
   - **适用访客**：处于参数比对初期的研发工程师或采购专员。
   - **核心动作**：主 CTA 文案写明具体结果（如 `Request Standard Sample Pack` 或 `Get Full Technical Datasheet`），点击后自动将当前型号/规格带入询盘草稿。
2. **Tier 2：OEM / ODM 定制与 BOM 拆解询盘（针对 OEM 定制页 / 行业解决方案页）**
   - **适用访客**：有明确贴牌、改款、模具开发或克重/材质配比需求的品牌商与进口商。
   - **核心动作**：提供结构化选项（如材质等级、表面处理、包装形式、目标市场认证要求），引导买家提供参考样或图纸参数，展现工厂专业度。
3. **Tier 3：整柜装载核算与阶梯 FOB 询价（针对品类聚合页 / 装柜计算器页）**
   - **适用访客**：准备下达试单或整柜订单（20GP / 40GP / 40HQ）的资深买手。
   - **核心动作**：联动 `scripts/design_math.py container` 与前端 `sourcing_estimator.js`，让买家实时计算外箱 CBM、毛重利用率与柜型下界，一键连同测算结果生成阶梯询价单。

## 三、B2B 独立站 GEO（生成式引擎优化）高引用率工程规范

当海外采购商在 ChatGPT、Perplexity、Google AI Overviews 或 Bing Copilot 中提问「Who are reliable OEM manufacturers for [Product] with [Certification/Spec]?」时，AI 引擎优先检索并引用具备以下结构特征的页面：

1. **自包含的工程直答块（Self-Contained Engineering Answer Blocks）**
   - 在每个核心分类页、产品页与选型指南页首屏下方，提供一段 **130-170 词** 的高信息密度直答段落：直接交代产品适用工况、核心材质/公差范围、符合的测试标准（仅限已核实事实）以及选型边界，方便大模型直接抽取作为 Grounding Citation。
2. **HTML 语义化规格对比表（Semantic Comparison & Spec Tables）**
   - 严禁把关键参数、尺寸表、材质对比做成纯图片。必须使用标准 `<table>`、`<thead>`、`<tbody>`、`<th scope="col">`，明确标注数值、单位与测试条件。
3. **同源 JSON-LD 结构化数据与弃用类型清理**
   - 仅输出与可见 HTML 完全一致的 `Organization`、`WebSite`、`BreadcrumbList`、`Product`、`TechArticle`。
   - 遵守 Google 2026 规范：不伪造无真实交易支撑的 `Offer` 价格或 `AggregateRating` 星级；不把已于 2026-05-07 停止展示富媒体结果的 `FAQPage` 或已废弃的 `HowTo` 当作搜索特殊展现承诺。
4. **搜索爬虫、训练爬虫与用户触发访问精细分流**
   - 在 `robots.txt` 与 Cloudflare Workers 边缘防护中，严格区分搜索检索机器人（`OAI-SearchBot`、`PerplexityBot`、`Googlebot`、`bingbot`）与基础模型训练机器人（`GPTBot`、`CCBot`）。确保正规搜索与 AI 引用爬虫畅通无阻，同时对恶意高频抓取执行边缘限流。
