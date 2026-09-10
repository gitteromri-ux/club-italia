#!/usr/bin/env python3
"""Course pages, pricing, indexes."""
import json, os, re, sys
from pathlib import Path
sys.path.insert(0, "/home/user/workspace/club-italia")
from build_fa import head, foot, clean, DATA, ROOT

# Course-specific mappings
TEACHER = {
    "ci1":("marco","Marco Rinaldi","Rome","Roma","Sapienza · Dante Alighieri certified"),
    "ci2":("chiara","Chiara Belli","Florence","Firenze","Università di Firenze · fifteen years teaching"),
    "ci3":("giulia","Giulia Ferri","Bologna","Bologna","Bologna DITALS II · trained chef"),
    "ci4":("luca","Luca Esposito","Naples","Napoli","L'Orientale Napoli · doctorate in linguistics"),
    "ps1":("marco","Marco Rinaldi","Rome","Roma","Sapienza · Dante Alighieri certified"),
    "ps2":("chiara","Chiara Belli","Florence","Firenze","Università di Firenze · fifteen years teaching"),
    "ps3":("francesca","Francesca Moretti","Venice","Venezia","Ca' Foscari · gondola-side teacher of ten years"),
    "ps4":("alessandro","Alessandro Conti","Milan","Milano","Bocconi & Cattolica · opera scholar"),
    "cap-food":("giulia","Giulia Ferri","Bologna","Bologna","Bologna DITALS II · trained chef"),
    "cap-art":("chiara","Chiara Belli","Florence","Firenze","Università di Firenze · fifteen years teaching"),
    "cap-opera":("alessandro","Alessandro Conti","Milan","Milano","Bocconi & Cattolica · opera scholar"),
}
VIDEO = {
    "ci1":"roma-piazza","ci2":"firenze-arno","ci3":"bologna-portici","ci4":"napoli-mare",
    "ps1":"roma-piazza","ps2":"firenze-arno","ps3":"venezia-canal","ps4":"bologna-portici",
    "cap-food":"cucina-pasta","cap-art":"opera-scala","cap-opera":"opera-scala",
}
CITY_ESSAY = {
    "Rome":("Rome, the city where the language began.",
            "Two thousand years ago, Latin filled these streets. A thousand years ago, the vulgar tongue that would become Italian was first written in a monastery here. Today, Rome is where our foundation course is broadcast from, and there is a reason for that.",
            "You cannot learn Italian without hearing the vowels open the way they do in Trastevere. You cannot understand the word piazza until you have heard a Roman say it. Marco teaches from a two-hundred-year-old apartment near Piazza Navona, and the church bells across the river ring at eleven, always at eleven.",
            "By the end of the term, you will not simply know Roman Italian. You will know what makes it Roman, and you will know how it differs from the Florentine standard you will meet in the next stage."),
    "Florence":("Florence, the city where the language was standardised.",
                "In the fourteenth century, Dante Alighieri wrote his Comedy in the Florentine of the merchants and the mothers. Five centuries later, that Florentine became the official Italian of a unified country. Every Italian sentence, whether spoken in Palermo or Milan, carries a Florentine ghost.",
                "Chiara teaches from a studio one street from Santa Croce, where Dante is buried. Her Italian is what the grammar books call standard, and her ear for what it means to speak well is legendary in our faculty.",
                "This term you will meet the language at its official centre. You will learn what makes an Italian sentence elegant, and why the Florentines still smile when a Neapolitan speaks it."),
    "Bologna":("Bologna, la Dotta, la Grassa, la Rossa.",
               "The learned, the fat, the red. Bologna is the oldest university city in the western world, the culinary capital of Italy, and a city of terracotta rooftops and long portici. Every one of those three names matters for how Italian is spoken here.",
               "Giulia teaches from a kitchen apartment near Piazza Maggiore, and lessons often run over a working stove. She is a trained chef as well as a certified teacher, and she knows why the Bolognese roll their r and lengthen their consonants.",
               "By the end of the term you will speak the Italian of the north-central heartland, the Italian a lawyer or a doctor from Emilia would use with a friend at Sunday lunch."),
    "Naples":("Naples, the city where Italian is sung, not spoken.",
              "Neapolitan is a language of its own. But standard Italian, spoken in the shadow of Vesuvius, takes on a musical shape that no other city produces. Vowels stretch, sentences rise and fall, the whole language becomes an opera.",
              "Luca holds a doctorate in the linguistics of southern Italian and teaches from an apartment overlooking the Bay of Naples. His lessons are famous in our faculty for the way they use rhythm to teach grammar.",
              "This term consolidates every tense and every register you have met in earlier stages, and does it against a soundtrack that is impossible to forget."),
    "Venice":("Venice, the city that invented modern travel.",
              "For a thousand years Venice was where east met west, and every ship that arrived at the Rialto brought a new set of loanwords into Italian. Every travel word you will learn this term has a Venetian ancestor.",
              "Francesca teaches from a studio in Cannaregio, and if the class is at four in the afternoon, you will hear the water outside the window. She has taught travellers of every nationality for ten years and knows exactly which Italian sentences survive a real conversation with a train conductor.",
              "By the end you will handle every transport, hotel, museum and mountain refuge you might meet on a real Italian trip, without switching to English once."),
    "Milan":("Milan, the city that made Italian modern.",
             "Milan is the Italy of the twenty-first century. It is the city of Prada, La Scala, the aperitivo hour and the Corriere della Sera. The Italian spoken here is fast, precise, and unafraid of an English loanword when it earns its place.",
             "Alessandro teaches from an apartment near Corso Como, and he is our opera scholar as well as our northern Italian specialist. His lessons close the CEFR arc by taking you into contemporary Italian, the language of a newspaper editorial and a boardroom.",
             "You will leave the term ready to sit an exam, to accept a job offer, or to hold your own with the fastest speakers in the country."),
}

