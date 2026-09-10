#!/usr/bin/env python3
"""Build courses.html and capsules.html with editorial depth."""
import json, os, html

ROOT = "/home/user/workspace/club-italia"
DATA = json.load(open(f"{ROOT}/research/course-data.json"))

def esc(s): return html.escape(str(s), quote=True)

NAV = """<header class="site-header">
  <div class="wrap nav">
    <a class="nav-logo" href="index.html" aria-label="Club Italia — home">
      <span class="logo-text"><span class="lt-main">Club Italia</span><span class="lt-sub">by eTeacher</span></span>
    </a>
    <nav class="nav-menu" aria-label="Primary">
      <span class="nav-item"><a class="nav-link" href="courses.html">Courses</a></span>
      <span class="nav-item"><a class="nav-link" href="how-it-works.html">How It Works</a></span>
      <span class="nav-item"><a class="nav-link" href="method.html">Method</a></span>
      <span class="nav-item"><a class="nav-link" href="teachers.html">Teachers</a></span>
      <span class="nav-item"><a class="nav-link" href="culture.html">Culture</a></span>
      <span class="nav-item"><a class="nav-link" href="biagio.html">AI Tutor</a></span>
      <span class="nav-item"><a class="nav-link" href="pricing.html">Pricing</a></span>
      <span class="nav-item"><a class="nav-link" href="blog.html">Blog</a></span>
    </nav>
    <button class="btn btn-3d btn-3d-primary nav-cta" data-advisor type="button">Talk to an Advisor</button>
    <button class="nav-toggle" aria-label="Open menu" aria-controls="navDrawer" type="button">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
<aside class="nav-drawer" id="navDrawer" aria-label="Mobile menu">
  <button class="nav-drawer-close" aria-label="Close menu" type="button">&times;</button>
  <a href="courses.html">Courses</a>
  <a href="how-it-works.html">How It Works</a>
  <a href="method.html">Method</a>
  <a href="teachers.html">Teachers</a>
  <a href="culture.html">Culture</a>
  <a href="capsules.html">Culture Capsules</a>
  <a href="biagio.html">AI Tutor</a>
  <a href="pricing.html">Pricing</a>
  <a href="blog.html">Blog</a>
  <a href="faq.html">FAQ</a>
  <a href="about.html">About</a>
  <a href="contact.html">Contact</a>
  <button class="btn btn-3d btn-3d-primary" data-advisor type="button" style="width:100%;margin-top:1.6rem">Talk to an Advisor</button>
</aside>"""

FOOTER = """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="logo-text" style="margin-bottom:1rem"><span class="lt-main" style="color:var(--on-dark)">Club Italia</span><span class="lt-sub">by eTeacher</span></div>
        <p>Live Italian, taught inside Italian cities. Small groups, master teachers, lifetime recordings. Certified by eTeacher Group.</p>
      </div>
      <div class="footer-col">
        <h4>Courses</h4>
        <a href="pages/courses/ci1.html">CI Principiante</a>
        <a href="pages/courses/ci2.html">CI Elementare</a>
        <a href="pages/courses/ci3.html">CI Intermedio</a>
        <a href="pages/courses/ci4.html">CI Avanzato</a>
        <a href="courses.html">All Courses</a>
      </div>
      <div class="footer-col">
        <h4>Spoken &amp; Capsules</h4>
        <a href="pages/spoken/ps1.html">Al Caffè</a>
        <a href="pages/spoken/ps2.html">A Tavola</a>
        <a href="pages/spoken/ps3.html">In Viaggio</a>
        <a href="pages/spoken/ps4.html">Chiacchierando</a>
        <a href="capsules.html">Culture Capsules</a>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <a href="about.html">About</a>
        <a href="method.html">Method</a>
        <a href="pricing.html">Pricing</a>
        <a href="faq.html">FAQ</a>
        <a href="contact.html">Contact</a>
        <a href="terms.html">Terms</a>
        <a href="privacy.html">Privacy</a>
      </div>
    </div>
    <div class="footer-bottom"><p>Presented by eTeacher Group &nbsp;·&nbsp; advisor@clubitalia.com &nbsp;·&nbsp; +1-888-230-5110</p></div>
    <p style="color:var(--on-dark-faint);font-size:.78rem;text-align:center;margin-top:1.6rem">Copyright eTeacher Group © 2026. All Rights Reserved.</p>
  </div>
</footer>"""

