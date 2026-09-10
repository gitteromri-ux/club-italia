"""Agent C part 2 — teachers index, biagio, blog deepening."""
import os, re, pathlib
ROOT = pathlib.Path("/home/user/workspace/club-italia")

NAV  = (ROOT/"_partials/nav.html").read_text()
FOOT = (ROOT/"_partials/footer.html").read_text()

def adapt(html, depth):
    prefix = "../" * depth
    def r(m):
        attr, url = m.group(1), m.group(2)
        if url.startswith(("http", "#", "mailto:", "tel:", "/")):
            return m.group(0)
        return f'{attr}="{prefix}{url}"'
    return re.sub(r'(href|src)="([^"#/][^"]*)"', r, html)

def page(title, desc, body, depth=0, extra_head=""):
    css = ("../" * depth) + "css/ci.css"
    js  = ("../" * depth) + "js/ci.js"
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{css}">
{extra_head}
</head><body>
{adapt(NAV, depth)}

{body}

{adapt(FOOT, depth)}
<script src="{js}"></script>
</body></html>"""

# ============================================================
# TEACHERS INDEX — magazine spread
# ============================================================
TEACHERS_META = [
    ("chiara","Chiara","Bellini","Firenze","Toscana","teacher-chiara.jpg",
     "The eye of an art historian, the ear of a Florentine. Chiara teaches Italian the way Dante wrote it, one detail at a time.",
     "Renaissance Italian. Literature. Art.", 43.77, 11.25),
    ("marco","Marco","Rinaldi","Roma","Lazio","teacher-marco.jpg",
     "Roman by birth, cinema-literate, football-obsessed. Marco teaches Italian at the pace of the capital, direct and generous.",
     "Cinema. Debate. Contemporary Italian.", 41.90, 12.50),
    ("giulia","Giulia","Moretti","Bologna","Emilia-Romagna","teacher-giulia.jpg",
     "Bologna-trained linguist, home-cook, author of two textbooks. Giulia teaches through food, and it works.",
     "Cucina. Textbook author. Rigour.", 44.50, 11.35),
    ("alessandro","Alessandro","Ferri","Milano","Lombardia","teacher-alessandro.jpg",
     "Precise, fast, warmly Northern. Alessandro is the teacher of choice for professionals headed to Milan.",
     "Business Italian. Northern precision.", 45.46, 9.19),
    ("francesca","Francesca","Zeno","Venezia","Veneto","teacher-francesca.jpg",
     "Ca' Foscari-trained literature scholar. Francesca teaches Italian slowly and with the patience of the lagoon.",
     "Literature. Reading. Goldoni.", 45.44, 12.32),
    ("luca","Luca","De Simone","Napoli","Campania","teacher-luca.jpg",
     "Theatrical, generous, Neapolitan to the core. Luca teaches Italian the way you would sing it.",
     "Songs. Theatre. Performance.", 40.83, 14.25),
    ("sofia","Sofia","Mazzara","Palermo","Sicilia","teacher-sofia.jpg",
     "Palermo-native art historian, licensed cultural guide. Sofia teaches Italian through the layered history of her island.",
     "History. Art. The Mediterranean.", 38.11, 13.36),
]

TEACHERS_INDEX_CSS = """
<style>
.ti-hero{position:relative;min-height:80vh;background:linear-gradient(120deg,var(--navy-deep) 0%,var(--navy) 60%,var(--terra-deep) 130%);color:var(--on-dark);display:flex;align-items:center;overflow:hidden}
.ti-hero::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 78% 35%,rgba(201,162,75,.14),transparent 55%);pointer-events:none}
.ti-hero-content{position:relative;z-index:2;padding:9rem clamp(1.6rem,5vw,6rem) 6rem;max-width:1240px;margin:0 auto;width:100%}
.ti-hero .eyebrow{color:var(--gold-soft)}
.ti-hero h1{font-family:var(--serif);font-weight:500;font-size:clamp(3rem,6vw,6rem);line-height:1;letter-spacing:-.018em;max-width:22ch;margin:1.4rem 0 2rem}
.ti-hero h1 em{font-style:italic;color:var(--gold-soft)}
.ti-hero p{font-size:1.2rem;color:var(--on-dark-soft);max-width:54ch;line-height:1.55;margin-bottom:2rem}

.regional-map{background:var(--paper);padding:clamp(4rem,7vw,7rem) 0;overflow:hidden}
.rm-grid{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;max-width:1240px;margin:0 auto;padding:0 clamp(1.4rem,3vw,3rem)}
@media (max-width:960px){.rm-grid{grid-template-columns:1fr}}
.rm-map{position:relative;aspect-ratio:3/4;max-width:520px;margin:0 auto;width:100%}
.rm-map svg{width:100%;height:100%;display:block}
.rm-pin{position:absolute;transform:translate(-50%,-100%);cursor:pointer}
.rm-pin-dot{width:14px;height:14px;background:var(--gold-deep);border:2px solid var(--paper);border-radius:50%;box-shadow:0 3px 10px rgba(58,14,18,.35);animation:pulse-pin 2.2s infinite}
@keyframes pulse-pin{0%,100%{box-shadow:0 3px 10px rgba(58,14,18,.35),0 0 0 0 rgba(201,162,75,.6)}50%{box-shadow:0 3px 10px rgba(58,14,18,.35),0 0 0 10px rgba(201,162,75,0)}}
.rm-pin-label{position:absolute;top:100%;left:50%;transform:translateX(-50%);white-space:nowrap;font-family:var(--serif);font-style:italic;font-size:.95rem;color:var(--navy);margin-top:.35rem;background:var(--paper);padding:.15rem .6rem;border-radius:2px}
.rm-copy h2{font-family:var(--serif);font-weight:500;font-size:clamp(2.2rem,4vw,3.4rem);line-height:1.05;color:var(--navy);margin-bottom:1.6rem}
.rm-copy h2 em{font-style:italic;color:var(--gold-deep)}
.rm-copy p{font-size:1.1rem;line-height:1.7;color:var(--on-light-soft);margin-bottom:1.2rem}

