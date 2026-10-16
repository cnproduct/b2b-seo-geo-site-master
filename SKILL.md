---
name: b2b-seo-geo-site-master
description: Build high-converting B2B independent sites engineered for SEO traffic, GEO (Generative Engine Optimization) AI citations, and qualified overseas buyer inquiries (RFQ). Fuses cnproduct/b2b-global-brand-site-master with yan-skills, marketingskills, claude-seo, Gefei B2B methodology, geo-seo-claude, seomachine, aaron-marketing-skills, Agentic-SEO-Skill, backlink_skills, and renwork-web-design-master into a 4-phase Single-Source-of-Truth (docs/seo/ + .claude/CLAUDE.md) workflow. Use when building or auditing B2B export websites, OEM/ODM factory sites, industrial product portals, B2B keyword matrices, Hub-and-Spoke topic clusters, GEO citability architectures, or RFQ conversion funnels.
---

# b2b-seo-geo-site-master

An end-to-end B2B independent site engineering and growth skill focused on a single business outcome: acquiring qualified overseas procurement inquiries (RFQs) through organic search (SEO) and generative AI engines (GEO). It fuses fact-governed B2B site compilation, 21-industry procurement blueprints, and edge protection with 10 leading open-source SEO, GEO, CRO, and web design skills, coordinated through a unified `docs/seo/` Single Source of Truth hub and `.claude/CLAUDE.md` routing protocol.

## When to Use

- Building a new B2B export, manufacturer, trading, or OEM/ODM independent site from a company logo, brief introduction, or product catalog.
- Refactoring or auditing an existing B2B website to boost organic rankings, ChatGPT/Perplexity/Google AI Overviews citations, and RFQ conversion rates.
- Initializing a unified `docs/seo/` Single Source of Truth workspace (`site-brief.md`, `keyword-matrix.json`, `topic-cluster.json`, `cro-copy-deck.md`, `backlink-tracker.csv`, `status-log.md`, `public/llms.txt`, `public/llms-full.txt`, and `.claude/CLAUDE.md`) to prevent multi-skill instruction conflicts.
- Expanding a core product term into a 6-branch B2B commercial intent keyword matrix with SERP weakness checks (inner-page rankings, DR < 30 spots) and Hub-and-Spoke topic clusters.
- Designing 3-tier B2B conversion funnels with B2B Risk Reversal (NDA protection, sample freight credit, pre-shipment AQL inspection) and 20GP/40HQ container calculators.
- Executing pre-launch 9-gate SEO/GEO verification, 0-100 GEO citability scoring, faceted navigation crawl-trap checks, Clean URL enforcement, Anti-FOUC cache-busting, Cloudflare Workers edge protection, and 7-state backlink/brand-mention tracking.

## Core Principles and B2B Filtering Guardrails

- Single Source of Truth Orchestration (`docs/seo/` + `content/public-facts.json`): All keyword assignments, H1/H2 contracts, CRO copy decks, and lifecycle logs live in `docs/seo/`, while verifiable company claims live in `private/knowledge-cards.json` -> `content/public-facts.json`. Copywriting and UI workflows must never drop assigned primary keywords from H1/H2 headings.
- Separate Verified Company Facts from Industry Baselines: Never turn industry-average MOQ, lead time, factory area, or certifications into company claims. Only export verified, approved facts (`status: verified_fact` or `public_fact`, `public_claim_approved: true`) into HTML, JSON-LD, PDFs, `llms.txt`, and `llms-full.txt`.
- Strict B2B Mechanism Filtering (No B2C/SaaS/Affiliate Noise): Never add SaaS subscription paywalls, credit-pack pricing tables, trial credit-card gates, or affiliate review roundups to a B2B manufacturing site. Replace SaaS paywalls with **3-Tier Commercial RFQ Cards (Standard Sample Pack / Custom BOM & Tooling / 20GP-40HQ Container Quote)** and **B2B Risk Reversal** micro-copy. Use `Organization`, `Product`, `TechArticle`, and `BreadcrumbList` JSON-LD rather than `SoftwareApplication`.
- Commercial Intent, SERP Weakness, and Native Multilingual Research: Target 1 homepage pillar keyword (`[product] manufacturer`) + 6 inner-page procurement branches (`OEM/ODM`, `Supplier/Factory`, `Bulk/40HQ`, `Technical Spec`, `Application`, `Comparison`). Verify SERP weaknesses (inner pages ranking in Top 10, DR < 30 competitors, >= 60% B2B supplier intent). When expanding to `es`, `pt`, `ja`, `de`, or `fr`, re-research native industrial standards (DIN/EN, ASTM, JIS) with bidirectional `hreflang` and `x-default` instead of machine-translating keywords.
- 134-167 Word Self-Contained GEO Citability (`geo-seo-claude` + `claude-seo`): Place a self-contained 134-167 word engineering answer block and semantic HTML `<table>` specification chart on every core category, product, and OEM page (target `citability-score >= 85`). Pair `/public/llms.txt` and `/public/llms-full.txt` with off-site brand mentions (LinkedIn technical articles, YouTube QC transcripts, verified trade directories).
- Clean URLs, Faceted Nav Guard, Anti-FOUC, and Anti-AI-Slop Typography: Strip `.html` suffixes across all links, canonicals, JSON-LD, and sitemaps. Canonicalize dynamic catalog filter parameters to parent Clean URLs. Append SHA-256 content hashes to CSS/JS, isolate off-canvas drawers with critical `display: none !important`, and enforce `renwork-web-design-master` fluid `clamp()` typography (45ch-75ch measure, 1.8x heading proximity, zero purple AI gradients).