ADVISOR = """<div class="advisor-modal" id="advisorModal" role="dialog" aria-modal="true" aria-labelledby="advisorTitle">
  <div class="advisor-card">
    <button class="advisor-modal-close" aria-label="Close" type="button">&times;</button>
    <div class="advisor-head">
      <p class="eyebrow eyebrow-line" style="justify-content:center">Placement conversation</p>
      <h3 id="advisorTitle">Speak to a Club Italia advisor</h3>
      <p>A 15-minute conversation to place you in the right level and answer everything about the course.</p>
    </div>
    <form class="advisor-form" novalidate>
      <div class="field"><label for="af-name">Your name</label><input id="af-name" name="name" required><span class="err-msg"></span></div>
      <div class="field"><label for="af-email">Email</label><input id="af-email" name="email" type="email" required><span class="err-msg"></span></div>
      <div class="field"><label for="af-phone">Phone (optional)</label><input id="af-phone" name="phone" type="tel"></div>
      <div class="field"><label for="af-level">Current Italian level</label><select id="af-level" name="level"><option>Complete beginner</option><option>A1 · basics</option><option>A2 · confident</option><option>B1 or higher</option></select></div>
      <button class="btn btn-3d btn-3d-primary" type="submit">Reserve My Placement Call</button>
    </form>
    <div class="advisor-success"><h3>Grazie mille.</h3><p>An advisor will call within one business day.</p></div>
  </div>
</div>"""

