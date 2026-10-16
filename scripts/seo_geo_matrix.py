#!/usr/bin/env python3
"""B2B SEO/GEO keyword tree, topic cluster stitcher, GEO citability scorer, evidence-backed audit rubric, and 7-state backlink ledger (V3.1).

Synthesizes B2B-appropriate capabilities from 10 open-source Agent Skills:
1. cnproduct/b2b-global-brand-site-master (21 industries, 21-module fact governance, Clean URLs, Anti-FOUC, Edge protection)
2. yan-labs/yan-skills (7-stage lifecycle, root-keyword expansion, 9-gate pre-launch check, 7-state backlink ledger)
3. coreyhaines31/marketingskills (B2B Hero value proposition, CRO objection handling, 3-tier RFQ conversion funnel)
4. AgriciDaniel/claude-seo (Technical SEO, E-E-A-T Trust-first, active Schema.org, international hreflang architecture)
5. seo.web.cafe / Gefei Official Methodology (Competitor-to-Keyword & Keyword-to-Competitor teardown, native multilingual keyword research, 6-point brand entity alignment)
6. zubair-trabzada/geo-seo-claude (134-167 word passage citability scoring, 6-dimension composite GEO score, off-site brand mention matrix, Markdown content negotiation)
7. TheCraigHewitt/seomachine (B2B Hub-and-Spoke topic cluster architecture, internal link anchor stitching, anti-AI-slop engineering prose)
8. aaron-he-zhu/aaron-marketing-skills (Survey -> Implement -> Tune -> Evaluate loop, CORE-EEAT & CITE gates)
9. Bhanunamikaze/Agentic-SEO-Skill (Evidence-backed Finding/Evidence/Impact/Fix rubric, B2B faceted navigation crawl-trap guard, orphan page & indexability matrix)
10. cnproduct/renwork-web-design-master (Fluid clamp typography, 45ch-75ch measure, 1.8x heading proximity, zero AI-slop gradients)
"""
import argparse
import html.parser
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
)

