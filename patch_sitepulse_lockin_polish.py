from pathlib import Path

css_path = Path("styles.css")
css_text = css_path.read_text(encoding="utf-8")

patch = r'''

/* =========================================================
   SITEPULSE FINAL LOCK-IN POLISH
   Header breathing room, diamond sparkle, and cleaner reviews.
   ========================================================= */

.app-header {
    padding-right: 6px;
}

.mode-pill {
    padding: 10px 18px;
    box-shadow:
        0 0 0 1px rgba(124,231,255,.08),
        0 0 18px rgba(35,186,255,.08);
}

.scanner-title-row h2 {
    letter-spacing: -0.07em;
}

.main-diamond {
    filter: saturate(1.14) contrast(1.08) brightness(1.08);
}

.main-diamond::after {
    opacity: 1;
    background:
        linear-gradient(115deg, transparent 0 24%, rgba(255,255,255,.5) 31%, transparent 43%),
        linear-gradient(245deg, transparent 0 40%, rgba(255,255,255,.25) 48%, transparent 58%);
}

.hero-diamond,
.main-diamond,
.gate-diamond {
    will-change: transform;
}

.review-card {
    align-items: center;
}

.review-card img {
    object-position: center center;
    border: 1px solid rgba(124,231,255,.18);
}

.review-card h4 {
    color: var(--ink);
}

.review-card blockquote {
    color: #a9bdcf;
}

.satisfaction-section {
    box-shadow:
        0 0 0 1px rgba(76,169,255,.18),
        0 0 42px rgba(35,186,255,.1),
        var(--shadow);
}

.repair-bay {
    margin-top: 2px;
}
'''

if "SITEPULSE FINAL LOCK-IN POLISH" not in css_text:
    css_text += patch

css_path.write_text(encoding="utf-8", data=css_text)
print("Final lock-in polish applied.")
