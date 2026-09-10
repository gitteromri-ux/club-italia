#!/usr/bin/env python3
"""Club Italia — remaining root pages."""
from pathlib import Path
import re
ROOT = Path("/home/user/workspace/club-italia")
NAV = open(ROOT/"_partials/nav.html").read()
FOOTER = open(ROOT/"_partials/footer.html").read()

def page(title, desc, body, rel=""):
    nav, footer = NAV, FOOTER
    if rel:
        def prefix(m):
            attr, val = m.group(1), m.group(2)
            if val.startswith(('http','#','mailto:','tel:','/', rel)): return m.group(0)
            return f'{attr}="{rel}{val}"'
        nav = re.sub(r'(href|src)="([^"]+)"', prefix, nav)
        footer = re.sub(r'(href|src)="([^"]+)"', prefix, footer)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{rel}css/ci.css"></head><body>
{nav}
{body}
{footer}
<script src="{rel}js/ci.js"></script></body></html>
"""

# ---------- COURSES INDEX ----------
courses_body = """
<section class="hero" style="min-height:70vh">
  <div class="hero-bg"><img src="assets/img/hero-poster.jpg" alt="All Club Italia courses"></div>
  <div class="hero-content"><div style="max-width:64ch">
    <p class="hero-tag">Eleven courses · one Italy</p>
    <h1>All <span class="gold-ital">Courses</span></h1>
    <p class="hero-sub">Four structured CEFR courses. Four spoken conversation courses. Three cultural capsules. Every course is live, small-group, and broadcast from Italy.</p>
  </div></div>
</section>

<section class="section-paper"><div class="wrap">
<div class="section-head reveal"><span class="eyebrow eyebrow-line">Structured Mastery</span><h2 class="display-md">Club Italia — Il Corso · Four Levels A0 → A2.2</h2></div>
<div class="course-grid">
  <a class="course-card reveal" href="pages/courses/ci1.html"><div class="cc-hero"><img src="assets/img/course-ci1.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">A0 → A1.1</span><span class="cc-num">CI · 01</span></div></div><div class="cc-body"><span class="cc-track">Foundation · Roma</span><h3 class="cc-title">CI Principiante</h3><p class="cc-desc">Your first Italian — sounds, greetings, ordering caffè. Set in Rome.</p><div class="cc-cta"><span class="cc-price">$1,240<small>full course</small></span><span class="cc-arrow">›</span></div></div></a>
  <a class="course-card reveal reveal-d1" href="pages/courses/ci2.html"><div class="cc-hero"><img src="assets/img/course-ci2.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">A1.1 → A1.2</span><span class="cc-num">CI · 02</span></div></div><div class="cc-body"><span class="cc-track">Elementare · Firenze</span><h3 class="cc-title">CI Elementare</h3><p class="cc-desc">Everyday exchanges from Florence, cradle of the Italian language.</p><div class="cc-cta"><span class="cc-price">$1,240<small>full course</small></span><span class="cc-arrow">›</span></div></div></a>
  <a class="course-card reveal reveal-d2" href="pages/courses/ci3.html"><div class="cc-hero"><img src="assets/img/course-ci3.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">A1.2 → A2.1</span><span class="cc-num">CI · 03</span></div></div><div class="cc-body"><span class="cc-track">Intermedio · Bologna</span><h3 class="cc-title">CI Intermedio</h3><p class="cc-desc">Past and future tenses, real context. Set in Bologna.</p><div class="cc-cta"><span class="cc-price">$1,240<small>full course</small></span><span class="cc-arrow">›</span></div></div></a>
  <a class="course-card reveal reveal-d3" href="pages/courses/ci4.html"><div class="cc-hero"><img src="assets/img/course-ci4.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">A2.1 → A2.2</span><span class="cc-num">CI · 04</span></div></div><div class="cc-body"><span class="cc-track">Avanzato · Napoli & Milano</span><h3 class="cc-title">CI Avanzato</h3><p class="cc-desc">Confident conversation between the warmth of Naples and the sharpness of Milan.</p><div class="cc-cta"><span class="cc-price">$1,240<small>full course</small></span><span class="cc-arrow">›</span></div></div></a>
</div>
</div></section>

<section class="section-cream"><div class="wrap">
<div class="section-head reveal"><span class="eyebrow eyebrow-line">Spoken · Conversation</span><h2 class="display-md">Parliamo Italiano — Four Courses in Spoken Fluency</h2></div>
<div class="course-grid">
  <a class="course-card reveal" href="pages/spoken/ps1.html"><div class="cc-hero"><img src="assets/img/spoken-ps1.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">Foundation</span><span class="cc-num">PS · 01</span></div></div><div class="cc-body"><span class="cc-track">Parliamo · Foundation</span><h3 class="cc-title">Al Caffè</h3><p class="cc-desc">Twenty conversations that happen at an Italian café.</p><div class="cc-cta"><span class="cc-price">$1,240<small>full course</small></span><span class="cc-arrow">›</span></div></div></a>
  <a class="course-card reveal reveal-d1" href="pages/spoken/ps2.html"><div class="cc-hero"><img src="assets/img/spoken-ps2.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">Beginner</span><span class="cc-num">PS · 02</span></div></div><div class="cc-body"><span class="cc-track">Parliamo · Beginner</span><h3 class="cc-title">A Tavola</h3><p class="cc-desc">Speak Italian at the table. Order, argue politely, and understand a Tuscan grandmother.</p><div class="cc-cta"><span class="cc-price">$1,240<small>full course</small></span><span class="cc-arrow">›</span></div></div></a>
  <a class="course-card reveal reveal-d2" href="pages/spoken/ps3.html"><div class="cc-hero"><img src="assets/img/spoken-ps3.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">Elementary</span><span class="cc-num">PS · 03</span></div></div><div class="cc-body"><span class="cc-track">Parliamo · Elementary</span><h3 class="cc-title">In Viaggio</h3><p class="cc-desc">Travel Italian for people who actually travel Italy.</p><div class="cc-cta"><span class="cc-price">$1,240<small>full course</small></span><span class="cc-arrow">›</span></div></div></a>
  <a class="course-card reveal reveal-d3" href="pages/spoken/ps4.html"><div class="cc-hero"><img src="assets/img/spoken-ps4.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">Confident</span><span class="cc-num">PS · 04</span></div></div><div class="cc-body"><span class="cc-track">Parliamo · Confident</span><h3 class="cc-title">Chiacchierando</h3><p class="cc-desc">Real conversation — opinion, humour, argument, storytelling.</p><div class="cc-cta"><span class="cc-price">$1,240<small>full course</small></span><span class="cc-arrow">›</span></div></div></a>
</div>
</div></section>

<section class="section-paper"><div class="wrap">
<div class="section-head reveal"><span class="eyebrow eyebrow-line">Cultural Deep-Dives</span><h2 class="display-md">Capsule Culturali — Three Six-Week Deep-Dives</h2></div>
<div class="course-grid" style="grid-template-columns:repeat(3,1fr)">
  <a class="course-card reveal" href="pages/culture/cap-food.html"><div class="cc-hero"><img src="assets/img/cap-food.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">Capsule</span><span class="cc-num">CAP · 01</span></div></div><div class="cc-body"><span class="cc-track">La Cucina</span><h3 class="cc-title">The Language of the Italian Table</h3><p class="cc-desc">Six sessions on pasta, pane, vino, caffè.</p><div class="cc-cta"><span class="cc-price">$390<small>capsule</small></span><span class="cc-arrow">›</span></div></div></a>
  <a class="course-card reveal reveal-d1" href="pages/culture/cap-art.html"><div class="cc-hero"><img src="assets/img/cap-art.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">Capsule</span><span class="cc-num">CAP · 02</span></div></div><div class="cc-body"><span class="cc-track">L'Arte</span><h3 class="cc-title">Renaissance in the Words That Made It</h3><p class="cc-desc">Six sessions on Italian art history from Giotto to Caravaggio.</p><div class="cc-cta"><span class="cc-price">$390<small>capsule</small></span><span class="cc-arrow">›</span></div></div></a>
  <a class="course-card reveal reveal-d2" href="pages/culture/cap-opera.html"><div class="cc-hero"><img src="assets/img/cap-opera.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">Capsule</span><span class="cc-num">CAP · 03</span></div></div><div class="cc-body"><span class="cc-track">L'Opera</span><h3 class="cc-title">Opera as a Second Language</h3><p class="cc-desc">Six sessions on Verdi, Puccini, Rossini.</p><div class="cc-cta"><span class="cc-price">$390<small>capsule</small></span><span class="cc-arrow">›</span></div></div></a>
