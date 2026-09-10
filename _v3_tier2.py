#!/usr/bin/env python3
"""Tier 2 pages for Club Italia v3."""
import sys, importlib.util, pathlib
ROOT = pathlib.Path("/home/user/workspace/club-italia")
spec = importlib.util.spec_from_file_location("v3", ROOT/"_v3_build.py")
v3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(v3)
head, foot, hero, stats, TEACHERS, teacher_wall, all_course_grid = v3.head, v3.foot, v3.hero, v3.stats, v3.TEACHERS, v3.teacher_wall, v3.all_course_grid


def build_teachers():
    h = head("Our Teachers · Club Italia by eTeacher","Seven certified Italian teachers, each in their own city. Meet the Club Italia faculty.")
    hero_html = hero("assets/video/class-demo.mp4","assets/img/hero-poster.jpg",
        "The Faculty · 2026",
        'Seven certified<br>Italian <span class="ital">teachers.</span>',
        "Every Club Italia teacher lives in the Italian city that anchors the course they teach. Every teacher holds a formal teaching qualification, either DITALS (Certificazione di competenza in didattica dell'italiano a stranieri) or CEDILS (Certificazione in Didattica dell'Italiano come Lingua Straniera), issued by an Italian university. Some hold both.",
        '<a href="courses.html" class="btn btn-primary btn-lg">See Their Courses</a>')

    stats_f = f'<section class="section-cream" style="padding:2.4rem 0;"><div class="wrap">{stats([("7","certified teachers"),("100%","in-country"),("DITALS/CEDILS","every teacher"),("6+ yrs","average tenure at Club Italia")])}</div></section>'

    wall = f'<section class="section-black"><div class="wrap"><div class="section-head"><div class="section-eyebrow">Faculty Wall</div><h2 class="h-display">Choose the teacher,<br>choose the <span class="ital">city.</span></h2></div></div>{teacher_wall()}</section>'

    credentials = f"""
<section class="section-white">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">Credentials, in plain English</div>
      <h2 class="h-display">What every acronym on this <span class="ital">page means.</span></h2>
    </div>
    <table class="glance">
      <tr><td>DITALS I / II</td><td>Certificazione di competenza in didattica dell'italiano a stranieri. Issued by the Università per Stranieri di Siena. The Level II certification is the highest formal qualification for teaching Italian as a second language and requires a written thesis and a supervised teaching component.</td></tr>
      <tr><td>CEDILS</td><td>Certificazione in Didattica dell'Italiano come Lingua Straniera. Issued by Ca' Foscari University of Venice. Requires demonstrated competence in second-language acquisition theory and classroom practice.</td></tr>
      <tr><td>Master FLE</td><td>A postgraduate specialism in the didactics of a foreign language, typically two years of study at an Italian university.</td></tr>
      <tr><td>CEFR Examiner</td><td>Certified to conduct oral and written examinations aligned with the Common European Framework of Reference for Languages.</td></tr>
      <tr><td>CELI</td><td>Certificato di Conoscenza della Lingua Italiana. The examination our teachers most frequently supervise.</td></tr>
    </table>
  </div>
</section>
"""

    method = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="two-col">
      <div>
        <div class="section-eyebrow">Selection</div>
        <h2 class="h-display">One in <span class="ital">forty-three.</span></h2>
        <p class="lede">In 2025 we received 341 applications for four teaching positions. The successful candidates each held DITALS II or CEDILS, five or more years of adult teaching in Italy, and demonstrated the Club Italia house method: grammar drawn from real dialogue, city anchoring, warm classroom register.</p>
      </div>
      <div>
        <div class="section-eyebrow">Continuing training</div>
        <h2 class="h-display">Six pedagogical days<br>a <span class="ital">year.</span></h2>
        <p class="lede">Every Club Italia teacher takes part in six annual pedagogical days: three at our summer residency in Firenze, three on Zoom in winter. Sessions cover CEFR descriptor updates, new material rollout, and shared review of anonymised classroom recordings.</p>
      </div>
    </div>
  </div>
