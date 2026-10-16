---
name: b2b-seo-geo-site-master
description: Build high-converting B2B independent sites engineered for SEO traffic, GEO (Generative Engine Optimization) AI citations, and qualified overseas buyer inquiries (RFQ). Fuses cnproduct/b2b-global-brand-site-master with yan-skills, claude-seo, marketingskills, aaron-marketing-skills, and backlink_skills. Use when building or auditing B2B export websites, OEM/ODM factory sites, industrial product portals, B2B keyword trees, GEO citability architectures, or RFQ conversion funnels.
---

# b2b-seo-geo-site-master

An end-to-end B2B independent site engineering and growth skill focused on a single business outcome: acquiring qualified overseas procurement inquiries (RFQs) through organic search (SEO) and generative AI engines (GEO). It fuses fact-governed B2B site compilation, 21-industry procurement blueprints, and edge protection with 7-stage SEO/GEO lifecycle gates, commercial intent keyword expansion, E-E-A-T passage citability, 3-tier CRO inquiry funnels, and a 7-state backlink evidence ledger.

## When to Use

- Building a new B2B export, manufacturer, trading, or OEM/ODM independent site from a company logo, brief introduction, or product catalog.
- Refactoring or auditing an existing B2B website to boost organic rankings, ChatGPT/Perplexity/Google AI Overviews citations, and RFQ conversion rates.
- Expanding a core product term into a 6-branch B2B commercial intent keyword tree (`OEM/ODM`, `Manufacturer`, `Bulk/Container`, `Technical Spec`, `Application`, `Comparison`).
- Designing 3-tier B2B conversion funnels (Standard Sample Request, Custom BOM/Drawing RFQ, and 20GP/40HQ Container Load Calculator) with verified backend delivery.
- Executing pre-launch 9-gate SEO/GEO verification, Clean URL enforcement, Anti-FOUC cache-busting, Cloudflare Workers edge protection, and 7-state backlink tracking.

## Core Principles and Non-Negotiable Guardrails

- Separate Verified Company Facts from Industry Baselines: Never turn industry-average MOQ, lead time, factory area, or certifications into company claims. Only export verified, approved facts (`status: verified_fact` or `public_fact`, `public_claim_approved: true`) into HTML, JSON-LD, PDFs, and `llms.txt`.
- Commercial Intent Over Vanity Traffic: Target B2B procurement intent (`oem manufacturer`, `custom tolerance`, `bulk 40hq`, `grade comparison`) and filter out retail/DIY keywords. Never fabricate search volume or keyword difficulty numbers.
- Evidence-Led GEO Citability: Google AI Overviews, ChatGPT Search (`OAI-SearchBot`), Perplexity (`PerplexityBot`), and Bing Copilot prioritize self-contained engineering answer blocks (130-170 words), semantic HTML specification tables, and verifiable test conditions over keyword stuffing or deprecated schema types.
- Clean URLs by Default: Strip `.html` suffixes across all internal links (`href="./"`, `href="products"`), `<link rel="canonical">`, `og:url`, JSON-LD `@id`/`url`, and `sitemap.xml`. Always ship matching `vercel.json`, `nginx.conf`, and `.htaccess` rewrite configs.
- Anti-FOUC and Layout Stability: Append SHA-256 content hashes to CSS/JS references (`/css/site.css?v={hash}`), enforce `hidden` and `display: none !important` on off-canvas drawers/modals in `<head>`, declare `<meta charset="utf-8">` within the first 1024 bytes, and avoid unstyled Unicode emoji lists.
- Default Edge Protection Coexisting with Search/AI Crawlers: Every build generates a Cloudflare Workers edge protection bundle (allowlisted public assets, rate limiting on abusive scraping and RFQ endpoints, anti-iframe mirroring) while keeping public content accessible to legitimate search and AI retrieval bots.

## On-Demand Reference Routing

1. Full 7-stage SEO + GEO + CRO inquiry workflow and upstream fusion architecture: Read [SEO/GEO Inquiry Playbook](references/seo-geo-inquiry-playbook.md).
2. Industry selection and 21-industry procurement blueprints: Read [Industry Routing](references/industry-routing.md) and inspect [21 Industries Catalog](assets/industries.json).
3. Fact governance and 21-module RenWork V4 knowledge base: Read [Knowledge and Asset Contract](references/knowledge-assets.md) and [Runtime Contract](references/runtime.md).
4. Brand system, 10 page templates, and typography math: Read [Site Blueprints](references/site-blueprints.md) and [Web Design Specification](references/web-design.md).
5. Technical SEO, 2026 Google/Bing/OpenAI crawler rules, and release gates: Read [Search and Release Acceptance](references/search-release.md), [Current Search Verification](references/search-current.md), [Procurement Components](references/procurement-components.md), and [Site Protection Contract](references/site-protection.md).

