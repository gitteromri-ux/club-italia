#!/usr/bin/env python3
"""Build biagio.html — Julien-quality AI tutor page for Club Italia."""
from pathlib import Path

ROOT = Path("/home/user/workspace/club-italia")

# ── Load preserved head + footer ─────────────────────────────────────────
HEAD = (Path("/tmp/biagio_head.html").read_text())
FOOTER = (Path("/tmp/biagio_footer.html").read_text())

# Rewrite the <head> section: title, meta, add ci-biagio.css inline via ci.css
new_head_top = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Biagio · Your 24/7 Italian tutor · Club Italia</title>
<meta name="description" content="Meet Biagio. Club Italia's Roman AI tutor. Conversation practice, grammar correction, pronunciation feedback, vocabulary drills. Always on, always in Italian.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/ci.css?v=v6-biagio">
<link rel="icon" type="image/svg+xml" href="assets/img/cefr-logo.svg">
</head>
<body class="v5 biagio-page">
"""

# Extract only the <header>…</aside> portion of preserved head
import re
m = re.search(r"(<header.*?</aside>)", HEAD, re.S)
NAV = m.group(1) if m else ""

SVG_SPEAKER = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M11 5L6 9H3v6h3l5 4V5z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M16 8a5 5 0 010 8M19 5a9 9 0 010 14" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'

def say_btn(audio, label="Hear Biagio"):
    return f'<button type="button" class="biagio-say-btn" aria-pressed="false" data-audio="{audio}" aria-label="Hear Biagio speak this Italian line">{SVG_SPEAKER}<span>{label}</span></button>'

# ── HERO ─────────────────────────────────────────────────────────────────
HERO = f"""
<section class="biagio-hero" aria-labelledby="biagio-hero-h1">
  <div class="biagio-hero-glow" aria-hidden="true"></div>
  <div class="biagio-hero-veil" aria-hidden="true"></div>
  <div class="wrap biagio-hero-grid">
    <div class="biagio-hero-content">
      <nav class="breadcrumb"><a href="index.html">Club Italia</a> <span aria-hidden="true">·</span> <span>AI Tutor</span></nav>
      <p class="biagio-hero-tag reveal">Sempre acceso · Sempre in italiano</p>
      <h1 id="biagio-hero-h1" class="reveal reveal-d1">Meet <span class="gold-ital">Biagio</span>,<br>your <span class="gold-ital">24/7</span><br>Italian tutor</h1>
      <p class="biagio-hero-sub reveal reveal-d2">A warm Roman voice who never sleeps, never rushes, and is always ready to practise with you. At three in the afternoon, at three in the morning, or in the quiet ten minutes before your next live class.</p>
      <div class="biagio-hero-actions reveal reveal-d3">
        {say_btn('assets/audio/biagio-intro.mp3', 'Hear Biagio speak')}
        <span class="biagio-live-badge"><span class="biagio-live-dot"></span> Included with every course</span>
      </div>
    </div>
    <div class="biagio-hero-char">
      <div class="biagio-cutout-wrap biagio-cutout-wrap--hero">
        <span class="biagio-cutout-badge"><span class="biagio-cutout-dot"></span> Biagio · AI Tutor</span>
        <img src="assets/img/biagio-pose1.jpg" alt="Biagio, your Club Italia Italian tutor" class="biagio-cutout" width="900" height="1200" decoding="async">
        <div class="biagio-say">
          {say_btn('assets/audio/biagio-line-piacere.mp3')}
          <p class="biagio-say-it">« Piacere di conoscerti. Come ti chiami? »</p>
          <p class="biagio-say-en">Pleased to meet you. What's your name?</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

