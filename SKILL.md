---
name: b2b-seo-geo-site-master
description: Build high-converting B2B independent sites engineered for SEO traffic, GEO (Generative Engine Optimization) AI citations, and qualified overseas buyer inquiries (RFQ). Fuses cnproduct/b2b-global-brand-site-master with yan-skills, marketingskills, claude-seo, Gefei B2B methodology, geo-seo-claude, seomachine, aaron-marketing-skills, Agentic-SEO-Skill, backlink_skills, and renwork-web-design-master. Use when building or auditing B2B export websites, OEM/ODM factory sites, industrial product portals, B2B keyword trees, Hub-and-Spoke topic clusters, GEO citability architectures, or RFQ conversion funnels.
---

# b2b-seo-geo-site-master

An end-to-end B2B independent site engineering and growth skill focused on a single business outcome: acquiring qualified overseas procurement inquiries (RFQs) through organic search (SEO) and generative AI engines (GEO). It fuses fact-governed B2B site compilation, 21-industry procurement blueprints, and edge protection with 10 leading open-source SEO, GEO, CRO, and web design skills, carefully filtered for B2B manufacturing and export businesses.

## When to Use

- Building a new B2B export, manufacturer, trading, or OEM/ODM independent site from a company logo, brief introduction, or product catalog.
- Refactoring or auditing an existing B2B website to boost organic rankings, ChatGPT/Perplexity/Google AI Overviews citations, and RFQ conversion rates.
- Expanding a core product term into a 6-branch B2B commercial intent keyword tree (`OEM/ODM`, `Manufacturer`, `Bulk/Container`, `Technical Spec`, `Application`, `Comparison`) with competitor teardown (`domain -> keyword -> domain`).
- Planning B2B Hub-and-Spoke engineering topic clusters (`seomachine` pattern) and scoring pages on the 0-100 B2B GEO Citability Rubric (`geo-seo-claude` 134-167 word passage standard).
- Designing 3-tier B2B conversion funnels (Standard Sample Request, Custom BOM/Drawing RFQ, and 20GP/40HQ Container Load Calculator) with verified backend delivery.
- Executing pre-launch 9-gate SEO/GEO verification, faceted navigation crawl-trap checks, Clean URL enforcement, Anti-FOUC cache-busting, Cloudflare Workers edge protection, and 7-state backlink/brand-mention tracking.

## Core Principles and B2B Filtering Guardrails

- Separate Verified Company Facts from Industry Baselines: Never turn industry-average MOQ, lead time, factory area, or certifications into company claims. Only export verified, approved facts (`status: verified_fact` or `public_fact`, `public_claim_approved: true`) into HTML, JSON-LD, PDFs, and `llms.txt`.
- Strict B2B Mechanism Filtering (No B2C/SaaS/Affiliate Noise): Never add SaaS subscription paywalls, trial credit-card gates, retail countdown timers, or affiliate review roundups to a B2B site. Keep technical datasheets, specification tables, and container calculators open and adjacent to friction-calibrated RFQ forms.
- Commercial Intent and Native Multilingual Research (Gefei B2B Rule): Target procurement intent (`oem manufacturer`, `custom tolerance`, `bulk 40hq`, `grade comparison`) and filter out retail/DIY keywords. Never use one-click machine translation to clone multilingual pages; re-research native industrial standards (e.g., DIN/EN for German, ASTM/ANSI for US) per target market with bidirectional `hreflang`.
- 134-167 Word Self-Contained GEO Citability (`geo-seo-claude` + `claude-seo`): Place a self-contained 134-167 word engineering answer block and semantic HTML `<table>` specification chart on every core category, product, and OEM page. Pair on-site schema (`Organization`, `WebSite`, `BreadcrumbList`, `Product`, `TechArticle`) with off-site brand mentions (LinkedIn technical articles, YouTube QC transcripts, verified trade directories).
- Hub-and-Spoke Internal Link Stitching (`seomachine` + `Agentic-SEO-Skill`): Connect engineering buying guides (`Spokes`) to core Category and OEM pages (`Hubs`) using descriptive technical anchor text. Guard multi-attribute catalog filters against faceted navigation crawl traps by canonicalizing dynamic filter queries to the parent Clean URL.
- Clean URLs, Anti-FOUC, and Anti-AI-Slop Typography (`renwork-web-design-master`): Strip `.html` suffixes across all links, canonicals, JSON-LD, and sitemaps. Append SHA-256 content hashes to CSS/JS, isolate off-canvas drawers with critical `display: none !important`, use fluid `clamp()` typography (45ch-75ch reading measure, 1.8x heading proximity), and ban purple/neon AI gradients or generic prose clichés.