.t-grid{background:var(--ivory);padding:clamp(4rem,7vw,7rem) 0}
.t-grid-inner{max-width:1240px;margin:0 auto;padding:0 clamp(1.4rem,3vw,3rem)}
.t-grid-head{max-width:820px;margin:0 auto 3.4rem;text-align:center}
.t-grid-head .eyebrow{color:var(--gold-deep)}
.t-grid-head h2{font-family:var(--serif);font-weight:500;font-size:clamp(2.4rem,4.4vw,3.8rem);line-height:1.05;color:var(--navy);margin-top:1rem}
.t-mag-row{display:grid;grid-template-columns:1.1fr 1fr;gap:0;align-items:stretch;background:var(--white);border:1px solid var(--gold-line-soft);margin-bottom:1.6rem;transition:box-shadow .35s var(--ease),transform .35s var(--ease);overflow:hidden;text-decoration:none;color:inherit}
.t-mag-row:hover{transform:translateY(-3px);box-shadow:0 16px 44px rgba(58,14,18,.14)}
.t-mag-row.rev{grid-template-columns:1fr 1.1fr}
.t-mag-row.rev .t-mag-photo{order:2}
.t-mag-row.rev .t-mag-body{order:1}
@media (max-width:820px){.t-mag-row,.t-mag-row.rev{grid-template-columns:1fr}.t-mag-row.rev .t-mag-photo{order:1}.t-mag-row.rev .t-mag-body{order:2}}
.t-mag-photo{position:relative;min-height:440px;overflow:hidden;background:var(--cream)}
.t-mag-photo img{width:100%;height:100%;object-fit:cover;object-position:center 20%;transition:transform .8s var(--ease)}
.t-mag-row:hover .t-mag-photo img{transform:scale(1.03)}
.t-mag-photo::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 60%,rgba(34,8,11,.35));pointer-events:none}
.t-mag-photo .t-mag-num{position:absolute;top:1.4rem;left:1.6rem;font-family:var(--serif);font-style:italic;color:var(--gold-soft);font-size:2.2rem;z-index:2;text-shadow:0 2px 8px rgba(0,0,0,.4)}
.t-mag-body{padding:clamp(2rem,4vw,3.4rem);display:flex;flex-direction:column;justify-content:center}
.t-mag-body .t-mag-region{font-size:.72rem;letter-spacing:.28em;text-transform:uppercase;color:var(--gold-deep);margin-bottom:1.4rem}
.t-mag-body h3{font-family:var(--serif);font-weight:500;font-size:clamp(2rem,3.4vw,2.8rem);line-height:1.02;color:var(--navy);margin-bottom:.4rem}
.t-mag-body h3 em{font-style:italic;color:var(--terra-deep)}
.t-mag-body .t-mag-teaches{font-family:var(--serif);font-style:italic;font-size:1.05rem;color:var(--gold-deep);margin-bottom:1.4rem}
.t-mag-body .t-mag-bio{font-size:1.06rem;line-height:1.65;color:var(--on-light-soft);margin-bottom:1.6rem}
.t-mag-body .t-mag-link{font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--terra-deep);font-weight:600}

