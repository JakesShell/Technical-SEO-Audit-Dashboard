from pathlib import Path

utils_path = Path("utils.py")
utils_text = utils_path.read_text(encoding="utf-8")

name_updates = {
    "'name': 'Maya Chen'": "'name': 'Claire Bennett'",
    "'company': 'Northline Health'": "'company': 'Northline Health'",
    "'name': 'Priya Solanki'": "'name': 'Emma Hart'",
    "'company': 'OrbitStack'": "'company': 'OrbitStack'",
}

for old, new in name_updates.items():
    utils_text = utils_text.replace(old, new)

utils_path.write_text(utils_text, encoding="utf-8")
print("Updated demo reviewer names to better match portrait assets.")
