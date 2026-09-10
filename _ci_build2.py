#!/usr/bin/env python3
"""Tier 1 top pages: teachers, biagio, how-it-works, method, culture."""
import sys
sys.path.insert(0, "/home/user/workspace/club-italia")
from _ci_build import page, stats_strip, final_cta_verona, tp_wall, TEACHERS, ROOT

# ============================================================
# TEACHERS.HTML — 8 folds
# ============================================================
def build_teachers_index():
    # Fold 1 — hero
    hero = """
<section class="section-ink hero-page hero-100">
  <div class="hero-bg">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/img/hero-teacher-live.jpg">
      <source src="assets/video/firenze-arno.mp4" type="video/mp4">
    </video>
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">The faculty</span>
    <h1 class="serif-display hero-h1">Seven native teachers.<br><em>Seven Italian cities.</em></h1>
    <p class="lead">Every teacher on the Club Italia faculty is native, holds a formal Italian-as-a-foreign-language qualification, and teaches from one Italian region. Not seven interchangeable staff. Seven specific people, in seven specific rooms in Italy.</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">Talk to an Advisor</button>
      <a class="btn btn-ghost btn-lg" href="#faculty">Meet the faculty</a>
    </div>
  </div>
</section>
"""
    fold2 = stats_strip("dark")
    fold3 = """
<section class="section-paper">
  <div class="wrap">
    <div class="section-head-split">
      <div>
        <span class="eyebrow">About the faculty</span>
        <h2 class="serif-display">Hired one at a time,<br>from one country</h2>
      </div>
    </div>
    <div class="editorial-2col">
      <div class="col-essay">
        <p>We do not staff by keyword. Every teacher on this faculty was hired individually, from a specific Italian city, after teaching a live audition class to real adult learners. Each one holds a DITALS II or CEDILS specialisation from an Italian university, and each one has spent at least seven years teaching foreign adults before joining us. There is no other route in.</p>
        <p>The size of the faculty is deliberate. Seven teachers is enough to give every course two open cohorts a term. It is small enough that a student who studies with us for a year knows the whole faculty by name, and often by voice. It is small enough that the head of school reads every end of term evaluation herself. It is what a school looks like when it is a school and not a marketplace.</p>
      </div>
      <div class="col-essay">
        <div class="pullquote-band pullquote-inline">
          <blockquote class="serif-display quote-md"><em>A teacher who teaches from her own city teaches a language that has a place. That is worth more than any curriculum I could write.</em></blockquote>
          <div class="quote-attr">Head of School · Club Italia</div>
        </div>
      </div>
    </div>
  </div>
</section>
"""
    # Fold 4 — teachers-grid, 7 cards
    cards = ""
    for t in TEACHERS:
        cards += f"""
      <a class="tc-card" href="pages/teachers/{t['slug']}.html">
        <div class="tc-img"><img src="assets/img/{t['portrait']}" alt="{t['first']} {t['last']}, teacher in {t['city']}" loading="lazy"></div>
        <div class="tc-over">
          <span class="tc-region">{t['region']}</span>
          <h3 class="tc-name serif-display">{t['first']} {t['last']}</h3>
          <div class="tc-cred">DITALS II · {t['city']}</div>
          <span class="tc-more">Read the profile</span>
        </div>
      </a>"""
    fold4 = f"""
<section class="section-cream" id="faculty">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The seven</span>
      <h2 class="serif-display">The Club Italia faculty</h2>
      <p class="lead">Click a teacher to read their region, their teaching manifesto, and their open cohorts for October.</p>
    </div>
    <div class="teachers-grid teachers-grid-7">{cards}
    </div>
  </div>
</section>
"""
    fold5 = """
<section class="section-verona">
  <div class="wrap center">
    <div class="pullquote-band pullquote-band-lg">
      <blockquote class="serif-display quote-xl"><em>To be taught Italian by someone who lives it is not a detail.<br>It is the whole method.</em></blockquote>
      <div class="quote-attr quote-attr-light">Founding principle · Club Italia</div>
    </div>
  </div>
</section>
"""
    fold6 = """
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">By region</span>
      <h2 class="serif-display">North, centre and south of the peninsula</h2>
      <p class="lead">The faculty is deliberately distributed across Italy. A student who studies with us for a full year hears the language from three different Italian rooms.</p>
    </div>
    <div class="region-grid">
      <div class="region-col">
        <h3 class="serif-display">North</h3>
        <ul class="region-list">
          <li><a href="pages/teachers/alessandro.html">Alessandro Ferri</a> · Milano · Lombardia</li>
          <li><a href="pages/teachers/francesca.html">Francesca Zeno</a> · Venezia · Veneto</li>
          <li><a href="pages/teachers/giulia.html">Giulia Moretti</a> · Bologna · Emilia-Romagna</li>
        </ul>
      </div>
      <div class="region-col">
        <h3 class="serif-display">Centre</h3>
        <ul class="region-list">
          <li><a href="pages/teachers/chiara.html">Chiara Bellini</a> · Firenze · Toscana</li>
          <li><a href="pages/teachers/marco.html">Marco Rinaldi</a> · Roma · Lazio</li>
        </ul>
      </div>
      <div class="region-col">
        <h3 class="serif-display">South and islands</h3>
        <ul class="region-list">
          <li><a href="pages/teachers/luca.html">Luca De Simone</a> · Napoli · Campania</li>
          <li><a href="pages/teachers/sofia.html">Sofia Mazzara</a> · Palermo · Sicilia</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""
    testis = [
        {"n":"Diane Whitfield","loc":"Portland, Oregon","img":"assets/img/student-diane.jpg","t":"A whole faculty, not a marketplace","b":"I have studied with three of the seven teachers now. Every one felt like the same school. That consistency is why I have stayed."},
        {"n":"Robert Marconi","loc":"Boston, Massachusetts","img":"assets/img/student-robert.jpg","t":"The rooms are real","b":"You can see the city behind every teacher on the camera. That is not a small thing. It is why the class feels like a class in Italy."},
        {"n":"Sarah Levine","loc":"Brooklyn, New York","img":"assets/img/student-sarah.jpg","t":"They know my name","b":"I switched teachers between levels and both of them had already read my file. That has never happened to me at another school."},
        {"n":"James O'Sullivan","loc":"Dublin, Ireland","img":"assets/img/student-james.jpg","t":"Small enough to be a school","b":"Seven teachers, six thousand students. Somehow it still feels small. My teacher answers me in one working day, every time."},
        {"n":"Linda Cavalli","loc":"San Diego, California","img":"assets/img/student-linda.jpg","t":"Grandmother, granddaughter, both learning","b":"My daughter and I have been through the ladder together. Two different teachers, two very different rooms, one very consistent school."},
        {"n":"Michael Feld","loc":"Tel Aviv, Israel","img":"assets/img/student-michael.jpg","t":"An adult school for adult learners","b":"I have taken a lot of language classes over the years. This is the first one that treated me like a working adult with limited time."},
    ]
    fold7 = tp_wall(testis).replace("What students actually say", "What our students say about the faculty")
    fold8 = final_cta_verona("Meet the teacher who will teach you.", "Every enrolment starts with a fifteen minute conversation with one of our academic advisors. We match you to the teacher who fits.", "Talk to an Advisor")

    body = hero + fold2 + fold3 + fold4 + fold5 + fold6 + fold7 + fold8
    (ROOT/"teachers.html").write_text(page(
        "Club Italia · The Faculty · Seven native Italian teachers from seven cities",
        "Meet the seven native teachers of Club Italia. Chiara, Marco, Giulia, Alessandro, Francesca, Luca and Sofia. Live from Firenze, Roma, Bologna, Milano, Venezia, Napoli and Palermo.",
        body))
    print("wrote teachers.html")


# ============================================================
# BIAGIO.HTML — 11 folds
# ============================================================
def build_biagio():
    hero = """