</div>
</div></section>

<section class="section-dark tagline-band"><div class="wrap-narrow">
<p class="tag-script">Non sai da dove iniziare?</p>
<p>Take a free 15-minute placement call with a Club Italia advisor. We will match you to the right course and start date.</p>
<div class="hero-ctas mt-3" style="justify-content:center;display:flex"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Talk to an Advisor</button></div>
</div></section>
"""
Path(ROOT/"courses.html").write_text(page("All Courses — Club Italia by eTeacher", "Eleven live-online Italian courses. Four structured CEFR levels, four spoken conversation courses, three cultural capsules. Live from Italy.", courses_body))

# ---------- HOW IT WORKS ----------
hiw_body = """
<section class="hero" style="min-height:65vh"><div class="hero-bg"><img src="assets/img/pillar-travel.jpg" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">The Journey</p><h1>From <span class="gold-ital">Ciao</span> to Certification</h1>
<p class="hero-sub">Five elegantly sequenced steps — from your first placement call to a CEFR-aligned certificate. Live from Italy, powered by Biagio AI, certified by eTeacher.</p></div></div></section>

<section class="section-cream" style="padding:0"><div class="wrap" style="padding-top:2rem;padding-bottom:2rem"><div class="proof-row">
<div class="proof-item"><div class="pi-num">20</div><div class="pi-label">Live Lessons</div></div>
<div class="proof-item"><div class="pi-num">85</div><div class="pi-label">Minutes Each Class</div></div>
<div class="proof-item"><div class="pi-num">10–12</div><div class="pi-label">Learners per Group</div></div>
<div class="proof-item"><div class="pi-num">$100</div><div class="pi-label">Cashback on Completion</div></div>
</div></div></section>

<section class="section-paper"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Two Tracks, One Club</span><h2 class="display-md">Choose your journey into Italian</h2><p class="lead">Every learner begins with a live placement call. From there, three distinct paths — structured mastery, conversational fluency, and cultural capsules — meet you exactly where your Italian life is.</p></div>
<div class="feature-grid">
<div class="feat-item reveal"><div class="feat-num">01</div><h3>Club Italia — Structured</h3><p>Four courses, A0 → A2.2, culture at the core, CEFR certification at the end of each course.</p></div>
<div class="feat-item reveal reveal-d1"><div class="feat-num">02</div><h3>Parliamo Italiano — Spoken</h3><p>Four courses, spoken confidence first, no grammar drills, only real talk from the first minute.</p></div>
<div class="feat-item reveal reveal-d2"><div class="feat-num">03</div><h3>Capsule Culturali</h3><p>Three six-session cultural deep-dives on cucina, arte, and opera. Pair with any structured or spoken course.</p></div>
</div></div></section>

<section class="section-dark"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Five Steps</span><h2 class="display-md">Your complete Club Italia journey</h2></div>
<div class="hiw-timeline">
<div class="hiw-step reveal"><div class="hs-num">01</div><h3>Assessment &amp; Enrollment</h3><p>A free 15-min placement call with an academic advisor.</p></div>
<div class="hiw-step reveal reveal-d1"><div class="hs-num">02</div><h3>Join the Platform</h3><p>Your live classroom, materials, and recordings — one home.</p></div>
<div class="hiw-step reveal reveal-d2"><div class="hs-num">03</div><h3>Attend Live Classes</h3><p>One 85-minute class a week, live from Italy, in a small group of 10 to 12.</p></div>
<div class="hiw-step reveal reveal-d3"><div class="hs-num">04</div><h3>Practice &amp; Reinforcement</h3><p>Biagio AI Tutor, weekly micro-tasks, cultural library, community forum.</p></div>
<div class="hiw-step reveal reveal-d3"><div class="hs-num">05</div><h3>Mastery &amp; Certification</h3><p>CEFR-aligned certificate on completion, plus $100 cashback towards your next course.</p></div>
</div></div></section>

<section class="section-cream"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">A Week at Club Italia</span><h2 class="display-md">What a typical week looks like</h2><p class="lead">One live class anchors the week. Everything else keeps your Italian alive between sessions — on your own schedule, at your own pace.</p></div>
<div class="week-grid">
<div class="week-card reveal"><div class="week-day">Monday</div><div class="week-what">Live Class</div><div class="week-note">85 min with your teacher and small group, live from Italy.</div></div>
<div class="week-card reveal reveal-d1"><div class="week-day">Wednesday</div><div class="week-what">Micro-Task</div><div class="week-note">15 min written or spoken cultural task in the platform.</div></div>
<div class="week-card reveal reveal-d2"><div class="week-day">Friday</div><div class="week-what">Biagio Practice</div><div class="week-note">20 min conversation with your AI Italian tutor.</div></div>
<div class="week-card reveal reveal-d3"><div class="week-day">Weekend</div><div class="week-what">Study Group</div><div class="week-note">Optional 60 min peer study group with your cohort.</div></div>
</div></div></section>

<section class="section-dark"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">The Technology</span><h2 class="display-md">A platform built for live learning</h2><p class="lead" style="color:var(--on-dark-soft)">Everything runs in the browser. No downloads, no friction. Just a laptop and a microphone, and Italy opens to you.</p></div>
<div class="feature-grid">
<div class="feat-item reveal"><h3>Live Classroom</h3><p>HD video, browser-based, no download. Your teacher, your classmates, live from Italy.</p></div>
<div class="feat-item reveal reveal-d1"><h3>Recordings Library</h3><p>Every class you attend is yours to keep, forever, even after you finish the course.</p></div>
<div class="feat-item reveal reveal-d2"><h3>Biagio AI Coach</h3><p>24/7 conversation practice with a precision Italian language coach.</p></div>
<div class="feat-item reveal"><h3>Dashboard &amp; Schedule</h3><p>Your calendar, your progress, your certificates — one clean interface.</p></div>
<div class="feat-item reveal reveal-d1"><h3>Cultural Library</h3><p>Curated Italian films, songs, articles and readings between every class.</p></div>
<div class="feat-item reveal reveal-d2"><h3>Community Forum</h3><p>A private forum of adult learners from every continent, moderated by our team.</p></div>
</div></div></section>

<section class="section-paper"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Common Questions</span><h2 class="display-md">Everything worth asking before you begin</h2></div>
<div class="wrap-narrow" style="padding:0">
<details class="faq-item"><summary class="faq-q">Are the classes really live?</summary><div class="faq-a">Every class is live, unscripted, and broadcast in real time from Italy. Nothing is pre-recorded.</div></details>
<details class="faq-item"><summary class="faq-q">How big are the groups?</summary><div class="faq-a">Never more than twelve, typically ten. Every learner speaks meaningfully in every class.</div></details>
<details class="faq-item"><summary class="faq-q">What do I need to join?</summary><div class="faq-a">A laptop or tablet, stable internet, a working microphone, and about 90 minutes a week.</div></details>
<details class="faq-item"><summary class="faq-q">Can I watch a class I missed?</summary><div class="faq-a">Yes, every live class is recorded and available in your dashboard for life.</div></details>
</div>
<div class="text-center mt-4"><a class="btn btn-3d btn-3d-navy" href="faq.html">All Questions Answered</a></div></div></section>

<section class="section-dark tagline-band"><div class="wrap-narrow"><p class="tag-script">Cultura parla italiano.</p><p>Join a live class broadcasting from Italy this week. Twenty lessons. A certificate. A language. A culture.</p>
<div class="hero-ctas mt-3" style="justify-content:center;display:flex"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Talk to an Advisor</button></div></div></section>
"""
Path(ROOT/"how-it-works.html").write_text(page("How It Works — Club Italia by eTeacher","Five elegant steps from placement to CEFR certification. Discover how Club Italia's live Italian program works.",hiw_body))

# ---------- METHOD ----------
method_body = """
<section class="hero" style="min-height:65vh"><div class="hero-bg"><img src="assets/img/pillar-art.jpg" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">Our Method</p><h1>The <span class="gold-ital">Cultural Method</span></h1><p class="hero-sub">Culture is not the reward for learning Italian. Culture is how Italian is learned.</p></div></div></section>

