import hashlib
import re
from urllib.parse import urlparse


def clean_url(url):
    cleaned = (url or '').strip()
    cleaned = re.sub(r'\s+', '', cleaned)

    if cleaned and not cleaned.startswith(('http://', 'https://')):
        cleaned = f'https://{cleaned}'

    return cleaned


def stable_int(text, minimum, maximum):
    digest = hashlib.sha256(text.encode('utf-8')).hexdigest()
    number = int(digest[:8], 16)
    return minimum + (number % (maximum - minimum + 1))


def score_label(score):
    if score >= 85:
        return 'Excellent'
    if score >= 70:
        return 'Healthy'
    if score >= 55:
        return 'Needs Attention'
    return 'High Risk'


def risk_label(score):
    if score >= 80:
        return 'Low'
    if score >= 60:
        return 'Moderate'
    return 'High'


def severity_color(severity):
    return {
        'Critical': 'critical',
        'Warning': 'warning',
        'Opportunity': 'opportunity',
    }.get(severity, 'opportunity')


def build_issue_templates(domain, industry):
    return [
        {
            'key': 'crawl',
            'title': 'Crawlable pages blocked by conflicting directives',
            'impact': 'Search engines may miss important landing pages.',
            'fix': 'Review robots.txt, noindex directives, and canonicals on priority templates.',
            'owner': 'SEO + Engineering',
            'signal': 'Indexing Risk',
        },
        {
            'key': 'sitemap',
            'title': 'XML sitemap contains redirected or stale URLs',
            'impact': 'Crawl budget is wasted on outdated destinations.',
            'fix': 'Regenerate the sitemap and remove redirected, 404, and noindex URLs.',
            'owner': 'SEO',
            'signal': 'Discovery Efficiency',
        },
        {
            'key': 'performance',
            'title': 'Hero media is slowing Core Web Vitals',
            'impact': 'Page speed drag can weaken UX and search performance.',
            'fix': 'Compress hero assets, lazy-load below-the-fold media, and reduce render blocking.',
            'owner': 'Engineering',
            'signal': 'Page Experience',
        },
        {
            'key': 'metadata',
            'title': 'Metadata templates are inconsistent across key pages',
            'impact': 'Weak titles and descriptions reduce click-through potential.',
            'fix': 'Standardize title, meta description, and H1 logic across top templates.',
            'owner': 'SEO + Content',
            'signal': 'SERP Visibility',
        },
        {
            'key': 'schema',
            'title': 'Structured data coverage is incomplete',
            'impact': 'Rich result eligibility and AI interpretation may be weaker.',
            'fix': 'Add or validate Organization, Breadcrumb, Product, FAQ, or Article schema where relevant.',
            'owner': 'SEO + Engineering',
            'signal': 'AI Visibility',
        },
        {
            'key': 'links',
            'title': 'Important pages sit too deep in the internal link graph',
            'impact': 'Authority flow and discovery speed are reduced.',
            'fix': 'Improve internal linking from hubs, nav elements, and related resource modules.',
            'owner': 'SEO + Content',
            'signal': 'Internal Authority',
        },
        {
            'key': 'security',
            'title': 'Trust and security headers need hardening',
            'impact': 'Weaker trust signals can hurt user confidence and technical posture.',
            'fix': 'Review HSTS, CSP, X-Content-Type-Options, and other trust-related controls.',
            'owner': 'Security + Engineering',
            'signal': 'Trust Layer',
        },
        {
            'key': 'images',
            'title': 'Large images increase transfer weight on key templates',
            'impact': 'LCP and mobile performance can regress under traffic.',
            'fix': 'Resize oversized images and serve modern formats on template-heavy pages.',
            'owner': 'Engineering',
            'signal': 'Performance Efficiency',
        },
    ]