<section class="section-ink hero-biagio hero-100">
  <div class="hero-bg-gradient hero-bg-verona"></div>
  <div class="wrap hero-biagio-grid">
    <div class="hero-biagio-left">
      <span class="eyebrow eyebrow-gold">Your Italian coach</span>
      <h1 class="serif-display hero-h1">Meet Biagio,<br><em>your Italian coach</em></h1>
      <p class="lead">Biagio lives in the corner of your class. He is trained on the Club Italia syllabus, on the Italian your teacher is teaching this month, and on the mistakes adult English speakers actually make. He is available at three in the afternoon and at three in the morning.</p>
      <div class="cta-row">
        <a class="btn btn-primary btn-lg" href="#biagio-demo">Try Biagio now</a>
        <button class="btn btn-ghost btn-lg" data-advisor type="button">Talk to an Advisor</button>
      </div>
    </div>
    <div class="hero-biagio-right">
      <div class="biagio-glow"></div>
      <img src="assets/img/biagio.png" alt="Biagio, the Club Italia Italian coach" class="biagio-portrait">
    </div>
  </div>
</section>
"""
    fold2 = """
<section class="section-verona">
  <div class="wrap center">
    <div class="pullquote-band pullquote-band-lg">
      <blockquote class="serif-display quote-xl"><em>Biagio is not a chatbot with an Italian filter.<br>He is a coach who has been in every one of your classes.</em></blockquote>
      <div class="quote-attr quote-attr-light">Head of AI · eTeacher Group</div>
    </div>
  </div>
</section>
"""
    pillars = [
        ("01","Conversation","Real dialogue at your level. Biagio speaks a little above where you are, on purpose. That is how the level moves."),
        ("02","Correction","Every message you write in Italian is quietly corrected. Nothing is red pen. Every fix is offered with a reason."),
        ("03","Pronunciation","Speak into Biagio, hear yourself back next to a native reading of the same sentence. Fifteen seconds of practice at a time."),
        ("04","Vocabulary","Words you meet in class come back in Biagio's conversation the same week. Spaced, natural, never as a flashcard."),
        ("05","Culture","Ask about a film, a recipe, a piazza. Biagio knows the Italy your teacher is showing you and adds to it, in Italian if you want."),
        ("06","Homework help","Stuck at eleven at night on a sentence for tomorrow's class. Biagio walks you through it. He does not do it for you."),
    ]
    plist = "".join(f'<article class="pillar-tile"><div class="pillar-num">{n}</div><h3>{t}</h3><p>{d}</p></article>' for n,t,d in pillars)
    fold3 = f"""
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What Biagio does</span>
      <h2 class="serif-display">Six things, done well</h2>
      <p class="lead">Biagio is deliberately narrow. He is a coach for the Club Italia course you are inside. He does not try to be everything.</p>
    </div>
    <div class="pillar-worlds pillar-worlds-6">{plist}
    </div>
  </div>
</section>
"""
    fold4 = """
<section class="section-ink section-biagio-demo" id="biagio-demo">
  <div class="wrap">
    <div class="section-head section-head-light">
      <span class="eyebrow eyebrow-gold">Try Biagio</span>
      <h2 class="serif-display">Say something in Italian</h2>
      <p class="lead lead-light">This is the real Biagio, running the Club Italia model. Try a sentence in Italian, or type in English and ask him to teach you the Italian for it.</p>
    </div>
    <div class="biagio-chat-panel">
      <div class="biagio-chat-head">
        <img src="assets/img/biagio.png" alt="Biagio" class="biagio-chat-avatar">
        <div><div class="biagio-chat-name">Biagio</div><div class="biagio-chat-status">Online · from Club Italia</div></div>
      </div>
      <div class="biagio-chat-msgs" id="biagio-chat-msgs">
        <div class="bmsg bmsg-in"><p>Ciao. Sono Biagio. Puoi scrivere in italiano o in inglese. Iniziamo con una domanda semplice, va bene?</p></div>
      </div>
      <form class="biagio-chat-form" id="biagio-chat-form" autocomplete="off">
        <input type="text" name="q" placeholder="Type your message in Italian or English" aria-label="Your message" required>
        <button class="btn btn-primary" type="submit">Send</button>
      </form>
    </div>
  </div>
