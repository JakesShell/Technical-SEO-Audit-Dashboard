from pathlib import Path

utils_path = Path("utils.py")
utils_text = utils_path.read_text(encoding="utf-8")

replacements = {
    "'avatar': 'testimonials/maya-chen.svg'": "'avatar': 'testimonials/maya-chen-real.png'",
    "'avatar': 'testimonials/leo-andrade.svg'": "'avatar': 'testimonials/leo-andrade-real.png'",
    "'avatar': 'testimonials/priya-solanki.svg'": "'avatar': 'testimonials/priya-solanki-real.png'",
}

for old, new in replacements.items():
    utils_text = utils_text.replace(old, new)

if "'short_display_url':" not in utils_text:
    utils_text = utils_text.replace(
        "'display_url': display_url,",
        "'display_url': display_url,\n        'short_display_url': display_url if len(display_url) <= 72 else display_url[:69] + '...',"
    )

utils_path.write_text(utils_text, encoding="utf-8")
print("Updated testimonial portraits and short display URL support.")
