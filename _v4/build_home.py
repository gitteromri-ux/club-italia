"""Build the Club Italia homepage — 15 folds, real cinematic imagery."""
import sys
sys.path.insert(0, "/home/user/workspace/club-italia/_v4")
from common import head, footer_scripts, nav_html, A, ROOT

D = 0
NAV = nav_html(D)
A_ = A(D)

# FOLD 1 — HERO
fold1 = f"""<section class="hero" style="position:relative;min-height:100vh;overflow:hidden;background:#04070e">
  <div class="hero-bg" aria-hidden="true">
    <video autoplay muted loop playsinline poster="{A_}img/hero-italian-life.jpg" preload="metadata"
      style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 40%">
      <source src="{A_}video/roma-piazza.mp4" type="video/mp4">
    </video>
    <div style="position:absolute;inset:0;background:
      linear-gradient(105deg, rgba(4,20,15,.88) 0%, rgba(4,20,15,.55) 42%, rgba(50,10,10,.35) 70%, rgba(0,0,0,.75) 100%),
      radial-gradient(ellipse at 30% 55%, rgba(230,201,155,.11), transparent 55%);"></div>
    <div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(0,0,0,.35), transparent 22%, transparent 65%, rgba(0,0,0,.55));"></div>
  </div>
  <div class="wrap hero-content" style="position:relative;z-index:2;display:grid;grid-template-columns:1.15fr .95fr;gap:clamp(2rem,4vw,5rem);align-items:center;min-height:100vh;padding-top:8rem;padding-bottom:6rem">
    <div>
      <div class="eyebrow paper" style="color:#8FC9AB;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">Live from Italy · A cultural language school</div>
      <h1 style="font-family:'Playfair Display',Georgia,serif;font-weight:700;font-size:clamp(4.4rem,10vw,9.5rem);line-height:1.02;letter-spacing:-.022em;color:#FBFAF6;margin:0 0 2rem">
        Learn Italian,<br>
        <span class="accent-ital" style="font-style:italic;font-weight:500;color:#E6C99B">live from Italy,</span><br>
        in small groups of<br>ten to twelve.
      </h1>
      <p class="hero-sub" style="font-family:'Inter',sans-serif;font-size:clamp(1.35rem,1.9vw,1.7rem);line-height:1.55;color:rgba(251,250,246,.86);max-width:52ch;margin:0 0 2.4rem;font-weight:300">
        Real classrooms broadcasting from Roma, Firenze, Bologna and Milano. Native teachers. A CEFR-aligned certificate at the end. Not another app — a school.
      </p>
      <div class="hero-actions" style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2.2rem">
        <button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button>
        <a class="btn btn-3d btn-3d-ghost" href="sample-class.html">Watch a Real Class</a>
      </div>
      <div style="display:flex;gap:2rem;align-items:center;flex-wrap:wrap;color:rgba(251,250,246,.75);font-size:.9rem">
        <div style="display:flex;align-items:center;gap:.6rem">
          <span style="color:#E6C99B;font-size:1.1rem">★★★★★</span>
          <span>4.8 on Trustpilot · 2,140 reviews</span>
        </div>
        <div style="display:flex;align-items:center;gap:.55rem">
          <span style="width:9px;height:9px;border-radius:50%;background:#e0413f;box-shadow:0 0 0 0 rgba(224,65,63,.6);animation:pulse 2s infinite;display:inline-block"></span>
          <span style="letter-spacing:.18em;text-transform:uppercase;font-size:.72rem">12 classrooms broadcasting right now</span>
        </div>
      </div>
    </div>
    <div style="position:relative;aspect-ratio:5/6;height:76%;justify-self:end;width:100%;max-width:640px;align-self:center">
      <img src="{A_}img/zoom-hero-composite.jpg" alt="A live Club Italia class on a laptop, Italian table, coffee at hand"
        style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:40% 22%;
          border-radius:2px;transform:rotate(-1.2deg);
          box-shadow:0 40px 120px -40px rgba(0,0,0,.85), 0 20px 60px -20px rgba(0,0,0,.65);
          mask-image:radial-gradient(ellipse 90% 92% at 50% 48%, black 60%, transparent 100%);
          -webkit-mask-image:radial-gradient(ellipse 90% 92% at 50% 48%, black 60%, transparent 100%);">
      <div style="position:absolute;left:-1.5rem;bottom:1.5rem;background:rgba(4,15,10,.85);backdrop-filter:blur(10px);padding:1rem 1.4rem;border-left:2px solid #E6C99B;max-width:280px">
        <div style="font-family:'Playfair Display',serif;font-style:italic;color:#E6C99B;font-size:1rem;line-height:1.35">Marco Rinaldi · live from Trastevere</div>
        <div style="color:rgba(255,255,255,.65);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;margin-top:.35rem">Monday 7pm ET</div>
      </div>
    </div>
  </div>
  <style>@keyframes pulse{{0%{{box-shadow:0 0 0 0 rgba(224,65,63,.6)}}70%{{box-shadow:0 0 0 12px rgba(224,65,63,0)}}100%{{box-shadow:0 0 0 0 rgba(224,65,63,0)}}}}
    @media(max-width:960px){{.hero-content{{grid-template-columns:1fr!important}}.hero-content>div:last-child{{display:none}}}}
  </style>
</section>"""

# FOLD 2 — SOCIAL PROOF STRIP
fold2 = f"""<section class="section-cream" style="padding:2.6rem 0;border-bottom:1px solid rgba(0,0,0,.06)">
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
  <div class="wrap" style="margin-top:1.8rem;text-align:center">
    <div style="display:inline-flex;gap:.6rem;align-items:center;color:#6b7168;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase">
      <span style="width:8px;height:8px;border-radius:50%;background:#e0413f;animation:pulse 2s infinite"></span>
      12 classrooms live right now · Milano, Roma, Firenze, Bologna, Napoli, Venezia
    </div>
  </div>
</section>"""

