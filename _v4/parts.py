"""Shared cinematic page-parts for Club Italia v4."""

def hero_cinematic(A_, video, poster, eyebrow, headline_html, sub, cta_primary="Reserve My Placement Call",
                   cta_ghost=("Watch a Real Class", "sample-class.html"), meta_pulse="12 classrooms broadcasting right now",
                   right_img=None, right_caption=None):
    right_col = ""
    if right_img:
        cap = f'<div style="position:absolute;left:-1.2rem;bottom:1.5rem;background:rgba(4,15,10,.85);backdrop-filter:blur(10px);padding:.9rem 1.2rem;border-left:2px solid #E6C99B;max-width:280px"><div style="font-family:\'Playfair Display\',serif;font-style:italic;color:#E6C99B;font-size:.98rem;line-height:1.35">{right_caption}</div></div>' if right_caption else ""
        right_col = f'''<div style="position:relative;aspect-ratio:5/6;height:76%;justify-self:end;width:100%;max-width:580px;align-self:center">
      <img src="{A_}img/{right_img}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:40% 22%;transform:rotate(-1.2deg);
          box-shadow:0 40px 120px -40px rgba(0,0,0,.85);
          mask-image:radial-gradient(ellipse 90% 92% at 50% 48%, black 60%, transparent 100%);
          -webkit-mask-image:radial-gradient(ellipse 90% 92% at 50% 48%, black 60%, transparent 100%);">
      {cap}
    </div>'''
    grid = "1.15fr .95fr" if right_img else "1fr"
    return f"""<section class="hero" style="position:relative;min-height:100vh;overflow:hidden;background:#04070e">
  <div class="hero-bg" aria-hidden="true">
    <video autoplay muted loop playsinline poster="{A_}img/{poster}" preload="metadata"
      style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 40%">
      <source src="{A_}video/{video}" type="video/mp4">
    </video>
    <div style="position:absolute;inset:0;background:
      linear-gradient(105deg, rgba(4,20,15,.88) 0%, rgba(4,20,15,.55) 42%, rgba(50,10,10,.35) 70%, rgba(0,0,0,.75) 100%),
      radial-gradient(ellipse at 30% 55%, rgba(230,201,155,.11), transparent 55%);"></div>
    <div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(0,0,0,.35), transparent 22%, transparent 65%, rgba(0,0,0,.55));"></div>
  </div>
  <div class="wrap hero-content" style="position:relative;z-index:2;display:grid;grid-template-columns:{grid};gap:clamp(2rem,4vw,5rem);align-items:center;min-height:100vh;padding-top:8rem;padding-bottom:6rem">
    <div>
      <div class="eyebrow paper" style="color:#8FC9AB;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">{eyebrow}</div>
      <h1 style="font-family:'Playfair Display',Georgia,serif;font-weight:700;font-size:clamp(3.4rem,8vw,7.6rem);line-height:1.02;letter-spacing:-.022em;color:#FBFAF6;margin:0 0 2rem">{headline_html}</h1>
      <p style="font-family:'Inter',sans-serif;font-size:clamp(1.2rem,1.7vw,1.55rem);line-height:1.55;color:rgba(251,250,246,.86);max-width:52ch;margin:0 0 2.4rem;font-weight:300">{sub}</p>
      <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2.2rem">
        <button class="btn btn-3d btn-3d-primary" data-advisor type="button">{cta_primary}</button>
        <a class="btn btn-3d btn-3d-ghost" href="{cta_ghost[1]}">{cta_ghost[0]}</a>
      </div>
      <div style="display:flex;gap:1.8rem;align-items:center;flex-wrap:wrap;color:rgba(251,250,246,.75);font-size:.86rem">
        <div style="display:flex;align-items:center;gap:.55rem"><span style="color:#E6C99B">★★★★★</span><span>4.8 · Trustpilot</span></div>
        <div style="display:flex;align-items:center;gap:.55rem"><span style="width:9px;height:9px;border-radius:50%;background:#e0413f;animation:pulse 2s infinite;display:inline-block"></span><span style="letter-spacing:.16em;text-transform:uppercase;font-size:.7rem">{meta_pulse}</span></div>
      </div>
    </div>
    {right_col}
  </div>
  <style>@keyframes pulse{{0%{{box-shadow:0 0 0 0 rgba(224,65,63,.6)}}70%{{box-shadow:0 0 0 12px rgba(224,65,63,0)}}100%{{box-shadow:0 0 0 0 rgba(224,65,63,0)}}}}
    @media(max-width:960px){{.hero-content{{grid-template-columns:1fr!important}}.hero-content>div:last-child{{display:none}}}}</style>
</section>"""