.ti-close{background:var(--navy);color:var(--on-dark);text-align:center;padding:clamp(4rem,7vw,7rem) 0}
.ti-close p.big{font-family:var(--serif);font-style:italic;font-size:clamp(2.4rem,4.4vw,3.6rem);line-height:1.1;color:var(--gold-soft);max-width:26ch;margin:0 auto 2rem}
</style>
"""

def teachers_index():
    # Build magazine-style rows
    rows = []
    for i,(slug,first,last,city,region,portrait,bio,teaches,_,_) in enumerate(TEACHERS_META):
        rev = "rev" if i%2==1 else ""
        rows.append(f'''<a class="t-mag-row {rev} reveal" href="pages/teachers/{slug}.html">
<div class="t-mag-photo"><span class="t-mag-num">{i+1:02d}</span><img src="assets/img/{portrait}" alt="Portrait of {first} {last}, {region}"></div>
<div class="t-mag-body">
<span class="t-mag-region">{city} · {region}</span>
<h3>{first} <em>{last}</em></h3>
<p class="t-mag-teaches">{teaches}</p>
<p class="t-mag-bio">{bio}</p>
<span class="t-mag-link">Meet {first} →</span>
</div>
</a>''')
    mag_rows = "\n".join(rows)

    # Italy silhouette SVG + pins
    # Coord system 0-100 x, 0-100 y. Place pins by lat/lon roughly mapped to that box.
    # Italy bbox roughly: lon 6.6 to 18.5, lat 47.1 to 36.6
    def to_xy(lat, lon):
        # normalize
        x = (lon - 6.6) / (18.5 - 6.6) * 100
        y = (47.1 - lat) / (47.1 - 36.6) * 100
        return x, y
    pins = []
    for slug,first,last,city,region,_,_,_,lat,lon in TEACHERS_META:
        x,y = to_xy(lat, lon)
        pins.append(f'<a class="rm-pin" style="left:{x:.1f}%;top:{y:.1f}%" href="pages/teachers/{slug}.html" title="{first} — {city}"><span class="rm-pin-dot"></span><span class="rm-pin-label">{first} · {city}</span></a>')
    pins_html = "\n".join(pins)
    # Simple Italy silhouette using an SVG outline path
    italy_svg = '''<svg viewBox="0 0 100 130" preserveAspectRatio="xMidYMid meet" aria-hidden="true">
<defs><linearGradient id="italyG" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#EBDFC7"/><stop offset="1" stop-color="#D9C8AA"/></linearGradient></defs>
<!-- Stylised boot -->
<path d="M28,8 C22,10 20,16 22,22 L22,30 C22,34 26,36 30,36 L36,36 C40,36 42,34 44,32 L50,28 C54,26 58,26 62,28 L68,32 C72,34 76,36 78,40 L80,52 C82,58 82,66 78,72 L72,80 C68,86 62,90 56,92 L48,96 C42,100 40,106 40,112 L40,118 C42,122 46,124 50,124 C54,124 58,122 60,118 L64,110 C68,108 72,108 74,112 L78,118 C80,120 84,120 86,118 L88,114 C90,110 88,106 84,104 L78,102 C74,100 72,96 74,92 L78,84 C82,76 84,66 82,58 L80,48 C78,38 72,32 66,28 L60,22 C56,18 50,16 44,16 L38,12 C34,10 32,8 28,8 Z" fill="url(#italyG)" stroke="#A88536" stroke-width=".6" opacity=".7"/>
<!-- Sicilia -->
<ellipse cx="38" cy="118" rx="11" ry="4" fill="url(#italyG)" stroke="#A88536" stroke-width=".6" opacity=".7"/>
<!-- Sardegna -->
<ellipse cx="12" cy="74" rx="5" ry="9" fill="url(#italyG)" stroke="#A88536" stroke-width=".6" opacity=".5"/>
</svg>'''

    body = f"""
<!-- HERO -->
<section class="ti-hero"><div class="ti-hero-content reveal">
<span class="eyebrow eyebrow-line">Seven voices. Seven regions. One method.</span>
<h1>The voices of Italy, <em>in every classroom.</em></h1>
<p>Seven certified native teachers, each broadcasting live from a different Italian region. Not a global tutor marketplace. A small, chosen faculty, each a specialist in their city and its way of speaking. When you enrol at Club Italia you are matched to a teacher, not a slot.</p>
<div class="hero-ctas"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Speak with an Advisor</button><a class="btn btn-3d btn-3d-ghost" href="#faculty">Meet the Faculty</a></div>
</div></section>

<!-- REGIONAL MAP -->
<section class="regional-map">
<div class="rm-grid">
<div class="rm-copy reveal">
<span class="eyebrow eyebrow-line">La geografia della nostra scuola</span>
<h2>From Palermo to <em>Venezia,</em> broadcasting live.</h2>
<p>Every one of our teachers lives, teaches and broadcasts from Italy. That is not a preference. It is a rule. When your class begins on a Tuesday evening in Boston it is one in the morning in Firenze, and Chiara is at her desk, coffee in hand, because that is where the country she is teaching actually is.</p>
<p>Italy is not one voice. The Italian of Palermo is not the Italian of Bologna, and neither is the Italian of Milano. We do not homogenise. Our teachers speak the standard, warmly inflected by the region they inhabit, and our students learn to hear the whole peninsula.</p>
</div>
<div class="rm-map reveal reveal-d1">
{italy_svg}
{pins_html}
</div>
</div></section>

<!-- FACULTY MAGAZINE GRID -->
<section class="t-grid" id="faculty">
<div class="t-grid-inner">
<div class="t-grid-head reveal">
<span class="eyebrow eyebrow-line">La Facoltà</span>
<h2>Seven certified native teachers.</h2>
</div>
{mag_rows}
</div></section>

