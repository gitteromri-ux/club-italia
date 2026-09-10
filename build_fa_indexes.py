#!/usr/bin/env python3
"""Courses index + Capsules index."""
import sys
sys.path.insert(0, "/home/user/workspace/club-italia")
from build_fa import head, foot, clean, DATA, ROOT
from build_fa_courses import TEACHER

def course_card(cid):
    c = DATA[cid]
    tk, tname, city_en, city, cred = TEACHER[cid]
    title = clean(c["title"].split("—")[0].strip() if "—" in c["title"] else c["title"])
    promise = clean(c["promise"])
    short = promise.split(".")[0] + "."
    if len(short) > 170: short = short[:167] + "..."
    code = c["code"]
    cefr = c["cefr"]
    subfolder = "culture" if cid.startswith("cap") else ("spoken" if cid.startswith("ps") else "courses")
    href = f"pages/{subfolder}/{cid}.html"
    img = c["hero_image"]
    return f'''
      <a class="course-card" href="{href}">
        <div class="cc-hero"><img src="{img}" alt="{title}" loading="lazy"><div class="cc-over"><span class="cc-kicker">{code} · CEFR {cefr}</span><h3 class="cc-title">{title}</h3></div></div>
        <div class="cc-body">
          <p class="cc-desc">{short}</p>
          <p class="cc-meta">Taught by {tname} · {city}</p>
          <div class="cc-cta-row"><span class="cc-price"><em>from $62 / week</em></span><span class="cc-enroll"><em>Enrol ›</em></span></div>
        </div>
      </a>'''

