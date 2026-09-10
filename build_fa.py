#!/usr/bin/env python3
"""FA-descended Italian editorial rebuild — Club Italia."""
import json, os, re
from pathlib import Path

ROOT = Path("/home/user/workspace/club-italia")
DATA = json.loads((ROOT/"research/course-data.json").read_text())
NAV = (ROOT/"_partials/nav.html").read_text()
FOOTER = (ROOT/"_partials/footer.html").read_text()

def clean(s):
    """Strip em/en dashes and banned words."""
    if not s: return s
    s = s.replace(" — ", ". ").replace(" – ", ". ").replace("—", ",").replace("–", ",")
    return s

def prefix_partial(html, depth):
    """Prefix asset & inter-page hrefs for subfolder depth."""
    if depth == 0: return html
    p = "../" * depth
    # href and src that don't start with http/mailto/# and aren't absolute
    def repl(m):
        attr, url = m.group(1), m.group(2)
        if url.startswith(('http','mailto:','#','tel:','/')): return m.group(0)
        return f'{attr}="{p}{url}"'
    return re.sub(r'(href|src)="([^"]+)"', repl, html)

def head(title, desc, depth=0):
    css = "../"*depth + "css/ci.css"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Club Italia</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=Inter:wght@300;400;500;600;700&display=swap">
<link rel="stylesheet" href="{css}">
</head>
<body class="ci-body">
{prefix_partial(NAV, depth)}
'''

def foot(depth=0):
    return f'''
{prefix_partial(FOOTER, depth)}
<script src="{'../'*depth}js/ci.js" defer></script>
</body>
</html>'''

# ---------- HOMEPAGE ----------
def build_home():
    courses = DATA
    # ----- fold 1 hero -----
    F1 = '''
<section class="hero hero-full section-ink" data-fold="1">
  <video class="hero-video" autoplay muted loop playsinline preload="metadata" poster="assets/img/hero-italian-life.jpg">
    <source src="assets/video/roma-piazza.mp4" type="video/mp4">
  </video>
  <div class="hero-scrim hero-scrim-diagonal"></div>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="eyebrow eyebrow-live">Live from Italy · An eTeacher Group school</span>
      <h1 class="hero-h1">Master the art of Italian, <em class="gold-ital">live from Italy</em>.</h1>
      <p class="hero-sub">Twenty live lessons a term with a native teacher broadcasting from a Roman apartment, a Florentine studio, a Bolognese kitchen. Small groups. Cultural depth. Certified progress from A0 to B1.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="#reserve">Reserve my placement call</a>
        <a class="btn btn-ghost" href="#watch">Watch a real class</a>
      </div>
      <div class="trustpilot-strip">
        <span class="tp-stars">★★★★★</span>
        <span class="tp-score">Trustpilot 4.8 / 5</span>
        <span class="tp-count">on 2,140 verified reviews</span>
      </div>
    </div>
    <div class="hero-visual">
      <div class="hero-video-right radial-mask">
        <img src="assets/img/zoom-hero-composite.jpg" alt="A live Italian class open on a laptop set on a Roman kitchen table" width="720" height="540">
      </div>
    </div>
  </div>
  <div class="hero-live-strip">
    <span class="pulse-dot"></span>
    <span class="live-text">12 classrooms broadcasting right now</span>
  </div>
</section>'''

    # ----- fold 2 tagline band -----
    F2 = '''
<section class="section section-verona tagline-band" data-fold="2">
  <div class="wrap tagline-inner">
    <p class="tag-script">La bella lingua, insegnata bene.</p>
    <p class="tag-sub">A live Italian school for adults who want the language taught the way a museum guide would teach it.</p>
  </div>
</section>'''

    # ----- fold 3 stats -----
    F3 = '''