<!-- CLOSING -->
<section class="ti-close"><div class="wrap-narrow reveal">
<p class="big">Il tuo insegnante non è un profilo. È una persona che ti aspetta ogni settimana.</p>
<div class="hero-ctas" style="justify-content:center;display:flex"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Match Me with a Teacher</button></div>
</div></section>
"""

    return page("Our Teachers — Seven Native Italian Voices · Club Italia by eTeacher",
                "Meet the seven certified native Italian teachers of Club Italia, each broadcasting live from a different Italian region — Firenze, Roma, Bologna, Milano, Venezia, Napoli, Palermo.",
                body, depth=0, extra_head=TEACHERS_INDEX_CSS)

(ROOT/"teachers.html").write_text(teachers_index())
print("wrote teachers.html")

# ============================================================
# BIAGIO — 12 folds
# ============================================================
BIAGIO_CSS = """
<style>
.b-hero{position:relative;min-height:100vh;background:linear-gradient(140deg,var(--navy-deep) 0%,var(--navy) 55%,var(--terra-deep) 130%);color:var(--on-dark);overflow:hidden;display:flex;align-items:center}
.b-hero::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 22% 30%,rgba(201,162,75,.20),transparent 55%),radial-gradient(circle at 78% 70%,rgba(182,85,56,.18),transparent 50%);pointer-events:none}
.b-hero-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:0;width:100%;position:relative;z-index:2;align-items:center}
@media (max-width:960px){.b-hero-grid{grid-template-columns:1fr}}
.b-hero-copy{padding:9rem clamp(1.6rem,5vw,6rem) 5rem}
.b-hero-copy .eyebrow{color:var(--gold-soft)}
.b-hero-copy h1{font-family:var(--serif);font-weight:500;font-size:clamp(3rem,6vw,6rem);line-height:1;letter-spacing:-.018em;margin:1.4rem 0 1.4rem;max-width:20ch}
.b-hero-copy h1 em{font-style:italic;color:var(--gold-soft)}
.b-hero-copy .b-tag{font-family:var(--serif);font-style:italic;color:var(--gold-soft);font-size:1.4rem;margin-bottom:2rem}
.b-hero-copy p.b-sub{font-size:1.18rem;color:var(--on-dark-soft);max-width:52ch;line-height:1.6;margin-bottom:2.4rem}
.b-portrait{padding:0 clamp(1.6rem,4vw,4rem);position:relative}
.b-portrait img{width:100%;max-width:520px;margin:0 auto;display:block;border-radius:6px;box-shadow:0 30px 80px rgba(0,0,0,.45),0 0 0 1px rgba(201,162,75,.25) inset}

.b-pull{background:var(--ivory);text-align:center;padding:clamp(4rem,6vw,6rem) 0}
.b-pull p{font-family:var(--serif);font-style:italic;font-size:clamp(2rem,4vw,3.2rem);line-height:1.15;max-width:26ch;margin:0 auto;color:var(--navy)}
.b-pull p em{color:var(--terra-deep)}

.b-pillars{background:var(--paper);padding:clamp(4rem,7vw,7rem) 0}
.b-pillar-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem}
@media (max-width:960px){.b-pillar-grid{grid-template-columns:repeat(2,1fr)}}
@media (max-width:640px){.b-pillar-grid{grid-template-columns:1fr}}
.b-pillar{background:var(--white);border:1px solid var(--gold-line-soft);padding:2.2rem 2rem;position:relative}
.b-pillar .b-pillar-num{font-family:var(--serif);font-style:italic;font-size:1.6rem;color:var(--gold-deep);position:absolute;top:1.6rem;right:1.6rem}
.b-pillar h3{font-family:var(--serif);font-size:1.5rem;color:var(--navy);margin-bottom:.8rem;line-height:1.15;max-width:14ch}
.b-pillar p{font-size:1rem;line-height:1.6;color:var(--on-light-soft)}

.b-corrections{background:var(--cream);padding:clamp(4rem,7vw,7rem) 0}
.b-corr{max-width:820px;margin:0 auto 2rem;background:var(--white);border:1px solid var(--gold-line-soft);padding:2rem 2.4rem;box-shadow:0 8px 24px rgba(58,14,18,.06)}
.b-corr .b-corr-user{background:var(--paper);padding:.9rem 1.1rem;border-left:3px solid var(--terra);font-family:var(--sans);color:var(--on-light);margin-bottom:1rem;font-size:1rem}
.b-corr .b-corr-user::before{content:"You";display:block;font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;color:var(--terra-deep);margin-bottom:.35rem;font-weight:600}
.b-corr .b-corr-bot{background:var(--navy);color:var(--on-dark);padding:.9rem 1.1rem;border-left:3px solid var(--gold-soft);font-family:var(--serif);font-style:italic;font-size:1.05rem}
.b-corr .b-corr-bot::before{content:"Biagio";display:block;font-family:var(--sans);font-style:normal;font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-soft);margin-bottom:.35rem;font-weight:600}
.b-corr .b-corr-note{margin-top:1rem;font-size:.9rem;color:var(--on-light-soft);border-top:1px dashed var(--light-line);padding-top:1rem}
.b-corr .b-corr-note strong{color:var(--terra-deep);font-family:var(--serif);font-style:italic;font-weight:600}

.b-culture{background:var(--navy);color:var(--on-dark);padding:clamp(4rem,7vw,7rem) 0}
.b-culture-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem}
@media (max-width:900px){.b-culture-grid{grid-template-columns:repeat(2,1fr)}}
@media (max-width:520px){.b-culture-grid{grid-template-columns:1fr}}
.b-culture-tile{aspect-ratio:4/3;position:relative;overflow:hidden;border:1px solid var(--gold-line-soft);cursor:pointer}
.b-culture-tile img{width:100%;height:100%;object-fit:cover;transition:transform .8s var(--ease)}
.b-culture-tile:hover img{transform:scale(1.05)}
.b-culture-tile .b-ct-overlay{position:absolute;inset:0;background:linear-gradient(180deg,rgba(34,8,11,.1) 40%,rgba(34,8,11,.85));display:flex;align-items:flex-end;padding:1.4rem 1.6rem}
.b-culture-tile h4{font-family:var(--serif);font-style:italic;font-size:1.7rem;color:var(--gold-soft);line-height:1;margin:0}
.b-culture-tile .b-ct-sub{position:absolute;top:1.4rem;left:1.6rem;font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:var(--on-dark-soft)}