<section class="section-dark"><div class="wrap-narrow"><p class="big-quote reveal">A language is not a set of rules. It is a way of being in the world. To teach Italian without culture is to teach a skeleton without a body.</p></div></section>

<section class="section-paper"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Built on the modern communicative tradition</span><h2 class="display-md">The action-oriented approach, elevated by culture.</h2><p class="lead">Every Club Italia lesson is structured as a live communicative event. There is a real cultural scenario, real interactive tasks, and a real Italian teacher broadcasting from a real Italian city. Grammar is introduced only where the scenario needs it — never as a decontextualised drill.</p></div>
<div class="feature-grid">
<div class="feat-item reveal"><div class="feat-num">01</div><h3>Cultural Scenario</h3><p>Every lesson opens with a real, culturally grounded situation — ordering espresso in Trastevere, arguing about ragù in Bologna, understanding a wall label in the Uffizi.</p></div>
<div class="feat-item reveal reveal-d1"><div class="feat-num">02</div><h3>Live Interaction</h3><p>You speak for at least 40 of every 85 minutes. Not to a bot, not to a recording — to a native Italian teacher and to nine or ten peers.</p></div>
<div class="feat-item reveal reveal-d2"><div class="feat-num">03</div><h3>Guided Structure</h3><p>Grammar and vocabulary emerge from the scenario, are taught in a live 15-minute focus block, and then are used, immediately, in a real task.</p></div>
<div class="feat-item reveal"><div class="feat-num">04</div><h3>Real Task</h3><p>Every lesson closes with a task you could actually do the next day in Italy — book a table, describe your family, order a wine, argue an opinion.</p></div>
</div></div></section>

<section class="section-dark"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Four Principles</span><h2 class="display-md">Four principles that shape every lesson.</h2></div>
<div class="feature-grid">
<div class="feat-item reveal"><h3>Culture First — Always</h3><p>Culture is the syllabus, not the extra. Every grammatical structure is introduced through a cultural context in which it actually lives.</p></div>
<div class="feat-item reveal reveal-d1"><h3>Contextual, Real-World Italian</h3><p>No decontextualised drills. No abstract exercises. Every structure is taught inside a scenario you could plausibly find yourself in tomorrow.</p></div>
<div class="feat-item reveal reveal-d2"><h3>Live Immersion, Never Pre-Recorded</h3><p>Every class is a real-time event. This cannot be faked. It cannot be paused. It cannot be replaced by a video.</p></div>
<div class="feat-item reveal"><h3>Small Groups, Maximum Speaking Time</h3><p>Ten to twelve learners. Every learner speaks meaningfully in every class. This is the mathematical floor of real progress.</p></div>
</div></div></section>

<section class="section-cream"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Six Cultural Worlds</span><h2 class="display-md">Six worlds, one Italy.</h2></div>
<div class="pillars-grid">
<div class="pillar reveal"><img src="assets/img/pillar-art.jpg" alt=""><div class="pillar-overlay"><h3 class="pillar-title">Arte &amp; Architettura</h3></div></div>
<div class="pillar reveal reveal-d1"><img src="assets/img/pillar-food.jpg" alt=""><div class="pillar-overlay"><h3 class="pillar-title">Cucina &amp; Vino</h3></div></div>
<div class="pillar reveal reveal-d2"><img src="assets/img/pillar-travel.jpg" alt=""><div class="pillar-overlay"><h3 class="pillar-title">Viaggio &amp; Paesaggio</h3></div></div>
<div class="pillar reveal"><img src="assets/img/pillar-cinema.jpg" alt=""><div class="pillar-overlay"><h3 class="pillar-title">Cinema &amp; Moda</h3></div></div>
<div class="pillar reveal reveal-d1"><img src="assets/img/pillar-opera.jpg" alt=""><div class="pillar-overlay"><h3 class="pillar-title">Opera &amp; Musica</h3></div></div>
<div class="pillar reveal reveal-d2"><img src="assets/img/pillar-tradition.jpg" alt=""><div class="pillar-overlay"><h3 class="pillar-title">Tradizione &amp; Storia</h3></div></div>
</div></div></section>

<section class="section-dark tagline-band"><div class="wrap-narrow"><p class="tag-script">Il metodo culturale.</p>
<div class="hero-ctas mt-3" style="justify-content:center;display:flex"><a class="btn btn-3d btn-3d-primary" href="courses.html">Explore the Courses</a></div></div></section>
"""
Path(ROOT/"method.html").write_text(page("Our Method — Club Italia by eTeacher","The cultural method of Club Italia: live from Italy, culture at the core, action-oriented CEFR-aligned Italian.",method_body))

# ---------- TEACHERS ----------
TEACHERS = [
    ("Chiara Bellini","Firenze","Toscana","chiara","A0 → B1","CEDILS certified · DITALS I","Chiara is Florentine by birth and by sensibility. She teaches the Italian of the salon, the museum wall label and the market — the language of the city where the language itself was standardised."),
    ("Marco Rinaldi","Roma","Lazio","marco","A0 → B1","DITALS II · Sapienza MA Linguistics","Marco teaches with the warm, cinematic authority of a Roman who has spent a lifetime between Trastevere and the Vatican. His classes hum with the everyday Italian of a real Roman kitchen, a real Roman café, a real Roman argument."),
    ("Giulia Moretti","Bologna","Emilia-Romagna","giulia","A0 → A2.2","DITALS I · Perugia CILS Examiner","Giulia is Bolognese to the bone — la Dotta, la Grassa, la Rossa. She teaches from her kitchen, and by week five you can hear the ragù on the stove in the background. Her method is warm, structured, and unforgiving of laziness."),
    ("Alessandro Ferri","Milano","Lombardia","alessandro","A1 → B1","DITALS II · Ca' Foscari MA Italian Studies","Alessandro brings the sharp, cosmopolitan Italian of Milan — the register of business, of fashion, of the aperitivo. His classes are structured, quick and elegant, with a particular gift for the congiuntivo."),
    ("Francesca Zeno","Venezia","Veneto","francesca","A0 → A2.2","DITALS I · Università Ca' Foscari","Francesca teaches from a Venetian apartment where you can hear the water lapping against the fondamenta. Her Italian is the Italian of the merchant republic — courteous, precise, cosmopolitan, and quietly musical."),
    ("Luca De Simone","Napoli","Campania","luca","A0 → A2.2","DITALS II · Università Federico II","Luca teaches the warm, generous, gestural Italian of Naples — a city where language is inseparable from body, from food, from song. His classes are joyful, fast and unforgettable."),
    ("Sofia Mazzara","Palermo","Sicilia","sofia","A1 → B1","DITALS II · Università di Palermo","Sofia brings the sun-drenched, Arab-Norman-Greek Italian of Sicily — the island where every word carries three civilizations. Her method is patient, cultural and quietly rigorous."),
]

teachers_body = f"""
<section class="hero" style="min-height:70vh"><div class="hero-bg"><img src="assets/img/pillar-tradition.jpg" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">Native · Certified · Live from Italy</p><h1>The voices of Italy, <span class="gold-ital">in every classroom.</span></h1><p class="hero-sub">Seven native certified teachers, each rooted in a different Italian region — from the Dolomites to Sicily — broadcasting live, bringing the real Italy into every lesson.</p></div></div></section>

<section class="section-cream" style="padding:0"><div class="wrap" style="padding-top:2rem;padding-bottom:2rem"><div class="proof-row">
<div class="proof-item"><div class="pi-num">100%</div><div class="pi-label">Native Italian Teachers</div></div>
<div class="proof-item"><div class="pi-num">100%</div><div class="pi-label">Live from Italy</div></div>
<div class="proof-item"><div class="pi-num">10–12</div><div class="pi-label">Learners per Class</div></div>
<div class="proof-item"><div class="pi-num">7</div><div class="pi-label">Italian Regions Represented</div></div>
</div></div></section>

