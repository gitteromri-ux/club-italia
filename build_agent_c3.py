"""Agent C part 3 — deepen 11 blog posts in place.

For each existing blog post, we:
  1. keep the hero + article intact
  2. wrap the article body in a two-column layout with a Reading Notes sidebar
  3. insert 2-3 pull-quote bands between paragraphs
  4. insert an "In your next class" callout linking to a specific course
  5. append a "Continue reading" 3-post footer
"""
import re, pathlib, random
ROOT = pathlib.Path("/home/user/workspace/club-italia")

# blog-scoped CSS block, inserted once inside <head>
BLOG_CSS = """
<style>
.post-body-grid{display:grid;grid-template-columns:1fr 320px;gap:4rem;max-width:1160px;margin:0 auto;padding:0 clamp(1.4rem,3vw,3rem);align-items:start}
@media (max-width:960px){.post-body-grid{grid-template-columns:1fr;gap:2.6rem}}
.post-main h2{font-family:var(--serif);font-weight:600;font-size:clamp(1.7rem,2.6vw,2.4rem);line-height:1.14;color:var(--navy);margin:2.4rem 0 1rem}
.post-main h2:first-child{margin-top:0}
.post-main p.lead{font-size:1.14rem;line-height:1.78;color:var(--on-light);margin-bottom:1.4rem;font-weight:400}
.post-main p.lead:first-of-type::first-letter{font-family:var(--serif);float:left;font-size:4.6rem;line-height:.88;padding:.3rem .55rem 0 0;color:var(--terra-deep);font-weight:600}
.post-sidebar{position:sticky;top:6rem;background:var(--ivory);border:1px solid var(--gold-line-soft);padding:1.8rem 1.6rem;font-size:.95rem}
@media (max-width:960px){.post-sidebar{position:static}}
.post-sidebar .rn-eyebrow{font-size:.7rem;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-deep);margin-bottom:1rem;display:block;font-weight:600}
.post-sidebar h4{font-family:var(--serif);font-size:1.35rem;color:var(--navy);margin-bottom:1rem;line-height:1.15}
.post-sidebar dl{margin:0;padding:0}
.post-sidebar dt{font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold-deep);margin-top:1rem}
.post-sidebar dt:first-of-type{margin-top:0}
.post-sidebar dd{margin:.25rem 0 0;font-family:var(--serif);font-size:1.05rem;color:var(--navy);line-height:1.4}
.post-sidebar .rn-tip{margin-top:1.4rem;padding-top:1.2rem;border-top:1px solid var(--gold-line-soft);font-style:italic;color:var(--on-light-soft);line-height:1.55}

.post-pull{margin:2.8rem -1rem;padding:2.4rem 2.4rem;border-top:1px solid var(--gold-line);border-bottom:1px solid var(--gold-line);background:linear-gradient(180deg,rgba(201,162,75,.06),rgba(201,162,75,0))}
.post-pull p{font-family:var(--serif);font-style:italic;font-size:clamp(1.4rem,2.4vw,1.9rem);line-height:1.35;color:var(--navy);margin:0;max-width:34ch}
.post-pull p::before{content:"\\201C";color:var(--gold-deep);font-size:1.4em;line-height:0;position:relative;top:.2em;margin-right:.1em}
.post-pull p::after{content:"\\201D";color:var(--gold-deep);font-size:1.4em;line-height:0;position:relative;top:.2em;margin-left:.05em}

.post-cta-box{margin:2.4rem 0;padding:2.2rem 2rem;background:var(--navy);color:var(--on-dark);border-left:4px solid var(--gold)}
.post-cta-box .cta-eyebrow{font-size:.72rem;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-soft);margin-bottom:.9rem;font-weight:600;display:block}
.post-cta-box h3{font-family:var(--serif);font-size:1.55rem;color:var(--on-dark);margin-bottom:.7rem;line-height:1.15}
.post-cta-box p{font-size:1rem;color:var(--on-dark-soft);line-height:1.6;margin-bottom:1.2rem}
.post-cta-box a.cta-link{display:inline-flex;align-items:center;gap:.6rem;font-size:.8rem;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-soft);border-bottom:1px solid var(--gold-line);padding-bottom:.35rem;font-weight:600}

.post-continue{background:var(--ivory);padding:clamp(4rem,7vw,6rem) 0}
.post-continue .section-head{margin-bottom:2.6rem}
.post-continue h2{font-family:var(--serif);color:var(--navy)}
.post-continue-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem}
@media (max-width:820px){.post-continue-grid{grid-template-columns:1fr}}
.post-continue-card{background:var(--white);border:1px solid var(--gold-line-soft);overflow:hidden;text-decoration:none;color:inherit;transition:all .3s var(--ease);display:flex;flex-direction:column}
.post-continue-card:hover{transform:translateY(-3px);box-shadow:0 12px 32px rgba(58,14,18,.14)}
.post-continue-card .pcc-img{aspect-ratio:16/10;overflow:hidden;background:var(--cream)}
.post-continue-card .pcc-img img{width:100%;height:100%;object-fit:cover;transition:transform .8s var(--ease)}
.post-continue-card:hover .pcc-img img{transform:scale(1.04)}
.post-continue-card .pcc-body{padding:1.6rem 1.6rem 1.8rem;flex:1;display:flex;flex-direction:column}
.post-continue-card .pcc-eyebrow{font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-deep);margin-bottom:.7rem;font-weight:600}
.post-continue-card h3{font-family:var(--serif);font-size:1.35rem;color:var(--navy);line-height:1.15;margin-bottom:.6rem}
.post-continue-card p{font-size:.94rem;color:var(--on-light-soft);line-height:1.5;margin-bottom:1rem}
.post-continue-card .pcc-cta{margin-top:auto;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--terra-deep);font-weight:600}
</style>
"""