# FOLD 3 — THE REAL LIVE CLASSROOM
fold3 = f"""<section class="section-cream" style="padding:clamp(5rem,10vw,9rem) 0">
  <div class="wrap" style="display:grid;grid-template-columns:1fr 1.1fr;gap:clamp(2.4rem,5vw,5.5rem);align-items:center">
    <div>
      <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">What a class actually looks like</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.8rem,5.2vw,4.6rem);line-height:1.05;letter-spacing:-.018em;color:#0e1a14;margin:0 0 1.8rem">
        This is a real Club Italia <span class="accent-ital" style="font-style:italic;font-weight:500;color:#166A47">class in session.</span>
      </h2>
      <p style="font-size:1.2rem;line-height:1.65;color:#3a3f3a;max-width:52ch;margin:0 0 2rem">
        Ten to twelve adult learners. One native teacher, broadcasting live from Trastevere. Cameras on, coffee in hand, an hour and twenty-five minutes of Italian at conversational pace. No app grind, no drill. A room.
      </p>
      <button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Seat</button>
    </div>
    <figure style="margin:0">
      <div style="aspect-ratio:4/3;overflow:hidden;box-shadow:0 40px 100px -30px rgba(14,26,20,.35), 0 15px 40px -10px rgba(14,26,20,.2)">
        <img src="{A_}img/zoom-classroom-marco.jpg" alt="Marco Rinaldi teaching a live Zoom classroom from Rome"
          style="width:100%;height:100%;object-fit:cover;display:block">
      </div>
      <figcaption style="font-family:'Playfair Display',serif;font-style:italic;font-size:1.1rem;color:#166A47;margin-top:1.2rem;text-align:center;line-height:1.5">
        Monday 7pm ET · Marco Rinaldi, live from Trastevere, Rome · 11 students, one hand raised.
      </figcaption>
    </figure>
  </div>
</section>"""

# FOLD 4 — TWO PHONES / TWO WAYS
fold4 = f"""<section class="section-tint" style="padding:clamp(5rem,10vw,9rem) 0;background:#F4EFE5">
  <div class="wrap" style="display:grid;grid-template-columns:1fr 1fr;gap:clamp(2.4rem,5vw,5.5rem);align-items:center">
    <div>
      <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">The Club Italia platform</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.6rem,5vw,4.4rem);line-height:1.06;letter-spacing:-.018em;color:#0e1a14;margin:0 0 1.6rem">
        Your course page. <span class="accent-ital" style="font-style:italic;font-weight:500;color:#166A47">Your live classroom.</span> Both at your fingertips.
      </h2>
      <p style="font-size:1.15rem;line-height:1.65;color:#3a3f3a;max-width:50ch;margin:0 0 1.6rem">
        Every lesson lives on your phone the way any beautiful thing does: quietly, ready. Materials before class, replay after, Biagio to practice with in between. One tap into the live Zoom room when the time comes.
      </p>
      <ul style="list-style:none;padding:0;margin:0;display:grid;gap:.8rem;font-size:1rem;color:#3a3f3a">
        <li>· Slides, transcripts, and homework, delivered the morning of class</li>
        <li>· Every lesson recorded for the life of your enrollment</li>
        <li>· Biagio, our Italian tutor, in your pocket 24/7</li>
      </ul>
    </div>
    <figure style="margin:0">
      <img src="{A_}img/zoom-two-phones.jpg" alt="Two phones side by side, one showing the course dashboard, one showing the live class"
        style="width:100%;aspect-ratio:5/6;object-fit:cover;display:block;box-shadow:0 40px 100px -30px rgba(14,26,20,.35)">
    </figure>
  </div>
</section>"""

# FOLD 5 — COURSE SHOWCASE
def course_card(img, badge, title, sub, meta, price, href):
    return f"""<a href="{href}" class="course-card" style="text-decoration:none;color:inherit;display:flex;flex-direction:column;background:#fff;border-right:1px solid rgba(0,0,0,.07);border-bottom:1px solid rgba(0,0,0,.07);transition:transform .35s ease, box-shadow .35s ease">
    <div style="position:relative;aspect-ratio:5/4;overflow:hidden">
      <img src="{A_}img/{img}" alt="{title}" style="width:100%;height:100%;object-fit:cover;transition:transform .8s ease">
      <div style="position:absolute;top:1rem;left:1rem;background:rgba(4,15,10,.72);color:#E6C99B;padding:.4rem .8rem;font-size:.62rem;letter-spacing:.22em;text-transform:uppercase;backdrop-filter:blur(6px)">{badge}</div>
      <div style="position:absolute;top:1rem;right:1rem;background:#166A47;color:#fff;padding:.5rem .8rem;font-family:'Playfair Display',serif;font-size:1.05rem">{price}</div>
    </div>
    <div style="padding:1.5rem 1.5rem 1.7rem;display:flex;flex-direction:column;gap:.7rem;flex:1;background:#fff">
      <h3 style="font-family:'Playfair Display',serif;font-size:1.55rem;line-height:1.15;margin:0;color:#0e1a14">{title}</h3>
      <div style="font-family:'Playfair Display',serif;font-style:italic;color:#166A47;font-size:1rem">{sub}</div>
      <div style="font-size:.82rem;color:#6b7168;letter-spacing:.04em;margin-top:auto">{meta}</div>
      <div style="display:inline-flex;align-items:center;gap:.5rem;color:#166A47;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;font-weight:600;margin-top:.4rem">Enroll →</div>
    </div>
  </a>"""

def track_header(kicker, title):
    return f"""<div style="grid-column:1/-1;padding:2.2rem 1.5rem 1.4rem;border-bottom:1px solid rgba(0,0,0,.1);background:#F7F3EA;display:flex;align-items:baseline;gap:1.4rem;flex-wrap:wrap">
      <div style="font-size:.7rem;letter-spacing:.28em;text-transform:uppercase;color:#166A47;font-weight:600">{kicker}</div>
      <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:1.35rem;color:#0e1a14">{title}</div>
    </div>"""