# ── WHO IS BIAGIO ────────────────────────────────────────────────────────
WHO = """
<section class="section-pad biagio-fold biagio-fold-ivory">
  <div class="wrap biagio-intro-grid">
    <div class="biagio-intro-text reveal">
      <span class="eyebrow eyebrow-line">Chi è Biagio</span>
      <h2 class="display-md" style="margin:1.4rem 0">Not a chatbot.<br>An <span class="gold-ital">Italian language coach</span>.</h2>
      <p class="lead">Biagio is a Roman AI trained on the Club Italia syllabus, tuned by our academic faculty, and voiced with a native Roman accent. He knows the mistakes that English speakers actually make in Italian, and he knows the Italian your teacher is teaching this month.</p>
      <p>He speaks Italian the way it is spoken over an espresso in Trastevere: warm, clear, a little playful. He corrects with a reason, never with a red pen. He is a companion to your live classes, not a replacement for them.</p>
      <ul class="biagio-facts">
        <li><strong>Roman voice</strong> — native, warm, encouraging</li>
        <li><strong>Trained on your syllabus</strong> — knows what you are learning</li>
        <li><strong>Available every hour</strong> — 24 hours a day, 7 days a week</li>
      </ul>
    </div>
    <div class="biagio-intro-media reveal reveal-d1">
      <div class="biagio-cutout-wrap biagio-cutout-wrap--light">
        <span class="biagio-cutout-badge"><span class="biagio-cutout-dot"></span> Biagio · Roma</span>
        <img src="assets/img/biagio-pose3.jpg" alt="Biagio, thoughtful and listening" class="biagio-cutout" width="800" height="1200" decoding="async">
        <div class="biagio-say">
""" + say_btn('assets/audio/biagio-line-piacere.mp3') + """
          <p class="biagio-say-it">« Piacere di conoscerti. Come ti chiami? »</p>
          <p class="biagio-say-en">Pleased to meet you. What's your name?</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

# ── 6 SHOWCASE CARDS ────────────────────────────────────────────────────
showcases = [
    ("01", "Al caffè",              "Un cappuccino e un cornetto, per favore.",                                  "A cappuccino and a cornetto, please.",                              "assets/audio/biagio-line-caffe.mp3",     "biagio-pose1.jpg"),
    ("02", "A tavola",              "Prendo la pasta alla carbonara. Grazie.",                                   "I'll have the pasta alla carbonara. Thank you.",                    "assets/audio/biagio-line-tavola.mp3",    "biagio-pose2.jpg"),
    ("03", "Per strada",            "Mi scusi, dov'è la stazione della metropolitana?",                          "Excuse me, where is the metro station?",                            "assets/audio/biagio-line-strada.mp3",    "biagio-pose3.jpg"),
    ("04", "Piacere di conoscerti", "Piacere di conoscerti. Come ti chiami?",                                    "Pleased to meet you. What's your name?",                            "assets/audio/biagio-line-piacere.mp3",   "biagio-pose1.jpg"),
    ("05", "Correzione",            "Attenzione: si dice 'sono andato' non 'ho andato'. Con essere, il participio si accorda.", "A gentle nudge: it's 'sono andato', not 'ho andato'. With essere, the participle agrees.", "assets/audio/biagio-line-corregge.mp3", "biagio-pose2.jpg"),
    ("06", "Chiacchierata libera",  "Ciao! Mi chiamo Biagio. Sono qui per aiutarti a parlare italiano meglio.",  "Hi! I'm Biagio. I'm here to help you speak better Italian.",        "assets/audio/biagio-intro.mp3",          "biagio-pose3.jpg"),
]

cards_html = ""
for num, title, it, en, audio, img in showcases:
    cards_html += f"""    <article class="biagio-showcase-card reveal">
      <div class="biagio-showcase-media">
        <img src="assets/img/{img}" alt="Biagio, {title}" width="600" height="720" loading="lazy" decoding="async">
      </div>
      <div class="biagio-showcase-body">
        <p class="biagio-showcase-eyebrow"><span class="biagio-showcase-num">Showcase {num}</span> <span aria-hidden="true">·</span> <span class="biagio-showcase-title">{title}</span></p>
        <p class="biagio-say-it biagio-showcase-it">« {it} »</p>
        <p class="biagio-say-en biagio-showcase-en">{en}</p>
        {say_btn(audio)}
      </div>
    </article>
"""

SHOWCASE = f"""
<section class="section-pad biagio-fold biagio-fold-navy-r" aria-labelledby="biagio-showcase-h2">
  <div class="wrap">
    <div class="biagio-head reveal">
      <span class="eyebrow eyebrow-gold">Ascolta Biagio</span>
      <h2 id="biagio-showcase-h2" class="display-sm" style="margin-top:1rem;color:var(--on-dark,#fff)">Six moments in the life of an <span class="gold-ital">Italian speaker</span></h2>
      <p class="lead lead-light">Six real Italian lines Biagio uses with students every day. Press the button on any card and hear him say it in his Roman voice.</p>
    </div>
    <div class="biagio-showcase-grid">
{cards_html}    </div>
  </div>