</section>
"""
    fold5 = """
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">How Biagio corrects</span>
      <h2 class="serif-display">Three real corrections, in three registers</h2>
    </div>
    <div class="dialog-grid">
      <div class="dialog-col">
        <div class="dialog-tag">The gentle one</div>
        <p class="dialog-you"><strong>You wrote:</strong> <em>Ieri io ho andato al mercato.</em></p>
        <p class="dialog-b"><strong>Biagio:</strong> Vicino. Con il verbo <em>andare</em> l'ausiliare è <em>essere</em>, non <em>avere</em>. Quindi: <em>Ieri sono andato al mercato</em>. Piccola cosa, grande frequenza. La rivedremo.</p>
      </div>
      <div class="dialog-col">
        <div class="dialog-tag">The teaching one</div>
        <p class="dialog-you"><strong>You wrote:</strong> <em>La ragazza che sto parlando è simpatica.</em></p>
        <p class="dialog-b"><strong>Biagio:</strong> La struttura in italiano vuole <em>con cui</em>: <em>La ragazza con cui sto parlando è simpatica</em>. Il pronome relativo <em>che</em> non regge la preposizione. Ne parliamo dopo con un esempio in più?</p>
      </div>
      <div class="dialog-col">
        <div class="dialog-tag">The cultural one</div>
        <p class="dialog-you"><strong>You wrote:</strong> <em>Voglio un caffè grande, per favore.</em></p>
        <p class="dialog-b"><strong>Biagio:</strong> Corretto grammaticalmente. Culturalmente, al bar in Italia il caffè è piccolo, e si chiama semplicemente <em>un caffè</em>. Se vuoi qualcosa di più lungo, prova <em>un caffè lungo</em> o <em>un americano</em>.</p>
      </div>
    </div>
  </div>
</section>
"""
    culture_tiles = [
        ("Calcio","pillar-tradition.jpg","From the Serie A talk on Monday morning to how a Roman argues about the derby."),
        ("Cinema","pillar-cinema.jpg","Sorrentino, Rohrwacher, Garrone. The Italian your favourite director actually writes."),
        ("Cucina","pillar-food.jpg","The vocabulary of a home kitchen, a trattoria menu, a market conversation in Bologna."),
        ("Opera","pillar-opera.jpg","The compressed, elevated Italian of a libretto, and why it teaches you ordinary Italian faster."),
        ("Arte","pillar-art.jpg","Renaissance Italian, gallery Italian, the language you meet in every wall label in Florence."),
        ("Politica","pillar-tradition.jpg","How to read La Repubblica or Il Corriere without a dictionary open in the other tab."),
    ]
    ctiles = "".join(f'<article class="culture-tile" style="background-image:linear-gradient(180deg,rgba(11,11,13,0) 40%,rgba(11,11,13,.85)),url(assets/img/{img})"><h3>{n}</h3><p>{d}</p></article>' for n,img,d in culture_tiles)
    fold6 = f"""
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Cultural range</span>
      <h2 class="serif-display">Biagio knows the Italy you came for</h2>
    </div>
    <div class="culture-grid">{ctiles}
    </div>
  </div>
</section>
"""
    fold7 = """
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head-split">
      <div>
        <span class="eyebrow">Voice and pronunciation</span>
        <h2 class="serif-display">Speak into Biagio,<br>hear yourself against a native</h2>
      </div>
    </div>
    <div class="two-col-list">
      <div class="wave-frame">
        <svg viewBox="0 0 400 120" width="100%" height="120" aria-hidden="true">
          <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="2">
            <line x1="10" y1="60" x2="10" y2="60"/>
            <line x1="25" y1="45" x2="25" y2="75"/>
            <line x1="40" y1="30" x2="40" y2="90"/>
            <line x1="55" y1="20" x2="55" y2="100"/>
            <line x1="70" y1="35" x2="70" y2="85"/>
            <line x1="85" y1="50" x2="85" y2="70"/>
            <line x1="100" y1="25" x2="100" y2="95"/>
            <line x1="115" y1="40" x2="115" y2="80"/>
            <line x1="130" y1="55" x2="130" y2="65"/>
            <line x1="145" y1="30" x2="145" y2="90"/>
            <line x1="160" y1="20" x2="160" y2="100"/>
            <line x1="175" y1="45" x2="175" y2="75"/>
            <line x1="190" y1="35" x2="190" y2="85"/>
            <line x1="205" y1="50" x2="205" y2="70"/>
            <line x1="220" y1="25" x2="220" y2="95"/>
            <line x1="235" y1="40" x2="235" y2="80"/>
            <line x1="250" y1="30" x2="250" y2="90"/>
            <line x1="265" y1="45" x2="265" y2="75"/>
            <line x1="280" y1="55" x2="280" y2="65"/>
            <line x1="295" y1="35" x2="295" y2="85"/>
            <line x1="310" y1="50" x2="310" y2="70"/>
            <line x1="325" y1="30" x2="325" y2="90"/>
            <line x1="340" y1="45" x2="340" y2="75"/>
            <line x1="355" y1="55" x2="355" y2="65"/>
            <line x1="370" y1="50" x2="370" y2="70"/>
            <line x1="385" y1="60" x2="385" y2="60"/>
          </g>
        </svg>
        <div class="wave-caption">Your voice · Ieri sono andato al mercato di Bologna</div>
      </div>
      <div class="cred-side">
        <p>Biagio's pronunciation coach records your voice, aligns it against a native reading of the same sentence, and shows you where the stress and the vowels drifted. Fifteen seconds at a time. Twelve times a week is more than most students do in a year of self study.</p>
        <p class="lead">This is the feature students use most. It is the one they mention most in year end reviews.</p>
      </div>
    </div>
  </div>