fold5_cards = (
    track_header("Club Italia", "Il Corso · CEFR structured, A0 to A2.2")
    + course_card("course-ci1.jpg", "A0 → A1.1", "CI Principiante", "Your first Italian",
                  "40 lessons · 85 min · 10–12 seats", "$84/wk", "pages/courses/ci1.html")
    + course_card("course-ci2.jpg", "A1.1 → A1.2", "CI Elementare", "Speaking with intention",
                  "40 lessons · 85 min · 10–12 seats", "$84/wk", "pages/courses/ci2.html")
    + course_card("course-ci3.jpg", "A1.2 → A2.1", "CI Intermedio", "Real conversations",
                  "40 lessons · 85 min · 10–12 seats", "$84/wk", "pages/courses/ci3.html")
    + course_card("course-ci4.jpg", "A2.1 → A2.2", "CI Avanzato", "Cultural fluency",
                  "40 lessons · 85 min · 10–12 seats", "$84/wk", "pages/courses/ci4.html")
    + track_header("Parliamo Italiano", "Spoken confidence, in twelve weeks")
    + course_card("spoken-ps1.jpg", "Foundation", "Parliamo · Foundation", "Sounds and greetings",
                  "12 lessons · 60 min · 10–12 seats", "$62/wk", "pages/spoken/ps1.html")
    + course_card("spoken-ps2.jpg", "Beginner", "Parliamo · Beginner", "Ordering and asking",
                  "12 lessons · 60 min · 10–12 seats", "$62/wk", "pages/spoken/ps2.html")
    + course_card("spoken-ps3.jpg", "Elementary", "Parliamo · Elementary", "Telling your day",
                  "12 lessons · 60 min · 10–12 seats", "$62/wk", "pages/spoken/ps3.html")
    + course_card("spoken-ps4.jpg", "Confident", "Parliamo · Confident", "Holding your ground",
                  "12 lessons · 60 min · 10–12 seats", "$62/wk", "pages/spoken/ps4.html")
    + track_header("Capsule Culturali", "Short courses. Great Italian passions.")
    + course_card("cap-food.jpg", "6 weeks", "La Cucina Italiana", "Regions on a plate",
                  "6 lessons · 75 min · 10–12 seats", "$220", "pages/culture/cap-food.html")
    + course_card("cap-art.jpg", "6 weeks", "L'Arte del Rinascimento", "Reading a Renaissance canvas",
                  "6 lessons · 75 min · 10–12 seats", "$220", "pages/culture/cap-art.html")
    + course_card("cap-opera.jpg", "6 weeks", "L'Opera in Italiano", "From La Scala with a libretto",
                  "6 lessons · 75 min · 10–12 seats", "$220", "pages/culture/cap-opera.html")
)

fold5 = f"""<section class="section-white" style="padding:clamp(5rem,9vw,8rem) 0 0">
  <div class="wrap" style="text-align:center;margin-bottom:3rem">
    <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">Eleven courses, three tracks</div>
    <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.8rem,5.4vw,4.8rem);line-height:1.05;color:#0e1a14;margin:0;max-width:22ch;margin:0 auto">
      Choose the room <span class="accent-ital" style="font-style:italic;color:#166A47">where your Italian begins.</span>
    </h2>
  </div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:1px solid rgba(0,0,0,.1);border-left:1px solid rgba(0,0,0,.07)">
    {fold5_cards}
  </div>
</section>
<style>.course-card:hover{{transform:translateY(-4px);box-shadow:0 20px 50px -20px rgba(14,26,20,.2);z-index:2;position:relative}}.course-card:hover img{{transform:scale(1.05)}}
  @media(max-width:960px){{.course-card~.course-card{{}}[style*="repeat(4,1fr)"]{{grid-template-columns:repeat(2,1fr)!important}}}}
  @media(max-width:540px){{[style*="repeat(4,1fr)"]{{grid-template-columns:1fr!important}}}}
</style>"""

# FOLD 6 — HOW IT WORKS
def step(num, title, desc, img, alt):
    return f"""<div style="display:grid;grid-template-columns:1.1fr 1fr;gap:clamp(2rem,4vw,4rem);align-items:center;padding:clamp(2rem,4vw,3.5rem) 0;border-bottom:1px solid rgba(255,255,255,.08)">
    <div>
      <div style="font-family:'Playfair Display',serif;font-style:italic;font-weight:400;font-size:clamp(4rem,7vw,6rem);color:#E6C99B;line-height:1;margin-bottom:1rem">{num}</div>
      <h3 style="font-family:'Playfair Display',serif;font-weight:600;font-size:clamp(2rem,3.6vw,3rem);line-height:1.1;color:#FBFAF6;margin:0 0 1.1rem">{title}</h3>
      <p style="font-size:1.1rem;line-height:1.65;color:rgba(251,250,246,.78);max-width:52ch;margin:0">{desc}</p>
    </div>
    <div style="aspect-ratio:4/3;overflow:hidden;box-shadow:0 30px 80px -20px rgba(0,0,0,.6)">
      <img src="{A_}img/{img}" alt="{alt}" style="width:100%;height:100%;object-fit:cover">
    </div>
  </div>"""

