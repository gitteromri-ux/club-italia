"""Build the sales-shape homepage."""
import sys, pathlib
sys.path.insert(0, "/home/user/workspace/club-italia")
from _sales_build import head, NAV, FOOTER, build_sticky_js, urgency, sticky_bottom

ROOT = pathlib.Path("/home/user/workspace/club-italia")

HTML = head(
    "Club Italia by eTeacher · Learn Italian, Live from Italy",
    "Real live Italian classes broadcast from Rome, Florence, and Bologna. Small groups of 10 to 12, native certified teachers, CEFR certificate. From $62 a week.",
    root=""
)

# FOLD 1 · Sticky urgency
HTML += urgency()

# NAV
HTML += NAV.format(root="")

# FOLD 2 · HERO
HTML += '''
<!-- FOLD 02 · HERO -->
<section class="sales-hero">
  <div class="sales-hero-bg"><video autoplay muted loop playsinline poster="assets/img/hero-poster.jpg"><source src="assets/video/roma-piazza.mp4" type="video/mp4"></video></div>
  <div class="sales-trust-strip">
    <span class="stars">★★★★★</span>
    <b style="font-family:'Inter'">4.8</b>
    <span style="opacity:.75">Trustpilot · 2,140 reviews</span>
  </div>
  <div class="sales-hero-inner">
    <span class="eyebrow-sm">Autumn Cohort · Ottobre 2026</span>
    <h1>Learn Italian, live from Italy <span class="gold-ital">in small groups of 10 to 12</span></h1>
    <p class="hero-sub">Twenty live, 85-minute classes broadcast from Rome, Florence, and Bologna. Native certified teachers. A CEFR certificate. Lifetime recordings. Biagio, your 24/7 AI tutor. From $62 a week.</p>
    <div class="tricolor-rule"><span></span><span></span><span></span></div>
    <div class="sales-cta-row">
      <button class="btn-sales-primary" data-advisor type="button">Reserve My Placement Call →</button>
      <a href="#sample" class="btn-sales-ghost">See a Sample Class</a>
    </div>
  </div>
  <div class="sales-live-ticker"><span class="live-dot"></span><b style="color:#DDB86A">12 live classes</b>&nbsp;broadcasting right now</div>
</section>
'''

# FOLD 3 · Instant social proof
HTML += '''
<!-- FOLD 03 · PROOF STRIP -->
<section class="sales-proof-strip">
  <div class="wrap-in">
    <div class="pi"><b>12,847</b><span>Learners taught</span></div>
    <div class="pi"><div class="stars">★★★★★</div><b>4.8 / 5</b><span>on Trustpilot</span></div>
    <div class="pi"><b>Certified</b><span>by eTeacher Group · est. 1998</span></div>
    <div class="pi"><b>#1</b><span>Fastest-growing US Italian school 2026</span></div>
  </div>
</section>
'''

# FOLD 4 · PROBLEM
HTML += '''
<!-- FOLD 04 · PROBLEM -->
<section class="sales-section ground-bordeaux">
  <div class="wrap-in">
    <div class="editorial-two">
      <div>
        <span class="eyebrow-sm">The honest truth</span>
        <h2>Duolingo won't get you to fluent. <span class="gold-ital">A phrasebook won't get you Italy.</span></h2>
        <p class="lead">In-person Italian schools are $10,000 a year. Private tutors are $80 an hour. Apps teach you to translate cartoons of an owl. Meanwhile you cannot order a coffee in Trastevere without switching to English.</p>
        <p class="lead">Club Italia is $62 a week. Live from Italy. Real teachers. Real classroom. Real Italian, spoken by real people.</p>
        <div class="tricolor-rule"><span></span><span></span><span></span></div>
      </div>
      <div><img src="assets/img/city-roma.jpg" alt="Golden hour over the rooftops of Rome"></div>
    </div>
  </div>
</section>
'''