</section>
"""
    quadrant = [
        ("Corrects","Every message you write in Italian is corrected quietly. Never red pen. Always a reason."),
        ("Extends","Every conversation lifts one register above where you are. That is where growth lives."),
        ("Remembers","Biagio holds a private note on the vocabulary you meet in class, and reintroduces it a week later."),
        ("Refuses","Biagio refuses to do the homework for you. He asks you three questions instead, and lets you find the sentence."),
    ]
    qgrid = "".join(f'<div class="quad-cell"><h3>{h}</h3><p>{p}</p></div>' for h,p in quadrant)
    fold8 = f"""
<section class="section-ink">
  <div class="wrap">
    <div class="section-head section-head-light">
      <span class="eyebrow eyebrow-gold">Biagio's method</span>
      <h2 class="serif-display">A coach, not a search box</h2>
    </div>
    <div class="quad-grid">{qgrid}
    </div>
  </div>
</section>
"""
    when = [
        ("Before class","Warm up your Italian in five minutes with a short conversation about the day's topic."),
        ("After class","Debrief with Biagio. What did you learn. What did you almost learn. What is worth reviewing tonight."),
        ("Between classes","One quiet fifteen minute session, midweek. Enough to keep the language warm without adding a real study session."),
        ("At three in the morning","When it hits you that you have no idea how the passato prossimo actually works, Biagio is awake."),
    ]
    wgrid = "".join(f'<article class="when-card"><h3>{h}</h3><p>{p}</p></article>' for h,p in when)
    fold9 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">When Biagio helps</span>
      <h2 class="serif-display">The times of day this coach is worth having</h2>
    </div>
    <div class="when-grid">{wgrid}
    </div>
  </div>
</section>
"""
    faqs = [
        ("Is Biagio really artificial intelligence, or is a human answering?","Biagio is a language model, trained and tuned by our team on the Club Italia syllabus. No human replies to your messages. Your teacher, however, is a real person, and any teacher matter goes to a human by email or in class."),
        ("Does using Biagio replace a live class?","No. Biagio is designed as a coach between classes. The live class remains the spine of the course. Biagio makes the days in between more productive."),
        ("What languages does Biagio speak?","Italian and English, at the register of an experienced adult teacher. He will not refuse to switch to English when you need him to."),
        ("Can I use Biagio without being a Club Italia student?","No. Biagio is available only to enrolled students. He is not a general product."),
        ("Does Biagio see my class notes and homework?","Only the material you choose to share with him inside the chat. Biagio does not read your teacher's private notes and does not report anything you write back to your teacher."),
    ]
    fitems = "".join(f'<details class="faq-item"><summary><span>{q}</span><span class="faq-plus" aria-hidden="true">+</span></summary><div class="faq-a"><p>{a}</p></div></details>' for q,a in faqs)
    fold10 = f"""
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Biagio · common questions</span>
      <h2 class="serif-display">Five questions students ask on day one</h2>
    </div>
    <div class="faq-list">{fitems}
    </div>
  </div>
</section>
"""
    fold11 = final_cta_verona("Meet Biagio in your first class.", "Every Club Italia enrolment includes Biagio, at no extra cost, from day one. Talk to an advisor to open your seat.", "Talk to an Advisor")
    body = hero + fold2 + fold3 + fold4 + fold5 + fold6 + fold7 + fold8 + fold9 + fold10 + fold11
    (ROOT/"biagio.html").write_text(page(
        "Biagio · Your Italian coach · Club Italia AI tutor",
        "Biagio is the Club Italia Italian coach. Trained on your syllabus. Corrects your writing. Rehearses your speaking. Available at three in the afternoon and three in the morning.",
        body))
    print("wrote biagio.html")