<section class="section-paper"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">The Faculty</span><h2 class="display-md">Seven teachers. Many regions. <span class="gold-ital">One Italy.</span></h2><p class="lead">Each a native speaker, each deeply rooted in a distinct corner of Italy — together, they cover the full cultural breadth of the country. From Palermo to Bolzano, from Naples to Milan, they bring the real accents, the cultural references, and the everyday rhythms of their region into every live class.</p></div>
<div class="teachers-grid">
{"".join(f'<div class="teacher-card reveal"><div class="teacher-portrait"><img src="assets/img/teacher-{slug}.jpg" alt="{name}"></div><div class="teacher-body"><div class="teacher-region">{city} · {region}</div><div class="teacher-name">{name}</div><p class="teacher-bio">{bio}</p><div class="teacher-creds">{levels} · {creds}</div></div></div>' for name,city,region,slug,levels,creds,bio in TEACHERS)}
</div></div></section>

<section class="section-dark"><div class="wrap-narrow"><p class="big-quote reveal">To be taught Italian by someone who lives it is not a detail. It is the whole method.</p></div></section>

<section class="section-cream"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">The Club Italia Difference</span><h2 class="display-md">Certified, native, and broadcasting live</h2><p class="lead">Every teacher is native — not near-native, not heritage — but living and breathing Italian in Italy, every day. And every class is live: a real-time, unscripted communicative event that cannot be faked or pre-recorded.</p></div>
<div class="feature-grid">
<div class="feat-item reveal"><h3>Native, in Italy</h3><p>Every teacher lives in the Italian city they broadcast from. The city is the classroom.</p></div>
<div class="feat-item reveal reveal-d1"><h3>Professionally Certified</h3><p>Every teacher holds a DITALS or CEDILS professional certification in teaching Italian to foreigners.</p></div>
<div class="feat-item reveal reveal-d2"><h3>Culture-First Trained</h3><p>Every teacher is trained in the Club Italia cultural method — culture is the syllabus, not the extra.</p></div>
</div></div></section>

<section class="section-dark tagline-band"><div class="wrap-narrow"><p class="tag-script">Scegli il tuo insegnante. Scegli la tua Italia.</p><p>All Club Italia teachers are available across our course tracks. Your placement call will match you to the right level, the right teacher, and the right cultural journey through Italy.</p>
<div class="hero-ctas mt-3" style="justify-content:center;display:flex"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Talk to an Advisor</button></div></div></section>
"""
Path(ROOT/"teachers.html").write_text(page("Our Teachers — Club Italia by eTeacher","Seven native, certified Italian teachers broadcasting live from across Italy — from Palermo to Bolzano.",teachers_body))

# ---------- CULTURE ----------
culture_body = """
<section class="hero" style="min-height:75vh"><div class="hero-bg"><img src="assets/img/pillar-cinema.jpg" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">Cultura</p><h1>Culture speaks <span class="gold-ital">Italian.</span></h1><p class="hero-sub">To learn Italian is to inherit three millennia of the West's most beloved culture — from the Etruscans to Fellini, from Dante to Ferragamo, from Verdi to the espresso.</p></div></div></section>

<section class="section-paper"><div class="wrap-narrow"><p class="big-quote reveal">Italian is the language of the West's most beloved civilization. To learn it is to inherit the vocabulary of art, food, faith, music, cinema, and the art of living.</p></div></section>

<section class="section-cream"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Six Cultural Chapters</span><h2 class="display-md">Six chapters in the Italian art of living.</h2></div>
<div class="pillars-grid">
<div class="pillar reveal"><img src="assets/img/pillar-art.jpg" alt=""><div class="pillar-overlay"><h3 class="pillar-title">Arte &amp; Architettura</h3><p class="pillar-desc">The vocabulary of beauty was written in Italian. Giotto, Botticelli, Michelangelo, Bernini, Caravaggio.</p></div></div>
<div class="pillar reveal reveal-d1"><img src="assets/img/pillar-food.jpg" alt=""><div class="pillar-overlay"><h3 class="pillar-title">Cucina &amp; Vino</h3><p class="pillar-desc">Italian is a language you can taste. Twenty regions, twenty cuisines, four hundred pasta shapes.</p></div></div>
<div class="pillar reveal reveal-d2"><img src="assets/img/pillar-travel.jpg" alt=""><div class="pillar-overlay"><h3 class="pillar-title">Viaggio &amp; Paesaggio</h3><p class="pillar-desc">A country you can practise in. Rome, Venice, Amalfi, the Dolomites, Sicily — every region a different Italy.</p></div></div>
<div class="pillar reveal"><img src="assets/img/pillar-cinema.jpg" alt=""><div class="pillar-overlay"><h3 class="pillar-title">Cinema &amp; Moda</h3><p class="pillar-desc">From Fellini to Sorrentino, from Armani to Prada — Italy dressed and filmed the twentieth century.</p></div></div>
<div class="pillar reveal reveal-d1"><img src="assets/img/pillar-opera.jpg" alt=""><div class="pillar-overlay"><h3 class="pillar-title">Opera &amp; Musica</h3><p class="pillar-desc">The most musical language in Europe. Verdi, Puccini, Rossini — opera was born in Italian and is still sung in it.</p></div></div>
<div class="pillar reveal reveal-d2"><img src="assets/img/pillar-tradition.jpg" alt=""><div class="pillar-overlay"><h3 class="pillar-title">Tradizione &amp; Storia</h3><p class="pillar-desc">Every word carries three millennia. Etruscan, Roman, Renaissance, Risorgimento — history in every phrase.</p></div></div>
</div></div></section>

<section class="section-dark tagline-band"><div class="wrap-narrow"><p class="tag-script">Non studiare l'italiano. Vivilo.</p><p>Every Club Italia lesson is structured around one of these six cultural worlds. Culture is not a reward for learning Italian. Culture is how Italian is learned.</p>
<div class="hero-ctas mt-3" style="justify-content:center;display:flex"><a class="btn btn-3d btn-3d-primary" href="courses.html">Explore the Courses</a><a class="btn btn-3d btn-3d-ghost" href="capsules.html">See the Culture Capsules</a></div></div></section>
"""
Path(ROOT/"culture.html").write_text(page("Italian Culture — Club Italia by eTeacher","Six cultural chapters that structure every Club Italia lesson — art, cucina, travel, cinema, opera, tradition.",culture_body))

# ---------- CAPSULES INDEX ----------
capsules_body = """
<section class="hero" style="min-height:65vh"><div class="hero-bg"><img src="assets/img/cap-art.jpg" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">Capsule Culturali</p><h1>Culture <span class="gold-ital">Capsules</span></h1><p class="hero-sub">A bite-sized cultural Italian deep-dive. Six live 60-minute sessions on a single Italian cultural world — pair with any structured or spoken course.</p></div></div></section>

<section class="section-paper"><div class="wrap"><div class="section-head reveal"><h2 class="display-md">Three doorways into the Italian cultural world.</h2></div>
<div class="course-grid" style="grid-template-columns:repeat(3,1fr)">
  <a class="course-card reveal" href="pages/culture/cap-food.html"><div class="cc-hero"><img src="assets/img/cap-food.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">Capsule</span><span class="cc-num">CAP · 01</span></div></div><div class="cc-body"><span class="cc-track">La Cucina</span><h3 class="cc-title">The Language of the Italian Table</h3><p class="cc-desc">Six sessions on pasta, pane, vino, caffè, and the sacred rituals of the Italian meal.</p><div class="cc-cta"><span class="cc-price">$390<small>capsule</small></span><span class="cc-arrow">›</span></div></div></a>
  <a class="course-card reveal reveal-d1" href="pages/culture/cap-art.html"><div class="cc-hero"><img src="assets/img/cap-art.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">Capsule</span><span class="cc-num">CAP · 02</span></div></div><div class="cc-body"><span class="cc-track">L'Arte</span><h3 class="cc-title">Renaissance in the Words That Made It</h3><p class="cc-desc">Six sessions on Italian art history — from Giotto to Caravaggio — with museum-ready vocabulary.</p><div class="cc-cta"><span class="cc-price">$390<small>capsule</small></span><span class="cc-arrow">›</span></div></div></a>
  <a class="course-card reveal reveal-d2" href="pages/culture/cap-opera.html"><div class="cc-hero"><img src="assets/img/cap-opera.jpg" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">Capsule</span><span class="cc-num">CAP · 03</span></div></div><div class="cc-body"><span class="cc-track">L'Opera</span><h3 class="cc-title">Opera as a Second Language</h3><p class="cc-desc">Six sessions on Verdi, Puccini, Rossini — read a libretto, follow an aria.</p><div class="cc-cta"><span class="cc-price">$390<small>capsule</small></span><span class="cc-arrow">›</span></div></div></a>
