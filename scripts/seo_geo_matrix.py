#!/usr/bin/env python3
"""B2B SEO/GEO keyword tree builder, GEO prompt benchmark generator, and 7-state backlink ledger.

Synthesizes workflow patterns from:
- cnproduct/b2b-global-brand-site-master (fact-gated B2B independent site engineering)
- yan-labs/yan-skills (root-keyword tree expansion, 7-stage lifecycle, 7-state backlink ledger)
- AgriciDaniel/claude-seo (E-E-A-T, active Schema.org, GEO passage citability & agent readiness)
- coreyhaines31/marketingskills (B2B CRO & 3-tier RFQ conversion funnel mapping)
- aaron-he-zhu/aaron-marketing-skills (CORE-EEAT & CITE audit gates)
- flaqai/backlink_skills (dual-track backlink prospecting & verification-first queue)
"""
import argparse
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

B2B_INTENT_BRANCHES = [
    {
        'branch_id': 'oem_odm_custom',
        'intent_label': 'OEM / ODM & Private Label',
        'buyer_stage': 'Supplier Qualification & Custom Briefing',
        'modifiers': ['oem manufacturer', 'odm supplier', 'private label factory', 'custom logo bulk', 'bespoke specification'],
        'target_page_type': 'oem-odm',
        'primary_cta_tier': 'Tier 2: Custom BOM / Drawing & Sample RFQ',
    },
    {
        'branch_id': 'manufacturer_supplier',
        'intent_label': 'Direct Manufacturer & Factory Verification',
        'buyer_stage': 'Vendor Shortlisting',
        'modifiers': ['manufacturer', 'factory direct', 'industrial supplier', 'iso certified manufacturer', 'export factory'],
        'target_page_type': 'home / manufacturing-quality',
        'primary_cta_tier': 'Tier 3: Factory Audit & Volume Production Quote',
    },
    {
        'branch_id': 'bulk_wholesale_logistics',
        'intent_label': 'Bulk Wholesale, MOQ & Container Loading',
        'buyer_stage': 'Commercial & Logistics Evaluation',
        'modifiers': ['bulk wholesale', 'moq', '20gp 40hq container load', 'fob price list', 'bulk packaging specification'],
        'target_page_type': 'category / calculator',
        'primary_cta_tier': 'Tier 3: Container Load & Tiered FOB Quote',
    },
    {
        'branch_id': 'technical_spec_material',
        'intent_label': 'Technical Parameters, Materials & Tolerances',
        'buyer_stage': 'Engineering & Specification Selection',
        'modifiers': ['technical specifications', 'material grade chart', 'dimension tolerance', 'datasheet pdf', 'performance test standard'],
        'target_page_type': 'product / resources',
        'primary_cta_tier': 'Tier 1: Datasheet & Standard Sample Request',
    },
    {
        'branch_id': 'application_solution',
        'intent_label': 'Industry Application & Operating Conditions',
        'buyer_stage': 'Problem-to-Solution Mapping',
        'modifiers': ['for industrial application', 'heavy duty solution', 'operating temperature range', 'selection guide', 'application case'],
        'target_page_type': 'solutions',
        'primary_cta_tier': 'Tier 2: Application Engineering Consultation',
    },
    {
        'branch_id': 'comparison_alternative',
        'intent_label': 'Material / Process Comparison & Alternatives',
        'buyer_stage': 'Trade-off Evaluation (High GEO Citation Value)',
        'modifiers': ['vs', 'comparison table', 'material alternative', 'cost vs performance', 'how to choose for bulk sourcing'],
        'target_page_type': 'resources / comparison-guide',
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
        'excluded_b2c_modifiers': ['cheap single piece', 'diy home craft', 'retail coupon', 'free shipping 1 pc', 'used second hand'],
        'branches': branches,
        'handoff_contract': {
            'stage_1_to_stage_2': 'Map each approved branch to a dedicated Clean URL page with zero keyword cannibalization.',
            'stage_2_to_stage_3': 'Bind each page to its matching primary_cta_tier and pre-filled RFQ context.',
            'stage_4_gate': 'Every target page must include a verifiable spec table and a self-contained 130-170 word engineering answer block.',
        },
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
    if entry['track'] not in ('batch_directory', 'editorial_authority'):
        return 'track must be batch_directory or editorial_authority'
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
        if entry.get('rel_attribute') not in ('dofollow', 'nofollow', 'ugc', 'sponsored', 'redirect_wrapped'):
            return 'rel_verified requires audited rel_attribute'
    return None


def init_backlink_ledger(output_path):
    now = datetime.now(timezone.utc).isoformat()
    sample = {
        'schema_version': '1.0.0',
        'updated_at': now,
        'rules': [
            'Never count a submitted directory form as an active backlink until live_url, HTTP status, redirect chain, and rel attribute are verified.',
            'Indexed status must specify the search engine explicitly (e.g., indexed@google, indexed@bing).',
            'Never bypass CAPTCHA, 2FA, or forced reciprocal link gates automatically; queue interactive verification for human approval.',
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
                'notes': 'Template candidate entry; replace with verified B2B industry directories or trade publications.',
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
    assert tree['industry_id'] == 'bento'
    suite = build_geo_prompt_suite('Example Bento Co.', 'stainless steel bento box', 'bento', 'North America')
    assert len(suite['prompts']) == 6
    with tempfile.TemporaryDirectory() as tmp:
        ledger_path = Path(tmp) / 'backlink-ledger.json'
        init_backlink_ledger(ledger_path)
        res = validate_ledger_file(ledger_path)
        assert res == {'valid': True, 'count': 1}
        bad = json.loads(ledger_path.read_text(encoding='utf-8'))
        bad['entries'][0]['state'] = 'indexed'
        ledger_path.write_text(json.dumps(bad), encoding='utf-8')
        try:
            validate_ledger_file(ledger_path)
        except ValueError:
            pass
        else:
            raise AssertionError('bare indexed without @engine must fail')
        bad['entries'][0]['state'] = 'indexed@google'
        ledger_path.write_text(json.dumps(bad), encoding='utf-8')
        assert validate_ledger_file(ledger_path)['valid'] is True
    print('PASS: seo_geo_matrix keyword-tree, geo-prompts, and 7-state backlink ledger validation')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('self-test')

    kt = sub.add_parser('keyword-tree', help='Generate 6-branch B2B commercial intent keyword tree')
    kt.add_argument('--seed', required=True)
    kt.add_argument('--industry', required=True)
    kt.add_argument('--markets', default='Global')
    kt.add_argument('--out')

    gp = sub.add_parser('geo-prompts', help='Generate B2B GEO buyer prompt benchmark suite')
    gp.add_argument('--company', required=True)
    gp.add_argument('--seed', required=True)
    gp.add_argument('--industry', required=True)
    gp.add_argument('--market', default='Global')
    gp.add_argument('--out')

    bl_init = sub.add_parser('init-ledger', help='Initialize 7-state B2B backlink evidence ledger')
    bl_init.add_argument('--out', required=True)

    bl_val = sub.add_parser('validate-ledger', help='Validate 7-state B2B backlink evidence ledger')
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