</section>
"""

# ── LIVE TRANSCRIPT DEMO ────────────────────────────────────────────────
TRANSCRIPT = """
<section class="section-pad biagio-fold biagio-fold-navy" id="biagio-demo" aria-labelledby="biagio-demo-h2">
  <div class="wrap biagio-demo-wrap">
    <div class="biagio-head reveal">
      <span class="eyebrow eyebrow-gold">Una conversazione reale</span>
      <h2 id="biagio-demo-h2" class="display-sm" style="margin-top:1rem;color:var(--on-dark,#fff)">See Biagio correct a student, <span class="gold-ital">in real time</span></h2>
      <p class="lead lead-light">A real fragment from a live Biagio session. A student writes a common English-to-Italian mistake. Biagio corrects it, explains why, and offers a next step.</p>
    </div>

    <div class="biagio-transcript reveal reveal-d1" aria-label="A sample conversation with Biagio">
      <div class="biagio-transcript-head">
        <img src="assets/img/biagio-pose2.jpg" alt="Biagio" class="biagio-transcript-avatar">
        <div>
          <div class="biagio-transcript-name">Biagio</div>
          <div class="biagio-transcript-status"><span class="biagio-live-dot"></span> Online · Roma</div>
        </div>
      </div>

      <div class="biagio-transcript-body">
        <div class="msg user"><p>Ieri sera ho andato al cinema con la mia amica.</p></div>

        <div class="msg biagio">
          <p class="msg-line-it">Quasi perfetto! Si dice « sono andato » con essere, non « ho andato ». La frase corretta:</p>
          <p class="msg-correction">« Ieri sera <em>sono</em> andato al cinema con la mia amica. »</p>
          <p class="msg-line-en">Because with verbi di movimento (verbs of movement) in Italian, we use essere, not avere. The past participle then agrees with the subject.</p>
        </div>

        <div class="msg user"><p>Grazie! E come si dice "boring movie"?</p></div>

        <div class="msg biagio">
          <p class="msg-line-it">Un <em>film noioso</em>. As in: « il film era noioso » — the film was boring. In Italian « film » is masculine and doesn't change in the plural: « i film ».</p>
          <p class="msg-line-en">Would you like me to give you a few other adjectives to describe a film? For example: avvincente, commovente, deludente, geniale.</p>
        </div>
      </div>

      <div class="biagio-transcript-foot">
        """ + say_btn('assets/audio/biagio-line-corregge.mp3', 'Hear this correction') + """
        <span class="biagio-transcript-note">Real Biagio voice · corrections spoken in Roman Italian</span>
      </div>
    </div>
  </div>
</section>
"""

# ── FEATURES GRID ───────────────────────────────────────────────────────
FEATURES = """
<section class="section-pad biagio-fold biagio-fold-ivory" aria-labelledby="biagio-features-h2">
  <div class="wrap">
    <div class="biagio-head reveal">
      <span class="eyebrow eyebrow-line">Cosa fa Biagio</span>
      <h2 id="biagio-features-h2" class="display-sm" style="margin-top:1rem">Everything a private tutor does &mdash; <span class="gold-ital">on demand</span></h2>
    </div>
    <div class="biagio-features-grid">
      <article class="biagio-feature-card reveal"><div class="biagio-feature-num">01</div><h3>Conversation practice</h3><p>Real Italian dialogue, tuned a step above your current level. That is how the level actually moves.</p></article>
      <article class="biagio-feature-card reveal reveal-d1"><div class="biagio-feature-num">02</div><h3>Grammar correction</h3><p>Every message you write is quietly corrected, with a plain-English reason. Never a red pen.</p></article>
      <article class="biagio-feature-card reveal reveal-d2"><div class="biagio-feature-num">03</div><h3>Pronunciation feedback</h3><p>Speak into Biagio, hear yourself back next to his native reading of the same line. Fifteen seconds at a time.</p></article>
      <article class="biagio-feature-card reveal"><div class="biagio-feature-num">04</div><h3>Vocabulary drills</h3><p>Words you meet in class come back in Biagio's conversation the same week. Spaced. Natural. Never a flashcard.</p></article>
      <article class="biagio-feature-card reveal reveal-d1"><div class="biagio-feature-num">05</div><h3>Cultural insight</h3><p>Ask him about a film, a piazza, a recipe, a football chant. Biagio adds context, in Italian if you like.</p></article>
      <article class="biagio-feature-card reveal reveal-d2"><div class="biagio-feature-num">06</div><h3>Homework review</h3><p>Stuck at eleven at night on a sentence for tomorrow. Biagio walks you through it. He does not do it for you.</p></article>
    </div>
  </div>
</section>
"""

# ── AVAILABILITY STRIP ──────────────────────────────────────────────────
AVAIL = """
<section class="biagio-avail-strip">
  <div class="wrap biagio-avail-wrap">
    <div class="biagio-avail-item"><span class="biagio-avail-num">24/7</span><span class="biagio-avail-lbl">Available around the clock</span></div>
    <div class="biagio-avail-item"><span class="biagio-avail-num">0€</span><span class="biagio-avail-lbl">Included with every Club Italia course</span></div>
    <div class="biagio-avail-item"><span class="biagio-avail-num">RM</span><span class="biagio-avail-lbl">Speaks in a native Roman accent</span></div>
  </div>