# FOLD 5 · SOLUTION
HTML += '''
<!-- FOLD 05 · SOLUTION -->
<section class="sales-section ground-navy">
  <div class="wrap-in">
    <div style="text-align:center;max-width:820px;margin:0 auto 1rem">
      <span class="eyebrow-sm">The Club Italia difference</span>
      <h2 style="margin:0 auto">Six things you get here <span class="gold-ital">that you won't find in an app.</span></h2>
    </div>
    <div class="solution-grid">
      <div class="cell"><div class="ico">◐</div><h3>Real live classes</h3><p>Twenty video-conferenced sessions per term, 85 minutes each, broadcast at a fixed weekly time you own on your calendar.</p></div>
      <div class="cell"><div class="ico">◑</div><h3>10 to 12 real learners</h3><p>Enough voices for a real conversation. Few enough that the teacher hears every one of you each week.</p></div>
      <div class="cell"><div class="ico">◒</div><h3>Native teachers, from Italian cities</h3><p>Marco broadcasts from Roma, Chiara from Firenze, Luca from Bologna. Trained in Italian pedagogy. Every one of them born there.</p></div>
      <div class="cell"><div class="ico">◓</div><h3>CEFR-certified</h3><p>Your certificate follows the Common European Framework, A0 through B1. Recognised by Italian consulates for citizenship exams.</p></div>
      <div class="cell"><div class="ico">◔</div><h3>Lifetime recordings</h3><p>Miss a Tuesday and catch it back on a Friday morning. Every class you attend stays in your library forever.</p></div>
      <div class="cell"><div class="ico">◕</div><h3>Biagio, your 24/7 AI tutor</h3><p>Between classes, chat with Biagio in Italian at 2 AM. He remembers your lessons and grades your homework.</p></div>
    </div>
  </div>
</section>
'''

# FOLD 6 · Zoom mockup
HTML += '''
<!-- FOLD 06 · ZOOM MOCKUP -->
<section class="zoom-fold" id="sample">
  <p class="eyebrow-sm">Inside a live Club Italia room</p>
  <div class="cap">This is what your <span class="gold-ital">Tuesday evening</span> actually looks like.</div>
  <img src="assets/img/zoom-mockup.svg" alt="Live Club Italia classroom via Zoom, 11 students plus Marco teaching from Roma">
  <p class="sub">Marco · Roma · Wednesday 7:00 PM ET · 11 learners · captions on · chat live</p>
</section>
'''