def social_proof_strip():
    return """<section class="section-cream" style="padding:2.6rem 0;border-bottom:1px solid rgba(0,0,0,.06)">
  <div class="wrap" style="display:grid;grid-template-columns:repeat(4,1fr);gap:0;text-align:center">
    <div style="padding:1.4rem 1.2rem;border-right:1px solid rgba(0,0,0,.08)">
      <div style="font-family:'Playfair Display',serif;font-size:2.2rem;color:#166A47;line-height:1">12,847</div>
      <div style="font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:#6b7168;margin-top:.4rem">Learners since 2019</div>
    </div>
    <div style="padding:1.4rem 1.2rem;border-right:1px solid rgba(0,0,0,.08)">
      <div style="font-family:'Playfair Display',serif;font-size:2.2rem;color:#166A47;line-height:1">4.8<span style="color:#E6C99B;font-size:1.4rem;margin-left:.4rem">★</span></div>
      <div style="font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:#6b7168;margin-top:.4rem">Trustpilot · 2,140 reviews</div>
    </div>
    <div style="padding:1.4rem 1.2rem;border-right:1px solid rgba(0,0,0,.08)">
      <div style="font-family:'Playfair Display',serif;font-size:2.2rem;color:#166A47;line-height:1">CEFR</div>
      <div style="font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:#6b7168;margin-top:.4rem">Aligned certificate</div>
    </div>
    <div style="padding:1.4rem 1.2rem">
      <div style="font-family:'Playfair Display',serif;font-size:2.2rem;color:#166A47;line-height:1">#1</div>
      <div style="font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:#6b7168;margin-top:.4rem">US Italian school 2026</div>
    </div>
  </div>
</section>"""


def big_headline_lead(color_scheme, eyebrow, headline_html, lead, ital_color="#166A47", eyebrow_color="#166A47"):
    """Section headline used at top of many folds."""
    txt_color = "#0e1a14" if color_scheme == "light" else "#FBFAF6"
    return f"""<div style="max-width:900px;margin-bottom:3rem">
    <div class="eyebrow" style="color:{eyebrow_color};letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">{eyebrow}</div>
    <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.4rem,5vw,4.2rem);line-height:1.05;letter-spacing:-.015em;color:{txt_color};margin:0 0 1.4rem">{headline_html}</h2>
    <p style="font-size:1.15rem;line-height:1.65;color:{'#3a3f3a' if color_scheme=='light' else 'rgba(251,250,246,.82)'};max-width:64ch;margin:0">{lead}</p>
  </div>"""


def two_col_photo_text(A_, img, alt, side, eyebrow, headline_html, body_html, cta=None, bg="cream", ital_color="#166A47"):
    section_class = {"cream": "section-cream", "white": "section-white", "tint": "section-tint", "black": "section-black", "green": "section-green", "red": "section-red"}[bg]
    txt_color = "#0e1a14" if bg in ("cream", "white", "tint") else "#FBFAF6"
    body_color = "#3a3f3a" if bg in ("cream", "white", "tint") else "rgba(251,250,246,.82)"
    eyebrow_col = ital_color if bg in ("cream", "white", "tint") else "#E6C99B"
    ital_c = ital_color if bg in ("cream", "white", "tint") else "#E6C99B"
    text_block = f"""<div>
      <div class="eyebrow" style="color:{eyebrow_col};letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">{eyebrow}</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.2rem,4.6vw,3.8rem);line-height:1.05;color:{txt_color};margin:0 0 1.4rem">{headline_html}</h2>
      <div style="font-size:1.12rem;line-height:1.65;color:{body_color};max-width:52ch">{body_html}</div>
      {"<div style='margin-top:1.6rem'><button class='btn btn-3d btn-3d-primary' data-advisor type='button'>" + cta + "</button></div>" if cta else ""}
    </div>"""
    img_block = f"""<figure style="margin:0">
      <div style="aspect-ratio:4/5;overflow:hidden;box-shadow:0 40px 100px -30px rgba(14,26,20,.35)">
        <img src="{A_}img/{img}" alt="{alt}" style="width:100%;height:100%;object-fit:cover;display:block">
      </div>
    </figure>"""
    cols = f"{img_block}{text_block}" if side == "left" else f"{text_block}{img_block}"
    return f"""<section class="{section_class}" style="padding:clamp(4.5rem,9vw,8rem) 0">
  <div class="wrap" style="display:grid;grid-template-columns:1fr 1fr;gap:clamp(2.4rem,5vw,5rem);align-items:center">
    {cols}
  </div>
  <style>@media(max-width:820px){{[style*="1fr 1fr"]{{grid-template-columns:1fr!important}}}}</style>
</section>"""


