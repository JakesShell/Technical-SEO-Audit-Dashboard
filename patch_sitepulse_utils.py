from pathlib import Path

utils_path = Path("utils.py")
utils_text = utils_path.read_text(encoding="utf-8")

old_domain_block = """    parsed = urlparse(normalized_url)
    domain = parsed.netloc or normalized_url.replace('https://', '').replace('http://', '')
"""

new_domain_block = """    parsed = urlparse(normalized_url)
    domain = parsed.netloc or normalized_url.replace('https://', '').replace('http://', '')

    is_local_demo = (
        domain.startswith('127.0.0.1')
        or domain.startswith('localhost')
        or domain.startswith('0.0.0.0')
    )

    display_domain = 'Local Demo Site' if is_local_demo else domain
    display_url = 'Demo environment detected' if is_local_demo else normalized_url
"""

utils_text = utils_text.replace(old_domain_block, new_domain_block)

old_return_block = """        'normalized_url': normalized_url,
        'domain': domain,
"""

new_return_block = """        'normalized_url': normalized_url,
        'display_url': display_url,
        'domain': domain,
        'display_domain': display_domain,
        'is_local_demo': is_local_demo,
"""

utils_text = utils_text.replace(old_return_block, new_return_block)

utils_path.write_text(utils_text, encoding="utf-8")

print("SitePulse utils patched for local demo display.")