.b-voice{background:var(--ivory);padding:clamp(4rem,7vw,7rem) 0}
.b-voice-card{max-width:720px;margin:0 auto;background:var(--white);border:1px solid var(--gold-line-soft);padding:2.4rem;text-align:center}
.b-voice-prompt{font-family:var(--serif);font-style:italic;font-size:1.6rem;color:var(--navy);margin-bottom:2rem;line-height:1.3}
.b-voice-play{display:inline-flex;align-items:center;gap:1rem;background:var(--navy);color:var(--on-dark);padding:1.2rem 2rem;border:1px solid var(--gold-line);cursor:pointer;font-family:var(--sans);letter-spacing:.06em;text-transform:uppercase;font-size:.85rem}
.b-voice-play:hover{background:var(--navy-soft)}
.b-voice-play .b-play-icon{width:2.4rem;height:2.4rem;border:1px solid var(--gold-soft);border-radius:50%;display:inline-flex;align-items:center;justify-content:center;color:var(--gold-soft)}
.b-voice-note{margin-top:2rem;font-size:.95rem;color:var(--on-light-soft);max-width:52ch;margin-left:auto;margin-right:auto}

.b-method{background:var(--paper);padding:clamp(4rem,7vw,7rem) 0}
.b-method-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.4rem}
@media (max-width:960px){.b-method-grid{grid-template-columns:repeat(2,1fr)}}
@media (max-width:520px){.b-method-grid{grid-template-columns:1fr}}
.b-method-col{padding:2rem 1.6rem;border-top:2px solid var(--gold);background:var(--white)}
.b-method-col .b-method-num{font-family:var(--serif);font-style:italic;color:var(--gold-deep);font-size:1.4rem;margin-bottom:.6rem}
.b-method-col h3{font-family:var(--serif);font-size:1.35rem;color:var(--navy);margin-bottom:.6rem;line-height:1.15}
.b-method-col p{font-size:.98rem;line-height:1.6;color:var(--on-light-soft)}

.b-moments{background:var(--cream);padding:clamp(4rem,7vw,7rem) 0}
.b-moments-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.2rem}
@media (max-width:960px){.b-moments-grid{grid-template-columns:repeat(2,1fr)}}
@media (max-width:520px){.b-moments-grid{grid-template-columns:1fr}}
.b-moment{background:var(--white);border:1px solid var(--gold-line-soft);padding:2rem 1.6rem;position:relative}
.b-moment .b-moment-time{font-family:var(--serif);font-style:italic;color:var(--terra-deep);font-size:1.1rem;margin-bottom:.6rem}
.b-moment h3{font-family:var(--serif);font-size:1.35rem;color:var(--navy);margin-bottom:.6rem;line-height:1.2}
.b-moment p{font-size:.95rem;line-height:1.6;color:var(--on-light-soft)}

.b-faq{background:var(--navy);color:var(--on-dark);padding:clamp(4rem,7vw,7rem) 0}
.b-faq-list{max-width:820px;margin:0 auto}
.b-faq details{border-bottom:1px solid var(--gold-line-soft);padding:1.6rem 0}
.b-faq summary{cursor:pointer;font-family:var(--serif);font-size:1.35rem;color:var(--gold-soft);list-style:none;display:flex;justify-content:space-between;align-items:baseline;gap:1rem}
.b-faq summary::-webkit-details-marker{display:none}
.b-faq summary::after{content:"+";color:var(--gold-soft);font-size:1.5rem;font-family:var(--sans);font-weight:300}
.b-faq details[open] summary::after{content:"−"}
.b-faq details p{margin-top:1rem;font-size:1.05rem;line-height:1.7;color:var(--on-dark-soft)}

.b-relation{background:var(--paper);padding:clamp(4rem,7vw,7rem) 0}
.b-relation-grid{display:grid;grid-template-columns:1fr 1fr;gap:3rem;max-width:1100px;margin:0 auto}
@media (max-width:820px){.b-relation-grid{grid-template-columns:1fr}}
.b-tier{background:var(--white);border:1px solid var(--gold-line-soft);padding:2.6rem 2.2rem}
.b-tier .b-tier-num{font-family:var(--serif);font-style:italic;font-size:2.6rem;color:var(--gold-deep);line-height:1;margin-bottom:.8rem}
.b-tier h3{font-family:var(--serif);font-size:1.8rem;color:var(--navy);margin-bottom:1rem;line-height:1.1}
.b-tier p{font-size:1.05rem;line-height:1.65;color:var(--on-light-soft);margin-bottom:1rem}