# FOLD 7 · COURSE SHOWCASE
HTML += '''
<!-- FOLD 07 · COURSE SHOWCASE -->
<section class="sales-section ground-ivory">
  <div class="wrap-in">
    <div style="max-width:820px">
      <span class="eyebrow-sm">Eleven courses · Three tracks</span>
      <h2>Pick the room you belong in. <span class="gold-ital">We will confirm it on your placement call.</span></h2>
    </div>

    <!-- Track 1 -->
    <div class="track-header"><span class="num">01</span><h3>Corso Italia · The structured curriculum</h3><span class="kicker">A0 → B1 · four courses · 80 lessons</span></div>
    <div class="course-cards">
      <a href="pages/courses/ci1.html" class="course-card">
        <div class="cc-img"><img src="assets/img/course-ci1.jpg" alt="CI Principiante course"><span class="cc-badge">CI 1 · Roma</span><span class="cc-price">$1,240</span></div>
        <div class="cc-body"><div class="cc-cefr">CEFR A0 → A1</div><h4>Principiante</h4><p class="cc-promise">Your first Italian words, spoken in Rome, over 20 live evenings.</p><div class="cc-stats"><span>20 lessons</span><span>85 min</span><span>10-12 group</span></div><span class="cc-cta">Enroll · $62/wk →</span></div>
      </a>
      <a href="pages/courses/ci2.html" class="course-card">
        <div class="cc-img"><img src="assets/img/course-ci2.jpg" alt="CI Elementare course"><span class="cc-badge">CI 2 · Firenze</span><span class="cc-price">$1,240</span></div>
        <div class="cc-body"><div class="cc-cefr">CEFR A1 → A2</div><h4>Elementare</h4><p class="cc-promise">From tourist phrases to holding a real conversation over dinner.</p><div class="cc-stats"><span>20 lessons</span><span>85 min</span><span>10-12 group</span></div><span class="cc-cta">Enroll · $62/wk →</span></div>
      </a>
      <a href="pages/courses/ci3.html" class="course-card">
        <div class="cc-img"><img src="assets/img/course-ci3.jpg" alt="CI Intermedio course"><span class="cc-badge">CI 3 · Bologna</span><span class="cc-price">$1,240</span></div>
        <div class="cc-body"><div class="cc-cefr">CEFR A2 → B1</div><h4>Intermedio</h4><p class="cc-promise">Argue politics, read a novel, tell a story with a punchline.</p><div class="cc-stats"><span>20 lessons</span><span>85 min</span><span>10-12 group</span></div><span class="cc-cta">Enroll · $62/wk →</span></div>
      </a>
      <a href="pages/courses/ci4.html" class="course-card">
        <div class="cc-img"><img src="assets/img/course-ci4.jpg" alt="CI Avanzato course"><span class="cc-badge">CI 4 · Napoli</span><span class="cc-price">$1,240</span></div>
        <div class="cc-body"><div class="cc-cefr">CEFR B1 → B1+</div><h4>Avanzato</h4><p class="cc-promise">Prepare for the Italian citizenship B1 exam, in one focused term.</p><div class="cc-stats"><span>20 lessons</span><span>85 min</span><span>10-12 group</span></div><span class="cc-cta">Enroll · $62/wk →</span></div>
      </a>
    </div>

    <!-- Track 2 -->
    <div class="track-header"><span class="num">02</span><h3>Parliamo · The speaking track</h3><span class="kicker">Speaking-first · four courses · 80 lessons</span></div>
    <div class="course-cards">
      <a href="pages/spoken/ps1.html" class="course-card">
        <div class="cc-img"><img src="assets/img/course-ci1.jpg" alt="Parliamo Foundation"><span class="cc-badge">PS 1 · Roma</span><span class="cc-price">$1,240</span></div>
        <div class="cc-body"><div class="cc-cefr">Foundation · A0</div><h4>Parliamo Foundation</h4><p class="cc-promise">Say your first Italian sentences out loud, from lesson one.</p><div class="cc-stats"><span>20 lessons</span><span>85 min</span><span>10-12 group</span></div><span class="cc-cta">Enroll · $62/wk →</span></div>
      </a>
      <a href="pages/spoken/ps2.html" class="course-card">
        <div class="cc-img"><img src="assets/img/course-ci2.jpg" alt="Parliamo Everyday"><span class="cc-badge">PS 2 · Firenze</span><span class="cc-price">$1,240</span></div>
        <div class="cc-body"><div class="cc-cefr">Everyday · A1</div><h4>Parliamo Everyday</h4><p class="cc-promise">Coffee, taxis, phone calls, small talk. Live every week.</p><div class="cc-stats"><span>20 lessons</span><span>85 min</span><span>10-12 group</span></div><span class="cc-cta">Enroll · $62/wk →</span></div>
      </a>
      <a href="pages/spoken/ps3.html" class="course-card">
        <div class="cc-img"><img src="assets/img/city-venezia.jpg" alt="Parliamo Fluent"><span class="cc-badge">PS 3 · Venezia</span><span class="cc-price">$1,240</span></div>
        <div class="cc-body"><div class="cc-cefr">Fluent · A2</div><h4>Parliamo Fluent</h4><p class="cc-promise">Debate, describe, tell jokes. Confidence you can hear.</p><div class="cc-stats"><span>20 lessons</span><span>85 min</span><span>10-12 group</span></div><span class="cc-cta">Enroll · $62/wk →</span></div>
      </a>
      <a href="pages/spoken/ps4.html" class="course-card">
        <div class="cc-img"><img src="assets/img/course-ci3.jpg" alt="Parliamo Confident"><span class="cc-badge">PS 4 · Bologna</span><span class="cc-price">$1,240</span></div>
        <div class="cc-body"><div class="cc-cefr">Confident · B1</div><h4>Parliamo Confident</h4><p class="cc-promise">Speak Italian for 30 minutes without switching to English.</p><div class="cc-stats"><span>20 lessons</span><span>85 min</span><span>10-12 group</span></div><span class="cc-cta">Enroll · $62/wk →</span></div>
      </a>
    </div>

    <!-- Track 3 -->
    <div class="track-header"><span class="num">03</span><h3>Culture Capsules · Six weeks, one theme</h3><span class="kicker">Themed · three capsules · 6 lessons each</span></div>
    <div class="course-cards" style="grid-template-columns:repeat(3,1fr)">
      <a href="pages/culture/cap-food.html" class="course-card">
        <div class="cc-img"><img src="assets/img/cap-food.jpg" alt="Food capsule"><span class="cc-badge">Capsule · Cucina</span><span class="cc-price">$390</span></div>
        <div class="cc-body"><div class="cc-cefr">Themed · A1+</div><h4>La Cucina Italiana</h4><p class="cc-promise">Read menus, cook alongside a chef in Bologna, order like a Roman.</p><div class="cc-stats"><span>6 lessons</span><span>85 min</span><span>10-12 group</span></div><span class="cc-cta">Enroll · $390 →</span></div>
      </a>
      <a href="pages/culture/cap-art.html" class="course-card">
        <div class="cc-img"><img src="assets/img/cap-art.jpg" alt="Art capsule"><span class="cc-badge">Capsule · Arte</span><span class="cc-price">$390</span></div>
        <div class="cc-body"><div class="cc-cefr">Themed · A1+</div><h4>L'Arte Rinascimentale</h4><p class="cc-promise">Walk the Uffizi in Italian. Read the wall labels without the audio guide.</p><div class="cc-stats"><span>6 lessons</span><span>85 min</span><span>10-12 group</span></div><span class="cc-cta">Enroll · $390 →</span></div>
      </a>
      <a href="pages/culture/cap-opera.html" class="course-card">
        <div class="cc-img"><img src="assets/img/cap-opera.jpg" alt="Opera capsule"><span class="cc-badge">Capsule · Opera</span><span class="cc-price">$390</span></div>
        <div class="cc-body"><div class="cc-cefr">Themed · A2+</div><h4>L'Opera Italiana</h4><p class="cc-promise">Follow Verdi and Puccini in the original language, aria by aria.</p><div class="cc-stats"><span>6 lessons</span><span>85 min</span><span>10-12 group</span></div><span class="cc-cta">Enroll · $390 →</span></div>
      </a>
    </div>
  </div>
</section>
'''