fold6 = f"""<section class="section-green" style="padding:clamp(6rem,10vw,9rem) 0">
  <div class="wrap">
    <div style="max-width:820px;margin-bottom:3.5rem">
      <div class="eyebrow" style="color:#E6C99B;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">The five steps</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.8rem,5.6vw,5rem);line-height:1.04;color:#FBFAF6;margin:0">
        From your first hello <span class="accent-ital" style="font-style:italic;color:#E6C99B">to your first conversation</span> in Rome.
      </h2>
    </div>
    {step("I.", "Assess and enroll", "A 20-minute placement call with an academic advisor puts you in the right room from day one. No aptitude test, no gimmicks.", "life-caffe-roma.jpg", "A moment of Roman café life")}
    {step("II.", "Join the platform", "Your course page opens the day you enroll: schedule, materials, replay library, and the Zoom link that will bring your classroom to your kitchen table.", "zoom-classroom-chiara.jpg", "Chiara teaching from her studio in Firenze")}
    {step("III.", "Live classes, every week", "Eighty-five minutes with a native teacher, ten to twelve classmates, and enough coffee. Cameras on. This is where your Italian is made.", "env-marco-desk.jpg", "Marco's teaching studio in Trastevere")}
    {step("IV.", "Practice with Biagio", "Between classes, Biagio, our conversational Italian tutor, keeps your ear warm. Ask him for a phrase, a correction, or a story about Trieste at 2am.", "env-chiara-desk.jpg", "A moment of practice at a warm desk")}
    {step("V.", "Get certified", "Complete the track and receive a printed, CEFR-aligned certificate. Then plan your first week in Italia and speak the language the country was written in.", "life-scala-milano.jpg", "La Scala di Milano at night")}
  </div>
</section>"""

# FOLD 7 — CULTURAL METHOD (4 quadrants)
def quadrant(img, title, desc, badge):
    return f"""<div style="position:relative;aspect-ratio:5/6;overflow:hidden;background:#000">
    <img src="{A_}img/{img}" alt="{title}" style="width:100%;height:100%;object-fit:cover;opacity:.72">
    <div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(0,0,0,.15) 30%, rgba(4,15,10,.9)); display:flex;flex-direction:column;justify-content:flex-end;padding:2rem"></div>
    <div style="position:absolute;inset:0;padding:2rem;display:flex;flex-direction:column;justify-content:flex-end;color:#FBFAF6">
      <div style="font-size:.7rem;letter-spacing:.24em;text-transform:uppercase;color:#E6C99B;margin-bottom:.6rem">{badge}</div>
      <h3 style="font-family:'Playfair Display',serif;font-weight:600;font-size:clamp(1.8rem,2.6vw,2.4rem);line-height:1.12;margin:0 0 .8rem">{title}</h3>
      <p style="font-size:.98rem;line-height:1.55;color:rgba(251,250,246,.86);margin:0;max-width:38ch">{desc}</p>
    </div>
  </div>"""

fold7 = f"""<section class="section-tint" style="padding:clamp(5rem,10vw,9rem) 0;background:#F4EFE5">
  <div class="wrap" style="text-align:center;margin-bottom:3.5rem">
    <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">The Club Italia method</div>
    <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.6rem,5vw,4.4rem);line-height:1.06;color:#0e1a14;margin:0 auto;max-width:22ch">
      Four principles. <span class="accent-ital" style="font-style:italic;color:#166A47">One way of learning.</span>
    </h2>
  </div>
  <div class="wrap-flush" style="display:grid;grid-template-columns:repeat(4,1fr);gap:2px;background:#0e1a14">
    {quadrant("pillar-art.jpg", "Cultural scenario", "Every lesson lives inside a real Italian moment. An espresso in Trastevere, a Sunday at the market, a matinee at La Scala.", "One")}
    {quadrant("pillar-food.jpg", "Live interaction", "Ten to twelve classmates, cameras on. You speak, you are answered. This is where Italian stops being an app and starts being a language.", "Two")}
    {quadrant("pillar-travel.jpg", "Guided structure", "CEFR-aligned progression from A0 to A2.2. Every session a chapter, every chapter a competence, every competence written down.", "Three")}
    {quadrant("pillar-cinema.jpg", "Real task", "You leave every class with a task in Italian: order the coffee, book the room, tell the story. Homework as rehearsal for the real thing.", "Four")}
  </div>
</section>
<style>@media(max-width:960px){{[style*="repeat(4,1fr)"][style*="0e1a14"]{{grid-template-columns:repeat(2,1fr)!important}}}}
  @media(max-width:540px){{[style*="repeat(4,1fr)"][style*="0e1a14"]{{grid-template-columns:1fr!important}}}}
</style>"""

# FOLD 8 — TEACHER WALL
teachers_data = [
    ("chiara", "Chiara Bianchi", "Firenze", "Università degli Studi di Firenze · 9 years"),
    ("marco", "Marco Rinaldi", "Roma", "Sapienza Università di Roma · 11 years"),
    ("giulia", "Giulia Ferrari", "Bologna", "Alma Mater Studiorum · 8 years"),
    ("alessandro", "Alessandro Conti", "Milano", "Università Cattolica · 12 years"),
    ("francesca", "Francesca Ricci", "Napoli", "Università Federico II · 7 years"),
    ("luca", "Luca Moretti", "Venezia", "Università Ca' Foscari · 10 years"),
    ("sofia", "Sofia Greco", "Palermo", "Università degli Studi di Palermo · 6 years"),
]

def teacher_card(slug, name, city, cred):
    return f"""<div style="position:relative;aspect-ratio:3/4;overflow:hidden;background:#000">
    <img src="{A_}img/teacher-{slug}.jpg" alt="{name}, native Italian teacher" style="width:100%;height:100%;object-fit:cover;transition:transform .8s ease, filter .6s ease;filter:grayscale(.15) brightness(.95)">
    <div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 45%,rgba(0,0,0,.9));display:flex;flex-direction:column;justify-content:flex-end;padding:1.4rem 1.4rem 1.6rem;color:#FBFAF6">
      <div style="font-family:'Playfair Display',serif;font-size:1.35rem;line-height:1.15">{name}</div>
      <div style="font-family:'Playfair Display',serif;font-style:italic;color:#E6C99B;font-size:.98rem;margin-top:.25rem">{city}</div>
      <div style="font-size:.75rem;color:rgba(255,255,255,.72);margin-top:.5rem;letter-spacing:.02em;opacity:0;max-height:0;transition:all .4s ease" class="tc-cred">{cred}</div>
    </div>
  </div>"""

