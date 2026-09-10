#!/usr/bin/env python3
"""Build all secondary pages for Club Italia. Editorial FA-descended density, own Italian brand."""
import os, re
from pathlib import Path

ROOT = Path("/home/user/workspace/club-italia")
NAV = (ROOT/"_partials/nav.html").read_text()
FOOTER = (ROOT/"_partials/footer.html").read_text()

def head(title, desc, prefix=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}css/ci.css?v=v5">
<link rel="icon" type="image/svg+xml" href="{prefix}assets/img/cefr-logo.svg">
</head>
<body class="v5">
"""

def close(prefix=""):
    return f'<script src="{prefix}js/ci.js?v=v5" defer></script>\n</body>\n</html>\n'

def apply_prefix(html, prefix):
    if not prefix:
        return html
    # Replace src="assets, href="assets, href="css, src="js
    html = re.sub(r'(src|href)="(assets/|css/|js/)', rf'\1="{prefix}\2', html)
    # Nav links: href="something.html" (relative, no prefix, no anchor, no http)
    def sub_nav_href(m):
        target = m.group(1)
        if target.startswith(("http", "#", "mailto", "tel", prefix, "/")):
            return m.group(0)
        return f'href="{prefix}{target}"'
    html = re.sub(r'href="([^"]+\.html)"', sub_nav_href, html)
    return html

def page(title, desc, folds_html, prefix=""):
    nav = apply_prefix(NAV, prefix)
    footer = apply_prefix(FOOTER, prefix)
    return head(title, desc, prefix) + nav + folds_html + footer + close(prefix)

# ============================================================
# COMMON FOLDS
# ============================================================

def stats_strip(variant="dark"):
    cls = "section-ink" if variant == "dark" else "section-cream"
    return f"""
<section class="{cls} stats-strip">
  <div class="wrap">
    <div class="stats-grid">
      <div class="stat-cell"><div class="stat-num">25+</div><div class="stat-lbl">years online teaching</div></div>
      <div class="stat-cell"><div class="stat-num">400k</div><div class="stat-lbl">adult learners since 2000</div></div>
      <div class="stat-cell"><div class="stat-num">197</div><div class="stat-lbl">countries served</div></div>
      <div class="stat-cell"><div class="stat-num">6</div><div class="stat-lbl">language faculties</div></div>
      <div class="stat-cell"><div class="stat-num">4.8</div><div class="stat-lbl">Trustpilot average</div></div>
    </div>
  </div>
</section>
"""

def final_cta_verona(headline="Begin in Italian this October.", sub="Small live cohorts. One native teacher per class. A cultural syllabus from Italy.", cta="Talk to an Advisor"):
    return f"""
<section class="section-verona final-cta">
  <div class="wrap center">
    <h2 class="serif-display"><em>{headline}</em></h2>
    <p class="lead">{sub}</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">{cta}</button>
      <a class="btn btn-ghost btn-lg" href="courses.html">See the courses</a>
    </div>
  </div>
</section>
"""

def tp_wall(cards):
    items = ""
    for c in cards:
        items += f"""
      <article class="tp-card">
        <div class="tp-stars" aria-label="5 stars">★★★★★</div>
        <h4 class="tp-title">{c['t']}</h4>
        <p class="tp-body">{c['b']}</p>
        <div class="tp-meta">
          <img class="tp-avatar" src="{c['img']}" alt="{c['n']}" loading="lazy">
          <div><div class="tp-name">{c['n']}</div><div class="tp-loc">{c['loc']}</div></div>
        </div>
      </article>"""
    return f"""
<section class="section-cream tp-section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Reviewed by learners</span>
      <h2 class="serif-display">What students actually say</h2>
    </div>
    <div class="tp-wall">{items}
    </div>
  </div>