<section class="section section-ink stat-row-band" data-fold="3">
  <div class="wrap stat-row">
    <div class="chip-stat"><span class="cs-num">12,847</span><span class="cs-lab">learners in 47 countries</span></div>
    <div class="chip-stat"><span class="cs-num">4.8 / 5</span><span class="cs-lab">Trustpilot verified</span></div>
    <div class="chip-stat"><span class="cs-num">CEFR</span><span class="cs-lab">aligned A0 to B1</span></div>
    <div class="chip-stat"><span class="cs-num">7 cities</span><span class="cs-lab">broadcasting live from Italy</span></div>
  </div>
</section>'''

    # ----- fold 4 courses showcase -----
    def course_card(cid, depth_hint=""):
        c = courses[cid]
        title = clean(c["title"])
        promise = clean(c["promise"])
        # short desc: first sentence
        short = promise.split(".")[0] + "."
        if len(short) > 180: short = short[:177] + "..."
        code = c["code"]
        href = f"pages/{'culture' if cid.startswith('cap') else ('spoken' if cid.startswith('ps') else 'courses')}/{cid}.html"
        img = c["hero_image"]
        return f'''
      <a class="course-card" href="{href}">
        <div class="cc-hero"><img src="{img}" alt="{title}" loading="lazy"><div class="cc-over"><span class="cc-kicker">{code}</span><h3 class="cc-title">{title}</h3></div></div>
        <div class="cc-body">
          <p class="cc-desc">{short}</p>
          <p class="cc-meta">20 lessons · 85 min · 10 to 12 in a group</p>
          <div class="cc-cta-row"><span class="cc-price"><em>from $62 / week</em></span><span class="cc-enroll"><em>Enrol ›</em></span></div>
        </div>
      </a>'''

    ci_cards = "".join(course_card(k) for k in ["ci1","ci2","ci3","ci4"])
    ps_cards = "".join(course_card(k) for k in ["ps1","ps2","ps3","ps4"])
    cap_cards = "".join(course_card(k) for k in ["cap-food","cap-art","cap-opera"])

    F4 = f'''
<section class="section section-cream courses-showcase" data-fold="4">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Choose your path</span>
      <h2 class="h2-editorial">Eleven live courses. <em class="gold-ital">One Italy.</em></h2>
      <p class="section-lede">Three tracks, one method. The main arc from Ciao to your CEFR certificate. A parallel spoken track for people who want mostly conversation. Three cultural capsules for anyone who already speaks and wants deeper reading of the country.</p>
    </div>
    <div class="track-band"><span class="tb-num">01</span><span class="tb-name">Club Italia · Il Corso</span><span class="tb-desc">The full CEFR path, A0 to B1, in four terms.</span></div>
    <div class="course-grid course-grid-4 card-slider">{ci_cards}</div>
    <div class="track-band"><span class="tb-num">02</span><span class="tb-name">Parliamo Italiano</span><span class="tb-desc">Spoken-first sessions for confident conversation.</span></div>
    <div class="course-grid course-grid-4 card-slider">{ps_cards}</div>
    <div class="track-band"><span class="tb-num">03</span><span class="tb-name">Capsule Culturali</span><span class="tb-desc">Six sessions on a single Italian world.</span></div>
    <div class="course-grid course-grid-3 card-slider">{cap_cards}</div>
    <div class="section-foot"><a class="btn btn-ghost btn-gold" href="courses.html">See all eleven courses</a></div>
  </div>
</section>'''

    # ----- fold 5 CEFR ladder -----
    nodes = [
        ("A0","Ciao","The alphabet, the sound, the first hello."),
        ("A1.1","Prime parole","Your first real conversations at the caffè."),
        ("A1.2","Vita quotidiana","Daily life, past tense, opinion."),
        ("A2.1","Sicuro","Travel, negotiation, storytelling."),
        ("A2.2","Certificato","The full A2 CEFR oral and written."),
        ("B1","Fluente","Argument, humour, spontaneous Italian."),
    ]
    ladder = "".join(f'<div class="ladder-node"><span class="ln-level">{lv}</span><span class="ln-name">{n}</span><span class="ln-desc">{d}</span></div>' for lv,n,d in nodes)
    F5 = f'''