## On-Demand Reference Routing

1. Full 10-skill B2B fusion matrix, 4-phase `docs/seo/` orchestration hub, and Slash Workflows: Read [SEO/GEO Inquiry Playbook](references/seo-geo-inquiry-playbook.md).
2. Industry selection and 21-industry procurement blueprints: Read [Industry Routing](references/industry-routing.md) and inspect [21 Industries Catalog](assets/industries.json).
3. Fact governance and 21-module RenWork V4 knowledge base: Read [Knowledge and Asset Contract](references/knowledge-assets.md) and [Runtime Contract](references/runtime.md).
4. Brand system, 10 page templates, and typography math: Read [Site Blueprints](references/site-blueprints.md) and [Web Design Specification](references/web-design.md).
5. Technical SEO, 2026 Google/Bing/OpenAI crawler rules, and release gates: Read [Search and Release Acceptance](references/search-release.md), [Current Search Verification](references/search-current.md), [Procurement Components](references/procurement-components.md), and [Site Protection Contract](references/site-protection.md).

## Steps: The 4-Phase B2B Tri-Core Orchestration Workflow

### Phase 1: Keyword Matrix, SERP Weakness Teardown, and Workspace Initialization (`rankup` + `seomachine` + Gefei B2B)

Initialize the isolated company project and scaffold the `docs/seo/` Single Source of Truth hub, `.claude/CLAUDE.md` routing protocol, and `public/llms.txt` / `public/llms-full.txt`:

```bash
python3 scripts/sitekit.py industries
python3 scripts/orchestrator.py \
  --name "Example Manufacturing Co., Ltd." \
  --intro-file /path/intro.txt \
  --industry bento \
  --logo /path/logo.png \
  --out /path/company-project

python3 scripts/seo_geo_matrix.py init-workspace \
  --project /path/company-project \
  --company "Example Manufacturing Co., Ltd." \
  --seed "stainless steel bento box" \
  --industry bento \
  --markets "US,DE,Global"
```

- Inspect `docs/seo/keyword-matrix.json` and `docs/seo/topic-cluster.json`.
- Verify live SERP weakness signals (`top10_has_inner_pages`, `top10_dr_under_30_count`, `b2b_supplier_share_ge_60pct`) before locking page TDKs.
- Decompose raw company files into atomic facts in `private/knowledge-cards.json` and export approved public claims via `python3 scripts/sitekit.py export --project /path/company-project`.

### Phase 2: High-Converting B2B Landing Pages, CRO Copy Deck, and 3-Tier Inquiry Funnel (`marketingskills` + `renwork-web-design-master`)

Review and customize `docs/seo/cro-copy-deck.md` while strictly preserving the `h1_contract` and `h2_contract` keywords from `docs/seo/keyword-matrix.json`:

- Hero Value Proposition: `[Verified Product/Manufacturing Capability] for [Target Industry & OEM Buyers]`, paired with 6-point brand name alignment (`<title>`, `WebSite` JSON-LD, `og:site_name`, header logo `alt`, hero subheadline, footer copyright).
- 4-Step B2B OEM / Sourcing Process: Spec & BOM Alignment -> Engineering DFM & Prototype Sampling -> In-Line QC & Pre-Shipment AQL -> Export Packaging & Global Logistics.
- 3-Tier Commercial RFQ Cards & Risk Reversal (replacing SaaS paywalls):
  1. Tier 1 (Product / Technical Guide Pages): Standard Sample & Spec Pack Request (NDA protection; sample courier credit on first bulk order).
  2. Tier 2 (OEM/ODM / Solution Pages): Custom BOM, Material Allocation (Option A vs Option B), and Tooling RFQ (golden sample sign-off before mass production).
  3. Tier 3 (Category / Container Calculator Pages): Interactive 20GP/40GP/40HQ load estimation via `sourcing_estimator.js` and `scripts/design_math.py container` with third-party inspection support (SGS/Intertek/BV).