</div></div></section>

<section class="section-cream"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Why capsules</span><h2 class="display-md">Pair a capsule with any course.</h2></div>
<div class="feature-grid">
<div class="feat-item reveal"><h3>One story, beautifully told</h3><p>Each session is a single cultural world, presented cinematically by a native Italian expert.</p></div>
<div class="feat-item reveal reveal-d1"><h3>Sixty minutes, not eighty-five</h3><p>Shorter than a full lesson, deeper than a lecture — designed to fit alongside any course.</p></div>
<div class="feat-item reveal reveal-d2"><h3>Living vocabulary</h3><p>Every capsule builds a set of cultural vocabulary you actually need — for the museum, the table, the opera house.</p></div>
</div></div></section>
"""
Path(ROOT/"capsules.html").write_text(page("Culture Capsules — Club Italia by eTeacher","Three bite-sized Italian cultural capsules: La Cucina, L'Arte, L'Opera. Six 60-minute live sessions each.",capsules_body))

# ---------- BIAGIO ----------
biagio_body = """
<section class="hero tutor-hero" style="min-height:80vh"><div class="hero-content" style="position:relative;z-index:2"><div class="tutor-grid" style="width:100%">
<div class="tutor-copy reveal"><p class="hero-tag">Available 24/7</p><h1>Meet <span class="gold-ital">Biagio,</span> your Italian coach.</h1><p class="hero-sub">Biagio is your AI Italian tutor — a 42-year-old cartoon Roman with a warm voice, a strict method, and unlimited patience. He never sleeps, never loses interest, and always corrects you in Italian.</p><div class="hero-ctas"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button><a class="btn btn-3d btn-3d-ghost" href="#chat">Chat with Biagio</a></div></div>
<div class="tutor-portrait reveal reveal-d1"><img src="assets/img/biagio.png" alt="Biagio, the AI Italian tutor of Club Italia"></div>
</div></div></section>

<section class="section-paper"><div class="wrap-narrow"><p class="big-quote reveal">Not a chatbot. A precision Italian coach.</p><p style="text-align:center;margin:2rem auto 0;color:var(--on-light-soft)">Biagio does not answer questions in English. He does not correct you with a red pen. He does not make you feel small. He speaks Italian — warmly, patiently — and coaxes you into speaking back, one small step at a time.</p></div></section>

<section class="section-cream"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">What Biagio Does</span><h2 class="display-md">Everything a private tutor does, and nothing they cannot.</h2></div>
<div class="feature-grid">
<div class="feat-item reveal"><div class="feat-num">i</div><h3>Conversation Practice</h3><p>Free-form talk on any topic, at your level, from the first minute.</p></div>
<div class="feat-item reveal reveal-d1"><div class="feat-num">ii</div><h3>Instant Correction</h3><p>Every mistake corrected gently, in Italian, with the reason why.</p></div>
<div class="feat-item reveal reveal-d2"><div class="feat-num">iii</div><h3>Pronunciation Coaching</h3><p>Repeat after Biagio — he hears your voice and tells you what to fix.</p></div>
<div class="feat-item reveal"><div class="feat-num">iv</div><h3>Vocabulary Drills</h3><p>Culturally-grounded vocabulary, always in context, never in lists.</p></div>
<div class="feat-item reveal reveal-d1"><div class="feat-num">v</div><h3>Cultural Questions</h3><p>Ask him about calcio, cinema, cucina, opera — he answers in Italian.</p></div>
<div class="feat-item reveal reveal-d2"><div class="feat-num">vi</div><h3>Homework &amp; Class Prep</h3><p>Prepare for tomorrow's live class or review yesterday's, with Biagio at your side.</p></div>
</div></div></section>

<section class="section-dark" id="chat"><div class="wrap-narrow"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Try it now</span><h2 class="display-md">Try Biagio for one minute.</h2><p class="lead" style="color:var(--on-dark-soft)">A short demo of the way Biagio corrects, praises and guides. Type below.</p></div>
<div class="form-card" style="background:var(--navy-soft);border-color:var(--gold-line);max-width:640px">
<div id="biagio-chat-msgs" style="min-height:200px;max-height:400px;overflow-y:auto;background:var(--navy-deep);padding:1rem;margin-bottom:1rem;color:var(--on-dark);font-size:.95rem"><div class="chat-msg bot" style="padding:.6rem 0;color:var(--gold-soft);font-style:italic">Ciao! Sono Biagio. Try ordering an espresso in Italian.</div></div>
<form id="biagio-chat-form" style="display:flex;gap:.5rem"><input type="text" placeholder="Scrivi qui in italiano..." style="flex:1"><button class="btn btn-3d btn-3d-primary" type="submit">Send</button></form>
</div></div></section>

<section class="section-paper"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">When Biagio helps</span><h2 class="display-md">Biagio lives in the moments between class.</h2></div>
<div class="feature-grid">
<div class="feat-item reveal"><h3 style="color:var(--navy)">Before class</h3><p>Preview tomorrow's vocabulary with Biagio for ten minutes before you sit down with your teacher.</p></div>
<div class="feat-item reveal reveal-d1"><h3 style="color:var(--navy)">After class</h3><p>Review what you struggled with, in a private one-on-one, no other learners watching.</p></div>
<div class="feat-item reveal reveal-d2"><h3 style="color:var(--navy)">Between classes</h3><p>Fifteen minutes a day of real conversation with Biagio doubles the speaking hours in your week.</p></div>
<div class="feat-item reveal"><h3 style="color:var(--navy)">At 3 am, any timezone</h3><p>When the moment hits and you want to speak Italian, Biagio is there.</p></div>
</div></div></section>

<section class="section-dark tagline-band"><div class="wrap-narrow"><p class="tag-script">Biagio è sempre qui.</p>
<div class="hero-ctas mt-3" style="justify-content:center;display:flex"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button></div></div></section>

<style>#biagio-chat-msgs .chat-msg{padding:.5rem 0;line-height:1.5}#biagio-chat-msgs .chat-msg.user{color:var(--on-dark);text-align:right}#biagio-chat-msgs .chat-msg.bot{color:var(--gold-soft);font-style:italic}</style>
"""
Path(ROOT/"biagio.html").write_text(page("Biagio — Your AI Italian Tutor · Club Italia by eTeacher","Meet Biagio, your 24/7 AI Italian coach. Conversation practice, correction, pronunciation and cultural questions in Italian.",biagio_body))

# ---------- PRICING ----------
pricing_body = """
<section class="hero" style="min-height:65vh"><div class="hero-bg"><img src="assets/img/course-ci2.jpg" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">Begin your journey in Italian</p><h1>Simple pricing. <span class="gold-ital">One clear promise.</span></h1><p class="hero-sub">A complete, immersive Italian education — live from Italy, small groups, CEFR-aligned, from $62 a week.</p></div></div></section>