# ============================================================
# HOW-IT-WORKS.HTML — 10 folds
# ============================================================
def build_how():
    hero = """
<section class="section-ink hero-page hero-100">
  <div class="hero-bg">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/img/hero-italian-life.jpg">
      <source src="assets/video/roma-piazza.mp4" type="video/mp4">
    </video>
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">How it works</span>
    <h1 class="serif-display hero-h1">From ciao <em>to certificate</em></h1>
    <p class="lead">The path is deliberate. Four levels, from a first word of Italian to a certificate at CEFR B1. Live weekly classes with the same teacher across a level. A cultural syllabus, not a syllabus of forms.</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">Talk to an Advisor</button>
      <a class="btn btn-ghost btn-lg" href="courses.html">See the courses</a>
    </div>
  </div>
</section>
"""
    fold2 = stats_strip("dark")
    fold3 = """
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The ladder</span>
      <h2 class="serif-display">Where the course begins,<br>and where it ends</h2>
      <p class="lead">The whole Club Italia course ladder is CEFR aligned. Your entry point is decided in your first advisor call and confirmed by a placement conversation with a teacher, not a form.</p>
    </div>
    <div class="cefr-ladder">
      <div class="cefr-step"><div class="cefr-code">A0</div><h3>No Italian yet</h3><p>You start here if buongiorno is the whole vocabulary. First class is a real class, not a demo.</p></div>
      <div class="cefr-step"><div class="cefr-code">A1</div><h3>First real sentences</h3><p>Present tense across the everyday verbs. Enough Italian to hold a slow conversation with a patient adult.</p></div>
      <div class="cefr-step"><div class="cefr-code">A2</div><h3>Life in Italian</h3><p>Past and future. Full sentences with clauses. A conversation with a stranger at a market, without English behind it.</p></div>
      <div class="cefr-step"><div class="cefr-code">B1</div><h3>Independent user</h3><p>The CEFR B1 milestone. Reading a newspaper, holding a working conversation, writing an email that reads as adult Italian.</p></div>
    </div>
  </div>
</section>
"""
    tracks = [
        ("Structured","CI · Corsi di Italiano","The main ladder. Four levels, thirty two lessons per level, one teacher across a level. This is the spine.","courses.html"),
        ("Spoken","PS · Parliamo Series","Four themed conversation courses. A Tavola, Al Caffè, Chiacchierando, In Viaggio. Speaking-only, no grammar drilling.","courses.html"),
        ("Cultural","Capsules","Six week thematic capsules. L'Arte, La Cucina, L'Opera. Culture taught as language, at the level you are already at.","capsules.html"),
    ]
    tgrid = "".join(f'<a class="track-card" href="{href}"><div class="track-eyebrow">{a}</div><h3 class="serif-display">{b}</h3><p>{c}</p><span class="track-more">See these courses</span></a>' for a,b,c,href in tracks)
    fold4 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Three tracks</span>
      <h2 class="serif-display">One school, three ways to learn</h2>
      <p class="lead">Most Club Italia students combine two tracks. Structured for the spine of the year. Spoken or Capsules for texture.</p>
    </div>
    <div class="tracks-grid">{tgrid}
    </div>
  </div>
</section>
"""
    steps = [
        ("01","Talk to an advisor","A fifteen minute call with a human. We ask about your Italian, your reasons and your time. We do not push. We match you to the right teacher and cohort.","env-marco-desk.jpg"),
        ("02","Placement conversation","A short call in Italian with the teacher we matched you to. This confirms the level. No test paper. No score.","env-chiara-desk.jpg"),
        ("03","First live class","Your first class is a real class. Twelve adults, one native teacher, eighty five minutes on Zoom, live from Italy.","zoom-classroom-chiara.jpg"),
        ("04","A week of Italian","One live class in the diary. One quiet review with Biagio. One short piece of homework. Around three and a half hours a week, total.","env-giulia-kitchen.jpg"),
        ("05","Level up","Eight to ten months at your level, then the transition. Same school, next teacher up the ladder. The certificate arrives at the top."," zoom-hero-composite.jpg".strip()),
    ]
    sgrid = ""
    for n,h,p,img in steps:
        sgrid += f"""
      <article class="step-card">
        <div class="step-img"><img src="assets/img/{img}" alt="{h}" loading="lazy"></div>
        <div class="step-body"><div class="step-num">{n}</div><h3 class="serif-display">{h}</h3><p>{p}</p></div>
      </article>"""
    fold5 = f"""
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The five step journey</span>
      <h2 class="serif-display">What actually happens, in order</h2>
    </div>
    <div class="steps-vertical">{sgrid}
    </div>
  </div>
</section>
"""
    week = [
        ("Mon","Live class","Eighty five minutes with your teacher. This is the spine of the week. Nothing else is required."),
        ("Wed","Quiet review","Twenty minutes with Biagio, reviewing the new material. Not a test. A conversation."),
        ("Fri","Real material","One short reading, one short recording, one written reply. Total: fifty minutes."),
        ("Weekend","Culture","One Italian film, one Italian recipe, one Italian song. Optional. Enjoyable. Effective."),
    ]
    wgrid = "".join(f'<article class="week-card"><div class="week-day">{d}</div><h3>{h}</h3><p>{p}</p></article>' for d,h,p in week)
    fold6 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">A week at Club Italia</span>
      <h2 class="serif-display">Three and a half hours,<br>evenly distributed</h2>
    </div>
    <div class="week-grid">{wgrid}
    </div>
  </div>
</section>
"""
    fold7 = """
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Inside the class</span>
      <h2 class="serif-display">The eighty five minute session</h2>
    </div>
    <div class="phase-grid session-detail">
      <div class="phase-col"><div class="phase-num">01</div><h3>Learning goals</h3><ul class="phase-list">
        <li>One grammar point named at the top</li>
        <li>Ten to fifteen items of new vocabulary</li>
        <li>One conversational function to practise</li>
        <li>A short cultural note</li>
        <li>One named piece of homework</li></ul></div>
      <div class="phase-col"><div class="phase-num">02</div><h3>The eighty five minute flow</h3><ul class="phase-list">
        <li>0 to 10 warm up in Italian</li>
        <li>10 to 25 new material introduced live</li>
        <li>25 to 45 breakout practice in pairs</li>
        <li>45 to 55 break, teacher stays online</li>
        <li>55 to 75 free conversation on the theme</li>
        <li>75 to 85 review and homework</li></ul></div>
      <div class="phase-col"><div class="phase-num">03</div><h3>Between lesson work</h3><ul class="phase-list">
        <li>A short reading, real Italian source</li>
        <li>An audio under three minutes</li>
        <li>A written reply, no more than 120 words</li>
        <li>Optional quiet time with Biagio</li>
        <li>Ninety to a hundred minutes total</li></ul></div>
    </div>
  </div>
</section>
"""
    fold8 = """
<section class="section-ink">
  <div class="wrap">
    <div class="section-head section-head-light">
      <span class="eyebrow eyebrow-gold">A real Club Italia classroom</span>
      <h2 class="serif-display">This is what your Wednesday evening looks like</h2>
    </div>
    <div class="zoom-frame">
      <img src="assets/img/zoom-classroom-marco.jpg" alt="A live Club Italia Zoom class with Marco Rinaldi, teaching adults from Roma" loading="lazy">
    </div>
    <p class="figure-cap">Marco Rinaldi, live from Roma, in a real Club Italia CI Principiante class. Ten adults on the screen.</p>
  </div>
</section>
"""
    testis = [
        {"n":"Diane Whitfield","loc":"Portland, Oregon","img":"assets/img/student-diane.jpg","t":"The path is the point","b":"I did not know what CEFR meant a year ago. I still do not talk about it. But the school knew, and it took me from nothing to a certificate that I will use."},
        {"n":"Robert Marconi","loc":"Boston, Massachusetts","img":"assets/img/student-robert.jpg","t":"Small enough to notice you","b":"Twelve adults in a room. My teacher noticed the week I was quieter, and asked why. That has never happened in an online class."},
        {"n":"Sarah Levine","loc":"Brooklyn, New York","img":"assets/img/student-sarah.jpg","t":"Three and a half hours, held","b":"The weekly load is honest. It is what I can give and no more. That is why I have kept going."},
        {"n":"James O'Sullivan","loc":"Dublin, Ireland","img":"assets/img/student-james.jpg","t":"It builds","b":"Every week's lesson uses last week's material. That is such an obvious thing and I have never seen a language course actually do it before."},
        {"n":"Linda Cavalli","loc":"San Diego, California","img":"assets/img/student-linda.jpg","t":"A real school, not a marketplace","b":"There is a head of school. She replies to email. The teachers know each other. That is what I was paying for."},
        {"n":"Michael Feld","loc":"Tel Aviv, Israel","img":"assets/img/student-michael.jpg","t":"Ready for Italy in a year","b":"I started with a trip in mind. I am going in April. My Italian is now what I hoped it would be."},
    ]
    fold9 = tp_wall(testis)
    fold10 = final_cta_verona("Book your placement call.", "A fifteen minute conversation with an academic advisor. We plan a real start, in a real cohort.", "Talk to an Advisor")
    body = hero + fold2 + fold3 + fold4 + fold5 + fold6 + fold7 + fold8 + fold9 + fold10
    (ROOT/"how-it-works.html").write_text(page(
        "How Club Italia works · From first word to CEFR B1",
        "How the Club Italia course works. Four CEFR levels, three tracks, live weekly classes from Italy, small groups of ten to twelve adults.",
        body))
    print("wrote how-it-works.html")