# Page-local styles used by indexes
IDX_STYLE = """<style>
.hero-badges{display:flex;gap:.55rem;flex-wrap:wrap;margin-bottom:1.6rem}
.h-badge{display:inline-flex;align-items:center;gap:.5rem;padding:.4rem .8rem;border:1px solid var(--gold-line);color:var(--on-dark);font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;border-radius:2px;background:rgba(34,8,11,.35);backdrop-filter:blur(6px)}
.h-badge.lvl{background:rgba(201,162,75,.14);color:var(--gold-soft);border-color:var(--gold-soft)}
.sec-head{max-width:820px;margin:0 auto 3.4rem;text-align:center}
.sec-head h2{margin:.6rem 0 1rem}
.sec-head p{margin:0 auto;color:var(--on-light-soft)}
.on-dark .sec-head p{color:var(--on-dark-soft)}
.gold-rule{border:0;height:1px;background:var(--gold);opacity:.7;width:60px;margin:1.6rem auto 0}
/* Big track intro */
.track-intro{display:grid;grid-template-columns:.9fr 1.1fr;gap:4rem;align-items:center;margin-bottom:3.4rem}
@media (max-width:900px){.track-intro{grid-template-columns:1fr;gap:2rem}}
.track-intro .ti-eyebrow{font-family:var(--serif);font-style:italic;color:var(--gold-deep);font-size:1.15rem;margin-bottom:.6rem}
.track-intro h2{font-size:clamp(2.4rem,4.4vw,4rem);line-height:1.04;margin-bottom:1.4rem}
.track-intro p{font-size:1.06rem;line-height:1.7;color:var(--on-light-soft)}
/* Course grid — big card 2-col */
.big-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1.6rem}
@media (max-width:820px){.big-grid{grid-template-columns:1fr}}
.big-card{position:relative;display:grid;grid-template-rows:auto 1fr;background:var(--white);border:1px solid var(--gold-line-soft);overflow:hidden;transition:transform .3s var(--ease),box-shadow .3s var(--ease)}
.big-card:hover{transform:translateY(-4px);box-shadow:0 18px 44px rgba(58,14,18,.14)}
.big-card .bc-hero{position:relative;aspect-ratio:16/9;overflow:hidden}
.big-card .bc-hero img{width:100%;height:100%;object-fit:cover;transition:transform .8s var(--ease)}
.big-card:hover .bc-hero img{transform:scale(1.05)}
.big-card .bc-hero .overlay{position:absolute;inset:0;background:linear-gradient(180deg,transparent 40%,rgba(34,8,11,.85));display:flex;align-items:flex-end;justify-content:space-between;padding:1.2rem 1.6rem}
.big-card .bc-code{font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-soft);background:rgba(34,8,11,.55);padding:.4rem .8rem;border:1px solid var(--gold-line)}
.big-card .bc-cefr{font-family:var(--serif);font-style:italic;color:var(--gold-soft);font-size:1.1rem}
.big-card .bc-body{padding:1.8rem 1.8rem 2rem;display:flex;flex-direction:column;gap:.7rem}
.big-card .bc-tag{font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-deep)}
.big-card .bc-title{font-family:var(--serif);font-size:1.85rem;line-height:1.1;color:var(--on-light)}
.big-card .bc-city{font-family:var(--serif);font-style:italic;color:var(--terra-deep);font-size:1rem}
.big-card .bc-promise{font-size:.98rem;line-height:1.55;color:var(--on-light-soft);margin:.4rem 0}
.big-card .bc-meta{display:flex;gap:1rem;font-size:.78rem;color:var(--on-light-faint);letter-spacing:.06em;padding-top:.6rem;border-top:1px solid var(--light-line)}
.big-card .bc-cta{margin-top:.8rem;display:inline-flex;align-items:center;gap:.5rem;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-deep);font-weight:600}
.big-card .bc-cta::after{content:"→";transition:transform .3s var(--ease)}
.big-card:hover .bc-cta::after{transform:translateX(6px)}
/* Level ladder */
.ladder{display:grid;grid-template-columns:repeat(4,1fr);gap:1.2rem;margin:3rem 0}
@media (max-width:900px){.ladder{grid-template-columns:repeat(2,1fr)}}
@media (max-width:520px){.ladder{grid-template-columns:1fr}}
.ladder-step{padding:1.6rem 1.4rem;background:var(--ivory);border:1px solid var(--gold-line-soft);text-align:center}
.ladder-step .ls-cefr{font-family:var(--serif);font-style:italic;color:var(--gold-deep);font-size:1.3rem}
.ladder-step .ls-name{font-family:var(--serif);font-size:1.3rem;margin:.3rem 0}
.ladder-step .ls-city{font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-deep)}
/* Capsule editorial band */
.cap-band{display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center;margin-top:3rem}
@media (max-width:900px){.cap-band{grid-template-columns:1fr}}
.cap-band .cbi img{width:100%;aspect-ratio:4/3;object-fit:cover;border:1px solid var(--gold-line-soft)}
.cap-band .cbt h3{font-family:var(--serif);font-size:2rem;line-height:1.1;margin-bottom:.6rem}
.cap-band .cbt .cbt-italian{font-family:var(--serif);font-style:italic;color:var(--gold-deep);font-size:1.15rem;margin-bottom:.8rem}
.cap-band .cbt p{color:var(--on-light-soft);line-height:1.7;font-size:1rem;margin-bottom:.6rem}
.cap-band.reverse .cbi{order:2}
@media (max-width:900px){.cap-band.reverse .cbi{order:0}}
.hero-meta-strip{display:grid;grid-template-columns:repeat(4,1fr);gap:1.4rem;margin-top:3rem;padding-top:2rem;border-top:1px solid var(--gold-line-soft);max-width:820px}
.hero-meta-strip .hm-k{font-size:.66rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold-soft);margin-bottom:.4rem}
.hero-meta-strip .hm-v{font-family:var(--serif);font-size:1.15rem;color:var(--on-dark)}
@media (max-width:820px){.hero-meta-strip{grid-template-columns:repeat(2,1fr);gap:1rem}}
.final-cta{text-align:center;padding:clamp(5rem,9vw,9rem) 0}
.final-cta h2{font-size:clamp(2.6rem,5vw,4.4rem);line-height:1.05;margin-bottom:1.4rem;color:var(--on-dark)}
.final-cta p{max-width:52ch;margin:0 auto 2.4rem;color:var(--on-dark-soft);font-size:1.15rem}
.final-cta .hero-ctas{justify-content:center}
</style>"""


