---
name: b2b-seo-geo-site-master
description: Build high-converting B2B independent sites engineered for SEO traffic, GEO (Generative Engine Optimization) AI citations, and qualified overseas buyer inquiries (RFQ). Fuses all 12 subsystems of cnproduct/b2b-global-brand-site-master (M0/M1/M2 data maturity, RenWork V4 7-state 21-module fact governance, 21-industry 9-field blueprints, 21-field asset register, 4 DOM layouts, 10 page templates, dual-mode RFQ & rfq_daemon, Cloudflare Workers edge protection, Logo DNA & WCAG 4.5 math, CJK/Latin/RTL typography, and PII-redacted learning) with 13 open-source SEO, GEO, CRO, and UI/UX skills into a 4-phase Single-Source-of-Truth (docs/seo/ + .claude/CLAUDE.md) workflow.
---

# b2b-seo-geo-site-master

An end-to-end B2B independent site engineering and growth skill focused on acquiring qualified overseas procurement inquiries (RFQs) through organic search (SEO) and generative AI engines (GEO). Version 4.0 deeply fuses all 12 core engineering subsystems of `cnproduct/b2b-global-brand-site-master` with 13 open-source SEO, GEO, CRO, UI/UX, and catalog skills into a single unified compiler and a 4-phase `docs/seo/` Single Source of Truth workflow.

## When to Use

- Building a new B2B export, manufacturer, trading, or OEM/ODM independent site from a company logo, brief introduction, or product catalog (`M0`, `M1`, or `M2` data maturity).
- Refactoring or auditing an existing B2B website to boost organic rankings, ChatGPT/Perplexity/Google AI Overviews citations, and RFQ conversion rates.
- Running a single unified command (`scripts/orchestrator.py`) to initialize the 21-module RenWork V4 fact base, 6-page `noindex` draft, Cloudflare Workers edge protection bundle, `docs/seo/` Single Source of Truth hub, `src/styles/design-tokens.css`, `src/components/seo/B2bJsonLd.tsx`, and `.claude/CLAUDE.md`.
- Expanding a core product term into a 6-branch B2B commercial intent keyword matrix, Hub-and-Spoke engineering topic clusters, and multi-platform LinkedIn/Medium/YouTube syndication packs.
- Auditing bulk B2B SKU catalogs (`catalog-audit`) and scoring pages on the 0-100 B2B GEO Citability & Zero-AI-Slop Dual Audit Rubric (`citability-score`).

## The 12 Deeply Fused Subsystems of `cnproduct/b2b-global-brand-site-master`

1. **Three-Tier Data Maturity Routing (`M0 -> M1 -> M2`, `references/industry-routing.md`)**:
   - `M0` (Logo + Intro only): Generates brand direction, 6-page `noindex` draft, category/selection guides, `email_draft` RFQ, and `private/gaps.md` without inventing SKU models, factory area, or certificates.
   - `M1` (Product Catalog + Real Photos + Commercial Terms): Adds model-level comparison tables, downloadable verified PDFs, OEM/ODM workflow pages, and live `http` RFQ (`rfq_daemon.py`).
   - `M2` (Test Reports + Customer Cases + Search Data): Expands technical resource hubs, evidence-backed case studies (anonymized when NDA-bound), localized multi-market routes, and GEO citation experiments.
2. **RenWork V4 7-State & 21-Module Fact Governance (`scripts/sitekit.py` + `assets/knowledge-card.schema.json`)**:
   - Atomic fact cards (`RW-XXXXXX-0001`) across modules `00` to `20` with 7 states (including `conflicted` and `deprecated`).
   - Fail-closed 6-gate `sitekit.py export`: Only exports facts with matching `tenant_id`, `knowledge_kind="fact"`, `status in ("verified_fact", "public_fact")`, `sensitivity="public"`, boolean `public_claim_approved=True`, non-expired `valid_until`, and non-inferred `source_refs` into `content/public-facts.json`.
3. **21-Field Digital Asset Register & AI Provenance Anti-Fake Guard (`private/asset-register.json`)**:
   - Enforces `rights_status in ("owned", "licensed", "permission_granted")`, SHA-256 integrity checks, and strict boolean `is_ai_generated`.
   - Blocks `is_ai_generated=True` from impersonating `certificate`, `test_report`, `factory_photo`, or `customer_case`, and auto-captions AI concept illustrations.
