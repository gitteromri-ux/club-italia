"""Build all secondary pages for Club Italia with authentic Italian brand system."""
import os
from pathlib import Path

ROOT = Path("/home/user/workspace/club-italia")
NAV = (ROOT / "_partials/nav.html").read_text()
FOOTER = (ROOT / "_partials/footer.html").read_text()


def html_head(title, css_prefix="", extra_css=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Club Italia</title>
<link rel="stylesheet" href="{css_prefix}css/ci.css">
<style>{extra_css}</style>
</head>
<body>
"""


def page(title, body, css_prefix="", extra_css="", js_prefix=""):
    nav = NAV
    footer = FOOTER
    if css_prefix:
        # rewrite hrefs to add prefix
        import re
        def fix(m):
            href = m.group(1)
            if href.startswith(("http", "#", "mailto:", "tel:", "/")):
                return m.group(0)
            return f'href="{css_prefix}{href}"'
        nav = re.sub(r'href="([^"]+)"', fix, nav)
        footer = re.sub(r'href="([^"]+)"', fix, footer)
    head = html_head(title, css_prefix, extra_css)
    return f"""{head}
{nav}
<main>
{body}
</main>
{footer}
<script src="{js_prefix}js/ci.js" defer></script>
</body>
</html>
"""


# ============================================================
# Reusable fragments
# ============================================================

def hero_video(video, poster, kicker, h1_pre, h1_ital, sub, ctas, extra_class=""):
    ctas_html = "".join([f'<a class="btn btn-3d btn-3d-primary" href="{u}">{t}</a>' if p=="primary" else f'<a class="btn btn-3d btn-3d-ghost" href="{u}">{t}</a>' for t,u,p in ctas])
    return f"""
<section class="hero hero-video section-ink {extra_class}">
  <video class="hero-bg" autoplay muted loop playsinline poster="{poster}">
    <source src="{video}" type="video/mp4">
  </video>
  <div class="hero-scrim"></div>
  <div class="wrap hero-content">
    <span class="eyebrow eyebrow-line">{kicker}</span>
    <h1>{h1_pre} <em class="accent-ital">{h1_ital}</em></h1>
    <p class="lead">{sub}</p>
    <div class="hero-actions">{ctas_html}</div>
  </div>
</section>
"""


def hero_image(img, kicker, h1_pre, h1_ital, sub, ctas):
    ctas_html = "".join([f'<a class="btn btn-3d btn-3d-primary" href="{u}">{t}</a>' if p=="primary" else f'<a class="btn btn-3d btn-3d-ghost" href="{u}">{t}</a>' for t,u,p in ctas])
    return f"""
<section class="hero hero-image section-ink">
  <img class="hero-bg" src="{img}" alt="">
  <div class="hero-scrim"></div>
  <div class="wrap hero-content">
    <span class="eyebrow eyebrow-line">{kicker}</span>
    <h1>{h1_pre} <em class="accent-ital">{h1_ital}</em></h1>
    <p class="lead">{sub}</p>
    <div class="hero-actions">{ctas_html}</div>
  </div>
</section>
"""


def eteacher_strip():
    return """
<section class="eteacher-strip section-travertine">
  <div class="wrap">
    <div class="et-strip">
      <div class="et-left">
        <span class="eyebrow eyebrow-line">Powered by eTeacher</span>
        <p>Twenty-five years of teaching adults live online. Club Italia is our newest language faculty.</p>
      </div>
      <div class="et-stats">
        <div class="et-stat"><span class="et-num">25+</span><span class="et-label">Years</span></div>
        <div class="et-stat"><span class="et-num">400k</span><span class="et-label">Learners</span></div>
        <div class="et-stat"><span class="et-num">197</span><span class="et-label">Countries</span></div>
        <div class="et-stat"><span class="et-num">6</span><span class="et-label">Language faculties</span></div>
      </div>
    </div>
  </div>
</section>
"""


def pull_quote_band(text, cite, cls="section-verona"):
    return f"""
<section class="pull-quote-band {cls}">
  <div class="wrap wrap-narrow">
    <blockquote class="big-quote">
      <p><em class="accent-ital">"{text}"</em></p>
      <cite>— {cite}</cite>
    </blockquote>
  </div>
</section>
"""


def final_cta(h2_pre, h2_ital, sub, cta_text, cta_url, cls="section-verona"):
    return f"""
<section class="final-cta {cls}">
  <div class="wrap wrap-narrow text-center">
    <h2>{h2_pre} <em class="accent-ital">{h2_ital}</em></h2>
    <p class="lead">{sub}</p>
    <div class="hero-actions" style="justify-content:center">
      <a class="btn btn-3d btn-3d-primary" href="{cta_url}">{cta_text}</a>
      <button class="btn btn-3d btn-3d-ghost" data-advisor type="button">Speak with an advisor</button>
    </div>
  </div>
</section>
"""


def trustpilot_wall(items, cls="section-cream"):
    cards = ""
    for name, photo, region, text in items:
        cards += f"""
    <article class="tp-review-card">
      <div class="tp-stars">★★★★★</div>
      <p class="tp-text">"{text}"</p>
      <div class="tp-meta">
        <img class="tp-photo" src="{photo}" alt="{name}" loading="lazy">
        <div>
          <div class="tp-name">{name}</div>
          <div class="tp-role">{region}</div>
        </div>
      </div>
      <div class="tp-verified">Verified · Trustpilot</div>
    </article>"""
    return f"""
<section class="trustpilot-wall {cls}">
  <div class="wrap">
    <div class="section-head text-center">
      <span class="eyebrow eyebrow-line">What students say</span>
      <h2>Reviews from adults who mean it.</h2>
    </div>
    <div class="tp-grid card-slider">{cards}
    </div>
  </div>
</section>
"""


# ============================================================
# TEACHERS INDEX
# ============================================================

TEACHERS = [
    ("chiara", "Chiara Bellini", "Firenze", "Toscana", "DITALS II · Università di Firenze", "teacher-chiara.jpg", "life-uffizi-hall.jpg"),
    ("marco", "Marco Rinaldi", "Roma", "Lazio", "CEDILS · Ca' Foscari · CEFR examiner", "teacher-marco.jpg", "life-caffe-roma.jpg"),
    ("giulia", "Giulia Moretti", "Bologna", "Emilia-Romagna", "DITALS II · CILS examiner Perugia", "teacher-giulia.jpg", "life-market-bologna.jpg"),
    ("alessandro", "Alessandro Ferri", "Milano", "Lombardia", "Master ITALS · Ca' Foscari", "teacher-alessandro.jpg", "life-scala-milano.jpg"),
    ("francesca", "Francesca Zeno", "Venezia", "Veneto", "DITALS II · Ca' Foscari · opera librettist", "teacher-francesca.jpg", "life-gondola-venezia.jpg"),
    ("luca", "Luca De Simone", "Napoli", "Campania", "CEDILS · trained chef · L2 examiner", "teacher-luca.jpg", "life-amalfi-coast.jpg"),
    ("sofia", "Sofia Mazzara", "Palermo", "Sicilia", "DITALS II · Master FLE Sorbonne", "teacher-sofia.jpg", "life-trattoria-toscana.jpg"),
]


def build_teachers_index():
    cards = ""
    for slug, name, city, region, cred, portrait, life in TEACHERS:
        cards += f"""
      <a class="teacher-card" href="pages/teachers/{slug}.html">
        <div class="tc-photo" style="aspect-ratio:3/4">
          <img src="assets/img/{portrait}" alt="{name}, {city}" loading="lazy">
        </div>
        <div class="tc-over">
          <span class="tc-region">{region}</span>
          <h3 class="tc-name">{name}</h3>
          <p class="tc-cred">{cred}</p>
          <span class="tc-arrow">Meet {name.split()[0]} →</span>
        </div>
      </a>"""

    pins = ""
    coords = [("Chiara","155,180"),("Marco","195,320"),("Giulia","165,215"),("Alessandro","130,140"),("Francesca","210,155"),("Luca","240,375"),("Sofia","210,470")]
    for n, xy in coords:
        x, y = xy.split(",")
        pins += f'<circle cx="{x}" cy="{y}" r="7" fill="#B08640" stroke="#F1E9D6" stroke-width="2"><title>{n}</title></circle>\n'

    map_svg = f"""
<svg viewBox="0 0 380 560" xmlns="http://www.w3.org/2000/svg" class="italy-map" role="img" aria-label="Map of Club Italia teachers across Italy">
  <path d="M110 90 Q140 60 175 80 Q220 95 210 140 Q235 170 230 205 Q255 235 240 280 Q265 330 235 360 Q225 400 250 430 Q265 480 230 495 Q210 520 195 490 Q170 470 160 440 Q145 405 155 375 Q135 340 145 305 Q125 265 145 230 Q125 200 130 170 Q100 130 110 90 Z" fill="#4B5320" stroke="#B08640" stroke-width="1.5" opacity=".92"/>
  <ellipse cx="200" cy="510" rx="30" ry="14" fill="#4B5320" stroke="#B08640" stroke-width="1.5"/>
  <ellipse cx="130" cy="340" rx="14" ry="10" fill="#4B5320" stroke="#B08640" stroke-width="1.5"/>
  {pins}
</svg>
"""

    student_reviews = [
        ("Diane Carter", "assets/img/student-diane.jpg", "Boston · with Chiara", "Chiara teaches Florence from inside Florence. Every lesson opens a door I didn't know existed."),
        ("Robert Klein", "assets/img/student-robert.jpg", "Chicago · with Marco", "Marco corrects like a barista in Trastevere. Warm, precise, never patronising."),
        ("Sarah Weiss", "assets/img/student-sarah.jpg", "New York · with Giulia", "Giulia turned a grammar hour into an evening in Bologna. I ordered dinner in Italian last week."),
        ("James Miller", "assets/img/student-james.jpg", "Denver · with Alessandro", "Alessandro is Milan calm. He gave me the confidence to answer the phone at work in Italian."),
        ("Linda Hoffman", "assets/img/student-linda.jpg", "Miami · with Francesca", "Francesca reads opera libretti with me. I have never been so gently corrected."),
        ("Michael Ross", "assets/img/student-michael.jpg", "Los Angeles · with Luca", "Luca is Naples in a Zoom window. Every lesson tastes like something."),
    ]

    body = f"""
{hero_video("assets/video/firenze-arno.mp4","assets/img/hero-teacher-live.jpg","The Club Italia faculty","Seven native teachers.","Seven Italian cities.","Not tutors. Not freelancers. Certified Italian educators who live in the country they teach, and who teach the region they call home.",[("Meet the faculty","#faculty","primary"),("Book a placement call","#book","ghost")])}

{eteacher_strip()}

<section class="editorial-2col section-cream">
  <div class="wrap">
    <div class="e2-grid">
      <div class="e2-text">
        <span class="eyebrow eyebrow-line">About the faculty</span>
        <h2>We hire the way a conservatory hires a conductor.</h2>
        <p>Every Club Italia teacher is native to the region they teach. Each holds a graduate qualification in teaching Italian as a second language, DITALS II, CEDILS or the Master ITALS from Ca' Foscari or Perugia. Each has taught adults, on video, for at least seven years. None of them freelance on the side.</p>
        <p>The faculty is small on purpose. Seven cities, seven teachers, one continuous methodological conversation that happens every Friday morning at ten. Nothing is franchised. Nothing is outsourced. When you book, you know which human being will open your Zoom window on Monday.</p>
      </div>
      <blockquote class="e2-pullquote">
        <em class="accent-ital">"To be taught Italian by someone who lives it is not a detail. It is the whole method."</em>
        <cite>— Chiara Bellini, faculty lead</cite>
      </blockquote>
    </div>
  </div>
</section>

<section id="faculty" class="teachers-index section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow eyebrow-line">The seven</span>
      <h2>Choose the city that <em class="accent-ital">calls you.</em></h2>
    </div>
    <div class="teachers-grid card-slider">{cards}
    </div>
  </div>
</section>

<section class="italy-map-fold section-travertine">
  <div class="wrap">
    <div class="map-grid">
      <div>
        <span class="eyebrow eyebrow-line">Where we teach from</span>
        <h2>An Italy of <em class="accent-ital">seven cities.</em></h2>
        <p class="lead">Every pin is a home. Every home is a classroom. Roma, Firenze, Bologna, Milano, Venezia, Napoli, Palermo. You can hear each city in the vowels of the teacher who lives there.</p>
        <ul class="map-list">
          <li><strong>Roma</strong> · Marco Rinaldi · Lazio, everyday Italian, cinema and food</li>
          <li><strong>Firenze</strong> · Chiara Bellini · Toscana, Renaissance art, high literary Italian</li>
          <li><strong>Bologna</strong> · Giulia Moretti · Emilia-Romagna, cuisine, university culture</li>
          <li><strong>Milano</strong> · Alessandro Ferri · Lombardia, business Italian, design</li>
          <li><strong>Venezia</strong> · Francesca Zeno · Veneto, opera, libretto, La Fenice</li>
          <li><strong>Napoli</strong> · Luca De Simone · Campania, gastronomy, southern warmth</li>
          <li><strong>Palermo</strong> · Sofia Mazzara · Sicilia, dialect awareness, island culture</li>
        </ul>
      </div>
      <div class="map-visual">{map_svg}</div>
    </div>
  </div>
</section>

{pull_quote_band("To be taught Italian by someone who lives it is not a detail. It is the whole method.", "The Club Italia faculty")}

{trustpilot_wall(student_reviews)}

{final_cta("Book with the teacher who","fits your Italy.","A twenty-minute placement call is on us. You will leave with a level, a start date and a name.","Book my placement call","#book")}
"""
    (ROOT / "teachers.html").write_text(page("Teachers", body))


build_teachers_index()
print("teachers.html built")