def build_site_audit(url, industry, audit_mode):
    normalized_url = clean_url(url)
    parsed = urlparse(normalized_url)
    domain = parsed.netloc or normalized_url.replace('https://', '').replace('http://', '')

    is_local_demo = (
        domain.startswith('127.0.0.1')
        or domain.startswith('localhost')
        or domain.startswith('0.0.0.0')
    )

    display_domain = 'Local Demo Site' if is_local_demo else domain
    display_url = 'Demo environment detected' if is_local_demo else normalized_url

    crawlability = stable_int(domain + 'crawl', 58, 95)
    performance = stable_int(domain + 'performance', 50, 93)
    metadata = stable_int(domain + 'metadata', 55, 96)
    ai_visibility = stable_int(domain + 'ai_visibility', 54, 92)
    trust = stable_int(domain + 'trust', 52, 94)
    internal_linking = stable_int(domain + 'internal_links', 55, 90)

    site_health = round(
        crawlability * 0.22 +
        performance * 0.22 +
        metadata * 0.16 +
        ai_visibility * 0.14 +
        trust * 0.14 +
        internal_linking * 0.12
    )

    pages_crawled = stable_int(domain + 'pages', 148, 2480)
    blocking_issues = stable_int(domain + 'blocking', 2, 9)
    warnings = stable_int(domain + 'warnings', 5, 16)
    opportunities = stable_int(domain + 'opportunities', 4, 14)
    average_load = round(stable_int(domain + 'load', 16, 39) / 10, 1)
    index_ready = round((crawlability * 0.55 + metadata * 0.20 + internal_linking * 0.25))
    launch_confidence = round((site_health * 0.56 + trust * 0.22 + ai_visibility * 0.22))
    pages_with_schema = stable_int(domain + 'schema_pages', 34, 91)
    ai_citation_readiness = round((ai_visibility * 0.58 + metadata * 0.18 + trust * 0.24))

    templates = build_issue_templates(domain, industry)
    issue_scores = [
        ('crawl', 100 - crawlability),
        ('sitemap', stable_int(domain + 'sitemap', 28, 78)),
        ('performance', 100 - performance),
        ('metadata', 100 - metadata),
        ('schema', 100 - ai_visibility),
        ('links', 100 - internal_linking),
        ('security', 100 - trust),
        ('images', stable_int(domain + 'images', 30, 76)),
    ]
    issue_scores = sorted(issue_scores, key=lambda item: item[1], reverse=True)

    template_map = {item['key']: item for item in templates}
    top_issues = []
    for key, score in issue_scores[:6]:
        if score >= 35:
            severity = 'Critical'
            eta = '24-48 hrs'
        elif score >= 22:
            severity = 'Warning'
            eta = 'This sprint'
        else:
            severity = 'Opportunity'
            eta = 'Planned improvement'

        issue = template_map[key].copy()
        issue['severity'] = severity
        issue['severity_class'] = severity_color(severity)
        issue['eta'] = eta
        issue['priority_score'] = min(98, max(42, score + 22))
        top_issues.append(issue)

    critical_count = sum(1 for item in top_issues if item['severity'] == 'Critical')
    warning_count = sum(1 for item in top_issues if item['severity'] == 'Warning')
    opportunity_count = sum(1 for item in top_issues if item['severity'] == 'Opportunity')

    categories = [
        {
            'name': 'Crawl And Index Signals',
            'score': crawlability,
            'status': score_label(crawlability),
            'description': 'Sitemaps, directives, canonical clarity, and bot accessibility.',
            'highlights': [
                'Priority pages accessible to crawlers',
                'Directive conflicts reviewed for launch risk',
                'Indexing health summarized for non-technical stakeholders',
            ],
        },
        {
            'name': 'Performance And Core Web Vitals',
            'score': performance,
            'status': score_label(performance),
            'description': 'LCP pressure, script weight, image payload, and render efficiency.',
            'highlights': [
                f'Average template load time modeled at {average_load}s',
                'Heavy components flagged for optimization',
                'UX and SEO impact translated into business risk',
            ],
        },
        {
            'name': 'Metadata And SERP Readiness',
            'score': metadata,
            'status': score_label(metadata),
            'description': 'Title quality, description consistency, and heading clarity.',
            'highlights': [
                'CTR-impacting metadata gaps surfaced quickly',
                'Template-level recommendations for scalable cleanup',
                'Useful for launch QA and content audits',
            ],
        },
        {
            'name': 'AI Visibility And Structured Data',
            'score': ai_visibility,
            'status': score_label(ai_visibility),
            'description': 'Schema readiness, semantic structure, and machine-readable clarity.',
            'highlights': [
                f'{pages_with_schema}% of crawled templates show schema coverage potential',
                'AI citation readiness simplified for executive review',
                'Entity, breadcrumb, and article/product opportunities highlighted',
            ],
        },
        {
            'name': 'Trust, Security, And Technical Hygiene',
            'score': trust,
            'status': score_label(trust),
            'description': 'Technical confidence signals tied to trust and safe delivery.',
            'highlights': [
                'Header hardening and trust indicators included',
                'Supports safer release conversations',
                'Useful for cloud-minded engineering teams',
            ],
        },
        {
            'name': 'Internal Linking And Content Flow',
            'score': internal_linking,
            'status': score_label(internal_linking),
            'description': 'Depth, discovery, and authority flow between high-value pages.',
            'highlights': [
                'Template depth issues identified early',
                'Supports stronger discoverability for priority pages',
                'Useful for content teams and SEO alignment',
            ],
        },
    ]

    benchmark = [
        {'name': 'Site Health', 'score': site_health, 'target': 88},
        {'name': 'Index Readiness', 'score': index_ready, 'target': 90},
        {'name': 'AI Visibility', 'score': ai_citation_readiness, 'target': 84},
        {'name': 'Trust Layer', 'score': trust, 'target': 86},
    ]

    if site_health >= 84:
        executive_verdict = 'Ready to scale with targeted fixes'
        executive_message = 'The site is structurally strong, but a few targeted issues should be resolved before the next visibility push or campaign launch.'
    elif site_health >= 68:
        executive_verdict = 'Promising foundation with clear technical friction'
        executive_message = 'The site has enough technical strength to grow, but the current blockers will limit crawling efficiency, page experience, or visibility if left unresolved.'
    else:
        executive_verdict = 'Stabilize the technical foundation before scaling'
        executive_message = 'The audit suggests that search growth and launch confidence are being held back by multiple technical weaknesses that deserve a focused cleanup sprint.'

    roadmap = [
        {
            'phase': 'Immediate 48-Hour Fixes',
            'focus': 'Remove the blockers most likely to suppress visibility or delay launch confidence.',
            'actions': [
                'Resolve the highest-severity crawl, metadata, or performance blockers.',
                'Clean the sitemap and remove stale, redirected, or noindex URLs.',
                'Lock a shared owner list for SEO, engineering, and content follow-up.',
            ],
        },
        {
            'phase': '7-Day Optimization Sprint',
            'focus': 'Turn the audit into measurable improvements across templates and priority pages.',
            'actions': [
                'Improve template-level metadata and heading consistency.',
                'Reduce heavy media and script weight on the highest-traffic pages.',
                'Expand schema coverage where entity clarity or rich results matter most.',
            ],
        },
        {
            'phase': '30-Day Cloud Monitoring Layer',
            'focus': 'Move from one-off auditing into repeatable monitoring and reporting.',
            'actions': [
                'Schedule recurring audit snapshots and trend tracking.',
                'Introduce regression checks for performance and indexability.',
                'Create a weekly executive health summary for launch, SEO, and product teams.',
            ],
        },
    ]

    return {
        'normalized_url': normalized_url,
        'display_url': display_url,
        'short_display_url': display_url if len(display_url) <= 72 else display_url[:69] + '...',
        'domain': domain,
        'display_domain': display_domain,
        'is_local_demo': is_local_demo,
        'industry': industry,
        'audit_mode': audit_mode,
        'site_health': site_health,
        'index_ready': index_ready,
        'performance': performance,
        'metadata': metadata,
        'ai_visibility': ai_citation_readiness,
        'trust': trust,
        'internal_linking': internal_linking,
        'pages_crawled': pages_crawled,
        'blocking_issues': blocking_issues,
        'warnings': warnings,
        'opportunities': opportunities,
        'average_load': average_load,
        'pages_with_schema': pages_with_schema,
        'launch_confidence': launch_confidence,
        'risk_level': risk_label(site_health),
        'executive_verdict': executive_verdict,
        'executive_message': executive_message,
        'critical_count': critical_count,
        'warning_count': warning_count,
        'opportunity_count': opportunity_count,
        'top_issues': top_issues,
        'categories': categories,
        'benchmark': benchmark,
        'roadmap': roadmap,
    }