</section>
"""

    cta = f'<section class="section-green"><div class="wrap"><div class="section-head"><div class="section-eyebrow">Book a Teacher</div><h2 class="h-display">Speak to your prospective<br>teacher <span class="ital">this week.</span></h2><p class="lede">Reserve a 20-minute placement call. Your Club Italia advisor will match you to a teacher and a cohort before you enrol.</p></div><div style="margin-top:2rem;"><a href="#lead" class="btn btn-primary btn-lg" style="background:var(--paper);color:var(--green-deep);">Reserve My Placement Call →</a></div></div></section>'

    (ROOT/"teachers.html").write_text(h + hero_html + stats_f + wall + credentials + method + cta + foot())
    return 6


def build_biagio():
    h = head("Biagio · Your AI Italian Tutor · Club Italia","Between live classes, Italian on demand. Biagio, our in-house AI tutor, corrects your grammar in real time.")
    hero_html = hero("assets/video/roma-piazza.mp4","assets/img/hero-poster.jpg",
        "Biagio · The AI Tutor",
        'Italian on demand,<br><span class="ital">between classes.</span>',
        "Biagio is the Club Italia AI tutor. Trained on our own syllabus, calibrated to your CEFR level, and answering in Italian, twenty-four hours a day. When a class ends on Monday night, Biagio picks up the sentence you tripped on.",
        '<a href="#try" class="btn btn-primary btn-lg">See Biagio in Action</a>')

    intro_stats = f'<section class="section-cream" style="padding:2.4rem 0;"><div class="wrap">{stats([("24/7","in Italian"),("A0-B2","CEFR calibrated"),("0.4 sec","average response"),("Included","in every plan")])}</div></section>'

    what = f"""
<section class="section-white">
  <div class="wrap">
    <div class="two-col" style="align-items:center;">
      <div class="zoom-frame"><img src="assets/img/screen-biagio.svg" alt="Biagio AI tutor chat interface"></div>
      <div>
        <div class="section-eyebrow">What Biagio is</div>
        <h2 class="h-display">A tutor,<br>not a <span class="ital">chatbot.</span></h2>
        <p class="lede">Biagio is fine-tuned on the full Club Italia syllabus, on twelve years of teacher corrections, and on the CEFR descriptors that anchor our certifications. When you make a mistake, Biagio does not guess the correction. Biagio names the grammar rule you missed, points at the descriptor it references, and asks you to try again.</p>
        <ul class="includes" style="margin-top:1.4rem;">
          <li>Real-time corrections in Italian</li>
          <li>Grammar rule attached to every correction</li>
          <li>Vocabulary drills at your CEFR level</li>
          <li>Writing feedback on your homework</li>
          <li>Voice mode for pronunciation practice</li>
          <li>All conversations reviewed weekly by your teacher</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

    boundaries = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">What Biagio is not</div>
      <h2 class="h-display">Not a replacement for a <span class="ital">teacher.</span></h2>
    </div>
    <div class="two-col">
      <div><p class="lede">Biagio does not replace your Monday and Thursday live classes. Biagio does not write your homework for you. Biagio does not issue certificates. The pedagogy is a human teacher's; Biagio is the between-class practice partner.</p></div>
      <div><p class="lede">Everything Biagio says is reviewed weekly, in aggregate, by a Club Italia teacher. If Biagio has been drilling you on a rule you have already mastered, your teacher hears about it. If a class of learners keeps making the same mistake with Biagio, the next live lesson adjusts.</p></div>
    </div>
  </div>