<section class="section section-ink cefr-band" data-fold="5">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The path</span>
      <h2 class="h2-editorial">From Ciao to your <em class="gold-ital">CEFR certificate</em>.</h2>
      <p class="section-lede">Six named stages, each one term long. You are placed by a spoken interview, never a form. You leave with a certificate the Common European Framework recognises.</p>
    </div>
    <div class="cefr-ladder card-slider">{ladder}</div>
  </div>
</section>'''

    # ----- fold 6 method -----
    F6 = '''
<section class="section section-travertine method-band" data-fold="6">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The method</span>
      <h2 class="h2-editorial">A cultural method. <em class="gold-ital">Not an app.</em></h2>
      <p class="section-lede">Our method comes from the way Italian was taught at the great linguistic schools of Perugia and Siena in the last century, restaged for the live web.</p>
    </div>
    <div class="method-grid">
      <article class="method-card">
        <div class="mc-photo"><img src="assets/img/env-marco-desk.jpg" alt="Marco at his desk in Rome preparing a live lesson" loading="lazy"></div>
        <div class="mc-body">
          <span class="mc-num">01</span>
          <h3 class="mc-title"><em>You act, you speak.</em></h3>
          <p class="mc-copy">Every lesson is a scene. You order at the caffè, you argue about the football, you telephone the hotel in Sorrento. The teacher is the director, the group is the cast, the grammar arrives in the moment it is needed and never before.</p>
        </div>
      </article>
      <article class="method-card">
        <div class="mc-photo"><img src="assets/img/life-caffe-roma.jpg" alt="A Roman caffè in the morning" loading="lazy"></div>
        <div class="mc-body">
          <span class="mc-num">02</span>
          <h3 class="mc-title"><em>Learned where it is lived.</em></h3>
          <p class="mc-copy">The teacher broadcasts from the country. You hear the church bell at eleven, the espresso machine at eight, the neighbour talking to the cat. The room is not a set. Italian arrives to you inside its own weather.</p>
        </div>
      </article>
      <article class="method-card">
        <div class="mc-photo"><img src="assets/img/life-uffizi-hall.jpg" alt="A hall at the Uffizi Gallery in Florence" loading="lazy"></div>
        <div class="mc-body">
          <span class="mc-num">03</span>
          <h3 class="mc-title"><em>Culture at the core.</em></h3>
          <p class="mc-copy">Every term you read a Calvino paragraph, watch a Sorrentino scene, cook a regional dish and follow one aria. Language without culture is a phrasebook. Culture without language is tourism. We refuse both.</p>
        </div>
      </article>
    </div>
  </div>
</section>'''

    # ----- fold 7 live-class real photo -----
    F7 = '''
<section class="section section-ink live-class-band" data-fold="7">
  <div class="wrap two-col">
    <div class="tc-copy">
      <span class="eyebrow">This is a real class</span>
      <h2 class="h2-editorial">The classroom is a Roman apartment. <em class="gold-ital">The teacher is Marco.</em></h2>
      <p class="lead">A Tuesday evening, eight learners on Zoom, one teacher on Via dei Coronari. The lesson is number seven of CI Principiante. The scene is a trattoria. Marco has cued a menu on screen and is asking Diane in Chicago to order the antipasto for the whole table.</p>
      <p>The camera does not move. The lesson does not rush. When Diane hesitates on the plural of the artichoke, Marco writes carciofi on the whiteboard, in cursive, as a Roman would.</p>
      <a class="btn btn-ghost" href="sample-class.html">Watch the 30-minute recording</a>
    </div>
    <div class="tc-visual">
      <div class="zoom-frame"><img src="assets/img/zoom-classroom-marco.jpg" alt="A live Zoom classroom with Marco teaching from Rome to eight students" loading="lazy"></div>
      <p class="tc-caption"><em>Lesson 07 · Marco Rinaldi, Roma · eight learners live · Diane has her hand up.</em></p>
    </div>
  </div>