B2B_INTENT_BRANCHES = [
    {
        'branch_id': 'oem_odm_custom',
        'intent_label': 'OEM / ODM & Private Label Manufacturing',
        'buyer_stage': 'Supplier Qualification & Custom Briefing',
        'modifiers': ['oem manufacturer', 'odm supplier', 'private label factory', 'custom tooling bulk', 'bespoke specification'],
        'target_page_type': 'oem-odm',
        'primary_cta_tier': 'Tier 2: Custom BOM / Drawing & Sample RFQ',
    },
    {
        'branch_id': 'manufacturer_supplier',
        'intent_label': 'Direct Factory & Certified Industrial Supplier',
        'buyer_stage': 'Vendor Shortlisting',
        'modifiers': ['manufacturer', 'factory direct', 'industrial supplier', 'iso certified manufacturer', 'export factory'],
        'target_page_type': 'home / quality',
        'primary_cta_tier': 'Tier 3: Factory Audit & Volume Production Quote',
    },
    {
        'branch_id': 'bulk_wholesale_logistics',
        'intent_label': 'Bulk Wholesale, MOQ & Container Loading',
        'buyer_stage': 'Commercial & Logistics Evaluation',
        'modifiers': ['bulk wholesale', 'moq', '20gp 40hq container load', 'fob price list', 'export carton specification'],
        'target_page_type': 'products / calculator',
        'primary_cta_tier': 'Tier 3: Container Load & Tiered FOB Quote',
    },
    {
        'branch_id': 'technical_spec_material',
        'intent_label': 'Technical Parameters, Materials & Tolerances',
        'buyer_stage': 'Engineering & Specification Selection',
        'modifiers': ['technical specifications', 'material grade chart', 'dimension tolerance', 'datasheet pdf', 'performance test standard'],
        'target_page_type': 'products / resources',
        'primary_cta_tier': 'Tier 1: Datasheet & Standard Sample Request',
    },
    {
        'branch_id': 'application_solution',
        'intent_label': 'Industry Application & Operating Conditions',
        'buyer_stage': 'Problem-to-Solution Mapping',
        'modifiers': ['for industrial application', 'heavy duty solution', 'operating temperature range', 'engineering selection guide', 'application case'],
        'target_page_type': 'solutions',
        'primary_cta_tier': 'Tier 2: Application Engineering Consultation',
    },
    {
        'branch_id': 'comparison_alternative',
        'intent_label': 'Material / Process Trade-off & Comparison',
        'buyer_stage': 'Trade-off Evaluation (High GEO Citation Value)',
        'modifiers': ['vs', 'material comparison table', 'process alternative', 'cost vs performance', 'how to specify for bulk sourcing'],
        'target_page_type': 'resources',
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
            'primary_cta_tier': branch['primary_cta_tier'],
            'candidate_queries': queries,
            'required_industry_fields': profile['product_fields'][:4],
            'required_evidence': profile['evidence'][:3],
            'verification_status': 'UNVERIFIED_VOLUME_AND_SERP',
            'gate_rule': 'Verify real SERP buyer intent and search volume before locking page TDK. Never fabricate volume or KD numbers.',
        })
    return {
        'seed_keyword': seed,
        'industry_id': industry_id,
        'industry_name': profile['name'],
        'target_markets': markets,
        'generated_at': now,
        'gefei_b2b_competitor_teardown': {
            'domain_to_keyword': 'Extract top organic landing pages and inquiry keywords from 3-5 overseas B2B niche manufacturers/importers.',
            'keyword_to_domain': 'Inspect live SERP top 10 for each branch; confirm at least 60% are B2B supplier/spec pages rather than B2C retail listings.',
            'multilingual_rule': 'Never machine-translate keywords across languages; re-research native industrial nomenclature (e.g., DIN/EN for DE, ASTM for US) per target market.',
        },
        'excluded_b2c_modifiers': ['cheap single piece', 'diy home craft', 'retail coupon', 'free shipping 1 pc', 'used second hand', 'paywall subscription'],
        'branches': branches,
        'handoff_contract': {
            'stage_1_to_stage_2': 'Map each approved branch to a dedicated Clean URL page with zero keyword cannibalization.',
            'stage_2_to_stage_3': 'Bind each page to its matching primary_cta_tier and pre-filled RFQ context.',
            'stage_4_gate': 'Every target page must include a verifiable spec table and a self-contained 134-167 word engineering answer block.',
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
                f'Semantic HTML comparison table across {f0}, {f1}, and {f2}',
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
            'Open every guide directly with engineering constraints, BOM cost drivers, or procurement failure modes.',
            'Ban generic filler openings ("In today\'s fast-paced world...", "Look no further...").',
            'Include at least one semantic HTML <table> with explicit units/conditions and one 134-167 word self-contained GEO answer block per article.',
            'Every spoke article must link to at least 1 Hub page (/products or /oem-odm) and 1 conversion tool (/calculator or /contact) using descriptive technical anchor text.',
        ],
        'hubs': hubs,
        'spokes': spokes,
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
    """Scores a B2B HTML or Markdown file on the 0-100 B2B GEO Citability & Inquiry Readiness Rubric (adapted from geo-seo-claude + claude-seo)."""
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

    # 1. Passage Citability (25 pts): 134-167 word self-contained answer blocks
    if optimal_passages:
        passage_score = 25
    elif near_optimal_passages:
        passage_score = 18
    elif any(wc >= 40 for wc in word_counts):
        passage_score = 10
    else:
        passage_score = 0

    # 2. Semantic Spec Table & Quantitative Fact Density (25 pts)
    unit_matches = re.findall(r'\b\d+(?:\.\d+)?\s*(?:mm|cm|m|kg|g|ml|l|pcs|cbm|20gp|40hq|mpa|kw|v|hz|%|°c|iso|astm|din|ce|fsc)\b', raw.lower())
    spec_score = 0
    if table_count >= 1 and th_count >= 2:
        spec_score += 15
    if len(unit_matches) >= 5:
        spec_score += 10
    elif len(unit_matches) >= 2:
        spec_score += 5

    # 3. Anti-AI-Slop & E-E-A-T Clarity (20 pts)
    slop_hits = [phrase for phrase in AI_SLOP_PHRASES if phrase in raw.lower()]
    eeat_score = max(0, 20 - len(slop_hits) * 5)

    # 4. Technical Structure, Clean URLs & Schema (15 pts)
    tech_score = 0
    if h1_count == 1:
        tech_score += 5
    html_link_violations = [lk for lk in links if lk.endswith('.html') or '.html#' in lk]
    if not html_link_violations:
        tech_score += 5
    if has_json_ld or not is_html:
        tech_score += 5

    # 5. B2B Inquiry Funnel & Internal Link Stitching (15 pts)
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
            'fix': 'Insert a semantic HTML <table> with <thead> and <th scope="col"> listing verified model parameters, units, and test conditions.',
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
    assert 'gefei_b2b_competitor_teardown' in tree
    cluster = build_topic_cluster('stainless steel bento box', 'bento', 'North America')
    assert len(cluster['hubs']) == 2 and len(cluster['spokes']) == 4
    suite = build_geo_prompt_suite('Example Bento Co.', 'stainless steel bento box', 'bento', 'North America')
    assert len(suite['prompts']) == 6
    assert len(suite['offsite_brand_mention_surfaces']) == 4
    with tempfile.TemporaryDirectory() as tmp:
        ledger_path = Path(tmp) / 'backlink-ledger.json'
        init_backlink_ledger(ledger_path)
        res = validate_ledger_file(ledger_path)
        assert res == {'valid': True, 'count': 1}
        sample_html = Path(tmp) / 'sample.html'
        sample_html.write_text(
            '<!doctype html><html><head><script type="application/ld+json">{}</script></head><body>'
            '<h1>Industrial Stainless Steel Bento Box for Bulk OEM</h1>'
            '<p>' + (' '.join(['304 stainless steel 0.8mm thickness food-grade contact tested ISO 9001 batch traceability for bulk OEM buyers.'] * 9)) + '</p>'
            '<table><thead><tr><th scope="col">Model</th><th scope="col">Thickness (mm)</th><th scope="col">Capacity (ml)</th></tr></thead>'
            '<tbody><tr><td>SB-100</td><td>0.8mm</td><td>1200ml</td></tr></tbody></table>'
            '<a href="/oem-odm">Request Custom BOM &amp; Sample RFQ</a>'
            '</body></html>',
            encoding='utf-8'
        )
        score = score_geo_citability(sample_html)
        assert score['composite_geo_score'] >= 90, score
    print('PASS: seo_geo_matrix V3.1 keyword-tree, topic-cluster, citability-score, geo-prompts, and 7-state backlink ledger validation')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('self-test')

    kt = sub.add_parser('keyword-tree', help='Generate 6-branch B2B commercial intent keyword tree + Gefei competitor teardown protocol')
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
