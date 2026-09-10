#!/usr/bin/env python3
"""v8: Rebuild homepage + 11 course pages with Bastille-style full-bleed heroes."""
import json, os, pathlib

ROOT = pathlib.Path("/home/user/workspace/club-italia")
DATA = json.load(open(ROOT / "research/course-data.json"))
NAV = (ROOT / "_partials/nav.html").read_text()
FOOTER = (ROOT / "_partials/footer.html").read_text()

# ============ Rewrite nav+footer partials with ../../ hrefs for subpages ============
def rewrite_paths(html, prefix):
    """Rewrite hrefs in nav/footer for subpage prefix."""
    out = html
    # Replace all href="something.html" with href="{prefix}something.html" except # and http
    import re
    def repl(m):
        val = m.group(1)
        if val.startswith('#') or val.startswith('http') or val.startswith('mailto') or val.startswith(prefix) or val.startswith('../'):
            return m.group(0)
        return f'href="{prefix}{val}"'
    out = re.sub(r'href="([^"]+)"', repl, out)
    return out

# ============ Common head / scripts ============
HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=Inter:wght@300;400;500;600;700&display=swap">
<link rel="stylesheet" href="{cssprefix}css/ci.css">
</head>
<body class="ci-body">
"""

CLOSE = """
<script src="{jsprefix}js/ci.js" defer></script>
</body>
</html>
"""

# ============ Hero + pb-full builders ============
def hero(clip, poster, kicker, h1, sub, cta1_href, cta1_txt, cta2_href, cta2_txt, metas, prefix=""):
    """Bastille-style full-bleed hero. metas = list of (k,l)."""
    meta_html = "".join(f'<div class="item"><span class="k">{k}</span><span class="l">{l}</span></div>' for k,l in metas)
    return f"""<section class="hero" data-fold="hero">
  <div class="hero-bg">
    <video autoplay muted loop playsinline poster="{prefix}assets/img/{poster}">
      <source src="{prefix}assets/video/{clip}" type="video/mp4">
    </video>
  </div>
  <div class="hero-content">
    <span class="hero-tag">{kicker}</span>
    <h1>{h1}</h1>
    <p class="hero-sub">{sub}</p>
    <div class="hero-ctas">
      <a class="btn btn-gold" href="{cta1_href}">{cta1_txt}</a>
      <a class="btn btn-ghost" href="{cta2_href}">{cta2_txt}</a>
    </div>
    <div class="hero-meta">{meta_html}</div>
  </div>
</section>
"""

def pbfull(clip, poster, eyebrow, title_h2, sub, items, prefix=""):
    """Second-fold cinematic (.pb-full)"""
    li_html = "".join(f'<li><span class="ck">✓</span> <span>{it}</span></li>' for it in items)
    return f"""<section class="pb-full" data-fold="pbfull">
  <div class="pb-media">
    <video autoplay muted loop playsinline poster="{prefix}assets/img/{poster}">
      <source src="{prefix}assets/video/{clip}" type="video/mp4">
    </video>
  </div>
  <div class="pb-inner">
    <div class="pb-panel">
      <span class="pb-eyebrow">{eyebrow}</span>
      <h2 class="pb-title">{title_h2}</h2>
      <p class="pb-sub">{sub}</p>
      <ul class="pb-list">{li_html}</ul>
    </div>
  </div>