</section>
"""

# ------------------------------------------------------------
# TEACHER DATA
# ------------------------------------------------------------
TEACHERS = [
    {
        "slug":"chiara", "first":"Chiara", "last":"Bellini",
        "city":"Firenze", "region":"Toscana", "regionEn":"Tuscany",
        "portrait":"teacher-chiara.jpg", "desk":"env-chiara-desk.jpg",
        "cityImg":"city-firenze.jpg", "lifeImg":"life-trattoria-toscana.jpg",
        "credentials":["DITALS II · Università per Stranieri di Siena","Master FLE · Università di Firenze","CEFR Examiner · A0 through B1","Twelve years teaching adults online"],
        "courses":[("ci2","CI Elementare · A1.1 to A1.2","Small live cohort, twice weekly."),("ps-tavola","Parliamo · A tavola","Speaking through Tuscan food culture."),("cap-arte","Capsule · L'Arte","Six weeks on Renaissance Italian.")],
        "quote":"Firenze taught me that Italian is not a set of rules. It is a way of noticing the light on a wall in November, the smell of a bakery at seven in the morning, a sentence overheard on a bridge. That is what I bring into class.",
        "manifesto":"I teach adults. Adults come with a life already written in another language, and my job is not to erase it. My job is to give them a second interior voice, one that speaks Italian back to them when they are washing dishes or driving home. That is the sign the language has taken root. So I move slowly on the first weeks. I resist the temptation to fill silence. I ask questions I actually want the answer to. When a student in Chicago tells me about her father in ninety careful Italian words, that is a class I remember for a year. Grammar is a bookshelf. Speech is a house you live in. I build the house first, and we add the shelves as we go. My students in Florence, my students in San Francisco and my students in Buenos Aires all get the same me. That consistency is the offer.",
        "essay":"Chiara was born in Fiesole, above Florence, and grew up walking down the hill to school past cypress rows that appear in half the paintings you have already seen. She read literature at Firenze, taught in Barcelona for two years, then came home. Her Italian is standard Tuscan, the source Italian, the one from which the language on television and in newspapers is drawn. Her English is warm and careful and does not compete with the Italian for space in the class."
    },
    {
        "slug":"marco", "first":"Marco", "last":"Rinaldi",
        "city":"Roma", "region":"Lazio", "regionEn":"Lazio",
        "portrait":"teacher-marco.jpg", "desk":"env-marco-desk.jpg",
        "cityImg":"city-roma.jpg", "lifeImg":"life-caffe-roma.jpg",
        "credentials":["DITALS II · Università per Stranieri di Siena","Laurea in Linguistica · Sapienza Roma","CEFR Examiner · A0 through A2","Nine years teaching absolute beginners"],
        "courses":[("ci1","CI Principiante · A0 to A1.1","For learners with no Italian at all."),("ps-caffe","Parliamo · Al caffè","First real conversations, over espresso.")],
        "quote":"A beginner is not a small learner. A beginner is a whole adult who has decided, at forty or sixty, to open a new room in their mind. That deserves respect, and it deserves a slow start.",
        "manifesto":"I love the first class. I love the moment a person who has never spoken Italian says buongiorno back to me and hears their own voice make a sound they did not make yesterday. That is why I only teach beginners. I know how to hold that room. I know how much silence a new speaker needs before they will try, and how much English I need to drop out of the class in month two, and how to write on the shared screen so a person on their sofa in Los Angeles feels they are in a room with me. Rome is a beginner city. Everyone in Rome starts somewhere. I teach as a Roman.",
        "essay":"Marco grew up in the Prati neighbourhood of Rome, five streets from St Peter's, in a family of teachers. He studied linguistics at Sapienza, wrote a thesis on how adults acquire a second phonology, and has taught Italian to adults ever since. He teaches from a study lined with paperbacks and one framed photograph of his grandfather, who was also a Roman teacher."
    },
    {
        "slug":"giulia", "first":"Giulia", "last":"Moretti",
        "city":"Bologna", "region":"Emilia-Romagna", "regionEn":"Emilia-Romagna",
        "portrait":"teacher-giulia.jpg", "desk":"env-giulia-kitchen.jpg",
        "cityImg":"city-bologna.jpg", "lifeImg":"life-market-bologna.jpg",
        "credentials":["DITALS II · Università per Stranieri di Siena","Specialisation in food language and gastronomic Italian","CEFR Examiner · A1 through B1","Eleven years teaching intermediate adults"],
        "courses":[("ci3","CI Intermedio · A1.2 to A2.1","The bridge from tourist Italian to real conversation."),("cap-cucina","Capsule · La Cucina","Six weeks in the language of Italian cooking.")],
        "quote":"Bologna is a city that feeds you and then asks you what you thought of it. My classes are like that. I feed you a piece of Italian, then I want to know what you noticed.",
        "manifesto":"The intermediate stage is the honest stage. The tourist phrases are behind you, the certificate is far ahead, and in the middle is a real language that has to become yours. I teach that middle. I refuse to move a class faster than the slowest student's confidence. I use recipes and market conversation as the spine of most weeks, not because food is a gimmick, but because Italian food language is the most concrete adult vocabulary there is. A verb tense taught through the preparation of ragu is a verb tense a student never forgets. My kitchen is behind me on the camera. That is deliberate.",
        "essay":"Giulia is Bolognese on both sides for four generations. She read modern languages at the Università di Bologna and then trained specifically in food language, the specialised Italian of ingredients and preparation and market negotiation. She teaches from the corner of her kitchen. Copper pans hang on the wall behind her. That is the classroom."
    },
    {
        "slug":"alessandro", "first":"Alessandro", "last":"Ferri",
        "city":"Milano", "region":"Lombardia", "regionEn":"Lombardy",
        "portrait":"teacher-alessandro.jpg", "desk":"teacher-alessandro.jpg",
        "cityImg":"city-milano.jpg", "lifeImg":"life-scala-milano.jpg",
        "credentials":["DITALS II · Università per Stranieri di Siena","Conservatorio training in vocal Italian and opera diction","CEFR Examiner · A2 through B1","Eight years teaching conversation and cultural Italian"],
        "courses":[("ps-chiacchierando","Parliamo · Chiacchierando","Conversation classes for confident speakers."),("cap-opera","Capsule · L'Opera","Six weeks in the language of Verdi and Puccini.")],
        "quote":"An opera libretto is not old Italian. It is compressed Italian, the language at its most designed. Read one line of Puccini closely and you understand fifty ordinary sentences.",
        "manifesto":"I did not start as a language teacher. I studied at the Conservatorio and spent five years as a coach for foreign singers learning to pronounce Italian for the stage. That trained my ear for what makes a non-Italian voice sound Italian, and I brought that training into the language classroom. Milan is the practical capital, the working capital, and my Italian is a working Italian. Fast when it needs to be, quiet when it needs to be, always in tune. I teach adults who can already survive in the language and want to sound like they belong. That is a specific job.",
        "essay":"Alessandro is from the Navigli district in Milan, near the canals. He trained as a vocal coach at the Milan Conservatorio, worked at La Scala's summer academy for four seasons, then made the full move into language teaching. He is the only member of our faculty with a formal music training, and it shows in the way he teaches rhythm and stress in a sentence."
    },
    {
        "slug":"francesca", "first":"Francesca", "last":"Zeno",
        "city":"Venezia", "region":"Veneto", "regionEn":"Veneto",
        "portrait":"teacher-francesca.jpg", "desk":"teacher-francesca.jpg",
        "cityImg":"city-venezia.jpg", "lifeImg":"life-gondola-venezia.jpg",
        "credentials":["DITALS II · Università per Stranieri di Siena","Master in Italian for tourism and cultural travel","CEFR Examiner · A1 through A2","Seven years teaching travel-focused Italian"],
        "courses":[("ps-viaggio","Parliamo · In viaggio","Speaking Italian on Italian trips.")],
        "quote":"Most of my students are planning a trip. That gives us a syllabus with a real deadline, a real place, and a real person on the other side of a counter in October.",
        "manifesto":"Travel Italian is often taught badly. It is taught as a list of phrases you memorise and then forget the moment a real Italian speaks back to you. I teach it as language for a specific trip. Each of my students tells me in the first week where they are going and when, and the class bends around those trips. We rehearse arrivals, we rehearse the awkward middle days, we rehearse the small conversations that will decide whether the trip felt like a vacation or like a place you actually visited. Venice is my classroom because Venice is a city that survives on travellers. I know exactly how a well-prepared foreign speaker is received here, and how a badly prepared one is treated.",
        "essay":"Francesca is Venetian. She grew up in the Cannaregio neighbourhood, took a first degree at Ca' Foscari, then trained specifically in the Italian of tourism and cultural travel. She teaches from an apartment overlooking a side canal. Her students often say the light behind her on the camera is enough on its own."
    },
    {
        "slug":"luca", "first":"Luca", "last":"De Simone",
        "city":"Napoli", "region":"Campania", "regionEn":"Campania",
        "portrait":"teacher-luca.jpg", "desk":"teacher-luca.jpg",
        "cityImg":"city-napoli.jpg", "lifeImg":"life-amalfi-coast.jpg",
        "credentials":["DITALS II · Università per Stranieri di Siena","Laurea in Filologia Italiana · Federico II","CEFR Examiner · A2 through B1","Ten years teaching upper intermediate adults"],
        "courses":[("ci4","CI Avanzato · A2.1 to A2.2","The last stage before a B1 certificate.")],
        "quote":"By the time a student reaches me they can already speak. My job is to make the language accurate, and to make the accuracy invisible. Correct Italian that still sounds like the student, not a textbook.",
        "manifesto":"I teach the last stage. My students arrive able to hold a conversation and leave with a language that can carry a professional email, a difficult phone call, a family visit that lasts a week. That transition is the hardest part of the whole course and it is the part I most enjoy. Naples is a demanding city and it made me a demanding teacher. I mark work carefully. I return it fast. I expect a student to work between our lessons and I say so on day one. Nothing about the last stage is passive. Neither am I.",
        "essay":"Luca is from the Vomero hill in Naples. He read Italian philology at Federico II with a dissertation on twentieth century Neapolitan writing, then trained as a language teacher in Perugia. He teaches the highest level in our course ladder. His students are often preparing for an official CEFR B1 examination in the twelve months after his course."
    },
    {
        "slug":"sofia", "first":"Sofia", "last":"Mazzara",
        "city":"Palermo", "region":"Sicilia", "regionEn":"Sicily",
        "portrait":"teacher-sofia.jpg", "desk":"teacher-sofia.jpg",
        "cityImg":"city-palermo.jpg", "lifeImg":"life-amalfi-coast.jpg",
        "credentials":["DITALS II · Università per Stranieri di Siena","Laurea in Lingue Moderne · Università di Palermo","CEDILS · Università Ca' Foscari Venezia","Nine years teaching adult learners across three continents"],
        "courses":[("ci4","CI Avanzato · A2.1 to A2.2","The last stage before a B1 certificate.")],
        "quote":"Sicily is a country of its own, inside Italy. Standard Italian on this island is a chosen thing, spoken with care. That care is what my students learn from me.",
        "manifesto":"I share the top level with Luca. We teach it the same way, from opposite ends of the peninsula, and that gives our advanced students two different accents to listen to before the certificate. That matters. A learner who has only heard one voice teach the language is a fragile learner. My Sicilian students, my French students, my Israeli students, my American students all get corrected the same way in my class, in a language that treats them as adults. I do not use baby exercises. I use texts, letters, phone calls, real recordings, and I coach the student through them.",
        "essay":"Sofia is Palermitana. She read modern languages at the Università di Palermo, took the CEDILS specialisation in Venice, then taught in Marseille and Tel Aviv before returning to teach online from Palermo. She is bilingual in Italian and French and has passable Arabic. Her advanced students often say she is the most exacting teacher they have ever had, and mean it as a compliment."
    },
]

def teacher_page(t):
    p = "../../"
    hero = f"""