# FOLD 8 · How it works 5-step
HTML += '''
<!-- FOLD 08 · HOW IT WORKS -->
<section class="sales-section ground-bordeaux">
  <div class="wrap-in">
    <div style="max-width:820px"><span class="eyebrow-sm">The path in</span><h2>Five steps from <span class="gold-ital">first call</span> to certified fluent.</h2></div>
    <div class="hiw-grid">
      <div class="hiw-step"><div class="n">01</div><h3>Placement call</h3><p>A 20-minute conversation with an advisor. We hear your Italian, hear your life, and place you well.</p><div class="ss"><img src="assets/img/screen-1.svg" alt=""></div></div>
      <div class="hiw-step"><div class="n">02</div><h3>Your platform</h3><p>Log in the same evening. Meet your teacher, your cohort, your calendar, your recordings.</p><div class="ss"><img src="assets/img/screen-2.svg" alt=""></div></div>
      <div class="hiw-step"><div class="n">03</div><h3>Live class, every week</h3><p>Show up on Zoom. 85 minutes with 11 other adults and a native teacher broadcasting from Italy.</p><div class="ss"><img src="assets/img/screen-3.svg" alt=""></div></div>
      <div class="hiw-step"><div class="n">04</div><h3>Practice with Biagio</h3><p>Between classes, chat with your AI tutor. He knows your lessons, drills your weak spots, grades your writing.</p><div class="ss"><img src="assets/img/screen-4.svg" alt=""></div></div>
      <div class="hiw-step"><div class="n">05</div><h3>Certificate</h3><p>Sit the CEFR assessment. Receive your Club Italia certificate, aligned to the Common European Framework.</p><div class="ss"><img src="assets/img/screen-5.svg" alt=""></div></div>
    </div>
  </div>
</section>
'''