<section class="section-paper"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Choose your plan</span><h2 class="display-md">A complete Italian education. Three ways to pay.</h2><p class="lead">Every plan includes the same live instruction, the same small groups of 10 to 12, and the same CEFR-aligned certificate. The plans differ only in how you pay.</p></div>
<div class="pricing-grid">
<div class="price-card reveal"><h3>Monthly</h3><div class="pc-perweek">$84<small> / week</small></div><div class="pc-total">$1,680 total · monthly installments</div><ul><li>20 live 85-minute classes</li><li>Native Italian teacher, live from Italy</li><li>Small group of 10 to 12 learners</li><li>Biagio, your 24/7 AI Italian tutor</li><li>Lifetime access to all recordings</li><li>CEFR A1 or A2 certificate</li><li>Private community &amp; cultural resources</li></ul><button class="btn btn-3d btn-3d-navy" data-advisor type="button">Choose Monthly</button></div>
<div class="price-card featured reveal reveal-d1"><span class="pc-badge">Best Value · Save $440</span><h3>Annual</h3><div class="pc-perweek">$62<small> / week</small></div><div class="pc-total">$1,240 total · single payment</div><ul><li>20 live 85-minute classes</li><li>Native Italian teacher, live from Italy</li><li>Small group of 10 to 12 learners</li><li>Twice-weekly peer study groups</li><li>Biagio, your 24/7 AI Italian tutor</li><li>Lifetime access to all recordings</li><li>CEFR A1 or A2 certificate by eTeacher</li><li>$100 credit toward your next course</li></ul><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Choose Annual</button></div>
<div class="price-card reveal reveal-d2"><h3>Term</h3><div class="pc-perweek">$73<small> / week</small></div><div class="pc-total">$1,460 total · two installments · save $220</div><ul><li>20 live 85-minute classes</li><li>Native Italian teacher, live from Italy</li><li>Small group of 10 to 12 learners</li><li>Biagio, your 24/7 AI Italian tutor</li><li>Lifetime access to all recordings</li><li>CEFR A1 or A2 certificate</li><li>Private community &amp; cultural resources</li></ul><button class="btn btn-3d btn-3d-navy" data-advisor type="button">Choose Term</button></div>
</div>
<p class="lead text-center mt-4" style="max-width:700px;margin-left:auto;margin-right:auto">Capsule Culturali (six 60-minute sessions) are $390 per capsule and can be added to any structured or spoken course.</p></div></section>

<section class="section-cream"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Everything about payment</span><h2 class="display-md">Clear, transparent, always in USD.</h2></div>
<div class="wrap-narrow" style="padding:0">
<details class="faq-item"><summary class="faq-q">Are prices in US dollars?</summary><div class="faq-a">Yes. All prices are in USD and shown for the complete 20-lesson course.</div></details>
<details class="faq-item"><summary class="faq-q">Is there a registration fee?</summary><div class="faq-a">No. There are no hidden materials fees, no registration fees, no exam fees. The price you see is the price you pay.</div></details>
<details class="faq-item"><summary class="faq-q">What payment methods do you accept?</summary><div class="faq-a">All major credit and debit cards, through a secure, encrypted checkout.</div></details>
<details class="faq-item"><summary class="faq-q">Do you offer refunds?</summary><div class="faq-a">Yes — a full refund is available within seven days of your first live class, no questions asked.</div></details>
<details class="faq-item"><summary class="faq-q">What is the $100 cashback credit?</summary><div class="faq-a">On completion of your 20-lesson course, you receive $100 in credit toward your next Club Italia course. It never expires.</div></details>
</div></div></section>

<section class="section-dark tagline-band"><div class="wrap-narrow"><p class="tag-script">Vale ogni centesimo.</p><p>Twenty live lessons. A certificate. A language. A culture. A new relationship with the West's most beloved civilization.</p>
<div class="hero-ctas mt-3" style="justify-content:center;display:flex"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Talk to an Advisor</button></div></div></section>
"""
Path(ROOT/"pricing.html").write_text(page("Pricing — Club Italia by eTeacher","Live Italian classes from $62 a week. Three plans, one clear promise — 20 live 85-min lessons, small groups of 10 to 12, CEFR certificate.",pricing_body))

# ---------- FAQ ----------
FAQ = [
    ("Courses",[
        ("How are the courses structured?","Every course is 20 live 85-minute lessons over 20 weeks. Each is set in a specific Italian cultural context and aligned with a CEFR level."),
        ("How many courses are there in total?","Eleven. Four structured mastery courses (CI Principiante → CI Avanzato, A0 → A2.2), four spoken conversation courses (Parliamo Italiano · Foundation → Confident), and three cultural capsules (La Cucina, L'Arte, L'Opera)."),
        ("How do I know which course is right for me?","A free 15-minute placement call with a Club Italia advisor. We assess your current Italian and match you to the right course, start date, and teacher."),
        ("Can I take more than one course at a time?","Yes. Many learners pair a structured course with a spoken or cultural capsule course."),
    ]),
    ("Pricing",[
        ("How much does a course cost?","$1,240 for the complete 20-lesson course on the annual plan. Monthly and term plans are also available. Cultural capsules are $390 each."),
        ("Are there hidden fees?","No. No registration fee, no materials fee, no exam fee. What you see is what you pay."),
        ("Do you offer refunds?","Yes. A full refund is available within seven days of your first live class, no questions asked."),
    ]),
    ("Teachers",[
        ("Where do the teachers live?","In Italy. Every teacher lives in the Italian city they broadcast from — Rome, Florence, Bologna, Milan, Venice, Naples, Palermo."),
        ("What qualifications do they hold?","Every teacher is a native Italian speaker with either a DITALS or CEDILS professional certification in teaching Italian to foreigners."),
        ("Can I choose my teacher?","On the placement call we will match you to the right teacher for your level and preferred class time. If a specific teacher is important to you, we will do our best to place you with them."),
    ]),
    ("Tech &amp; Access",[
        ("What do I need to join?","A laptop or tablet, stable internet, a working microphone, and about 90 minutes a week."),
        ("Do I need to download anything?","No. Everything runs in your browser."),
        ("Can I take a class from my phone?","We recommend a laptop or tablet — the classroom uses HD video and a large enough screen makes a real difference. But a phone works if it is your only option."),
        ("What if I miss a class?","Every live class is recorded and available in your dashboard for the rest of your life."),
    ]),
    ("Biagio · AI Tutor",[
        ("Is Biagio included in every plan?","Yes. Biagio, your 24/7 AI Italian coach, is included with every Club Italia course at no additional cost."),
        ("Does Biagio replace live class?","No. Biagio is designed to work between live classes — for extra conversation practice, pronunciation, and cultural questions."),
        ("What language does Biagio speak?","Italian. Biagio corrects you in Italian, gently, always in context."),
    ]),
    ("Certification",[
        ("What certificate do I receive?","A CEFR-aligned certificate at the level you completed (A1.1 through B1), issued by eTeacher Group."),
        ("Is the certificate internationally recognised?","The certificate is issued by eTeacher, one of the largest live-online language groups in the world, and follows the Common European Framework of Reference for Languages (CEFR). It is designed to prepare you for an internationally-recognised external exam such as CILS (Perugia) or CELI (Siena) at the corresponding level."),
        ("Do I need to take an exam to get the certificate?","Every course includes internal assessment (mid-course oral and end-of-course full assessment). The certificate is issued on successful completion of the full course."),
    ]),
]
faq_body = f"""
<section class="hero" style="min-height:55vh"><div class="hero-bg"><img src="assets/img/pillar-tradition.jpg" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">Frequently Asked Questions</p><h1>Everything worth asking <span class="gold-ital">before you enroll.</span></h1></div></div></section>

<section class="section-paper"><div class="wrap-narrow">
{"".join(f'<div class="faq-cat reveal"><h3>{cat}</h3>' + "".join(f'<details class="faq-item"><summary class="faq-q">{q}</summary><div class="faq-a">{a}</div></details>' for q,a in items) + '</div>' for cat, items in FAQ)}
</div></section>

<section class="section-dark tagline-band"><div class="wrap-narrow"><p class="tag-script">Ancora domande?</p><p>Speak to one of our advisors — 15 minutes, no obligation, in your timezone.</p>
<div class="hero-ctas mt-3" style="justify-content:center;display:flex"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Talk to an Advisor</button></div></div></section>
"""
Path(ROOT/"faq.html").write_text(page("FAQ — Club Italia by eTeacher","Answers to your questions about Club Italia — live classes, group sizes, recordings, scheduling, cost.",faq_body))

# ---------- ABOUT ----------
about_body = """
<section class="hero" style="min-height:60vh"><div class="hero-bg"><img src="assets/img/course-ci1.jpg" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">About Club Italia</p><h1>An Italian school for <span class="gold-ital">adults who mean it.</span></h1><p class="hero-sub">Club Italia is the Italian faculty of eTeacher Group — a live-online school for adult learners in the United States and around the world who want to learn Italian the way it is actually spoken, taught by the people who live it.</p></div></div></section>