# Per-post configuration: sidebar, pull-quotes (indexes to insert after which h2), CTA target, continue reading
POSTS = {
  "americans-italy.html": {
    "sidebar": {
      "title":"Reading Notes",
      "meta":[("Read time","8 minutes"),("Level","B1 · Intermediate"),("New Italian words","fascino, meta, itinerario, dogana, viaggiatore"),("Filed under","Travel · Contemporary Italy")],
      "tip":"If you plan to travel this year, take our Parliamo Iniziamo cohort before you go, four weeks and you will order in Italian on arrival."
    },
    "pulls":["Italy is not on the itinerary because it is convenient. Italy is on the itinerary because it is Italy.",
             "The American traveller who returns from Italy speaking a little of the language returns with a different Italy."],
    "cta":{"eyebrow":"In your next class","title":"Practise arrival Italian in Parliamo Iniziamo.","body":"A four-week spoken cohort designed around the exact conversations you will have in an Italian airport, hotel and trattoria.","href":"../courses/ci2.html","label":"See the syllabus"},
    "continue":["aperitivo","dual-citizenship","italian-coffee"]
  },
  "aperitivo.html": {
    "sidebar":{
      "title":"Reading Notes",
      "meta":[("Read time","6 minutes"),("Level","A2 · Elementary"),("New Italian words","vermut, spritz, apericena, stuzzichini, salatini"),("Filed under","Culture · Milano")],
      "tip":"The Milanese aperitivo has its own vocabulary. We drill it, in context, in Parliamo Chiacchierando."
    },
    "pulls":["Aperitivo is a shared, social ritual. It is taken standing, with friends. It is not a solitary sitting-and-scrolling drink.",
             "The Milanese did not invent vermouth. They invented the ritual that put vermouth at the centre of the evening."],
    "cta":{"eyebrow":"In your next class","title":"Hold a full aperitivo conversation in Italian.","body":"Parliamo Chiacchierando dedicates one full session to the vocabulary and register of the Milanese aperitivo.","href":"../spoken/ps4.html","label":"See the course"},
    "continue":["italian-coffee","ragu-alla-bolognese","americans-italy"]
  },
  "dual-citizenship.html": {
    "sidebar":{
      "title":"Reading Notes",
      "meta":[("Read time","10 minutes"),("Level","B1 · Intermediate"),("New Italian words","cittadinanza, discendenza, consolato, riconoscimento, avo"),("Filed under","Culture · Bureaucracy")],
      "tip":"The B1 Italian language exam is now required for citizenship. Our CI Avanzato is calibrated to that exam."
    },
    "pulls":["The 2025 reform did not close the door. It moved the door. And it demanded you speak, in Italian, before you walked through it.",
             "Citizenship in the country of one's grandparents is not, in the end, a passport. It is a language."],
    "cta":{"eyebrow":"In your next class","title":"Reach B1 with CI Avanzato.","body":"CI Avanzato is our A2 to B1 track, the exact language required for the citizenship interview and the CILS B1 Cittadinanza exam.","href":"../courses/ci4.html","label":"See CI Avanzato"},
    "continue":["americans-italy","tuscan-italian","passato-prossimo"]
  },
  "italian-coffee.html": {
    "sidebar":{
      "title":"Reading Notes",
      "meta":[("Read time","7 minutes"),("Level","A2 · Elementary"),("New Italian words","tostatura, moka, macchinetta, espresso, ristretto"),("Filed under","Cuisine · Everyday Italy")],
      "tip":"Ordering coffee in Italian is the single most useful conversation for a first-time visitor. We drill it, in dialogue, in CI Principiante."
    },
    "pulls":["A cappuccino after eleven o'clock in the morning is not a rebellion. It is a category error.",
             "Espresso is not a small coffee. It is a different beverage, invented in Napoli, served in seconds, drunk in one."],
    "cta":{"eyebrow":"In your next class","title":"Order like a local in CI Principiante.","body":"CI Principiante is our A0 to A1 course, and the coffee-ordering dialogue arrives in the third session.","href":"../courses/ci1.html","label":"See CI Principiante"},
    "continue":["aperitivo","ragu-alla-bolognese","neapolitan-humour"]
  },
  "italian-golden-age.html": {
    "sidebar":{
      "title":"Reading Notes",
      "meta":[("Read time","12 minutes"),("Level","B1 · Intermediate"),("New Italian words","regista, sceneggiatura, neorealismo, dialogo, colonna sonora"),("Filed under","Cinema · Twentieth Century")],
      "tip":"Italian cinema is a magnificent teaching text. Marco runs a monthly Cinema Club for CI Intermedio students and above."
    },
    "pulls":["Neorealism was not a style. It was a decision, made after a war, to point the camera at the country and let it speak.",
             "Fellini's Rome is not a place, it is a way of remembering. Watch La dolce vita and you have entered his memory."],
    "cta":{"eyebrow":"In your next class","title":"Read a Fellini scene in the original.","body":"CI Intermedio uses short film scenes as its primary text. By the end of the course you can follow a Fellini monologue.","href":"../courses/ci3.html","label":"See CI Intermedio"},
    "continue":["neapolitan-humour","verdi-life","uffizi-italian"]
  },
  "neapolitan-humour.html": {
    "sidebar":{
      "title":"Reading Notes",
      "meta":[("Read time","6 minutes"),("Level","B1 · Intermediate"),("New Italian words","battuta, sfottò, presa in giro, arte di arrangiarsi, guagliò"),("Filed under","Culture · Napoli")],
      "tip":"Luca teaches Italian through the theatricality of Napoli. His courses are the fastest route into the humour of the south."
    },
    "pulls":["Neapolitan humour is not a joke. It is a philosophy that treats the improbable as a resource.",
             "In Napoli, laughter is not what happens after the difficulty. It is what happens inside the difficulty."],
    "cta":{"eyebrow":"In your next class","title":"Learn Italian with Luca, from Napoli.","body":"Luca De Simone teaches CI Principiante, CI Elementare and a Napoli-focused Parliamo Beginner cohort.","href":"../teachers/luca.html","label":"Meet Luca"},
    "continue":["italian-golden-age","aperitivo","ragu-alla-bolognese"]
  },
  "passato-prossimo.html": {
    "sidebar":{
      "title":"Reading Notes",
      "meta":[("Read time","9 minutes"),("Level","A2 · Elementary"),("New Italian words","ausiliare, participio passato, andato, arrivato, mangiato"),("Filed under","Language · Grammar")],
      "tip":"Every Club Italia elementary course dedicates two full sessions to the passato prossimo. You will not leave without it."
    },
    "pulls":["The passato prossimo is not a trick. It is a machine with two moving parts, and once you see the parts, you own the tense.",
             "Italian past tenses are three, not one. The passato prossimo is the one you will use most, the one you will need first, and the one that will stop scaring you the fastest."],
    "cta":{"eyebrow":"In your next class","title":"Master the passato prossimo in CI Elementare.","body":"CI Elementare introduces the passato prossimo in week three and drills it, in speech, for the rest of the course.","href":"../courses/ci2.html","label":"See CI Elementare"},
    "continue":["tuscan-italian","dual-citizenship","aperitivo"]
  },
  "ragu-alla-bolognese.html": {
    "sidebar":{
      "title":"Reading Notes",
      "meta":[("Read time","8 minutes"),("Level","A2 · Elementary"),("New Italian words","ragù, soffritto, brodo, tagliatelle, mattarello"),("Filed under","Cuisine · Emilia-Romagna")],
      "tip":"Giulia runs a monthly Cucina Live where students cook a Bolognese menu together, in Italian. Enrolled Club Italia students only."
    },
    "pulls":["Bolognese sauce, as invented in Bologna in 1891, has never contained tomato in the way you know it. It contains tomato in the way you do not.",
             "The word ragù, in Bologna, is not the name of a sauce. It is the name of a discipline that takes four hours and no shortcuts."],
    "cta":{"eyebrow":"In your next class","title":"Cook, and speak, with Giulia.","body":"Giulia Moretti runs a monthly Saturday Cucina Live in Italian, plus a full Culture Capsule on La Cucina.","href":"../culture/cap-food.html","label":"See La Cucina Capsule"},
    "continue":["aperitivo","italian-coffee","americans-italy"]
  },
  "tuscan-italian.html": {
    "sidebar":{
      "title":"Reading Notes",
      "meta":[("Read time","11 minutes"),("Level","B1 · Intermediate"),("New Italian words","volgare, dialetto, standard, unificazione, gorgia"),("Filed under","Language · History")],
      "tip":"Chiara teaches in Firenze, in the accent that gave Italy its standard. Her lessons are calibrated for adult learners."
    },
    "pulls":["Italian is not, in a sense that would please a linguist, a national language at all. It is a Tuscan dialect that won.",
             "Dante did not choose Tuscan because Tuscan was best. He chose Tuscan because Tuscan was his. That is the accident on which a national language now rests."],
    "cta":{"eyebrow":"In your next class","title":"Learn from a Florentine.","body":"Chiara Bellini teaches CI Elementare and CI Intermedio live from Firenze. Her Italian is the Italian that Dante wrote.","href":"../teachers/chiara.html","label":"Meet Chiara"},
    "continue":["passato-prossimo","dual-citizenship","uffizi-italian"]
  },
  "uffizi-italian.html": {
    "sidebar":{
      "title":"Reading Notes",
      "meta":[("Read time","7 minutes"),("Level","A2 · Elementary"),("New Italian words","tavola, tempera, olio, pala, predella"),("Filed under","Art · Firenze")],
      "tip":"Sofia's Culture Capsule L'Arte teaches art history through the Italian vocabulary that unlocks the museum."
    },
    "pulls":["Five words. That is what stands between the wall label and the painting. Learn the five, and the museum reopens.",
             "An Uffizi label written in Italian is not a translation of the English. It is the original, and the English is the translation, imperfect."],
    "cta":{"eyebrow":"In your next class","title":"Read the museum in Italian.","body":"Culture Capsule L'Arte is a six-week course on Italian art history taught in accessible Italian. Suitable from A2.","href":"../culture/cap-art.html","label":"See L'Arte Capsule"},
    "continue":["italian-golden-age","verdi-life","tuscan-italian"]
  },
  "verdi-life.html": {
    "sidebar":{
      "title":"Reading Notes",
      "meta":[("Read time","10 minutes"),("Level","B1 · Intermediate"),("New Italian words","libretto, aria, coro, palcoscenico, teatro"),("Filed under","Opera · Ottocento")],
      "tip":"Francesca's Culture Capsule L'Opera teaches Verdi and Puccini through the Italian of their librettos, at your level."
    },
    "pulls":["Verdi did not write music for Italy. Italy heard his music and decided, listening, that it was Italy.",
             "The Va, pensiero of Nabucco is not a chorus. It is the moment when a fractured peninsula recognised itself in the singing of exiles."],
    "cta":{"eyebrow":"In your next class","title":"Read Verdi in the original.","body":"Culture Capsule L'Opera runs for six weeks, one Verdi opera a session, taught in Italian at intermediate level.","href":"../culture/cap-opera.html","label":"See L'Opera Capsule"},
    "continue":["italian-golden-age","uffizi-italian","neapolitan-humour"]
  }
}