<section class="section-ink hero-teacher">
  <div class="hero-teacher-grid">
    <div class="hero-teacher-left">
      <span class="eyebrow eyebrow-gold">{t['region']} · {t['city']}</span>
      <h1 class="serif-display hero-teacher-h1"><em>{t['first']}</em><br>{t['last']}</h1>
      <p class="lead hero-teacher-cred">Native teacher · CEFR Examiner · Faculty since 2022</p>
      <div class="cta-row">
        <button class="btn btn-primary btn-lg" data-advisor type="button">Book with {t['first']}</button>
        <a class="btn btn-ghost btn-lg" href="../../teachers.html">All teachers</a>
      </div>
    </div>
    <div class="hero-teacher-right">
      <img src="{p}assets/img/{t['portrait']}" alt="{t['first']} {t['last']}, teacher in {t['city']}" class="hero-teacher-portrait">
    </div>
  </div>
</section>
"""
    region = f"""
<section class="section-paper">
  <div class="wrap">
    <div class="section-head-split">
      <div>
        <span class="eyebrow">The region</span>
        <h2 class="serif-display">{t['regionEn']}, as {t['first']} teaches it</h2>
      </div>
    </div>
    <div class="editorial-2col">
      <div class="col-essay">
        <p class="lead">{t['essay']}</p>
      </div>
      <div class="col-essay">
        <p>Every teacher on our faculty teaches from one Italian region and from one only. That is not a marketing point. It is what allows a class to have a place. When {t['first']} opens a lesson at seven in the morning her time, the light behind her is {t['city']} light. The bread on her desk was bought at a {t['city']} bakery. The vocabulary that emerges in a conversation about weekends is {t['regionEn']} vocabulary. Students on the other side of the world tell us the same thing, class after class. They are not on a language platform. They are in {t['city']}, for eighty five minutes.</p>
        <p>Regional Italian is not dialect. {t['first']} teaches the standard national language, the Italian of newspapers and universities and the state broadcaster. What she brings is location. A verb form is illustrated with a scene from her city. A grammar point is drawn out of a conversation that could have taken place on her street. The language stays standard. The teaching room is specific.</p>
      </div>
    </div>
    <figure class="figure-full">
      <img src="{p}assets/img/{t['lifeImg']}" alt="{t['regionEn']} scene" loading="lazy">
      <figcaption>A scene from {t['regionEn']}. The language {t['first']} teaches is the language of this place.</figcaption>
    </figure>
  </div>