4. **21-Industry 9-Field Procurement Blueprints (`assets/industries.json`)**:
   - Automatically binds each industry's `buyers`, `decision_path`, `layout`, `product_fields`, `evidence`, `rfq_fields`, `topic_clusters`, `red_lines`, and `missing_data_fallback` into `docs/seo/site-brief.md`, `keyword-matrix.json`, and `cro-copy-deck.md`.
5. **Four Procurement DOM Layouts (`data-layout="engineering | materials | oem | evidence"`)**:
   - `engineering`: Wide copy hero + dual-column fact readouts + `tabular-nums` parameter tables.
   - `materials`: Uncropped 5:4 material media + dual-column surface/node links + optional serif display titles.
   - `oem`: Brand-accented customization sidebar + left-bordered sampling steps + BOM option blocks.
   - `evidence`: Restrained heading scale + explicit operating-condition groups + batch/regulatory document rows.
6. **Ten B2B Page Blueprints & Product-to-Inquiry Context Prefill (`references/site-blueprints.md`)**:
   - Covers Home, Category, Product, Solution, OEM/ODM, Manufacturing & Quality, About & Contact, Technical Resources/FAQ, Cases, and RFQ.
   - Product page CTAs automatically route to `/contact/?product=<URL-encoded heading>#inquiry`, pre-filling blank requirement fields without overwriting user input.
7. **Progressive Dual-Mode RFQ & Standalone Ingestion Daemon (`scripts/rfq_daemon.py` + `inquiry.js`)**:
   - Default `email_draft` mode with `<noscript>` fallback; `http` mode requires `endpoint_approved=True` and a reviewed `privacy_notice`.
   - `rfq_daemon.py` provides HMAC-SHA256 math CAPTCHA (`/api/captcha`), 5-field honeypot trapping (`_hp_check`, `website_hp`, etc.), dual JSON + UTF-8-SIG Excel CSV persistence, async FormSubmit multi-email dispatch, and `/api/inquiries?key=...&format=csv`.
8. **Cloudflare Workers Default Edge Protection Coexisting with Search/AI Bots (`references/site-protection.md`)**:
   - Every build emits `private/deploy/edge-<id>/` (`worker.mjs`, `policy.json`, `wrangler.json` with `run_worker_first: true`).
   - Enforces strict allowlisted public paths (404 on `.env`/`.git`/`private/`), `READ_LIMITER` (300 req/60s/IP), `INQUIRY_LIMITER` (5 req/60s/IP, 16KiB max body), `CSP frame-ancestors 'none'` + `X-Frame-Options: DENY`, and exempts only edge-verified `request.cf.botManagement.verifiedBot === true`.
9. **Logo Raster DNA Sampling & WCAG 4.5:1 Button Contrast Guard (`scripts/extract_brand_dna.py` + `design_math.py`)**:
   - Samples 128x128 quantized dominant raster colors (recording explicit `neutral_fallback` when Pillow is absent or input is SVG) and mathematically guarantees `>= 4.5:1` contrast on primary/accent buttons.
10. **Multi-Script Typography (`65ch` Latin / `36em` CJK / `dir="rtl"`) & 4-Viewport Reflow Matrix (`references/web-design.md`)**:
    - Adapts font stacks and line measures for `en`, `zh-Hans`, `zh-Hant`, `ja`, `ko`, and RTL languages (`ar`, `fa`, `he`, `ur`), verified across `320 / 390 / 768 / 1440 CSS px` and `200%` text zoom.
11. **Six Anti-AI-Slop Visual Rules & 10-Item Dual Audit Checklist (`src/styles/design-tokens.css` + `B2bJsonLd.tsx`)**:
    - Bans neon `bg-clip-text` gradients, `shadow-xl` nested cards, pure hex greys (`#777/#888/#999`), and generic AI prose clichés; enforces `tabular-nums`, `&nbsp;` unit spacing, `1.8x-2.5x` heading proximity, and 12-column asymmetrical grids.
12. **PII-Redacted Experience Ledger (`scripts/record_learning.py`)**:
    - Regex-guards against leaking tokens, company names, emails, floor prices, or local paths while recording de-identified site/SEO lessons with `0o600` permissions.

## On-Demand Reference Routing