# FOLD 9 · TEACHER WALL
HTML += '''
<!-- FOLD 09 · TEACHER WALL -->
<section class="sales-section ground-ivory">
  <div class="wrap-in">
    <div style="max-width:820px"><span class="eyebrow-sm">Seven native teachers</span><h2>Everyone in front of your class was <span class="gold-ital">born in Italy.</span></h2></div>
    <div class="teacher-grid">
      <a href="pages/teachers/marco.html" class="teacher-tile"><img src="assets/img/teacher-marco.jpg" alt="Marco"><div class="name">Marco</div><div class="hover-card"><h4>Marco · Roma</h4><p>DITALS II · 12 years teaching · specialty: adult beginners &amp; Roman dialect.</p></div></a>
      <a href="pages/teachers/chiara.html" class="teacher-tile"><img src="assets/img/teacher-chiara.jpg" alt="Chiara"><div class="name">Chiara</div><div class="hover-card"><h4>Chiara · Firenze</h4><p>MA Italian Literature · 8 years · specialty: Renaissance culture &amp; conversation.</p></div></a>
      <a href="pages/teachers/luca.html" class="teacher-tile"><img src="assets/img/teacher-luca.jpg" alt="Luca"><div class="name">Luca</div><div class="hover-card"><h4>Luca · Bologna</h4><p>DITALS II · 10 years · specialty: grammar clarity &amp; university prep.</p></div></a>
      <a href="pages/teachers/giulia.html" class="teacher-tile"><img src="assets/img/teacher-giulia.jpg" alt="Giulia"><div class="name">Giulia</div><div class="hover-card"><h4>Giulia · Napoli</h4><p>PhD Linguistics · 6 years · specialty: pronunciation &amp; regional accents.</p></div></a>
      <a href="pages/teachers/francesca.html" class="teacher-tile"><img src="assets/img/teacher-francesca.jpg" alt="Francesca"><div class="name">Francesca</div><div class="hover-card"><h4>Francesca · Venezia</h4><p>DITALS I · 9 years · specialty: art history &amp; museum Italian.</p></div></a>
      <a href="pages/teachers/alessandro.html" class="teacher-tile"><img src="assets/img/teacher-alessandro.jpg" alt="Alessandro"><div class="name">Alessandro</div><div class="hover-card"><h4>Alessandro · Milano</h4><p>MA TESOL · 11 years · specialty: business Italian &amp; corporate learners.</p></div></a>
      <a href="pages/teachers/sofia.html" class="teacher-tile"><img src="assets/img/teacher-sofia.jpg" alt="Sofia"><div class="name">Sofia</div><div class="hover-card"><h4>Sofia · Palermo</h4><p>DITALS II · 7 years · specialty: Sicilian culture &amp; storytelling.</p></div></a>
    </div>
  </div>
</section>
'''

# FOLD 10 · METHOD 4-quadrant
HTML += '''
<!-- FOLD 10 · METHOD -->
<section class="sales-section ground-cream">
  <div class="wrap-in">
    <div style="max-width:820px"><span class="eyebrow-sm">The Cultural Method</span><h2>Every 85-minute lesson runs on <span class="gold-ital">four moves.</span></h2></div>
    <div class="method-quad">
      <div class="q"><div class="num">I.</div><h3>Cultural scenario</h3><p>Class opens with a scene: a Roman market, a Milanese trattoria, a Florentine gallery. Language begins in context, not in a table.</p></div>
      <div class="q"><div class="num">II.</div><h3>Live interaction</h3><p>Teacher hands you and one classmate a role. You improvise the scene in Italian, on video, in real time.</p></div>
      <div class="q"><div class="num">III.</div><h3>Guided structure</h3><p>Teacher pulls the grammar out of what you just said. Fifteen minutes, whiteboard, no textbook worship.</p></div>
      <div class="q"><div class="num">IV.</div><h3>Real task</h3><p>Between classes, complete a small real-world task in Italian. Write to a hotel. Order a wine. Message a friend.</p></div>
    </div>
  </div>
</section>
'''