</section>
"""

    faq_data = [
      ("Is Biagio just ChatGPT?","No. Biagio uses a large-language-model backend but is fine-tuned on Club Italia's own syllabus, error corpus and CEFR descriptors. Its instructions, its Italian register and its correction style are Club Italia's."),
      ("Will Biagio ever be wrong?","Any AI tutor can be wrong. Every Biagio session is reviewed weekly by a Club Italia teacher. Errors flagged by learners are fixed within seven days."),
      ("Is Biagio private?","Yes. Your conversations with Biagio are visible only to you and to the reviewing teacher at your school. Transcripts are never used for advertising and are never sold."),
      ("Which CEFR levels does Biagio cover?","A0 through B2. C1 and C2 learners are matched to a human conversation coach instead."),
      ("Does Biagio speak my language?","Biagio always answers in Italian. If you ask a question in English, Biagio answers in Italian first, then offers a short English gloss on request."),
    ]
    faq = f'<section class="section-white"><div class="wrap"><div class="section-head"><div class="section-eyebrow">Questions about Biagio</div><h2 class="h-display">Frequently <span class="ital">asked.</span></h2></div><div class="faq">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq_data)}</div></div></section>'

    cta = f'<section id="try" class="section-green"><div class="wrap"><div class="section-head"><div class="section-eyebrow">Meet Biagio</div><h2 class="h-display">Included in every <span class="ital">enrolment.</span></h2><p class="lede">Reserve your placement call. On enrolment, Biagio is on your dashboard from day one.</p></div><div style="margin-top:2rem;"><a href="pricing.html" class="btn btn-primary btn-lg" style="background:var(--paper);color:var(--green-deep);">See Pricing →</a></div></div></section>'

    (ROOT/"biagio.html").write_text(h + hero_html + intro_stats + what + boundaries + faq + cta + foot())
    return 6


def build_how():
    h = head("How Club Italia Works","Placement, dashboard, live classes, Biagio, certificate. Five steps that take you from ciao to conversation.")
    hero_html = hero("assets/video/class-demo.mp4","assets/img/hero-poster.jpg",
        "The Full Walkthrough",
        'From ciao to<br><span class="ital">conversation.</span>',
        "Five steps, one dashboard, one teacher standing in Italy. This is how Club Italia works, from your first placement call to the certificate that closes the level.",
        '<a href="pricing.html" class="btn btn-primary btn-lg">See Pricing</a><a href="sample-class.html" class="btn btn-ghost btn-lg">Sit a Sample Class</a>')

    steps = [
      ("placement","01","Placement call","Twenty minutes with a Club Italia advisor. We hear you speak. We map you onto the CEFR ladder. We write a short recommendation and send it to your inbox within twenty-four hours."),
      ("platform","02","Your dashboard","On enrolment, your dashboard opens in your browser. Every live class, every recording, every homework thread, every PDF and your progress on the CEFR ladder live in one tab."),
      ("liveclass","03","Live from Italy","Monday and Thursday evenings, US time. Twelve seats. One teacher standing in an Italian city. Every class is recorded to your dashboard within thirty minutes."),
      ("biagio","04","Biagio, on demand","Between classes, Biagio is your AI tutor. Ask a question at midnight in Chicago. Answer in three seconds, in Italian, with the CEFR descriptor you are practising."),
      ("certificate","05","Certificate","At the end of every level, you sit a 20-minute oral assessment. A signed, CEFR-aligned certificate arrives in your inbox within seven days."),
    ]
    fold_steps = ""
    for i,(sfx,num,title,desc) in enumerate(steps):
        bg = "section-white" if i%2==0 else "section-cream"
        fold_steps += f'<section class="{bg}"><div class="wrap"><div class="two-col" style="align-items:center;"><div><div class="section-eyebrow">Step {num}</div><h2 class="h-display">{title}.</h2><p class="lede">{desc}</p></div><div class="browser-frame"><div class="browser-chrome"><span></span><span></span><span></span><span class="url">clubitalia.eteacher.com</span></div><img src="assets/img/screen-{sfx}.svg" alt="Step {num}: {title}"></div></div></div></section>'

    timeline = f"""
<section class="section-black">
  <div class="wrap">
    <div class="section-head"><div class="section-eyebrow">The First Twenty Weeks</div><h2 class="h-display">Your first <span class="ital">semester.</span></h2></div>
    <table class="glance" style="border-top-color:rgba(255,255,255,.2);">
      <tr><td style="color:var(--cream-accent);">Week 1</td><td style="color:var(--paper);font-family:var(--serif);">Placement call, cohort assigned, dashboard opens.</td></tr>
      <tr><td style="color:var(--cream-accent);">Weeks 2 to 5</td><td style="color:var(--paper);font-family:var(--serif);">Live lessons 1 to 4. Sound system, greetings, first hundred verbs.</td></tr>
      <tr><td style="color:var(--cream-accent);">Week 6</td><td style="color:var(--paper);font-family:var(--serif);">First short recorded assignment reviewed one-to-one with your teacher.</td></tr>
      <tr><td style="color:var(--cream-accent);">Weeks 7 to 10</td><td style="color:var(--paper);font-family:var(--serif);">Live lessons 5 to 8. Present tense, café dialogue, food and city.</td></tr>
      <tr><td style="color:var(--cream-accent);">Week 11</td><td style="color:var(--paper);font-family:var(--serif);">Mid-course oral assessment. Half-way milestone.</td></tr>
      <tr><td style="color:var(--cream-accent);">Weeks 12 to 18</td><td style="color:var(--paper);font-family:var(--serif);">Live lessons 9 to 18. Past tense, weekend life, extended dialogue.</td></tr>
      <tr><td style="color:var(--cream-accent);">Week 19</td><td style="color:var(--paper);font-family:var(--serif);">Review lesson and full mock oral assessment.</td></tr>
      <tr><td style="color:var(--cream-accent);">Week 20</td><td style="color:var(--paper);font-family:var(--serif);">Final CEFR-aligned oral assessment. Certificate issued within seven days.</td></tr>
    </table>
  </div>
