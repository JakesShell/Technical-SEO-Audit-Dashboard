from pathlib import Path

css_path = Path("styles.css")
css_text = css_path.read_text(encoding="utf-8")

patch = r'''

/* =========================================================
   SITEPULSE FINAL CEO POLISH PASS
   Fixes portrait presentation, diamond dominance, scanner glow,
   and final premium command-center spacing.
   ========================================================= */

.scanner-stage {
    height: 470px;
}

.glass-browser {
    inset: 64px 96px 58px;
}

.main-diamond {
    width: 260px;
    height: 260px;
    left: calc(50% - 130px);
    top: calc(50% - 138px);
    background:
        radial-gradient(circle at 32% 20%, rgba(255,255,255,1), transparent 15%),
        radial-gradient(circle at 70% 72%, rgba(91,215,255,.42), transparent 22%),
        linear-gradient(145deg, rgba(179,247,255,.98), rgba(69,144,255,.94) 42%, rgba(4,20,54,.98) 100%);
    box-shadow:
        0 0 0 14px rgba(133,237,255,.08),
        0 0 38px rgba(133,237,255,.95),
        0 0 92px rgba(50,128,255,.72),
        0 36px 110px rgba(0,0,0,.52),
        inset 0 1px 0 rgba(255,255,255,.72),
        inset 0 -18px 38px rgba(4,18,48,.55);
}

.main-diamond strong {
    font-size: 4.2rem;
}

.main-diamond span {
    margin-top: -28px;
    font-size: 1.25rem;
}

.main-diamond::after {
    content: "";
    position: absolute;
    inset: 10px;
    clip-path: inherit;
    background:
        linear-gradient(115deg, transparent 0 26%, rgba(255,255,255,.38) 32%, transparent 42%),
        linear-gradient(245deg, transparent 0 42%, rgba(255,255,255,.18) 48%, transparent 56%);
    opacity: .8;
    z-index: 2;
    pointer-events: none;
}

.facet {
    background: rgba(255,255,255,.11);
    border-color: rgba(255,255,255,.22);
}

.diamond-shadow {
    width: 320px;
    height: 44px;
    bottom: 42px;
    background: radial-gradient(ellipse, rgba(133,237,255,.88), transparent 70%);
}

.node {
    box-shadow:
        0 0 0 1px rgba(124,231,255,.18),
        0 0 30px rgba(35,186,255,.32),
        inset 0 1px 0 rgba(255,255,255,.18);
}

.node::after {
    box-shadow:
        0 0 14px currentColor,
        0 0 34px currentColor,
        0 0 58px currentColor;
}

.beam {
    height: 4px;
    opacity: 1;
    filter:
        drop-shadow(0 0 8px currentColor)
        drop-shadow(0 0 24px currentColor)
        drop-shadow(0 0 42px currentColor);
}

.beam-index { width: 430px; }
.beam-meta { width: 440px; }
.beam-schema { width: 430px; }
.beam-speed { width: 430px; }

.review-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 22px;
}

.review-card {
    grid-template-columns: 170px 1fr;
    min-height: 270px;
    padding: 20px;
    border-radius: 20px;
}

.review-card img {
    width: 170px;
    height: 230px;
    object-fit: cover;
    object-position: center center;
    border-radius: 18px;
    filter: saturate(1.04) contrast(1.03);
}

.review-card h4 {
    font-size: 1.15rem;
}

.review-card p,
.review-card small {
    font-size: .9rem;
}

.review-card blockquote {
    font-size: 1rem;
    line-height: 1.5;
}

.satisfaction-section {
    padding: 28px;
}

.satisfaction-header h3 {
    font-size: 2rem;
}

.gate-diamond {
    width: 220px;
    height: 220px;
    left: calc(50% - 110px);
    top: 32px;
    box-shadow:
        0 0 0 14px rgba(133,237,255,.08),
        0 0 38px rgba(133,237,255,.85),
        0 0 84px rgba(50,128,255,.62),
        0 34px 100px rgba(0,0,0,.5),
        inset 0 1px 0 rgba(255,255,255,.65);
}

.gate-diamond strong {
    font-size: 3.4rem;
}

.gate-floor {
    width: 320px;
    height: 58px;
    bottom: 24px;
}

@media (max-width: 1500px) {
    .review-grid {
        grid-template-columns: 1fr;
    }

    .review-card {
        grid-template-columns: 180px 1fr;
    }

    .review-card img {
        width: 180px;
        height: 240px;
    }
}

@media (max-width: 680px) {
    .review-card {
        grid-template-columns: 1fr;
    }

    .review-card img {
        width: 100%;
        max-width: 220px;
    }
}
'''

if "SITEPULSE FINAL CEO POLISH PASS" not in css_text:
    css_text += patch

css_path.write_text(css_text, encoding="utf-8")
print("Final CEO polish CSS applied.")