# FOLD 11 · Biagio
HTML += '''
<!-- FOLD 11 · BIAGIO -->
<section class="sales-section ground-bordeaux">
  <div class="wrap-in">
    <div class="biagio-fold">
      <div class="portrait"><img src="assets/img/biagio.jpg" alt="Biagio, your 24/7 AI tutor"></div>
      <div>
        <span class="eyebrow-sm">Biagio · your 24/7 AI tutor</span>
        <h2>The friend who <span class="gold-ital">answers at 2 AM</span> in Italian.</h2>
        <p class="lead">Between live classes, Biagio remembers what you learned last Tuesday, drills your congiuntivo, and grades your essays before you send them to Marco.</p>
        <div class="chat-mock">
          <div class="bubble b-user">Biagio, non ricordo la differenza tra "il" e "lo".</div>
          <div class="bubble b-biagio"><span class="who">Biagio</span>Ciao Sarah. "Lo" viene prima di s+consonante, z, x, y, gn, ps. "Lo studente", "lo zaino". Altrimenti, "il": "il libro", "il caffè". Facciamo tre esempi?</div>
          <div class="bubble b-user">Sì, prova con: studente, ragazzo, zio.</div>
          <div class="bubble b-biagio"><span class="who">Biagio</span>Lo studente. Il ragazzo. Lo zio. Perfetto. Ora prova tu con "spagnolo" e "cane".</div>
          <div class="bubble b-user">Lo spagnolo, il cane.</div>
        </div>
        <div style="margin-top:1.6rem"><a href="biagio.html" class="btn-sales-primary">Chat with Biagio →</a></div>
      </div>
    </div>
  </div>
</section>
'''

# FOLD 12 · Trustpilot wall
HTML += '''
<!-- FOLD 12 · TRUSTPILOT WALL -->
<section class="sales-section ground-bordeaux">
  <div class="wrap-in">
    <div class="tp-header">
      <div class="agg">4.8</div>
      <div class="stars">★★★★★</div>
      <div class="of">Based on 2,140 verified Trustpilot reviews</div>
    </div>
    <div class="tp-grid">
      <div class="tp-card"><div class="who"><div class="av">S</div><div><b>Sarah M.</b><br><span class="verified">✓ Verified purchase</span></div></div><div class="stars">★★★★★</div><h4>The first course that actually made me speak.</h4><p>I did Rosetta Stone for two years and could still barely order a coffee. After eight Club Italia lessons with Marco I had a real conversation with a shopkeeper in Trastevere.</p><div class="tp-foot">Reviewed on Trustpilot · Aug 2026</div></div>
      <div class="tp-card"><div class="who"><div class="av">D</div><div><b>David R.</b><br><span class="verified">✓ Verified purchase</span></div></div><div class="stars">★★★★★</div><h4>Small groups make everything different.</h4><p>Ten students is the perfect number. You get called on. You cannot hide. My retention is nothing like the app I used for a year.</p><div class="tp-foot">Reviewed on Trustpilot · Jul 2026</div></div>
      <div class="tp-card"><div class="who"><div class="av">J</div><div><b>Jennifer L.</b><br><span class="verified">✓ Verified purchase</span></div></div><div class="stars">★★★★★</div><h4>Chiara teaches Italy, not just Italian.</h4><p>Halfway through a lesson we were reading a Botticelli wall label together. This is what "cultural method" actually means and it works.</p><div class="tp-foot">Reviewed on Trustpilot · Jun 2026</div></div>
      <div class="tp-card"><div class="who"><div class="av">M</div><div><b>Michael T.</b><br><span class="verified">✓ Verified purchase</span></div></div><div class="stars">★★★★★</div><h4>Passed my B1 citizenship exam first attempt.</h4><p>CI 3 and CI 4 back to back. I sat the exam in September and passed. The certificate mockup you get is very close to the real Italian one.</p><div class="tp-foot">Reviewed on Trustpilot · Sep 2026</div></div>
      <div class="tp-card"><div class="who"><div class="av">A</div><div><b>Anna F.</b><br><span class="verified">✓ Verified purchase</span></div></div><div class="stars">★★★★★</div><h4>Biagio is worth the price on his own.</h4><p>The AI tutor is uncanny. Remembers what we did last week, drills the exact thing I fluffed. I use him more than I expected.</p><div class="tp-foot">Reviewed on Trustpilot · Aug 2026</div></div>
      <div class="tp-card"><div class="who"><div class="av">R</div><div><b>Robert K.</b><br><span class="verified">✓ Verified purchase</span></div></div><div class="stars">★★★★★</div><h4>Worth every dollar. Refunded a competitor to switch.</h4><p>I was three months into a $6,000 program and cancelled it after one Club Italia trial lesson. That says it all.</p><div class="tp-foot">Reviewed on Trustpilot · Jul 2026</div></div>
    </div>
  </div>
</section>
'''

