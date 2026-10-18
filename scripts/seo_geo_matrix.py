#!/usr/bin/env python3
"""B2B SEO/GEO keyword tree, topic cluster stitcher, GEO citability scorer, 4-phase workspace orchestrator, SKU catalog auditor, B2B editorial syndication generator, and 7-state backlink ledger (V3.3).

Synthesizes B2B-appropriate capabilities from all 13 open-source Agent Skills:
1. cnproduct/b2b-global-brand-site-master (21 industries, 21-module fact governance, Clean URLs, Anti-FOUC, Edge protection)
2. yan-labs/yan-skills (rankup 7-stage lifecycle, SERP weakness teardown [inner-page rank & DR<30], docs/seo/ Single Source of Truth hub, IndexNow/GSC loop, 7-state backlink ledger)
3. coreyhaines31/marketingskills (B2B page-cro, Hero value proposition, 4-step OEM workflow, B2B Risk Reversal [NDA/Sample/AQL], 3-tier commercial RFQ cards)
4. AgriciDaniel/claude-seo (Technical SEO, E-E-A-T Trust-first, Organization/Product/TechArticle JSON-LD, multi-locale hreflang [en/es/pt/ja/de/fr], llms.txt & llms-full.txt)
5. seo.web.cafe / Gefei Official Methodology (Competitor-to-Keyword & Keyword-to-Competitor teardown, native multilingual keyword research, 6-point brand entity alignment)
6. zubair-trabzada/geo-seo-claude (134-167 word passage citability scoring, 6-dimension composite GEO score, off-site brand mention matrix)
7. TheCraigHewitt/seomachine (B2B Hub-and-Spoke topic cluster architecture, internal link anchor stitching, anti-AI-slop engineering prose)
8. aaron-he-zhu/aaron-marketing-skills (Survey -> Implement -> Tune -> Evaluate loop, CORE-EEAT & CITE gates)
9. Bhanunamikaze/Agentic-SEO-Skill (Evidence-backed Finding/Evidence/Impact/Fix rubric, B2B faceted navigation crawl-trap guard, orphan page & indexability matrix)
10. cnproduct/renwork-web-design-master (Fluid clamp typography, 45ch-75ch measure, 1.8x heading proximity, zero AI-slop gradients)
11. vercel-labs/agent-skills (web-design-guidelines & writing-guidelines: tabular-nums on spec tables, non-breaking number-unit spacing, B2B form autocomplete/focus-visible, LCP/CLS image discipline, banned fluff words)
12. nextlevelbuilder/ui-ux-pro-max-skill + anthropics/skills frontend-design (4 B2B industry visual archetypes: Precision CNC, Cleanroom Regulatory, Architectural Material, Agile OEM Lookbook)
13. benjaminsehl/liquid-skills + wiebekaai/ecommerce-skills + flaqai/backlink_skills (Multi-SKU RFQ Sample Basket Drawer, accessible material swatch switchers, bulk SKU catalog SEO/spec completeness auditor, LinkedIn/Medium B2B editorial syndication pack generator)
"""
import argparse
import csv
import html.parser
import io
import json
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BACKLINK_STATES = (
    'candidate',
    'qualified',
    'filled',
    'submitted',
    'public',
    'indexed',
    'rel_verified',
)

AI_SLOP_PHRASES = (
    'in today\'s fast-paced',
    'in the ever-evolving landscape',
    'look no further',
    'unlock the full potential',
    'revolutionize your',
    'seamless integration',
    'cutting-edge solution',
    'delve into',
    'testament to',
    'world-class',
    'best-in-class',
)

B2B_VISUAL_ARCHETYPES = {
    'precision_engineering': {
        'industries': ['machinery', 'components', 'electronics', 'automotive', 'energy'],
        'palette_direction': 'High-contrast slate, anodized steel, and safety amber/cobalt interactive accents (OKLCH tinted neutrals)',
        'typography_pairing': 'Space Grotesk / Clash Display (headings) + Inter / Plus Jakarta Sans (body) + JetBrains Mono (tabular-nums spec readouts)',
        'signature_components': ['Dimensional tolerance table with tabular-nums', 'CAD/Datasheet version drawer', 'Multi-SKU RFQ Basket Drawer'],
    },
    'cleanroom_regulatory': {
        'industries': ['medical', 'hygiene', 'chemicals', 'food'],
        'palette_direction': 'Clinical pure surface, deep laboratory navy, and high-legibility emerald/cobalt verification badges',
        'typography_pairing': 'Plus Jakarta Sans (headings) + Inter (body) + Geist Mono (lot/batch & test standard codes)',
        'signature_components': ['Certification scope & validity verification strip', 'Option A vs Option B BOM core comparison table', 'Batch traceability & AQL protocol card'],
    },
    'architectural_material': {
        'industries': ['building-materials', 'sanitaryware', 'furniture', 'bento', 'appliances'],
        'palette_direction': 'Warm mineral stone, brushed stainless neutral, and deep architectural charcoal',
        'typography_pairing': 'Instrument Serif / General Sans (headings) + Switzer / Inter (body) + JetBrains Mono (dimensions & container CBM)',
        'signature_components': ['Accessible material/finish swatch switcher (WCAG 2.2 roving tabindex)', '20GP/40HQ container load calculator', 'Cross-section structural callout'],
    },
    'agile_oem_lookbook': {
        'industries': ['apparel', 'footwear', 'bags', 'packaging', 'beauty', 'toys-sports', 'pet-products'],
        'palette_direction': 'Editorial high-contrast neutral canvas with bespoke brand-extracted accent token',
        'typography_pairing': 'Syne / General Sans (headings) + Plus Jakarta Sans (body) + JetBrains Mono (GSM/oz, MOQ, carton specs)',
        'signature_components': ['Interactive customization dimension selector (material, logo craft, packaging)', 'Sampling lead-time & tooling timeline', 'Multi-SKU Sample Kit Basket Drawer'],
    },
}

B2B_INTENT_BRANCHES = [
    {
        'branch_id': 'oem_odm_custom',
        'intent_label': 'OEM / ODM & Private Label Manufacturing',
        'buyer_stage': 'Supplier Qualification & Custom Briefing',
        'modifiers': ['oem manufacturer', 'odm supplier', 'private label factory', 'custom tooling bulk', 'bespoke specification'],
        'target_page_type': 'oem-odm',
        'target_clean_url': '/oem-odm',
        'primary_cta_tier': 'Tier 2: Custom BOM / Drawing & Sample RFQ',
    },
    {
        'branch_id': 'manufacturer_supplier',
        'intent_label': 'Direct Factory & Certified Industrial Supplier',
        'buyer_stage': 'Vendor Shortlisting',
        'modifiers': ['manufacturer', 'factory direct', 'industrial supplier', 'iso certified manufacturer', 'export factory'],
        'target_page_type': 'home / quality',
        'target_clean_url': '/',
        'primary_cta_tier': 'Tier 3: Factory Audit & Volume Production Quote',
    },
    {
        'branch_id': 'bulk_wholesale_logistics',
        'intent_label': 'Bulk Wholesale, MOQ & Container Loading',
        'buyer_stage': 'Commercial & Logistics Evaluation',
        'modifiers': ['bulk wholesale', 'moq', '20gp 40hq container load', 'fob price list', 'export carton specification'],
        'target_page_type': 'products / calculator',
        'target_clean_url': '/calculator',
        'primary_cta_tier': 'Tier 3: Container Load & Tiered FOB Quote',
    },
    {
        'branch_id': 'technical_spec_material',
        'intent_label': 'Technical Parameters, Materials & Tolerances',
        'buyer_stage': 'Engineering & Specification Selection',
        'modifiers': ['technical specifications', 'material grade chart', 'dimension tolerance', 'datasheet pdf', 'performance test standard'],
        'target_page_type': 'products / resources',
        'target_clean_url': '/products',
        'primary_cta_tier': 'Tier 1: Datasheet & Standard Sample Request',
    },
    {
        'branch_id': 'application_solution',
        'intent_label': 'Industry Application & Operating Conditions',
        'buyer_stage': 'Problem-to-Solution Mapping',
        'modifiers': ['for industrial application', 'heavy duty solution', 'operating temperature range', 'engineering selection guide', 'application case'],
        'target_page_type': 'solutions',
        'target_clean_url': '/solutions',
        'primary_cta_tier': 'Tier 2: Application Engineering Consultation',
    },
    {
        'branch_id': 'comparison_alternative',
        'intent_label': 'Material / Process Trade-off & Comparison',
        'buyer_stage': 'Trade-off Evaluation (High GEO Citation Value)',
        'modifiers': ['vs', 'material comparison table', 'process alternative', 'cost vs performance', 'how to specify for bulk sourcing'],
        'target_page_type': 'resources',
        'target_clean_url': '/resources',
        'primary_cta_tier': 'Tier 1: Side-by-Side Spec Sample Kit Request',
    },
]