.b-final{background:linear-gradient(140deg,var(--terra-deep) 0%,var(--navy) 60%);color:var(--on-dark);text-align:center;padding:clamp(4rem,8vw,8rem) 0}
.b-final h2{font-family:var(--serif);font-style:italic;font-weight:500;font-size:clamp(2.6rem,5.4vw,4.4rem);line-height:1.02;margin-bottom:1.4rem;max-width:22ch;margin-left:auto;margin-right:auto}
.b-final p{font-size:1.2rem;color:var(--on-dark-soft);max-width:52ch;margin:0 auto 2.4rem;line-height:1.55}
</style>
"""

BIAGIO_BODY = f"""
<!-- FOLD 1 · HERO -->
<section class="b-hero"><div class="b-hero-grid">
<div class="b-hero-copy reveal">
<span class="eyebrow eyebrow-line">Available 24 hours, in any timezone</span>
<h1>Meet <em>Biagio,</em> your Italian coach.</h1>
<p class="b-tag">Il tuo insegnante privato che non dorme mai.</p>
<p class="b-sub">Biagio is your AI Italian tutor. A forty-two-year-old Roman with a warm voice, a strict method, and unlimited patience. He does not sleep, he does not lose interest, he does not switch to English when the going gets hard. He speaks Italian, and he speaks it with you.</p>
<div class="hero-ctas"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button><a class="btn btn-3d btn-3d-ghost" href="#chat">Chat with Biagio</a></div>
</div>
<div class="b-portrait reveal reveal-d1"><img src="assets/img/biagio.png" alt="Portrait of Biagio, the AI Italian tutor of Club Italia"></div>
</div></section>

<!-- FOLD 2 · PULL QUOTE -->
<section class="b-pull reveal">
<p>Not a chatbot. <em>A precision Italian coach,</em> engineered for the way adults actually learn a language.</p>
</section>

<!-- FOLD 3 · 6 PILLARS -->
<section class="b-pillars">
<div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">What Biagio Does</span><h2 class="display-md" style="color:var(--navy)">Everything a private tutor does, and nothing they cannot.</h2></div>
<div class="b-pillar-grid">
<div class="b-pillar reveal"><span class="b-pillar-num">i</span><h3>Conversation Practice</h3><p>Free-form talk on any topic at your level, from the first minute. Biagio adapts to your vocabulary, not the other way around.</p></div>
<div class="b-pillar reveal reveal-d1"><span class="b-pillar-num">ii</span><h3>Instant Correction</h3><p>Every mistake noted and corrected gently, in Italian, with the reason why. Never with a red pen. Always with an alternative.</p></div>
<div class="b-pillar reveal reveal-d2"><span class="b-pillar-num">iii</span><h3>Pronunciation Coaching</h3><p>Speak into your microphone. Biagio hears you, models the correct sound, and asks you to try again until it sits right.</p></div>
<div class="b-pillar reveal"><span class="b-pillar-num">iv</span><h3>Vocabulary in Context</h3><p>Culturally grounded vocabulary, always in a real sentence, always attached to a real Italian object. Never in flashcards.</p></div>
<div class="b-pillar reveal reveal-d1"><span class="b-pillar-num">v</span><h3>Cultural Questions</h3><p>Ask about calcio, cinema, cucina, opera, arte, politica. Biagio answers in Italian, at your level, with a real Italian's point of view.</p></div>
<div class="b-pillar reveal reveal-d2"><span class="b-pillar-num">vi</span><h3>Homework and Class Prep</h3><p>Preview tomorrow's live class, review yesterday's homework, or drill the one point that did not stick. Your teacher's ally, all week long.</p></div>
</div></div></section>

<!-- FOLD 4 · INTERACTIVE CHAT DEMO -->
<section class="section-dark" id="chat">
<div class="wrap-narrow">
<div class="section-head reveal"><span class="eyebrow eyebrow-line" style="color:var(--gold-soft)">Try it now</span><h2 class="display-md">Try Biagio for one minute.</h2><p class="lead" style="color:var(--on-dark-soft)">A short live demonstration of the way Biagio corrects, praises and guides. Type something below in Italian, or in English if you must.</p></div>
<div class="form-card" style="background:var(--navy-soft);border-color:var(--gold-line);max-width:640px">
<div id="biagio-chat-msgs" style="min-height:220px;max-height:400px;overflow-y:auto;background:var(--navy-deep);padding:1.2rem;margin-bottom:1rem;color:var(--on-dark);font-size:.98rem">
<div class="chat-msg bot" style="padding:.6rem 0;color:var(--gold-soft);font-style:italic;font-family:var(--serif);font-size:1.1rem">Ciao! Sono Biagio. Try ordering an espresso in Italian.</div>
</div>
<form id="biagio-chat-form" style="display:flex;gap:.5rem"><input type="text" placeholder="Scrivi qui in italiano..." style="flex:1"><button class="btn btn-3d btn-3d-primary" type="submit">Send</button></form>
</div>
</div></section>

<!-- FOLD 5 · HOW BIAGIO CORRECTS -->
<section class="b-corrections">
<div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">How Biagio Corrects</span><h2 class="display-md" style="color:var(--navy)">Three ways he moves you forward.</h2><p class="lead">Correction, done badly, kills a learner. Biagio was trained to correct the way a warm human tutor corrects, with an alternative, a reason, and one small next step.</p></div>