## On-Demand Reference Routing

1. Full 10-skill B2B fusion matrix, 7-stage lifecycle, and GEO/CRO/Topic-Cluster playbook: Read [SEO/GEO Inquiry Playbook](references/seo-geo-inquiry-playbook.md).
2. Industry selection and 21-industry procurement blueprints: Read [Industry Routing](references/industry-routing.md) and inspect [21 Industries Catalog](assets/industries.json).
3. Fact governance and 21-module RenWork V4 knowledge base: Read [Knowledge and Asset Contract](references/knowledge-assets.md) and [Runtime Contract](references/runtime.md).
4. Brand system, 10 page templates, and typography math: Read [Site Blueprints](references/site-blueprints.md) and [Web Design Specification](references/web-design.md).
5. Technical SEO, 2026 Google/Bing/OpenAI crawler rules, and release gates: Read [Search and Release Acceptance](references/search-release.md), [Current Search Verification](references/search-current.md), [Procurement Components](references/procurement-components.md), and [Site Protection Contract](references/site-protection.md).

## Steps: The 7-Stage B2B SEO/GEO Inquiry Workflow

### Stage 1: B2B Commercial Intent Keyword Tree, Competitor Teardown, and Topic Cluster Plan

Generate the 6-branch B2B commercial keyword tree and the Hub-and-Spoke internal link stitching plan:

```bash
python3 scripts/seo_geo_matrix.py keyword-tree \
  --seed "stainless steel bento box" \
  --industry bento \
  --markets "US,EU,Global" \
  --out /path/company-project/private/keyword-tree.json

python3 scripts/seo_geo_matrix.py topic-cluster \
  --seed "stainless steel bento box" \
  --industry bento \
  --market "North America" \
  --out /path/company-project/private/topic-cluster.json
```

- Run the `domain -> keyword -> domain` teardown on 3-5 overseas niche B2B competitors and verify at least 60% of SERP results represent B2B suppliers or specification pages.
- Map each Hub (`/products`, `/oem-odm`) to 4 high-intent engineering Spoke guides (Material Trade-offs, QC & Testing Checklist, Packaging & 20GP/40HQ Loading, Application Selection).

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

- Decompose raw company documents into atomic facts in `private/knowledge-cards.json` and log missing parameters in `private/gaps.md`.
- Run `python3 scripts/sitekit.py export --project /path/company-project` to project only approved public facts into `content/public-facts.json`.

### Stage 3: Anti-Slop Brand Architecture, Procurement Layouts, and 3-Tier Inquiry Engine

Select the procurement layout that matches buyer decision-making, align the brand name across 6 key signals (`<title>`, `WebSite` JSON-LD, `og:site_name`, header logo `alt`, hero subheadline, footer copyright), and wire the 3-tier RFQ funnel:

- Engineering Selection Layout (`machinery`, `components`, `electronics`, `automotive`): Highlight parameter tables, tolerances, CAD/datasheet downloads, and engineering consultation CTAs.
- Material and Spatial Layout (`building-materials`, `sanitaryware`, `furniture`): Highlight material grades, surface finishes, installation nodes, and sample kit requests.
- OEM/ODM Project Layout (`hygiene`, `footwear`, `apparel`, `bags`, `packaging`, `beauty`, `bento`): Highlight customization dimensions, BOM options, sampling lead times, and private-label MOQ structure.
- Evidence and Compliance Layout (`medical`, `food`, `chemicals`, `energy`): Highlight operating boundaries, batch traceability, test reports, and regulatory documentation.