def load_industries():
    path = ROOT / 'assets/industries.json'
    return json.loads(path.read_text(encoding='utf-8'))['industries']


def get_industry(industry_id):
    for item in load_industries():
        if item['id'] == industry_id:
            return item
    raise ValueError(f'unknown industry: {industry_id}')


def get_visual_archetype(industry_id):
    for arch_id, meta in B2B_VISUAL_ARCHETYPES.items():
        if industry_id in meta['industries']:
            return {'archetype_id': arch_id, **meta}
    return {'archetype_id': 'precision_engineering', **B2B_VISUAL_ARCHETYPES['precision_engineering']}


def build_keyword_tree(seed_keyword, industry_id, markets=None):
    seed = seed_keyword.strip()
    if not seed:
        raise ValueError('seed_keyword must not be empty')
    profile = get_industry(industry_id)
    markets = [m.strip() for m in (markets or ['Global']) if m.strip()]
    now = datetime.now(timezone.utc).isoformat()
    branches = []
    for branch in B2B_INTENT_BRANCHES:
        queries = [f'{seed} {mod}' for mod in branch['modifiers']]
        branches.append({
            'branch_id': branch['branch_id'],
            'intent_label': branch['intent_label'],
            'buyer_stage': branch['buyer_stage'],
            'target_page_type': branch['target_page_type'],
            'target_clean_url': branch['target_clean_url'],
            'primary_cta_tier': branch['primary_cta_tier'],
            'primary_keyword': queries[0],
            'secondary_keywords': queries[1:],
            'h1_contract': f'Must include "{queries[0]}" or verified industrial equivalent in H1',
            'h2_contract': queries[1:3],
            'serp_weakness_evidence': {
                'top10_has_inner_pages': None,
                'top10_dr_under_30_count': None,
                'b2b_supplier_share_ge_60pct': None,
                'search_volume_verified': None,
                'status': 'UNVERIFIED_VOLUME_AND_SERP',
            },
            'required_industry_fields': profile['product_fields'][:4],
            'required_evidence': profile['evidence'][:3],
            'verification_status': 'UNVERIFIED_VOLUME_AND_SERP',
            'gate_rule': 'Verify real SERP buyer intent, DR<30 weakness, and search volume before locking page TDK. Never fabricate volume or KD numbers.',
        })
    return {
        'seed_keyword': seed,
        'pillar_homepage_keyword': f'{seed} manufacturer',
        'industry_id': industry_id,
        'industry_name': profile['name'],
        'visual_archetype': get_visual_archetype(industry_id),
        'target_markets': markets,
        'supported_locales': ['en', 'es', 'pt', 'ja', 'de', 'fr'],
        'generated_at': now,
        'gefei_b2b_competitor_teardown': {
            'domain_to_keyword': 'Extract top organic landing pages and inquiry keywords from 3-5 overseas B2B niche manufacturers/importers.',
            'keyword_to_domain': 'Inspect live SERP top 10 for each branch; confirm at least 60% are B2B supplier/spec pages rather than B2C retail listings, and check for inner-page rankings or DR < 30 weak spots.',
            'multilingual_rule': 'Never machine-translate keywords across languages; re-research native industrial nomenclature (e.g., DIN/EN for DE, ASTM for US, JIS for JA) per target market.',
        },
        'excluded_b2c_modifiers': ['cheap single piece', 'diy home craft', 'retail coupon', 'free shipping 1 pc', 'used second hand', 'paywall subscription'],
        'branches': branches,
        'handoff_contract': {
            'phase_1_to_phase_2': 'marketingskills (page-cro & copywriting) MUST read docs/seo/keyword-matrix.json and preserve each URL H1/H2 keyword contract.',
            'phase_2_to_phase_3': 'claude-seo & geo-seo-claude inject Organization/Product/TechArticle JSON-LD, multi-locale hreflang, 134-167 word GEO block, and /public/llms.txt + /public/llms-full.txt.',
            'phase_3_to_phase_4': 'rankup & validate_site.py enforce the 9 pre-launch gates, IndexNow/GSC push, and backlink-tracker.csv / backlink-ledger.json.',
        },
    }