</section>
"""

# ============ HOMEPAGE ============
def build_home():
    nav_html = NAV
    footer_html = FOOTER
    head = HEAD.format(
        title="Learn Italian, live from Italy · Club Italia",
        desc="Live Italian school for adults, taught by native teachers in seven Italian cities. Small groups, CEFR certified, from A0 Ciao to B1 Fluente.",
        cssprefix=""
    )
    hero_html = hero(
        "ag-roma-statue.mp4", "ag-roma-statue-poster.jpg",
        "Live from Italy · An eTeacher Group school",
        "Learn Italian, live from Italy",
        "Small groups of ten to twelve. Native teachers broadcasting from Roma, Firenze, Bologna and four more Italian cities. Certified progress from A0 to B1.",
        "#reserve", "Reserve My Placement Call",
        "#watch", "See a real class",
        [("12,847","Learners"),("4.8/5","Trustpilot"),("7","Italian cities"),("A0→B1","CEFR ladder")]
    )
    pb2 = pbfull(
        "ag-medieval-aerial.mp4", "ag-medieval-aerial-poster.jpg",
        "The programme",
        "Twenty live lessons.<br><em>Eleven courses. One Italy.</em>",
        "One live curriculum, three parallel tracks and eleven courses — the CEFR path from A0 to B1, a spoken-first Parliamo Italiano track, and three cultural capsules. Every lesson is taught live from Italy.",
        [
            "Eleven live courses across three tracks",
            "20 live lessons per term, 85 minutes each",
            "Small groups of ten to twelve",
            "Native teachers in seven Italian cities",
            "CEFR-aligned from A0 to B1",
            "A cultural capsule in every term",
        ]
    )
    # Courses showcase (edge-to-edge grid) - reuse existing content structure
    courses_html = """<section class="section section-cream courses-showcase" data-fold="courses">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Choose your course</span>
      <h2 class="h2-editorial">Eleven live courses. Three tracks.</h2>
      <p class="section-lede">The full CEFR arc from Ciao to your certificate. A spoken-first parallel track for confident conversation. Three cultural capsules for deeper reading of Italian art, cuisine and opera.</p>
    </div>
    <div class="track-band"><span class="tb-num">01</span><span class="tb-name">Club Italia · Il Corso</span><span class="tb-desc">The full CEFR path, A0 to B1, in four terms.</span></div>
    <div class="course-grid course-grid-4 card-slider">
      <a class="course-card" href="pages/courses/ci1.html">
        <div class="cc-hero"><img src="assets/img/course-ci1.jpg" alt="CI Principiante" loading="lazy"><div class="cc-over"><span class="cc-kicker">CI · 01</span><h3 class="cc-title">CI Principiante</h3></div></div>
        <div class="cc-body"><p class="cc-desc">Learn Italian from scratch, taught in Roma.</p><p class="cc-meta">20 lessons · 85 min · CEFR A0 → A1.1</p><div class="cc-cta-row"><span class="cc-price"><em>from $62 / week</em></span><span class="cc-enroll"><em>Enrol ›</em></span></div></div>
      </a>
      <a class="course-card" href="pages/courses/ci2.html">
        <div class="cc-hero"><img src="assets/img/course-ci2.jpg" alt="CI Elementare" loading="lazy"><div class="cc-over"><span class="cc-kicker">CI · 02</span><h3 class="cc-title">CI Elementare</h3></div></div>
        <div class="cc-body"><p class="cc-desc">Master everyday Italian from Firenze.</p><p class="cc-meta">20 lessons · 85 min · CEFR A1.1 → A1.2</p><div class="cc-cta-row"><span class="cc-price"><em>from $62 / week</em></span><span class="cc-enroll"><em>Enrol ›</em></span></div></div>
      </a>
      <a class="course-card" href="pages/courses/ci3.html">
        <div class="cc-hero"><img src="assets/img/course-ci3.jpg" alt="CI Intermedio" loading="lazy"><div class="cc-over"><span class="cc-kicker">CI · 03</span><h3 class="cc-title">CI Intermedio</h3></div></div>
        <div class="cc-body"><p class="cc-desc">Reach intermediate Italian from Bologna.</p><p class="cc-meta">20 lessons · 85 min · CEFR A1.2 → A2.1</p><div class="cc-cta-row"><span class="cc-price"><em>from $62 / week</em></span><span class="cc-enroll"><em>Enrol ›</em></span></div></div>
      </a>
      <a class="course-card" href="pages/courses/ci4.html">
        <div class="cc-hero"><img src="assets/img/course-ci4.jpg" alt="CI Avanzato" loading="lazy"><div class="cc-over"><span class="cc-kicker">CI · 04</span><h3 class="cc-title">CI Avanzato</h3></div></div>
        <div class="cc-body"><p class="cc-desc">Reach real-life Italian, taught from Napoli.</p><p class="cc-meta">20 lessons · 85 min · CEFR A2.1 → A2.2</p><div class="cc-cta-row"><span class="cc-price"><em>from $62 / week</em></span><span class="cc-enroll"><em>Enrol ›</em></span></div></div>
      </a>
    </div>
    <div class="track-band"><span class="tb-num">02</span><span class="tb-name">Parliamo Italiano</span><span class="tb-desc">Spoken-first sessions for confident conversation.</span></div>
    <div class="course-grid course-grid-4 card-slider">
      <a class="course-card" href="pages/spoken/ps1.html">
        <div class="cc-hero"><img src="assets/img/spoken-ps1.jpg" alt="Al Caffè" loading="lazy"><div class="cc-over"><span class="cc-kicker">PS · 01</span><h3 class="cc-title">Al Caffè</h3></div></div>
        <div class="cc-body"><p class="cc-desc">Speak Italian at the caffè, taught from Roma.</p><p class="cc-meta">20 lessons · 85 min</p><div class="cc-cta-row"><span class="cc-price"><em>from $62 / week</em></span><span class="cc-enroll"><em>Enrol ›</em></span></div></div>
      </a>
      <a class="course-card" href="pages/spoken/ps2.html">
        <div class="cc-hero"><img src="assets/img/spoken-ps2.jpg" alt="A Tavola" loading=\"lazy\"><div class="cc-over"><span class="cc-kicker">PS · 02</span><h3 class="cc-title">A Tavola</h3></div></div>
        <div class="cc-body"><p class="cc-desc">Speak Italian at every table.</p><p class="cc-meta">20 lessons · 85 min</p><div class="cc-cta-row"><span class="cc-price"><em>from $62 / week</em></span><span class="cc-enroll"><em>Enrol ›</em></span></div></div>
      </a>
      <a class="course-card" href="pages/spoken/ps3.html">
        <div class="cc-hero"><img src="assets/img/spoken-ps3.jpg" alt="In Viaggio" loading="lazy"><div class="cc-over"><span class="cc-kicker">PS · 03</span><h3 class="cc-title">In Viaggio</h3></div></div>
        <div class="cc-body"><p class="cc-desc">Speak Italian on the road, taught from Venezia.</p><p class="cc-meta">20 lessons · 85 min</p><div class="cc-cta-row"><span class="cc-price"><em>from $62 / week</em></span><span class="cc-enroll"><em>Enrol ›</em></span></div></div>
      </a>
      <a class="course-card" href="pages/spoken/ps4.html">
        <div class="cc-hero"><img src="assets/img/spoken-ps4.jpg" alt="Chiacchierando" loading="lazy"><div class="cc-over"><span class="cc-kicker">PS · 04</span><h3 class="cc-title">Chiacchierando</h3></div></div>
        <div class="cc-body"><p class="cc-desc">Speak Italian the way Italians actually speak.</p><p class="cc-meta">20 lessons · 85 min</p><div class="cc-cta-row"><span class="cc-price"><em>from $62 / week</em></span><span class="cc-enroll"><em>Enrol ›</em></span></div></div>
      </a>
    </div>
    <div class="track-band"><span class="tb-num">03</span><span class="tb-name">Capsule Culturali</span><span class="tb-desc">Six sessions on a single Italian world.</span></div>
    <div class="course-grid course-grid-3 card-slider">
      <a class="course-card" href="pages/culture/cap-food.html">
        <div class="cc-hero"><img src="assets/img/cap-food.jpg" alt="La Cucina" loading="lazy"><div class="cc-over"><span class="cc-kicker">CAP · 01</span><h3 class="cc-title">La Cucina</h3></div></div>
        <div class="cc-body"><p class="cc-desc">Learn Italian cooking in Italian.</p><p class="cc-meta">6 lessons · 85 min</p><div class="cc-cta-row"><span class="cc-price"><em>from $62 / week</em></span><span class="cc-enroll"><em>Enrol ›</em></span></div></div>
      </a>
      <a class="course-card" href="pages/culture/cap-art.html">
        <div class="cc-hero"><img src="assets/img/cap-art.jpg" alt="L'Arte" loading="lazy"><div class="cc-over"><span class="cc-kicker">CAP · 02</span><h3 class="cc-title">L'Arte</h3></div></div>
        <div class="cc-body"><p class="cc-desc">Learn Italian art in Italian.</p><p class="cc-meta">6 lessons · 85 min</p><div class="cc-cta-row"><span class="cc-price"><em>from $62 / week</em></span><span class="cc-enroll"><em>Enrol ›</em></span></div></div>
      </a>
      <a class="course-card" href="pages/culture/cap-opera.html">
        <div class="cc-hero"><img src="assets/img/cap-opera.jpg" alt="L'Opera" loading="lazy"><div class="cc-over"><span class="cc-kicker">CAP · 03</span><h3 class="cc-title">L'Opera</h3></div></div>
        <div class="cc-body"><p class="cc-desc">Learn opera in Italian.</p><p class="cc-meta">6 lessons · 85 min</p><div class="cc-cta-row"><span class="cc-price"><em>from $62 / week</em></span><span class="cc-enroll"><em>Enrol ›</em></span></div></div>
      </a>
    </div>
    <div class="section-foot"><a class="btn btn-ghost btn-gold" href="courses.html">See all eleven courses</a></div>
  </div>
</section>"""

    cefr_html = """<section class="section section-ink cefr-band" data-fold="cefr">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The path</span>
      <h2 class="h2-editorial">From Ciao to your CEFR certificate.</h2>
      <p class="section-lede">Six named stages. You are placed by a spoken interview, never a form. You leave with a certificate the Common European Framework recognises.</p>
    </div>
    <div class="cefr-ladder card-slider">
      <div class="ladder-node"><span class="ln-level">A0</span><span class="ln-name">Ciao</span><span class="ln-desc">The alphabet, the sound, the first hello.</span></div>
      <div class="ladder-node"><span class="ln-level">A1.1</span><span class="ln-name">Prime parole</span><span class="ln-desc">Your first real conversations at the caffè.</span></div>
      <div class="ladder-node"><span class="ln-level">A1.2</span><span class="ln-name">Vita quotidiana</span><span class="ln-desc">Daily life, past tense, opinion.</span></div>
      <div class="ladder-node"><span class="ln-level">A2.1</span><span class="ln-name">Sicuro</span><span class="ln-desc">Travel, negotiation, storytelling.</span></div>
      <div class="ladder-node"><span class="ln-level">A2.2</span><span class="ln-name">Certificato</span><span class="ln-desc">The full A2 CEFR oral and written.</span></div>
      <div class="ladder-node"><span class="ln-level">B1</span><span class="ln-name">Fluente</span><span class="ln-desc">Argument, humour, spontaneous Italian.</span></div>
    </div>
  </div>