## Steps: The 7-Stage B2B SEO/GEO Inquiry Workflow

### Stage 1: B2B Commercial Intent Keyword Tree and Demand Mapping

Run the keyword tree generator to expand any seed product into 6 procurement-focused branches and map each branch to a target page type and CTA tier:

```bash
python3 scripts/seo_geo_matrix.py keyword-tree \
  --seed "stainless steel bento box" \
  --industry bento \
  --markets "US,EU,Global" \
  --out /path/company-project/private/keyword-tree.json
```

- Prune retail, single-piece, or DIY modifiers immediately.
- Verify real SERP buyer intent before locking page titles. If paid keyword APIs are not connected, keep `verification_status` as `UNVERIFIED_VOLUME_AND_SERP` and validate via search autocomplete and buyer RFQ history.

### Stage 2: Fact Ingestion and 21-Module Knowledge Base Initialization

Initialize the isolated company project directory and generate the 21-module knowledge base skeleton, brand color suggestions, and initial 6-page `noindex` draft:

```bash
python3 scripts/sitekit.py industries
python3 scripts/orchestrator.py \
  --name "Example Manufacturing Co., Ltd." \
  --intro-file /path/intro.txt \
  --industry machinery \
  --logo /path/logo.png \
  --out /path/company-project
```

- Decompose raw company documents into atomic facts in `private/knowledge-cards.json`.
- Record unverified specifications, certificates, or commercial terms in `private/gaps.md` rather than inventing placeholders.
- Run `python3 scripts/sitekit.py export --project /path/company-project` to project only approved public facts into `content/public-facts.json`.

### Stage 3: Brand Architecture, Procurement Layouts, and 3-Tier Inquiry Engine

Select the procurement layout that matches buyer decision-making and wire the 3-tier RFQ conversion funnel:

- Engineering Selection Layout (`machinery`, `components`, `electronics`, `automotive`): Highlight parameter tables, tolerances, CAD/datasheet downloads, and engineering consultation CTAs.
- Material and Spatial Layout (`building-materials`, `sanitaryware`, `furniture`): Highlight material grades, surface finishes, installation nodes, and sample kit requests.
- OEM/ODM Project Layout (`hygiene`, `footwear`, `apparel`, `bags`, `packaging`, `beauty`, `bento`): Highlight customization dimensions, BOM options, sampling lead times, and private-label MOQ structure.
- Evidence and Compliance Layout (`medical`, `food`, `chemicals`, `energy`): Highlight operating boundaries, batch traceability, test reports, and regulatory documentation.

Configure the 3-tier inquiry path across pages:

1. Tier 1 (Product / Datasheet Pages): Low-friction sample pack or technical spec sheet request with pre-filled model context.
2. Tier 2 (OEM/ODM / Solution Pages): Structured custom BOM, material allocation, or drawing evaluation form.
3. Tier 3 (Category / Container Calculator Pages): Interactive 20GP/40GP/40HQ load estimation via `sourcing_estimator.js` and `scripts/design_math.py container`, passing calculated CBM and carton counts directly into the RFQ draft.

```bash
python3 scripts/design_math.py contrast '#1e293b' '#ffffff'
python3 scripts/design_math.py fluid 36 60 360 1440
python3 scripts/design_math.py container --length 540 --width 380 --height 420 --weight 14.5 --pcs 24
```

### Stage 4: Pre-Launch 9-Gate SEO, GEO, and Engineering Verification

Compile the project and run the automated validator on the preview build (`noindex` preserved until Stage 5 gates pass):

```bash
python3 scripts/orchestrator.py --project /path/company-project
python3 scripts/validate_site.py /path/company-project/site --domain https://example.com
```

Verify all 9 pre-launch gates before cutting a release candidate:

1. Gate 0 (Site Identity & Assets): Favicon, OG metadata, logo proportions, and approved asset hashes match existing files.
2. Gate 1 (Clean URLs & Technical SEO): Zero `.html` suffixes in internal links, canonicals, `og:url`, JSON-LD, or `sitemap.xml`; zero broken links or anchors.
3. Gate 2 (Unique TDK & Heading Hierarchy): Every page has a unique `<title>`, `<meta name="description">`, and exactly one `<h1>` aligned with its Stage 1 keyword branch.
4. Gate 3 (Fact-Source Parity): Every specification table and quantitative claim traces to `content/public-facts.json`; zero placeholder text (`Lorem ipsum`, `TBD`, fake phone numbers).
5. Gate 4 (GEO Passage Citability): Core product, category, and OEM pages include a self-contained 130-170 word engineering summary block and semantic `<table>` specs with units and test conditions.
6. Gate 5 (Schema.org Accuracy): Valid `Organization`, `WebSite`, `BreadcrumbList`, `Product`, or `TechArticle` JSON-LD matching visible text; no fabricated `Offer` prices, fake `AggregateRating`, or reliance on retired Google `FAQPage` rich results.
7. Gate 6 (Agent & Crawler Readiness): Clean `robots.txt` separating search/citation bots (`Googlebot`, `bingbot`, `OAI-SearchBot`, `PerplexityBot`) from training crawlers (`GPTBot`), plus optional `llms.txt` v2 public index.
8. Gate 7 (Anti-FOUC & Core Web Vitals): CSS/JS cache-busting query hashes active, off-canvas drawers hidden via inline/critical CSS, LCP <= 2.5s, INP <= 200ms, CLS <= 0.1.
9. Gate 8 (End-to-End RFQ & Edge Protection): Verify `email_draft` mode or live `rfq_daemon.py` HTTP endpoint (HMAC math captcha, honeypot `_hp_check`, JSON/CSV persistence, email dispatch) and Cloudflare Workers edge protection rules.

### Stage 5: Two-Batch Platform Integration and Release Compilation

Never bind a production domain or open indexation before checking domain history and analytics readiness:

- Batch A (Domain-Agnostic Setup): Configure analytics, Microsoft Clarity (for RFQ form drop-off heatmaps), and the production RFQ backend (`scripts/rfq_daemon.py --port 8012 --emails sales@example.com`).
- Domain Black-History Audit: Check Wayback Machine and search safety records for the target domain to rule out prior spam penalties.
- Production Release Build: Once identity and contact facts are approved, build the release candidate and deploy via the generated `deployment_directory` Cloudflare Workers bundle:

```bash
python3 scripts/orchestrator.py --project /path/company-project --release
python3 scripts/validate_site.py /path/company-project/site --release --domain https://example.com
```

- Batch B (Domain-Bound Submission): Deploy the IndexNow key file, verify ownership in Google Search Console and Bing Webmaster Tools, submit `sitemap.xml`, and record actual platform status (`PASS` / `NOT_RUN` / `BLOCKED`) in `acceptance.md`.

### Stage 6: Dual-Track B2B Backlink Operations and 7-State Ledger

Initialize and validate the project backlink evidence ledger:

```bash
python3 scripts/seo_geo_matrix.py init-ledger --out /path/company-project/private/backlink-ledger.json
python3 scripts/seo_geo_matrix.py validate-ledger --file /path/company-project/private/backlink-ledger.json
```

- Track A (Batch B2B Directories): Pre-inspect submission forms, queue interactive CAPTCHAs for human review, and never count a form submission as an active link until verified on the public page.
- Track B (Editorial & Multi-Platform Authority): Repurpose approved engineering guides and material comparison tables into LinkedIn technical articles and Medium procurement guides linking back to core product/RFQ pages.
- Strict 7-State Progression: Advance each target through `candidate -> qualified -> filled -> submitted -> public -> indexed@<engine> -> rel_verified`.

### Stage 7: GEO Buyer Prompt Benchmarking and Inquiry Attribution

Generate the standardized B2B buyer prompt suite to monitor AI citation share and accuracy across ChatGPT, Perplexity, Google AI Overviews, and Bing Copilot:

```bash
python3 scripts/seo_geo_matrix.py geo-prompts \
  --company "Example Manufacturing Co., Ltd." \
  --seed "stainless steel bento box" \
  --industry bento \
  --market "North America" \
  --out /path/company-project/private/geo-prompt-suite.json
```

- Track funnel metrics separately: `CTA Click -> Form Start -> Validation Error -> Backend Accepted -> Inbox/CRM Delivered -> Qualified Buyer Inquiry`.
- Maintain project knowledge as an in-place updated Wiki (`acceptance.md` and `private/knowledge-cards.json`) rather than leaving contradicted historical claims active.

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