def cta_final(bg="green", headline_html=None, sub=None):
    return f"""<section class="section-{bg}" style="padding:clamp(6rem,12vw,11rem) 0;position:relative;overflow:hidden">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 30% 40%, rgba(230,201,155,.08), transparent 60%);pointer-events:none"></div>
  <div class="wrap-narrow" style="position:relative;text-align:center">
    <div class="eyebrow" style="color:#E6C99B;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.6rem">Enrolment</div>
    <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.6rem,6vw,5.4rem);line-height:1.02;color:#FBFAF6;margin:0 0 1.6rem">{headline_html}</h2>
    <p style="font-size:1.2rem;line-height:1.6;color:rgba(251,250,246,.82);max-width:56ch;margin:0 auto 2.4rem">{sub}</p>
    <button class="btn btn-3d btn-3d-primary" data-advisor type="button" style="font-size:1.05rem;padding:1.35rem 2.6rem">Reserve My Placement Call</button>
    <div style="margin-top:2rem;color:rgba(251,250,246,.6);font-size:.85rem">· 4.8 ★ Trustpilot · 12,847 alumni · 7-day money-back guarantee</div>
  </div>
</section>"""


def zoom_class_fold(A_, img="zoom-classroom-marco.jpg", caption="Marco Rinaldi, live from Trastevere · 11 students, one hand raised.", bg="cream"):
    section_class = f"section-{bg}"
    return f"""<section class="{section_class}" style="padding:clamp(4.5rem,9vw,8rem) 0">
  <div class="wrap" style="display:grid;grid-template-columns:1fr 1.1fr;gap:clamp(2.4rem,5vw,5rem);align-items:center">
    <div>
      <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">The room, from the inside</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.4rem,5vw,4rem);line-height:1.05;color:#0e1a14;margin:0 0 1.6rem">A real class, <span class="accent-ital" style="font-style:italic;color:#166A47">in session.</span></h2>
      <p style="font-size:1.12rem;line-height:1.65;color:#3a3f3a;max-width:52ch;margin:0 0 1.6rem">Ten to twelve classmates. One native teacher. Eighty-five minutes of Italian at conversational pace. Cameras on, coffee in hand.</p>
    </div>
    <figure style="margin:0">
      <div style="aspect-ratio:4/3;overflow:hidden;box-shadow:0 40px 100px -30px rgba(14,26,20,.35)">
        <img src="{A_}img/{img}" alt="A Club Italia live class" style="width:100%;height:100%;object-fit:cover">
      </div>
      <figcaption style="font-family:'Playfair Display',serif;font-style:italic;font-size:1.05rem;color:#166A47;margin-top:1rem;text-align:center">{caption}</figcaption>
    </figure>
  </div>
  <style>@media(max-width:820px){{[style*="1fr 1.1fr"]{{grid-template-columns:1fr!important}}}}</style>
</section>"""


def life_grid_fold(A_, headline_html='The Italy <span class="accent-ital" style="font-style:italic;color:#166A47">you speak into.</span>', bg="cream"):
    photos = [
        ("life-caffe-roma.jpg", "A morning in Roma"),
        ("life-trattoria-toscana.jpg", "Sunday lunch in Toscana"),
        ("life-market-bologna.jpg", "The market in Bologna"),
        ("life-scala-milano.jpg", "La Scala di Milano"),
        ("life-gondola-venezia.jpg", "A canal in Venezia"),
        ("life-amalfi-coast.jpg", "The Amalfi coast at dusk"),
    ]
    tiles = "".join(f'''<figure style="margin:0;position:relative;aspect-ratio:4/5;overflow:hidden">
      <img src="{A_}img/{img}" alt="{cap}" style="width:100%;height:100%;object-fit:cover;transition:transform .9s ease">
      <figcaption style="position:absolute;left:0;right:0;bottom:0;padding:1rem 1.2rem;background:linear-gradient(transparent,rgba(0,0,0,.7));color:#FBFAF6;font-family:'Playfair Display',serif;font-style:italic;font-size:1.05rem">{cap}</figcaption>
    </figure>''' for img, cap in photos)
    return f"""<section class="section-{bg}" style="padding:clamp(4.5rem,9vw,8rem) 0">
  <div class="wrap" style="text-align:center;margin-bottom:2.6rem">
    <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">Where the language lives</div>
    <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.4rem,5vw,4rem);line-height:1.05;color:#0e1a14;margin:0 auto;max-width:22ch">{headline_html}</h2>
  </div>
  <div class="wrap-flush" style="padding:0 clamp(1.2rem,2vw,2rem);display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:#0e1a14">
    {tiles}
  </div>
  <style>@media(max-width:820px){{[style*="repeat(3,1fr)"]{{grid-template-columns:repeat(2,1fr)!important}}}}
    @media(max-width:520px){{[style*="repeat(3,1fr)"]{{grid-template-columns:1fr!important}}}}</style>
</section>"""