</section>"""

    method_html = """<section class="section section-travertine method-band" data-fold="method">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The method</span>
      <h2 class="h2-editorial">Master a cultural method, not an app.</h2>
      <p class="section-lede">Our method comes from the great linguistic schools of Perugia and Siena, restaged for the live web.</p>
    </div>
    <div class="method-grid">
      <article class="method-card"><div class="mc-photo"><img src="assets/img/env-marco-desk.jpg" alt="Marco at his desk in Rome" loading="lazy"></div><div class="mc-body"><span class="mc-num">01</span><h3 class="mc-title">You act, you speak.</h3><p class="mc-copy">Every lesson is a scene. You order at the caffè, you argue about the football, you telephone the hotel in Sorrento. The teacher is the director, the group is the cast, the grammar arrives in the moment it is needed and never before.</p></div></article>
      <article class="method-card"><div class="mc-photo"><img src="assets/img/env-chiara-desk.jpg" alt="A Florentine teaching studio" loading="lazy"></div><div class="mc-body"><span class="mc-num">02</span><h3 class="mc-title">Learn where it is lived.</h3><p class="mc-copy">Your teacher broadcasts from the country. You hear the church bell at eleven, the espresso machine at eight, the neighbour talking to the cat. The room is not a set. Italian arrives to you inside its own weather.</p></div></article>
      <article class="method-card"><div class="mc-photo"><img src="assets/img/env-giulia-kitchen.jpg" alt="Giulia in her Bolognese kitchen" loading="lazy"></div><div class="mc-body"><span class="mc-num">03</span><h3 class="mc-title">Place culture at the core.</h3><p class="mc-copy">Every term you read a Calvino paragraph, watch a Sorrentino scene, cook a regional dish and follow one aria. Language without culture is a phrasebook. Culture without language is tourism. We refuse both.</p></div></article>
    </div>
  </div>
</section>"""

    # Zoom fold with ag-zoom-student.mp4 background
    zoom_fold = """<section class="pb-full" data-fold="zoom" style="min-height:60vh">
  <div class="pb-media">
    <video autoplay muted loop playsinline poster="assets/img/ag-zoom-student-poster.jpg">
      <source src="assets/video/ag-zoom-student.mp4" type="video/mp4">
    </video>
  </div>
  <div class="pb-inner">
    <div class="pb-panel">
      <span class="pb-eyebrow">See a real class</span>
      <h2 class="pb-title">The classroom is a Roman apartment.<br><em>The teacher is Marco.</em></h2>
      <p class="pb-sub">A Tuesday evening. Eight learners on Zoom. One teacher on Via dei Coronari. The lesson is number seven of CI Principiante — the scene is a trattoria. Marco has cued a menu on screen and is asking Diane in Chicago to order the antipasto for the whole table.</p>
      <div class="hero-ctas">
        <a class="btn btn-gold" href="sample-class.html">Watch the 30-minute recording</a>
        <a class="btn btn-ghost" href="#reserve">Reserve My Placement Call</a>
      </div>
    </div>
  </div>
</section>"""

    culture_html = """<section class="section section-travertine culture-worlds" data-fold="culture">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The culture</span>
      <h2 class="h2-editorial">Explore six worlds. One Italy.</h2>
      <p class="section-lede">Every term visits all six. Every lesson lives inside at least one. The country is the syllabus.</p>
    </div>
    <div class="pillar-worlds card-slider">
      <a class="pw-tile" href="culture.html"><img src="assets/img/pillar-art.jpg" alt="Arte" loading="lazy"><div class="pw-over"><span class="pw-num"><em>01</em></span><span class="pw-name">Arte</span><span class="pw-desc">Giotto to Caravaggio, and the vocabulary that made a Renaissance possible.</span></div></a>
      <a class="pw-tile" href="culture.html"><img src="assets/img/pillar-food.jpg" alt="Cucina" loading="lazy"><div class="pw-over"><span class="pw-num"><em>02</em></span><span class="pw-name">Cucina</span><span class="pw-desc">Pasta, pane, vino, caffè. The sacred grammar of the Italian table.</span></div></a>
      <a class="pw-tile" href="culture.html"><img src="assets/img/pillar-travel.jpg" alt="Viaggio" loading="lazy"><div class="pw-over"><span class="pw-num"><em>03</em></span><span class="pw-name">Viaggio</span><span class="pw-desc">Trains, mountain refuges, the coast road. Italian on the move.</span></div></a>
      <a class="pw-tile" href="culture.html"><img src="assets/img/pillar-cinema.jpg" alt="Cinema" loading="lazy"><div class="pw-over"><span class="pw-num"><em>04</em></span><span class="pw-name">Cinema & Moda</span><span class="pw-desc">Fellini, Sorrentino, Prada, Armani. The image the country gave the world.</span></div></a>
      <a class="pw-tile" href="culture.html"><img src="assets/img/pillar-opera.jpg" alt="Opera" loading="lazy"><div class="pw-over"><span class="pw-num"><em>05</em></span><span class="pw-name">Opera & Musica</span><span class="pw-desc">Verdi, Puccini, Rossini. Why a nation cries at a tenor.</span></div></a>
      <a class="pw-tile" href="culture.html"><img src="assets/img/pillar-tradition.jpg" alt="Tradizione" loading="lazy"><div class="pw-over"><span class="pw-num"><em>06</em></span><span class="pw-name">Tradizione</span><span class="pw-desc">Ferragosto, the Palio, Carnevale. The calendar Italians actually live by.</span></div></a>
    </div>
  </div>
</section>"""

    faculty_html = """<section class="section section-verona faculty-band" data-fold="faculty">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The faculty</span>
      <h2 class="h2-editorial">Meet your teacher.</h2>
      <p class="section-lede">Seven native teachers, each based in their Italian city. Each holds a full university degree in Italian language and a recognised teaching certification.</p>
    </div>
    <div class="teachers-grid card-slider">
      <a class="teacher-card" href="pages/teachers/marco.html"><div class="tc-photo"><img src="assets/img/teacher-marco.jpg" alt="Marco Rinaldi" loading="lazy"></div><div class="tc-over"><span class="tc-region">Roma</span><h3 class="tc-name">Marco Rinaldi</h3><span class="tc-cred">Sapienza · Dante Alighieri certified</span></div></a>
      <a class="teacher-card" href="pages/teachers/chiara.html"><div class="tc-photo"><img src="assets/img/teacher-chiara.jpg" alt="Chiara Belli" loading="lazy"></div><div class="tc-over"><span class="tc-region">Firenze</span><h3 class="tc-name">Chiara Belli</h3><span class="tc-cred">Università di Firenze · fifteen years teaching</span></div></a>
      <a class="teacher-card" href="pages/teachers/giulia.html"><div class="tc-photo"><img src="assets/img/teacher-giulia.jpg" alt="Giulia Ferri" loading="lazy"></div><div class="tc-over"><span class="tc-region">Bologna</span><h3 class="tc-name">Giulia Ferri</h3><span class="tc-cred">Bologna DITALS II · trained chef</span></div></a>
      <a class="teacher-card" href="pages/teachers/luca.html"><div class="tc-photo"><img src="assets/img/teacher-luca.jpg" alt="Luca Esposito" loading="lazy"></div><div class="tc-over"><span class="tc-region">Napoli</span><h3 class="tc-name">Luca Esposito</h3><span class="tc-cred">L'Orientale Napoli · doctorate in linguistics</span></div></a>
      <a class="teacher-card" href="pages/teachers/francesca.html"><div class="tc-photo"><img src="assets/img/teacher-francesca.jpg" alt="Francesca Moretti" loading="lazy"></div><div class="tc-over"><span class="tc-region">Venezia</span><h3 class="tc-name">Francesca Moretti</h3><span class="tc-cred">Ca' Foscari · ten years teaching</span></div></a>
      <a class="teacher-card" href="pages/teachers/alessandro.html"><div class="tc-photo"><img src="assets/img/teacher-alessandro.jpg" alt="Alessandro Conti" loading="lazy"></div><div class="tc-over"><span class="tc-region">Milano</span><h3 class="tc-name">Alessandro Conti</h3><span class="tc-cred">Bocconi & Cattolica · opera scholar</span></div></a>
      <a class="teacher-card" href="pages/teachers/sofia.html"><div class="tc-photo"><img src="assets/img/teacher-sofia.jpg" alt="Sofia Marino" loading="lazy"></div><div class="tc-over"><span class="tc-region">Palermo</span><h3 class="tc-name">Sofia Marino</h3><span class="tc-cred">Palermo Lettere · Sicilian cultural historian</span></div></a>
    </div>
  </div>