OUTCOMES = {
    "ps1":["Order a coffee, a pastry and a full breakfast at any Italian caffè","Handle small talk with strangers in a queue or at a bar","Understand a Neapolitan barista at seven in the morning","Ask directions with the polite forms Italians actually use","Use the Italian version of please, thank you and excuse me correctly","Follow the news headlines of a two-minute morning radio segment"],
    "ps2":["Order antipasto, primo, secondo and dolce for a whole table","Talk about food with the vocabulary a chef would recognise","Argue politely about the correct shape of pasta for a sauce","Read a full trattoria menu and understand every regional dish","Discuss a wine with a sommelier and follow her recommendation","Send a compliment to a Roman nonna in her own kitchen"],
    "ps3":["Buy a train ticket, book a hotel, and change a booking on the phone","Handle a museum visit, a boat tour and a mountain refuge","Discuss the weather, the road, the traffic like a local","Explain a health need at an Italian pharmacy","Read the announcement board at Termini and Milano Centrale","Ask a farmer, a fisherman or a guide for practical local advice"],
    "ps4":["Hold an opinion in Italian and defend it for two full minutes","Follow a Sorrentino film without the subtitles","Read an editorial in Corriere della Sera and summarise it","Tell a joke and land the punchline in Italian","Disagree politely with an Italian friend in the street","Narrate a memory with the correct sequence of past tenses"],
    "cap-food":["Read a regional Italian menu the way an Italian reads it","Discuss the Italian meal in its correct order and philosophy","Understand the vocabulary of pasta shapes, sauces and regions","Follow a live cooking demonstration in Italian","Order and drink Italian coffee correctly at every hour of the day","Argue the pineapple question with sincerity"],
    "cap-art":["Read a museum label at the Uffizi in Italian","Follow a guided tour of a Roman basilica in Italian","Recognise the vocabulary of colour, line, composition and light","Discuss Giotto, Piero, Raphael and Caravaggio in Italian","Understand why the Renaissance uses the words it does","Write a short reflection on a painting in Italian"],
    "cap-opera":["Read the libretto of one full aria in Italian","Follow the third act of La Bohème without a translation","Understand why Italian is called the opera language","Discuss Verdi, Puccini and Rossini in Italian","Recognise the vocabulary of love, betrayal, longing and forgiveness in opera","Attend an Italian opera and understand more than half of it"],
}

def lesson_names(cid):
    # From course-data.json
    d = DATA[cid]
    return [(i+1, l[0], l[1]) for i, l in enumerate(d.get("syllabus", []))]

