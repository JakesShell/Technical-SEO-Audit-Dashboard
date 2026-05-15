from pathlib import Path

index_path = Path("index.html")
css_path = Path("styles.css")

index_text = index_path.read_text(encoding="utf-8")
css_text = css_path.read_text(encoding="utf-8")

old_gate = """
                <div class="gate-visual {% if report.launch_confidence >= 80 %}open{% elif report.launch_confidence >= 65 %}partial{% else %}blocked{% endif %}">
                    <div class="gate-door left-door"></div>
                    <div class="gate-door right-door"></div>
                    <div class="gate-core">
                        <strong>{{ report.launch_confidence }}%</strong>
                        <span>Confidence</span>
                    </div>
                </div>
"""

new_gate = """
                <div class="gate-visual {% if report.launch_confidence >= 80 %}open{% elif report.launch_confidence >= 65 %}partial{% else %}blocked{% endif %}">
                    <div class="gate-door left-door"></div>
                    <div class="gate-door right-door"></div>

                    <div class="diamond-aura"></div>

                    <div class="diamond-core-wrap">
                        <div class="glass-diamond">
                            <i class="facet facet-1"></i>
                            <i class="facet facet-2"></i>
                            <i class="facet facet-3"></i>
                            <i class="facet facet-4"></i>
                            <i class="facet facet-5"></i>
                            <i class="facet facet-6"></i>
                            <strong>{{ report.launch_confidence }}%</strong>
                            <span>Confidence</span>
                        </div>
                    </div>
                </div>
"""

index_text = index_text.replace(old_gate, new_gate)

index_path.write_text(index_text, encoding="utf-8")

premium_css = """

/* =========================================================
   PREMIUM DIAMOND CORE UPGRADE
   ========================================================= */

.gate-visual {
    position: relative;
    min-height: 260px;
    border-radius: 28px;
    background:
        radial-gradient(circle at center, rgba(98,212,255,0.10), transparent 42%),
        rgba(255,255,255,0.035);
    border: 1px solid var(--line);
    overflow: hidden;
}

.gate-door {
    position: absolute;
    top: 18px;
    bottom: 18px;
    width: 42%;
    border-radius: 24px;
    background:
        linear-gradient(145deg, rgba(98,212,255,0.12), rgba(255,255,255,0.03));
    border: 1px solid var(--line);
    transition: transform 0.45s ease;
    backdrop-filter: blur(10px);
}

.left-door { left: 18px; }
.right-door { right: 18px; }

.gate-visual.open .left-door { transform: translateX(-22%); }
.gate-visual.open .right-door { transform: translateX(22%); }

.gate-visual.partial .left-door { transform: translateX(-8%); }
.gate-visual.partial .right-door { transform: translateX(8%); }

.gate-visual.blocked .left-door,
.gate-visual.blocked .right-door {
    background: rgba(255, 143, 143, 0.08);
}

.diamond-aura {
    position: absolute;
    inset: 50% auto auto 50%;
    width: 220px;
    height: 220px;
    transform: translate(-50%, -50%);
    border-radius: 999px;
    background:
        radial-gradient(circle, rgba(98,212,255,0.24), transparent 48%);
    filter: blur(18px);
    animation: auraPulse 2.8s ease-in-out infinite;
    z-index: 2;
}

@keyframes auraPulse {
    0%, 100% { transform: translate(-50%, -50%) scale(1); opacity: 0.75; }
    50% { transform: translate(-50%, -50%) scale(1.08); opacity: 1; }
}

.diamond-core-wrap {
    position: absolute;
    inset: 50% auto auto 50%;
    transform: translate(-50%, -50%);
    width: 180px;
    height: 180px;
    z-index: 4;
    animation: diamondFloat 3.2s ease-in-out infinite;
}

@keyframes diamondFloat {
    0%, 100% { transform: translate(-50%, -50%) translateY(0px); }
    50% { transform: translate(-50%, -50%) translateY(-10px); }
}

.glass-diamond {
    position: relative;
    width: 100%;
    height: 100%;
    clip-path: polygon(
        50% 0%,
        82% 18%,
        100% 50%,
        82% 82%,
        50% 100%,
        18% 82%,
        0% 50%,
        18% 18%
    );
    display: grid;
    place-items: center;
    color: #ffffff;
    background:
        radial-gradient(circle at 30% 24%, rgba(255,255,255,0.88), transparent 18%),
        linear-gradient(145deg, rgba(133, 226, 255, 0.95), rgba(18, 53, 82, 0.92) 45%, rgba(7, 20, 31, 0.98) 100%);
    border: 1px solid rgba(255,255,255,0.35);
    box-shadow:
        0 0 0 10px rgba(98,212,255,0.07),
        0 18px 40px rgba(0,0,0,0.28),
        inset 0 1px 0 rgba(255,255,255,0.42);
    overflow: hidden;
}

.glass-diamond strong {
    position: relative;
    z-index: 6;
    font-size: 2.1rem;
    letter-spacing: -0.05em;
    text-shadow: 0 6px 18px rgba(0,0,0,0.22);
}

.glass-diamond span {
    position: relative;
    z-index: 6;
    margin-top: -6px;
    color: rgba(255,255,255,0.84);
    font-weight: 900;
    font-size: 0.82rem;
    letter-spacing: 0.03em;
}

.facet {
    position: absolute;
    background: rgba(255,255,255,0.16);
    border: 1px solid rgba(255,255,255,0.18);
    backdrop-filter: blur(6px);
    z-index: 3;
}

.facet-1 {
    top: 10%;
    left: 20%;
    width: 60%;
    height: 24%;
    clip-path: polygon(0 100%, 50% 0, 100% 100%);
}

.facet-2 {
    top: 28%;
    left: 10%;
    width: 30%;
    height: 36%;
    clip-path: polygon(100% 0, 0 50%, 100% 100%);
}

.facet-3 {
    top: 28%;
    right: 10%;
    width: 30%;
    height: 36%;
    clip-path: polygon(0 0, 100% 50%, 0 100%);
}

.facet-4 {
    bottom: 8%;
    left: 18%;
    width: 30%;
    height: 28%;
    clip-path: polygon(50% 100%, 0 0, 100% 0);
}

.facet-5 {
    bottom: 8%;
    right: 18%;
    width: 30%;
    height: 28%;
    clip-path: polygon(50% 100%, 0 0, 100% 0);
}

.facet-6 {
    top: 36%;
    left: 36%;
    width: 28%;
    height: 28%;
    border-radius: 18px;
    background: rgba(255,255,255,0.10);
}

/* make the old orb styling harmless if it still exists anywhere */
.gate-core {
    display: none !important;
}

/* stronger review portraits */
.review-card img {
    width: 110px;
    height: 110px;
    object-fit: cover;
    border-radius: 24px;
    border: 1px solid var(--line);
    box-shadow: 0 14px 28px rgba(0,0,0,0.12);
    background: #dfe7ec;
}

/* make review cards feel more premium */
.review-card {
    align-items: start;
}

.review-body blockquote {
    font-size: 1.05rem;
}

/* optional stronger light mode contrast for diamond */
body.light-mode .glass-diamond {
    background:
        radial-gradient(circle at 30% 24%, rgba(255,255,255,0.92), transparent 18%),
        linear-gradient(145deg, rgba(170, 237, 255, 0.98), rgba(41, 107, 148, 0.94) 45%, rgba(10, 31, 47, 0.98) 100%);
}
"""

if premium_css not in css_text:
    css_text += premium_css

css_path.write_text(css_text, encoding="utf-8")

print("Premium diamond upgrade applied.")