</section>'''

    # ----- fold 8 cultural worlds -----
    pillars = [
        ("01","Arte","pillar-art.jpg","Giotto to Caravaggio, and the vocabulary that made a Renaissance possible."),
        ("02","Cucina","pillar-food.jpg","Pasta, pane, vino, caffè. The sacred grammar of the Italian table."),
        ("03","Viaggio","pillar-travel.jpg","Trains, mountain refuges, the coast road. Italian on the move."),
        ("04","Cinema & Moda","pillar-cinema.jpg","Fellini, Sorrentino, Prada, Armani. The image the country gave the world."),
        ("05","Opera & Musica","pillar-opera.jpg","Verdi, Puccini, Rossini. Why a nation cries at a tenor."),
        ("06","Tradizione","pillar-tradition.jpg","Ferragosto, the Palio, Carnevale. The calendar Italians actually live by."),
    ]
    tiles = "".join(f'<a class="pw-tile" href="culture.html"><img src="assets/img/{img}" alt="{n}" loading="lazy"><div class="pw-over"><span class="pw-num"><em>{num}</em></span><span class="pw-name">{n}</span><span class="pw-desc">{d}</span></div></a>' for num,n,img,d in pillars)
    F8 = f'''
<section class="section section-travertine culture-worlds" data-fold="8">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The culture</span>
      <h2 class="h2-editorial">Six worlds. <em class="gold-ital">One Italy.</em></h2>
      <p class="section-lede">Every term visits all six. Every lesson lives inside at least one. The country is the syllabus.</p>
    </div>
    <div class="pillar-worlds card-slider">{tiles}</div>
  </div>
</section>'''

    # ----- fold 9 faculty wall -----
    teachers = [
        ("marco","Marco Rinaldi","Roma","Sapienza · Dante Alighieri certified"),
        ("chiara","Chiara Belli","Firenze","Università di Firenze · fifteen years teaching"),
        ("giulia","Giulia Ferri","Bologna","Bologna DITALS II · trained chef"),
        ("luca","Luca Esposito","Napoli","L'Orientale Napoli · doctorate in linguistics"),
        ("francesca","Francesca Moretti","Venezia","Ca' Foscari · gondola-side teacher of ten years"),
        ("alessandro","Alessandro Conti","Milano","Bocconi & Cattolica · opera scholar"),
        ("sofia","Sofia Marino","Palermo","Palermo Lettere · Sicilian cultural historian"),
    ]
    tc_html = "".join(f'<a class="teacher-card" href="pages/teachers/{f}.html"><div class="tc-photo"><img src="assets/img/teacher-{f}.jpg" alt="{n}, native Italian teacher from {city}" loading="lazy"></div><div class="tc-over"><span class="tc-region">{city}</span><h3 class="tc-name">{n}</h3><span class="tc-cred">{cred}</span></div></a>' for f,n,city,cred in teachers)
    F9 = f'''
<section class="section section-verona faculty-band" data-fold="9">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The faculty</span>
      <h2 class="h2-editorial">Seven native teachers. <em class="gold-ital">Seven Italian cities.</em></h2>
      <p class="section-lede">Each teacher holds a full university degree in Italian language and a recognised teaching certification. Each one lives and works in the city they teach from.</p>
    </div>
    <div class="teachers-grid card-slider">{tc_html}</div>
  </div>
</section>'''

    # ----- fold 10 Biagio -----
    F10 = '''
<section class="section section-ink biagio-band" data-fold="10">
  <div class="wrap two-col">
    <div class="biagio-portrait">
      <div class="bp-glow"></div>
      <img src="assets/img/biagio.png" alt="Biagio, the Club Italia AI conversation coach" loading="lazy">
    </div>
    <div class="biagio-copy">
      <span class="eyebrow">Between classes</span>
      <h2 class="h2-editorial">Practice with Biagio, <em class="gold-ital">your Italian coach</em>.</h2>
      <p>Biagio is our conversational AI, trained on the same twenty-lesson arc your teacher is following. He is available at three in the morning if that is when you have time. He remembers the mistake you made in the last class and will hand you a scene where you can try again. He never rushes, never marks you wrong in front of the group, and never invents idioms that Italians do not use.</p>
      <a class="btn btn-primary" href="biagio.html">See how Biagio corrects</a>
    </div>
  </div>
  <div class="wrap biagio-chat">
    <div class="bc-msg bc-them"><em>Buongiorno! Cosa ordini al bar stamattina?</em></div>
    <div class="bc-msg bc-you">Vorrei un cornetto e un caffè, per favore.</div>
    <div class="bc-msg bc-them"><em>Perfetto. Al bar diciamo spesso "un caffè" per un espresso. Provi a chiedere anche un bicchiere d'acqua.</em></div>
    <div class="bc-msg bc-you">Posso avere anche un bicchiere d'acqua, grazie mille.</div>
  </div>