# Continue-reading catalog for card metadata
CATALOG = {
  "americans-italy": ("Travel · 24 Aug 2026","7.5 Million Americans, One Italy","Why U.S. travellers made Italy their second-most-visited country","spoken-ps1.jpg"),
  "aperitivo": ("Culture · 22 Apr 2026","The Milanese Aperitivo, Decoded","When it started, what it costs, what you actually eat","spoken-ps4.jpg"),
  "dual-citizenship": ("Culture · 15 Jul 2026","Italian Dual Citizenship, 2026","What the March 2025 reform means for Italian-descent Americans","culture.jpg"),
  "italian-coffee": ("Cuisine · 18 May 2026","Italian Coffee Is Not What You Think","A history of espresso, from Naples 1901 to your kitchen","pillar-food.jpg"),
  "italian-golden-age": ("Cinema · 10 Sep 2026","The Golden Age of Italian Cinema","How Fellini, Visconti and Rossellini rewrote what film could be","pillar-cinema.jpg"),
  "neapolitan-humour": ("Culture · 02 Jun 2026","Neapolitan Humour, Explained","The philosophy underneath the world's most laughed-in city","pillar-tradition.jpg"),
  "passato-prossimo": ("Language · 12 Aug 2026","The Passato Prossimo Is Not the Enemy","Why the Italian past tense is the friendliest tense you will meet","spoken-ps2.jpg"),
  "ragu-alla-bolognese": ("Cuisine · 28 Jul 2026","The Real Ragù alla Bolognese","And the eight things it is not","cap-food.jpg"),
  "tuscan-italian": ("Language · 18 Jun 2026","Why Italian Is Really Tuscan","Dante, Boccaccio, Petrarch and the accident of the standard","pillar-art.jpg"),
  "uffizi-italian": ("Art · 05 May 2026","How to Read an Uffizi Wall Label","The five Italian words that unlock the museum","cap-art.jpg"),
  "verdi-life": ("Opera · 01 Jul 2026","Verdi in a Life","Six operas that shaped a nation and still shape Italian","cap-opera.jpg"),
}