```bash
python3 scripts/design_math.py contrast '#1e293b' '#ffffff'
python3 scripts/design_math.py fluid 36 60 360 1440
python3 scripts/design_math.py container --length 540 --width 380 --height 420 --weight 14.5 --pcs 24
```

### Phase 3: Code-Level Technical SEO, Schema, Multilingual Hreflang, and GEO Citability (`claude-seo` + `geo-seo-claude` + `Agentic-SEO-Skill`)

Harden every generated page and Hub-and-Spoke technical guide for both traditional search crawlers and generative AI engines:

- Structured Data Injection: Emit same-source `Organization`, `WebSite`, `BreadcrumbList`, `Product`, and `TechArticle` JSON-LD matching visible HTML and `content/public-facts.json`.
- 134-167 Word GEO Answer Block & Spec Table: Ensure every core page contains a self-contained 134-167 word engineering summary paragraph and a semantic `<table>` with explicit units and testing conditions.
- International Hreflang Architecture: For multilingual builds (`en`, `es`, `pt`, `ja`, `de`, `fr`), use native industrial standard keywords, self-referencing canonicals, bidirectional `hreflang` links, and `x-default`.
- Faceted Navigation & Clean URL Guard: Strip `.html` suffixes everywhere and canonicalize dynamic filter URLs back to the parent Clean URL.
- AI Discovery Index: Keep `/public/llms.txt` and `/public/llms-full.txt` synced with approved public facts and Clean URLs.

### Phase 4: Pre-Launch 9-Gate Audit, IndexNow/GSC Push, and Tri-Track Backlink Loop (`rankup` + `validate_site.py`)

Compile the site, run the 9-gate validator and 0-100 GEO citability scorer, and execute the two-batch launch and backlink loop:

```bash
python3 scripts/orchestrator.py --project /path/company-project
python3 scripts/validate_site.py /path/company-project/site --domain https://example.com
python3 scripts/seo_geo_matrix.py citability-score --file /path/company-project/site/products.html

# When identity and contact facts are approved for production release:
python3 scripts/orchestrator.py --project /path/company-project --release
python3 scripts/validate_site.py /path/company-project/site --release --domain https://example.com
```

- Deploy via the generated `deployment_directory` Cloudflare Workers edge protection bundle and start `scripts/rfq_daemon.py --port 8012 --emails sales@example.com`.
- Submit `sitemap.xml` and updated URLs via IndexNow API, Google Search Console, and Bing Webmaster Tools.
- Track B2B directories (`batch_directory`), LinkedIn/Medium engineering articles (`editorial_authority`), and YouTube/trade brand mentions (`brand_mention_surface`) in `docs/seo/backlink-tracker.csv` and `private/backlink-ledger.json` (`candidate -> qualified -> filled -> submitted -> public -> indexed@<engine> -> rel_verified`).

```bash
python3 scripts/seo_geo_matrix.py init-ledger --out /path/company-project/private/backlink-ledger.json
python3 scripts/seo_geo_matrix.py validate-ledger --file /path/company-project/private/backlink-ledger.json
python3 scripts/seo_geo_matrix.py geo-prompts --company "Example Manufacturing Co., Ltd." --seed "stainless steel bento box" --industry bento --market "North America" --out /path/company-project/docs/seo/geo-prompt-suite.json
```

## Slash Workflow Quick Triggers

- `"立项/拓词 [产品/行业]"`: Runs Phase 1 (`orchestrator.py` + `seo_geo_matrix.py init-workspace`) -> populates `docs/seo/keyword-matrix.json`, `docs/seo/topic-cluster.json`, `docs/seo/site-brief.md`, and `.claude/CLAUDE.md`.
- `"生成落地页 [URL/词]"`: Runs Phase 2 & Phase 3 -> reads `docs/seo/keyword-matrix.json` & `docs/seo/cro-copy-deck.md` -> builds B2B Hero, 134-167 word GEO block, semantic spec `<table>`, 3-tier Risk-Reversal RFQ cards, JSON-LD, and `hreflang` -> verifies `citability-score >= 85`.
- `"上线前体检"`: Runs Phase 4 -> executes `validate_site.py`, `citability-score`, Clean URL & Anti-FOUC checks, Cloudflare Workers edge protection verification, and updates `acceptance.md` and `docs/seo/status-log.md`.

## Self-Test and Validation Suite

Run the full verification suite after modifying any skill script or template:

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

## Gotchas

- Never upload the root project directory (which contains `private/` knowledge cards and gap notes) to a public static host; always deploy from the generated `deployment_directory` bundle.
- Do not promise guaranteed Google rankings, 100% AI citation scores, or automated inquiry counts from local validation alone; always distinguish local build checks (`PASS`) from unexecuted live platform steps (`NOT_RUN`).
- Do not block `OAI-SearchBot` or `PerplexityBot` when restricting AI training crawlers (`GPTBot`), or your B2B product pages will disappear from AI buyer discovery answers.