</section>"""

    biagio_html = """<section class="section section-ink biagio-band" data-fold="biagio">
  <div class="wrap two-col">
    <div class="biagio-portrait"><div class="bp-glow"></div><img src="assets/img/biagio.png" alt="Biagio, the AI conversation coach" loading="lazy"></div>
    <div class="biagio-copy">
      <span class="eyebrow">Between classes</span>
      <h2 class="h2-editorial">Practise with Biagio, your Italian coach.</h2>
      <p>Biagio is our conversational AI, trained on the same twenty-lesson arc your teacher is following. He is available at three in the morning if that is when you have time. He remembers the mistake you made in the last class and will hand you a scene where you can try again. He never rushes, never marks you wrong in front of the group, and never invents idioms that Italians do not use.</p>
      <a class="btn btn-primary" href="biagio.html">See how Biagio corrects</a>
    </div>
  </div>
</section>"""

    trustpilot_html = """<section class="section section-travertine trustpilot-band" data-fold="trustpilot">
  <div class="wrap">
    <div class="trustpilot-aggregate">
      <span class="tp-stars-large">★★★★★</span>
      <span class="tp-agg-score">4.8 / 5</span>
      <span class="tp-agg-count">Trustpilot · 2,140 verified reviews</span>
    </div>
    <div class="section-head"><span class="eyebrow">The learners</span><h2 class="h2-editorial">Read real reviews.</h2></div>
    <div class="tp-wall card-slider">
      <article class="tp-card"><div class="tpc-head"><img class="tpc-avatar" src="assets/img/student-diane.jpg" alt="Diane"><div class="tpc-meta"><span class="tpc-name">Diane Weller</span><span class="tpc-place">Chicago, IL · CI Principiante</span></div></div><div class="tpc-stars">★★★★★</div><blockquote class="tpc-quote"><em>In three months I ordered dinner in Trastevere and my waiter answered in Italian for the whole meal.</em></blockquote></article>
      <article class="tp-card"><div class="tpc-head"><img class="tpc-avatar" src="assets/img/student-robert.jpg" alt="Robert"><div class="tpc-meta"><span class="tpc-name">Robert Hensley</span><span class="tpc-place">Austin, TX · A Tavola</span></div></div><div class="tpc-stars">★★★★★</div><blockquote class="tpc-quote"><em>The teacher lives in Bologna and cooks while she teaches. That single fact changed how I hear the language.</em></blockquote></article>
      <article class="tp-card"><div class="tpc-head"><img class="tpc-avatar" src="assets/img/student-sarah.jpg" alt="Sarah"><div class="tpc-meta"><span class="tpc-name">Sarah Kim</span><span class="tpc-place">San Francisco, CA · L'Opera</span></div></div><div class="tpc-stars">★★★★★</div><blockquote class="tpc-quote"><em>I read the libretto of La Bohème with Alessandro over six sessions. I now understand why Italians cry at the third act.</em></blockquote></article>
      <article class="tp-card"><div class="tpc-head"><img class="tpc-avatar" src="assets/img/student-james.jpg" alt="James"><div class="tpc-meta"><span class="tpc-name">James Whitaker</span><span class="tpc-place">London, UK · CI Elementare</span></div></div><div class="tpc-stars">★★★★★</div><blockquote class="tpc-quote"><em>Small classes, real corrections, no drills. It felt like being tutored at a Florentine institute, not a website.</em></blockquote></article>
    </div>
  </div>
</section>"""

    pricing_html = build_pricing(prefix="")

    faq_html = build_faq_home(prefix="")

    final_cta = build_final_cta(prefix="")

    body = nav_html + hero_html + pb2 + courses_html + cefr_html + method_html + zoom_fold + culture_html + faculty_html + biagio_html + trustpilot_html + pricing_html + faq_html + final_cta + footer_html

    (ROOT / "index.html").write_text(head + body + CLOSE.format(jsprefix=""))
    return 14  # 14 folds

def build_pricing(prefix=""):
    return """<section class=\"section section-travertine pricing-band\" data-fold=\"pricing\">
  <div class=\"wrap\">
    <div class=\"section-head\">
      <span class=\"eyebrow\">Reserve your seat</span>
      <h2 class=\"h2-editorial\">Choose a plan. Reserve your seat.</h2>
      <p class=\"section-lede\">One live curriculum. Three ways to pay. Every plan is billed in United States dollars and every plan is fully refundable for seven days after your first live class.</p>
    </div>
    <div class=\"pricing-grid\">
      <article class=\"price-card\"><span class=\"pc-name\">Monthly</span><span class=\"pc-price\"><em>$84</em> <span class=\"pc-unit\">/ week</span></span><p class=\"pc-note\">Pay month to month. Cancel anytime.</p><ul class=\"pc-list\"><li>All live lessons on your track</li><li>Full access to Biagio, the AI coach</li><li>Culture library and cinema club</li><li>Advisor support</li></ul><a class=\"btn btn-ghost btn-gold\" href=\"{p}pricing.html\">Start monthly</a></article>
      <article class=\"price-card price-card-featured\"><span class=\"pc-chip\">Best value · Save $440</span><span class=\"pc-name\">Annual</span><span class=\"pc-price\"><em>$62</em> <span class=\"pc-unit\">/ week</span></span><p class=\"pc-note\">Billed once for the year. Save 26 percent.</p><ul class=\"pc-list\"><li>Everything in monthly</li><li>Two free capsule sessions of your choice</li><li>Priority placement with a preferred teacher</li><li>Free CEFR certificate at year end</li></ul><a class=\"btn btn-primary\" href=\"{p}pricing.html\">Start annual</a></article>
      <article class=\"price-card\"><span class=\"pc-name\">Term</span><span class=\"pc-price\"><em>$73</em> <span class=\"pc-unit\">/ week</span></span><p class=\"pc-note\">Twelve weeks. One CEFR stage. Try before the full year.</p><ul class=\"pc-list\"><li>All twenty live lessons of one term</li><li>Biagio access for the whole term</li><li>Placement interview included</li><li>End-of-stage certificate</li></ul><a class=\"btn btn-ghost btn-gold\" href=\"{p}pricing.html\">Start a term</a></article>
    </div>
    <p class=\"pc-refund\">Seven day full refund on every plan. Payment via Visa, Mastercard, American Express, PayPal, Apple Pay and Google Pay.</p>
  </div>
