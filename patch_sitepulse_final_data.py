from pathlib import Path

utils_path = Path("utils.py")
utils_text = utils_path.read_text(encoding="utf-8")

quote_replacements = {
    "SitePulse gave our team one place to spot crawl blockers, page-speed drag, and metadata gaps before launch. It turned a messy audit into a decision-ready action plan.": "SitePulse turned our launch audit into a clear repair plan before traffic was affected.",
    "The visual issue scoring made client conversations easier instantly. Instead of vague SEO talk, we could show exactly what was slowing trust, indexing, and content performance.": "The visual scoring made every client conversation sharper, faster, and easier to defend.",
    "I loved the AI visibility section. It helped our content and engineering teams align on structured data, performance, and launch readiness without needing separate reports.": "The AI visibility view helped content, product, and engineering align in one meeting."
}

for old, new in quote_replacements.items():
    utils_text = utils_text.replace(old, new)

avatar_replacements = {
    "'avatar': 'testimonials/maya-chen.svg'": "'avatar': 'testimonials/maya-chen-real.png'",
    "'avatar': 'testimonials/leo-andrade.svg'": "'avatar': 'testimonials/leo-andrade-real.png'",
    "'avatar': 'testimonials/priya-solanki.svg'": "'avatar': 'testimonials/priya-solanki-real.png'",
}

for old, new in avatar_replacements.items():
    utils_text = utils_text.replace(old, new)

if "'short_display_url':" not in utils_text:
    utils_text = utils_text.replace(
        "'display_url': display_url,",
        "'display_url': display_url,\n        'short_display_url': display_url if len(display_url) <= 72 else display_url[:69] + '...',"
    )

utils_path.write_text(utils_text, encoding="utf-8")
print("Updated SitePulse data copy and portrait references.")