<div class="b-corr reveal">
<div class="b-corr-user">Io ho andato a Roma la settimana scorsa.</div>
<div class="b-corr-bot">Quasi. Si dice sono andato, perché andare vuole l'ausiliare essere. Prova ancora, con la stessa frase.</div>
<div class="b-corr-note"><strong>The pattern.</strong> Biagio never says "wrong." He offers the correct form, gives a one-line reason, and asks you to try again. The whole exchange happens in Italian.</div>
</div>

<div class="b-corr reveal reveal-d1">
<div class="b-corr-user">Vorrei un espresso, per piacere.</div>
<div class="b-corr-bot">Perfetto. Piccola nota, in Italia diciamo di solito per favore o per cortesia. Per piacere si capisce ma è raro. Ripetiamo, ordina anche un cornetto.</div>
<div class="b-corr-note"><strong>The pattern.</strong> When you are technically right but not idiomatic, Biagio celebrates first, then nudges. He never withholds praise for a technical improvement.</div>
</div>

<div class="b-corr reveal reveal-d2">
<div class="b-corr-user">Domani io vado al cinema con mio amico Marco.</div>
<div class="b-corr-bot">Bene. Un piccolo dettaglio, con l'amico si dice il mio amico Marco, tranne quando è tuo padre, tua madre, tuo fratello. È una regola strana, lo so. Riprova.</div>
<div class="b-corr-note"><strong>The pattern.</strong> When the rule is genuinely counterintuitive, Biagio names that it is counterintuitive. That single acknowledgement is what separates a good tutor from a good textbook.</div>
</div>
</div></section>

<!-- FOLD 6 · CULTURAL RANGE -->
<section class="b-culture">
<div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line" style="color:var(--gold-soft)">Biagio's Cultural Range</span><h2 class="display-md">Six worlds. One conversation.</h2><p class="lead" style="color:var(--on-dark-soft)">Ask Biagio about any of these and he will answer in Italian, at your level, with a real Italian's opinion, not a search engine's summary.</p></div>
<div class="b-culture-grid">
<div class="b-culture-tile reveal"><img src="assets/img/pillar-tradition.jpg" alt="Calcio"><span class="b-ct-sub">01</span><div class="b-ct-overlay"><h4>Calcio</h4></div></div>
<div class="b-culture-tile reveal reveal-d1"><img src="assets/img/pillar-cinema.jpg" alt="Cinema"><span class="b-ct-sub">02</span><div class="b-ct-overlay"><h4>Cinema</h4></div></div>
<div class="b-culture-tile reveal reveal-d2"><img src="assets/img/pillar-food.jpg" alt="Cucina"><span class="b-ct-sub">03</span><div class="b-ct-overlay"><h4>Cucina</h4></div></div>
<div class="b-culture-tile reveal"><img src="assets/img/pillar-opera.jpg" alt="Opera"><span class="b-ct-sub">04</span><div class="b-ct-overlay"><h4>Opera</h4></div></div>
<div class="b-culture-tile reveal reveal-d1"><img src="assets/img/pillar-art.jpg" alt="Arte"><span class="b-ct-sub">05</span><div class="b-ct-overlay"><h4>Arte</h4></div></div>
<div class="b-culture-tile reveal reveal-d2"><img src="assets/img/pillar-travel.jpg" alt="Politica"><span class="b-ct-sub">06</span><div class="b-ct-overlay"><h4>Politica</h4></div></div>
</div></div></section>

<!-- FOLD 7 · VOICE / PRONUNCIATION -->
<section class="b-voice">
<div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Voice and Pronunciation</span><h2 class="display-md" style="color:var(--navy)">Biagio hears you. Then he corrects you.</h2><p class="lead">Speak into your microphone. Biagio models the correct Italian phrasing, plays it back at your speed, and asks you to try it again. The whole loop takes ten seconds.</p></div>
<div class="b-voice-card reveal">
<p class="b-voice-prompt">"Vorrei un caffè macchiato, per favore."</p>
<button class="b-voice-play" type="button"><span class="b-play-icon">▶</span><span>Listen to Biagio pronounce this</span></button>
<p class="b-voice-note">Full voice interaction is available on desktop and mobile inside your Club Italia dashboard. This demo is a preview.</p>
</div>
</div></section>

<!-- FOLD 8 · METHOD (4 PILLARS) -->
<section class="b-method">
<div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Biagio's Method</span><h2 class="display-md" style="color:var(--navy)">Four rules Biagio never breaks.</h2></div>
<div class="b-method-grid">
<div class="b-method-col reveal"><div class="b-method-num">i.</div><h3>Italian, always</h3><p>Biagio does not translate. When you do not know a word, he describes it in easier Italian. That constraint is what makes fluency happen.</p></div>
<div class="b-method-col reveal reveal-d1"><div class="b-method-num">ii.</div><h3>Correction with an alternative</h3><p>He never says "wrong." He offers the correct form, a one-line reason, and asks you to try again. Confidence is a resource, and he protects it.</p></div>
<div class="b-method-col reveal reveal-d2"><div class="b-method-num">iii.</div><h3>Culture inside every sentence</h3><p>The example sentences arrive from a real Italian life, a tabaccheria, a piazza, a nonna's kitchen. Vocabulary attached to place stays.</p></div>
<div class="b-method-col reveal reveal-d3"><div class="b-method-num">iv.</div><h3>Small steps, held for years</h3><p>He remembers what you learned last week and reintroduces it this week. Spaced retrieval, quiet, deliberate, built into every conversation.</p></div>
</div></div></section>