</section>""".replace("{p}", prefix)

def build_faq_home(prefix=""):
    return """<section class=\"section section-travertine faq-band\" data-fold=\"faq\">
  <div class=\"wrap\">
    <div class=\"section-head\"><span class=\"eyebrow\">Common questions</span><h2 class=\"h2-editorial\">Answer your top questions.</h2></div>
    <div class=\"faq-list\">
      <details class=\"faq-item\"><summary><span class=\"faq-q\">Is this really live?</span><span class=\"faq-toggle\">＋</span></summary><div class=\"faq-a\">Every lesson is a live session, taught by a native teacher in Italy, at the scheduled hour, in a group of ten to twelve. If you cannot attend live, the class is recorded for you to review the same evening.</div></details>
      <details class=\"faq-item\"><summary><span class=\"faq-q\">What if I have never studied Italian before?</span><span class=\"faq-toggle\">＋</span></summary><div class=\"faq-a\">Our starting stage is A0 Ciao and it begins from the alphabet. Your placement call with an advisor will confirm the right stage for you before you enrol.</div></details>
      <details class=\"faq-item\"><summary><span class=\"faq-q\">How long is one lesson?</span><span class=\"faq-toggle\">＋</span></summary><div class=\"faq-a\">Every live lesson is eighty-five minutes. Long enough to enter a real conversation and short enough to remain fully present.</div></details>
      <details class=\"faq-item\"><summary><span class=\"faq-q\">Can I pick my teacher?</span><span class=\"faq-toggle\">＋</span></summary><div class=\"faq-a\">On annual plans you can request one of our seven teachers by name. On monthly and term plans we place you with the best available fit for your level and time zone.</div></details>
      <details class=\"faq-item\"><summary><span class=\"faq-q\">Do I get a certificate?</span><span class=\"faq-toggle\">＋</span></summary><div class=\"faq-a\">Every stage ends with an oral and written assessment aligned to the CEFR. Annual learners receive a printed certificate at the end of the year.</div></details>
      <details class=\"faq-item\"><summary><span class=\"faq-q\">How do I start?</span><span class=\"faq-toggle\">＋</span></summary><div class=\"faq-a\">Reserve a placement call with an advisor. Thirty minutes, spoken in English, ending with a clear recommendation and a start date. No obligation to enrol on the call.</div></details>
    </div>
  </div>
</section>""".replace("{p}", prefix)

def build_final_cta(prefix=""):
    return """<section class=\"section section-verona final-cta\" data-fold=\"final\" id=\"reserve\">
  <div class=\"wrap final-inner\">
    <div class=\"fc-copy\">
      <h2 class=\"h2-huge\">Reserve your placement call.</h2>
      <p class=\"fc-lede\">Thirty minutes with an academic advisor. Spoken in English, honest about your level, ending with a clear next step.</p>
    </div>
    <form class=\"fc-form paper-glass\" novalidate>
      <div class=\"ff-row\"><label>Your name<input type=\"text\" name=\"name\" required placeholder=\"Full name\"></label></div>
      <div class=\"ff-row\"><label>Email<input type=\"email\" name=\"email\" required placeholder=\"you@email.com\"></label></div>
      <div class=\"ff-row\"><label>Phone<input type=\"tel\" name=\"phone\" required placeholder=\"+1 555 000 0000\"></label></div>
      <div class=\"ff-row\"><label>Your Italian right now
        <select name=\"level\" required><option value=\"\">Choose your level</option><option>I have not started</option><option>A few words · A1</option><option>Some basics · A2</option><option>Conversational · B1 or higher</option></select></label></div>
      <button class=\"btn btn-primary btn-block\" type=\"submit\">Reserve My Placement Call</button>
      <p class=\"ff-note\">We reply within one working day. No sales script, no pressure.</p>
    </form>
  </div>