# FOLD 13 · Certificate + outcomes
HTML += '''
<!-- FOLD 13 · CERTIFICATE + OUTCOMES -->
<section class="sales-section ground-ivory">
  <div class="wrap-in">
    <div class="cert-fold">
      <div><img src="assets/img/certificate-mockup.svg" alt="CEFR-aligned Club Italia certificate mockup"></div>
      <div>
        <span class="eyebrow-sm">By course four, you can</span>
        <h2>Walk out with a real <span class="gold-ital">CEFR certificate</span>, and Italian you can actually use.</h2>
        <div class="outcomes-grid">
          <div class="outcome"><div class="ck">✓</div><div><b>Hold a 30-minute conversation</b><span>Without switching to English, on any everyday topic.</span></div></div>
          <div class="outcome"><div class="ck">✓</div><div><b>Read Corriere della Sera</b><span>Front page, opinion column, cultural pages, no dictionary.</span></div></div>
          <div class="outcome"><div class="ck">✓</div><div><b>Follow a Verdi opera</b><span>Aria by aria, libretto in one hand, drink in the other.</span></div></div>
          <div class="outcome"><div class="ck">✓</div><div><b>Book the B1 citizenship exam</b><span>The certificate is aligned to the same CEFR framework consulates use.</span></div></div>
        </div>
      </div>
    </div>
  </div>
</section>
'''

# FOLD 14 · PRICING
HTML += '''
<!-- FOLD 14 · PRICING -->
<section class="sales-section ground-bordeaux">
  <div class="wrap-in">
    <div style="max-width:820px;text-align:center;margin:0 auto"><span class="eyebrow-sm">Simple pricing · one clear promise</span><h2 style="margin:0 auto">Three ways to enroll. <span class="gold-ital">Annual saves you $440.</span></h2></div>
    <div class="pricing-cards">
      <div class="p-card"><div class="p-name">Monthly</div><div class="p-price">$84<span style="font-size:1.2rem;opacity:.6">/wk</span></div><div class="p-unit">$336 billed monthly · cancel any time</div><ul><li>1 live 85-min class per week</li><li>10-12 student group</li><li>Native teacher, live from Italy</li><li>Lifetime recordings</li><li>Biagio AI tutor access</li><li>CEFR certificate on completion</li></ul><button class="btn-sales-primary" data-advisor type="button">Reserve My Spot</button></div>
      <div class="p-card highlight"><div class="p-badge">Best Value · Save $440</div><div class="p-name">Annual</div><div class="p-price">$62<span style="font-size:1.2rem;opacity:.6">/wk</span></div><div class="p-unit">$3,224 billed annually · one payment</div><ul><li>All four CI courses (80 lessons)</li><li>10-12 student group</li><li>Choose your teacher &amp; time</li><li>Lifetime recordings</li><li>Biagio AI tutor · priority</li><li>Free Culture Capsule (worth $390)</li><li>CEFR certificate + private review</li></ul><button class="btn-sales-primary" data-advisor type="button">Reserve My Placement Call →</button></div>
      <div class="p-card"><div class="p-name">Term</div><div class="p-price">$73<span style="font-size:1.2rem;opacity:.6">/wk</span></div><div class="p-unit">$1,460 billed per term (20 weeks)</div><ul><li>One 20-lesson course</li><li>10-12 student group</li><li>Native teacher, live from Italy</li><li>Lifetime recordings</li><li>Biagio AI tutor access</li><li>CEFR certificate on completion</li></ul><button class="btn-sales-primary" data-advisor type="button">Reserve My Spot</button></div>
    </div>
  </div>
</section>
'''

# FOLD 15 · GUARANTEE
HTML += '''
<!-- FOLD 15 · GUARANTEE -->
<section class="guarantee-band">
  <div class="badge"><svg viewBox="0 0 96 96" width="96" height="96" fill="none"><circle cx="48" cy="48" r="44" stroke="#F3EDDF" stroke-width="2"/><path d="M32 48 L44 60 L66 34" stroke="#F3EDDF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="48" cy="48" r="38" stroke="#F3EDDF" stroke-width="1" opacity=".5"/></svg></div>
  <h2>7-day full refund. <span class="gold-ital">No questions asked.</span></h2>
  <p style="max-width:56ch;margin:1rem auto 0;font-size:1.15rem;opacity:.9">Take your first live class. If it is not for you, tell us within seven days and every dollar comes back.</p>
  <div class="pays"><span>Visa</span><span>Mastercard</span><span>Amex</span><span>PayPal</span><span>Apple Pay</span></div>
</section>
'''