# ---------- COURSES INDEX ----------
def build_courses_index():
    F1 = '''
<section class="hero hero-full section-ink" data-fold="1">
  <video class="hero-video" autoplay muted loop playsinline preload="metadata" poster="assets/img/hero-italian-life.jpg">
    <source src="assets/video/roma-piazza.mp4" type="video/mp4">
  </video>
  <div class="hero-scrim hero-scrim-diagonal"></div>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="eyebrow eyebrow-live">The curriculum · Three tracks · Eleven live courses</span>
      <h1 class="hero-h1">Every course, <em class="gold-ital">every level, every teacher</em>.</h1>
      <p class="hero-sub">The complete Club Italia curriculum in one place. Four CEFR-graded stages of the main course. Four spoken-first sessions. Three cultural capsules for anyone who already reads Italian.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="#the-eleven">See the eleven courses</a>
        <a class="btn btn-ghost" href="pricing.html">See pricing</a>
      </div>
      <div class="trustpilot-strip"><span class="tp-stars">★★★★★</span><span class="tp-score">Trustpilot 4.8 / 5</span><span class="tp-count">on 2,140 verified reviews</span></div>
    </div>
    <div class="hero-visual"><div class="hero-video-right radial-mask"><img src="assets/img/zoom-hero-composite.jpg" alt="A live Italian class" width="720" height="540"></div></div>
  </div>
</section>'''

    ci_cards = "".join(course_card(k) for k in ["ci1","ci2","ci3","ci4"])
    ps_cards = "".join(course_card(k) for k in ["ps1","ps2","ps3","ps4"])
    cap_cards = "".join(course_card(k) for k in ["cap-food","cap-art","cap-opera"])
    F2 = f'''
<section class="section section-cream courses-showcase" id="the-eleven" data-fold="2">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Choose your track</span>
      <h2 class="h2-editorial">Three tracks. <em class="gold-ital">One method.</em></h2>
      <p class="section-lede">Most learners begin with the main course and add a spoken track after the second term. Capsules are open to anyone who already reads Italian at A2 or higher.</p>
    </div>
    <div class="track-band"><span class="tb-num">01</span><span class="tb-name">Club Italia · Il Corso</span><span class="tb-desc">The full CEFR arc from A0 to B1, in four terms.</span></div>
    <div class="course-grid course-grid-4 card-slider">{ci_cards}</div>
    <div class="track-band"><span class="tb-num">02</span><span class="tb-name">Parliamo Italiano</span><span class="tb-desc">Spoken-first live sessions on four Italian scenes.</span></div>
    <div class="course-grid course-grid-4 card-slider">{ps_cards}</div>
    <div class="track-band"><span class="tb-num">03</span><span class="tb-name">Capsule Culturali</span><span class="tb-desc">Six live sessions on a single cultural world.</span></div>
    <div class="course-grid course-grid-3 card-slider">{cap_cards}</div>
  </div>
</section>'''

    nodes = [
        ("A0","Ciao","The alphabet, the sound, the first hello."),
        ("A1.1","Prime parole","Your first real conversations at the caffè."),
        ("A1.2","Vita quotidiana","Daily life, past tense, opinion."),
        ("A2.1","Sicuro","Travel, negotiation, storytelling."),
        ("A2.2","Certificato","The full A2 CEFR oral and written."),
        ("B1","Fluente","Argument, humour, spontaneous Italian."),
    ]
    ladder = "".join(f'<div class="ladder-node"><span class="ln-level">{lv}</span><span class="ln-name">{n}</span><span class="ln-desc">{d}</span></div>' for lv,n,d in nodes)
    F3 = f'''
<section class="section section-ink cefr-band" data-fold="3">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">The path</span><h2 class="h2-editorial">From Ciao to your <em class="gold-ital">CEFR certificate</em>.</h2><p class="section-lede">Six named stages, each one term long. You are placed by a spoken interview, never a form.</p></div>
    <div class="cefr-ladder card-slider">{ladder}</div>
  </div>
</section>'''

    F4 = '''
<section class="section section-travertine method-band" data-fold="4">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">The method, in short</span><h2 class="h2-editorial">A cultural method. <em class="gold-ital">Not an app.</em></h2><p class="section-lede">The same method runs through every one of the eleven courses. It comes from the great Italian language institutes, restaged for the live web.</p></div>
    <div class="method-grid method-grid-3">
      <article class="method-card"><div class="mc-photo"><img src="assets/img/env-marco-desk.jpg" alt="Marco's Roman apartment" loading="lazy"></div><div class="mc-body"><span class="mc-num">01</span><h3 class="mc-title"><em>Live, always.</em></h3><p class="mc-copy">Every lesson is a real live class with a native teacher in Italy and ten to twelve learners. No recorded modules, no self-paced apps.</p></div></article>
      <article class="method-card"><div class="mc-photo"><img src="assets/img/life-trattoria-toscana.jpg" alt="A Tuscan trattoria" loading="lazy"></div><div class="mc-body"><span class="mc-num">02</span><h3 class="mc-title"><em>Scene by scene.</em></h3><p class="mc-copy">You act every lesson. You order coffee, you argue about a film, you telephone the hotel. The grammar arrives in the moment it is needed.</p></div></article>
      <article class="method-card"><div class="mc-photo"><img src="assets/img/life-uffizi-hall.jpg" alt="The Uffizi Gallery" loading="lazy"></div><div class="mc-body"><span class="mc-num">03</span><h3 class="mc-title"><em>Culture at the core.</em></h3><p class="mc-copy">Every term reads a Calvino paragraph, watches a Sorrentino scene, cooks a regional dish and follows one aria.</p></div></article>
    </div>
  </div>
</section>'''

    F5 = '''
<section class="section section-verona placement-band" data-fold="5">
  <div class="wrap section-head-narrow">
    <span class="eyebrow">Not sure which course</span>
    <h2 class="h2-editorial">The placement call, <em class="gold-ital">answered honestly</em>.</h2>
    <p class="section-lede">Thirty minutes with an academic advisor, spoken in English, ending with a clear recommendation. If your Italian is not ready for the course you had in mind, we will say so. If you are already past it, we will say that too.</p>
    <a class="btn btn-primary" href="#reserve">Reserve my placement call</a>
  </div>
</section>'''

    F6 = '''
<section class="section section-verona final-cta" data-fold="6" id="reserve">
  <div class="wrap final-inner">
    <div class="fc-copy"><h2 class="h2-huge">Choose your course, <em class="gold-ital">with an advisor</em>.</h2><p class="fc-lede">Thirty minute placement call. Spoken in English. Ends with a clear recommendation. No obligation to enrol.</p></div>
    <form class="fc-form paper-glass" novalidate>
      <div class="ff-row"><label>Your name<input type="text" name="name" required placeholder="Full name"></label></div>
      <div class="ff-row"><label>Email<input type="email" name="email" required placeholder="you@email.com"></label></div>
      <div class="ff-row"><label>Phone<input type="tel" name="phone" required placeholder="+1 555 000 0000"></label></div>
      <div class="ff-row"><label>Course of interest<select name="course" required><option value="">Choose a course</option><option>CI Principiante</option><option>CI Elementare</option><option>CI Intermedio</option><option>CI Avanzato</option><option>Parliamo · Al Caffè</option><option>Parliamo · A Tavola</option><option>Parliamo · In Viaggio</option><option>Parliamo · Chiacchierando</option><option>Capsule · La Cucina</option><option>Capsule · L'Arte</option><option>Capsule · L'Opera</option><option>Not sure yet</option></select></label></div>
      <button class="btn btn-primary btn-block" type="submit">Reserve my placement call</button>
      <p class="ff-note">We reply within one working day. No sales script, no pressure.</p>
    </form>
  </div>
</section>'''
    html = head("All courses", "Every Club Italia course in one place. Four CEFR stages, four spoken sessions, three cultural capsules.", depth=0) + F1+F2+F3+F4+F5+F6 + foot(0)
    (ROOT/"courses.html").write_text(html)