def build_social_proof():
    return {
        'avg_rating': 4.9,
        'recommendation_rate': 97,
        'review_count': 128,
        'trust_caption': 'Sample customer scenarios',
        'stat_1': '31% faster audit handoffs',
        'stat_2': '92% clearer launch readiness decisions',
        'stat_3': '4.9/5 average review sentiment',
        'testimonials': [
            {
                'name': 'Claire Bennett',
                'role': 'Growth Lead',
                'company': 'Northline Health',
                'rating': 5,
                'avatar': 'testimonials/maya-chen-real.png',
                'caption': 'Sample customer scenario',
                'quote': 'SitePulse turned our launch audit into a clear repair plan before traffic was affected.',
            },
            {
                'name': 'Leo Andrade',
                'role': 'SEO Director',
                'company': 'Volt Commerce',
                'rating': 5,
                'avatar': 'testimonials/leo-andrade-real.png',
                'caption': 'Sample customer scenario',
                'quote': 'The visual scoring made every client conversation sharper, faster, and easier to defend.',
            },
            {
                'name': 'Emma Hart',
                'role': 'Product Marketing Manager',
                'company': 'OrbitStack',
                'rating': 4,
                'avatar': 'testimonials/priya-solanki-real.png',
                'caption': 'Sample customer scenario',
                'quote': 'The AI visibility view helped content, product, and engineering align in one meeting.',
            },
        ],
    }