fold8 = f"""<section class="section-black" style="padding:clamp(6rem,10vw,9rem) 0">
  <div class="wrap" style="max-width:1000px;margin-bottom:3.5rem;text-align:center">
    <div class="eyebrow paper" style="color:#E6C99B;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">The teachers</div>
    <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.6rem,5.4vw,4.6rem);line-height:1.05;color:#FBFAF6;margin:0 auto;max-width:22ch">
      Seven teachers. Seven Italian cities. <span class="accent-ital" style="font-style:italic;color:#E6C99B">One method.</span>
    </h2>
  </div>
  <div class="wrap-flush" style="padding:0 clamp(1rem,2vw,2rem);display:grid;grid-template-columns:repeat(7,1fr);gap:2px">
    {"".join(teacher_card(*t) for t in teachers_data)}
  </div>
  <div class="wrap" style="text-align:center;margin-top:3rem">
    <a class="btn btn-3d btn-3d-ghost" href="teachers.html">Meet all seven teachers</a>
  </div>
</section>
<style>[style*="repeat(7,1fr)"] > div:hover img{{transform:scale(1.06);filter:none}}
  [style*="repeat(7,1fr)"] > div:hover .tc-cred{{opacity:1;max-height:60px}}
  @media(max-width:1100px){{[style*="repeat(7,1fr)"]{{grid-template-columns:repeat(4,1fr)!important}}}}
  @media(max-width:640px){{[style*="repeat(7,1fr)"]{{grid-template-columns:repeat(2,1fr)!important}}}}
</style>"""

# FOLD 9 — THE STUDENT LIFE (grid)
life_photos = [
    ("life-caffe-roma.jpg", "A morning in Roma"),
    ("life-trattoria-toscana.jpg", "Sunday lunch in Toscana"),
    ("life-market-bologna.jpg", "The market in Bologna"),
    ("life-scala-milano.jpg", "La Scala di Milano"),
    ("life-gondola-venezia.jpg", "A canal in Venezia"),
    ("life-amalfi-coast.jpg", "The Amalfi coast at dusk"),
]

def life_tile(img, cap):
    return f"""<figure style="margin:0;position:relative;aspect-ratio:4/5;overflow:hidden">
      <img src="{A_}img/{img}" alt="{cap}" style="width:100%;height:100%;object-fit:cover;transition:transform .9s ease">
      <figcaption style="position:absolute;left:0;right:0;bottom:0;padding:1rem 1.2rem;background:linear-gradient(transparent,rgba(0,0,0,.7));color:#FBFAF6;font-family:'Playfair Display',serif;font-style:italic;font-size:1.05rem">{cap}</figcaption>
    </figure>"""

fold9 = f"""<section class="section-cream" style="padding:clamp(5rem,10vw,9rem) 0">
  <div class="wrap" style="text-align:center;margin-bottom:3rem">
    <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">Where the language lives</div>
    <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.6rem,5vw,4.4rem);line-height:1.05;color:#0e1a14;margin:0 auto;max-width:22ch">
      The Italy <span class="accent-ital" style="font-style:italic;color:#166A47">you speak into.</span>
    </h2>
  </div>
  <div class="wrap-flush" style="padding:0 clamp(1.2rem,2vw,2rem);display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:#0e1a14">
    {"".join(life_tile(*p) for p in life_photos)}
  </div>
</section>
<style>[style*="repeat(3,1fr)"] figure:hover img{{transform:scale(1.04)}}
  @media(max-width:820px){{[style*="repeat(3,1fr)"]{{grid-template-columns:repeat(2,1fr)!important}}}}
  @media(max-width:520px){{[style*="repeat(3,1fr)"]{{grid-template-columns:1fr!important}}}}
</style>"""

# FOLD 10 — BIAGIO
fold10 = f"""<section class="section-red" style="padding:clamp(6rem,10vw,9rem) 0;overflow:hidden">
  <div class="wrap" style="display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(2.5rem,5vw,5rem);align-items:center">
    <div style="position:relative">
      <div style="position:absolute;inset:-20%;background:radial-gradient(circle at center, rgba(230,201,155,.28), transparent 60%);pointer-events:none"></div>
      <img src="{A_}img/biagio.png" alt="Biagio, the Club Italia AI Italian tutor" style="width:100%;max-width:420px;position:relative;filter:drop-shadow(0 30px 60px rgba(0,0,0,.5))">
    </div>
    <div>
      <div class="eyebrow" style="color:#E6C99B;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">Between classes</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.6rem,5.2vw,4.6rem);line-height:1.05;color:#FBFAF6;margin:0 0 1.6rem">
        Between classes, <span class="accent-ital" style="font-style:italic;color:#E6C99B">meet Biagio.</span>
      </h2>
      <p style="font-size:1.2rem;line-height:1.65;color:rgba(251,250,246,.86);max-width:52ch;margin:0 0 2rem">
        Biagio is your after-hours Italian tutor. Ask him a question, hand him a sentence, let him correct your pronunciation at midnight. He is trained on the same syllabus your teacher uses and available to every enrolled Club Italia member.
      </p>
      <a class="btn btn-3d btn-3d-primary" href="biagio.html">Meet Biagio</a>
      <div style="margin-top:2.5rem;background:rgba(0,0,0,.35);backdrop-filter:blur(12px);border:1px solid rgba(230,201,155,.2);padding:1.6rem 1.6rem;max-width:560px">
        <div style="font-size:.68rem;letter-spacing:.24em;text-transform:uppercase;color:#E6C99B;margin-bottom:1rem">A conversation, this morning</div>
        <div style="display:grid;gap:.7rem;font-size:.98rem;line-height:1.5">
          <div style="color:rgba(255,255,255,.82)"><em style="font-style:italic;color:#E6C99B">You</em> · Come si dice "sold out" in italiano?</div>
          <div style="color:rgba(255,255,255,.82)"><em style="font-style:italic;color:#E6C99B">Biagio</em> · "Tutto esaurito" — literally "all used up". Often you'll see it on café signs at the end of a busy Saturday.</div>
          <div style="color:rgba(255,255,255,.82)"><em style="font-style:italic;color:#E6C99B">You</em> · E "I'll have another"?</div>
          <div style="color:rgba(255,255,255,.82)"><em style="font-style:italic;color:#E6C99B">Biagio</em> · "Un altro, per favore." Add a smile and you're a local.</div>
          <div style="color:rgba(255,255,255,.82)"><em style="font-style:italic;color:#E6C99B">You</em> · Grazie mille.</div>
        </div>
      </div>
    </div>
  </div>
</section>
<style>@media(max-width:960px){{[style*=".85fr 1.15fr"]{{grid-template-columns:1fr!important}}}}</style>"""