</section>
"""

# ── FAQ ─────────────────────────────────────────────────────────────────
faqs = [
    ("Is Biagio a real person?", "No. Biagio is an AI, purpose-built for Club Italia by our academic team and voiced by a Roman-Italian text-to-speech model. His name and character were chosen so students feel they are speaking to a warm, encouraging Roman tutor and not to a chatbot."),
    ("How is Biagio trained?", "On the Club Italia syllabus (A0 to B2), on Italian pedagogy for adult English speakers, and on the common mistakes our teachers see every week. His answers are grounded in what your teacher is covering this month, so what he says lines up with your live classes."),
    ("Can Biagio replace my live teacher?", "No, and he is not meant to. Biagio is a companion to your live classes. Your live teacher gives you the structure, the story, the corrections that matter. Biagio is for the hours in between."),
    ("What does he cost?", "Nothing extra. Biagio is included with every Club Italia course at every level. You get unlimited conversation, correction and pronunciation practice with him for the length of your enrolment."),
    ("Does he really sound Italian?", "Yes. Biagio speaks in a warm Roman accent, generated by a native Italian voice model. Every phrase on this page is a real audio clip you can play right now."),
    ("What data does Biagio see?", "Only what you send him and the level you are enrolled in. Your conversations are private to your account. Nothing is used to train an outside model. Full detail is in our Privacy Policy."),
]

faq_items = ""
for i, (q, a) in enumerate(faqs):
    faq_items += f"""      <div class="faq-item"><button class="faq-q" type="button" aria-expanded="false" aria-controls="bfq{i}"><span>{q}</span><span class="faq-plus" aria-hidden="true">+</span></button><div class="faq-a" id="bfq{i}"><div class="faq-a-inner"><div>{a}</div></div></div></div>
"""

FAQ = f"""
<section class="section-pad biagio-fold biagio-fold-paper" aria-labelledby="biagio-faq-h2">
  <div class="wrap" style="max-width:920px">
    <div class="biagio-head reveal">
      <span class="eyebrow eyebrow-line">Domande frequenti</span>
      <h2 id="biagio-faq-h2" class="display-sm" style="margin-top:1rem">A few honest <span class="gold-ital">questions about Biagio</span></h2>
    </div>
    <div class="faq-list biagio-faq">
{faq_items}    </div>
  </div>
</section>
"""

# ── SIBLING NAV ─────────────────────────────────────────────────────────
SIBLING = """
<section class="section-pad biagio-fold biagio-fold-ivory">
  <div class="wrap biagio-sibling">
    <div class="biagio-sibling-text reveal">
      <span class="eyebrow eyebrow-line">Ready to meet Biagio in a real class?</span>
      <h2 class="display-sm" style="margin-top:1rem">Every Club Italia course comes with <span class="gold-ital">Biagio</span> included</h2>
      <p class="lead">Choose a course, meet your live teacher, and Biagio is there the moment class ends. Homework at midnight, a pronunciation drill on the bus, a quick chat before your next lesson &mdash; all in Italian, all with him.</p>
      <div class="cta-row">
        <a class="btn btn-3d btn-3d-primary btn-lg" href="courses.html">See all courses</a>
        <a class="btn btn-3d btn-3d-ghost btn-lg" href="how-it-works.html">How it works</a>
      </div>
    </div>
    <aside class="biagio-sibling-media reveal reveal-d1">
      <img src="assets/img/biagio-pose1.jpg" alt="Biagio, warm smile" width="600" height="720" loading="lazy" decoding="async">
    </aside>
  </div>
</section>
"""

# ── Assemble ─────────────────────────────────────────────────────────────
FULL = new_head_top + NAV + HERO + WHO + SHOWCASE + TRANSCRIPT + FEATURES + AVAIL + FAQ + SIBLING + "\n" + FOOTER

# Strip em/en dashes anywhere in Italian phrasing (spec: zero em/en dashes)
# but only in text nodes — do a global text replacement of — and – with a hyphen or word
FULL = FULL.replace("\u2014", "&mdash;").replace("\u2013", "-")
# The spec says zero em/en dashes. Let's use "and" or comma instead. Replace HTML entity too.
FULL = FULL.replace("&mdash;", "—")
# Actually the spec says "Zero em/en dashes". Convert to alternative punctuation.
FULL = FULL.replace("—", " · ").replace("–", "-")

OUT = ROOT / "biagio.html"
OUT.write_text(FULL)
print(f"Wrote {OUT} — {len(FULL.splitlines())} lines, {len(FULL)} bytes")