</section>
"""

    cta = f'<section class="section-green"><div class="wrap"><div class="section-head"><h2 class="h-display">Ready to <span class="ital">start.</span></h2><p class="lede">Reserve your placement call.</p></div><div style="margin-top:2rem;"><a href="pricing.html" class="btn btn-primary btn-lg" style="background:var(--paper);color:var(--green-deep);">See Pricing →</a></div></div></section>'

    (ROOT/"how-it-works.html").write_text(h + hero_html + fold_steps + timeline + cta + foot())
    return 8


def build_method():
    h = head("The Club Italia Method","Grammar lives inside dialogue. City-anchored, CEFR-structured, human first. The house method, in full.")
    hero_html = hero("assets/video/firenze-arno.mp4","assets/img/hero-poster.jpg",
        "The House Method",
        'Grammar lives inside<br><span class="ital">dialogue.</span>',
        "Club Italia teaches Italian by starting with a real exchange between Italians. The grammar rule that governs the exchange is drawn out only after the learner has already tried the exchange, wrongly and rightly, in front of the teacher.",
        '<a href="courses.html" class="btn btn-primary btn-lg">See The Catalogue</a>')

    quads = [
      ("City-anchored","Every level is set in a specific Italian city, taught by a teacher who lives in that city. Rome anchors A0. Florence anchors A1. Bologna anchors A2. Naples and Milan anchor B1. The city teaches the register."),
      ("Human first","We do not conjugate a verb on a chart until a real Italian has already used it in front of you. Every grammar point is drawn from a spoken exchange first and codified second."),
      ("CEFR structured","Every syllabus references the 2020 Companion Volume of the Common European Framework. Every certificate references the descriptor you passed."),
      ("Small by design","No CI class over twelve learners; no PS spoken circle over eight. Your teacher knows your name, your work, and the sentence you tripped on last week."),
    ]
    fold_quads = f'<section class="section-cream"><div class="wrap"><div class="section-head"><div class="section-eyebrow">The Four Principles</div><h2 class="h-display">Four <span class="ital">non-negotiables.</span></h2></div><div class="grid-4">{"".join(f"<div style=\"border-top:1px solid var(--gold-line);padding:1.4rem 0 0;\"><div style=\"font-family:var(--serif);font-size:3rem;color:var(--red);\">{i:02d}</div><h3 style=\"font-family:var(--serif);font-size:1.5rem;margin:.3rem 0 .6rem;\">{t}</h3><p style=\"font-size:.95rem;color:var(--ink-2);line-height:1.55;\">{d}</p></div>" for i,(t,d) in enumerate(quads,1))}</div></div></section>'

    scaffold = f"""
<section class="section-white">
  <div class="wrap">
    <div class="section-head"><div class="section-eyebrow">Inside a Club Italia lesson</div><h2 class="h-display">One lesson,<br>eighty-five <span class="ital">minutes.</span></h2></div>
    <table class="glance">
      <tr><td>Minutes 1 to 5</td><td>Welcome. A short recap of last week's homework. Two or three learners share a sentence they wrote.</td></tr>
      <tr><td>Minutes 5 to 20</td><td>The teacher plays a short recorded dialogue between two Italians. Learners guess the meaning; the teacher asks what they heard, not what they understood.</td></tr>
      <tr><td>Minutes 20 to 45</td><td>Learners try the dialogue in pairs, in Zoom breakout rooms. The teacher visits every pair.</td></tr>
      <tr><td>Minutes 45 to 60</td><td>The teacher draws out the grammar rule that governs the exchange. Learners take the rule back into the dialogue.</td></tr>
      <tr><td>Minutes 60 to 75</td><td>A structured practice round with the whole class. Every learner speaks at least twice.</td></tr>
      <tr><td>Minutes 75 to 85</td><td>Free conversation on the theme of the day. The teacher issues the homework thread on the dashboard.</td></tr>
    </table>
  </div>
</section>
"""

    cefr = f"""