# FOLD 11 — TRUSTPILOT WALL
reviews_data = [
    ("student-diane.jpg", "Diane", "Boston, MA", "CI Intermedio", "I have taken three courses now and I finally speak Italian with my in-laws in Puglia. The class feels like a dinner table."),
    ("student-robert.jpg", "Robert", "Austin, TX", "Parliamo Confident", "I tried Duolingo for four years. I learned more in Marco's first six weeks than in all of that."),
    ("student-linda.jpg", "Linda", "New York, NY", "CI Elementare", "Chiara teaches with the calm of a woman who has done this for a decade. I look forward to Wednesday nights."),
    ("student-james.jpg", "James", "Seattle, WA", "Capsule Cucina", "Six weeks on Italian food, in Italian, with Giulia from Bologna. My kitchen and my accent are both better."),
    ("student-sarah.jpg", "Sarah", "Chicago, IL", "CI Avanzato", "By the end of the fourth level I was reading Elena Ferrante in the original. That is worth the price of everything I have ever paid for."),
    ("student-michael.jpg", "Michael", "Denver, CO", "Parliamo Foundation", "The advisor placed me perfectly, and Alessandro is the calmest, kindest teacher I have had since college."),
]

def review_card(img, name, city, course, quote):
    return f"""<article class="tp-review-card" style="background:#fff;border:1px solid rgba(0,0,0,.08);padding:1.8rem 1.6rem;display:flex;flex-direction:column;gap:1rem">
    <div style="display:flex;align-items:center;gap:.9rem">
      <img src="{A_}img/{img}" alt="{name}" style="width:56px;height:56px;border-radius:50%;object-fit:cover">
      <div>
        <div style="font-family:'Playfair Display',serif;font-size:1.05rem;color:#0e1a14">{name}</div>
        <div style="font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:#6b7168;margin-top:.15rem">{city} · {course}</div>
      </div>
    </div>
    <div style="color:#E6C99B;font-size:1rem;letter-spacing:.15em">★★★★★</div>
    <p style="font-family:'Playfair Display',serif;font-style:italic;font-size:1.05rem;line-height:1.5;color:#0e1a14;margin:0">"{quote}"</p>
    <div style="margin-top:auto;padding-top:1rem;border-top:1px solid rgba(0,0,0,.08);display:flex;justify-content:space-between;align-items:center;font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:#6b7168">
      <span style="color:#166A47">✓ Verified</span>
      <span>Reviewed on Trustpilot</span>
    </div>
  </article>"""

fold11 = f"""<section class="section-white" style="padding:clamp(5rem,10vw,9rem) 0">
  <div class="wrap" style="text-align:center;margin-bottom:3rem">
    <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">2,140 reviews on Trustpilot</div>
    <div style="font-family:'Playfair Display',serif;font-size:clamp(3rem,5vw,4rem);color:#0e1a14;line-height:1">
      4.8<span style="color:#E6C99B;font-size:.8em;margin-left:.4rem">★★★★★</span>
    </div>
    <p style="color:#6b7168;font-size:1rem;margin-top:.6rem;letter-spacing:.02em">"Excellent" · Ranked #1 US Italian language school 2026</p>
  </div>
  <div class="wrap" style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem">
    {"".join(review_card(*r) for r in reviews_data)}
  </div>
</section>
<style>@media(max-width:960px){{[style*="repeat(3,1fr)"][style*="1.4rem"]{{grid-template-columns:repeat(2,1fr)!important}}}}
  @media(max-width:620px){{[style*="repeat(3,1fr)"][style*="1.4rem"]{{grid-template-columns:1fr!important}}}}
</style>"""