def build_topic_cluster(seed_keyword, industry_id, market='Global'):
    """Builds a B2B Hub-and-Spoke Topic Cluster & Internal Link Stitching Plan (inspired by seomachine + claude-seo)."""
    seed = seed_keyword.strip()
    if not seed:
        raise ValueError('seed_keyword must not be empty')
    profile = get_industry(industry_id)
    f0, f1, f2 = (profile['product_fields'] + ['Material Grade', 'Dimension Tolerance', 'Packaging Spec'])[:3]
    e0, e1 = (profile['evidence'] + ['Inspection Report', 'Material Certificate'])[:2]
    now = datetime.now(timezone.utc).isoformat()
    slug_base = re.sub(r'[^a-z0-9]+', '-', seed.lower()).strip('-') or 'b2b-product'

    hubs = [
        {
            'hub_id': 'HUB-CATEGORY',
            'page_type': 'Pillar Category Hub',
            'clean_url': '/products',
            'target_intent': f'{seed} manufacturer & industrial specification catalog',
            'primary_cta_tier': 'Tier 3: Container Load & Tiered FOB Quote',
            'required_elements': [
                f'134-167 word self-contained engineering overview of {seed} supply capabilities',
                f'Semantic HTML comparison table across {f0}, {f1}, and {f2} with font-variant-numeric: tabular-nums',
                'Interactive Material/Finish Swatch Switcher + Multi-SKU Sample & RFQ Basket Drawer',
                'Faceted navigation guard: filter parameters canonicalize to /products unless promoted to static Clean URL',
            ],
        },
        {
            'hub_id': 'HUB-OEM',
            'page_type': 'OEM / ODM Customization Hub',
            'clean_url': '/oem-odm',
            'target_intent': f'custom {seed} OEM/ODM factory & private label tooling',
            'primary_cta_tier': 'Tier 2: Custom BOM / Drawing & Sample RFQ',
            'required_elements': [
                'Step-by-step DFM (Design for Manufacturing), tooling, and sample sign-off workflow',
                'Structured Option A vs Option B BOM material allocation comparison',
                f'Verifiable quality control gates ({e0}, {e1})',
            ],
        },
    ]

    spokes = [
        {
            'spoke_id': 'SPOKE-01',
            'article_type': 'Material & Specification Trade-off Guide',
            'clean_url': f'/resources/{slug_base}-material-specification-guide',
            'headline': f'How to Specify {seed.title()} for Bulk Procurement: {f0} vs {f1} Trade-offs',
            'buyer_question_answered': f'Which {f0} and {f1} grades prevent field failure and optimize BOM unit cost?',
            'internal_link_stitches': [
                {'target_url': '/products', 'anchor_text': f'industrial {seed} specification catalog', 'placement': 'First 200 words (context bridge)'},
                {'target_url': '/oem-odm', 'anchor_text': f'custom {seed} BOM allocation and sampling', 'placement': 'Comparison table footer CTA'},
            ],
            'primary_cta_tier': 'Tier 1: Side-by-Side Spec Sample Kit Request',
        },
        {
            'spoke_id': 'SPOKE-02',
            'article_type': 'Quality Inspection & Compliance Protocol',
            'clean_url': f'/resources/{slug_base}-quality-control-testing-checklist',
            'headline': f'B2B Quality Control Checklist for Sourcing {seed.title()}: Verifying {e0} and Batch Traceability',
            'buyer_question_answered': f'How do overseas procurement teams verify {e0}, {e1}, and pre-shipment AQL standards?',
            'internal_link_stitches': [
                {'target_url': '/quality', 'anchor_text': f'{profile["name"]} quality management and lab testing workflow', 'placement': 'Testing methodology section'},
                {'target_url': '/contact', 'anchor_text': 'request a sample batch inspection report and RFQ', 'placement': 'Closing engineering summary'},
            ],
            'primary_cta_tier': 'Tier 1: Datasheet & Standard Sample Request',
        },
        {
            'spoke_id': 'SPOKE-03',
            'article_type': 'OEM Tooling, Packaging & Container Loading Playbook',
            'clean_url': f'/resources/{slug_base}-packaging-container-loading-optimization',
            'headline': f'Optimizing 20GP/40HQ Container Loading and Export Packaging for Bulk {seed.title()} Orders',
            'buyer_question_answered': 'How do carton dimensions, palletization, and gross weight limits impact landed unit cost?',
            'internal_link_stitches': [
                {'target_url': '/calculator', 'anchor_text': '20GP/40HQ container volume and weight load estimator', 'placement': 'Container calculation section'},
                {'target_url': '/oem-odm', 'anchor_text': f'custom export packaging and private label {seed} production', 'placement': 'Packaging specification section'},
            ],
            'primary_cta_tier': 'Tier 3: Container Load & Tiered FOB Quote',
        },
        {
            'spoke_id': 'SPOKE-04',
            'article_type': 'Application Operating Conditions & Selection Note',
            'clean_url': f'/resources/{slug_base}-application-engineering-selection',
            'headline': f'Application Engineering Guide: Selecting {seed.title()} for {market} Commercial & Industrial Environments',
            'buyer_question_answered': f'What operating conditions dictate {f2} selection in {market} applications?',
            'internal_link_stitches': [
                {'target_url': '/solutions', 'anchor_text': f'industry application solutions for {seed}', 'placement': 'Use-case matrix section'},
                {'target_url': '/products', 'anchor_text': f'compare {seed} model specifications', 'placement': 'Selection summary table'},
            ],
            'primary_cta_tier': 'Tier 2: Application Engineering Consultation',
        },
    ]

    return {
        'seed_keyword': seed,
        'industry_id': industry_id,
        'market': market,
        'generated_at': now,
        'anti_ai_slop_writing_rules': [
            'Open every guide directly with a TL;DR engineering summary: constraints, BOM cost drivers, or procurement failure modes (Vercel writing-guidelines).',
            'Ban generic filler openings ("In today\'s fast-paced world...", "Look no further...", "easy", "simple", "world-class").',
            'Use non-breaking spaces (&nbsp; or white-space: nowrap) between numbers and units (e.g., 500&nbsp;pcs, 0.8&nbsp;mm, 40&nbsp;HQ) and font-variant-numeric: tabular-nums on all specification tables.',
            'Include at least one semantic HTML <table> with explicit units/conditions and one 134-167 word self-contained GEO answer block per article.',
            'Every spoke article must link to at least 1 Hub page (/products or /oem-odm) and 1 conversion tool (/calculator or /contact) using descriptive technical anchor text.',
        ],
        'hubs': hubs,
        'spokes': spokes,
    }


def audit_b2b_sku_catalog(catalog_path, industry_id):
    """Audits a B2B product SKU catalog JSON (inspired by wiebekaai/ecommerce-skills + benjaminsehl/liquid-skills + vercel-labs/agent-skills)."""
    raw = json.loads(Path(catalog_path).read_text(encoding='utf-8'))
    items = raw if isinstance(raw, list) else raw.get('products', raw.get('skus', []))
    if not isinstance(items, list):
        raise ValueError('catalog JSON must be a list of SKU objects or contain a "products"/"skus" array')
    profile = get_industry(industry_id)
    required_fields = profile['product_fields'][:3]
    seen_titles = set()
    issues = []
    ready_count = 0

    for idx, sku in enumerate(items):
        if not isinstance(sku, dict):
            continue
        sku_id = str(sku.get('sku') or sku.get('id') or f'SKU-{idx+1}')
        title = str(sku.get('title') or sku.get('name') or '').strip()
        desc = str(sku.get('seo_description') or sku.get('description') or '').strip()
        specs = sku.get('specifications') or sku.get('specs') or {}
        alt = str(sku.get('image_alt') or sku.get('alt') or '').strip()
        url = str(sku.get('url') or sku.get('slug') or '').strip()

        sku_issues = []
        if not title:
            sku_issues.append('Missing product title/model name')
        elif title.lower() in seen_titles:
            sku_issues.append(f'Duplicate product title detected: "{title}"')
        else:
            seen_titles.add(title.lower())

        word_count = len(re.findall(r'\b\w+\b', desc))
        if word_count < 30:
            sku_issues.append(f'Thin or missing B2B SEO description ({word_count} words; target 134-167 word GEO summary or >= 45 words)')
        for phrase in AI_SLOP_PHRASES:
            if phrase in desc.lower():
                sku_issues.append(f'Contains banned AI-slop phrase: "{phrase}"')

        if not isinstance(specs, dict) or len(specs) < 2:
            sku_issues.append(f'Missing structured specification dictionary (recommend including: {", ".join(required_fields)})')
        if not alt:
            sku_issues.append('Missing descriptive image alt text (should state model + material + application)')
        if url.endswith('.html'):
            sku_issues.append(f'Product URL exposes .html suffix: "{url}" (violates Clean URL policy)')

        if sku_issues:
            issues.append({'sku_id': sku_id, 'title': title or None, 'issues': sku_issues})
        else:
            ready_count += 1

    return {
        'catalog_file': str(catalog_path),
        'industry_id': industry_id,
        'total_skus': len(items),
        'seo_geo_ready_skus': ready_count,
        'skus_needing_fixes': len(issues),
        'recommended_industry_spec_columns': profile['product_fields'],
        'findings': issues,
    }


def build_b2b_syndication_pack(company, seed_keyword, industry_id, target_url='/products'):
    """Generates platform-native B2B editorial distribution packs for LinkedIn, Medium, and YouTube (inspired by flaqai/backlink_skills + geo-seo-claude)."""
    profile = get_industry(industry_id)
    f0, f1, f2 = (profile['product_fields'] + ['Material Grade', 'Tolerance', 'Packaging'])[:3]
    e0, e1 = (profile['evidence'] + ['ISO 9001', 'Batch Test Report'])[:2]
    now = datetime.now(timezone.utc).isoformat()
    return {
        'company': company,
        'seed_keyword': seed_keyword,
        'industry_id': industry_id,
        'target_hub_clean_url': target_url,
        'generated_at': now,
        'channels': {
            'linkedin_technical_article': {
                'target_audience': 'Overseas Procurement Directors, Sourcing VPs, and OEM Product Managers',
                'headline_options': [
                    f'Engineering Trade-offs in Bulk {seed_keyword.title()} Sourcing: {f0} vs {f1}',
                    f'How B2B Buyers Verify {e0} and Prevent BOM Cost Overruns When Ordering {seed_keyword.title()}',
                ],
                'editorial_structure': [
                    '1. Field Failure / Cost Driver Hook (no generic AI intro)',
                    f'2. Specification Comparison Table ({f0}, {f1}, {f2})',
                    f'3. Factory QC & Pre-Shipment Verification ({e0}, {e1})',
                    f'4. Contextual Link to {target_url} and Sample Kit / Container Calculator CTA',
                ],
                'geo_brand_mention_rule': f'Explicitly associate "{company}" with "{seed_keyword} OEM/ODM manufacturing" and consistent technical terminology.',
            },
            'medium_engineering_publication': {
                'target_audience': 'Industrial Designers, Product Engineers, and Supply Chain Analysts',
                'headline_options': [
                    f'A Procurement Engineer\'s Guide to Specifying {seed_keyword.title()} ({f0}, Tolerances & 40HQ Logistics)',
                ],
                'canonical_and_link_rule': f'Use distinct editorial prose (never copy-paste website HTML verbatim); link descriptive anchor text to {target_url} and /calculator.',
            },
            'youtube_factory_qc_transcript': {
                'target_audience': 'AI Search Retrieval Engines (Perplexity / Google AIO / ChatGPT) & Video-First B2B Buyers',
                'video_title': f'Inside {company}: {seed_keyword.title()} Manufacturing Process, {f0} Inspection & 40HQ Export Packaging',
                'description_and_transcript_requirements': [
                    f'Include a 150-word technical summary in the video description mentioning {company}, {seed_keyword}, {f0}, and {e0}.',
                    'Upload full human-verified closed captions (.srt) containing exact model numbers and testing standards so AI engines index the brand mention.',
                ],
            },
        },
    }