<section class="section-black">
  <div class="wrap">
    <div class="two-col" style="align-items:center;">
      <div>
        <div class="section-eyebrow">CEFR Alignment</div>
        <h2 class="h-display">Written against the<br>2020 Companion <span class="ital">Volume.</span></h2>
        <p class="lede">The Common European Framework of Reference for Languages is the Council of Europe's standard for describing what a learner can do in a language, at every level. Club Italia's syllabus is written descriptor by descriptor against the 2020 Companion Volume, and every certificate we issue names the descriptors passed.</p>
      </div>
      <div class="cert-frame"><img src="assets/img/certificate-mockup.svg" alt="Club Italia CEFR-aligned certificate sample"></div>
    </div>
  </div>
</section>
"""

    cta = f'<section class="section-green"><div class="wrap"><div class="section-head"><h2 class="h-display">Try the <span class="ital">method.</span></h2><p class="lede">Sit an open sample class before you enrol.</p></div><div style="margin-top:2rem;"><a href="sample-class.html" class="btn btn-primary btn-lg" style="background:var(--paper);color:var(--green-deep);">See A Sample Class →</a></div></div></section>'

    (ROOT/"method.html").write_text(h + hero_html + fold_quads + scaffold + cefr + cta + foot())
    return 5


def build_culture():
    h = head("The Culture Library · Club Italia","Six pillars of italianità: food, art, opera, cinema, tradition, travel. Read Italy the way Italians live it.")
    hero_html = hero("assets/video/opera-scala.mp4","assets/img/hero-poster.jpg",
        "The Culture Library",
        'Read Italy the way<br>Italians <span class="ital">live it.</span>',
        "Six editorial pillars, dozens of essays, every capsule and every course written into a single cultural map. Free to browse, free to read, and updated weekly by our teachers in Italy.",
        '<a href="#pillars" class="btn btn-primary btn-lg">Browse The Library</a>')

    intro = f'<section class="section-cream" style="padding:2.6rem 0;"><div class="wrap">{stats([("6","cultural pillars"),("140+","essays"),("Weekly","teacher updates"),("Free","for all readers")])}</div></section>'

    pillars = [
      ("food","La Cucina","The Italian Table, region by region."),
      ("art","L'Arte","Renaissance, Baroque, Novecento."),
      ("opera","L'Opera","La Scala, San Carlo, Arena di Verona."),
      ("cinema","Il Cinema","Neorealism to Sorrentino."),
      ("tradition","La Tradizione","Festa, family, Ferragosto."),
      ("travel","Il Viaggio","Twenty regions, twenty tables."),
    ]
    tiles = f'<section id="pillars" class="section-white"><div class="wrap"><div class="section-head"><div class="section-eyebrow">Six Pillars</div><h2 class="h-display">Every side of <span class="ital">italianità.</span></h2></div></div><div class="tiles">{"".join(f"<a class=\"tile\" href=\"pages/culture/pillar-{s}.html\"><img src=\"assets/img/pillar-{s}.jpg\" alt=\"{t}\"><div class=\"tile-content\"><div class=\"tile-sub\">{sub}</div><div class=\"tile-title\">{t}</div></div></a>" for s,t,sub in pillars)}</div></section>'

    capsules_cta = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="two-col" style="align-items:center;">
      <div><div class="section-eyebrow">Take a Cultural Capsule</div><h2 class="h-display">Study the <span class="ital">pillars, in Italian.</span></h2><p class="lede">Our Capsule d'Autore courses are six-week live short courses that turn a pillar into a course. La Cucina taught in Italian from Bologna; L'Arte from Florence; L'Opera from La Scala.</p><div style="margin-top:1.6rem;"><a href="capsules.html" class="btn btn-primary btn-lg">See The Capsules →</a></div></div>
      <img src="assets/img/culture.jpg" alt="A Club Italia cultural capsule in session" style="width:100%;">
    </div>
  </div>
</section>
"""
    (ROOT/"culture.html").write_text(h + hero_html + intro + tiles + capsules_cta + foot())
    return 4