# FOLD 12 — CERTIFICATE + OUTCOMES
fold12 = f"""<section class="section-cream" style="padding:clamp(5rem,10vw,9rem) 0">
  <div class="wrap" style="display:grid;grid-template-columns:1.1fr 1fr;gap:clamp(2.4rem,5vw,5.5rem);align-items:center">
    <div>
      <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">On graduation</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.6rem,5vw,4.4rem);line-height:1.05;color:#0e1a14;margin:0 0 1.6rem">
        A CEFR-aligned certificate. <span class="accent-ital" style="font-style:italic;color:#166A47">A new life in Italian.</span>
      </h2>
      <p style="font-size:1.15rem;line-height:1.65;color:#3a3f3a;max-width:52ch;margin:0 0 1.8rem">
        Every track ends with an assessed CEFR competence, a printed certificate, and a real-world outcome. Not a badge, not a screenshot: a document from a school.
      </p>
      <ul style="list-style:none;padding:0;margin:0;display:grid;gap:1rem;font-size:1.05rem;color:#0e1a14">
        <li style="padding-left:1.4rem;position:relative"><span style="position:absolute;left:0;top:.55rem;width:8px;height:8px;background:#166A47;border-radius:50%"></span>Speak Italian in real classroom settings by lesson 12</li>
        <li style="padding-left:1.4rem;position:relative"><span style="position:absolute;left:0;top:.55rem;width:8px;height:8px;background:#166A47;border-radius:50%"></span>Read a menu, a signboard, a short article without a phone</li>
        <li style="padding-left:1.4rem;position:relative"><span style="position:absolute;left:0;top:.55rem;width:8px;height:8px;background:#166A47;border-radius:50%"></span>Hold a five-minute conversation with a stranger in Firenze</li>
        <li style="padding-left:1.4rem;position:relative"><span style="position:absolute;left:0;top:.55rem;width:8px;height:8px;background:#166A47;border-radius:50%"></span>Write an email, a text, a short letter in idiomatic Italian</li>
        <li style="padding-left:1.4rem;position:relative"><span style="position:absolute;left:0;top:.55rem;width:8px;height:8px;background:#166A47;border-radius:50%"></span>Sit and pass a formal CEFR external exam if you choose to</li>
      </ul>
    </div>
    <figure style="margin:0">
      <div style="aspect-ratio:5/6;overflow:hidden;box-shadow:0 40px 100px -30px rgba(14,26,20,.35)">
        <img src="{A_}img/env-chiara-desk.jpg" alt="A Club Italia certificate on a warm wooden table beside a moka pot"
          style="width:100%;height:100%;object-fit:cover">
      </div>
      <figcaption style="font-family:'Playfair Display',serif;font-style:italic;font-size:1rem;color:#166A47;margin-top:1rem;text-align:center">Every graduate receives a printed certificate.</figcaption>
    </figure>
  </div>
</section>
<style>@media(max-width:960px){{[style*="1.1fr 1fr"]{{grid-template-columns:1fr!important}}}}</style>"""

# FOLD 13 — PRICING
def price_card(kicker, price, per, title, feats, cta, featured=False):
    border = "2px solid #166A47" if featured else "1px solid rgba(0,0,0,.1)"
    badge = '<div style="position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:#166A47;color:#fff;padding:.4rem 1rem;font-size:.68rem;letter-spacing:.22em;text-transform:uppercase;font-weight:600;white-space:nowrap">Best Value · Save $440</div>' if featured else ""
    feats_html = "".join(f'<li style="padding:.6rem 0;border-bottom:1px solid rgba(0,0,0,.06);color:#3a3f3a;font-size:.95rem">{f}</li>' for f in feats)
    return f"""<div style="position:relative;background:#fff;border:{border};padding:2.4rem 1.8rem;display:flex;flex-direction:column;gap:1.2rem">
    {badge}
    <div style="font-size:.7rem;letter-spacing:.26em;text-transform:uppercase;color:#166A47;font-weight:600">{kicker}</div>
    <h3 style="font-family:'Playfair Display',serif;font-size:1.9rem;margin:0;color:#0e1a14;line-height:1.15">{title}</h3>
    <div style="font-family:'Playfair Display',serif;font-size:3.4rem;color:#0e1a14;line-height:1">
      {price}<span style="font-size:1rem;color:#6b7168;font-style:italic;margin-left:.4rem">{per}</span>
    </div>
    <ul style="list-style:none;padding:0;margin:.6rem 0 0">{feats_html}</ul>
    <button class="btn btn-3d btn-3d-primary" data-advisor type="button" style="margin-top:auto">{cta}</button>
  </div>"""

fold13 = f"""<section class="section-white" style="padding:clamp(5rem,10vw,9rem) 0">
  <div class="wrap" style="text-align:center;margin-bottom:3rem">
    <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">Three ways to enrol</div>
    <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.6rem,5vw,4.4rem);line-height:1.05;color:#0e1a14;margin:0 auto;max-width:22ch">
      Fair pricing, <span class="accent-ital" style="font-style:italic;color:#166A47">quiet commitment.</span>
    </h2>
  </div>
  <div class="wrap" style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem;align-items:stretch">
    {price_card("Monthly", "$84", "/wk", "Monthly Rolling", ["1 live class per week", "10–12 classmates, native teacher", "Lifetime replays", "Biagio AI tutor", "Cancel any month"], "Reserve My Placement Call")}
    {price_card("Annual · 12 months", "$62", "/wk", "Club Italia Annual", ["Everything in Monthly, plus:", "Save $440 across the year", "Priority scheduling", "Capsule Culturali included", "CEFR certificate on graduation"], "Reserve My Placement Call", featured=True)}
    {price_card("Term · 4 months", "$73", "/wk", "Single Term", ["1 CEFR level, cover to cover", "Group placement guaranteed", "Lifetime replays", "Biagio AI tutor", "Renew or upgrade any time"], "Reserve My Placement Call")}
  </div>
  <div class="wrap" style="text-align:center;margin-top:3rem;color:#6b7168;font-size:.98rem">
    <span style="color:#166A47;font-weight:600">✓</span>&nbsp; 7-day full refund guarantee · Sit through your first two lessons, decide from there.
  </div>
</section>
<style>@media(max-width:960px){{[style*="repeat(3,1fr)"][style*="1.6rem"]{{grid-template-columns:1fr!important}}}}</style>"""