# ============================================================
# METHOD.HTML — 9 folds
# ============================================================
def build_method():
    hero = """
<section class="section-ink hero-page hero-100">
  <div class="hero-bg">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/img/life-uffizi-hall.jpg">
      <source src="assets/video/opera-scala.mp4" type="video/mp4">
    </video>
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">The method</span>
    <h1 class="serif-display hero-h1">A cultural method.<br><em>Not an app</em></h1>
    <p class="lead">Club Italia teaches Italian the way a serious European school teaches a language. Live, small groups, native teachers, a cultural syllabus, and a certificate at the end that means what it says.</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">Talk to an Advisor</button>
      <a class="btn btn-ghost btn-lg" href="how-it-works.html">How the class works</a>
    </div>
  </div>
</section>
"""
    fold2 = """
<section class="section-verona">
  <div class="wrap center">
    <div class="pullquote-band pullquote-band-lg">
      <blockquote class="serif-display quote-xl"><em>A language is not an application.<br>It is a country that gives you a second life.</em></blockquote>
      <div class="quote-attr quote-attr-light">Founding principle · Club Italia</div>
    </div>
  </div>
</section>
"""
    principles = [
        ("Live","No pre recorded video is a class. A class is a room in which a native teacher is with you, in real time, this evening. Everything else is a course product."),
        ("Small","Ten to twelve adults per cohort. Small enough that the teacher hears every voice every week. Not a webinar, not a broadcast."),
        ("Native","Every teacher is Italian, from an Italian city, and teaches from that city. Location is not decoration. It is what makes the language sound like the language."),
        ("Cultural","The syllabus is built around Italian life. Cooking, art, opera, travel, cinema, politics. Grammar is delivered inside these frames, not before them."),
    ]
    pgrid = "".join(f'<article class="principle-card"><h3 class="serif-display">{h}</h3><p>{p}</p></article>' for h,p in principles)
    fold3 = f"""
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Four principles</span>
      <h2 class="serif-display">What the method commits to</h2>
    </div>
    <div class="principle-grid">{pgrid}
    </div>
  </div>
</section>
"""
    quad = [
        ("Read","Every week you read a short piece of real Italian. Newspaper, essay, recipe, review. Not a graded text with the difficulty removed."),
        ("Listen","One recording under three minutes. A conversation, an interview, a piece of radio. You listen twice."),
        ("Speak","Half of every live class is spent speaking. Not to the teacher. To another adult in the room, in breakout, on the day's theme."),
        ("Write","One short reply a week, no longer than 120 words. Written to a person, not to the exercise. Corrected in full by the teacher."),
    ]
    qgrid = "".join(f'<article class="quad-cell"><h3>{h}</h3><p>{p}</p></article>' for h,p in quad)
    fold4 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The action oriented method</span>
      <h2 class="serif-display">Four things a student does every week</h2>
      <p class="lead">The method is not a theory. It is a weekly routine. Four verbs, one per column, every week for eight months.</p>
    </div>
    <div class="quad-grid">{qgrid}
    </div>
  </div>
</section>
"""
    fold5 = """