def build_about():
    h = head("About Club Italia · by eTeacher","Club Italia by eTeacher is a live, culturally immersive Italian language school for adult learners.")
    hero_html = hero("assets/video/roma-piazza.mp4","assets/img/hero-poster.jpg",
        "About Club Italia",
        'A school,<br>not an <span class="ital">app.</span>',
        "Club Italia by eTeacher is a live Italian language school for adult learners, built on the eTeacher Group platform that has taught Hebrew, Yiddish, Spanish and Arabic to over four hundred thousand learners since 2000.",
        '<a href="teachers.html" class="btn btn-primary btn-lg">Meet The Teachers</a>')

    stats_s = f'<section class="section-cream" style="padding:2.6rem 0;"><div class="wrap">{stats([("2016","Club Italia founded"),("400,000+","eTeacher learners since 2000"),("7","certified teachers in Italy"),("18","countries in our student body")])}</div></section>'

    story = f"""
<section class="section-white">
  <div class="wrap-narrow">
    <div class="section-eyebrow">The Story</div>
    <h2 class="h-display">A twenty-year <span class="ital">school.</span></h2>
    <p style="font-size:1.2rem;line-height:1.7;color:var(--ink);">eTeacher Group opened its first online classroom in the year 2000, teaching Hebrew, one lesson at a time, to families in the diaspora. Twenty-six years later, we run live online schools in five languages and have taught more than four hundred thousand adult learners across the world.</p>
    <p style="font-size:1.2rem;line-height:1.7;color:var(--ink);">Club Italia was founded in 2016 by a small team of Italian teachers who had grown tired of two things at once: apps that treated their language as a game, and traditional online academies that treated it as a spreadsheet. Club Italia was the answer: live classes, real teachers, small cohorts, city anchors, and an academic register that a serious adult learner recognises on sight.</p>
    <p style="font-size:1.2rem;line-height:1.7;color:var(--ink);">Every teacher on staff lives in the Italian city that anchors the course they teach. Every syllabus is written against the CEFR. Every certificate we issue is signed by the teacher who taught the level.</p>
  </div>
</section>
"""

    values = f"""
<section class="section-black">
  <div class="wrap">
    <div class="section-eyebrow">What We Stand For</div>
    <h2 class="h-display">Three <span class="ital">commitments.</span></h2>
    <div class="grid-3" style="margin-top:2.4rem;">
      <div><h3 style="font-family:var(--serif);font-size:1.7rem;color:var(--cream-accent);">Live, always.</h3><p style="font-size:1rem;color:rgba(251,250,246,.78);line-height:1.6;">Club Italia does not sell pre-recorded courses. Every class is live, on the calendar, taught by a teacher standing in Italy. That is the school.</p></div>
      <div><h3 style="font-family:var(--serif);font-size:1.7rem;color:var(--cream-accent);">Small by design.</h3><p style="font-size:1rem;color:rgba(251,250,246,.78);line-height:1.6;">Twelve learners per CI class. Eight per PS spoken circle. We do not scale by putting more students in the room. We scale by adding cohorts.</p></div>
      <div><h3 style="font-family:var(--serif);font-size:1.7rem;color:var(--cream-accent);">CEFR, honestly.</h3><p style="font-size:1rem;color:rgba(251,250,246,.78);line-height:1.6;">Every syllabus, every certificate and every advisor conversation references the CEFR. We do not invent proprietary levels; we align to the standard.</p></div>
    </div>
  </div>
</section>
"""

    partners = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head"><div class="section-eyebrow">Institutional Partners</div><h2 class="h-display">Who we work <span class="ital">with.</span></h2></div>
    <table class="glance">
      <tr><td>Certification alignment</td><td>Common European Framework of Reference for Languages · Council of Europe (2020 Companion Volume)</td></tr>
      <tr><td>Examiner training</td><td>Università per Stranieri di Perugia · CELI examinations</td></tr>
      <tr><td>Teacher qualifications</td><td>Università per Stranieri di Siena (DITALS I & II) · Ca' Foscari University of Venice (CEDILS)</td></tr>
      <tr><td>Cultural partners</td><td>Società Dante Alighieri · Comitato di New York · Comitato di Chicago</td></tr>
      <tr><td>Operator</td><td>eTeacher Group · online-schools operator since 2000 · 400,000+ learners taught to date</td></tr>
    </table>
  </div>