</section>
"""
    manifesto = f"""
<section class="section-cream section-manifesto">
  <div class="wrap">
    <div class="pullquote-band">
      <span class="eyebrow">Teaching manifesto</span>
      <blockquote class="serif-display quote-lg"><em>{t['manifesto']}</em></blockquote>
      <div class="quote-attr">{t['first']} {t['last']} · {t['city']}</div>
    </div>
  </div>
</section>
"""
    creds = "".join(f'<li><span class="cred-mark">·</span><span>{c}</span></li>' for c in t['credentials'])
    credentials = f"""
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Credentials</span>
      <h2 class="serif-display">The formal training behind the class</h2>
    </div>
    <div class="two-col-list">
      <ul class="cred-list">{creds}</ul>
      <div class="cred-side">
        <p>Every teacher on this faculty holds a formal Italian-as-a-foreign-language qualification from an Italian university. That is a non negotiable in our hiring. It is not the whole of the class, but it is the floor. What the students hear in the lesson is built on this training, and on years of teaching adults in exactly this format.</p>
        <p class="lead">Ask us for the paper credentials. We share them.</p>
      </div>
    </div>
  </div>
</section>
"""
    students = [
        {"n":"Diane Whitfield","loc":"Portland, Oregon","img":f"{p}assets/img/student-diane.jpg","t":f"{t['first']} makes the language patient","b":f"I had tried three apps before I found {t['first']}. She teaches like an adult teaching another adult. I finally have Italian I can use."},
        {"n":"Robert Marconi","loc":"Boston, Massachusetts","img":f"{p}assets/img/student-robert.jpg","t":f"A real teacher, from a real place","b":f"Eighty five minutes in a class with {t['first']} feels like eighty five minutes in {t['city']}. That is the whole reason it worked for me."},
        {"n":"Linda Cavalli","loc":"San Diego, California","img":f"{p}assets/img/student-linda.jpg","t":f"Ten months in and still enjoying it","b":f"I was afraid the novelty would wear off. It hasn't. {t['first']} keeps changing the shape of the class so it never gets stale."},
    ]
    testis = tp_wall(students)
    # Custom heading for teacher testis
    testis = testis.replace("What students actually say", f"What {t['first']}'s students say")

    lesson = f"""
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">A typical lesson with {t['first']}</span>
      <h2 class="serif-display">Eighty five minutes, structured for adults</h2>
    </div>
    <div class="phase-grid">
      <div class="phase-col">
        <div class="phase-num">01</div>
        <h3>Learning goals</h3>
        <ul class="phase-list">
          <li>One grammar point named at the start of the lesson</li>
          <li>Ten to fifteen new items of {t['regionEn']}-anchored vocabulary</li>
          <li>One conversational function students will leave able to perform</li>
          <li>One short cultural note tied to the day's material</li>
          <li>A named piece of work to bring back next week</li>
        </ul>
      </div>
      <div class="phase-col">
        <div class="phase-num">02</div>
        <h3>The eighty five minute flow</h3>
        <ul class="phase-list">
          <li>0 to 10 · warm up in Italian, weekend and week ahead</li>
          <li>10 to 25 · new material, introduced through a real scene</li>
          <li>25 to 45 · guided practice, in pairs on breakout</li>
          <li>45 to 55 · a short break, {t['first']} stays online</li>
          <li>55 to 75 · free conversation on the day's theme</li>
          <li>75 to 85 · review, homework, questions</li>
        </ul>
      </div>
      <div class="phase-col">
        <div class="phase-num">03</div>
        <h3>Between lesson work</h3>
        <ul class="phase-list">
          <li>One short reading from {t['first']}'s Italian sources</li>
          <li>One audio, usually a real recording under three minutes</li>
          <li>One written piece, no longer than 120 words</li>
          <li>A quiet fifteen minutes with Biagio, if you want it</li>
          <li>Total realistic weekly load: ninety to a hundred minutes</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""
    course_cards = "".join(f"""
      <a class="course-card" href="../../pages/courses/{cid}.html">
        <div class="course-card-body">
          <h3 class="serif-display">{name}</h3>
          <p>{desc}</p>
          <span class="course-more">See the course</span>
        </div>
      </a>""" for cid,name,desc in t['courses'])
    courses = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Which courses I teach</span>
      <h2 class="serif-display">{t['first']}'s teaching load</h2>
      <p class="lead">Every teacher on the faculty holds a fixed teaching load. This is {t['first']}'s.</p>
    </div>
    <div class="course-grid course-grid-{len(t['courses'])}">{course_cards}
    </div>
  </div>