def build_sidebar(cfg):
    meta_html = "\n".join([f"<dt>{k}</dt><dd>{v}</dd>" for k,v in cfg["meta"]])
    return f"""<aside class="post-sidebar">
<span class="rn-eyebrow">Reading Notes</span>
<h4>{cfg['title']}</h4>
<dl>{meta_html}</dl>
<p class="rn-tip">{cfg['tip']}</p>
</aside>"""

def build_cta(cfg):
    return f"""<div class="post-cta-box">
<span class="cta-eyebrow">{cfg['eyebrow']}</span>
<h3>{cfg['title']}</h3>
<p>{cfg['body']}</p>
<a class="cta-link" href="{cfg['href']}">{cfg['label']} →</a>
</div>"""

def build_continue(slugs, filename):
    cards = []
    for s in slugs:
        if s + ".html" == filename:
            continue
        cat, title, sub, img = CATALOG[s]
        eyebrow = cat.split(" · ")[0].upper()
        cards.append(f'''<a class="post-continue-card" href="{s}.html">
<div class="pcc-img"><img src="../../assets/img/{img}" alt=""></div>
<div class="pcc-body">
<span class="pcc-eyebrow">{cat}</span>
<h3>{title}</h3>
<p>{sub}</p>
<span class="pcc-cta">Read on →</span>
</div></a>''')
    cards_html = "\n".join(cards[:3])
    return f'''<section class="post-continue">
<div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Continue Reading</span><h2 class="display-md">More from the Cultural Journal.</h2></div>
<div class="post-continue-grid">{cards_html}</div>
</div></section>'''