<section class="section-paper"><div class="wrap-narrow"><p class="big-quote reveal">We built Club Italia because there was no premium, live, small-group Italian school for adults who wanted to learn seriously.</p></div></section>

<section class="section-cream"><div class="wrap two-col">
<div class="reveal"><span class="eyebrow eyebrow-line">Our story</span><h2 class="display-md">Why we built it</h2><p class="lead">Between 2020 and 2025, more than 7.5 million Americans travelled to Italy every year. Thousands more began the journey toward Italian dual citizenship. Millions more discovered a love for Italian food, film, art and opera. And yet — for the American adult who wanted to learn Italian seriously, live, in a small group, from real Italians in Italy — the options were remarkably thin.</p><p style="margin-top:1rem;color:var(--on-light-soft)">Club Italia was built to fill that gap. A serious school. A cultural method. Live from Italy. Small groups of 10 to 12. A CEFR-aligned certificate. Backed by 25 years of live-online adult language teaching at eTeacher Group.</p></div>
<div class="reveal reveal-d1"><div class="proof-row" style="grid-template-columns:repeat(2,1fr)">
<div class="proof-item"><div class="pi-num">25+</div><div class="pi-label">years teaching adults online</div></div>
<div class="proof-item"><div class="pi-num">250k+</div><div class="pi-label">learners globally</div></div>
<div class="proof-item"><div class="pi-num">7</div><div class="pi-label">Italian regions</div></div>
<div class="proof-item"><div class="pi-num">10–12</div><div class="pi-label">learners per class</div></div>
</div></div>
</div></section>

<section class="section-dark"><div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">What we believe</span><h2 class="display-md">Three beliefs that shape everything we do.</h2></div>
<div class="feature-grid">
<div class="feat-item reveal"><div class="feat-num">i</div><h3>Culture is the syllabus.</h3><p>Not the reward for learning Italian. Not the bonus. The syllabus itself.</p></div>
<div class="feat-item reveal reveal-d1"><div class="feat-num">ii</div><h3>Live cannot be faked.</h3><p>Every class is live, unscripted, and broadcast in real time from Italy. This is the whole method.</p></div>
<div class="feat-item reveal reveal-d2"><div class="feat-num">iii</div><h3>Small groups, real speaking.</h3><p>10 to 12 learners is the mathematical floor of real progress. We do not go above it.</p></div>
</div></div></section>

<section class="section-cream tagline-band"><div class="wrap-narrow"><p class="tag-script" style="color:var(--terra-deep)">Benvenuti in Club Italia.</p>
<div class="hero-ctas mt-3" style="justify-content:center;display:flex"><a class="btn btn-3d btn-3d-primary" href="courses.html">Explore the Courses</a><button class="btn btn-3d btn-3d-navy" data-advisor type="button">Talk to an Advisor</button></div></div></section>
"""
Path(ROOT/"about.html").write_text(page("About Club Italia by eTeacher","A live-online Italian school for adult learners in the United States and worldwide. Culture at the core, live from Italy.",about_body))

# ---------- ETEACHER GROUP ----------
eteacher_body = """
<section class="hero" style="min-height:55vh"><div class="hero-bg"><img src="assets/img/pillar-art.jpg" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">Backed by eTeacher Group</p><h1>25 years of teaching adults, <span class="gold-ital">live online.</span></h1></div></div></section>

<section class="section-paper"><div class="wrap-narrow"><p class="lead">eTeacher Group was founded in 2000 with a single conviction: that adult learners deserved a real classroom experience delivered live, over the internet, at a fraction of the cost and friction of in-person study. Twenty-five years and more than a quarter of a million learners later, we operate one of the world's largest live-online language faculties — teaching Hebrew, Yiddish, French, Spanish, and now Italian.</p>
<p class="lead mt-3">Club Italia is our Italian faculty — the same live-classroom platform, the same small-group discipline, the same lifetime-recording promise, applied to the language and culture of Italy.</p></div></section>

<section class="section-cream"><div class="wrap"><div class="proof-row">
<div class="proof-item"><div class="pi-num">2000</div><div class="pi-label">Founded</div></div>
<div class="proof-item"><div class="pi-num">250k+</div><div class="pi-label">Adult Learners</div></div>
<div class="proof-item"><div class="pi-num">6</div><div class="pi-label">Language Faculties</div></div>
<div class="proof-item"><div class="pi-num">120+</div><div class="pi-label">Countries Served</div></div>
</div></div></section>

<section class="section-dark tagline-band"><div class="wrap-narrow"><p class="tag-script">Adults, taught seriously, live online.</p>
<div class="hero-ctas mt-3" style="justify-content:center;display:flex"><a class="btn btn-3d btn-3d-primary" href="courses.html">Explore Club Italia</a></div></div></section>
"""
Path(ROOT/"eteacher.html").write_text(page("eTeacher Group — Backing Club Italia","eTeacher Group has taught more than 250,000 adult learners live online since 2000. Club Italia is our Italian faculty.",eteacher_body))

# ---------- CONTACT ----------
contact_body = """
<section class="hero" style="min-height:55vh"><div class="hero-bg"><img src="assets/img/course-ci3.jpg" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">Contact</p><h1>Speak with a <span class="gold-ital">Club Italia advisor.</span></h1><p class="hero-sub">A free 15-minute call, in your timezone, with an academic advisor who will match you to the right course and start date.</p></div></div></section>

<section class="section-paper"><div class="wrap"><div class="two-col">
<div class="reveal"><span class="eyebrow eyebrow-line">By phone or by email</span><h2 class="display-md">Reach us.</h2><p class="lead">We answer every inquiry within one business day. If you prefer, click below and an advisor will reach out to you.</p>
<div style="margin-top:2rem;font-family:var(--serif);font-size:1.4rem;color:var(--navy)">
<p>+1 (888) 230-5110</p>
<p style="margin-top:.5rem">advisor@eTeacherGroup.com</p>
<p style="margin-top:.5rem;font-size:1rem;color:var(--on-light-soft)">Mon–Fri · 8 am – 8 pm US Eastern</p>
</div></div>
<div class="reveal reveal-d1"><div class="form-card">
<div class="advisor-head" style="text-align:left;margin-bottom:1.6rem"><span class="eyebrow eyebrow-line">Talk to an advisor</span><h3 style="font-family:var(--serif);font-size:1.9rem;margin:.4rem 0 .6rem">Request a call</h3></div>
<div class="field"><label for="ct-name">Name</label><input id="ct-name" type="text" placeholder="Your full name"></div>
<div class="field"><label for="ct-email">Email</label><input id="ct-email" type="email" placeholder="you@email.com"></div>
<div class="field"><label for="ct-phone">Phone</label><input id="ct-phone" type="tel" placeholder="+1 555 000 0000"></div>
<div class="field"><label for="ct-msg">Anything we should know</label><textarea id="ct-msg" rows="3" placeholder="Your Italian right now, when you want to start, any question"></textarea></div>
<button class="btn btn-3d btn-3d-primary" data-advisor type="button">Request My Call</button>
</div></div>
</div></div></section>
"""
Path(ROOT/"contact.html").write_text(page("Contact — Club Italia by eTeacher","Contact a Club Italia academic advisor. Free 15-minute call, in your timezone, no obligation.",contact_body))

# ---------- BLOG INDEX ----------
POSTS = [
    ("italian-golden-age","Cinema","The Golden Age of Italian Cinema","How Fellini, Visconti and Rossellini rewrote what film could be","10 Sep 2026","8 min","pillar-cinema.jpg"),
    ("americans-italy","Travel","7.5 Million Americans, One Italy","Why U.S. travellers made Italy their second-most-visited country","24 Aug 2026","7 min","pillar-travel.jpg"),
    ("passato-prossimo","Language","The Passato Prossimo Is Not the Enemy","Why the Italian past tense is the friendliest tense you will meet","12 Aug 2026","6 min","course-ci2.jpg"),
    ("ragu-alla-bolognese","Cuisine","The Real Ragù alla Bolognese","And the eight things it is not","28 Jul 2026","7 min","pillar-food.jpg"),
    ("dual-citizenship","Culture","Italian Dual Citizenship, 2026","What the March 2025 reform means for Italian-descent Americans","15 Jul 2026","9 min","pillar-tradition.jpg"),
    ("verdi-life","Opera","Verdi in a Life","Six operas that shaped a nation and still shape Italian","01 Jul 2026","10 min","pillar-opera.jpg"),
    ("tuscan-italian","Language","Why Italian Is Really Tuscan","Dante, Boccaccio, Petrarch and the accident of the standard","18 Jun 2026","7 min","course-ci2.jpg"),
    ("neapolitan-humour","Culture","Neapolitan Humour, Explained","The philosophy underneath the world's most laughed-in city","02 Jun 2026","6 min","course-ci4.jpg"),
    ("italian-coffee","Cuisine","Italian Coffee Is Not What You Think","A history of espresso, from Naples 1901 to your kitchen","18 May 2026","6 min","cap-food.jpg"),
    ("uffizi-italian","Art","How to Read an Uffizi Wall Label","The five Italian words that unlock the museum","05 May 2026","8 min","cap-art.jpg"),
    ("aperitivo","Culture","The Milanese Aperitivo, Decoded","When it started, what it costs, what you actually eat","22 Apr 2026","6 min","spoken-ps4.jpg"),
]
blog_body = f"""
<section class="hero" style="min-height:55vh"><div class="hero-bg"><img src="assets/img/pillar-tradition.jpg" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">Il Diario Culturale</p><h1>Cultural <span class="gold-ital">Journal</span></h1><p class="hero-sub">Dispatches from Italy — on gastronomy, language, travel, cinema, opera, and the art of living beautifully.</p></div></div></section>