</section>
"""
    schedule = f"""
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Live cohorts · October start</span>
      <h2 class="serif-display">Open time slots with {t['first']}</h2>
      <p class="lead">Times are shown in New York time. All classes are live from {t['city']}.</p>
    </div>
    <div class="schedule-table">
      <div class="sch-row sch-head"><div>Cohort</div><div>Day</div><div>Time (ET)</div><div>Course</div><div>Seats</div><div></div></div>
      <div class="sch-row"><div>CI-{t['slug'][:2].upper()}-01</div><div>Mon and Wed</div><div>7:00 pm to 8:25 pm</div><div>{t['courses'][0][1].split(' · ')[0]}</div><div>3 of 12 left</div><div><button class="btn btn-primary btn-sm" data-advisor type="button">Hold my seat</button></div></div>
      <div class="sch-row"><div>CI-{t['slug'][:2].upper()}-02</div><div>Tue and Thu</div><div>11:00 am to 12:25 pm</div><div>{t['courses'][0][1].split(' · ')[0]}</div><div>7 of 12 left</div><div><button class="btn btn-primary btn-sm" data-advisor type="button">Hold my seat</button></div></div>
      <div class="sch-row"><div>CI-{t['slug'][:2].upper()}-03</div><div>Sat</div><div>9:30 am to 12:20 pm</div><div>Weekend intensive</div><div>5 of 10 left</div><div><button class="btn btn-primary btn-sm" data-advisor type="button">Hold my seat</button></div></div>
      <div class="sch-row"><div>CI-{t['slug'][:2].upper()}-04</div><div>Mon Wed Fri</div><div>6:00 pm to 7:00 pm</div><div>Accelerated</div><div>2 of 8 left</div><div><button class="btn btn-primary btn-sm" data-advisor type="button">Hold my seat</button></div></div>
    </div>
  </div>
</section>
"""
    book = final_cta_verona(f"Book your first class with {t['first']}.", f"One native teacher from {t['city']}, live from {t['regionEn']}, in a small group of adults who mean it.", f"Book with {t['first']}")

    body = hero + region + manifesto + credentials + testis + lesson + courses + schedule + book
    return page(f"{t['first']} {t['last']} · Italian teacher from {t['city']} · Club Italia",
                f"Meet {t['first']} {t['last']}, native Italian teacher from {t['city']}, {t['regionEn']}. CEFR examiner. Live small group classes for adults, from Italy.",
                body, prefix=p)

# Write all teacher pages
def write_teacher_pages():
    for t in TEACHERS:
        out = ROOT/f"pages/teachers/{t['slug']}.html"
        out.write_text(teacher_page(t))
        print(f"wrote {out}")

if __name__ == "__main__":
    write_teacher_pages()
