---
name: b2b-seo-geo-site-master
description: Build high-converting B2B independent sites engineered for SEO traffic, GEO (Generative Engine Optimization) AI citations, and qualified overseas buyer inquiries (RFQ). Fuses cnproduct/b2b-global-brand-site-master with yan-skills, marketingskills, claude-seo, Gefei B2B methodology, geo-seo-claude, seomachine, aaron-marketing-skills, Agentic-SEO-Skill, vercel-labs/agent-skills, ui-ux-pro-max-skill, liquid-skills, ecommerce-skills, backlink_skills, and renwork-web-design-master into a 4-phase Single-Source-of-Truth (docs/seo/ + .claude/CLAUDE.md) workflow. Use when building or auditing B2B export websites, OEM/ODM factory sites, industrial product portals, B2B keyword matrices, Hub-and-Spoke topic clusters, SKU catalog audits, GEO citability architectures, or RFQ conversion funnels.
---

# b2b-seo-geo-site-master

An end-to-end B2B independent site engineering and growth skill focused on a single business outcome: acquiring qualified overseas procurement inquiries (RFQs) through organic search (SEO) and generative AI engines (GEO). It fuses fact-governed B2B site compilation, 21-industry procurement blueprints, and edge protection with 14 leading open-source and custom SEO, GEO, CRO, UI/UX, and catalog engineering skills, coordinated through a unified `docs/seo/` Single Source of Truth hub and `.claude/CLAUDE.md` routing protocol.

## When to Use

- Building a new B2B export, manufacturer, trading, or OEM/ODM independent site from a company logo, brief introduction, or product catalog.
- Refactoring or auditing an existing B2B website to boost organic rankings, ChatGPT/Perplexity/Google AI Overviews citations, and RFQ conversion rates.
- Initializing a unified `docs/seo/` Single Source of Truth workspace (`site-brief.md`, `keyword-matrix.json`, `topic-cluster.json`, `syndication-pack.json`, `cro-copy-deck.md`, `backlink-tracker.csv`, `status-log.md`, `src/styles/design-tokens.css`, `src/components/seo/B2bJsonLd.tsx`, `public/llms.txt`, `public/llms-full.txt`, and `.claude/CLAUDE.md`) to prevent multi-skill instruction conflicts.
- Auditing bulk B2B SKU catalogs (`catalog-audit`) for missing technical specs, thin SEO descriptions, duplicate titles, or Clean URL violations.
- Designing B2B interactive catalog UX (Zero-Signup Friction First-Viewport Spec/Container Workbench, 4 B2B industry visual archetypes, `tabular-nums` spec tables, accessible material/finish swatch switchers, Multi-SKU Sample & RFQ Basket drawers, and 20GP/40HQ container calculators).
- Executing pre-launch 10-item Dual Audits (SEO + Zero AI-Slop Visual Engineering), 0-100 GEO citability scoring, faceted navigation crawl-trap checks, Clean URL enforcement, Anti-FOUC cache-busting, Cloudflare Workers edge protection, and LinkedIn/Medium/YouTube syndication + 7-state backlink tracking.

## Core Principles and B2B Filtering Guardrails