<section class="section-ink">
  <div class="wrap">
    <div class="section-head section-head-light">
      <span class="eyebrow eyebrow-gold">Where the method comes from</span>
      <h2 class="serif-display">The credentials behind the syllabus</h2>
    </div>
    <div class="credibility-strip">
      <div class="cred-block"><h3>CEFR Companion Volume</h3><p>Council of Europe · 2020. The current European reference for language teaching. Our four level ladder maps to it exactly.</p></div>
      <div class="cred-block"><h3>The Action Oriented Approach</h3><p>Piccardo and North · 2019. The current European framework for language teaching. Our weekly cycle of reading, listening, speaking, writing is built on it.</p></div>
      <div class="cred-block"><h3>Applied linguistics training</h3><p>Università per Stranieri di Perugia and Università per Stranieri di Siena. Every teacher on our faculty is qualified through one of these two Italian institutions.</p></div>
    </div>
  </div>
</section>
"""
    pillars = [
        ("Arte","pillar-art.jpg"),("Cucina","pillar-food.jpg"),
        ("Viaggio","pillar-travel.jpg"),("Cinema","pillar-cinema.jpg"),
        ("Opera","pillar-opera.jpg"),("Tradizione","pillar-tradition.jpg"),
    ]
    ptiles = "".join(f'<article class="culture-tile" style="background-image:linear-gradient(180deg,rgba(11,11,13,0) 40%,rgba(11,11,13,.85)),url(assets/img/{img})"><h3>{n}</h3></article>' for n,img in pillars)
    fold6 = f"""
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Six cultural pillars</span>
      <h2 class="serif-display">The frame the syllabus is built on</h2>
      <p class="lead">Every course, every level, every capsule is designed around one or more of these six. Grammar is a subordinate structure. Culture is the syllabus.</p>
    </div>
    <div class="culture-grid">{ptiles}
    </div>
    <div class="center" style="margin-top:2.4rem">
      <a class="btn btn-ghost-dark btn-lg" href="culture.html">Read about the cultural syllabus</a>
    </div>
  </div>
</section>
"""
    fold7 = """
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">A real class</span>
      <h2 class="serif-display">The method, inside a Wednesday evening</h2>
    </div>
    <div class="zoom-frame">
      <img src="assets/img/zoom-classroom-chiara.jpg" alt="Live Club Italia class with Chiara Bellini from Firenze" loading="lazy">
    </div>
    <p class="figure-cap">Chiara Bellini teaching from Firenze. Eleven adults on the screen. Eighty five minutes.</p>
  </div>
</section>
"""
    fold8 = """
<section class="section-olive">
  <div class="wrap center">
    <div class="pullquote-band pullquote-band-lg">
      <blockquote class="serif-display quote-xl"><em>Culture is the syllabus.<br>Grammar is the scaffolding you take down at the end.</em></blockquote>
      <div class="quote-attr quote-attr-light">Head of School · Club Italia</div>
    </div>
  </div>
</section>
"""
    fold9 = final_cta_verona("Study the method by living inside it.", "Book a first class and see the method in the room. Fifteen minutes with an advisor is enough to plan it.", "Talk to an Advisor")
    body = hero + fold2 + fold3 + fold4 + fold5 + fold6 + fold7 + fold8 + fold9
    (ROOT/"method.html").write_text(page(
        "The Club Italia method · A cultural method, live and small",
        "The Club Italia method. Live classes, native teachers, a cultural syllabus, action oriented weekly routine. CEFR aligned. Rooted in Italian university teaching.",
        body))
    print("wrote method.html")


# ============================================================
# CULTURE.HTML — 8 folds
# ============================================================
def build_culture():
    hero = """
<section class="section-ink hero-page hero-100">
  <div class="hero-bg">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/img/life-uffizi-hall.jpg">
      <source src="assets/video/opera-scala.mp4" type="video/mp4">
    </video>
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">Cultura</span>
    <h1 class="serif-display hero-h1">Cultura parla italiano.<br><em>Anche tu?</em></h1>
    <p class="lead">Italian is not a bag of grammar rules. It is a country. Six cultural chapters organise our whole syllabus. This page is a tour of them, in the order a Club Italia student meets them.</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">Talk to an Advisor</button>
      <a class="btn btn-ghost btn-lg" href="capsules.html">See the Culture Capsules</a>
    </div>
  </div>
</section>
"""
    fold2 = """
<section class="section-paper">
  <div class="wrap">
    <div class="editorial-2col">
      <div class="col-essay">
        <span class="eyebrow">Culture is the syllabus</span>
        <h2 class="serif-display">A syllabus that begins with Italian life, not with the verb tables</h2>
      </div>
      <div class="col-essay">
        <p>Most language teaching begins with the language and then, if it has time, adds a little culture at the edges. We begin the other way around. Our syllabus is built out of six chapters of Italian cultural life. Each chapter carries a specific band of vocabulary and grammar, and the class enters those grammar points through the culture, not the other way around.</p>
        <p>This is not a small pedagogical choice. It changes what students walk out with. They walk out with Italian anchored to something they care about, and that Italian survives the eighteen months after the course ends. That is the ambition. Not a certificate on a shelf. An Italian that lives on in the student's ordinary week.</p>
      </div>
    </div>
  </div>