# ---------- Course page builder ----------
def build_course(cid):
    d = DATA[cid]
    tk, tname, tcity_en, tcity, tcred = TEACHER[cid]
    video = VIDEO[cid]
    title = clean(d["title"].split("—")[0].strip() if "—" in d["title"] else d["title"])
    tag = d["tag"]
    cefr = d["cefr"]
    hours = d["hours"]
    promise = clean(d["promise"])
    hero_img = d["hero_image"]  # relative from root; we need ../../ prefix

    subfolder = "culture" if cid.startswith("cap") else ("spoken" if cid.startswith("ps") else "courses")
    depth = 2  # pages/<subfolder>/
    P = "../../"  # prefix
    is_capsule = cid.startswith("cap")
    lesson_count = 6 if is_capsule else 20
    price_range = "$740" if is_capsule else "$1,240"
    contact = "8.5 hours" if is_capsule else "28.3 hours"

    # ---- Fold 1 hero ----
    F1 = f'''
<section class="hero hero-full section-ink" data-fold="1">
  <video class="hero-video" autoplay muted loop playsinline preload="metadata" poster="{P}{hero_img}">
    <source src="{P}assets/video/{video}.mp4" type="video/mp4">
  </video>
  <div class="hero-scrim hero-scrim-diagonal"></div>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="eyebrow eyebrow-live">{tag} · Live from {tcity}</span>
      <h1 class="hero-h1">{title}. <em class="gold-ital">Your Italian, taught in {tcity_en}.</em></h1>
      <p class="hero-sub">{promise}</p>
      <div class="hero-price-chip"><span class="hpc-a">{price_range}</span><span class="hpc-b">{lesson_count} lessons · CEFR {cefr}</span></div>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="#reserve">Reserve my seat</a>
        <a class="btn btn-ghost" href="{P}pdf/{cid}-syllabus.pdf" download>Download syllabus PDF</a>
      </div>
      <div class="trustpilot-strip">
        <span class="tp-stars">★★★★★</span>
        <span class="tp-score">Trustpilot 4.8 / 5</span>
        <span class="tp-count">347 alumni completed · Next start Oct 6</span>
      </div>
    </div>
    <div class="hero-visual">
      <div class="hero-video-right radial-mask">
        <img src="{P}assets/img/zoom-classroom-{tk if tk in ('marco','chiara') else 'marco'}.jpg" alt="A live Zoom class with {tname}" width="720" height="540">
      </div>
    </div>
  </div>
  <div class="hero-live-strip"><span class="pulse-dot"></span><span class="live-text">Next live class: this Tuesday, 8pm EST</span></div>
</section>'''

    # ---- Fold 2 stats strip ----
    F2 = f'''
<section class="section section-ink stat-row-band" data-fold="2">
  <div class="wrap stat-row">
    <div class="chip-stat"><span class="cs-num">Live</span><span class="cs-lab">on Zoom, in real time</span></div>
    <div class="chip-stat"><span class="cs-num">{lesson_count}</span><span class="cs-lab">lessons over one term</span></div>
    <div class="chip-stat"><span class="cs-num">{contact}</span><span class="cs-lab">total contact time</span></div>
    <div class="chip-stat"><span class="cs-num">10 to 12</span><span class="cs-lab">learners in your group</span></div>
    <div class="chip-stat"><span class="cs-num">CEFR {cefr}</span><span class="cs-lab">certification</span></div>
  </div>
</section>'''

    # ---- Fold 3 outcomes ----
    outs = OUTCOMES.get(cid) or d.get("outcomes", [])
    outs = [clean(o) for o in outs][:6]
    outs_html = "".join(f'<li class="lo-item"><span class="lo-check">✓</span><span class="lo-text">{o}.</span></li>' for o in outs)
    F3 = f'''
<section class="section section-travertine outcomes-band" data-fold="3">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">By the end</span>
      <h2 class="h2-editorial">You will be able to <em class="gold-ital">actually do this</em>.</h2>
      <p class="section-lede">Six real behaviours from the Common European Framework, chosen to match {cefr}. Every outcome is measured in your final oral and written assessment.</p>
    </div>
    <ul class="learning-outcomes">{outs_html}</ul>
  </div>
</section>'''

    # ---- Fold 4 four-phase arc ----
    lessons = lesson_names(cid)
    def phase(num, name, kick, start, end):
        rng = [l for l in lessons if start <= l[0] <= end]
        items = "".join(f'<li><em>{n:02d}.</em> {clean(t)}</li>' for n,t,_ in rng)
        return f'<article class="phase-card"><span class="pc-kick">{kick}</span><span class="pc-num"><em>{num}</em></span><h4 class="pc-name">{name}</h4><ol class="pc-lessons">{items}</ol></article>'

    if is_capsule:
        F4 = f'''
<section class="section section-cream phase-band" data-fold="4">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">How the six sessions unfold</span>
      <h2 class="h2-editorial">Two phases. <em class="gold-ital">One capsule.</em></h2>
    </div>
    <div class="phase-grid card-slider">
      {phase("01","Foundation","Sessions 1 to 3", 1, 3)}
      {phase("02","Immersion","Sessions 4 to 6", 4, 6)}
    </div>
  </div>
</section>'''
    else:
        F4 = f'''
<section class="section section-cream phase-band" data-fold="4">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">How the twenty lessons unfold</span>
      <h2 class="h2-editorial">Four phases. <em class="gold-ital">One arc.</em></h2>
      <p class="section-lede">The twenty lessons are grouped into four phases of five lessons each. Every phase closes with a scene rehearsal and a short informal check.</p>
    </div>
    <div class="phase-grid card-slider">
      {phase("01","Foundation","Lessons 1 to 5", 1, 5)}
      {phase("02","Everyday Life","Lessons 6 to 10", 6, 10)}
      {phase("03","Storytelling","Lessons 11 to 15", 11, 15)}
      {phase("04","Confident Speaker","Lessons 16 to 20", 16, 20)}
    </div>
  </div>
</section>'''

    # ---- Fold 5 full syllabus table ----
    rows = ""
    for n,name,body in lessons:
        name = clean(name)
        # Split body into grammar/cultural crudely: cultural is last sentence
        parts = clean(body).split(". ")
        cultural = parts[-1] if parts else ""
        grammar = ". ".join(parts[:-1]) if len(parts) > 1 else parts[0]
        if not cultural.endswith("."): cultural += "."
        if not grammar.endswith("."): grammar += "."
        rows += f'<tr><td class="sy-num"><em>{n:02d}</em></td><td class="sy-topic"><em>{name}</em></td><td class="sy-grammar">{grammar}</td><td class="sy-culture">{cultural}</td></tr>'

    F5 = f'''
<section class="section section-travertine syllabus-band" data-fold="5">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The syllabus, week by week</span>
      <h2 class="h2-editorial">{lesson_count} lessons. <em class="gold-ital">One continuous story.</em></h2>
      <p class="section-lede">Every line below is a real live class taught by {tname} from {tcity}. Nothing is a recording, nothing is a module, nothing is optional.</p>
    </div>
    <div class="section-foot section-foot-top"><a class="btn btn-primary" href="{P}pdf/{cid}-syllabus.pdf" download>Download the complete syllabus (12-page PDF)</a></div>
    <div class="syllabus-table-wrap">
      <table class="syllabus-table">
        <thead><tr><th>#</th><th>Topic</th><th>Grammar &amp; vocabulary</th><th>Cultural setting</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  </div>
</section>'''

    # ---- Fold 6 session deep-dive ----
    lesson07 = lessons[6] if len(lessons) > 6 else (lessons[len(lessons)//2] if lessons else (1, "Lesson", ""))
    lesson07 = (lesson07[0], clean(lesson07[1]), clean(lesson07[2]))
    F6 = f'''
<section class="section section-cream session-band" data-fold="6">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Inside a single lesson</span>
      <h2 class="h2-editorial">Eighty-five minutes with <em class="gold-ital">{tname.split()[0]}</em>.</h2>
      <p class="section-lede">Lesson {lesson07[0]:02d} · {lesson07[1]}. Every learner logs in at 8pm EST on a Tuesday. The camera opens on {tname.split()[0]}'s desk in {tcity}. This is what the next eighty-five minutes look like.</p>
    </div>
    <div class="session-detail">
      <div class="sd-col">
        <h4 class="sd-kick">Learning goals</h4>
        <ul class="sd-list">
          <li>You can hold the scene of the lesson in Italian for four full turns.</li>
          <li>You can use the new grammar without translating in your head.</li>
          <li>You can pronounce the new vocabulary the way {tname.split()[0]} does.</li>
          <li>You leave with two written examples in your own notebook.</li>
        </ul>
      </div>
      <div class="sd-col sd-col-highlight">
        <h4 class="sd-kick">The 85-minute flow</h4>
        <ol class="sd-flow">
          <li><em>00:00 to 00:10</em> · Warm greetings and last week's carryover.</li>
          <li><em>00:10 to 00:30</em> · The new scene, first read together, then acted out in pairs.</li>
          <li><em>00:30 to 00:50</em> · Grammar in the moment. {tname.split()[0]} draws on the whiteboard.</li>
          <li><em>00:50 to 01:10</em> · Pair rooms with focused correction from {tname.split()[0]}.</li>
          <li><em>01:10 to 01:25</em> · Group reunion, final rehearsal, homework for next week.</li>
        </ol>
      </div>
      <div class="sd-col">
        <h4 class="sd-kick">Between-lesson work</h4>
        <ul class="sd-list">
          <li>A twelve-minute Biagio conversation on the new scene.</li>
          <li>One short reading, one short listening, one short writing.</li>
          <li>Optional: a matching cultural clip from our library.</li>
          <li>Expected weekly load: about ninety minutes outside class.</li>
        </ul>
      </div>
    </div>
  </div>
</section>'''

    # ---- Fold 7 real Zoom classroom ----
    zk = tk if tk in ("marco","chiara") else "marco"
    F7 = f'''
<section class="section section-ink live-class-band" data-fold="7">
  <div class="wrap two-col">
    <div class="tc-copy">
      <span class="eyebrow">The classroom</span>
      <h2 class="h2-editorial">Small groups. <em class="gold-ital">Real live faces.</em></h2>
      <p class="lead">Every class in {title} runs at ten to twelve learners. No lecture halls, no chat-only sessions, no automatic exercises. Your camera is on, your microphone is on, and {tname.split()[0]} calls on you by name.</p>
      <p>The room you see on the right is a real Tuesday evening on our platform. You will recognise it after your first week.</p>
      <a class="btn btn-ghost" href="{P}sample-class.html">Watch a 30-minute recording</a>
    </div>
    <div class="tc-visual">
      <div class="zoom-frame"><img src="{P}assets/img/zoom-classroom-{zk}.jpg" alt="A live Zoom classroom with {tname}" loading="lazy"></div>
      <p class="tc-caption"><em>Tuesday, 8pm EST · {tname} broadcasting from {tcity} · nine learners live · one hand raised.</em></p>
    </div>
  </div>
</section>'''

    # ---- Fold 8 cultural context ----
    e = CITY_ESSAY.get(tcity_en) or CITY_ESSAY["Rome"]
    F8 = f'''
<section class="section section-travertine city-band" data-fold="8">
  <div class="wrap two-col">
    <div class="tc-copy">
      <span class="eyebrow">The city is the classroom</span>
      <h2 class="h2-editorial">{e[0].replace(", ", ", <em class=\"gold-ital\">", 1)}</em></h2>
      <p class="lead">{e[1]}</p>
      <p>{e[2]}</p>
      <p>{e[3]}</p>
    </div>
    <div class="tc-visual tc-visual-full">
      <img src="{P}assets/img/city-{tcity.lower()}.jpg" alt="{tcity_en}, the classroom city" loading="lazy" onerror="this.src='{P}assets/img/life-caffe-roma.jpg'">
    </div>
  </div>
</section>'''

    # ---- Fold 9 your teacher ----
    env_img = f"env-{tk}-desk.jpg" if tk in ("marco","chiara") else (f"env-giulia-kitchen.jpg" if tk=="giulia" else f"city-{tcity.lower()}.jpg")
    F9 = f'''
<section class="section section-cream teacher-band" data-fold="9">
  <div class="wrap two-col">
    <div class="teacher-env"><img src="{P}assets/img/{env_img}" alt="{tname.split()[0]}'s workspace in {tcity}" loading="lazy"></div>
    <div class="teacher-side">
      <img class="teacher-portrait" src="{P}assets/img/teacher-{tk}.jpg" alt="{tname}" loading="lazy">
      <span class="eyebrow">{tcity}, Italy</span>
      <h2 class="h2-editorial">{tname}</h2>
      <p class="lead"><em>{tcred}</em></p>
      <p>{tname.split()[0]} has taught Italian to adult learners for over a decade. She holds a full degree in Italian language and literature and a recognised international teaching certification.</p>
      <p>Her lessons are built on scenes, not slides. She believes an adult learner deserves the same respect a graduate student receives in a Perugia or Siena classroom, and she plans every ninety minutes on that principle.</p>
      <p>She teaches only from {tcity}. When you take her class, you take it into the country she loves and knows.</p>
      <a class="btn btn-primary" href="#reserve">Book with {tname.split()[0]}</a>
    </div>
  </div>
</section>'''

    # ---- Fold 10 what's included ----
    inc = [
        f"{lesson_count} live small-group classes with {tname}",
        "Every class recorded for your review the same evening",
        "Full access to Biagio, the AI conversation coach",
        "Weekly personal note from your teacher by email",
        "Cultural library of films, articles and cooking clips",
        "Placement interview before day one",
        "End of stage oral and written CEFR assessment",
        "Printed CEFR certificate on completion",
        "Priority advisor line during the whole term",
        "Seven day full refund after your first class",
    ]
    inc_html = "".join(f'<li class="inc-item"><span class="inc-check"><em>✓</em></span><span class="inc-text">{i}.</span></li>' for i in inc)
    F10 = f'''
<section class="section section-travertine included-band" data-fold="10">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Included in your course</span>
      <h2 class="h2-editorial">Ten things you receive <em class="gold-ital">the day you enrol</em>.</h2>
    </div>
    <ul class="included-list included-2col">{inc_html}</ul>
  </div>
</section>'''

    # ---- Fold 11 alumni + pricing ----
    alum = [
        ("Diane Weller","Chicago","student-diane.jpg", f"After {title} I ordered dinner in Trastevere and the waiter answered in Italian for the whole meal."),
        ("Robert Hensley","Austin","student-robert.jpg", f"{tname.split()[0]} caught a mistake I had been making since 2014. In one live class."),
        ("Sarah Kim","San Francisco","student-sarah.jpg", f"Small classes, real corrections, no drills. It felt like being tutored at an Italian institute."),
    ]
    al_html = "".join(f'<article class="tp-card"><div class="tpc-head"><img class="tpc-avatar" src="{P}assets/img/{img}" alt="{n}" loading="lazy"><div class="tpc-meta"><span class="tpc-name">{n}</span><span class="tpc-place">{c}</span></div></div><div class="tpc-stars">★★★★★</div><blockquote class="tpc-quote"><em>{q}</em></blockquote></article>' for n,c,img,q in alum)

    F11 = f'''
<section class="section section-cream alumni-price" data-fold="11">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Alumni</span>
      <h2 class="h2-editorial">Real progress. <em class="gold-ital">Real graduates.</em></h2>
    </div>
    <div class="tp-wall tp-wall-3 card-slider">{al_html}</div>
  </div>
  <div class="wrap wrap-narrow">
    <div class="section-head">
      <span class="eyebrow">Enrol in {title}</span>
      <h2 class="h2-editorial">Three ways to <em class="gold-ital">start</em>.</h2>
    </div>
    <div class="pricing-grid">
      <article class="price-card"><span class="pc-name">Monthly</span><span class="pc-price"><em>$84</em> <span class="pc-unit">/ week</span></span><p class="pc-note">Cancel anytime after the first month.</p><a class="btn btn-ghost btn-gold" href="{P}pricing.html">Start monthly</a></article>
      <article class="price-card price-card-featured"><span class="pc-chip">Best value · Save $440</span><span class="pc-name">Annual</span><span class="pc-price"><em>$62</em> <span class="pc-unit">/ week</span></span><p class="pc-note">Full year, all four terms, one payment.</p><a class="btn btn-primary" href="{P}pricing.html">Start annual</a></article>
      <article class="price-card"><span class="pc-name">Term</span><span class="pc-price"><em>$73</em> <span class="pc-unit">/ week</span></span><p class="pc-note">Twelve weeks. One CEFR stage.</p><a class="btn btn-ghost btn-gold" href="{P}pricing.html">Start a term</a></article>
    </div>
  </div>
</section>'''

    # ---- Fold 12 guarantee + FAQ ----
    faqs = [
        (f"Is {title} really live?", f"Every one of the {lesson_count} lessons is a live session on Zoom with {tname} in {tcity}. Nothing is a recording, nothing is automated. If you cannot attend, the lesson is recorded for you to watch the same night."),
        (f"What if my Italian is too weak for {tag}?", f"Your placement call with an advisor will confirm that {tag} is the right stage for you. If it is not, we will recommend the correct stage without pressure."),
        (f"Who teaches {title}?", f"{tname} teaches every group of this course from {tcity}. She holds {tcred.split(' · ')[0]} and has taught adult learners for over a decade."),
        ("What time zone does the class run in?", "This course is taught in evening slots convenient for the Americas and morning slots convenient for Europe and Asia. Your placement call will confirm the exact group time."),
        ("What if I miss a class?", "The class is recorded and available to you the same evening. Your teacher will also send you a short personal note so you never fall behind."),
        ("Do I get a certificate?", f"Yes. The course ends with a formal oral and written CEFR {cefr} assessment. On successful completion you receive a printed certificate."),
    ]
    faq_html = "".join(f'<details class="faq-item"><summary><span class="faq-q">{q}</span><span class="faq-toggle">＋</span></summary><div class="faq-a">{a}</div></details>' for q,a in faqs)
    F12 = f'''
<section class="section section-cream faq-band" data-fold="12">
  <div class="wrap">
    <div class="guarantee-line"><span class="gl-icon">◆</span><span class="gl-text"><em>Seven day full refund</em> on {title}. Sit the first lesson. If it is not for you, we return every dollar without a form.</span></div>
    <div class="section-head">
      <span class="eyebrow">Common questions</span>
      <h2 class="h2-editorial">Everything <em class="gold-ital">worth asking</em>.</h2>
    </div>
    <div class="faq-list">{faq_html}</div>
  </div>
</section>'''

    # ---- Fold 13 final CTA ----
    F13 = f'''
<section class="section section-verona final-cta" data-fold="13" id="reserve">
  <div class="wrap final-inner">
    <div class="fc-copy">
      <h2 class="h2-huge">Reserve your seat with <em class="gold-ital">{tname.split()[0]}</em>.</h2>
      <p class="fc-lede">Thirty minute placement call. Spoken in English. Ends with a clear recommendation and a start date. No obligation to enrol.</p>
    </div>
    <form class="fc-form paper-glass" novalidate>
      <div class="ff-row"><label>Your name<input type="text" name="name" required placeholder="Full name"></label></div>
      <div class="ff-row"><label>Email<input type="email" name="email" required placeholder="you@email.com"></label></div>
      <div class="ff-row"><label>Phone<input type="tel" name="phone" required placeholder="+1 555 000 0000"></label></div>
      <div class="ff-row"><label>Preferred start
        <select name="start" required>
          <option value="">Choose a start window</option>
          <option>Next term (October)</option>
          <option>Winter term (January)</option>
          <option>Spring term (April)</option>
          <option>Summer term (July)</option>
        </select></label></div>
      <button class="btn btn-primary btn-block" type="submit">Reserve my seat</button>
      <p class="ff-note">We reply within one working day. No sales script, no pressure.</p>
    </form>
  </div>
</section>'''

    html = head(f"{title} · {tag}",
                f"{promise[:150]}", depth=depth) + F1+F2+F3+F4+F5+F6+F7+F8+F9+F10+F11+F12+F13 + foot(depth)
    out = ROOT/"pages"/subfolder/f"{cid}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)

def build_all_courses():
    for cid in DATA.keys():
        build_course(cid)

# ---------- Pricing ----------
def build_pricing():
    depth = 0
    F1 = '''
<section class="hero hero-full section-ink" data-fold="1">
  <video class="hero-video" autoplay muted loop playsinline preload="metadata" poster="assets/img/course-ci2.jpg">
    <source src="assets/video/firenze-arno.mp4" type="video/mp4">
  </video>
  <div class="hero-scrim hero-scrim-diagonal"></div>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="eyebrow eyebrow-live">Simple pricing · Billed in United States dollars</span>
      <h1 class="hero-h1">One live curriculum. <em class="gold-ital">Three ways to pay.</em></h1>
      <p class="hero-sub">Every plan gives you the full live curriculum. The only choice is how long a commitment you want to make, and how much you want to save by choosing a longer one.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="#plans">See the three plans</a>
        <a class="btn btn-ghost" href="#refund">Read the seven day refund</a>
      </div>
      <div class="trustpilot-strip"><span class="tp-stars">★★★★★</span><span class="tp-score">Trustpilot 4.8 / 5</span><span class="tp-count">on 2,140 verified reviews</span></div>
    </div>
    <div class="hero-visual"><div class="hero-video-right radial-mask"><img src="assets/img/zoom-classroom-chiara.jpg" alt="A live class in progress" width="720" height="540"></div></div>
  </div>
</section>'''
    F2 = '''
<section class="section section-ink stat-row-band" data-fold="2">
  <div class="wrap stat-row">
    <div class="chip-stat"><span class="cs-num">$62 / wk</span><span class="cs-lab">annual plan, best value</span></div>
    <div class="chip-stat"><span class="cs-num">7 days</span><span class="cs-lab">full refund, always</span></div>
    <div class="chip-stat"><span class="cs-num">No fees</span><span class="cs-lab">no enrolment, no exam</span></div>
    <div class="chip-stat"><span class="cs-num">USD</span><span class="cs-lab">every plan billed in dollars</span></div>
  </div>
</section>'''
    F3 = '''
<section class="section section-travertine pricing-band" id="plans" data-fold="3">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The three plans</span>
      <h2 class="h2-editorial">Pick the length of your <em class="gold-ital">commitment</em>.</h2>
      <p class="section-lede">The curriculum is identical on every plan. Choose by how you like to pay, and by how sure you are that a full year is right for you.</p>
    </div>
    <div class="pricing-grid pricing-grid-big">
      <article class="price-card">
        <span class="pc-name">Monthly</span>
        <span class="pc-price"><em>$84</em> <span class="pc-unit">/ week</span></span>
        <p class="pc-note">Billed $336 monthly. Cancel anytime after the first month.</p>
        <ul class="pc-list">
          <li>All live lessons on your chosen track</li>
          <li>Full access to Biagio, the AI coach</li>
          <li>Cultural library and cinema club</li>
          <li>Priority advisor support</li>
          <li>Class recordings the same evening</li>
        </ul>
        <a class="btn btn-ghost btn-gold" href="#reserve">Start monthly</a>
      </article>
      <article class="price-card price-card-featured">
        <span class="pc-chip">Best value · Save $440 a year</span>
        <span class="pc-name">Annual</span>
        <span class="pc-price"><em>$62</em> <span class="pc-unit">/ week</span></span>
        <p class="pc-note">Billed once at $3,224 for the year. Save 26 percent on the monthly rate.</p>
        <ul class="pc-list">
          <li>Everything included in the monthly plan</li>
          <li>Two free cultural capsule sessions</li>
          <li>Priority placement with a preferred teacher</li>
          <li>Printed CEFR certificate on completion</li>
          <li>Guest invitations to two live cultural events</li>
        </ul>
        <a class="btn btn-primary" href="#reserve">Start annual</a>
      </article>
      <article class="price-card">
        <span class="pc-name">Term</span>
        <span class="pc-price"><em>$73</em> <span class="pc-unit">/ week</span></span>
        <p class="pc-note">Billed $876 for one full term of twelve weeks.</p>
        <ul class="pc-list">
          <li>All twenty live lessons of one term</li>
          <li>Full access to Biagio for the whole term</li>
          <li>Placement interview included</li>
          <li>End of stage certificate</li>
          <li>No auto-renewal</li>
        </ul>
        <a class="btn btn-ghost btn-gold" href="#reserve">Start a term</a>
      </article>
    </div>
  </div>
</section>'''
    inc = [
        "All live small-group lessons on your track",
        "Placement interview with a real academic advisor",
        "Full access to Biagio, our AI conversation coach",
        "Recordings of every class, sent the same evening",
        "Weekly personal note from your teacher",
        "Cultural library of films, articles and readings",
        "Live monthly cultural masterclass with a guest speaker",
        "End of stage oral and written CEFR assessment",
        "Printed CEFR certificate on the annual plan",
        "Seven day full refund after your first live class",
    ]
    inc_html = "".join(f'<li class="inc-item"><span class="inc-check"><em>✓</em></span><span class="inc-text">{i}.</span></li>' for i in inc)
    F4 = f'''
<section class="section section-cream included-band" data-fold="4">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Everything included</span>
      <h2 class="h2-editorial">Ten things every learner receives, <em class="gold-ital">on every plan</em>.</h2>
    </div>
    <ul class="included-list included-2col">{inc_html}</ul>
  </div>
</section>'''
    F5 = '''
<section class="section section-verona pull-quote-band" data-fold="5">
  <div class="wrap"><blockquote class="pull-quote"><em>The classroom is a Roman apartment. The teacher is Marco. The price is honest.</em></blockquote><p class="pq-attr">Diane Weller · Chicago · alumna of CI Principiante</p></div>
</section>'''
    tp = [
        ("Diane Weller","Chicago","CI Principiante","student-diane.jpg","In three months I ordered dinner in Trastevere and the waiter answered in Italian for the whole meal."),
        ("Robert Hensley","Austin","Parliamo · A Tavola","student-robert.jpg","The teacher cooks while she teaches. That single fact changed how I hear the language."),
        ("Sarah Kim","San Francisco","Capsule · L'Opera","student-sarah.jpg","I read the libretto of La Bohème with Alessandro over six sessions. I now understand why Italians cry at the third act."),
        ("James Whitaker","London","CI Elementare","student-james.jpg","Small classes, real corrections, no drills. It felt like being tutored at a Florentine institute."),
        ("Linda Bauer","Toronto","CI Intermedio","student-linda.jpg","Chiara caught a mistake I had been making since 2014. In one live class."),
        ("Michael O'Rourke","Boston","Parliamo · Chiacchierando","student-michael.jpg","I now argue about football with my Italian in-laws. Poorly. But in Italian, which is the point."),
    ]
    tp_html = "".join(f'<article class="tp-card"><div class="tpc-head"><img class="tpc-avatar" src="assets/img/{img}" alt="{n}" loading="lazy"><div class="tpc-meta"><span class="tpc-name">{n}</span><span class="tpc-place">{c} · {co}</span></div></div><div class="tpc-stars">★★★★★</div><blockquote class="tpc-quote"><em>{q}</em></blockquote><span class="tpc-verified">✓ Verified Trustpilot review</span></article>' for n,c,co,img,q in tp)
    F6 = f'''
<section class="section section-travertine trustpilot-band" data-fold="6">
  <div class="wrap">
    <div class="trustpilot-aggregate"><span class="tp-stars-large">★★★★★</span><span class="tp-agg-score">4.8 / 5</span><span class="tp-agg-count">Trustpilot · 2,140 verified reviews</span></div>
    <div class="section-head"><span class="eyebrow">The learners</span><h2 class="h2-editorial">Real learners. <em class="gold-ital">Real value.</em></h2></div>
    <div class="tp-wall card-slider">{tp_html}</div>
  </div>
</section>'''
    F7 = '''
<section class="section section-cream refund-band" id="refund" data-fold="7">
  <div class="wrap two-col">
    <div class="tc-copy">
      <span class="eyebrow">The refund</span>
      <h2 class="h2-editorial">Seven full days. <em class="gold-ital">No form. No question.</em></h2>
      <p class="lead">Sit your first live class. If it is not for you, write a one-line email to your advisor within seven days. Every dollar is returned to your card the same working day.</p>
      <p>We do this because we believe the first live class is the honest test of the school, and we would rather you leave freely than stay unhappy.</p>
    </div>
    <div class="tc-visual">
      <div class="payment-methods">
        <span class="pm-eyebrow">We accept</span>
        <div class="pm-row">
          <span class="pm-chip">Visa</span><span class="pm-chip">Mastercard</span><span class="pm-chip">American Express</span><span class="pm-chip">PayPal</span><span class="pm-chip">Apple Pay</span><span class="pm-chip">Google Pay</span>
        </div>
        <p class="pm-note">All payments processed by Stripe and PayPal on TLS 1.3 encrypted channels. Every card is verified with 3D Secure.</p>
      </div>
    </div>
  </div>
</section>'''
    faqs = [
        ("How much does the whole year cost on the annual plan?","The full year on the annual plan is billed once at $3,224. That is the equivalent of $62 a week, and saves $440 compared to paying monthly for the same year."),
        ("Can I switch from monthly to annual later?","Yes. You can upgrade to annual at any time and we credit the months you have already paid against the annual price."),
        ("Is there an enrolment fee or a materials fee?","No. Every fee is included in your plan price. There is no enrolment fee, no materials fee and no exam fee."),
        ("Do I have to pay in United States dollars?","Yes. All plans are billed in USD. Your card will handle the conversion at the day's exchange rate if you are outside the United States."),
        ("What if I want to pause my learning?","Annual learners may pause once per year for up to eight weeks without extra cost. Monthly learners can simply cancel and rejoin at any time."),
        ("What does the seven day refund cover?","It covers everything you have paid. If within seven days of your first live class you decide the school is not right for you, we return every dollar without a form."),
    ]
    faq_html = "".join(f'<details class="faq-item"><summary><span class="faq-q">{q}</span><span class="faq-toggle">＋</span></summary><div class="faq-a">{a}</div></details>' for q,a in faqs)
    F8 = f'''
<section class="section section-travertine faq-band" data-fold="8">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Pricing questions</span><h2 class="h2-editorial">Everything <em class="gold-ital">worth asking about money</em>.</h2></div>
    <div class="faq-list">{faq_html}</div>
  </div>
</section>'''
    F9 = '''
<section class="section section-verona final-cta" data-fold="9" id="reserve">
  <div class="wrap final-inner">
    <div class="fc-copy"><h2 class="h2-huge">Reserve your <em class="gold-ital">placement call</em>.</h2><p class="fc-lede">Thirty minutes. Spoken in English. Ends with a clear recommendation and a start date. No obligation to enrol.</p></div>
    <form class="fc-form paper-glass" novalidate>
      <div class="ff-row"><label>Your name<input type="text" name="name" required placeholder="Full name"></label></div>
      <div class="ff-row"><label>Email<input type="email" name="email" required placeholder="you@email.com"></label></div>
      <div class="ff-row"><label>Phone<input type="tel" name="phone" required placeholder="+1 555 000 0000"></label></div>
      <div class="ff-row"><label>Preferred plan<select name="plan" required><option value="">Choose a plan</option><option>Monthly</option><option>Annual</option><option>Single term</option><option>Not sure yet</option></select></label></div>
      <button class="btn btn-primary btn-block" type="submit">Reserve my placement call</button>
      <p class="ff-note">We reply within one working day. No sales script, no pressure.</p>
    </form>
  </div>
</section>'''
    html = head("Pricing", "Simple pricing for Club Italia. Three plans, one live curriculum, seven day full refund.", depth=0) + F1+F2+F3+F4+F5+F6+F7+F8+F9 + foot(0)
    (ROOT/"pricing.html").write_text(html)

if __name__ == "__main__":
    build_all_courses()
    build_pricing()
    print("courses & pricing built.")