# ---------- CAPSULES INDEX ----------
def build_capsules_index():
    F1 = '''
<section class="hero hero-full section-ink" data-fold="1">
  <video class="hero-video" autoplay muted loop playsinline preload="metadata" poster="assets/img/life-uffizi-hall.jpg">
    <source src="assets/video/opera-scala.mp4" type="video/mp4">
  </video>
  <div class="hero-scrim hero-scrim-diagonal"></div>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="eyebrow eyebrow-live">Capsule Culturali · Six live sessions each</span>
      <h1 class="hero-h1">Six sessions on <em class="gold-ital">a single Italian world</em>.</h1>
      <p class="hero-sub">A capsule is not a course. It is a cultural retreat. Six ninety-minute live sessions with a specialist teacher on a single Italian subject. Read a libretto, cook a Sunday lunch, walk the Uffizi. In Italian, from Italy, with ten other learners in the room.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="#capsules">See the three capsules</a>
        <a class="btn btn-ghost" href="pricing.html">See pricing</a>
      </div>
      <div class="trustpilot-strip"><span class="tp-stars">★★★★★</span><span class="tp-score">Trustpilot 4.8 / 5</span><span class="tp-count">on 2,140 verified reviews</span></div>
    </div>
    <div class="hero-visual"><div class="hero-video-right radial-mask"><img src="assets/img/life-uffizi-hall.jpg" alt="A hall at the Uffizi Gallery" width="720" height="540"></div></div>
  </div>
</section>'''

    F2 = '''
<section class="section section-cream intro-band" data-fold="2">
  <div class="wrap section-head-narrow">
    <span class="eyebrow">What a capsule is</span>
    <h2 class="h2-editorial">Cultural depth. <em class="gold-ital">In six sessions.</em></h2>
    <p class="section-lede">Every capsule runs for six weeks, with one live ninety-minute session per week. Each is taught by one of our specialist teachers from a real Italian city. Any level from A2 upwards is welcome. There is no exam, no grade, and no attendance rule. Just six weeks inside one Italian world.</p>
  </div>
</section>'''

    caps = [
        ("cap-food","La Cucina","Bologna, with Giulia","cap-food.jpg","Six sessions on the vocabulary and history of the Italian table. Pasta, pane, vino, caffè, and the sacred order of a Sunday lunch."),
        ("cap-art","L'Arte","Florence, with Chiara","cap-art.jpg","Six sessions on the Italian language of art history. Giotto, Piero, Raphael, Caravaggio. The vocabulary that made a Renaissance possible."),
        ("cap-opera","L'Opera","Milan, with Alessandro","cap-opera.jpg","Six sessions on Verdi, Puccini and Rossini. Read a libretto, follow an aria, understand why Italians still cry at the third act."),
    ]
    cap_html = "".join(f'''
      <a class="course-card course-card-tall" href="pages/culture/{cid}.html">
        <div class="cc-hero"><img src="assets/img/{img}" alt="{name}" loading="lazy"><div class="cc-over"><span class="cc-kicker">Capsule · {name}</span><h3 class="cc-title">{name}</h3></div></div>
        <div class="cc-body">
          <p class="cc-desc">{d}</p>
          <p class="cc-meta">Six live 90-minute sessions · {teacher}</p>
          <div class="cc-cta-row"><span class="cc-price"><em>$740 total</em></span><span class="cc-enroll"><em>See capsule ›</em></span></div>
        </div>
      </a>''' for cid,name,teacher,img,d in caps)
    F3 = f'''
<section class="section section-travertine capsules-showcase" id="capsules" data-fold="3">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The three capsules</span>
      <h2 class="h2-editorial">Three worlds. <em class="gold-ital">One country.</em></h2>
    </div>
    <div class="course-grid course-grid-3 card-slider">{cap_html}</div>
  </div>
</section>'''

    F4 = '''
<section class="section section-ink why-capsules" data-fold="4">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Why a capsule</span>
      <h2 class="h2-editorial">Small. Deep. <em class="gold-ital">Complete.</em></h2>
    </div>
    <div class="method-grid method-grid-3">
      <article class="method-card"><div class="mc-body"><span class="mc-num">01</span><h3 class="mc-title"><em>One subject, whole.</em></h3><p class="mc-copy">A capsule closes the loop on a single Italian world in six weeks. You leave with vocabulary, context, and the confidence to speak about it.</p></div></article>
      <article class="method-card"><div class="mc-body"><span class="mc-num">02</span><h3 class="mc-title"><em>Any level from A2.</em></h3><p class="mc-copy">Capsules are open to any learner who already reads Italian at A2 or higher. There is no test to enter, only a short placement note from your advisor.</p></div></article>
      <article class="method-card"><div class="mc-body"><span class="mc-num">03</span><h3 class="mc-title"><em>Free with the annual.</em></h3><p class="mc-copy">Two capsule sessions are free with the Club Italia annual plan. The full capsule can be added to any plan for $740.</p></div></article>
    </div>
  </div>
</section>'''

    tp = [
        ("Sarah Kim","San Francisco","L'Opera","student-sarah.jpg","I read the libretto of La Bohème with Alessandro over six sessions. I now understand why Italians cry at the third act."),
        ("Robert Hensley","Austin","La Cucina","student-robert.jpg","Giulia cooked while she taught. In six weeks I could read a menu in Bologna the way a Bolognese reads it."),
        ("Linda Bauer","Toronto","L'Arte","student-linda.jpg","Six Wednesdays at the Uffizi with Chiara. I now walk into any Italian museum and read the labels."),
    ]
    tp_html = "".join(f'<article class="tp-card"><div class="tpc-head"><img class="tpc-avatar" src="assets/img/{img}" alt="{n}" loading="lazy"><div class="tpc-meta"><span class="tpc-name">{n}</span><span class="tpc-place">{c} · Capsule · {co}</span></div></div><div class="tpc-stars">★★★★★</div><blockquote class="tpc-quote"><em>{q}</em></blockquote><span class="tpc-verified">✓ Verified Trustpilot review</span></article>' for n,c,co,img,q in tp)
    F5 = f'''
<section class="section section-travertine trustpilot-band" data-fold="5">
  <div class="wrap">
    <div class="trustpilot-aggregate"><span class="tp-stars-large">★★★★★</span><span class="tp-agg-score">4.8 / 5</span><span class="tp-agg-count">Trustpilot · 2,140 verified reviews</span></div>
    <div class="section-head"><span class="eyebrow">Capsule graduates</span><h2 class="h2-editorial">Six weeks. <em class="gold-ital">Real depth.</em></h2></div>
    <div class="tp-wall tp-wall-3 card-slider">{tp_html}</div>
  </div>
</section>'''

    F6 = '''
<section class="section section-verona final-cta" data-fold="6" id="reserve">
  <div class="wrap final-inner">
    <div class="fc-copy"><h2 class="h2-huge">Pick your <em class="gold-ital">capsule</em>.</h2><p class="fc-lede">Thirty minute call with an advisor. Spoken in English. Ends with a start date. No obligation to enrol.</p></div>
    <form class="fc-form paper-glass" novalidate>
      <div class="ff-row"><label>Your name<input type="text" name="name" required placeholder="Full name"></label></div>
      <div class="ff-row"><label>Email<input type="email" name="email" required placeholder="you@email.com"></label></div>
      <div class="ff-row"><label>Phone<input type="tel" name="phone" required placeholder="+1 555 000 0000"></label></div>
      <div class="ff-row"><label>Capsule of interest<select name="cap" required><option value="">Choose a capsule</option><option>La Cucina</option><option>L'Arte</option><option>L'Opera</option><option>All three</option></select></label></div>
      <button class="btn btn-primary btn-block" type="submit">Reserve my capsule seat</button>
      <p class="ff-note">We reply within one working day. No sales script, no pressure.</p>
    </form>
  </div>
</section>'''
    html = head("Culture capsules", "Six-session live cultural capsules on the Italian table, art history, and opera. Any level from A2 upwards.", depth=0) + F1+F2+F3+F4+F5+F6 + foot(0)
    (ROOT/"capsules.html").write_text(html)

if __name__ == "__main__":
    build_courses_index()
    build_capsules_index()
    print("indexes built.")