def big_card(slug, folder, code):
    d = DATA[slug]
    img = d.get('hero_image', '').replace('assets/img/', '')
    if not img:
        img = f"{slug}.jpg"
    return f"""<a class="big-card" href="pages/{folder}/{slug}.html">
      <div class="bc-hero">
        <img src="assets/img/{img}" alt="{esc(d['title'])} — {esc(d['city'])}">
        <div class="overlay">
          <span class="bc-code">{esc(code)}</span>
          <span class="bc-cefr">{esc(d['cefr'])}</span>
        </div>
      </div>
      <div class="bc-body">
        <span class="bc-tag">{esc(d['tag'])}</span>
        <h3 class="bc-title">{esc(d['title'])}</h3>
        <p class="bc-city">Set in {esc(d['city'])}</p>
        <p class="bc-promise">{esc(d['promise'][:200])}{'…' if len(d['promise'])>200 else ''}</p>
        <div class="bc-meta"><span>{esc(d['hours'])}</span><span>·</span><span>10–12 learners</span></div>
        <span class="bc-cta">Explore the course</span>
      </div>
    </a>"""


def build_courses_html():
    ci_cards = "".join(big_card(s, "courses", f"CI · 0{i+1}") for i, s in enumerate(['ci1','ci2','ci3','ci4']))
    ps_cards = "".join(big_card(s, "spoken", f"PS · 0{i+1}") for i, s in enumerate(['ps1','ps2','ps3','ps4']))
    cap_cards = "".join(big_card(s, "culture", f"CAP · 0{i+1}") for i, s in enumerate(['cap-food','cap-art','cap-opera']))
    ladder = ""
    for s, name, cfr, city in [
        ("ci1","Principiante","A0 → A1.1","Roma"),
        ("ci2","Elementare","A1.1 → A1.2","Firenze"),
        ("ci3","Intermedio","A1.2 → A2.1","Bologna"),
        ("ci4","Avanzato","A2.1 → A2.2","Napoli · Milano"),
    ]:
        ladder += f"""<a class="ladder-step" href="pages/courses/{s}.html"><div class="ls-cefr">{esc(cfr)}</div><div class="ls-name">{esc(name)}</div><div class="ls-city">{esc(city)}</div></a>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>All Courses &mdash; Club Italia by eTeacher</title>
<meta name="description" content="Eleven live Italian courses, taught inside Italian cities. Four structured CEFR levels, four spoken conversation courses, three cultural capsules.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="css/ci.css">
{IDX_STYLE}
</head>
<body>
{NAV}

<section class="hero" style="min-height:74vh">
  <div class="hero-bg"><img src="assets/img/hero-poster.jpg" alt="Live Italian, live from Italy"></div>
  <div class="hero-content">
    <div style="max-width:820px">
      <div class="hero-badges">
        <span class="h-badge lvl">11 live courses</span>
        <span class="h-badge"><span class="live-dot"></span>Live from Italia</span>
        <span class="h-badge">Certified by eTeacher</span>
      </div>
      <p class="hero-tag">The Courses</p>
      <h1>Eleven ways to arrive in <span class="gold-ital">Italiano</span></h1>
      <p class="hero-sub">Four structured CEFR levels from A0 to A2.2. Four spoken-only conversation courses. Three cultural capsules. Every one of them taught live from an Italian city by a master Italian teacher.</p>
      <div class="hero-ctas">
        <button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button>
        <a class="btn btn-3d btn-3d-ghost" href="#structured">Explore the tracks</a>
      </div>
      <div class="hero-meta-strip">
        <div class="hm"><div class="hm-k">Structured</div><div class="hm-v">4 CEFR levels</div></div>
        <div class="hm"><div class="hm-k">Spoken</div><div class="hm-v">4 conversation courses</div></div>
        <div class="hm"><div class="hm-k">Capsules</div><div class="hm-v">3 culture short courses</div></div>
        <div class="hm"><div class="hm-k">Cities</div><div class="hm-v">Roma · Firenze · Bologna · Napoli · Milano</div></div>
      </div>
    </div>
  </div>
</section>

<section class="section-cream" id="structured">
  <div class="wrap">
    <div class="track-intro">
      <div>
        <p class="eyebrow eyebrow-line">Track one</p>
        <p class="ti-eyebrow">Club Italia · Structured</p>
        <h2>Four levels, four <span class="gold-ital">cities</span>, one Italian.</h2>
      </div>
      <div>
        <p>The CI track takes you from A0 to A2.2 across four Italian cities. Rome for the beginning, Florence for the sentence, Bologna for the argument, Naples and Milan together for the last mile. Each level is twenty live lessons with one master teacher who stays with you throughout.</p>
      </div>
    </div>
    <div class="ladder">{ladder}</div>
    <div class="big-grid">{ci_cards}</div>
  </div>
</section>

<section class="section-paper">
  <div class="wrap">
    <div class="track-intro">
      <div>
        <p class="eyebrow eyebrow-line">Track two</p>
        <p class="ti-eyebrow">Parlato · Spoken Italian</p>
        <h2>Four courses. <span class="gold-ital">No textbook.</span></h2>
      </div>
      <div>
        <p>The PS track is for the learner who wants Italian in the mouth, not on the page. Cafés, tables, journeys, and confident conversation — four twenty-session courses, each set inside the real Italian rooms where the language is spoken loudest.</p>
      </div>
    </div>
    <div class="big-grid">{ps_cards}</div>
  </div>
</section>

<section class="section-dark" style="background:linear-gradient(180deg,var(--navy) 0%,var(--navy-deep) 100%)">
  <div class="wrap">
    <div class="track-intro">
      <div>
        <p class="eyebrow eyebrow-line" style="color:var(--gold-soft)">Track three</p>
        <p class="ti-eyebrow" style="color:var(--gold-soft)">Culture Capsules</p>
        <h2 style="color:var(--on-dark)">Six sessions. <span class="gold-ital">One obsession.</span></h2>
      </div>
      <div>
        <p style="color:var(--on-dark-soft)">Our short cultural courses. Six sessions apiece on the Italian of the table, the Italian of the museum, and the Italian of the opera house. Designed for any learner at any level, hosted by the specialists who love the subject most.</p>
      </div>
    </div>
    <div class="big-grid">{cap_cards}</div>
  </div>
</section>

<section class="section-dark final-cta" style="background:linear-gradient(180deg,var(--navy-deep) 0%,var(--navy) 100%)">
  <div class="wrap-narrow">
    <p class="eyebrow eyebrow-line" style="justify-content:center">Live Italian. Live.</p>
    <h2>Not sure where to <span class="gold-ital">begin</span>?</h2>
    <p>A 15-minute placement conversation with a Club Italia advisor. We place you in the right course, at the right level, with the right teacher.</p>
    <div class="hero-ctas">
      <button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button>
      <a class="btn btn-3d btn-3d-ghost" href="how-it-works.html">See how it works</a>
    </div>
  </div>
</section>

{FOOTER}
{ADVISOR}
<script src="js/ci.js" defer></script>
</body>
</html>
"""