<section class="section-paper"><div class="wrap">
<div class="section-head reveal"><span class="eyebrow eyebrow-line">Featured Essay</span><h2 class="display-md">{POSTS[0][2]}</h2><p class="lead">{POSTS[0][3]}</p></div>
<a class="course-card reveal" href="pages/blog/{POSTS[0][0]}.html" style="max-width:820px;margin:0 auto"><div class="cc-hero" style="aspect-ratio:16/9"><img src="assets/img/{POSTS[0][6]}" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">{POSTS[0][1]}</span><span class="cc-num">{POSTS[0][4]}</span></div></div><div class="cc-body"><h3 class="cc-title">{POSTS[0][2]}</h3><p class="cc-desc">{POSTS[0][3]}</p><div class="cc-cta"><span style="color:var(--gold-deep);font-family:var(--serif);font-size:1.1rem">Read the essay</span><span class="cc-arrow">›</span></div></div></a>
</div></section>

<section class="section-cream"><div class="wrap">
<div class="section-head reveal"><span class="eyebrow eyebrow-line">All Essays</span><h2 class="display-md">Eleven dispatches from Italy</h2></div>
<div class="course-grid" style="grid-template-columns:repeat(3,1fr)">
{"".join(f'<a class="course-card reveal" href="pages/blog/{slug}.html"><div class="cc-hero"><img src="assets/img/{img}" alt=""><div class="cc-hero-overlay"><span class="cc-cefr">{cat}</span><span class="cc-num">{date}</span></div></div><div class="cc-body"><span class="cc-track">{cat}</span><h3 class="cc-title">{title}</h3><p class="cc-desc">{sub}</p><div class="cc-cta"><span style="color:var(--gold-deep);font-family:var(--serif)">{read}</span><span class="cc-arrow">›</span></div></div></a>' for slug,cat,title,sub,date,read,img in POSTS)}
</div></div></section>

<section class="section-dark tagline-band"><div class="wrap-narrow"><p class="tag-script">Leggi. Poi parla.</p><p>Read the journal. Then speak the language.</p>
<div class="hero-ctas mt-3" style="justify-content:center;display:flex"><a class="btn btn-3d btn-3d-primary" href="courses.html">Explore the Courses</a></div></div></section>
"""
Path(ROOT/"blog.html").write_text(page("Cultural Journal — Club Italia by eTeacher","Dispatches from Italy on cuisine, language, travel, cinema, opera, and the art of living.",blog_body))

# ---------- PRIVACY & TERMS ----------
privacy_body = """
<section class="hero" style="min-height:45vh"><div class="hero-bg"><img src="assets/img/course-ci4.jpg" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">Legal</p><h1>Privacy <span class="gold-ital">Policy</span></h1></div></div></section>

<section class="section-paper"><div class="wrap-narrow">
<h2 class="display-sm">1. Who we are</h2><p>Club Italia is a trading style of eTeacher Group. This privacy policy explains how we collect, use, store and share your personal data when you visit clubitalia.live or enroll in a Club Italia course.</p>
<h2 class="display-sm mt-4">2. What we collect</h2><p>We collect the personal data you give us — name, email, phone, level of Italian, timezone, and, if you enroll, billing information. We also collect standard technical data (IP address, browser, device, session length) via cookies for analytics and platform performance.</p>
<h2 class="display-sm mt-4">3. How we use it</h2><p>We use your personal data to contact you about your inquiry, deliver your Italian courses, issue certificates, provide customer support, improve our platform, and — with your explicit consent — send you occasional updates about Club Italia. We do not sell your data.</p>
<h2 class="display-sm mt-4">4. Who we share it with</h2><p>We share your data only with our payment processor (for billing), our email delivery provider (for communications), and our analytics provider (for platform improvement). All processors are contractually bound to protect your data.</p>
<h2 class="display-sm mt-4">5. Your rights</h2><p>You have the right to access, correct, port and delete your personal data at any time. Email advisor@eTeacherGroup.com and we will respond within 30 days.</p>
<h2 class="display-sm mt-4">6. Contact</h2><p>Any privacy question: advisor@eTeacherGroup.com. Last updated 10 September 2026.</p>
</div></section>
"""
Path(ROOT/"privacy.html").write_text(page("Privacy Policy — Club Italia by eTeacher","Club Italia privacy policy. How we collect, use, store and share your personal data.",privacy_body))

terms_body = """
<section class="hero" style="min-height:45vh"><div class="hero-bg"><img src="assets/img/pillar-cinema.jpg" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">Legal</p><h1>Terms &amp; <span class="gold-ital">Conditions</span></h1></div></div></section>

<section class="section-paper"><div class="wrap-narrow">
<h2 class="display-sm">1. Agreement</h2><p>By enrolling in a Club Italia course, you agree to these terms of service between you and eTeacher Group (trading as Club Italia).</p>
<h2 class="display-sm mt-4">2. Enrollment &amp; payment</h2><p>Course pricing is displayed in US dollars. On enrollment, you agree to the payment schedule you selected (annual, term, or monthly). All payments are processed by our secure payment processor.</p>
<h2 class="display-sm mt-4">3. Refunds</h2><p>You may request a full refund within seven days of your first live class, no questions asked. After that, refunds are pro-rated for term and monthly plans and not available for the annual single-payment plan.</p>
<h2 class="display-sm mt-4">4. Class attendance</h2><p>Every live class is recorded and available in your dashboard for life. You do not lose access to material by missing a live class.</p>
<h2 class="display-sm mt-4">5. Certification</h2><p>The CEFR-aligned certificate is issued on successful completion of a full 20-lesson course. eTeacher Group reserves the right to withhold certification for non-completion.</p>
<h2 class="display-sm mt-4">6. Code of conduct</h2><p>Learners are expected to treat teachers and other learners with respect. Harassment, hate speech, or disruptive behaviour will result in removal without refund.</p>
<h2 class="display-sm mt-4">7. Contact</h2><p>Any terms question: advisor@eTeacherGroup.com. Last updated 10 September 2026.</p>
</div></section>
"""
Path(ROOT/"terms.html").write_text(page("Terms & Conditions — Club Italia by eTeacher","Club Italia terms of service — enrollment, payment, refunds, certification, code of conduct.",terms_body))

print("Wrote all root pages.")
