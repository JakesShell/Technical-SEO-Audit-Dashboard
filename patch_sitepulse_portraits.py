from pathlib import Path

css_path = Path("styles.css")
css_text = css_path.read_text(encoding="utf-8")

portrait_patch = r'''

/* =========================================================
   SITEPULSE PORTRAIT FIX
   Fixes bad headshot crops and improves testimonial layout
   ========================================================= */

.satisfaction-card {
    min-height: 280px;
}

.review-row {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 16px;
    align-items: stretch;
}

.review-tile {
    display: grid;
    grid-template-columns: 112px 1fr;
    gap: 16px;
    padding: 16px;
    border-radius: 18px;
    background:
        linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.025));
    border: 1px solid var(--line);
    align-items: start;
    min-height: 250px;
}

.review-tile img {
    width: 112px;
    height: 148px;
    object-fit: cover;
    object-position: center top;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 12px 28px rgba(0,0,0,0.28);
    background: rgba(255,255,255,0.04);
}

/* If some portraits still crop too tightly, bias them further upward */
.review-tile:nth-child(1) img,
.review-tile:nth-child(2) img,
.review-tile:nth-child(3) img {
    object-position: center 18%;
}

.review-tile h4 {
    margin: 0 0 4px;
    font-size: 0.98rem;
    line-height: 1.1;
}

.review-tile p {
    margin: 0;
    font-size: 0.8rem;
    line-height: 1.35;
    color: var(--muted);
}

.review-tile small {
    display: block;
    margin-top: 2px;
    font-size: 0.76rem;
    color: var(--muted);
}

.stars {
    display: inline-block;
    margin-top: 8px;
    margin-bottom: 8px;
    color: #ffc94e;
    font-size: 1rem;
    letter-spacing: 0.08em;
}

.review-tile blockquote {
    margin: 0;
    font-size: 0.8rem;
    line-height: 1.5;
    color: var(--muted);
    max-width: 100%;
}

/* Make cards feel cleaner in light mode too */
body.light-mode .review-tile {
    background:
        linear-gradient(180deg, rgba(255,255,255,0.92), rgba(245,252,255,0.9));
}

/* Tablet */
@media (max-width: 1300px) {
    .review-row {
        grid-template-columns: 1fr;
    }

    .review-tile {
        grid-template-columns: 120px 1fr;
    }

    .review-tile img {
        width: 120px;
        height: 156px;
    }
}

/* Mobile */
@media (max-width: 700px) {
    .review-tile {
        grid-template-columns: 1fr;
    }

    .review-tile img {
        width: 100%;
        max-width: 180px;
        height: 210px;
    }
}
'''

if "SITEPULSE PORTRAIT FIX" not in css_text:
    css_text += portrait_patch

css_path.write_text(css_text, encoding="utf-8")
print("Portrait fix applied.")