- Single Source of Truth Orchestration (`docs/seo/` + `content/public-facts.json`): All keyword assignments, H1/H2 contracts, CRO copy decks, and lifecycle logs live in `docs/seo/`, while verifiable company claims live in `private/knowledge-cards.json` -> `content/public-facts.json`. Target primary keywords must appear in the Clean URL slug, `<title>`, `<h1>`, and first 100 words of copy.
- Separate Verified Company Facts from Industry Baselines: Never turn industry-average MOQ, lead time, factory area, or certifications into company claims. Only export verified, approved facts (`status: verified_fact` or `public_fact`, `public_claim_approved: true`) into HTML, JSON-LD, PDFs, `llms.txt`, and `llms-full.txt`.
- First-Viewport Interactive B2B Workbench (`Zero-Signup Friction` Adaptation): Place an interactive engineering utility (1-click Material/Spec Preset Switcher, BOM Core Selector, or Instant 20GP/40HQ Carton Load Estimator + Multi-SKU Sample Basket trigger) directly in the first viewport so overseas buyers experience technical value before hitting an RFQ form.
- Strict B2B Mechanism Filtering (No B2C/SaaS/Affiliate Noise): Never add SaaS subscription paywalls, credit-pack pricing tables, B2C impulse credit-card checkouts, or affiliate review roundups to a B2B manufacturing site. Replace SaaS paywalls with **3-Tier Commercial RFQ Cards (Standard Sample Pack / Custom BOM & Tooling / 20GP-40HQ Container Quote)**, **Multi-SKU Sample Basket Drawers**, and **B2B Risk Reversal** micro-copy. Render `Organization` + `Product` + `TechArticle` (+ optional `FAQPage` for PAA buyer questions) via `src/components/seo/B2bJsonLd.tsx` rather than `SoftwareApplication`.
- Six Anti-AI-Slop Visual Engineering Rules (`renwork-web-design-master` + `src/styles/design-tokens.css`):
  1. **No Neon Text Gradients**: Never apply `bg-clip-text text-transparent bg-gradient-to-r` on headline words.
  2. **Kill Nested Shadow Cards**: Replace `rounded-2xl shadow-xl` cards with `1px` subtle borders (`var(--border-subtle)`) or tonal surface shifts (`var(--bg-elevated)`).
  3. **Strict 2+1 Font Pairing & Tabular Numerals**: Max 2 font families (`Heading` + `Body`) + 1 `Monospace` font (`JetBrains Mono` / `Geist Mono`) with `font-variant-numeric: tabular-nums` on all specification tables and calculators, plus `&nbsp;` between numbers and units (`500&nbsp;pcs`, `0.8&nbsp;mm`).
  4. **Heading Proximity Rule**: Set `margin-top` on H2/H3 headings to `1.8x` to `2.5x` their `margin-bottom`.
  5. **12-Column Asymmetrical Grid**: Use `grid-template-columns: repeat(12, minmax(0, 1fr))` (e.g., 4-col sticky header on left + 8-col spec table or 4-step OEM workflow on right) to break centered monotony.
  6. **OKLCH Tinted Neutrals & Restrained Accent**: Ban pure hex greys (`#777`, `#888`, `#999`); reserve `--accent-interactive` strictly for primary RFQ CTAs, active swatches, and focus rings.
- 134-167 Word Self-Contained GEO Citability (`geo-seo-claude` + `claude-seo`): Place a self-contained 134-167 word engineering answer block and semantic HTML `<table>` specification chart on every core category, product, and OEM page (target `citability-score >= 85`). Pair `/public/llms.txt` and `/public/llms-full.txt` with off-site brand mentions (LinkedIn technical articles, YouTube QC transcripts, verified trade directories).

## On-Demand Reference Routing

1. Full 14-skill B2B fusion matrix, 4-phase `docs/seo/` orchestration hub, and Slash Workflows: Read [SEO/GEO Inquiry Playbook](references/seo-geo-inquiry-playbook.md).
2. Industry selection and 21-industry procurement blueprints: Read [Industry Routing](references/industry-routing.md) and inspect [21 Industries Catalog](assets/industries.json).
3. Fact governance and 21-module RenWork V4 knowledge base: Read [Knowledge and Asset Contract](references/knowledge-assets.md) and [Runtime Contract](references/runtime.md).
4. Brand system, 10 page templates, and typography math: Read [Site Blueprints](references/site-blueprints.md) and [Web Design Specification](references/web-design.md).
5. Technical SEO, 2026 Google/Bing/OpenAI crawler rules, and release gates: Read [Search and Release Acceptance](references/search-release.md), [Current Search Verification](references/search-current.md), [Procurement Components](references/procurement-components.md), and [Site Protection Contract](references/site-protection.md).

## Steps: The 4-Phase B2B Orchestration Workflow

### Phase 1: Keyword Matrix, SERP Weakness Teardown, and Workspace Initialization (`rankup` + `seomachine` + Gefei B2B)

Initialize the isolated company project and scaffold the `docs/seo/` Single Source of Truth hub, `src/styles/design-tokens.css`, `src/components/seo/B2bJsonLd.tsx`, `.claude/CLAUDE.md` routing protocol, and `public/llms.txt` / `public/llms-full.txt`:

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

### Phase 2: First-Viewport B2B Workbench, CRO Copy Deck, and 3-Tier Inquiry Funnel (`marketingskills` + `liquid-skills`)

Review and customize `docs/seo/cro-copy-deck.md` while strictly preserving the `h1_contract` and `h2_contract` keywords from `docs/seo/keyword-matrix.json`:

- First-Viewport Interactive B2B Workbench (`Zero-Signup Friction` Hero): Embed a 1-click Material/Spec Preset Switcher, BOM option toggle, or mini 20GP/40HQ container calculator directly in the first viewport alongside `Add to Multi-SKU Sample Basket`.
- Asymmetrical 4-Step B2B OEM / Sourcing Process: Spec & BOM Alignment -> Engineering DFM & Prototype Sampling -> In-Line QC & Pre-Shipment AQL -> Export Packaging & Global Logistics.
- 3-Tier Commercial RFQ Cards & Risk Reversal (replacing SaaS paywalls):
  1. Tier 1 (Product / Technical Guide Pages): Standard Sample & Spec Pack Request (NDA protection; sample courier credit on first bulk order).
  2. Tier 2 (OEM/ODM / Solution Pages): Custom BOM, Material Allocation (Option A vs Option B), and Tooling RFQ (golden sample sign-off before mass production).
  3. Tier 3 (Category / Container Calculator Pages): Interactive 20GP/40GP/40HQ load estimation via `sourcing_estimator.js` and `scripts/design_math.py container` with third-party inspection support (SGS/Intertek/BV).