Configure the 3-tier inquiry path across pages:

1. Tier 1 (Product / Technical Guide Pages): Low-friction sample pack or datasheet request with pre-filled model context.
2. Tier 2 (OEM/ODM / Solution Pages): Structured custom BOM, material allocation (Option A vs Option B), or drawing evaluation form.
3. Tier 3 (Category / Container Calculator Pages): Interactive 20GP/40GP/40HQ load estimation via `sourcing_estimator.js` and `scripts/design_math.py container`, passing calculated CBM and carton counts directly into the RFQ draft.

```bash
python3 scripts/design_math.py contrast '#1e293b' '#ffffff'
python3 scripts/design_math.py fluid 36 60 360 1440
python3 scripts/design_math.py container --length 540 --width 380 --height 420 --weight 14.5 --pcs 24
```

### Stage 4: Pre-Launch 9-Gate SEO, GEO Citability, and Engineering Verification

Compile the project, run the site validator, and score core pages on the 0-100 B2B GEO Citability Rubric (`noindex` preserved until Stage 5 gates pass):

```bash
python3 scripts/orchestrator.py --project /path/company-project
python3 scripts/validate_site.py /path/company-project/site --domain https://example.com
python3 scripts/seo_geo_matrix.py citability-score --file /path/company-project/site/products.html
```

Verify all 9 pre-launch gates using the evidence-backed `Finding | Evidence | Impact | Fix` rubric:

1. Gate 0 (Site Identity & 6-Point Brand Alignment): Favicon, OG metadata, logo proportions, 6-point brand name consistency, and approved asset hashes match existing files.
2. Gate 1 (Clean URLs, Faceted Nav Guard & Technical SEO): Zero `.html` suffixes in internal links, canonicals, `og:url`, JSON-LD, or `sitemap.xml`; dynamic filter parameters canonicalize to parent Clean URLs; zero orphan pages or broken links.
3. Gate 2 (Unique TDK & Heading Hierarchy): Every page has a unique `<title>`, `<meta name="description">`, and exactly one `<h1>` aligned with its Stage 1 keyword branch.
4. Gate 3 (Fact-Source Parity & Anti-AI-Slop): Every specification table and quantitative claim traces to `content/public-facts.json`; zero placeholder text or banned AI marketing clichés.
5. Gate 4 (GEO 134-167 Word Citability & Spec Tables): Core pages achieve a composite GEO citability score >= 85 with a self-contained 134-167 word engineering answer block and semantic `<table>` specs with explicit units and conditions.
6. Gate 5 (Schema.org & Hreflang Accuracy): Valid `Organization`, `WebSite`, `BreadcrumbList`, `Product`, or `TechArticle` JSON-LD matching visible text; bidirectional `hreflang` and `x-default` for verified translations; no fabricated `Offer` prices or reliance on retired `FAQPage` rich results.
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

### Stage 6: Tri-Track B2B Backlink, Authority Article, and Brand Mention Ledger

Initialize and validate the 7-state backlink and off-site brand mention ledger:

```bash
python3 scripts/seo_geo_matrix.py init-ledger --out /path/company-project/private/backlink-ledger.json
python3 scripts/seo_geo_matrix.py validate-ledger --file /path/company-project/private/backlink-ledger.json
```

- Track A (`batch_directory`): Pre-inspect B2B directory forms, queue interactive CAPTCHAs for human review, and verify final public URLs and `rel` attributes.
- Track B (`editorial_authority`): Repurpose Spoke engineering guides and comparison tables into LinkedIn technical articles and Medium procurement guides linking back to core Hub/RFQ pages.
- Track C (`brand_mention_surface`): Build consistent off-site entity mentions across LinkedIn Company profiles, YouTube factory/QC video transcripts, and industry trade registries (which correlate 3x more strongly with AI search citations).
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