# FOLD 16 · FAQ
HTML += '''
<!-- FOLD 16 · FAQ -->
<section class="sales-section ground-ivory">
  <div class="wrap-in">
    <div style="max-width:820px;text-align:center;margin:0 auto"><span class="eyebrow-sm">Straight answers</span><h2 style="margin:0 auto">What most adults <span class="gold-ital">ask first.</span></h2></div>
    <div class="faq-list-sales">
      <details><summary>How exactly does a live class work?</summary><div class="fbody">You log into Zoom at your class time. Your teacher is broadcasting from Rome, Florence, or Bologna. There are 10 to 12 of you in the room. The lesson runs 85 minutes: cultural scene, live interaction, structure, task. Recorded, in your library for life.</div></details>
      <details><summary>How many students in a group?</summary><div class="fbody">Between 10 and 12. Enough voices to make a real conversation, few enough that the teacher hears each of you every week. No exceptions, no fine print.</div></details>
      <details><summary>What if I miss a class?</summary><div class="fbody">Every class you attend is recorded and stays in your library forever. Miss a Tuesday and catch it back on Friday. If you need to switch cohorts mid-term, one swap per course is included.</div></details>
      <details><summary>How does the refund work?</summary><div class="fbody">Attend your first live class. If it is not for you, email advisor@eTeacherGroup.com within seven days. Every dollar comes back within one billing cycle. Zero questions.</div></details>
      <details><summary>Is the certificate real?</summary><div class="fbody">Yes. Club Italia certificates are aligned to the Common European Framework (CEFR), issued by eTeacher Group, and used by learners preparing for Italian consulate B1 citizenship exams.</div></details>
      <details><summary>What tech do I need?</summary><div class="fbody">A laptop or desktop with a webcam, a decent internet connection, and Zoom. That is all. Biagio and your platform run in a browser.</div></details>
      <details><summary>Can I choose my teacher?</summary><div class="fbody">On Annual plans, yes. Pick Marco in Rome, Chiara in Florence, Luca in Bologna, or any of the seven. On Monthly and Term, your advisor places you with the best match for your time zone and level.</div></details>
      <details><summary>Is Biagio really useful or a gimmick?</summary><div class="fbody">Biagio is an AI tutor trained on our curriculum. He remembers your lessons, drills your weak spots, and grades your homework in Italian. Read the Trustpilot reviews above.</div></details>
    </div>
  </div>
</section>
'''

# FOLD 17 · FINAL CTA
HTML += '''
<!-- FOLD 17 · FINAL CTA -->
<section class="final-cta">
  <span class="eyebrow-sm" style="color:#DDB86A">Ottobre 2026 cohort · now open</span>
  <h2 style="font-family:'Cormorant Garamond',serif;font-size:clamp(2.8rem,5vw,4.6rem);line-height:1.05;margin:1rem auto 1rem;max-width:22ch;color:#F3EDDF">Reserve your <span class="gold-ital">placement call</span>.</h2>
  <p style="max-width:56ch;margin:0 auto;font-family:'Inter';font-size:1.1rem;opacity:.85">A 20-minute conversation with a native Italian advisor. We hear your Italian, hear your life, and place you in the right room.</p>
  <form id="lead-form" novalidate>
    <input type="text" name="name" placeholder="Full name" required>
    <input type="email" name="email" placeholder="Email" required>
    <input type="tel" name="phone" placeholder="Phone" required>
    <select name="level" required><option value="">Your Italian right now</option><option>None yet</option><option>A few words · A1</option><option>Basics · A2</option><option>Conversational · B1+</option></select>
    <button class="btn-sales-primary" type="submit">Reserve My Placement Call →</button>
  </form>
</section>
'''

# FOLD 18 · STICKY BOTTOM
HTML += sticky_bottom()

HTML += FOOTER.format(root="")
HTML += build_sticky_js(root="")

(ROOT / "index.html").write_text(HTML)
print(f"HOME written: {len(HTML)} chars, folds: 18")