- Intent-Driven PAA FAQ: Answer 5-8 real procurement questions (MOQ mixing, tooling ownership, lead time, AQL standards, incoterms).

### Phase 3: Zero AI-Slop UI, Bulk SKU Catalog Audit, and GEO Citability (`renwork-web-design-master` + `ui-ux-pro-max` + `vercel-labs` + `ecommerce-skills`)

Apply `src/styles/design-tokens.css` (Major Third `clamp()` scale, OKLCH tinted neutrals, `1px` borders, 12-column asymmetrical grid, `tabular-nums`) and audit the SKU catalog:

```bash
python3 scripts/design_math.py contrast '#1e293b' '#ffffff'
python3 scripts/design_math.py fluid 36 60 360 1440
python3 scripts/design_math.py container --length 540 --width 380 --height 420 --weight 14.5 --pcs 24

python3 scripts/seo_geo_matrix.py catalog-audit \
  --file /path/company-project/content/skus.json \
  --industry bento
```

### Phase 4: Technical SEO, `B2bJsonLd.tsx`, 10-Item Dual Audit, and Tri-Track Backlink Closure (`claude-seo` + `geo-seo-claude` + `rankup` + `backlink_skills`)

Compile the site, run the 9-gate validator and 0-100 GEO + Zero-AI-Slop dual scorer, and execute the launch, syndication, and backlink loop:

```bash
python3 scripts/orchestrator.py --project /path/company-project
python3 scripts/validate_site.py /path/company-project/site --domain https://example.com
python3 scripts/seo_geo_matrix.py citability-score --file /path/company-project/site/products.html

python3 scripts/seo_geo_matrix.py syndication-pack \
  --company "Example Manufacturing Co., Ltd." \
  --seed "stainless steel bento box" \
  --industry bento \
  --url "/products" \
  --out /path/company-project/docs/seo/syndication-pack.json
```

## Pre-Release 10-Item Dual Audit Checklist (SEO + Zero AI-Slop Visual)

Verify all 10 items in `docs/seo/status-log.md` before marking any B2B page complete:

1. [ ] **Keyword Alignment**: Primary keyword is present in Clean URL slug, `<title>`, `<h1>`, and first 100 words of copy.
2. [ ] **Zero-Friction First-Viewport Workbench**: First viewport includes an interactive spec filter, swatch switcher, or 20GP/40HQ container calculator plus 1-click RFQ/Sample Basket trigger.
3. [ ] **Zero Neon Gradient Gimmicks**: No `bg-clip-text text-transparent bg-gradient-to-r` highlights on headline words.
4. [ ] **Reading Measure & Tabular Numerals**: Body paragraphs constrained to `45ch-75ch` (`max-w-[65ch]`); all spec tables enforce `font-variant-numeric: tabular-nums` and `&nbsp;` between numbers and units.
5. [ ] **Heading Proximity**: H2/H3 `margin-top` is `1.8x` to `2.5x` larger than `margin-bottom`.
6. [ ] **Card & Color Discipline**: Zero `shadow-xl`/`shadow-2xl` nested cards or pure hex greys (`#777`/`#888`/`#999`); uses `1px` subtle borders (`var(--border-subtle)`) and OKLCH tinted neutrals (`src/styles/design-tokens.css`).
7. [ ] **12-Column Asymmetrical Grid**: Process steps, spec breakdowns, and FAQs use a 12-column asymmetrical split rather than monotonous full-page center alignment.
8. [ ] **Same-Source B2B JSON-LD**: `Organization` + `Product` + `TechArticle` (+ optional `FAQPage`) rendered via `src/components/seo/B2bJsonLd.tsx` with zero fabricated prices or ratings.
9. [ ] **GEO Citability >= 85 & `llms.txt` Parity**: Core pages contain a 134-167 word self-contained engineering answer block, semantic `<table>` specs, and synced `/public/llms.txt` + `/public/llms-full.txt`.
10. [ ] **Clean URLs, Anti-FOUC, Edge Protection & IndexNow**: Zero `.html` suffixes, SHA-256 CSS/JS cache-busting, Cloudflare Workers edge protection active, and URLs queued for IndexNow/GSC.

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