def build_capsules_html():
    caps = [
        ("cap-food", "La Cucina", "The Italian of the Table", "cap-food.jpg",
         "Six live sessions on the vocabulary and history of the Italian table. Pasta, pane, vino, caffè — the language before the menu.",
         [("Weeks 1-2","Le Regioni — the north-south axis of Italian cuisine."),
          ("Weeks 3-4","La Pasta — four hundred shapes and the rules that govern them."),
          ("Week 5","Il Vino — the vocabulary of Italian wine."),
          ("Week 6","Il Pranzo della Domenica — a full Sunday lunch, in real time, in Italian.")],
         "Hosted by Giulia Bianchi · Cordon Bleu Firenze"),
        ("cap-art", "L'Arte", "Renaissance in the Words That Made It", "cap-art.jpg",
         "Six live sessions on the Italian language of art history — from Giotto to Caravaggio — filmed inside the museums and churches where these paintings live.",
         [("Weeks 1-2","Il Trecento e il Quattrocento — Giotto, Masaccio, the birth of perspective."),
          ("Weeks 3-4","Il Cinquecento — Leonardo, Michelangelo, Raphael."),
          ("Week 5","Il Barocco — Caravaggio and the drama of light."),
          ("Week 6","Al Museo — a real museum visit, in real time.")],
         "Hosted by Alessandro Fiorini · former Accademia della Crusca researcher"),
        ("cap-opera", "L'Opera", "Opera as a Second Language", "cap-opera.jpg",
         "Six live sessions on Verdi, Puccini and Rossini. Read a libretto, follow an aria, and understand why Italian was the language opera was invented in.",
         [("Weeks 1-2","Verdi — Rigoletto and La Traviata."),
          ("Weeks 3-4","Puccini — La Bohème and Turandot."),
          ("Week 5","Rossini — Il Barbiere di Siviglia."),
          ("Week 6","Alla Scala — a filmed visit to Milan's opera house.")],
         "Hosted by Sofia Marchetti · former RAI opera correspondent"),
    ]
    bands = ""
    for i, (slug, name, sub, img, promise, rhythm, host) in enumerate(caps):
        reverse = "reverse" if i % 2 == 1 else ""
        rh = "".join(f"<li><strong style='font-family:var(--serif);color:var(--gold-deep);font-size:1rem'>{esc(w)}.</strong> {esc(txt)}</li>" for w, txt in rhythm)
        bands += f"""<div class="cap-band {reverse}">
  <div class="cbi"><img src="assets/img/{img}" alt="{esc(name)}"></div>
  <div class="cbt">
    <p class="eyebrow eyebrow-line">Capsule · 0{i+1}</p>
    <p class="cbt-italian">{esc(name)}</p>
    <h3>{esc(sub)}</h3>
    <p>{esc(promise)}</p>
    <ul style="margin:1.4rem 0 1.6rem;padding-left:0;list-style:none;display:grid;gap:.5rem">{rh}</ul>
    <p style="font-size:.86rem;color:var(--on-light-faint);letter-spacing:.02em;margin-bottom:1.4rem"><em>{esc(host)}</em></p>
    <a class="btn btn-3d btn-3d-primary" href="pages/culture/{slug}.html">Explore the Capsule</a>
  </div>
</div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Culture Capsules &mdash; Club Italia by eTeacher</title>
<meta name="description" content="Three six-session culture capsules on the Italian of the table, the museum, and the opera house. Hosted by specialists. Live from Italy.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="css/ci.css">
{IDX_STYLE}
</head>
<body>
{NAV}

<section class="hero" style="min-height:70vh">
  <div class="hero-bg"><img src="assets/img/culture.jpg" alt="Culture Capsules — the Italian of food, art, and opera"></div>
  <div class="hero-content">
    <div style="max-width:820px">
      <div class="hero-badges">
        <span class="h-badge lvl">3 short courses</span>
        <span class="h-badge"><span class="live-dot"></span>Any level</span>
        <span class="h-badge">6 sessions each</span>
      </div>
      <p class="hero-tag">Culture Capsules</p>
      <h1>The Italian of <span class="gold-ital">food, art, and opera</span></h1>
      <p class="hero-sub">Three short, dense, cultural courses. Six live sessions apiece, hosted by the specialists who love the subject most. Designed for any Italian learner at any level.</p>
      <div class="hero-ctas">
        <button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button>
        <a class="btn btn-3d btn-3d-ghost" href="#capsules">Explore the capsules</a>
      </div>
    </div>
  </div>
</section>

<section class="section-paper" id="capsules">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow eyebrow-line" style="justify-content:center">The three capsules</p>
      <h2 class="display-lg">Small courses, <span class="gold-ital">deep</span> culture</h2>
      <p>Each capsule is six live sessions of 85 minutes. Held every Tuesday evening for six weeks. Any level welcome. Every session recorded for life.</p>
      <hr class="gold-rule">
    </div>
    {bands}
  </div>
</section>

<section class="section-dark final-cta" style="background:linear-gradient(180deg,var(--navy) 0%,var(--navy-deep) 100%)">
  <div class="wrap-narrow">
    <p class="eyebrow eyebrow-line" style="justify-content:center">A short course. A whole culture.</p>
    <h2>Six sessions. One <span class="gold-ital">obsession</span>.</h2>
    <p>Take one capsule, take all three. Each stands alone; together they are a small education in the culture of Italian.</p>
    <div class="hero-ctas">
      <button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button>
      <a class="btn btn-3d btn-3d-ghost" href="courses.html">See All Courses</a>
    </div>
  </div>
</section>

{FOOTER}
{ADVISOR}
<script src="js/ci.js" defer></script>
</body>
</html>
"""

def main():
    with open(f"{ROOT}/courses.html", "w", encoding="utf-8") as f:
        f.write(build_courses_html())
    print("wrote", f"{ROOT}/courses.html")
    with open(f"{ROOT}/capsules.html", "w", encoding="utf-8") as f:
        f.write(build_capsules_html())
    print("wrote", f"{ROOT}/capsules.html")

if __name__ == "__main__":
    main()