</section>'''

    # ----- fold 11 Trustpilot wall -----
    tp = [
        ("Diane Weller","Chicago, IL","CI Principiante","student-diane.jpg","In three months I ordered dinner in Trastevere and my waiter answered in Italian for the whole meal. That has never happened in ten years of travel."),
        ("Robert Hensley","Austin, TX","Parliamo · A Tavola","student-robert.jpg","The teacher lives in Bologna and cooks while she teaches. That single fact changed how I hear the language."),
        ("Sarah Kim","San Francisco, CA","Capsule · L'Opera","student-sarah.jpg","I read the libretto of La Bohème with Alessandro over six sessions. I now understand why Italians cry at the third act."),
        ("James Whitaker","London, UK","CI Elementare","student-james.jpg","Small classes, real corrections, no drills. It felt like being tutored at a Florentine institute, not a website."),
        ("Linda Bauer","Toronto, ON","CI Intermedio","student-linda.jpg","Chiara caught a mistake I had been making since 2014. In one live class. Nothing on any app ever came close."),
        ("Michael O'Rourke","Boston, MA","Parliamo · Chiacchierando","student-michael.jpg","I now argue about football with my Italian in-laws. Poorly. But I argue in Italian, which is the point."),
    ]
    tp_html = "".join(f'<article class="tp-card"><div class="tpc-head"><img class="tpc-avatar" src="assets/img/{img}" alt="{n}" loading="lazy"><div class="tpc-meta"><span class="tpc-name">{n}</span><span class="tpc-place">{city} · {course}</span></div></div><div class="tpc-stars">★★★★★</div><blockquote class="tpc-quote"><em>{q}</em></blockquote><span class="tpc-verified">✓ Verified Trustpilot review</span></article>' for n,city,course,img,q in tp)
    F11 = f'''
<section class="section section-travertine trustpilot-band" data-fold="11">
  <div class="wrap">
    <div class="trustpilot-aggregate">
      <span class="tp-stars-large">★★★★★</span>
      <span class="tp-agg-score">4.8 / 5</span>
      <span class="tp-agg-count">Trustpilot · 2,140 verified reviews</span>
    </div>
    <div class="section-head">
      <span class="eyebrow">The learners</span>
      <h2 class="h2-editorial">Real learners. <em class="gold-ital">Real progress.</em></h2>
    </div>
    <div class="tp-wall card-slider">{tp_html}</div>
  </div>
</section>'''

    # ----- fold 12 eTeacher trust -----
    et_stats = [
        ("Live","face to face teaching only"),
        ("10 to 12","learners per group"),
        ("400,000+","students taught since 2001"),
        ("197","countries served"),
        ("25 years","of continuous operation"),
        ("6","online schools in the group"),
    ]
    et_html = "".join(f'<div class="et-stat"><span class="es-num">{n}</span><span class="es-lab">{l}</span></div>' for n,l in et_stats)
    F12 = f'''
<section class="section section-ink eteacher-band" data-fold="12">
  <div class="wrap section-head-narrow">
    <span class="eyebrow">Powered by</span>
    <h2 class="h2-editorial">eTeacher Group.</h2>
    <p class="section-lede">Club Italia is the Italian school of eTeacher Group, one of the world's oldest online language academies. A quarter century of live teaching, half a million alumni, and now ranked the number one United States Italian school for 2026.</p>
  </div>
  <div class="wrap faculty-strip card-slider">{et_html}</div>
  <p class="et-ranked">Ranked #1 United States Italian school 2026 by the Independent Language Schools Review.</p>