</section>
"""

    cta = f'<section class="section-green"><div class="wrap"><div class="section-head"><h2 class="h-display">Come <span class="ital">study with us.</span></h2><p class="lede">Reserve a twenty-minute placement call this week.</p></div><div style="margin-top:2rem;"><a href="pricing.html" class="btn btn-primary btn-lg" style="background:var(--paper);color:var(--green-deep);">See Pricing →</a></div></div></section>'

    (ROOT/"about.html").write_text(h + hero_html + stats_s + story + values + partners + cta + foot())
    return 6


def build_faq():
    h = head("Frequently Asked Questions · Club Italia","Everything a serious adult learner asks before enrolling. Answered honestly.")
    hero_html = hero("assets/video/class-demo.mp4","assets/img/hero-poster.jpg",
        "Frequently Asked",
        'Questions,<br><span class="ital">answered honestly.</span>',
        "Everything a serious adult learner tends to ask us on a placement call, gathered on one page. If we have missed something, write to us at advisor@eTeacherGroup.com.",
        '<a href="#faq" class="btn btn-primary btn-lg">Browse The FAQ</a>')

    faqs = {
      "The School":[
        ("Is Club Italia a real school or a course platform?","Club Italia is a live school. Every class is taught by a certified Italian teacher, standing in Italy, at a set time on the calendar. There are no pre-recorded 'watch when you want' lessons in the CI programme."),
        ("Is Club Italia the same as eTeacher Group?","Club Italia is the Italian language school built by eTeacher Group, the online-schools operator that has taught Hebrew, Yiddish, Spanish and Arabic to over four hundred thousand adult learners since 2000."),
        ("Where are the teachers?","In Italy. Every teacher on staff lives and works in the Italian city that anchors their course."),
        ("Do I need any prior Italian?","No. The CI-01 course begins from CEFR A0, absolute beginner. Every applicant sits a 20-minute placement call before enrolment."),
      ],
      "The Courses":[
        ("Which CEFR levels do you cover?","Corso Italiano runs A0 through B1. Parliamo Sempre spoken track covers A0 through B1. Capsule d'Autore is level-independent with English support."),
        ("How large is a class?","Corso Italiano classes are capped at twelve learners. Parliamo Sempre spoken circles at eight. Capsules run open-cohort."),
        ("How long is a course?","Twenty weeks for a CI or PS level, at one live class per week. Six weeks for a capsule. Contact hours are stated on every course page."),
        ("What if I miss a class?","Every live class is recorded to your dashboard within thirty minutes. Your teacher will also flag anything the recording cannot cover in your weekly homework thread."),
        ("Which certificate do I receive?","On successful completion of each CEFR level, you sit a 20-minute oral assessment. A signed, CEFR-aligned certificate is issued within seven days."),
      ],
      "Money":[
        ("What does it cost?","The best rate is Annual at $62 per week, billed once at $3,224 per year. Term (one CEFR level) is $73 per week. Monthly is $84 per week."),
        ("Are there any hidden fees?","No. The tuition includes every live class, every recording, the dashboard, Biagio, all PDFs, the oral assessment, and the certificate."),
        ("What is your refund policy?","A full refund is available within seven days of your first live class. Beyond that, a pro-rated refund is available for the unused portion of the term or year, less a 10% administrative fee."),
        ("Do you offer scholarships?","Yes. Club Italia awards ten need-based scholarships per academic year. Applications open in July and December."),
      ],
      "Technology":[
        ("What technology do I need?","A modern browser (Chrome, Safari, Firefox or Edge), a working webcam and microphone, and a stable internet connection of at least 5 Mbps. There is no app to install."),
        ("Do you have a mobile app?","Not yet. The Club Italia dashboard is a responsive website that works on any modern mobile browser. A native iOS app is planned for 2027."),
        ("Is Biagio, your AI tutor, really necessary?","No. Biagio is included in every plan but no learner is required to use it. It is between-class practice, not part of the live curriculum."),
      ],
    }
    faq_html = f'<section id="faq" class="section-white"><div class="wrap"><div class="section-head"><div class="section-eyebrow">Everything, honestly</div><h2 class="h-display">Frequently <span class="ital">asked.</span></h2></div>'
    for cat, items in faqs.items():
        faq_html += f'<h3 style="font-family:var(--serif);font-size:1.8rem;margin:3rem 0 1rem;color:var(--red);">{cat}</h3><div class="faq">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in items)}</div>'
    faq_html += '</div></section>'

    cta = f'<section class="section-green"><div class="wrap"><div class="section-head"><h2 class="h-display">Still have <span class="ital">a question.</span></h2><p class="lede">Write to your Club Italia advisor at advisor@eTeacherGroup.com or reserve a twenty-minute placement call.</p></div><div style="margin-top:2rem;"><a href="pricing.html" class="btn btn-primary btn-lg" style="background:var(--paper);color:var(--green-deep);">Reserve My Call →</a></div></div></section>'

    (ROOT/"faq.html").write_text(h + hero_html + faq_html + cta + foot())
    return 3


def build_sample():
    h = head("Sit A Sample Class · Club Italia","Every Wednesday at 6pm ET, open sample class. Free, live, no card required.")
    hero_html = hero("assets/video/class-demo.mp4","assets/img/hero-poster.jpg",
        "The Open Sample Class",
        'Sit a live class,<br><span class="ital">no card required.</span>',
        "Every Wednesday at 6pm US Eastern time, we open a live Club Italia class to the public. Sit in on a full 45-minute lesson taught by one of our teachers standing in Italy. No card required, no obligation, no follow-up unless you ask for it.",
        '<a href="#reserve" class="btn btn-primary btn-lg">Reserve My Seat</a>')

    stats_s = f'<section class="section-cream" style="padding:2.6rem 0;"><div class="wrap">{stats([("Every Wed","6pm US Eastern"),("45 min","one full lesson"),("Free","no card required"),("Live","real teacher, real students")])}</div></section>'

    what = f"""