def trustpilot_wall(A_):
    reviews = [
        ("student-diane.jpg", "Diane", "Boston, MA", "CI Intermedio", "I have taken three courses now and I finally speak Italian with my in-laws in Puglia. The class feels like a dinner table."),
        ("student-robert.jpg", "Robert", "Austin, TX", "Parliamo Confident", "I tried Duolingo for four years. I learned more in Marco's first six weeks than in all of that."),
        ("student-linda.jpg", "Linda", "New York, NY", "CI Elementare", "Chiara teaches with the calm of a woman who has done this for a decade. I look forward to Wednesday nights."),
        ("student-james.jpg", "James", "Seattle, WA", "Capsule Cucina", "Six weeks on Italian food, in Italian, with Giulia from Bologna. My kitchen and my accent are both better."),
        ("student-sarah.jpg", "Sarah", "Chicago, IL", "CI Avanzato", "By the end of the fourth level I was reading Elena Ferrante in the original. Worth every dollar."),
        ("student-michael.jpg", "Michael", "Denver, CO", "Parliamo Foundation", "The advisor placed me perfectly, and Alessandro is the calmest, kindest teacher I have had since college."),
    ]
    cards = "".join(f'''<article class="tp-review-card" style="background:#fff;border:1px solid rgba(0,0,0,.08);padding:1.7rem 1.5rem;display:flex;flex-direction:column;gap:1rem">
    <div style="display:flex;align-items:center;gap:.9rem">
      <img src="{A_}img/{img}" alt="{name}" style="width:52px;height:52px;border-radius:50%;object-fit:cover">
      <div><div style="font-family:'Playfair Display',serif;font-size:1.05rem;color:#0e1a14">{name}</div><div style="font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:#6b7168;margin-top:.15rem">{city} · {course}</div></div>
    </div>
    <div style="color:#E6C99B;font-size:.98rem;letter-spacing:.15em">★★★★★</div>
    <p style="font-family:'Playfair Display',serif;font-style:italic;font-size:1.02rem;line-height:1.5;color:#0e1a14;margin:0">"{quote}"</p>
    <div style="margin-top:auto;padding-top:.9rem;border-top:1px solid rgba(0,0,0,.08);display:flex;justify-content:space-between;font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;color:#6b7168">
      <span style="color:#166A47">✓ Verified</span><span>Reviewed on Trustpilot</span>
    </div>
  </article>''' for img, name, city, course, quote in reviews)
    return f"""<section class="section-white" style="padding:clamp(4.5rem,9vw,8rem) 0">
  <div class="wrap" style="text-align:center;margin-bottom:2.6rem">
    <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">2,140 reviews on Trustpilot</div>
    <div style="font-family:'Playfair Display',serif;font-size:clamp(2.8rem,4.6vw,3.8rem);color:#0e1a14;line-height:1">4.8<span style="color:#E6C99B;font-size:.8em;margin-left:.4rem">★★★★★</span></div>
    <p style="color:#6b7168;font-size:1rem;margin-top:.6rem">"Excellent" · Ranked #1 US Italian school 2026</p>
  </div>
  <div class="wrap" style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.3rem">{cards}</div>
  <style>@media(max-width:960px){{[style*="repeat(3,1fr)"][style*="1.3rem"]{{grid-template-columns:repeat(2,1fr)!important}}}}@media(max-width:600px){{[style*="repeat(3,1fr)"][style*="1.3rem"]{{grid-template-columns:1fr!important}}}}</style>
</section>"""