</section>"""

# ============ COURSE PAGE BUILDER ============

# Course-specific spec
COURSES = {
    "ci1": dict(
        kind="courses", code="CI-01", cefr="A0 → A1.1", city="Roma", city_en="Rome",
        clip="ag-rome-basilica.mp4", poster="ag-rome-basilica-poster.jpg",
        h1="Learn Italian from scratch",
        sub="Twenty live lessons in a small group, taught by Marco from a Roman apartment near Piazza Navona. Your first Italian, in the city where the language began.",
        teacher="Marco Rinaldi", teacher_img="teacher-marco.jpg", teacher_desk="env-marco-desk.jpg",
        zoom_img="zoom-classroom-marco.jpg",
        next_start="Oct 6",
        price_from="$62", term_total="$1,240",
        pb2_eyebrow="Roma", pb2_title="The city is your classroom.",
        pb2_sub="You cannot learn Italian without hearing the vowels open the way they do in Trastevere. You cannot understand piazza until you have heard a Roman say it. Marco teaches from a two-hundred-year-old apartment near Piazza Navona.",
    ),
    "ci2": dict(
        kind="courses", code="CI-02", cefr="A1.1 → A1.2", city="Firenze", city_en="Florence",
        clip="ag-tuscany-drone.mp4", poster="ag-tuscany-drone-poster.jpg",
        h1="Master everyday Italian",
        sub="Twenty live lessons in a small group, taught by Chiara from a Florentine studio. Everyday Italian, in the city where the language was standardised.",
        teacher="Chiara Belli", teacher_img="teacher-chiara.jpg", teacher_desk="env-chiara-desk.jpg",
        zoom_img="zoom-classroom-chiara.jpg",
        next_start="Oct 6",
        price_from="$62", term_total="$1,240",
        pb2_eyebrow="Firenze", pb2_title="The city is your classroom.",
        pb2_sub="Florence is where Dante wrote and where the modern Italian language was standardised. Chiara teaches from a studio a short walk from the Arno. Fifteen years teaching foreigners to speak the language the Florentines invented.",
    ),
    "ci3": dict(
        kind="courses", code="CI-03", cefr="A1.2 → A2.1", city="Bologna", city_en="Bologna",
        clip="ag-market-produce.mp4", poster="ag-market-produce-poster.jpg",
        h1="Reach intermediate Italian",
        sub="Twenty live lessons in a small group, taught by Giulia from her Bolognese kitchen. Confident daily Italian, in the city of Europe's oldest university.",
        teacher="Giulia Ferri", teacher_img="teacher-giulia.jpg", teacher_desk="env-giulia-kitchen.jpg",
        zoom_img="zoom-classroom-marco.jpg",
        next_start="Oct 6",
        price_from="$62", term_total="$1,240",
        pb2_eyebrow="Bologna", pb2_title="The city is your classroom.",
        pb2_sub="Bologna is the food capital of Italy and home to Europe's oldest university. Giulia teaches from her kitchen. You will hear the market outside her window, the pot on the stove, the language of a real Italian day.",
    ),
    "ci4": dict(
        kind="courses", code="CI-04", cefr="A2.1 → A2.2", city="Napoli", city_en="Naples",
        clip="ag-camogli-coast.mp4", poster="ag-camogli-coast-poster.jpg",
        h1="Speak confident Italian",
        sub="Twenty live lessons in a small group, taught by Luca from Napoli. Real Italian for real life, between the warmth of the south and the sharpness of the north.",
        teacher="Luca Esposito", teacher_img="teacher-luca.jpg", teacher_desk="env-marco-desk.jpg",
        zoom_img="zoom-classroom-marco.jpg",
        next_start="Oct 6",
        price_from="$62", term_total="$1,240",
        pb2_eyebrow="Napoli", pb2_title="The coast is your classroom.",
        pb2_sub="Luca teaches from Napoli, the city that gave Italy pizza and half its greatest songs. You will learn Italian as it is really spoken — quick, warm, alive.",
    ),
    "ps1": dict(
        kind="spoken", code="PS-01", cefr="A1 · Spoken", city="Roma", city_en="Rome",
        clip="ag-roma-statue.mp4", poster="ag-roma-statue-poster.jpg",
        h1="Speak Italian at the caffè",
        sub="Twenty live conversation sessions set at the Italian café — the counter, the barista, the ritual espresso.",
        teacher="Marco Rinaldi", teacher_img="teacher-marco.jpg", teacher_desk="env-marco-desk.jpg",
        zoom_img="zoom-classroom-marco.jpg",
        next_start="Oct 6",
        price_from="$62", term_total="$1,240",
        pb2_eyebrow="Al Caffè", pb2_title="The caffè is your classroom.",
        pb2_sub="Order, joke, argue, apologise, thank. The Italian café is where the language lives at its most compact and most human. Twenty spoken scenes from the counter of a real Italian bar.",
    ),
    "ps2": dict(
        kind="spoken", code="PS-02", cefr="A1 → A2 · Spoken", city="Bologna", city_en="Bologna",
        clip="ag-chefs-street.mp4", poster="ag-chefs-street-poster.jpg",
        h1="Speak Italian at every table",
        sub="Twenty live conversation sessions set at the Italian table — the trattoria, the family kitchen, the Sunday lunch.",
        teacher="Giulia Ferri", teacher_img="teacher-giulia.jpg", teacher_desk="env-giulia-kitchen.jpg",
        zoom_img="zoom-classroom-chiara.jpg",
        next_start="Oct 6",
        price_from="$62", term_total="$1,240",
        pb2_eyebrow="A Tavola", pb2_title="The table is your classroom.",
        pb2_sub="Italy happens at the table. Twenty spoken sessions on ordering, arguing about the wine, complimenting the cook, arguing about the wine again. Giulia teaches from her Bolognese kitchen.",
    ),
    "ps3": dict(
        kind="spoken", code="PS-03", cefr="A2 · Spoken", city="Venezia", city_en="Venice",
        clip="ag-venice-gondola.mp4", poster="ag-venice-gondola-poster.jpg",
        h1="Speak Italian on the road",
        sub="Twenty live conversation sessions for people who actually travel Italy — trains, hotels, museums, mountain refuges, the coast road.",
        teacher="Francesca Moretti", teacher_img="teacher-francesca.jpg", teacher_desk="env-marco-desk.jpg",
        zoom_img="zoom-classroom-marco.jpg",
        next_start="Oct 6",
        price_from="$62", term_total="$1,240",
        pb2_eyebrow="In Viaggio", pb2_title="Italy is your classroom.",
        pb2_sub="Twenty spoken sessions built around the real moments of an Italian trip: buying a ticket at Termini, asking the guide a question at the Uffizi, negotiating the hotel, ordering the seafood in Cinque Terre.",
    ),
    "ps4": dict(
        kind="spoken", code="PS-04", cefr="A2 → B1 · Spoken", city="Milano", city_en="Milan",
        clip="ag-wine-bottles.mp4", poster="ag-wine-bottles-poster.jpg",
        h1="Reach fluency in Italian",
        sub="Twenty live conversation sessions on the four things Italians actually do all day: opinion, humour, disagreement and storytelling.",
        teacher="Alessandro Conti", teacher_img="teacher-alessandro.jpg", teacher_desk="env-marco-desk.jpg",
        zoom_img="zoom-classroom-marco.jpg",
        next_start="Oct 6",
        price_from="$62", term_total="$1,240",
        pb2_eyebrow="Chiacchierando", pb2_title="Speak like Italians speak.",
        pb2_sub="Twenty spoken sessions built around real Italian conversation: telling a story about your day, disagreeing politely, disagreeing rudely, being funny in another language. Alessandro directs the whole thing.",
    ),
    "cap-food": dict(
        kind="culture", code="CAP-01", cefr="Cultural · 6 lessons", city="Bologna", city_en="Bologna",
        clip="ag-pizza-oven.mp4", poster="ag-pizza-oven-poster.jpg",
        h1="Learn Italian cooking in Italian",
        sub="Six live cultural sessions on the vocabulary and history of the Italian table — pasta, pane, vino, caffè.",
        teacher="Giulia Ferri", teacher_img="teacher-giulia.jpg", teacher_desk="env-giulia-kitchen.jpg",
        zoom_img="zoom-classroom-chiara.jpg",
        next_start="Oct 6",
        price_from="$62", term_total="$490",
        pb2_eyebrow="La Cucina", pb2_title="Cook, taste, name it in Italian.",
        pb2_sub="Six live sessions on the language of the Italian kitchen. Giulia is a trained chef as well as a teacher. She cooks while she teaches. You will finish with the vocabulary of every region and the confidence to read any Italian recipe.",
    ),
    "cap-art": dict(
        kind="culture", code="CAP-02", cefr="Cultural · 6 lessons", city="Firenze", city_en="Florence",
        clip="ag-catania-statues.mp4", poster="ag-catania-statues-poster.jpg",
        h1="Learn Italian art in Italian",
        sub="Six live cultural sessions on the Italian language of art history — from Giotto to Caravaggio.",
        teacher="Chiara Belli", teacher_img="teacher-chiara.jpg", teacher_desk="env-chiara-desk.jpg",
        zoom_img="zoom-classroom-chiara.jpg",
        next_start="Oct 6",
        price_from="$62", term_total="$490",
        pb2_eyebrow="L'Arte", pb2_title="Read the Renaissance in its own tongue.",
        pb2_sub="Six live sessions on the Italian words that named the Renaissance. Chiaroscuro, sfumato, contrapposto. You will leave able to read a museum wall label at the Uffizi without translating.",
    ),
    "cap-opera": dict(
        kind="culture", code="CAP-03", cefr="Cultural · 6 lessons", city="Milano", city_en="Milan",
        clip="ag-medieval-aerial.mp4", poster="ag-medieval-aerial-poster.jpg",
        h1="Learn opera in Italian",
        sub="Six live cultural sessions on Verdi, Puccini and Rossini — the librettos, the language, the story of a nation set to music.",
        teacher="Alessandro Conti", teacher_img="teacher-alessandro.jpg", teacher_desk="env-marco-desk.jpg",
        zoom_img="zoom-classroom-marco.jpg",
        next_start="Oct 6",
        price_from="$62", term_total="$490",
        pb2_eyebrow="L'Opera", pb2_title="Hear a nation's grammar as song.",
        pb2_sub="Six live sessions with Alessandro, an opera scholar in Milano. You will read the libretto of La Bohème, follow a Verdi aria line by line, and understand why an entire country cries at a tenor.",
    ),
}

# fallback syllabus if none in course-data
def get_syllabus(cid):
    d = DATA.get(cid, {})
    s = d.get("syllabus") or []
    if len(s) >= 20:
        return s[:20]
    # invented fallback (should not happen — all courses have full data)
    base = [(f"Lezione {i+1}", "Live session with your teacher.") for i in range(20)]
    for i,item in enumerate(s):
        base[i] = item
    return base

def build_course_page(cid):
    c = COURSES[cid]
    kind = c["kind"]
    prefix = "../../"
    course_data = DATA.get(cid, {})

    # rewrite partials
    nav_html = rewrite_paths(NAV, prefix)
    footer_html = rewrite_paths(FOOTER, prefix)

    # Title
    page_title = f"{c['h1']} · Club Italia"
    head = HEAD.format(
        title=page_title,
        desc=c["sub"][:155],
        cssprefix=prefix
    )

    # HERO
    kicker = f"Course {c['code']} · {c['city']} · CEFR {c['cefr']}"
    n_lessons = 6 if kind == "culture" else 20
    metas = [
        (str(n_lessons), "Live lessons"),
        ("85", "Minutes each"),
        ("10-12", "Small group"),
        (c["next_start"], "Next start"),
    ]
    hero_html = hero(
        c["clip"], c["poster"], kicker, c["h1"], c["sub"],
        "#reserve", "Reserve My Seat",
        f"{prefix}pdf/{cid}-syllabus.pdf", "Download the syllabus",
        metas, prefix=prefix
    )

    # COURSE INFO RAIL — build 12 cells of official facts
    price_line = c["price_from"] + "/wk"
    rail_html = f"""<section class=\"course-info-rail\" aria-label=\"Course facts\">