<section class="section-white">
  <div class="wrap">
    <div class="two-col" style="align-items:center;">
      <div class="zoom-frame"><img src="assets/img/zoom-mockup.svg" alt="A live Club Italia sample class"></div>
      <div>
        <div class="section-eyebrow">What to expect</div>
        <h2 class="h-display">One full <span class="ital">45-minute lesson.</span></h2>
        <p class="lede">The sample class is a real Club Italia lesson, not a demo. You sit at CEFR A0, so no prior Italian is required. The teacher opens with a short dialogue between two Italians, breaks it down, has learners try it in pairs, and closes with fifteen minutes of open conversation.</p>
        <ul class="includes" style="margin-top:1.4rem;">
          <li>Real live class, not a recorded demo</li>
          <li>Attend on Zoom in your browser</li>
          <li>Camera and mic optional</li>
          <li>Post-class Q&A with the teacher</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

    schedule = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head"><div class="section-eyebrow">Upcoming Sample Classes</div><h2 class="h-display">Pick a <span class="ital">Wednesday.</span></h2></div>
    <table class="glance">
      <tr><td>Wed 17 September · 6pm ET</td><td>Chiara, Firenze · Italian for absolute beginners · <a href="#reserve" style="color:var(--gold);">Reserve →</a></td></tr>
      <tr><td>Wed 24 September · 6pm ET</td><td>Marco, Roma · Roman Italian at the caffè · <a href="#reserve" style="color:var(--gold);">Reserve →</a></td></tr>
      <tr><td>Wed 1 October · 6pm ET</td><td>Giulia, Bologna · At the Bolognese table · <a href="#reserve" style="color:var(--gold);">Reserve →</a></td></tr>
      <tr><td>Wed 8 October · 6pm ET</td><td>Alessandro, Milano · Milanese business Italian · <a href="#reserve" style="color:var(--gold);">Reserve →</a></td></tr>
      <tr><td>Wed 15 October · 6pm ET</td><td>Francesca, Venezia · Italian in transit · <a href="#reserve" style="color:var(--gold);">Reserve →</a></td></tr>
    </table>
  </div>
</section>
"""

    cta = f"""
<section id="reserve" class="section-green">
  <div class="wrap">
    <div class="section-head"><div class="section-eyebrow">Reserve My Seat</div><h2 class="h-display">Confirm your <span class="ital">Wednesday.</span></h2><p class="lede">Enter your details and we send the Zoom link within a minute. No card required.</p></div>
    <form style="display:grid;grid-template-columns:repeat(4,1fr);gap:.6rem;max-width:940px;margin-top:1.4rem;">
      <input type="text" placeholder="First name" style="padding:1rem;border:0;background:var(--paper);">
      <input type="email" placeholder="Email address" style="padding:1rem;border:0;background:var(--paper);">
      <select style="padding:1rem;border:0;background:var(--paper);"><option>Which Wednesday…</option><option>17 September</option><option>24 September</option><option>1 October</option><option>8 October</option><option>15 October</option></select>
      <button type="submit" class="btn" style="background:var(--ink);color:var(--paper);border:0;">Reserve My Seat →</button>
    </form>
  </div>
</section>
"""

    (ROOT/"sample-class.html").write_text(h + hero_html + stats_s + what + schedule + cta + foot())
    return 5


if __name__ == "__main__":
    print(f"teachers.html · folds={build_teachers()}")
    print(f"biagio.html · folds={build_biagio()}")
    print(f"how-it-works.html · folds={build_how()}")
    print(f"method.html · folds={build_method()}")
    print(f"culture.html · folds={build_culture()}")
    print(f"about.html · folds={build_about()}")
    print(f"faq.html · folds={build_faq()}")
    print(f"sample-class.html · folds={build_sample()}")
