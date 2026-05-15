from pathlib import Path

output_dir = Path("assets/testimonials")
output_dir.mkdir(parents=True, exist_ok=True)

profiles = [
    {
        "filename": "maya-chen.svg",
        "bg1": "#1b4965",
        "bg2": "#3fa7d6",
        "skin": "#f0c7a4",
        "hair": "#1d1d1f",
        "shirt": "#e8f1f2",
        "accent": "#89d2dc",
    },
    {
        "filename": "leo-andrade.svg",
        "bg1": "#243b53",
        "bg2": "#2f80ed",
        "skin": "#d9a780",
        "hair": "#2b1f19",
        "shirt": "#f6d365",
        "accent": "#80ffea",
    },
    {
        "filename": "priya-solanki.svg",
        "bg1": "#3d405b",
        "bg2": "#5f0f40",
        "skin": "#d9a27f",
        "hair": "#101014",
        "shirt": "#d8f3dc",
        "accent": "#f4acb7",
    },
]

for profile in profiles:
    svg = f'''<svg width="320" height="320" viewBox="0 0 320 320" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="320" height="320" rx="42" fill="url(#bg)"/>
<circle cx="258" cy="60" r="44" fill="{profile["accent"]}" fill-opacity="0.18"/>
<circle cx="72" cy="74" r="28" fill="white" fill-opacity="0.08"/>
<path d="M68 288C77 233 114 210 160 210C206 210 243 233 252 288H68Z" fill="{profile["shirt"]}"/>
<circle cx="160" cy="140" r="56" fill="{profile["skin"]}"/>
<path d="M106 132C106 94 131 72 160 72C191 72 214 95 214 132V143H106V132Z" fill="{profile["hair"]}"/>
<path d="M115 124C126 103 143 92 160 92C178 92 196 103 205 124V150H115V124Z" fill="{profile["hair"]}"/>
<ellipse cx="141" cy="140" rx="5" ry="6" fill="#1E2630"/>
<ellipse cx="180" cy="140" rx="5" ry="6" fill="#1E2630"/>
<path d="M146 171C154 177 165 178 174 171" stroke="#8E5A47" stroke-width="4" stroke-linecap="round"/>
<path d="M159 151V164" stroke="#C68B6D" stroke-width="3" stroke-linecap="round"/>
<path d="M109 114C116 88 135 66 160 66C186 66 207 88 212 114" stroke="white" stroke-opacity="0.08" stroke-width="10" stroke-linecap="round"/>
<defs>
<linearGradient id="bg" x1="22" y1="14" x2="282" y2="304" gradientUnits="userSpaceOnUse">
<stop stop-color="{profile["bg1"]}"/>
<stop offset="1" stop-color="{profile["bg2"]}"/>
</linearGradient>
</defs>
</svg>'''
    (output_dir / profile["filename"]).write_text(svg, encoding="utf-8")

print("Generated testimonial portrait assets.")