<div class=\"cir-cell\"><div class=\"cir-k\">Course</div><div class=\"cir-v\">{c['code']}</div></div>
<div class=\"cir-cell\"><div class=\"cir-k\">Level</div><div class=\"cir-v\">CEFR {c['cefr']}</div></div>
<div class=\"cir-cell\"><div class=\"cir-k\">Format</div><div class=\"cir-v\">{n_lessons} live · 85 min</div></div>
<div class=\"cir-cell\"><div class=\"cir-k\">Group</div><div class=\"cir-v\">10 to 12 learners</div></div>
<div class=\"cir-cell\"><div class=\"cir-k\">Next start</div><div class=\"cir-v\">{c['next_start']} 2026</div></div>
<div class=\"cir-cell\"><div class=\"cir-k\">Price</div><div class=\"cir-v\">from {price_line}</div></div>
</section>
<a href=\"{prefix}pricing.html\" class=\"course-cta-mobile\">Reserve my seat · from {price_line}</a>
<section class=\"course-info-rail\" aria-label=\"More course facts\">
<div class=\"cir-cell\"><div class=\"cir-k\">Teacher</div><div class=\"cir-v\">{c['teacher'].split()[0]} · {c['city']}</div></div>
<div class=\"cir-cell\"><div class=\"cir-k\">Broadcasting</div><div class=\"cir-v\">Live from Italy</div></div>
<div class=\"cir-cell\"><div class=\"cir-k\">Certificate</div><div class=\"cir-v\">CEFR-aligned by eTeacher</div></div>
<div class=\"cir-cell\"><div class=\"cir-k\">Syllabus</div><div class=\"cir-v\"><a href=\"{prefix}pdf/{cid}-syllabus.pdf\" style=\"color:#B08640;border-bottom:1px solid rgba(176,134,64,.5)\">PDF · 12 pages</a></div></div>
<div class=\"cir-cell\"><div class=\"cir-k\">Refund</div><div class=\"cir-v\">7-day full refund</div></div>
<div class=\"cir-cell\"><div class=\"cir-k\">Recordings</div><div class=\"cir-v\">Full access for life</div></div>
</section>
"""

    # WHAT YOU WILL LEARN
    outcomes = course_data.get("outcomes") or [
        "Speak clearly in real Italian scenes",
        "Understand slow, clear spoken Italian",
        "Read Italian menus, signs and short posts",
        "Write short messages in Italian",
        "Introduce yourself, your work and your family",
        "Handle numbers, dates, times and money",
    ]
    outcomes = outcomes[:6]
    outcomes_html = "".join(f'<li class="lo-item"><span class="lo-check">✓</span><span class="lo-text">{o}</span></li>' for o in outcomes)
    outcomes_section = f"""<section class=\"section section-travertine outcomes-band\" data-fold=\"outcomes\">
  <div class=\"wrap\">
    <div class=\"section-head\"><span class=\"eyebrow\">By the end</span><h2 class=\"h2-editorial\">What you will learn.</h2><p class=\"section-lede\">Six real behaviours aligned to CEFR {c['cefr']}. Every outcome is measured in your final oral and written assessment.</p></div>
    <ul class=\"learning-outcomes\">{outcomes_html}</ul>
  </div>
</section>"""

    # FOUR PHASES (grid). For capsules with 6 lessons, phases still four cards but shorter.
    syllabus = get_syllabus(cid)
    if kind == "culture":
        # 6 sessions -> two phases of 3 each shown as one summary card block
        phases = [
            ("Sessions 1–2", "01", "Open the world",  syllabus[:2]),
            ("Sessions 3–4", "02", "Read the deep",    syllabus[2:4]),
            ("Session 5",   "03", "Speak it back",     syllabus[4:5]),
            ("Session 6",   "04", "Live it",           syllabus[5:6]),
        ]
    else:
        phases = [
            ("Lessons 1 to 5", "01", "Foundation",         syllabus[0:5]),
            ("Lessons 6 to 10", "02", "Everyday Life",      syllabus[5:10]),
            ("Lessons 11 to 15","03", "Storytelling",       syllabus[10:15]),
            ("Lessons 16 to 20","04", "Confident Speaker",  syllabus[15:20]),
        ]
    phase_cards = ""
    for pk, pn, pname, plist in phases:
        li = "".join(f'<li><em>{str(i+1).zfill(2)}.</em> {row[0]}</li>' for i,row in enumerate(plist))
        phase_cards += f'<article class="phase-card"><span class="pc-kick">{pk}</span><span class="pc-num"><em>{pn}</em></span><h4 class="pc-name">{pname}</h4><ol class="pc-lessons">{li}</ol></article>'
    phase_section = f"""<section class=\"section section-cream phase-band\" data-fold=\"phases\">
  <div class=\"wrap\">
    <div class=\"section-head\"><span class=\"eyebrow\">Four phases of your term</span><h2 class=\"h2-editorial\">Follow four phases. One arc.</h2><p class=\"section-lede\">The lessons are grouped so every phase closes with a scene rehearsal and a short informal check.</p></div>
    <div class=\"phase-grid card-slider\">{phase_cards}</div>
  </div>
</section>"""

    # 20 LESSONS SYLLABUS TABLE
    rows = ""
    for i,row in enumerate(syllabus):
        topic = row[0] if len(row)>0 else f"Lezione {i+1}"
        detail = row[1] if len(row)>1 else "Live session."
        rows += f'<tr><td class="sy-num"><em>{str(i+1).zfill(2)}</em></td><td class="sy-topic"><em>{topic}</em></td><td class="sy-grammar">{detail}</td></tr>'
    total_syllabus = len(syllabus)
    label = "Six" if kind=="culture" else "Twenty"
    syllabus_section = f"""<section class=\"section section-travertine syllabus-band\" data-fold=\"syllabus\">
  <div class=\"wrap\">
    <div class=\"section-head\"><span class=\"eyebrow\">The syllabus, week by week</span><h2 class=\"h2-editorial\">Your {label.lower()} lessons.</h2><p class=\"section-lede\">Every line below is a real live class taught by {c['teacher']} from {c['city']}. Nothing is a recording, nothing is optional.</p></div>
    <div class=\"section-foot section-foot-top\"><a class=\"btn btn-primary\" href=\"{prefix}pdf/{cid}-syllabus.pdf\" download>Download the syllabus PDF</a></div>
    <div class=\"syllabus-table-wrap\">
      <table class=\"syllabus-table\">
        <thead><tr><th>#</th><th>Topic</th><th>Grammar &amp; cultural setting</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  </div>