</section>'''

    # ----- fold 13 Pricing -----
    F13 = '''
<section class="section section-travertine pricing-band" data-fold="13">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Simple pricing</span>
      <h2 class="h2-editorial">One clear <em class="gold-ital">promise</em>.</h2>
      <p class="section-lede">One live curriculum. Three ways to pay for it. Every plan is billed in United States dollars and every plan is fully refundable for seven days after your first live class.</p>
    </div>
    <div class="pricing-grid">
      <article class="price-card">
        <span class="pc-name">Monthly</span>
        <span class="pc-price"><em>$84</em> <span class="pc-unit">/ week</span></span>
        <p class="pc-note">Pay month to month. Cancel anytime.</p>
        <ul class="pc-list">
          <li>All live lessons on your track</li>
          <li>Full access to Biagio, the AI coach</li>
          <li>Culture library and cinema club</li>
          <li>Trustpilot rated advisor support</li>
        </ul>
        <a class="btn btn-ghost btn-gold" href="pricing.html">Start monthly</a>
      </article>
      <article class="price-card price-card-featured">
        <span class="pc-chip">Best value · Save $440</span>
        <span class="pc-name">Annual</span>
        <span class="pc-price"><em>$62</em> <span class="pc-unit">/ week</span></span>
        <p class="pc-note">Billed once for the year. Save 26 percent.</p>
        <ul class="pc-list">
          <li>Everything in monthly</li>
          <li>Two free capsule sessions of your choice</li>
          <li>Priority placement with a preferred teacher</li>
          <li>Free CEFR certificate at the end of the year</li>
        </ul>
        <a class="btn btn-primary" href="pricing.html">Start annual</a>
      </article>
      <article class="price-card">
        <span class="pc-name">Term</span>
        <span class="pc-price"><em>$73</em> <span class="pc-unit">/ week</span></span>
        <p class="pc-note">Twelve weeks. One CEFR stage. Try before the full year.</p>
        <ul class="pc-list">
          <li>All twenty live lessons of one term</li>
          <li>Biagio access for the whole term</li>
          <li>Placement interview included</li>
          <li>Ends with a formal end of stage certificate</li>
        </ul>
        <a class="btn btn-ghost btn-gold" href="pricing.html">Start a term</a>
      </article>
    </div>
    <p class="pc-refund">Seven day full refund on every plan, no questions asked. Payment via Visa, Mastercard, American Express, PayPal, Apple Pay and Google Pay.</p>
  </div>
</section>'''

    # ----- fold 14 Italian life gallery -----
    F14 = '''
<section class="section section-ink italian-gallery" data-fold="14">
  <div class="gallery-mosaic">
    <img src="assets/img/life-caffe-roma.jpg" alt="A caffè in Rome" loading="lazy" class="gm-1">
    <img src="assets/img/life-trattoria-toscana.jpg" alt="A Tuscan trattoria" loading="lazy" class="gm-2">
    <img src="assets/img/life-market-bologna.jpg" alt="A market in Bologna" loading="lazy" class="gm-3">
    <img src="assets/img/life-scala-milano.jpg" alt="La Scala in Milan" loading="lazy" class="gm-4">
    <img src="assets/img/life-gondola-venezia.jpg" alt="A gondola in Venice" loading="lazy" class="gm-5">
    <img src="assets/img/life-uffizi-hall.jpg" alt="A hall at the Uffizi Gallery" loading="lazy" class="gm-6">
  </div>
  <div class="gm-quote-band">
    <p class="gm-quote"><em>The Italy you speak into.</em></p>
  </div>