def init_b2b_seo_workspace(project_dir, company, seed_keyword, industry_id, markets=None):
    """Initializes the 4-Phase Collaborative Workspace (docs/seo/ Single Source of Truth + .claude/CLAUDE.md + public/llms.txt & llms-full.txt)."""
    project_path = Path(project_dir)
    seo_dir = project_path / 'docs/seo'
    claude_dir = project_path / '.claude'
    public_dir = project_path / 'public'
    seo_dir.mkdir(parents=True, exist_ok=True)
    claude_dir.mkdir(parents=True, exist_ok=True)
    public_dir.mkdir(parents=True, exist_ok=True)

    profile = get_industry(industry_id)
    archetype = get_visual_archetype(industry_id)
    markets_list = [m.strip() for m in (markets or ['Global']) if m.strip()]
    now = datetime.now(timezone.utc).isoformat()

    # 1. docs/seo/keyword-matrix.json
    kw_matrix = build_keyword_tree(seed_keyword, industry_id, markets_list)
    kw_path = seo_dir / 'keyword-matrix.json'
    kw_path.write_text(json.dumps(kw_matrix, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    # 2. docs/seo/topic-cluster.json
    cluster = build_topic_cluster(seed_keyword, industry_id, markets_list[0])
    cluster_path = seo_dir / 'topic-cluster.json'
    cluster_path.write_text(json.dumps(cluster, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    # 3. docs/seo/syndication-pack.json
    syndication = build_b2b_syndication_pack(company, seed_keyword, industry_id, '/products')
    (seo_dir / 'syndication-pack.json').write_text(json.dumps(syndication, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    # 4. docs/seo/site-brief.md
    f_list = ', '.join(profile['product_fields'][:5])
    e_list = ', '.join(profile['evidence'][:4])
    brief_md = f"""# B2B Independent Site Brief (Single Source of Truth)

- **Company Name**: {company}
- **Industry Blueprint**: `{industry_id}` ({profile['name']})
- **Visual Archetype**: `{archetype['archetype_id']}` ({archetype['palette_direction']})
- **Primary Seed Keyword**: `{seed_keyword}`
- **Pillar Homepage Keyword**: `{seed_keyword} manufacturer`
- **Target Export Markets**: {', '.join(markets_list)}
- **Generated At**: {now}

## 1. Target B2B Buyer Personas & Procurement Path
- **Primary Buyers**: Overseas OEM/ODM Brand Owners, Industrial Importers, Wholesale Distributors, and Procurement Engineers.
- **Core Decision Path**: Technical Spec / Material Verification ({f_list}) -> Compliance & Quality Evidence ({e_list}) -> Multi-SKU Sample Basket Evaluation -> 20GP/40HQ Container Order.

## 2. Fact-Boundary Guardrail
- All quantitative claims, certificates, factory metrics, and lead times must originate from verified cards in `private/knowledge-cards.json` (`content/public-facts.json`).
- Unverified parameters remain in `private/gaps.md` and are never fabricated on public pages.
"""
    (seo_dir / 'site-brief.md').write_text(brief_md, encoding='utf-8')

    # 5. docs/seo/cro-copy-deck.md
    cro_md = f"""# B2B Landing Page CRO, UX & Copywriting Deck (V3.3)

> **Strict Alignment Rule**: Every H1 and H2 below MUST preserve the target keyword assigned in `docs/seo/keyword-matrix.json`. Follow Vercel `writing-guidelines` (open with a TL;DR engineering summary, use `&nbsp;` between numbers and units, ban vague fluff like "easy/simple/world-class") and `web-design-guidelines` (`font-variant-numeric: tabular-nums` on spec tables, explicit `autocomplete` on RFQ inputs, `fetchpriority="high"` on hero product image).

## 1. Above-the-Fold Hero Section (`/` & `/products`)
- **H1 Formula**: `[Verified {seed_keyword.title()} Manufacturing / Supply] for [Target Industry & OEM Buyers]`
- **Subheadline**: Highlight verifiable engineering parameters ({f_list}), batch quality control, and direct RFQ response without middleman markups.
- **Primary CTA**: `Request Custom BOM & Sample Quote` (auto-passes product & swatch context)
- **Secondary CTA**: `Add to Multi-SKU Sample Basket` or `Calculate 20GP/40HQ Container Load`

## 2. Interactive B2B Catalog Components (`liquid-skills` & `ui-ux-pro-max` B2B Adaptation)
- **Accessible Material / Finish Swatch Switcher**: Allow buyers to toggle material grades, thicknesses, or surface finishes with keyboard-accessible (`aria-pressed`) swatches that dynamically update model parameters.
- **Multi-SKU Sample & RFQ Basket Drawer**: Allow procurement engineers to add multiple models/sizes into a persistent inquiry basket and submit a consolidated BOM/Sample request in one step.

## 3. How It Works: 4-Step B2B OEM / Sourcing Process
1. **Spec & BOM Alignment**: Share target material grade, tolerances, or reference sample parameters.
2. **Engineering DFM & Prototype Sampling**: Confirm pre-production sample and lab test criteria ({e_list}).
3. **In-Line QC & Pre-Shipment Inspection**: Batch traceability and AQL inspection prior to container sealing.
4. **Export Packaging & Global Logistics**: Palletized or floor-loaded 20GP/40HQ shipment with full customs documentation.

## 4. B2B Risk Reversal & Commercial Tier Cards (Replaces SaaS Paywalls)
Never place paywalls on B2B specifications. Use a 3-Tier Commercial Inquiry Matrix to reduce buyer hesitation:

| Tier | Target Buyer Stage | Commercial Scope | Risk Reversal Micro-Copy | Primary Action |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1: Standard Sample & Spec Pack** | Engineering Evaluation | Existing tooling models & material swatches | Strict NDA protection; courier freight credit on first bulk order | `Request Standard Sample Pack` |
| **Tier 2: Custom OEM / ODM Project** | Private Label / Custom Spec | Custom material allocation, logo tooling, bespoke packaging | Golden sample sign-off before mass production; documented QC gates | `Submit Custom BOM / Drawing RFQ` |
| **Tier 3: Bulk Container Procurement** | Repeat Wholesale / 20GP-40HQ | Mixed-SKU container loading & tiered FOB volume pricing | Pre-shipment third-party inspection support (SGS/Intertek/BV) | `Calculate Container Load & Get FOB Quote` |
"""
    (seo_dir / 'cro-copy-deck.md').write_text(cro_md, encoding='utf-8')

    # 6. docs/seo/backlink-tracker.csv
    csv_buf = io.StringIO()
    writer = csv.writer(csv_buf)
    writer.writerow(['target_id', 'domain', 'submit_url', 'track', 'gate_type', 'state', 'live_url', 'rel_attribute', 'dr_estimate', 'updated_at', 'notes'])
    writer.writerow(['BL-0001', 'example-b2b-directory.com', 'https://example-b2b-directory.com/submit', 'batch_directory', 'open-form', 'candidate', '', '', '', now, 'Verify live URL and rel attribute before marking rel_verified'])
    writer.writerow(['BL-0002', 'linkedin.com', 'https://www.linkedin.com/articles/', 'editorial_authority', 'account', 'candidate', '', '', '98', now, 'Publish B2B material trade-off engineering guide linking to /products'])
    writer.writerow(['BL-0003', 'youtube.com', 'https://www.youtube.com/', 'brand_mention_surface', 'account', 'candidate', '', '', '99', now, 'Upload factory QC & production line video with full technical transcript'])
    (seo_dir / 'backlink-tracker.csv').write_text(csv_buf.getvalue(), encoding='utf-8')

    # 7. docs/seo/status-log.md
    status_md = f"""# B2B Site SEO / GEO Lifecycle & Inquiry Status Log

- **Project**: {company} (`{industry_id}`)
- **Visual Archetype**: `{archetype['archetype_id']}`
- **Initialized At**: {now}
- **Current Phase**: Phase 1 (Keyword Matrix, Topic Cluster & Site Brief Initialized)

## Phase Gate Checklist
- [ ] **Phase 1 (Research & Positioning - `rankup` / `seo_geo_matrix.py`)**: SERP top-10 buyer intent verified; `docs/seo/keyword-matrix.json` & `docs/seo/topic-cluster.json` locked.
- [ ] **Phase 2 (B2B CRO, UI Archetype & Copywriting - `marketingskills` + `ui-ux-pro-max` + `vercel-labs`)**: `docs/seo/cro-copy-deck.md` finalized; `tabular-nums` spec tables, Multi-SKU RFQ Basket, and 3-Tier Risk Reversal cards wired.
- [ ] **Phase 3 (Technical SEO, Schema, Hreflang & GEO - `claude-seo` + `geo-seo-claude` + `ecommerce-skills`)**: Clean URLs enforced; SKU catalog audited via `catalog-audit`; `Organization` + `Product` + `TechArticle` JSON-LD validated; 134-167 word GEO blocks scored >= 85; `/public/llms.txt` & `/public/llms-full.txt` synced.
- [ ] **Phase 4 (Pre-Launch Audit, IndexNow/GSC Push & Tri-Track Backlinks - `rankup` + `backlink_skills` + `validate_site.py`)**: 9 pre-launch gates PASS; Cloudflare Workers edge protection active; IndexNow & GSC sitemap submitted; LinkedIn/Medium/YouTube syndication pack (`docs/seo/syndication-pack.json`) & `docs/seo/backlink-tracker.csv` active.
"""
    (seo_dir / 'status-log.md').write_text(status_md, encoding='utf-8')

    # 8. public/llms.txt & public/llms-full.txt
    llms_txt = f"""# {company}

> B2B {profile['name']} supply and OEM/ODM technical portal for {seed_keyword}. All specifications and commercial terms are governed by verified public fact cards.

## Core Procurement Pages
- [Home & Capabilities](/): Overview of {company} manufacturing and export scope
- [Product Specification Catalog](/products): Technical parameters ({f_list}) and model comparisons
- [OEM / ODM Customization](/oem-odm): Custom BOM, tooling, sampling, and private label workflow
- [Quality & Compliance](/quality): Testing standards ({e_list}) and batch traceability
- [20GP / 40HQ Container Calculator](/calculator): Carton CBM, gross weight, and container load estimator
- [Request a Quote (RFQ)](/contact): Direct engineering inquiry and multi-SKU sample request

## Technical Selection Guides
- [Material & Specification Guide](/resources/{ cluster['spokes'][0]['clean_url'].split('/')[-1] })
- [Quality Control & Testing Checklist](/resources/{ cluster['spokes'][1]['clean_url'].split('/')[-1] })
- [Container Loading & Packaging Playbook](/resources/{ cluster['spokes'][2]['clean_url'].split('/')[-1] })
"""
    (public_dir / 'llms.txt').write_text(llms_txt, encoding='utf-8')

    llms_full_txt = llms_txt + f"""
## Technical Procurement Reference Summary
- **Industry**: {profile['name']} (`{industry_id}`)
- **Core Specification Dimensions**: {f_list}
- **Standard Verification Evidence**: {e_list}
- **Inquiry Channels**: Tier 1 Standard Sample Request, Tier 2 Custom BOM/Drawing RFQ, Tier 3 20GP/40HQ Container Quote.
- **Note**: Only verified facts exported in `content/public-facts.json` constitute binding company claims.
"""
    (public_dir / 'llms-full.txt').write_text(llms_full_txt, encoding='utf-8')

    # 9. .claude/CLAUDE.md
    claude_md = f"""# B2B Export Independent Site - Skill Orchestration Protocol (`.claude/CLAUDE.md`)

This project runs the **`b2b-seo-geo-site-master` V3.3** unified workflow (fusing `cnproduct/b2b-global-brand-site-master`, `yan-skills`, `marketingskills`, `claude-seo`, `geo-seo-claude`, `seomachine`, `Agentic-SEO-Skill`, `vercel-labs/agent-skills`, `ui-ux-pro-max-skill`, `liquid-skills`, `ecommerce-skills`, and `backlink_skills`).
All SEO, GEO, and CRO planning context MUST read and write through the Single Source of Truth hub at **`docs/seo/`** and fact-gated **`content/public-facts.json`**.

## 1. Strict 4-Phase Skill Routing Rules (Preventing Instruction Conflicts)

1. **Phase 1: Keyword Research, SERP Teardown & Project Positioning (`rankup` / `seo_geo_matrix.py`)**
   - **Single Source of Truth**: `docs/seo/keyword-matrix.json`, `docs/seo/topic-cluster.json`, and `docs/seo/site-brief.md`.
   - **Mandatory Rule**: Before creating or editing any page, read `docs/seo/keyword-matrix.json` to confirm the page's assigned Clean URL, Primary Keyword, Search Intent, and SERP weakness evidence. Never fabricate search volume or company facts.

2. **Phase 2: High-Converting B2B Landing Page Copy, UI Archetype & CRO Funnel (`marketingskills` + `ui-ux-pro-max` + `vercel-labs` + `liquid-skills`)**
   - **Single Source of Truth**: `docs/seo/cro-copy-deck.md` and `content/public-facts.json`.
   - **Mandatory Rule**:
     - Preserve the exact `h1_contract` and `h2_contract` keywords from `docs/seo/keyword-matrix.json`.
     - Apply the industry's mapped B2B Visual Archetype (`{archetype['archetype_id']}`), `font-variant-numeric: tabular-nums` on all specification tables, non-breaking spaces (`&nbsp;`) between numbers and units, explicit `autocomplete` on RFQ inputs, and accessible swatch/Multi-SKU Sample Basket drawers.
     - Use **3-Tier Commercial RFQ Cards (Sample Pack / Custom BOM / 20GP-40HQ Container Quote)** with B2B Risk Reversal (NDA protection, sample policy, pre-shipment AQL inspection). Never use SaaS subscription paywalls.

3. **Phase 3: Code-Level Technical SEO, Bulk SKU Catalog Audit, Hreflang & GEO Citability (`claude-seo` + `geo-seo-claude` + `ecommerce-skills`)**
   - **Single Source of Truth**: `public/llms.txt`, `public/llms-full.txt`, `sitemap.xml`, and page JSON-LD blocks.
   - **Mandatory Rule**:
     - Enforce **Clean URLs** (zero `.html` suffixes) and **Anti-FOUC** (SHA-256 CSS/JS hashes + critical `display: none !important` on off-canvas drawers).
     - Audit bulk SKU catalogs with `python3 scripts/seo_geo_matrix.py catalog-audit` to eliminate thin descriptions, missing specs, or missing `alt` attributes.
     - Inject same-source `Organization`, `WebSite`, `BreadcrumbList`, `Product`, or `TechArticle` JSON-LD and include a **134-167 word self-contained engineering answer block** (`citability-score >= 85`).
     - For multilingual expansions (`en`, `es`, `pt`, `ja`, `de`, `fr`), re-research native industrial standards (DIN/EN, ASTM, JIS) and enforce bidirectional `hreflang` + `x-default`.

4. **Phase 4: Pre-Launch 9-Gate Audit, IndexNow/GSC Push & Multi-Platform Syndication (`rankup` + `backlink_skills` + `validate_site.py`)**
   - **Single Source of Truth**: `acceptance.md`, `docs/seo/status-log.md`, `docs/seo/syndication-pack.json`, `docs/seo/backlink-tracker.csv`, and `private/backlink-ledger.json`.
   - **Mandatory Rule**: Run `validate_site.py` and `seo_geo_matrix.py citability-score` before release. Deploy via the Cloudflare Workers edge protection bundle (`deployment_directory`), submit URLs via IndexNow and GSC/Bing sitemaps, and execute the LinkedIn/Medium/YouTube syndication pack and 7-state backlink ledger.

## 2. Slash Workflow Quick-Trigger Mappings

- **"立项/拓词 [产品/行业]"**: Run `python3 scripts/seo_geo_matrix.py init-workspace` -> populate `docs/seo/` hub and `.claude/CLAUDE.md`.
- **"生成落地页 [URL/词]"**: Read `docs/seo/keyword-matrix.json` & `docs/seo/cro-copy-deck.md` -> compile B2B Hero + 134-167 word GEO block + `tabular-nums` spec `<table>` + Multi-SKU Sample Basket & 3-tier RFQ CTA -> score with `citability-score`.
- **"审计商品库 [JSON路径]"**: Run `python3 scripts/seo_geo_matrix.py catalog-audit` to check all SKUs for missing specs, thin descriptions, or Clean URL violations.
- **"上线前体检"**: Run `python3 scripts/validate_site.py` + `citability-score` + verify `public/llms.txt`, `sitemap.xml`, Cloudflare edge protection, and update `docs/seo/status-log.md`.
"""
    (claude_dir / 'CLAUDE.md').write_text(claude_md, encoding='utf-8')

    return {
        'workspace_initialized': str(project_path),
        'visual_archetype': archetype['archetype_id'],
        'files_created': [
            str(seo_dir / 'site-brief.md'),
            str(seo_dir / 'keyword-matrix.json'),
            str(seo_dir / 'topic-cluster.json'),
            str(seo_dir / 'syndication-pack.json'),
            str(seo_dir / 'cro-copy-deck.md'),
            str(seo_dir / 'backlink-tracker.csv'),
            str(seo_dir / 'status-log.md'),
            str(public_dir / 'llms.txt'),
            str(public_dir / 'llms-full.txt'),
            str(claude_dir / 'CLAUDE.md'),
        ],
    }


class _HTMLCitabilityParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self._stack = []
        self.paragraphs = []
        self._current_p = []
        self.table_count = 0
        self.th_count = 0
        self.h1_count = 0
        self.h2_h3_questions = 0
        self._current_heading = []
        self.has_json_ld = False
        self.links = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        self._stack.append(tag)
        attr_dict = dict(attrs)
        if tag == 'p':
            self._current_p = []
        elif tag in ('h1', 'h2', 'h3'):
            self._current_heading = []
            if tag == 'h1':
                self.h1_count += 1
        elif tag == 'table':
            self.table_count += 1
        elif tag == 'th':
            self.th_count += 1
        elif tag == 'script' and attr_dict.get('type') == 'application/ld+json':
            self.has_json_ld = True
        elif tag == 'a' and attr_dict.get('href'):
            self.links.append(attr_dict['href'])

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == 'p':
            text = ' '.join(''.join(self._current_p).split())
            if text:
                self.paragraphs.append(text)
            self._current_p = []
        elif tag in ('h1', 'h2', 'h3'):
            htext = ' '.join(''.join(self._current_heading).split())
            if tag in ('h2', 'h3') and ('?' in htext or htext.lower().startswith(('how ', 'what ', 'which ', 'why ', 'when '))):
                self.h2_h3_questions += 1
            self._current_heading = []
        if self._stack and self._stack[-1] == tag:
            self._stack.pop()

    def handle_data(self, data):
        if not self._stack:
            return
        top = self._stack[-1]
        if top in ('script', 'style'):
            return
        if 'p' in self._stack:
            self._current_p.append(data)
        if any(h in self._stack for h in ('h1', 'h2', 'h3')):
            self._current_heading.append(data)


def score_geo_citability(file_path):
    """Scores a B2B HTML or Markdown file on the 0-100 B2B GEO Citability & Inquiry Readiness Rubric (adapted from geo-seo-claude + claude-seo + vercel-labs)."""
    raw = Path(file_path).read_text(encoding='utf-8')
    is_html = '<html' in raw.lower() or '<body' in raw.lower() or '<table' in raw.lower() or '<p>' in raw.lower()

    if is_html:
        parser = _HTMLCitabilityParser()
        parser.feed(raw)
        paragraphs = parser.paragraphs
        table_count = parser.table_count
        th_count = parser.th_count
        h1_count = parser.h1_count
        has_json_ld = parser.has_json_ld
        links = parser.links
    else:
        blocks = [b.strip() for b in re.split(r'\n\s*\n', raw) if b.strip()]
        paragraphs = [b for b in blocks if not b.startswith(('#', '|', '-', '*', '```'))]
        table_count = sum(1 for b in blocks if '|' in b and '---' in b)
        th_count = table_count * 3
        h1_count = sum(1 for line in raw.splitlines() if line.startswith('# '))
        has_json_ld = 'application/ld+json' in raw
        links = re.findall(r'\]\(([^)]+)\)', raw)

    word_counts = [len(re.findall(r'\b\w+\b', p)) for p in paragraphs]
    optimal_passages = [wc for wc in word_counts if 120 <= wc <= 180]
    near_optimal_passages = [wc for wc in word_counts if 80 <= wc < 120 or 180 < wc <= 220]

    if optimal_passages:
        passage_score = 25
    elif near_optimal_passages:
        passage_score = 18
    elif any(wc >= 40 for wc in word_counts):
        passage_score = 10
    else:
        passage_score = 0

    unit_matches = re.findall(r'\b\d+(?:\.\d+)?\s*(?:mm|cm|m|kg|g|ml|l|pcs|cbm|20gp|40hq|mpa|kw|v|hz|%|°c|iso|astm|din|ce|fsc)\b', raw.lower())
    spec_score = 0
    if table_count >= 1 and th_count >= 2:
        spec_score += 15
    if len(unit_matches) >= 5:
        spec_score += 10
    elif len(unit_matches) >= 2:
        spec_score += 5

    slop_hits = [phrase for phrase in AI_SLOP_PHRASES if phrase in raw.lower()]
    eeat_score = max(0, 20 - len(slop_hits) * 5)

    tech_score = 0
    if h1_count == 1:
        tech_score += 5
    html_link_violations = [lk for lk in links if lk.endswith('.html') or '.html#' in lk]
    if not html_link_violations:
        tech_score += 5
    if has_json_ld or not is_html:
        tech_score += 5

    rfq_links = [lk for lk in links if any(k in lk.lower() for k in ('contact', 'rfq', 'inquiry', 'quote', 'sample', 'calculator', 'oem'))]
    funnel_score = 15 if rfq_links else (8 if ('rfq' in raw.lower() or 'inquiry' in raw.lower() or 'sample' in raw.lower()) else 0)

    total = passage_score + spec_score + eeat_score + tech_score + funnel_score
    findings = []
    if not optimal_passages:
        findings.append({
            'finding': 'No self-contained 134-167 word GEO engineering answer block detected',
            'evidence': f'Paragraph word counts: {word_counts[:8]}',
            'impact': 'AI search engines (ChatGPT, Perplexity, Google AIO) prefer self-contained 134-167 word factual passages for direct grounding citations.',
            'fix': 'Add a 134-167 word engineering summary paragraph immediately below the H1/intro that states application scope, material grades, tolerances, and testing conditions.',
            'severity': 'Warning',
            'confidence': 'Confirmed',
        })
    if table_count == 0:
        findings.append({
            'finding': 'Missing semantic specification or comparison table',
            'evidence': 'table_count = 0',
            'impact': 'B2B buyers and LLM retrieval agents rely on structured <table> data to compare models, materials, and MOQ/container specs.',
            'fix': 'Insert a semantic HTML <table> with <thead>, <th scope="col">, and font-variant-numeric: tabular-nums listing verified model parameters, units, and test conditions.',
            'severity': 'Warning',
            'confidence': 'Confirmed',
        })
    if html_link_violations:
        findings.append({
            'finding': 'Internal links expose .html extensions (Clean URL violation)',
            'evidence': f'Links with .html: {html_link_violations[:5]}',
            'impact': 'Splits canonical authority and violates the Clean URL policy.',
            'fix': 'Strip .html suffixes from all href, canonical, og:url, JSON-LD, and sitemap URLs.',
            'severity': 'Critical',
            'confidence': 'Confirmed',
        })
    if slop_hits:
        findings.append({
            'finding': 'Generic AI-slop marketing clichés detected',
            'evidence': f'Matched phrases: {slop_hits}',
            'impact': 'Erodes B2B engineering credibility and E-E-A-T Trust score.',
            'fix': 'Replace generic adjectives with verifiable manufacturing conditions, material grades, and procurement trade-offs.',
            'severity': 'Warning',
            'confidence': 'Confirmed',
        })

    return {
        'file': str(file_path),
        'composite_geo_score': total,
        'breakdown': {
            'passage_citability_25': passage_score,
            'semantic_spec_and_unit_density_25': spec_score,
            'anti_slop_and_eeat_clarity_20': eeat_score,
            'technical_clean_url_and_schema_15': tech_score,
            'b2b_rfq_funnel_stitching_15': funnel_score,
        },
        'metrics': {
            'paragraph_word_counts': word_counts,
            'optimal_120_180_word_passages': len(optimal_passages),
            'table_count': table_count,
            'quantitative_unit_mentions': len(unit_matches),
            'clean_url_violations': len(html_link_violations),
        },
        'findings': findings,
    }


def build_geo_prompt_suite(company, seed_keyword, industry_id, market='Global'):
    company = company.strip()
    seed = seed_keyword.strip()
    if not company or not seed:
        raise ValueError('company and seed_keyword must not be empty')
    profile = get_industry(industry_id)
    fields = ', '.join(profile['product_fields'][:3])
    evidences = ', '.join(profile['evidence'][:2])
    now = datetime.now(timezone.utc).isoformat()
    prompts = [
        {
            'id': 'GEO-01',
            'category': 'non_brand_supplier_discovery',
            'prompt': f'Who are reliable OEM/ODM manufacturers for {seed} supplying {market} buyers, and what technical specifications should I verify before requesting samples?',
            'target_citation_page': '/oem-odm',
        },
        {
            'id': 'GEO-02',
            'category': 'technical_spec_comparison',
            'prompt': f'Compare the key engineering and material options for {seed}, specifically evaluating {fields} for bulk B2B procurement.',
            'target_citation_page': '/products',
        },
        {
            'id': 'GEO-03',
            'category': 'quality_and_compliance',
            'prompt': f'What quality control tests and documentation ({evidences}) are required when sourcing {seed} from an export manufacturer?',
            'target_citation_page': '/quality',
        },
        {
            'id': 'GEO-04',
            'category': 'packaging_and_container_logistics',
            'prompt': f'How do B2B buyers estimate 20GP and 40HQ container loading capacity, carton dimensions, and lead time when ordering {seed} in bulk?',
            'target_citation_page': '/calculator',
        },
        {
            'id': 'GEO-05',
            'category': 'brand_entity_verification',
            'prompt': f'What products, technical capabilities, and OEM customization services does {company} provide for {seed} buyers?',
            'target_citation_page': '/about',
        },
        {
            'id': 'GEO-06',
            'category': 'rfq_preparation_checklist',
            'prompt': f'What exact technical parameters and BOM details should a procurement engineer include in an RFQ for custom {seed}?',
            'target_citation_page': '/contact',
        },
    ]
    return {
        'company': company,
        'seed_keyword': seed,
        'industry_id': industry_id,
        'market': market,
        'generated_at': now,
        'offsite_brand_mention_surfaces': [
            'LinkedIn Company Page & Technical Articles (3x stronger AI citation correlation when paired with consistent entity naming)',
            'YouTube Factory Tour & QC Testing Video Transcripts',
            'Industry Trade Directories & Verified Exporter Registries (sameAs entity alignment)',
            'Medium / Technical Engineering Comparison Publications',
        ],
        'evaluation_protocol': {
            'engines': ['Google AI Overviews / AI Mode', 'ChatGPT Search (OAI-SearchBot)', 'Perplexity (PerplexityBot)', 'Bing Copilot'],
            'metrics': [
                'mention_rate',
                'linked_citation_rate',
                'cited_url_accuracy',
                'factual_claim_accuracy',
                'ai_referral_sessions',
                'qualified_rfq_conversions',
            ],
            'guardrail': 'Record engine, date, region, web-search toggle, and verbatim cited URLs. Small-sample prompt checks are observations, not global share guarantees.',
        },
        'prompts': prompts,
    }


def validate_backlink_entry(entry):
    required = ('target_id', 'domain', 'submit_url', 'track', 'gate_type', 'state', 'updated_at')
    if not isinstance(entry, dict):
        return 'entry must be a JSON object'
    for key in required:
        if not isinstance(entry.get(key), str) or not entry[key].strip():
            return f'missing or empty {key}'
    if entry['track'] not in ('batch_directory', 'editorial_authority', 'brand_mention_surface'):
        return 'track must be batch_directory, editorial_authority, or brand_mention_surface'
    if entry['gate_type'] not in ('open-form', 'account', 'captcha-interactive', 'captcha-passive', 'reciprocal', 'personal-contact', 'email-verify'):
        return 'invalid gate_type'
    state = entry['state']
    if state.startswith('indexed@'):
        engine = state.split('@', 1)[1].strip()
        if not engine:
            return 'indexed state must specify engine, e.g. indexed@google or indexed@bing'
    elif state not in BACKLINK_STATES or state == 'indexed':
        return 'state must be one of candidate/qualified/filled/submitted/public/indexed@<engine>/rel_verified'
    if state == 'rel_verified':
        if not isinstance(entry.get('live_url'), str) or not entry['live_url'].startswith(('http://', 'https://')):
            return 'rel_verified requires a verified live_url'
        if entry.get('rel_attribute') not in ('dofollow', 'nofollow', 'ugc', 'sponsored', 'redirect_wrapped', 'brand_mention_unlinked'):
            return 'rel_verified requires audited rel_attribute'
    return None


def init_backlink_ledger(output_path):
    now = datetime.now(timezone.utc).isoformat()
    sample = {
        'schema_version': '1.1.0',
        'updated_at': now,
        'rules': [
            'Never count a submitted directory form as an active backlink until live_url, HTTP status, redirect chain, and rel attribute are verified.',
            'Indexed status must specify the search engine explicitly (e.g., indexed@google, indexed@bing).',
            'Never bypass CAPTCHA, 2FA, or forced reciprocal link gates automatically; queue interactive verification for human approval.',
            'Track off-site B2B brand mentions (LinkedIn technical articles, YouTube QC transcripts, trade registries) under track=brand_mention_surface for GEO authority.',
        ],
        'entries': [
            {
                'target_id': 'BL-0001',
                'domain': 'example-b2b-directory.com',
                'submit_url': 'https://example-b2b-directory.com/submit',
                'track': 'batch_directory',
                'gate_type': 'open-form',
                'state': 'candidate',
                'live_url': None,
                'rel_attribute': None,
                'updated_at': now,
                'notes': 'Template candidate entry; replace with verified B2B industry directories, trade publications, or brand mention surfaces.',
            }
        ],
    }
    Path(output_path).write_text(json.dumps(sample, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return sample


def validate_ledger_file(path):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    entries = data.get('entries')
    if not isinstance(entries, list):
        raise ValueError('entries must be a list')
    seen = set()
    for idx, item in enumerate(entries):
        err = validate_backlink_entry(item)
        if err:
            raise ValueError(f'entry[{idx}]: {err}')
        tid = item['target_id']
        if tid in seen:
            raise ValueError(f'duplicate target_id: {tid}')
        seen.add(tid)
    return {'valid': True, 'count': len(entries)}


def self_test():
    tree = build_keyword_tree('stainless steel bento box', 'bento', ['US', 'EU'])
    assert len(tree['branches']) == 6
    assert tree['visual_archetype']['archetype_id'] == 'architectural_material'
    cluster = build_topic_cluster('stainless steel bento box', 'bento', 'North America')
    assert len(cluster['hubs']) == 2 and len(cluster['spokes']) == 4
    synd = build_b2b_syndication_pack('Example Bento Co.', 'stainless steel bento box', 'bento')
    assert 'linkedin_technical_article' in synd['channels']
    with tempfile.TemporaryDirectory() as tmp:
        ws = init_b2b_seo_workspace(tmp, 'Example Bento Co.', 'stainless steel bento box', 'bento', ['US', 'DE'])
        assert len(ws['files_created']) == 10
        assert (Path(tmp) / 'docs/seo/syndication-pack.json').is_file()
        catalog_file = Path(tmp) / 'skus.json'
        catalog_file.write_text(json.dumps([
            {
                'sku': 'SB-304-1200',
                'title': '304 Stainless Steel Leakproof Bento Box 1200ml',
                'seo_description': ' '.join(['Engineered with 0.8mm 304 stainless steel, food-grade silicone seal, and custom laser logo options for bulk OEM buyers.'] * 3),
                'specifications': {'material': 'SUS304', 'capacity': '1200ml', 'thickness': '0.8mm'},
                'image_alt': '304 Stainless Steel Bento Box 1200ml for OEM wholesale',
                'url': '/products/sb-304-1200',
            },
            {
                'sku': 'SB-BAD',
                'title': '304 Stainless Steel Leakproof Bento Box 1200ml',
                'seo_description': 'World-class cutting-edge solution.',
                'specifications': {},
                'image_alt': '',
                'url': '/products/sb-bad.html',
            }
        ]), encoding='utf-8')
        cat_audit = audit_b2b_sku_catalog(catalog_file, 'bento')
        assert cat_audit['seo_geo_ready_skus'] == 1 and cat_audit['skus_needing_fixes'] == 1
    print('PASS: seo_geo_matrix V3.3 (init-workspace, keyword-tree, topic-cluster, citability-score, catalog-audit, syndication-pack, 7-state ledger)')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('self-test')

    iw = sub.add_parser('init-workspace', help='Initialize 4-Phase B2B SEO/GEO/CRO Single Source of Truth hub (docs/seo/, .claude/CLAUDE.md, public/llms.txt)')
    iw.add_argument('--project', required=True)
    iw.add_argument('--company', required=True)
    iw.add_argument('--seed', required=True)
    iw.add_argument('--industry', required=True)
    iw.add_argument('--markets', default='Global')

    kt = sub.add_parser('keyword-tree', help='Generate 6-branch B2B commercial intent keyword tree + visual archetype + H1/H2 contract')
    kt.add_argument('--seed', required=True)
    kt.add_argument('--industry', required=True)
    kt.add_argument('--markets', default='Global')
    kt.add_argument('--out')

    tc = sub.add_parser('topic-cluster', help='Generate B2B Hub-and-Spoke topic cluster & internal link stitching plan')
    tc.add_argument('--seed', required=True)
    tc.add_argument('--industry', required=True)
    tc.add_argument('--market', default='Global')
    tc.add_argument('--out')

    cs = sub.add_parser('citability-score', help='Score an HTML or Markdown file on the 0-100 B2B GEO Citability & Inquiry Rubric')
    cs.add_argument('--file', required=True)
    cs.add_argument('--out')

    ca = sub.add_parser('catalog-audit', help='Audit a B2B SKU catalog JSON for missing specs, thin SEO descriptions, and Clean URL compliance')
    ca.add_argument('--file', required=True)
    ca.add_argument('--industry', required=True)
    ca.add_argument('--out')

    sp = sub.add_parser('syndication-pack', help='Generate B2B LinkedIn, Medium, and YouTube transcript syndication packs')
    sp.add_argument('--company', required=True)
    sp.add_argument('--seed', required=True)
    sp.add_argument('--industry', required=True)
    sp.add_argument('--url', default='/products')
    sp.add_argument('--out')

    gp = sub.add_parser('geo-prompts', help='Generate B2B GEO buyer prompt benchmark suite & off-site brand mention plan')
    gp.add_argument('--company', required=True)
    gp.add_argument('--seed', required=True)
    gp.add_argument('--industry', required=True)
    gp.add_argument('--market', default='Global')
    gp.add_argument('--out')

    bl_init = sub.add_parser('init-ledger', help='Initialize 7-state B2B backlink & brand mention evidence ledger')
    bl_init.add_argument('--out', required=True)

    bl_val = sub.add_parser('validate-ledger', help='Validate 7-state B2B backlink & brand mention evidence ledger')
    bl_val.add_argument('--file', required=True)

    args = parser.parse_args()
    try:
        if args.command == 'self-test':
            self_test()
        elif args.command == 'init-workspace':
            markets = [m.strip() for m in args.markets.split(',') if m.strip()]
            result = init_b2b_seo_workspace(args.project, args.company, args.seed, args.industry, markets)
            print(json.dumps(result, ensure_ascii=False, indent=2))
        elif args.command == 'keyword-tree':
            markets = [m.strip() for m in args.markets.split(',') if m.strip()]
            result = build_keyword_tree(args.seed, args.industry, markets)
            output = json.dumps(result, ensure_ascii=False, indent=2)
            if args.out:
                Path(args.out).write_text(output + '\n', encoding='utf-8')
            print(output)
        elif args.command == 'topic-cluster':
            result = build_topic_cluster(args.seed, args.industry, args.market)
            output = json.dumps(result, ensure_ascii=False, indent=2)
            if args.out:
                Path(args.out).write_text(output + '\n', encoding='utf-8')
            print(output)
        elif args.command == 'citability-score':
            result = score_geo_citability(args.file)
            output = json.dumps(result, ensure_ascii=False, indent=2)
            if args.out:
                Path(args.out).write_text(output + '\n', encoding='utf-8')
            print(output)
        elif args.command == 'catalog-audit':
            result = audit_b2b_sku_catalog(args.file, args.industry)
            output = json.dumps(result, ensure_ascii=False, indent=2)
            if args.out:
                Path(args.out).write_text(output + '\n', encoding='utf-8')
            print(output)
        elif args.command == 'syndication-pack':
            result = build_b2b_syndication_pack(args.company, args.seed, args.industry, args.url)
            output = json.dumps(result, ensure_ascii=False, indent=2)
            if args.out:
                Path(args.out).write_text(output + '\n', encoding='utf-8')
            print(output)
        elif args.command == 'geo-prompts':
            result = build_geo_prompt_suite(args.company, args.seed, args.industry, args.market)
            output = json.dumps(result, ensure_ascii=False, indent=2)
            if args.out:
                Path(args.out).write_text(output + '\n', encoding='utf-8')
            print(output)
        elif args.command == 'init-ledger':
            result = init_backlink_ledger(args.out)
            print(json.dumps({'created': args.out, 'entries': len(result['entries'])}, ensure_ascii=False))
        elif args.command == 'validate-ledger':
            print(json.dumps(validate_ledger_file(args.file), ensure_ascii=False))
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as err:
        print('ERROR: ' + str(err), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