# FOLD 14 — FAQ
faqs = [
    ("How is Club Italia different from Duolingo, Babbel or a private tutor?",
     "Club Italia is a school, not an app. You are placed by an advisor into a live weekly classroom of ten to twelve adult learners taught by a native, university-credentialed Italian teacher on the ground in Italy. Every course is CEFR-aligned, every graduation is certified, and every student is known by name. A private tutor is one voice with no peer conversation; an app is no voice with no classroom. Club Italia is both a room and a syllabus."),
    ("Who teaches, and where are they?",
     "Seven Italian teachers, each based in an Italian city: Chiara in Firenze, Marco in Roma, Giulia in Bologna, Alessandro in Milano, Francesca in Napoli, Luca in Venezia, and Sofia in Palermo. All hold university degrees in Italian pedagogy or literature. All are native speakers with a minimum of six years of adult-education experience. All broadcast live from their Italian studios."),
    ("How does the placement call work?",
     "You book a 20-minute video call with an academic advisor. We ask about your goals, your exposure to Italian, and your schedule, then place you in the correct level. No test, no fee, no obligation. Most learners are enrolled by the end of the call, but you may take a week to decide."),
    ("Can I switch levels if my group is too easy or too hard?",
     "Yes. Within your first four weeks you may transfer between levels at no cost. After that we reassess only at the start of a new term, when transfers remain free."),
    ("What technology do I need?",
     "A laptop or tablet with a camera, a stable internet connection, and a quiet room. That is all. Every class is on Zoom. If you can join a video call, you can attend Club Italia."),
    ("What happens if I miss a class?",
     "Every session is recorded and uploaded to your course page within 24 hours. You retain access to your recordings for the life of your enrollment. Miss more than two consecutive sessions and your teacher will reach out personally to help you catch up."),
    ("Do I receive a certificate?",
     "Yes. On completion of every CEFR track you receive a printed Club Italia certificate stating your level, teacher, and cohort. It is not a state-issued diploma, but it is a formal document from a private language school and is recognized by employers as continuing education."),
    ("What is the refund policy?",
     "You have seven days from your first live class to request a full refund. No forms, no negotiations. Beyond seven days, monthly plans may cancel at any time; annual and term plans may transfer credit toward future courses."),
    ("Do you offer courses for children?",
     "Not at this time. Club Italia serves adult learners aged 18 and over, most of whom are between 30 and 70. Our sister brand at eTeacher Group offers Italian for younger learners; ask an advisor for a referral."),
    ("How do I pay, and can I split the cost?",
     "We accept every major credit card, PayPal, and bank transfer. Annual enrollments may be paid in three equal instalments at no interest; term and monthly plans are billed on the same day each month. Enterprise and gift arrangements are also available on request."),
]

def faq_item(q, a):
    return f"""<details class="faq-item" style="border-bottom:1px solid rgba(0,0,0,.1);padding:1.6rem 0;cursor:pointer;list-style:none">
    <summary style="display:flex;justify-content:space-between;align-items:flex-start;gap:2rem;font-family:'Playfair Display',serif;font-weight:500;font-size:1.35rem;line-height:1.35;color:#0e1a14;list-style:none;cursor:pointer">
      <span style="flex:1">{q}</span>
      <span style="color:#E6C99B;font-family:'Playfair Display',serif;font-size:1.8rem;line-height:1;transition:transform .3s ease" class="faq-plus">+</span>
    </summary>
    <div style="padding-top:1.2rem;font-size:1.05rem;line-height:1.65;color:#3a3f3a;max-width:72ch">{a}</div>
  </details>"""

fold14 = f"""<section class="section-tint" style="padding:clamp(5rem,10vw,9rem) 0;background:#F4EFE5">
  <div class="wrap-narrow">
    <div style="text-align:center;margin-bottom:3rem">
      <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">Answers</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.4rem,5vw,4rem);line-height:1.05;color:#0e1a14;margin:0">
        Everything worth asking <span class="accent-ital" style="font-style:italic;color:#166A47">before you enroll.</span>
      </h2>
    </div>
    <div>{"".join(faq_item(q, a) for q, a in faqs)}</div>
  </div>
</section>
<style>.faq-item[open] .faq-plus{{transform:rotate(45deg)}}
  .faq-item summary::-webkit-details-marker{{display:none}}</style>"""

# FOLD 15 — FINAL CTA
fold15 = f"""<section class="section-green" style="padding:clamp(6rem,12vw,11rem) 0;position:relative;overflow:hidden">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 30% 40%, rgba(230,201,155,.08), transparent 60%);pointer-events:none"></div>
  <div class="wrap-narrow" style="position:relative;text-align:center">
    <div class="eyebrow" style="color:#E6C99B;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.6rem">Enrolment</div>
    <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(3rem,6.5vw,6rem);line-height:1.02;color:#FBFAF6;margin:0 0 1.6rem">
      Culture speaks Italian. <span class="accent-ital" style="font-style:italic;color:#E6C99B">What about you?</span>
    </h2>
    <p style="font-size:1.25rem;line-height:1.6;color:rgba(251,250,246,.82);max-width:56ch;margin:0 auto 2.8rem">
      Twenty minutes with an academic advisor. No aptitude test, no pressure. Just a plan for the year of Italian ahead of you.
    </p>
    <button class="btn btn-3d btn-3d-primary" data-advisor type="button" style="font-size:1.05rem;padding:1.4rem 2.8rem">Reserve My Placement Call</button>
    <div style="margin-top:2.4rem;color:rgba(251,250,246,.6);font-size:.85rem;letter-spacing:.02em">
      · 4.8 ★ on Trustpilot · 12,847 alumni · CEFR certified · 7-day money-back guarantee
    </div>
  </div>
</section>"""

# ASSEMBLE
html = head("Club Italia — Learn Italian, live from Italy",
            "A cultural language school for adults. Live weekly classes from Italy with native teachers, small groups of 10 to 12, CEFR-aligned certificate. Ranked #1 US Italian school 2026.",
            depth=0) + "\n"
html += NAV + "\n"
html += fold1 + "\n" + fold2 + "\n" + fold3 + "\n" + fold4 + "\n" + fold5 + "\n"
html += fold6 + "\n" + fold7 + "\n" + fold8 + "\n" + fold9 + "\n" + fold10 + "\n"
html += fold11 + "\n" + fold12 + "\n" + fold13 + "\n" + fold14 + "\n" + fold15 + "\n"
html += footer_scripts(depth=0)

(ROOT / "index.html").write_text(html)
print(f"index.html written · {len(html)} bytes · 15 folds")