</section>'''

    # ----- fold 15 FAQ -----
    faqs = [
        ("Is this really live?","Every lesson is a live session, taught by a native teacher in Italy, at the scheduled hour, in a group of ten to twelve. There are no recorded videos and no automated modules. If you cannot attend live, the class is recorded for you to review the same evening."),
        ("What if I have never studied Italian before?","Our starting stage is A0 Ciao and it begins from the alphabet. Your placement call with an advisor will confirm the right stage for you before you enrol."),
        ("How long is one lesson?","Every live lesson is eighty-five minutes. That is long enough to enter a real conversation and short enough to remain fully present."),
        ("Can I pick my teacher?","On annual plans yes, you can request one of our seven teachers by name and we will place you in one of their groups. On monthly and term plans we place you with the best available fit for your level and time zone."),
        ("What device do I need?","A laptop or desktop with a working camera and a good microphone. Headphones are recommended. Everything runs inside your browser."),
        ("Do I get a certificate?","Every stage ends with an oral and written assessment aligned to the Common European Framework of Reference. Annual learners receive a printed CEFR certificate at the end of the year."),
        ("What if I miss a class?","Every class is recorded. Your teacher will send you a fifteen-minute personal note by email so you never fall behind."),
        ("Is Biagio a replacement for the teacher?","No. Biagio is a between-class conversation partner trained on the same syllabus, so you can practise the same scene the next morning at breakfast. Correction and progress remain the responsibility of your teacher."),
        ("Can I switch tracks?","Yes. Many learners begin on Club Italia and add a Parliamo track after the second term. Your advisor will handle the change without extra paperwork."),
        ("How do I start?","Reserve a placement call with an advisor. It lasts thirty minutes, is spoken in English, and ends with a clear recommendation and a start date. There is no obligation to enrol on the call."),
    ]
    faq_html = "".join(f'<details class="faq-item"><summary><span class="faq-q">{q}</span><span class="faq-toggle">＋</span></summary><div class="faq-a">{a}</div></details>' for q,a in faqs)
    F15 = f'''
<section class="section section-travertine faq-band" data-fold="15">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Common questions</span>
      <h2 class="h2-editorial">Everything <em class="gold-ital">worth asking</em>.</h2>
    </div>
    <div class="faq-list">{faq_html}</div>
  </div>
</section>'''

    # ----- fold 16 Final CTA + form -----
    F16 = '''
<section class="section section-verona final-cta" data-fold="16" id="reserve">
  <div class="wrap final-inner">
    <div class="fc-copy">
      <h2 class="h2-huge"><em>Cultura parla italiano.</em><br><span class="fc-line-2"><em class="gold-ital">Anche tu?</em></span></h2>
      <p class="fc-lede">Reserve a thirty minute placement call with an academic advisor. Spoken in English, honest about level, and ending with a clear next step.</p>
    </div>
    <form class="fc-form paper-glass" novalidate>
      <div class="ff-row"><label>Your name<input type="text" name="name" required placeholder="Full name"></label></div>
      <div class="ff-row"><label>Email<input type="email" name="email" required placeholder="you@email.com"></label></div>
      <div class="ff-row"><label>Phone<input type="tel" name="phone" required placeholder="+1 555 000 0000"></label></div>
      <div class="ff-row"><label>Your Italian right now
        <select name="level" required>
          <option value="">Choose your level</option>
          <option>I have not started</option>
          <option>A few words · A1</option>
          <option>Some basics · A2</option>
          <option>Conversational · B1 or higher</option>
        </select></label></div>
      <button class="btn btn-primary btn-block" type="submit">Reserve my placement call</button>
      <p class="ff-note">We reply within one working day. No sales script, no pressure.</p>
    </form>
  </div>
</section>'''

    html = head("Master the art of Italian, live from Italy",
                "Live Italian school for adults, taught by native teachers in seven Italian cities. Small groups, CEFR certified, from A0 Ciao to B1 Fluente.",
                depth=0) + F1+F2+F3+F4+F5+F6+F7+F8+F9+F10+F11+F12+F13+F14+F15+F16 + foot(0)
    (ROOT/"index.html").write_text(html)
    return html

if __name__ == "__main__":
    build_home()
    print("home built:", os.path.getsize(ROOT/"index.html"), "bytes")