def deepen(path):
    fname = path.name
    cfg = POSTS[fname]
    html = path.read_text()

    # Inject CSS before </head>
    if "post-body-grid" not in html:
        html = html.replace("</head>", BLOG_CSS + "\n</head>")

    # Locate the <article class="section-paper"><div class="wrap-narrow"> ... </div></article>
    # Restructure it into a wrap + two-col layout, keep inner content.
    m = re.search(r'<article class="section-paper"><div class="wrap-narrow">\s*(.*?)</div></article>', html, re.S)
    if not m:
        # Try alternative container
        m = re.search(r'<article class="section-paper">\s*<div class="wrap-narrow">\s*(.*?)</div>\s*</article>', html, re.S)
    if not m:
        print(f"WARN: could not locate article body in {fname}")
        return
    inner = m.group(1).strip()

    # Split inner into blocks per <h2> occurrence for pull-quote insertion.
    # Simpler: split by <h2 tags
    parts = re.split(r'(<h2[^>]*>)', inner)
    # parts is like: [before, "<h2 ...>", text..., "<h2 ...>", text..., ...]
    # Rebuild with pull quotes inserted after selected h2-blocks.
    blocks = []
    if parts and parts[0].strip():
        blocks.append(parts[0])
    i = 1
    block_index = 0
    while i < len(parts):
        h2_tag = parts[i]
        content = parts[i+1] if i+1 < len(parts) else ""
        blocks.append(h2_tag + content)
        i += 2
        block_index += 1

    # Insert pull-quote after 2nd and 4th block (if exists)
    pulls = cfg["pulls"]
    insert_after = [1, 3]  # 0-indexed
    pull_idx = 0
    new_blocks = []
    for idx, b in enumerate(blocks):
        new_blocks.append(b)
        if idx in insert_after and pull_idx < len(pulls):
            new_blocks.append(f'<div class="post-pull"><p>{pulls[pull_idx]}</p></div>')
            pull_idx += 1
    # Add remaining pull quotes at end if unused
    while pull_idx < len(pulls):
        new_blocks.append(f'<div class="post-pull"><p>{pulls[pull_idx]}</p></div>')
        pull_idx += 1

    main = "".join(new_blocks)
    # Append CTA box near end
    main += build_cta(cfg["cta"])

    sidebar = build_sidebar(cfg["sidebar"])
    new_article = f'''<article class="section-paper"><div class="post-body-grid">
<div class="post-main">{main}</div>
{sidebar}
</div></article>'''

    # Replace article
    html = html[:m.start()] + new_article + html[m.end():]

    # Insert Continue Reading section BEFORE the tagline-band CTA
    cont = build_continue(cfg["continue"], fname)
    # Insert before <section class="section-dark tagline-band">
    if 'section-dark tagline-band' in html:
        html = html.replace('<section class="section-dark tagline-band">', cont + '\n<section class="section-dark tagline-band">', 1)
    else:
        # Insert before footer
        html = html.replace('<footer class="site-footer">', cont + '\n<footer class="site-footer">', 1)

    path.write_text(html)
    print(f"deepened {fname}")

for post in POSTS.keys():
    p = ROOT / "pages/blog" / post
    if p.exists():
        deepen(p)
    else:
        print(f"MISSING: {p}")