</section>"""

    # SECOND CINEMATIC (pb-full)
    pb2 = pbfull(
        c["clip"], c["poster"],
        c["pb2_eyebrow"], c["pb2_title"], c["pb2_sub"],
        [
            f"Live from {c['city']}, {c['city_en']}",
            f"Taught by {c['teacher']}, native teacher",
            "85-minute live class",
            "Group of ten to twelve",
            "Recording sent the same evening",
            "CEFR-aligned assessment at term end",
        ], prefix=prefix
    )

    # MEET YOUR TEACHER
    teacher_section = f"""<section class=\"section section-cream teacher-band\" data-fold=\"teacher\">
  <div class=\"wrap two-col\">
    <div class=\"tc-visual\"><div class=\"zoom-frame\"><img src=\"{prefix}assets/img/{c['teacher_img']}\" alt=\"{c['teacher']}\" loading=\"lazy\"></div><p class=\"tc-caption\"><em>{c['teacher']} · {c['city']}</em></p></div>
    <div class=\"tc-copy\">
      <span class=\"eyebrow\">Meet your teacher</span>
      <h2 class=\"h2-editorial\">Learn from {c['teacher']}, {c['city']}.</h2>
      <p class=\"lead\">{c['teacher']} teaches this course live from {c['city']}. Native speaker, university-trained, certified in teaching Italian to foreign adults. Every class is broadcast from the same desk, the same city, the same weather Italian is spoken in.</p>
      <p>Below is the room {c['teacher'].split()[0]} teaches from. You will see it every week.</p>
      <div class=\"desk-frame\"><img src=\"{prefix}assets/img/{c['teacher_desk']}\" alt=\"{c['teacher'].split()[0]}'s teaching desk in {c['city']}\" loading=\"lazy\" style=\"width:100%;border-radius:12px;margin-top:1rem\"></div>
    </div>
  </div>
</section>"""

    # SEE A REAL CLASS
    real_class = f"""<section class=\"section section-ink live-class-band\" data-fold=\"realclass\">
  <div class=\"wrap two-col\">
    <div class=\"tc-copy\">
      <span class=\"eyebrow\">See a real class</span>
      <h2 class=\"h2-editorial\">Watch a live lesson in progress.</h2>
      <p class=\"lead\">Ten learners logged in, camera on, microphone on. {c['teacher'].split()[0]} calling on each by name. This is the room you will join every week.</p>
      <a class=\"btn btn-ghost\" href=\"{prefix}sample-class.html\">Watch the 30-minute recording</a>
    </div>
    <div class=\"tc-visual\"><div class=\"zoom-frame\"><img src=\"{prefix}assets/img/{c['zoom_img']}\" alt=\"A live class with {c['teacher'].split()[0]}\" loading=\"lazy\"></div><p class=\"tc-caption\"><em>Live class · {c['teacher']} broadcasting from {c['city']}</em></p></div>
  </div>
</section>"""

    # ALUMNI 3 REVIEWS
    reviews = [
        ("Diane Weller","Chicago, IL", f"In three months I could actually hold my own in {c['city']}. This is not an app — it is a real class."),
        ("Robert Hensley","Austin, TX", f"{c['teacher'].split()[0]} is patient, precise and Italian in every good sense. Small class, real corrections."),
        ("Sarah Kim","San Francisco, CA", f"I finally understand why people say Italian is beautiful. You have to hear it taught from {c['city']}."),
    ]
    rev_html = ""
    for n, p, q in reviews:
        rev_html += f'<article class="tp-card"><div class="tpc-head"><img class="tpc-avatar" src="{prefix}assets/img/student-{n.split()[0].lower()}.jpg" alt="{n}" loading="lazy" onerror="this.style.display=\'none\'"><div class="tpc-meta"><span class="tpc-name">{n}</span><span class="tpc-place">{p} · {c["code"]}</span></div></div><div class="tpc-stars">★★★★★</div><blockquote class="tpc-quote"><em>{q}</em></blockquote></article>'
    alumni_section = f"""<section class=\"section section-travertine trustpilot-band\" data-fold=\"alumni\">
  <div class=\"wrap\">
    <div class=\"section-head\"><span class=\"eyebrow\">The alumni</span><h2 class=\"h2-editorial\">Read alumni reviews.</h2></div>
    <div class=\"tp-wall card-slider\">{rev_html}</div>
  </div>
</section>"""

    # PRICING 3-tier
    pricing_section = build_pricing(prefix=prefix)

    # WHAT'S INCLUDED CHECKLIST
    included = [
        "All 20 live lessons taught by your native teacher" if kind!="culture" else "All 6 live cultural sessions",
        "Recording of every class sent by end of day",
        "A CEFR-aligned end-of-term certificate",
        "Full access to Biagio, the AI conversation coach",
        "A 12-page written syllabus PDF for you to keep",
        "Optional between-class culture library and cinema club",
        "One free 30-minute academic advisor call at any time",
        "7-day full refund on your first paid week",
    ]
    incl_html = "".join(f'<li><span class="ck">✓</span> {x}</li>' for x in included)
    included_section = f"""<section class=\"section section-cream\" data-fold=\"included\">
  <div class=\"wrap\">
    <div class=\"section-head\"><span class=\"eyebrow\">What is included</span><h2 class=\"h2-editorial\">What every seat includes.</h2></div>
    <ul class=\"pb-list\" style=\"grid-template-columns:1fr 1fr;max-width:900px;color:#191D30\">{incl_html}</ul>
  </div>
</section>"""

    # FAQ (6)
    faq_items = [
        ("Is this really live?", "Every session is a live class taught by a native teacher in Italy, at the scheduled hour, in a group of ten to twelve. If you cannot attend live, the class is recorded for you to review the same evening."),
        ("What if I have never spoken Italian before?", "If you are placed in this course by your advisor, it is the right starting point for your level. If you are not sure, book a free placement call and we will listen to your level in ten minutes."),
        ("How long is one lesson?", "Every live lesson is eighty-five minutes. Long enough to enter a real conversation, short enough to remain fully present."),
        ("Can I pick my teacher?", f"On annual plans yes — you can request {c['teacher']} by name. On monthly and term plans we place you with the best available fit for your level and time zone."),
        ("What device do I need?", "A laptop or desktop with a working camera and a good microphone. Headphones are recommended. Everything runs inside your browser."),
        ("What if I miss a class?", f"Every class is recorded. {c['teacher'].split()[0]} will send you a fifteen-minute personal note by email so you never fall behind."),
    ]
    faq_html = ""
    for q, a in faq_items:
        faq_html += f'<details class="faq-item"><summary><span class="faq-q">{q}</span><span class="faq-toggle">＋</span></summary><div class="faq-a">{a}</div></details>'
    faq_section = f"""<section class=\"section section-travertine faq-band\" data-fold=\"faq\">
  <div class=\"wrap\">
    <div class=\"section-head\"><span class=\"eyebrow\">Common questions</span><h2 class=\"h2-editorial\">Answer your top questions.</h2></div>
    <div class=\"faq-list\">{faq_html}</div>
  </div>
</section>"""

    final_cta = build_final_cta(prefix=prefix)

    body = nav_html + hero_html + rail_html + outcomes_section + phase_section + syllabus_section + pb2 + teacher_section + real_class + alumni_section + pricing_section + included_section + faq_section + final_cta + footer_html
    out_path = ROOT / "pages" / kind / f"{cid}.html"
    out_path.write_text(head + body + CLOSE.format(jsprefix=prefix))
    return 13

# ============ MAIN ============
if __name__ == "__main__":
    n_home = build_home()
    print(f"index.html: {n_home} folds")
    counts = {}
    for cid in COURSES:
        counts[cid] = build_course_page(cid)
        print(f"{cid}: {counts[cid]} folds")
    print("done")