<!-- FOLD 9 · WHEN BIAGIO HELPS -->
<section class="b-moments">
<div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">When Biagio Helps</span><h2 class="display-md" style="color:var(--navy)">He lives in the moments between class.</h2></div>
<div class="b-moments-grid">
<div class="b-moment reveal"><div class="b-moment-time">Before class</div><h3>Preview</h3><p>Ten minutes with Biagio before you sit down with your teacher. Pre-loaded with tomorrow's vocabulary so you arrive already warm.</p></div>
<div class="b-moment reveal reveal-d1"><div class="b-moment-time">After class</div><h3>Review</h3><p>The point that did not click, drilled one on one, no other learners watching, at your own pace, for as long as you need.</p></div>
<div class="b-moment reveal reveal-d2"><div class="b-moment-time">Between classes</div><h3>Practice</h3><p>Fifteen minutes a day of real conversation with Biagio doubles the effective speaking hours in your Italian week. Quietly, without ceremony.</p></div>
<div class="b-moment reveal reveal-d3"><div class="b-moment-time">03:14 in your timezone</div><h3>Insomnia</h3><p>When the moment hits and you want to speak Italian, Biagio is awake, at his desk, coffee in hand, ready to talk about Sorrentino's latest film.</p></div>
</div></div></section>

<!-- FOLD 10 · FAQ -->
<section class="b-faq">
<div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line" style="color:var(--gold-soft)">Questions about Biagio</span><h2 class="display-md">The things everyone asks first.</h2></div>
<div class="b-faq-list">
<details reveal><summary>Is Biagio a real person?</summary><p>No. Biagio is an artificial tutor, engineered by our academic team and voiced by an Italian actor. He is designed to behave like a warm, patient Italian tutor from Roma, and he is with you at any hour. He is not, and does not pretend to be, a human being.</p></details>
<details><summary>Can Biagio replace my live teacher?</summary><p>No, and we do not want him to. Biagio replaces the private tutor you cannot afford at four in the morning. Your live teacher, Chiara or Marco or Sofia, is the human presence that gives your week its shape. Biagio fills the gaps between.</p></details>
<details><summary>Does Biagio speak English?</summary><p>Only in emergencies. Ninety-nine per cent of the time he answers in Italian, adjusted to your level. That constraint is deliberate. It is the single most important reason our students become fluent.</p></details>
<details><summary>How does Biagio correct me?</summary><p>He offers the correct form, a one-line reason, and asks you to try again, all in Italian. He never says "wrong." He never withholds praise for a technical improvement.</p></details>
<details><summary>Is Biagio included in my Club Italia enrolment?</summary><p>Yes. Every Club Italia student gets unlimited access to Biagio, on desktop and mobile, for the length of their enrolment. There is no additional fee and no separate app.</p></details>
</div>
</div></section>

<!-- FOLD 11 · TWO TIERS -->
<section class="b-relation">
<div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Biagio and Your Teacher</span><h2 class="display-md" style="color:var(--navy)">The two-tier relationship.</h2><p class="lead">Club Italia is designed as a partnership, a human teacher and an AI coach, each doing what the other cannot. This is the shape.</p></div>
<div class="b-relation-grid">
<div class="b-tier reveal">
<div class="b-tier-num">01</div>
<h3>Your live teacher</h3>
<p>One hundred minutes a week with a certified native teacher, live, in a small group of no more than twelve. This is where the real learning arc happens, the syllabus, the culture, the correction that only a human eye can catch, the community of classmates who become friends.</p>
<p>Your teacher knows your name, your work, your goals, the specific mistake you made three weeks ago. They plan the semester. They care about your outcome.</p>
</div>
<div class="b-tier reveal reveal-d1">
<div class="b-tier-num">02</div>
<h3>Biagio, your daily coach</h3>
<p>Fifteen minutes a day, at any hour, on any device. This is where the between-class practice happens, the drills that would bore a live teacher, the third and fourth pass at yesterday's grammar, the free-form conversation at three in the morning.</p>
<p>Biagio does not replace your teacher. He is the private tutor you could never otherwise afford, sitting between your live classes, making sure the hour with your teacher is spent on the hard work, not the housekeeping.</p>
</div>
</div></div></section>

<!-- FOLD 12 · FINAL CTA -->
<section class="b-final"><div class="wrap-narrow reveal">
<h2>Biagio è sempre qui. <em>Anche adesso.</em></h2>
<p>A Club Italia advisor will place you, match you with a live teacher, and open your Biagio access on the same day. The consultation is free and takes twenty minutes.</p>
<div class="hero-ctas" style="justify-content:center;display:flex;flex-wrap:wrap"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button><a class="btn btn-3d btn-3d-ghost" href="#chat">Try Biagio First</a></div>
</div></section>
"""

biagio_html = page("Biagio — Your AI Italian Tutor · Club Italia by eTeacher",
                   "Meet Biagio, your 24-hour AI Italian coach. Conversation, correction, pronunciation and cultural questions, all in Italian, engineered for adult learners.",
                   BIAGIO_BODY, depth=0, extra_head=BIAGIO_CSS)
(ROOT/"biagio.html").write_text(biagio_html)
print("wrote biagio.html")
