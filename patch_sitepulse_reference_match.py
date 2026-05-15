from pathlib import Path

css_path = Path("styles.css")
css_text = css_path.read_text(encoding="utf-8")

patch = r'''

/* =========================================================
   SITEPULSE REFERENCE-MATCH VISUAL PASS
   Goal: make screenshot 1 move much closer to screenshot 2
   ========================================================= */

.console-shell {
    width: min(1920px, calc(100% - 24px));
    padding: 8px 0 24px;
}

.console-grid {
    grid-template-columns: minmax(0, 1fr) 440px;
    gap: 16px;
    margin-bottom: 12px;
}

.main-console,
.audit-panel,
.metric-card,
.launch-card,
.gate-diamond-card,
.damage-map-card,
.satisfaction-card,
.repair-bay {
    border-radius: 18px;
    box-shadow:
        0 0 0 1px rgba(67, 157, 255, 0.16),
        0 0 36px rgba(10, 115, 255, 0.12),
        0 20px 60px rgba(0, 0, 0, 0.42);
}

.main-console {
    padding: 16px;
}

.audit-panel {
    padding: 18px;
}

.console-header {
    margin-bottom: 14px;
}

.brand-row {
    gap: 12px;
}

.hex-logo {
    width: 48px;
    height: 48px;
    box-shadow:
        0 0 0 1px rgba(124,231,255,0.22),
        0 0 24px rgba(32,183,255,0.34);
}

h1 {
    font-size: 1.15rem;
}

.scanner-console {
    padding: 16px;
    border-radius: 16px;
    background:
        radial-gradient(circle at 50% 40%, rgba(31, 160, 255, 0.12), transparent 36%),
        linear-gradient(180deg, rgba(255,255,255,0.018), rgba(255,255,255,0.01)),
        rgba(3, 16, 31, 0.86);
}

.scanner-head h2 {
    font-size: clamp(2.35rem, 4vw, 3.8rem);
    margin-bottom: 10px;
}

.url-pill {
    max-width: 620px;
    font-size: 0.78rem;
    min-height: 34px;
    padding: 8px 12px;
}

.risk-pill {
    min-height: 38px;
    padding: 8px 14px;
    box-shadow: 0 0 22px rgba(255, 201, 92, 0.12);
}

.xray-board {
    position: relative;
    height: 240px;
    margin-top: 16px;
    border-radius: 16px;
    overflow: hidden;
    background:
        radial-gradient(circle at 50% 42%, rgba(20, 126, 255, 0.15), transparent 30%),
        linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01)),
        rgba(4, 16, 31, 0.92);
}

.xray-board::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 16% 62%, rgba(145,89,255,0.32), transparent 12%),
        radial-gradient(circle at 28% 24%, rgba(101,244,168,0.28), transparent 12%),
        radial-gradient(circle at 78% 28%, rgba(255,201,92,0.25), transparent 12%),
        radial-gradient(circle at 78% 70%, rgba(32,183,255,0.3), transparent 12%);
    opacity: 0.55;
    pointer-events: none;
}

.cosmic-map {
    opacity: 1;
    background:
        radial-gradient(circle at 50% 50%, rgba(20,170,255,0.22), transparent 28%),
        radial-gradient(circle at 22% 28%, rgba(101,244,168,0.28), transparent 3%),
        radial-gradient(circle at 80% 28%, rgba(255,201,92,0.28), transparent 3%),
        radial-gradient(circle at 20% 74%, rgba(155,99,255,0.26), transparent 3%),
        radial-gradient(circle at 79% 74%, rgba(32,183,255,0.32), transparent 3%),
        radial-gradient(circle at 40% 30%, rgba(255,255,255,0.55) 1px, transparent 1.6px),
        radial-gradient(circle at 60% 58%, rgba(255,255,255,0.55) 1px, transparent 1.6px),
        radial-gradient(circle at 72% 44%, rgba(255,255,255,0.55) 1px, transparent 1.6px),
        repeating-linear-gradient(0deg, transparent 0 16px, rgba(255,255,255,0.015) 17px),
        repeating-linear-gradient(90deg, transparent 0 16px, rgba(255,255,255,0.015) 17px);
    filter: saturate(1.15);
}

.scanner-glass {
    inset: 26px 54px 24px;
    border-radius: 20px;
    transform: perspective(1200px) rotateX(5deg);
    background:
        linear-gradient(145deg, rgba(255,255,255,0.08), rgba(255,255,255,0.018)),
        rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.14);
    box-shadow:
        0 18px 60px rgba(0,0,0,0.3),
        inset 0 1px 0 rgba(255,255,255,0.15);
}

.signal-label {
    z-index: 6;
    padding: 7px 12px;
    border-radius: 999px;
    font-size: 0.76rem;
    background: rgba(4, 16, 31, 0.88);
    box-shadow: 0 0 18px rgba(255,255,255,0.04);
}

.broken { left: 10px; top: 54px; }
.heavy { right: 10px; top: 54px; }
.schema { left: 10px; bottom: 14px; }
.trust { right: 10px; bottom: 14px; }

.signal-node {
    min-width: 84px;
    text-align: center;
    padding: 10px 14px;
    border-radius: 12px;
    font-size: 0.82rem;
    background:
        linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02)),
        rgba(7, 26, 46, 0.92);
    box-shadow:
        0 0 0 1px rgba(124,231,255,0.12),
        0 0 20px rgba(32,183,255,0.22),
        inset 0 1px 0 rgba(255,255,255,0.12);
}

.signal-node::after {
    content: "";
    position: absolute;
    width: 14px;
    height: 14px;
    right: -8px;
    top: 50%;
    transform: translateY(-50%);
    border-radius: 999px;
    background: currentColor;
    box-shadow:
        0 0 10px currentColor,
        0 0 22px currentColor;
    opacity: 0.95;
}

.node-index { left: 18%; top: 18%; color: #6bff90; }
.node-meta { right: 18%; top: 18%; color: #ffbf44; }
.node-schema { left: 14%; bottom: 16%; color: #be79ff; }
.node-speed { right: 18%; bottom: 16%; color: #36b8ff; }

.beam {
    z-index: 4;
    height: 3px;
    border-radius: 999px;
    opacity: 0.95;
    filter:
        drop-shadow(0 0 6px currentColor)
        drop-shadow(0 0 16px currentColor);
}

.beam-index { width: 280px; left: 50%; top: 50%; transform: rotate(-154deg); color: #6bff90; }
.beam-meta { width: 290px; left: 50%; top: 50%; transform: rotate(-25deg); color: #ffbf44; }
.beam-schema { width: 285px; left: 50%; top: 50%; transform: rotate(152deg); color: #be79ff; }
.beam-speed { width: 285px; left: 50%; top: 50%; transform: rotate(26deg); color: #36b8ff; }

.diamond-platform {
    width: 190px;
    height: 24px;
    bottom: 10px;
    background: radial-gradient(ellipse, rgba(108, 235, 255, 0.72), transparent 68%);
    filter: blur(4px);
}

.hero-diamond {
    width: 182px;
    height: 182px;
    left: calc(50% - 91px);
    top: calc(50% - 94px);
    clip-path: polygon(50% 0%, 74% 10%, 100% 50%, 74% 90%, 50% 100%, 26% 90%, 0 50%, 26% 10%);
    background:
        radial-gradient(circle at 34% 22%, rgba(255,255,255,0.98), transparent 16%),
        linear-gradient(145deg, rgba(133, 233, 255, 0.98), rgba(68, 132, 255, 0.92) 46%, rgba(6, 28, 62, 0.98) 100%);
    box-shadow:
        0 0 0 10px rgba(119,229,255,0.08),
        0 0 24px rgba(124,231,255,0.9),
        0 0 52px rgba(49,126,255,0.62),
        0 30px 80px rgba(0,0,0,0.38),
        inset 0 1px 0 rgba(255,255,255,0.55);
    animation: floatDiamond 3.2s ease-in-out infinite;
}

.hero-diamond::before {
    content: "";
    position: absolute;
    inset: -10px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(102,228,255,0.35), transparent 60%);
    filter: blur(12px);
    z-index: 0;
}

.hero-diamond strong {
    font-size: 3rem;
    text-shadow: 0 0 18px rgba(255,255,255,0.18);
}

.hero-diamond span {
    font-size: 1.15rem;
    margin-top: -12px;
    color: rgba(255,255,255,0.88);
}

.facet {
    inset: 18%;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.15);
}

.verdict-strip {
    grid-template-columns: minmax(0, 1fr) 380px;
    gap: 10px;
    margin-top: 10px;
}

.verdict-copy,
.confidence-trend {
    padding: 14px 16px;
    border-radius: 14px;
    background: rgba(3, 16, 31, 0.88);
    box-shadow: inset 0 0 0 1px rgba(71, 160, 255, 0.14);
}

.verdict-copy h3 {
    font-size: 0.95rem;
    margin-bottom: 6px;
}

.verdict-copy p {
    font-size: 0.82rem;
    line-height: 1.45;
}

.confidence-trend {
    grid-template-columns: 126px 1fr;
}

.confidence-trend strong {
    font-size: 1.8rem;
}

.sparkline {
    height: 44px;
}

.audit-panel h2 {
    font-size: 1.9rem;
    line-height: 1;
    margin-bottom: 10px;
}

.audit-form {
    gap: 14px;
}

.run-button {
    min-height: 52px;
    border-radius: 12px;
    background: linear-gradient(90deg, #7d30ff, #31c6ff);
    box-shadow:
        0 0 0 1px rgba(147,95,255,0.18),
        0 0 28px rgba(64,171,255,0.26);
}

.metric-row {
    gap: 8px;
    margin-bottom: 10px;
}

.metric-card {
    min-height: 84px;
    padding: 12px 14px;
    border-radius: 14px;
    box-shadow:
        0 0 0 1px rgba(69, 159, 255, 0.14),
        0 0 24px rgba(32,183,255,0.08);
}

.mini-ring {
    width: 52px;
    height: 52px;
    box-shadow: 0 0 12px rgba(101,244,168,0.12);
}

.metric-card span {
    font-size: 0.92rem;
}

.number-card strong {
    font-size: 2rem;
}

.lower-grid {
    grid-template-columns: 0.9fr 1.25fr 1fr 1.95fr;
    gap: 8px;
    align-items: stretch;
    margin-bottom: 10px;
}

.launch-card,
.gate-diamond-card,
.damage-map-card,
.satisfaction-card {
    min-height: 250px;
    padding: 14px;
    border-radius: 16px;
}

.launch-card h3 {
    font-size: 0.98rem;
    line-height: 1.15;
    margin-bottom: 8px;
}

.launch-card p {
    font-size: 0.76rem;
    line-height: 1.45;
}

.launch-card a {
    margin-top: 10px;
    padding: 9px 14px;
    font-size: 0.76rem;
}

.gate-diamond-card {
    background:
        radial-gradient(circle at center, rgba(34,185,255,0.18), transparent 36%),
        rgba(3, 16, 31, 0.88);
}

.gate-door {
    top: 18px;
    bottom: 18px;
    width: 25%;
    border-radius: 16px;
    background:
        linear-gradient(145deg, rgba(60,190,255,0.18), rgba(151,100,255,0.08)),
        rgba(10, 25, 46, 0.8);
    box-shadow:
        inset 0 0 0 1px rgba(85, 168, 255, 0.18),
        0 0 22px rgba(32,183,255,0.08);
}

.floor-ring {
    width: 190px;
    height: 28px;
    bottom: 12px;
    background: radial-gradient(ellipse, rgba(124,231,255,0.72), transparent 72%);
    filter: blur(4px);
}

.large-diamond {
    width: 160px;
    height: 160px;
    left: calc(50% - 80px);
    top: 20px;
    clip-path: polygon(50% 0%, 74% 10%, 100% 50%, 74% 90%, 50% 100%, 26% 90%, 0 50%, 26% 10%);
    background:
        radial-gradient(circle at 34% 22%, rgba(255,255,255,0.98), transparent 16%),
        linear-gradient(145deg, rgba(133, 233, 255, 0.98), rgba(68, 132, 255, 0.92) 46%, rgba(6, 28, 62, 0.98) 100%);
    box-shadow:
        0 0 0 10px rgba(119,229,255,0.08),
        0 0 24px rgba(124,231,255,0.82),
        0 0 50px rgba(49,126,255,0.48),
        0 24px 70px rgba(0,0,0,0.38),
        inset 0 1px 0 rgba(255,255,255,0.55);
}

.large-diamond strong {
    font-size: 2.3rem;
}

.damage-map-card .eyebrow,
.satisfaction-card .eyebrow,
.launch-card .eyebrow {
    margin-bottom: 8px;
}

.damage-map {
    height: 172px;
    margin-top: 8px;
    border-radius: 14px;
    background:
        radial-gradient(circle at 50% 50%, rgba(34,185,255,0.12), transparent 32%),
        repeating-linear-gradient(0deg, transparent 0 14px, rgba(255,255,255,0.02) 15px),
        repeating-linear-gradient(90deg, transparent 0 14px, rgba(255,255,255,0.02) 15px),
        rgba(4,16,31,0.86);
}

.damage::after {
    animation: ping 2s ease-out infinite;
}

.satisfaction-card {
    overflow: hidden;
    padding: 12px 14px;
}

.satisfaction-head {
    gap: 12px;
    margin-bottom: 8px;
}

.satisfaction-head h3 {
    max-width: 430px;
    font-size: 0.98rem;
    line-height: 1.15;
}

.rating-box {
    min-width: 100px;
}

.rating-box strong {
    font-size: 1.8rem;
}

.review-stats {
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 8px;
    margin: 10px 0 12px;
}

.review-stats span {
    min-height: 62px;
    padding: 10px;
    border-radius: 12px;
    font-size: 0.68rem;
}

.review-stats strong {
    font-size: 1.15rem;
}

.review-row {
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 10px;
}

.review-tile {
    grid-template-columns: 94px 1fr;
    gap: 10px;
    min-height: 176px;
    padding: 10px;
    border-radius: 14px;
    background:
        linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02)),
        rgba(4,16,31,0.85);
    box-shadow: inset 0 0 0 1px rgba(68, 157, 255, 0.14);
}

.review-tile img {
    width: 94px;
    height: 138px;
    object-fit: cover;
    object-position: center 18%;
    border-radius: 12px;
    box-shadow:
        0 0 0 1px rgba(255,255,255,0.08),
        0 0 18px rgba(255,255,255,0.04);
}

.review-tile h4 {
    font-size: 0.84rem;
    margin-bottom: 2px;
}

.review-tile p {
    font-size: 0.72rem;
    line-height: 1.2;
}

.review-tile small {
    font-size: 0.68rem;
}

.stars {
    display: block;
    margin: 6px 0;
    font-size: 0.86rem;
}

.review-tile blockquote {
    font-size: 0.66rem;
    line-height: 1.38;
    color: var(--muted);
}

.repair-bay {
    padding: 14px;
    border-radius: 16px;
}

.repair-header {
    margin-bottom: 10px;
}

.repair-header h3 {
    font-size: 1.1rem;
}

.severity-tabs {
    gap: 8px;
}

.severity-tabs span {
    padding: 6px 10px;
    font-size: 0.76rem;
}

.repair-grid {
    gap: 10px;
}

.repair-card {
    padding: 12px;
    border-radius: 14px;
}

.repair-card h4 {
    font-size: 0.94rem;
    margin: 10px 0;
    line-height: 1.25;
}

.repair-meta {
    gap: 8px;
}

.repair-meta span {
    font-size: 0.7rem;
}

/* stronger glow for icons / rings / chips */
.metric-card,
.signal-node,
.signal-label,
.damage,
.review-stats span,
.repair-card {
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.metric-card:hover,
.signal-node:hover,
.review-stats span:hover,
.repair-card:hover {
    transform: translateY(-2px);
}

/* mobile / tablet */
@media (max-width: 1600px) {
    .lower-grid {
        grid-template-columns: 1fr 1fr;
    }

    .satisfaction-card {
        grid-column: span 2;
    }
}

@media (max-width: 1200px) {
    .console-grid,
    .lower-grid {
        grid-template-columns: 1fr;
    }

    .metric-row {
        grid-template-columns: repeat(3, 1fr);
    }

    .review-row,
    .repair-grid {
        grid-template-columns: 1fr;
    }

    .satisfaction-card {
        grid-column: auto;
    }
}

@media (max-width: 800px) {
    .metric-row,
    .review-stats,
    .repair-meta {
        grid-template-columns: 1fr;
    }

    .review-tile {
        grid-template-columns: 84px 1fr;
    }

    .review-tile img {
        width: 84px;
        height: 126px;
    }
}

'''

if "SITEPULSE REFERENCE-MATCH VISUAL PASS" not in css_text:
    css_text += patch

css_path.write_text(css_text, encoding="utf-8")
print("Reference-match visual pass applied.")