</section>
"""
    chapters = [
        ("Arte","pillar-art.jpg","01","The Italian of the wall label, the gallery guide and the Renaissance essay. Students learn to read the language of Florence in Florence's own tongue. Grammar band: descriptive present, imperfect, subordinate clauses. Cultural anchor: three centuries of painting from Giotto to Caravaggio, taught by Chiara from Firenze."),
        ("Cucina","pillar-food.jpg","02","The Italian of the market, the family kitchen, and the trattoria menu. The most concrete adult vocabulary in the language, taught by Giulia from her Bolognese kitchen. Grammar band: imperative, quantities, procedural sequence. Cultural anchor: regional Italian cooking, from ragù bolognese to pasta alla Norma."),
        ("Viaggio","pillar-travel.jpg","03","The Italian of the trip you are actually planning. Practical, oral, situational. Taught by Francesca from Venezia, with rehearsals of arrivals, hotels, restaurants, small talk with strangers, awkward middle days. Grammar band: modal verbs, polite forms, spatial prepositions."),
        ("Cinema","pillar-cinema.jpg","04","Modern Italian at the pace it is actually spoken. Sorrentino, Rohrwacher, Garrone. Learners meet the language as it lives in a contemporary Italian film script, with all the elision, register shift and slang that involves. Grammar band: idiomatic constructions, subjunctive in real speech."),
        ("Opera & Musica","pillar-opera.jpg","05","Compressed, elevated, sung Italian. A single line of Puccini teaches more about vowels and stress than a week of drills. Taught by Alessandro from Milano, formerly of the La Scala summer academy. Grammar band: word order, poetic register, high vocabulary."),
        ("Tradizione","pillar-tradition.jpg","06","The Italy that is not in a museum. Festa della Repubblica, Carnevale, the Palio di Siena, the way a family Sunday actually works. Taught in rotation across the faculty. Grammar band: narrative past, cultural register, formal versus familiar."),
    ]
    chaps = ""
    for i,(name,img,num,body) in enumerate(chapters):
        left_img = i % 2 == 0
        chaps += f"""
    <article class="chapter-row {'chapter-left' if left_img else 'chapter-right'}">
      <figure class="chapter-fig"><img src="assets/img/{img}" alt="{name}" loading="lazy"></figure>
      <div class="chapter-body">
        <div class="chapter-num">{num}</div>
        <h3 class="serif-display">{name}</h3>
        <p>{body}</p>
      </div>
    </article>
"""
    fold3 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Six chapters</span>
      <h2 class="serif-display">The cultural syllabus, in the order a student meets it</h2>
    </div>
    <div class="chapter-stack">{chaps}
    </div>
  </div>
</section>
"""
    fold4 = """
<section class="section-verona">
  <div class="wrap center">
    <div class="pullquote-band pullquote-band-lg">
      <blockquote class="serif-display quote-xl"><em>An Italian who has never seen a Fellini film<br>speaks the same Italian as one who has.<br>You will not.</em></blockquote>
      <div class="quote-attr quote-attr-light">Faculty note · Club Italia</div>
    </div>
  </div>
</section>
"""
    lib = [
        ("Books","Ferrante · L'amica geniale","Pavese · La luna e i falò","Ginzburg · Lessico famigliare","Calvino · Marcovaldo","Sciascia · Il giorno della civetta"),
        ("Films","Rohrwacher · La chimera","Sorrentino · La grande bellezza","Garrone · Il racconto dei racconti","Moretti · Caro diario","Fellini · Amarcord"),
        ("Podcasts","Morning · Il Post","Storie di Roma · Rai","Ci vuole una scienza · Il Post","Cinema Italiano · storia","Radio 3 Suite · Rai"),
    ]
    lgrid = ""
    for kind, *items in lib:
        li = "".join(f"<li>{x}</li>" for x in items)
        lgrid += f'<div class="lib-col"><h3 class="serif-display">{kind}</h3><ul>{li}</ul></div>'
    fold5 = f"""
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Cultural library</span>
      <h2 class="serif-display">What our faculty asks students to read, watch and listen to</h2>
      <p class="lead">Not required. Curated. Every enrolled student gets the full library, updated each term by the faculty.</p>
    </div>
    <div class="lib-grid">{lgrid}
    </div>
  </div>
</section>
"""
    caps = [
        ("La Cucina","cap-food.jpg","Six weeks in the language of the Italian kitchen. Taught by Giulia from Bologna.","pages/culture/cap-food.html"),
        ("L'Arte","cap-art.jpg","Six weeks in the language of Italian art. Taught by Chiara from Firenze.","pages/culture/cap-art.html"),
        ("L'Opera","cap-opera.jpg","Six weeks in the language of Italian opera. Taught by Alessandro from Milano.","pages/culture/cap-opera.html"),
    ]
    cgrid = "".join(f'<a class="cap-card" href="{href}"><figure><img src="assets/img/{img}" alt="{n}" loading="lazy"></figure><div class="cap-body"><h3 class="serif-display">{n}</h3><p>{d}</p><span class="cap-more">See the capsule</span></div></a>' for n,img,d,href in caps)
    fold6 = f"""
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">A door into a chapter</span>
      <h2 class="serif-display">Culture Capsules · six weeks each</h2>
      <p class="lead">The capsules are for students already on the ladder, and for adults who want to try Club Italia inside one specific cultural theme.</p>
    </div>
    <div class="cap-grid">{cgrid}
    </div>
  </div>
</section>
"""
    fold7 = """
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Inside a culture class</span>
      <h2 class="serif-display">A live cultural session, on Wednesday evening</h2>
    </div>
    <div class="zoom-frame">
      <img src="assets/img/zoom-classroom-chiara.jpg" alt="Live Club Italia culture class from Firenze" loading="lazy">
    </div>
    <p class="figure-cap">Chiara Bellini teaching a Capsule L'Arte session on Piero della Francesca. Twelve adults on screen.</p>
  </div>
</section>
"""
    fold8 = final_cta_verona("Study Italian as an Italian would study it.", "Culture is not an extra with Club Italia. It is the spine. Talk to an advisor and we build a start around the chapters you care most about.", "Talk to an Advisor")
    body = hero + fold2 + fold3 + fold4 + fold5 + fold6 + fold7 + fold8
    (ROOT/"culture.html").write_text(page(
        "Culture · The cultural syllabus of Club Italia",
        "The Club Italia cultural syllabus. Six chapters, from Arte to Tradizione, taught by native teachers from seven Italian cities.",
        body))
    print("wrote culture.html")


if __name__ == "__main__":
    build_teachers_index()
    build_biagio()
    build_how()
    build_method()
    build_culture()
