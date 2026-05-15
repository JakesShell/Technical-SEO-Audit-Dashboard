from pathlib import Path

css_path = Path("styles.css")
css_text = css_path.read_text(encoding="utf-8")

spacing_patch = r'''

/* =========================================================
   SITEPULSE FINAL SPACING + LAYOUT POLISH
   Keeps the premium dark command-center look, but gives
   the scanner, cards, metrics, and reviews more breathing room.
   ========================================================= */

.console-shell {
    width: min(1780px, calc(100% - 36px));
    padding: 18px 0 34px;
}

.console-grid {
    grid-template-columns: minmax(0, 1fr) minmax(420px, 500px);
    gap: 18px;
    margin-bottom: 16px;
}

.main-console,
.audit-panel {
    border-radius: 26px;
}

.main-console {
    padding: 22px;
}

.audit-panel {
    padding: 28px;
}

.console-header {
    margin-bottom: 20px;
}

.scanner-console {
    padding: 24px;
    border-radius: 22px;
}

.scanner-head {
    margin-bottom: 16px;
}

.scanner-head h2 {
    margin-bottom: 12px;
}

.url-pill {
    max-width: 720px;
}

.risk-pill {
    margin-top: 4px;
}

/* Give the main scan board more room so it feels like the feature, not a thumbnail. */
.xray-board {
    height: 340px;
    margin-top: 22px;
    border-radius: 22px;
}

.scanner-glass {
    inset: 48px 128px 42px;
    border-radius: 24px;
}

/* Pull labels away from edges and improve visual balance. */
.broken {
    left: 18px;
    top: 36px;
}

.heavy {
    right: 18px;
    top: 36px;
}

.schema {
    left: 18px;
    bottom: 34px;
}

.trust {
    right: 18px;
    bottom: 34px;
}

/* Better node spacing around the diamond. */
.node-index {
    left: 18%;
    top: 28%;
}

.node-meta {
    right: 18%;
    top: 28%;
}

.node-schema {
    left: 18%;
    bottom: 22%;
}

.node-speed {
    right: 19%;
    bottom: 22%;
}

/* Give verdict and confidence cards a cleaner rhythm. */
.verdict-strip {
    grid-template-columns: minmax(0, 1fr) 390px;
    gap: 18px;
    margin-top: 16px;
}

.verdict-copy,
.confidence-trend {
    padding: 18px 20px;
    border-radius: 18px;
}

.confidence-trend {
    grid-template-columns: 140px 1fr;
}

/* Metric row was too squeezed. */
.metric-row {
    gap: 14px;
    margin-bottom: 16px;
}

.metric-card {
    min-height: 104px;
    padding: 18px 20px;
    border-radius: 18px;
}

.mini-ring {
    width: 66px;
    height: 66px;
}

.number-card strong {
    font-size: 2.15rem;
}

/* Make the lower section less cramped and more deliberate. */
.lower-grid {
    grid-template-columns: 0.9fr 1.15fr 0.9fr 1.75fr;
    gap: 14px;
    margin-bottom: 16px;
}

.launch-card,
.gate-diamond-card,
.damage-map-card,
.satisfaction-card {
    min-height: 250px;
    padding: 22px;
    border-radius: 22px;
}

.launch-card h3 {
    font-size: 1.55rem;
}

.launch-card a {
    margin-top: 14px;
}

/* The gate diamond needs room to feel expensive. */
.large-diamond {
    width: 158px;
    height: 158px;
    left: calc(50% - 79px);
    top: 40px;
}

.floor-ring {
    bottom: 26px;
    width: 240px;
    height: 50px;
}

.left-door {
    left: 26px;
}

.right-door {
    right: 26px;
}

/* Technical damage map spacing. */
.damage-map {
    height: 178px;
    margin-top: 16px;
}

.damage {
    padding: 8px 12px;
}

/* Satisfaction area needed the most spacing help. */
.satisfaction-head {
    gap: 18px;
    margin-bottom: 16px;
}

.satisfaction-head h3 {
    max-width: 620px;
    font-size: 1.45rem;
}

.rating-box {
    min-width: 150px;
}

.review-stats {
    gap: 10px;
    margin: 16px 0;
}

.review-stats span {
    min-height: 74px;
    padding: 12px;
}

.review-row {
    gap: 14px;
}

.review-tile {
    grid-template-columns: 96px 1fr;
    gap: 14px;
    padding: 14px;
    border-radius: 16px;
}

.review-tile img {
    width: 96px;
    height: 138px;
    border-radius: 14px;
}

.review-tile h4 {
    font-size: 0.95rem;
}

.review-tile p,
.review-tile small {
    font-size: 0.78rem;
}

.review-tile blockquote {
    margin-top: 8px;
    font-size: 0.78rem;
    line-height: 1.45;
}

/* Repair bay cards should look intentional, not squashed. */
.repair-bay {
    padding: 22px;
    border-radius: 24px;
}

.repair-header {
    margin-bottom: 18px;
}

.repair-grid {
    gap: 16px;
}

.repair-card {
    padding: 18px;
    border-radius: 18px;
}

.repair-card h4 {
    margin: 14px 0;
}

.repair-meta {
    gap: 10px;
}

/* Keep responsiveness clean. */
@media (max-width: 1500px) {
    .console-grid,
    .lower-grid {
        grid-template-columns: 1fr;
    }

    .metric-row {
        grid-template-columns: repeat(3, 1fr);
    }

    .review-row {
        grid-template-columns: repeat(3, 1fr);
    }

    .review-stats {
        grid-template-columns: repeat(4, 1fr);
    }

    .audit-panel {
        order: -1;
    }

    .xray-board {
        height: 380px;
    }
}

@media (max-width: 1150px) {
    .metric-row,
    .repair-grid,
    .review-row,
    .review-stats {
        grid-template-columns: repeat(2, 1fr);
    }

    .verdict-strip {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 850px) {
    .console-shell {
        width: min(100% - 20px, 1780px);
        padding-top: 10px;
    }

    .main-console,
    .audit-panel,
    .scanner-console,
    .launch-card,
    .gate-diamond-card,
    .damage-map-card,
    .satisfaction-card,
    .repair-bay {
        padding: 18px;
        border-radius: 20px;
    }

    .console-header,
    .scanner-head,
    .repair-header,
    .satisfaction-head {
        flex-direction: column;
        align-items: flex-start;
    }

    .metric-row,
    .repair-grid,
    .review-row,
    .review-stats,
    .repair-meta {
        grid-template-columns: 1fr;
    }

    .xray-board {
        height: 430px;
    }

    .scanner-glass {
        inset: 64px 24px 50px;
    }

    .hero-diamond {
        width: 138px;
        height: 138px;
        left: calc(50% - 69px);
        top: calc(50% - 72px);
    }

    .signal-node,
    .signal-label {
        font-size: 0.68rem;
    }

    .review-tile {
        grid-template-columns: 90px 1fr;
    }
}
'''

if "SITEPULSE FINAL SPACING + LAYOUT POLISH" not in css_text:
    css_text += spacing_patch

css_path.write_text(css_text, encoding="utf-8")

print("Final SitePulse spacing polish applied.")