1. Full 14-skill B2B fusion matrix, 4-phase `docs/seo/` orchestration hub, and Slash Workflows: Read [SEO/GEO Inquiry Playbook](references/seo-geo-inquiry-playbook.md).
2. Industry selection, `M0/M1/M2` maturity, and 21-industry blueprints: Read [Industry Routing](references/industry-routing.md) and inspect [21 Industries Catalog](assets/industries.json).
3. Fact governance and 21-module RenWork V4 knowledge base: Read [Knowledge and Asset Contract](references/knowledge-assets.md) and [Runtime Contract](references/runtime.md).
4. Brand system, 10 page templates, and typography math: Read [Site Blueprints](references/site-blueprints.md) and [Web Design Specification](references/web-design.md).
5. Technical SEO, 2026 Google/Bing/OpenAI crawler rules, and release gates: Read [Search and Release Acceptance](references/search-release.md), [Current Search Verification](references/search-current.md), [Procurement Components](references/procurement-components.md), and [Site Protection Contract](references/site-protection.md).

## Steps: The Unified 4-Phase B2B Workflow

### Phase 1: One-Command Project, Fact Base & `docs/seo/` SSOT Initialization

Run `orchestrator.py` to initialize the 21-module RenWork V4 knowledge base, 6-page `noindex` draft, Cloudflare Workers edge protection bundle, AND the entire 12-file `docs/seo/` + `src/` + `.claude/CLAUDE.md` workspace in a single command:

```bash
python3 scripts/sitekit.py industries
python3 scripts/orchestrator.py \
  --name "Example Manufacturing Co., Ltd." \
  --intro-file /path/intro.txt \
  --industry bento \
  --seed "stainless steel bento box" \
  --logo /path/logo.png \
  --out /path/company-project
```

- Review `docs/seo/site-brief.md` (which records `M0/M1/M2` maturity, `decision_path`, `product_fields`, `evidence`, `rfq_fields`, and `red_lines`), `docs/seo/keyword-matrix.json`, and `docs/seo/topic-cluster.json`.
- Decompose verified company documents into atomic cards in `private/knowledge-cards.json` and export approved claims via `python3 scripts/sitekit.py export --project /path/company-project`.

### Phase 2: First-Viewport B2B Workbench, 10 Page Blueprints & 3-Tier Inquiry Funnel

Edit `content/site.json` and `docs/seo/cro-copy-deck.md` while preserving `h1_contract` and `h2_contract` keywords:

- Place a **Zero-Signup Friction Interactive B2B Workbench** (material/spec preset switcher, BOM selector, or 20GP/40HQ load calculator + Multi-SKU Sample Basket trigger) in the first viewport.
- Wire the 3-Tier Commercial RFQ Matrix (Tier 1 Sample Pack, Tier 2 Custom BOM/Drawing, Tier 3 20GP/40HQ Container Quote) with B2B Risk Reversal micro-copy.

```bash
python3 scripts/design_math.py contrast '#1e293b' '#ffffff'
python3 scripts/design_math.py fluid 36 60 360 1440
python3 scripts/design_math.py container --length 540 --width 380 --height 420 --weight 14.5 --pcs 24
```

### Phase 3: Zero AI-Slop UI, Bulk SKU Catalog Audit & GEO Citability

Apply `src/styles/design-tokens.css` and `src/components/seo/B2bJsonLd.tsx`, and audit product catalogs and generated HTML pages:

```bash
python3 scripts/seo_geo_matrix.py catalog-audit \
  --file /path/company-project/content/skus.json \
  --industry bento

python3 scripts/seo_geo_matrix.py citability-score \
  --file /path/company-project/builds/site-xxx/products/index.html
```

### Phase 4: Release Candidate Compilation, Edge Protection, Syndication & 7-State Backlink Loop

Once company identity, contact email, and at least one public fact card are approved, compile the release candidate, start the RFQ daemon, and run the syndication and backlink loop:

```bash
python3 scripts/orchestrator.py --project /path/company-project --release
python3 scripts/validate_site.py /path/company-project/builds/site-xxx --release --domain https://example.com
python3 scripts/rfq_daemon.py --port 8012 --emails sales@example.com
python3 scripts/seo_geo_matrix.py init-ledger --out /path/company-project/private/backlink-ledger.json
python3 scripts/record_learning.py --category "搜索与GEO" --observation "..." --outcome "..." --suggestion "..." --evidence "代码验证"
```

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

- Never upload the root project directory (which contains `private/` knowledge cards and gap notes) to a public static host; always deploy from the generated `deployment_directory` Cloudflare Workers bundle.
- Do not promise guaranteed Google rankings, 100% AI citation scores, or automated inquiry counts from local validation alone; always distinguish local build checks (`PASS`) from unexecuted live platform steps (`NOT_RUN`).
- Do not block `OAI-SearchBot` or `PerplexityBot` when restricting AI training crawlers (`GPTBot`), or your B2B product pages will disappear from AI buyer discovery answers.
