"""Build the remaining 10 pages: teachers, biagio, how-it-works, pricing,
culture, method, courses (index), faq, sample-class.
All at depth 0 (root)."""
import sys
sys.path.insert(0, "/home/user/workspace/club-italia/_v4")
from common import head, footer_scripts, nav_html, ROOT
from parts import (hero_cinematic, social_proof_strip, zoom_class_fold,
                   life_grid_fold, trustpilot_wall, cta_final, two_col_photo_text)

D = 0
A_ = "assets/"
NAV = nav_html(D)
FOOT = footer_scripts(D)

TEACHERS = [
    ("chiara", "Chiara Bianchi", "Firenze", "Toscana",
     "Università degli Studi di Firenze · 9 years",
     "Chiara reads Ferrante on the train and teaches with the calm of a decade in the classroom. Her students say she makes the imperfetto feel like a favor Italian is doing them.",
     "env-chiara-desk.jpg", "life-uffizi-hall.jpg"),
    ("marco", "Marco Rinaldi", "Roma", "Lazio",
     "Sapienza Università di Roma · 11 years",
     "Marco has taught Italian for eleven years at Sapienza and at Club Italia. He believes the first year of Italian is best learned inside a real Roman morning: at a bar, at a market, in a taxi.",
     "env-marco-desk.jpg", "life-caffe-roma.jpg"),
    ("giulia", "Giulia Ferrari", "Bologna", "Emilia-Romagna",
     "Alma Mater Studiorum · 8 years",
     "Giulia teaches at Alma Mater and at Club Italia. Her third-level students say she is the reason they finally understood the congiuntivo, because she treats it like a mood, not a form.",
     "env-giulia-kitchen.jpg", "life-market-bologna.jpg"),
    ("alessandro", "Alessandro Conti", "Milano", "Lombardia",
     "Università Cattolica del Sacro Cuore · 12 years",
     "Alessandro has taught adult learners for twelve years, from Milano and Torino. His fourth-level class reads Ferrante together, argues about Sorrentino, and finishes the year hosting a two-hour dinner in Italian.",
     "env-marco-desk.jpg", "life-scala-milano.jpg"),
    ("francesca", "Francesca Ricci", "Napoli", "Campania",
     "Università Federico II · 7 years",
     "Francesca is a Neapolitan who teaches with the warmth and speed of her city. Her Parliamo groups leave able to argue about pasta with the person next to them.",
     "env-chiara-desk.jpg", "life-amalfi-coast.jpg"),
    ("luca", "Luca Moretti", "Venezia", "Veneto",
     "Università Ca' Foscari · 10 years",
     "Luca teaches from a small room above a canal. His Parliamo groups leave able to tell a five-minute story about their last week with the tense-work of a native.",
     "env-marco-desk.jpg", "life-gondola-venezia.jpg"),
    ("sofia", "Sofia Greco", "Palermo", "Sicilia",
     "Università degli Studi di Palermo · 6 years",
     "Sofia teaches beginners with the patience of an aunt. Her Parliamo groups leave with a Sicilian ear and a Roman confidence: they say the word, they mean it.",
     "env-giulia-kitchen.jpg", "life-trattoria-toscana.jpg"),
]

# ====================================================================
# TEACHERS PAGE
# ====================================================================
def build_teachers():
    def teacher_row(slug, name, city, region, cred, bio, env_img, life_img, side):
        left = f"""<div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem">
          <img src="{A_}img/teacher-{slug}.jpg" alt="{name}" style="width:100%;aspect-ratio:3/4;object-fit:cover;box-shadow:0 30px 80px -20px rgba(14,26,20,.35)">
          <img src="{A_}img/{env_img}" alt="{name}'s studio in {city}" style="width:100%;aspect-ratio:3/4;object-fit:cover;box-shadow:0 30px 80px -20px rgba(14,26,20,.35)">
        </div>"""
        right = f"""<div>
          <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1rem">{region} · {cred}</div>
          <h3 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.2rem,4.6vw,3.6rem);line-height:1.05;color:#0e1a14;margin:0 0 1rem">{name},<br><span class="accent-ital" style="font-style:italic;color:#166A47">live from {city}.</span></h3>
          <p style="font-size:1.12rem;line-height:1.65;color:#3a3f3a;max-width:46ch;margin:0">{bio}</p>
        </div>"""
        cols = f"{left}{right}" if side == "left" else f"{right}{left}"
        return f"""<section class="section-cream" style="padding:clamp(4.5rem,9vw,8rem) 0;border-bottom:1px solid rgba(0,0,0,.06)">
          <div class="wrap" style="display:grid;grid-template-columns:1fr 1fr;gap:clamp(2.4rem,5vw,5rem);align-items:center">{cols}</div>
          <style>@media(max-width:820px){{[style*="1fr 1fr"]{{grid-template-columns:1fr!important}}}}</style>
        </section>"""

    rows = ""
    for i, t in enumerate(TEACHERS):
        rows += teacher_row(*t, side=("left" if i % 2 == 0 else "right"))

    html = head("The seven teachers · Club Italia",
                "Seven native Italian teachers, in seven Italian cities. Sapienza, Alma Mater, Ca' Foscari. Meet Chiara, Marco, Giulia, Alessandro, Francesca, Luca and Sofia.",
                depth=0) + "\n" + NAV + "\n"
    html += hero_cinematic(A_, "roma-piazza.mp4", "hero-teacher-live.jpg",
                            "The teachers",
                            'Seven teachers.<br>Seven Italian cities.<br><span class="accent-ital" style="font-style:italic;color:#E6C99B">One method.</span>',
                            "Every Club Italia teacher is a native Italian, university-credentialed in pedagogy or literature, and living and broadcasting from their Italian city. This is not a marketplace of freelancers. It is a faculty.",
                            cta_ghost=("See the courses", "courses.html"),
                            right_img="zoom-classroom-marco.jpg",
                            right_caption="A live faculty class · morning of enrollment") + "\n"
    html += social_proof_strip() + "\n"
    html += rows
    html += trustpilot_wall(A_) + "\n"
    html += cta_final(bg="green",
                      headline_html='One of these seven, <span class="accent-ital" style="font-style:italic;color:#E6C99B">will be your teacher.</span>',
                      sub="A 20-minute placement call with an academic advisor will put you in the right room with the right teacher.")
    html += FOOT
    (ROOT / "teachers.html").write_text(html)
    return len(html)

# ====================================================================
# BIAGIO PAGE
# ====================================================================
def build_biagio():
    def hero():
        return f"""<section class="hero" style="position:relative;min-height:100vh;overflow:hidden;background:linear-gradient(180deg, #6b1a20 0%, #3a0810 100%)">
          <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 60% 40%, rgba(230,201,155,.15), transparent 60%);"></div>
          <div class="wrap" style="position:relative;z-index:2;display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(2rem,4vw,5rem);align-items:center;min-height:100vh;padding-top:8rem;padding-bottom:6rem">
            <div style="position:relative">
              <div style="position:absolute;inset:-20%;background:radial-gradient(circle at center, rgba(230,201,155,.28), transparent 60%);pointer-events:none"></div>
              <img src="{A_}img/biagio.png" alt="Biagio, the AI Italian tutor" style="width:100%;max-width:460px;position:relative;filter:drop-shadow(0 40px 80px rgba(0,0,0,.6))">
            </div>
            <div>
              <div class="eyebrow paper" style="color:#E6C99B;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">Your after-hours Italian tutor</div>
              <h1 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(3.8rem,9vw,8rem);line-height:1.02;letter-spacing:-.022em;color:#FBFAF6;margin:0 0 1.6rem">Meet <span class="accent-ital" style="font-style:italic;color:#E6C99B">Biagio.</span></h1>
              <p style="font-size:1.4rem;line-height:1.55;color:rgba(251,250,246,.86);max-width:52ch;margin:0 0 2rem;font-weight:300">Trained on the same syllabus your teacher uses. Available at every hour of every day. Included in every Club Italia enrollment.</p>
              <div style="display:flex;gap:1rem;flex-wrap:wrap">
                <button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button>
                <a class="btn btn-3d btn-3d-ghost" href="#chat">Try Biagio below</a>
              </div>
            </div>
          </div>
          <style>@media(max-width:820px){{[style*=".85fr 1.15fr"]{{grid-template-columns:1fr!important}}}}</style>
        </section>"""

    def chat_fold():
        return f"""<section id="chat" class="section-cream" style="padding:clamp(5rem,9vw,8rem) 0">
          <div class="wrap-narrow" style="text-align:center;margin-bottom:2.6rem">
            <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">Try Biagio</div>
            <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.4rem,5vw,4rem);line-height:1.05;color:#0e1a14;margin:0">A conversation, <span class="accent-ital" style="font-style:italic;color:#166A47">happening this morning.</span></h2>
          </div>
          <div class="wrap-narrow" style="background:#fff;border:1px solid rgba(0,0,0,.1);box-shadow:0 30px 80px -20px rgba(14,26,20,.2);overflow:hidden">
            <div style="background:#0e1a14;color:#E6C99B;padding:1rem 1.4rem;display:flex;justify-content:space-between;font-size:.72rem;letter-spacing:.2em;text-transform:uppercase">
              <span>Biagio · your Italian tutor</span><span style="color:#8FC9AB">● online</span>
            </div>
            <div style="padding:1.6rem;display:grid;gap:1rem;font-family:'Inter',sans-serif">
              <div style="align-self:flex-end;background:#166A47;color:#FBFAF6;padding:.9rem 1.2rem;border-radius:14px 14px 3px 14px;max-width:75%">Come si dice "sold out" in italiano?</div>
              <div style="background:#F4EFE5;color:#0e1a14;padding:.9rem 1.2rem;border-radius:14px 14px 14px 3px;max-width:75%"><em style="font-style:italic;color:#166A47">Biagio.</em> "Tutto esaurito" — literally "all used up". You'll see it on café signs at the end of a busy Saturday.</div>
              <div style="align-self:flex-end;background:#166A47;color:#FBFAF6;padding:.9rem 1.2rem;border-radius:14px 14px 3px 14px;max-width:75%">E "I'll have another"?</div>
              <div style="background:#F4EFE5;color:#0e1a14;padding:.9rem 1.2rem;border-radius:14px 14px 14px 3px;max-width:75%"><em style="font-style:italic;color:#166A47">Biagio.</em> "Un altro, per favore." Add a smile and you're a local.</div>
              <div style="align-self:flex-end;background:#166A47;color:#FBFAF6;padding:.9rem 1.2rem;border-radius:14px 14px 3px 14px;max-width:75%">Perfetto, grazie mille.</div>
              <div style="background:#F4EFE5;color:#0e1a14;padding:.9rem 1.2rem;border-radius:14px 14px 14px 3px;max-width:75%"><em style="font-style:italic;color:#166A47">Biagio.</em> Prego, sempre a disposizione.</div>
            </div>
            <div style="padding:1rem 1.6rem;border-top:1px solid rgba(0,0,0,.08);display:flex;gap:.8rem;align-items:center;color:#6b7168;font-size:.9rem"><span style="flex:1">Ask Biagio anything in Italian or English…</span><button class="btn btn-3d btn-3d-primary" style="padding:.7rem 1.4rem;font-size:.72rem" data-advisor type="button">Enrol to unlock</button></div>
          </div>
        </section>"""

    def in_the_wild():
        return two_col_photo_text(A_, "life-caffe-roma.jpg", "Biagio in a Roman café", "left",
            "Biagio in the wild",
            'On the train, in the café, <span class="accent-ital" style="font-style:italic;color:#166A47">on the sofa at midnight.</span>',
            "<p>Biagio lives in your phone the way any good tutor should: quietly, ready, uninterrupting. Ask him for a phrase before your dinner, a correction on an email, a story about Trieste at 2am. He answers in Italian, in English, or in both.</p>",
            bg="cream")

    def capabilities():
        caps = [
            ("Corrects your Italian", "Paste a sentence, an email, a text; Biagio returns a native-register rewrite and explains the change in one line."),
            ("Explains grammar in one line", "Ask 'why the subjunctive here'; Biagio gives one line of grammar and one line of example. No lecture."),
            ("Reads texts aloud", "Paste an Italian article; Biagio reads it aloud in a native voice and lets you hit pause on any phrase."),
            ("Roleplays a scene", "Ask for a market scene, a hotel check-in, a phone reservation. Biagio takes the other role and responds in Italian."),
            ("Trained on your syllabus", "Biagio knows what you covered in class last Tuesday and won't get ahead of you or fall behind."),
            ("Available at every hour", "Class is Monday at 7pm. Practice is any hour of any day."),
        ]
        cards = "".join(f"""<div style="background:#fff;border:1px solid rgba(0,0,0,.08);padding:1.6rem 1.4rem">
          <h3 style="font-family:'Playfair Display',serif;font-size:1.35rem;color:#0e1a14;margin:0 0 .7rem;font-weight:600">{t}</h3>
          <p style="font-size:.98rem;color:#3a3f3a;line-height:1.55;margin:0">{d}</p>
        </div>""" for t, d in caps)
        return f"""<section class="section-white" style="padding:clamp(5rem,9vw,8rem) 0">
          <div class="wrap" style="text-align:center;margin-bottom:2.6rem">
            <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">What Biagio can do</div>
            <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.4rem,5vw,4rem);line-height:1.05;color:#0e1a14;margin:0">Six things you can ask Biagio, <span class="accent-ital" style="font-style:italic;color:#166A47">tonight.</span></h2>
          </div>
          <div class="wrap" style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem">{cards}</div>
          <style>@media(max-width:960px){{.section-white [style*="repeat(3,1fr)"]{{grid-template-columns:repeat(2,1fr)!important}}}}@media(max-width:600px){{.section-white [style*="repeat(3,1fr)"]{{grid-template-columns:1fr!important}}}}</style>
        </section>"""

    html = head("Biagio · Your Italian AI Tutor · Club Italia",
                "Biagio is Club Italia's AI Italian tutor. Trained on the same syllabus your teacher uses. Available at every hour of every day. Included in every enrollment.",
                depth=0) + "\n" + NAV + "\n"
    html += hero() + "\n"
    html += social_proof_strip() + "\n"
    html += chat_fold() + "\n"
    html += capabilities() + "\n"
    html += in_the_wild() + "\n"
    html += life_grid_fold(A_, bg="cream") + "\n"
    html += trustpilot_wall(A_) + "\n"
    html += cta_final(bg="green",
                      headline_html='Meet Biagio. <span class="accent-ital" style="font-style:italic;color:#E6C99B">And meet the teacher who sent him.</span>',
                      sub="Enrol in any Club Italia course and Biagio is yours. Twenty minutes with an academic advisor and you're in.")
    html += FOOT
    (ROOT / "biagio.html").write_text(html)
    return len(html)

# ====================================================================
# HOW-IT-WORKS PAGE
# ====================================================================
def build_how_it_works():
    def step(num, title, desc, img, alt, bg="green"):
        color = "#FBFAF6" if bg in ("green", "red", "black") else "#0e1a14"
        body_c = "rgba(251,250,246,.78)" if bg in ("green", "red", "black") else "#3a3f3a"
        num_c = "#E6C99B" if bg in ("green", "red", "black") else "#166A47"
        return f"""<div style="display:grid;grid-template-columns:1.1fr 1fr;gap:clamp(2rem,4vw,4rem);align-items:center;padding:clamp(2rem,4vw,3.5rem) 0;border-bottom:1px solid {('rgba(255,255,255,.08)' if bg in ('green','red','black') else 'rgba(0,0,0,.08)')}">
          <div>
            <div style="font-family:'Playfair Display',serif;font-style:italic;font-weight:400;font-size:clamp(4rem,7vw,6rem);color:{num_c};line-height:1;margin-bottom:1rem">{num}</div>
            <h3 style="font-family:'Playfair Display',serif;font-weight:600;font-size:clamp(2rem,3.6vw,3rem);line-height:1.1;color:{color};margin:0 0 1.1rem">{title}</h3>
            <p style="font-size:1.1rem;line-height:1.65;color:{body_c};max-width:52ch;margin:0">{desc}</p>
          </div>
          <div style="aspect-ratio:4/3;overflow:hidden;box-shadow:0 30px 80px -20px rgba(0,0,0,.5)">
            <img src="{A_}img/{img}" alt="{alt}" style="width:100%;height:100%;object-fit:cover">
          </div>
        </div>"""

    steps = [
        ("I.", "Assess and enroll", "A 20-minute placement call with an academic advisor puts you in the right room from day one. No aptitude test, no gimmicks.", "life-caffe-roma.jpg", "A Roman café"),
        ("II.", "Join the platform", "Your course page opens the day you enroll: schedule, materials, replay library, and the Zoom link that will bring your classroom to your kitchen table.", "zoom-classroom-chiara.jpg", "Chiara's Zoom room"),
        ("III.", "Live classes, every week", "Eighty-five minutes with a native teacher, ten to twelve classmates, and enough coffee. Cameras on. This is where your Italian is made.", "env-marco-desk.jpg", "Marco's studio in Trastevere"),
        ("IV.", "Practice with Biagio", "Between classes, Biagio, our conversational Italian tutor, keeps your ear warm. Ask him for a phrase, a correction, or a story about Trieste at 2am.", "env-chiara-desk.jpg", "Chiara's warm desk"),
        ("V.", "Get certified, travel there", "Complete the track and receive a printed, CEFR-aligned certificate. Then plan your first week in Italia and speak the language the country was written in.", "life-scala-milano.jpg", "La Scala di Milano"),
    ]
    steps_html = "".join(step(*s) for s in steps)

    html = head("How Club Italia works — the five steps from your first hello to your first conversation in Rome",
                "Five simple steps: placement call, platform, live classes, Biagio, certification. The full journey of a Club Italia student.",
                depth=0) + "\n" + NAV + "\n"
    html += hero_cinematic(A_, "firenze-arno.mp4", "hero-italian-life.jpg",
                            "How it works",
                            'The five steps <span class="accent-ital" style="font-style:italic;color:#E6C99B">from your first hello,</span> to your first conversation in Rome.',
                            "No apps to configure, no aptitude tests to pass. A 20-minute call with an advisor puts you in the right room. Ten to twelve classmates and a native teacher take you from there.",
                            cta_ghost=("View the courses", "courses.html"),
                            right_img="zoom-two-phones.jpg",
                            right_caption="Your course page and your live class, both at your fingertips") + "\n"
    html += social_proof_strip() + "\n"
    html += f"""<section class="section-green" style="padding:clamp(5rem,9vw,8rem) 0">
      <div class="wrap">
        <div style="max-width:820px;margin-bottom:3rem">
          <div class="eyebrow" style="color:#E6C99B;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">The five steps</div>
          <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.8rem,5.6vw,5rem);line-height:1.04;color:#FBFAF6;margin:0">The journey, <span class="accent-ital" style="font-style:italic;color:#E6C99B">step by step.</span></h2>
        </div>
        {steps_html}
      </div>
    </section>"""
    html += zoom_class_fold(A_, bg="cream") + "\n"
    html += life_grid_fold(A_, bg="cream") + "\n"
    html += trustpilot_wall(A_) + "\n"
    html += cta_final(bg="green",
                      headline_html='Step one is <span class="accent-ital" style="font-style:italic;color:#E6C99B">twenty minutes.</span>',
                      sub="Reserve a placement call with an academic advisor and take the first step this week.")
    html += FOOT
    (ROOT / "how-it-works.html").write_text(html)
    return len(html)

# ====================================================================
# PRICING PAGE
# ====================================================================
def build_pricing():
    def price_card_full(kicker, price, per, title, blurb, feats, featured=False):
        border = "2px solid #166A47" if featured else "1px solid rgba(0,0,0,.1)"
        badge = '<div style="position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:#166A47;color:#fff;padding:.4rem 1rem;font-size:.68rem;letter-spacing:.22em;text-transform:uppercase;font-weight:600;white-space:nowrap">Best Value · Save $440</div>' if featured else ""
        feats_html = "".join(f'<li style="padding:.7rem 0;border-bottom:1px solid rgba(0,0,0,.06);color:#3a3f3a;font-size:.98rem;display:flex;gap:.7rem"><span style="color:#166A47">✓</span><span>{f}</span></li>' for f in feats)
        return f"""<div style="position:relative;background:#fff;border:{border};padding:2.6rem 2rem;display:flex;flex-direction:column;gap:1.2rem">
        {badge}
        <div style="font-size:.7rem;letter-spacing:.26em;text-transform:uppercase;color:#166A47;font-weight:600">{kicker}</div>
        <h3 style="font-family:'Playfair Display',serif;font-size:2rem;margin:0;color:#0e1a14;line-height:1.15">{title}</h3>
        <div style="font-family:'Playfair Display',serif;font-size:3.8rem;color:#0e1a14;line-height:1">{price}<span style="font-size:1rem;color:#6b7168;font-style:italic;margin-left:.4rem">{per}</span></div>
        <p style="font-size:.95rem;color:#3a3f3a;margin:0;line-height:1.55">{blurb}</p>
        <ul style="list-style:none;padding:0;margin:.6rem 0 0">{feats_html}</ul>
        <button class="btn btn-3d btn-3d-primary" data-advisor type="button" style="margin-top:auto">Reserve My Placement Call</button>
      </div>"""

    pricing_grid = f"""<section class="section-white" style="padding:clamp(5rem,9vw,8rem) 0">
      <div class="wrap" style="text-align:center;margin-bottom:3rem">
        <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">Three ways to enrol</div>
        <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.6rem,5.4vw,4.4rem);line-height:1.05;color:#0e1a14;margin:0 auto;max-width:22ch">Fair pricing, <span class="accent-ital" style="font-style:italic;color:#166A47">quiet commitment.</span></h2>
      </div>
      <div class="wrap" style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem;align-items:stretch">
        {price_card_full("Monthly Rolling", "$84", "/wk", "Monthly", "Cancel any month, keep the recordings for the life of your account.",
          ["One live class per week", "10–12 classmates, native teacher", "Lifetime replays of your classes", "Biagio AI tutor 24/7", "Cancel any month"])}
        {price_card_full("Annual · 12 months", "$62", "/wk", "Club Italia Annual", "The full year: two CEFR levels, priority scheduling, all Capsule Culturali included.",
          ["Everything in Monthly, plus:", "Save $440 across the year", "Priority scheduling", "All Capsule Culturali included", "Printed CEFR certificate on graduation"], featured=True)}
        {price_card_full("Single Term · 4 months", "$73", "/wk", "Term", "One CEFR level, cover to cover, then decide whether to continue.",
          ["1 CEFR level, cover to cover", "Group placement guaranteed", "Lifetime replays", "Biagio AI tutor 24/7", "Renew or upgrade any time"])}
      </div>
      <style>@media(max-width:960px){{.section-white [style*="repeat(3,1fr)"]{{grid-template-columns:1fr!important}}}}</style>
    </section>"""

    guarantee = f"""<section class="section-cream" style="padding:clamp(4.5rem,9vw,8rem) 0">
      <div class="wrap-narrow" style="text-align:center">
        <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">Our guarantee</div>
        <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.4rem,5vw,4rem);line-height:1.05;color:#0e1a14;margin:0 0 1.6rem">Seven days, <span class="accent-ital" style="font-style:italic;color:#166A47">any reason.</span></h2>
        <p style="font-size:1.2rem;line-height:1.65;color:#3a3f3a;max-width:56ch;margin:0 auto 1.6rem">Sit through your first two live classes, meet your teacher, meet your classmates. If Club Italia is not for you, request a full refund within seven days. No forms, no negotiations.</p>
        <p style="font-size:1rem;color:#6b7168;max-width:56ch;margin:0 auto">Monthly plans may cancel any month. Annual and term plans transfer credit toward any future Club Italia course.</p>
      </div>
    </section>"""

    included = f"""<section class="section-tint" style="padding:clamp(4.5rem,9vw,8rem) 0;background:#F4EFE5">
      <div class="wrap">
        <div style="max-width:820px;margin-bottom:2.6rem">
          <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">What is included</div>
          <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.2rem,4.6vw,3.6rem);line-height:1.05;color:#0e1a14;margin:0">Everything is included. <span class="accent-ital" style="font-style:italic;color:#166A47">Really.</span></h2>
        </div>
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1.4rem">
          {"".join(f'<div style="background:#fff;padding:1.6rem 1.4rem;border:1px solid rgba(0,0,0,.08)"><h3 style="font-family:\'Playfair Display\',serif;font-size:1.2rem;color:#0e1a14;margin:0 0 .6rem">{t}</h3><p style="font-size:.92rem;color:#3a3f3a;line-height:1.5;margin:0">{d}</p></div>' for t, d in [("Live classes", "Weekly Zoom sessions with your native teacher and 10–12 classmates."), ("Lifetime replays", "Every class recorded, every recording yours for the life of your account."), ("Course platform", "Your dedicated course page, materials, homework, transcripts and syllabus."), ("Biagio AI tutor", "24/7 Italian tutor trained on your exact syllabus."), ("Placement and support", "20-minute placement call, academic advisor, live student services."), ("Capsule Culturali", "Six-week culture courses in food, art and opera — Annual only."), ("CEFR certificate", "Printed, signed Club Italia certificate on completion."), ("Community events", "Optional live virtual events with Italian guests each term.")])}
        </div>
      </div>
      <style>@media(max-width:960px){{[style*="repeat(4,1fr)"]{{grid-template-columns:repeat(2,1fr)!important}}}}@media(max-width:600px){{[style*="repeat(4,1fr)"]{{grid-template-columns:1fr!important}}}}</style>
    </section>"""

    faqs = [
        ("Can I pay in instalments?", "Yes. Annual enrollments may be paid in three equal instalments at zero interest. Term and monthly plans are billed on the same day each month."),
        ("Do prices include the CEFR certificate?", "Yes. The printed, signed Club Italia certificate is included at no additional cost on completion of any CEFR track."),
        ("Are gift enrollments available?", "Yes. Ask an advisor about gift arrangements; we send a physical enrollment card to your recipient."),
        ("Will the price go up?", "The price you enrol at is the price you renew at, for as long as your subscription is continuous."),
        ("Can my employer pay?", "Yes. We accept purchase orders and invoicing for employer-funded enrollment. Ask an advisor for the enterprise packet."),
    ]
    faq_html = "".join(f"""<details style="border-bottom:1px solid rgba(0,0,0,.1);padding:1.4rem 0;cursor:pointer">
      <summary style="display:flex;justify-content:space-between;gap:1.4rem;font-family:'Playfair Display',serif;font-size:1.2rem;color:#0e1a14;list-style:none;cursor:pointer"><span>{q}</span><span style="color:#E6C99B;font-size:1.5rem" class="faq-plus">+</span></summary>
      <div style="padding-top:1rem;font-size:1rem;line-height:1.6;color:#3a3f3a">{a}</div>
    </details>""" for q, a in faqs)
    pricing_faq = f"""<section class="section-cream" style="padding:clamp(4.5rem,9vw,8rem) 0">
      <div class="wrap-narrow">
        <div style="text-align:center;margin-bottom:2.4rem">
          <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2rem,4.4vw,3.4rem);line-height:1.05;color:#0e1a14;margin:0">On price, briefly.</h2>
        </div>
        {faq_html}
      </div>
    </section>"""

    html = head("Pricing · Club Italia",
                "Three ways to enrol: Monthly $84/wk, Annual $62/wk (save $440), Term $73/wk. All plans include live classes, Biagio AI tutor, lifetime replays, and a printed CEFR certificate.",
                depth=0) + "\n" + NAV + "\n"
    html += hero_cinematic(A_, "roma-piazza.mp4", "hero-italian-life.jpg",
                            "Pricing",
                            'Fair pricing, <span class="accent-ital" style="font-style:italic;color:#E6C99B">quiet commitment.</span>',
                            "No hidden fees, no surprise renewals. Three ways to enrol, all inclusive of Biagio, all backed by a seven-day full-refund guarantee.",
                            cta_ghost=("Read the guarantee", "#guarantee"),
                            right_img="zoom-hero-composite.jpg",
                            right_caption="Everything included · every plan") + "\n"
    html += social_proof_strip() + "\n"
    html += pricing_grid + "\n"
    html = html.replace('<section class="section-cream" style="padding:clamp(4.5rem,9vw,8rem) 0">\n      <div class="wrap-narrow" style="text-align:center">\n        <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">Our guarantee</div>',
                        '<section id="guarantee" class="section-cream" style="padding:clamp(4.5rem,9vw,8rem) 0">\n      <div class="wrap-narrow" style="text-align:center">\n        <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">Our guarantee</div>', 1)
    html += guarantee + "\n"
    html += included + "\n"
    html += trustpilot_wall(A_) + "\n"
    html += pricing_faq + "\n"
    html += cta_final(bg="green",
                      headline_html='Enrol at the price that <span class="accent-ital" style="font-style:italic;color:#E6C99B">fits your year.</span>',
                      sub="A 20-minute placement call with an academic advisor is the entire cost of finding out.")
    html += FOOT
    (ROOT / "pricing.html").write_text(html)
    return len(html)

# ====================================================================
# CULTURE PAGE (luxury maison brand-film mood — FA culture.html)
# ====================================================================
def build_culture():
    def pillar(img, kicker, headline, body):
        return f"""<div style="position:relative;aspect-ratio:5/6;overflow:hidden;background:#000">
          <img src="{A_}img/{img}" alt="{kicker}" style="width:100%;height:100%;object-fit:cover;opacity:.78">
          <div style="position:absolute;inset:0;background:linear-gradient(180deg, rgba(0,0,0,.15) 30%, rgba(4,15,10,.92));display:flex;flex-direction:column;justify-content:flex-end;padding:2rem;color:#FBFAF6">
            <div style="font-size:.7rem;letter-spacing:.24em;text-transform:uppercase;color:#E6C99B;margin-bottom:.6rem">{kicker}</div>
            <h3 style="font-family:'Playfair Display',serif;font-weight:600;font-size:clamp(1.8rem,2.6vw,2.4rem);line-height:1.12;margin:0 0 .7rem">{headline}</h3>
            <p style="font-size:.98rem;line-height:1.55;color:rgba(251,250,246,.86);margin:0;max-width:38ch">{body}</p>
          </div>
        </div>"""

    html = head("Culture · Club Italia",
                "Not a language. A way of living. Italian food, art, cinema, opera, tradition and travel, all taught in Italian, live from Italy.",
                depth=0) + "\n" + NAV + "\n"
    html += hero_cinematic(A_, "opera-scala.mp4", "hero-cucina-italiana.jpg",
                            "The Club Italia culture",
                            'Not a language. <span class="accent-ital" style="font-style:italic;color:#E6C99B">A way of living.</span>',
                            "Italy is not a country you can order in translation. Its food, its art, its opera, its arguments about politics all live inside Italian. Club Italia is not a language school with culture on the side; it is a cultural school that happens to teach language.",
                            cta_ghost=("See the capsule courses", "capsules.html"),
                            right_img="life-scala-milano.jpg",
                            right_caption="La Scala di Milano, an evening in November") + "\n"
    html += social_proof_strip() + "\n"

    html += f"""<section class="section-tint" style="padding:clamp(5rem,9vw,8rem) 0;background:#F4EFE5">
      <div class="wrap" style="text-align:center;margin-bottom:3rem">
        <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">The six pillars</div>
        <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.6rem,5.4vw,4.6rem);line-height:1.05;color:#0e1a14;margin:0 auto;max-width:22ch">Six pillars of Italian culture, <span class="accent-ital" style="font-style:italic;color:#166A47">taught in Italian.</span></h2>
      </div>
      <div class="wrap-flush" style="padding:0 clamp(1rem,2vw,2rem);display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:#0e1a14">
        {pillar("pillar-food.jpg", "La Cucina", "Food, regionally", "Every region of Italy is a menu. Six weeks with Giulia Ferrari in Bologna, at her kitchen table.")}
        {pillar("pillar-art.jpg", "L'Arte", "Art, closely", "The Renaissance was written in Italian and can only be read there. Six weeks with Chiara Bianchi at the Uffizi.")}
        {pillar("pillar-opera.jpg", "L'Opera", "Opera, sung", "The libretto is the language of the aria. Six weeks with Alessandro Conti from La Scala.")}
        {pillar("pillar-cinema.jpg", "Il Cinema", "Cinema, discussed", "Fellini and Sorrentino argue in Italian. Every level includes a weekly cinema fragment.")}
        {pillar("pillar-travel.jpg", "Il Viaggio", "Travel, prepared", "Every syllabus is scored to a city. Your first week in Italy is included in the plan.")}
        {pillar("pillar-tradition.jpg", "La Tradizione", "Tradition, lived", "Sagre, feste, the Sunday lunch — the calendar of Italian life is a curriculum in itself.")}
      </div>
      <style>@media(max-width:960px){{[style*="repeat(3,1fr)"][style*="0e1a14"]{{grid-template-columns:repeat(2,1fr)!important}}}}@media(max-width:600px){{[style*="repeat(3,1fr)"][style*="0e1a14"]{{grid-template-columns:1fr!important}}}}</style>
    </section>"""

    html += two_col_photo_text(A_, "life-caffe-roma.jpg", "A café in Roma", "left",
        "The morning ritual",
        'Culture starts <span class="accent-ital" style="font-style:italic;color:#166A47">at the bar.</span>',
        "<p>Every Italian day begins the same way, in every one of Italy's twenty regions: at a bar, at the counter, with a coffee, with a word. Club Italia scores that ritual — its language, its manners, its unwritten sequence — into the first ten lessons of every course.</p><p>You will not just know how to order a cappuccino. You will know why an Italian never orders one after 11am.</p>", bg="cream")

    html += zoom_class_fold(A_, img="zoom-classroom-chiara.jpg",
        caption="Chiara Bianchi, live from Firenze · a room reading a Botticelli caption aloud",
        bg="cream")

    html += two_col_photo_text(A_, "life-uffizi-hall.jpg", "A hall in the Uffizi", "right",
        "The Uffizi in Italian",
        'A canvas <span class="accent-ital" style="font-style:italic;color:#166A47">is a page.</span>',
        "<p>The Florentine Renaissance was written in Italian and can only be read there. Chiara Bianchi teaches L'Arte del Rinascimento — a six-week capsule course that turns six of the Uffizi's paintings into six Italian evenings.</p><p>You leave able to describe a canvas in Italian technical vocabulary, and to guide a visiting friend through an Uffizi room in the language it was painted in.</p>", bg="cream")

    html += life_grid_fold(A_, bg="tint") + "\n"

    html += two_col_photo_text(A_, "life-scala-milano.jpg", "La Scala di Milano", "left",
        "The opera, closely",
        'A libretto is <span class="accent-ital" style="font-style:italic;color:#166A47">a poem, sung.</span>',
        "<p>Alessandro Conti's L'Opera in Italiano reads Verdi, Puccini, Rossini and Donizetti as literature. Six weeks in which the great arias are handed back to you as Italian, with the register they were written in and the meaning they were sung for.</p><p>You attend the next Scala broadcast with the libretto in your hand and follow it.</p>", bg="cream")

    html += trustpilot_wall(A_)
    html += cta_final(bg="green",
                      headline_html='Culture speaks Italian. <span class="accent-ital" style="font-style:italic;color:#E6C99B">What about you?</span>',
                      sub="Twenty minutes with an academic advisor. No aptitude test, no pressure. Just a plan for the year of Italian ahead of you.")
    html += FOOT
    (ROOT / "culture.html").write_text(html)
    return len(html)

# ====================================================================
# METHOD PAGE
# ====================================================================
def build_method():
    def principle(num, img, title, headline, body):
        return f"""<section class="section-cream" style="padding:clamp(5rem,9vw,8rem) 0;border-bottom:1px solid rgba(0,0,0,.06)">
          <div class="wrap" style="display:grid;grid-template-columns:1fr 1fr;gap:clamp(2.4rem,5vw,5rem);align-items:center">
            <figure style="margin:0">
              <div style="aspect-ratio:4/5;overflow:hidden;box-shadow:0 40px 100px -30px rgba(14,26,20,.35)">
                <img src="{A_}img/{img}" alt="{title}" style="width:100%;height:100%;object-fit:cover">
              </div>
            </figure>
            <div>
              <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:3.4rem;color:#E6C99B;line-height:1;margin-bottom:.7rem">{num}</div>
              <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1rem">{title}</div>
              <h3 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.2rem,4.6vw,3.6rem);line-height:1.05;color:#0e1a14;margin:0 0 1.4rem">{headline}</h3>
              <div style="font-size:1.12rem;line-height:1.65;color:#3a3f3a;max-width:48ch">{body}</div>
            </div>
          </div>
          <style>@media(max-width:820px){{[style*="1fr 1fr"]{{grid-template-columns:1fr!important}}}}</style>
        </section>"""

    html = head("The Club Italia method · four principles",
                "Cultural scenario, live interaction, guided structure, real task. The four principles behind every Club Italia lesson.",
                depth=0) + "\n" + NAV + "\n"
    html += hero_cinematic(A_, "cucina-pasta.mp4", "hero-teacher-live.jpg",
                            "The method",
                            'Four principles. <span class="accent-ital" style="font-style:italic;color:#E6C99B">One way of learning.</span>',
                            "Every Club Italia lesson is built on the same four principles: a real Italian scene, a live human class, a structured CEFR progression, and a real-world task you leave the room with.",
                            cta_ghost=("See a real class", "sample-class.html"),
                            right_img="env-marco-desk.jpg",
                            right_caption="Marco's studio in Trastevere · the morning of class") + "\n"
    html += social_proof_strip() + "\n"
    html += principle("I.", "pillar-art.jpg", "Cultural scenario", 'Every lesson lives inside <span class="accent-ital" style="font-style:italic;color:#166A47">an Italian scene.</span>',
        "<p>An espresso in Trastevere. A Sunday at the market in Bologna. A matinee at La Scala. Every lesson opens with a real Italian moment your teacher was in, this week — with the vocabulary, the register, and the small unwritten rules the moment required.</p><p>Language separated from culture is a translation. Language inside culture is a life.</p>")
    html += principle("II.", "pillar-food.jpg", "Live interaction", 'Ten to twelve classmates, <span class="accent-ital" style="font-style:italic;color:#166A47">cameras on.</span>',
        "<p>You speak. You are answered. This is where Italian stops being an app and starts being a language. Ten to twelve classmates is the right number: enough voices to make a room, small enough that your teacher knows your name.</p><p>Every Club Italia session is one hour and twenty-five minutes on Zoom, with a native teacher who lives in Italy, and no recording of you unless you want one.</p>")
    html += principle("III.", "pillar-travel.jpg", "Guided structure", 'CEFR-aligned, chapter by chapter, <span class="accent-ital" style="font-style:italic;color:#166A47">to your certificate.</span>',
        "<p>Every course is scored to the Common European Framework, A0 to A2.2 and beyond. Every session is a chapter. Every chapter a competence. Every competence written down and assessed.</p><p>You will not wander. You will progress.</p>")
    html += principle("IV.", "pillar-cinema.jpg", "Real task", 'You leave every class <span class="accent-ital" style="font-style:italic;color:#166A47">with a task.</span>',
        "<p>Order the coffee. Book the room. Tell the story. Every session ends with a small, verifiable, Italian-life task; every next session opens by discussing how it went.</p><p>Homework in a Club Italia course is not drill. It is rehearsal for the real thing.</p>")
    html += zoom_class_fold(A_, bg="tint") + "\n"
    html += life_grid_fold(A_, bg="cream") + "\n"
    html += trustpilot_wall(A_) + "\n"
    html += cta_final(bg="green",
                      headline_html='See the method <span class="accent-ital" style="font-style:italic;color:#E6C99B">in a real class.</span>',
                      sub="Sit in on a live session before you enrol — with your camera off if you like.")
    html += FOOT
    (ROOT / "method.html").write_text(html)
    return len(html)

# ====================================================================
# COURSES INDEX PAGE
# ====================================================================
def build_courses_index():
    # Reuse the course-grid pattern from homepage, but bigger
    def course_card(img, badge, title, sub, meta, price, href):
        return f"""<a href="{href}" class="course-card" style="text-decoration:none;color:inherit;display:flex;flex-direction:column;background:#fff;border-right:1px solid rgba(0,0,0,.07);border-bottom:1px solid rgba(0,0,0,.07);transition:transform .35s ease, box-shadow .35s ease">
    <div style="position:relative;aspect-ratio:5/4;overflow:hidden">
      <img src="{A_}img/{img}" alt="{title}" style="width:100%;height:100%;object-fit:cover;transition:transform .8s ease">
      <div style="position:absolute;top:1rem;left:1rem;background:rgba(4,15,10,.72);color:#E6C99B;padding:.4rem .8rem;font-size:.62rem;letter-spacing:.22em;text-transform:uppercase;backdrop-filter:blur(6px)">{badge}</div>
      <div style="position:absolute;top:1rem;right:1rem;background:#166A47;color:#fff;padding:.5rem .8rem;font-family:'Playfair Display',serif;font-size:1.05rem">{price}</div>
    </div>
    <div style="padding:1.6rem 1.6rem 1.8rem;display:flex;flex-direction:column;gap:.7rem;flex:1;background:#fff">
      <h3 style="font-family:'Playfair Display',serif;font-size:1.6rem;line-height:1.15;margin:0;color:#0e1a14">{title}</h3>
      <div style="font-family:'Playfair Display',serif;font-style:italic;color:#166A47;font-size:1rem">{sub}</div>
      <div style="font-size:.82rem;color:#6b7168;letter-spacing:.04em;margin-top:auto">{meta}</div>
      <div style="display:inline-flex;align-items:center;gap:.5rem;color:#166A47;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;font-weight:600;margin-top:.4rem">Enroll →</div>
    </div>
  </a>"""

    def track_header(kicker, title, blurb):
        return f"""<div style="grid-column:1/-1;padding:2.6rem 1.6rem 1.6rem;border-bottom:1px solid rgba(0,0,0,.1);background:#F7F3EA">
      <div style="display:flex;align-items:baseline;gap:1.4rem;flex-wrap:wrap;margin-bottom:.5rem">
        <div style="font-size:.7rem;letter-spacing:.28em;text-transform:uppercase;color:#166A47;font-weight:600">{kicker}</div>
        <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:1.5rem;color:#0e1a14">{title}</div>
      </div>
      <p style="color:#3a3f3a;font-size:1.02rem;line-height:1.55;max-width:64ch;margin:0">{blurb}</p>
    </div>"""

    cards = (
        track_header("Club Italia · Il Corso", "The CEFR-structured year, A0 to A2.2",
                     "Four levels, each forty live lessons, 85 minutes each, in groups of 10 to 12. The complete Italian journey from zero to conversational fluency, taught by native teachers in four Italian cities.")
        + course_card("course-ci1.jpg", "A0 → A1.1", "CI Principiante", "Your first Italian", "40 lessons · 85 min · 10–12 seats", "$84/wk", "pages/courses/ci1.html")
        + course_card("course-ci2.jpg", "A1.1 → A1.2", "CI Elementare", "Speaking with intention", "40 lessons · 85 min · 10–12 seats", "$84/wk", "pages/courses/ci2.html")
        + course_card("course-ci3.jpg", "A1.2 → A2.1", "CI Intermedio", "Real conversations", "40 lessons · 85 min · 10–12 seats", "$84/wk", "pages/courses/ci3.html")
        + course_card("course-ci4.jpg", "A2.1 → A2.2", "CI Avanzato", "Cultural fluency", "40 lessons · 85 min · 10–12 seats", "$84/wk", "pages/courses/ci4.html")
        + track_header("Parliamo Italiano", "Spoken confidence, in twelve weeks",
                       "A shorter, spoken-only track for learners who need the mouth of Italian: rhythm, greetings, café, market, direction, opinion. Twelve one-hour sessions.")
        + course_card("spoken-ps1.jpg", "Foundation", "Parliamo · Foundation", "Sounds and greetings", "12 lessons · 60 min · 10–12 seats", "$62/wk", "pages/spoken/ps1.html")
        + course_card("spoken-ps2.jpg", "Beginner", "Parliamo · Beginner", "Ordering and asking", "12 lessons · 60 min · 10–12 seats", "$62/wk", "pages/spoken/ps2.html")
        + course_card("spoken-ps3.jpg", "Elementary", "Parliamo · Elementary", "Telling your day", "12 lessons · 60 min · 10–12 seats", "$62/wk", "pages/spoken/ps3.html")
        + course_card("spoken-ps4.jpg", "Confident", "Parliamo · Confident", "Holding your ground", "12 lessons · 60 min · 10–12 seats", "$62/wk", "pages/spoken/ps4.html")
        + track_header("Capsule Culturali", "Short courses. Great Italian passions.",
                       "Six-week culture capsules for intermediate learners. Italian food with Giulia in Bologna, Italian art with Chiara at the Uffizi, Italian opera with Alessandro from La Scala.")
        + course_card("cap-food.jpg", "6 weeks", "La Cucina Italiana", "Regions on a plate", "6 lessons · 75 min · 10–12 seats", "$220", "pages/culture/cap-food.html")
        + course_card("cap-art.jpg", "6 weeks", "L'Arte del Rinascimento", "Reading a Renaissance canvas", "6 lessons · 75 min · 10–12 seats", "$220", "pages/culture/cap-art.html")
        + course_card("cap-opera.jpg", "6 weeks", "L'Opera in Italiano", "From La Scala with a libretto", "6 lessons · 75 min · 10–12 seats", "$220", "pages/culture/cap-opera.html")
    )

    html = head("Courses · Club Italia",
                "Eleven courses across three tracks. CEFR-structured Il Corso, spoken Parliamo Italiano, and cultural Capsule courses. Every course live from Italy with a native teacher.",
                depth=0) + "\n" + NAV + "\n"
    html += hero_cinematic(A_, "roma-piazza.mp4", "hero-italian-life.jpg",
                            "The courses",
                            'Eleven courses. Three tracks. <span class="accent-ital" style="font-style:italic;color:#E6C99B">One school.</span>',
                            "Choose the CEFR journey, the spoken track, or a six-week culture capsule. Every Club Italia course is live from Italy, small-group, and CEFR-aligned.",
                            cta_ghost=("Take the placement", "how-it-works.html"),
                            right_img="zoom-classroom-marco.jpg",
                            right_caption="A live class · this morning") + "\n"
    html += social_proof_strip() + "\n"
    html += f"""<section class="section-white" style="padding:clamp(4rem,8vw,7rem) 0 0">
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:1px solid rgba(0,0,0,.1);border-left:1px solid rgba(0,0,0,.07)">
        {cards}
      </div>
      <style>@media(max-width:960px){{.section-white [style*="repeat(4,1fr)"]{{grid-template-columns:repeat(2,1fr)!important}}}}@media(max-width:560px){{.section-white [style*="repeat(4,1fr)"]{{grid-template-columns:1fr!important}}}}
        .course-card:hover{{transform:translateY(-3px);box-shadow:0 20px 50px -20px rgba(14,26,20,.2);z-index:2;position:relative}}
        .course-card:hover img{{transform:scale(1.05)}}</style>
    </section>"""
    html += trustpilot_wall(A_) + "\n"
    html += cta_final(bg="green",
                      headline_html='Not sure which course? <span class="accent-ital" style="font-style:italic;color:#E6C99B">That is what the call is for.</span>',
                      sub="Twenty minutes with an academic advisor. No aptitude test, no pressure. Just a plan for the year of Italian ahead of you.")
    html += FOOT
    (ROOT / "courses.html").write_text(html)
    return len(html)

# ====================================================================
# FAQ PAGE
# ====================================================================
def build_faq():
    sections = [
        ("The essentials", [
            ("How is Club Italia different from Duolingo, Babbel or a private tutor?",
             "Club Italia is a school, not an app. You are placed by an advisor into a live weekly classroom of ten to twelve adult learners taught by a native, university-credentialed Italian teacher on the ground in Italy. Every course is CEFR-aligned, every graduation is certified, and every student is known by name. A private tutor is one voice with no peer conversation; an app is no voice with no classroom. Club Italia is both a room and a syllabus."),
            ("Who teaches, and where are they?",
             "Seven Italian teachers, each based in an Italian city: Chiara in Firenze, Marco in Roma, Giulia in Bologna, Alessandro in Milano, Francesca in Napoli, Luca in Venezia, and Sofia in Palermo. All hold university degrees in Italian pedagogy or literature. All are native speakers with a minimum of six years of adult-education experience."),
            ("What technology do I need?",
             "A laptop or tablet with a camera, a stable internet connection, and a quiet room. If you can join a video call, you can attend Club Italia."),
        ]),
        ("Placement and enrolment", [
            ("How does the placement call work?",
             "You book a 20-minute video call with an academic advisor. We ask about your goals, your exposure to Italian, and your schedule, then place you in the correct level. No test, no fee, no obligation. Most learners are enrolled by the end of the call, but you may take a week to decide."),
            ("Can I switch levels if my group is too easy or too hard?",
             "Yes. Within your first four weeks you may transfer between levels at no cost. After that we reassess only at the start of a new term, when transfers remain free."),
            ("Do I have to commit to a full year?",
             "No. We offer monthly, term (4 months), and annual plans. Monthly may be cancelled any month; the annual plan simply saves you $440 across the year."),
        ]),
        ("Attendance and progress", [
            ("What happens if I miss a class?",
             "Every session is recorded and uploaded to your course page within 24 hours. You retain access to your recordings for the life of your enrollment. Miss more than two consecutive sessions and your teacher will reach out personally to help you catch up."),
            ("What if I need to pause?",
             "Any student may pause enrollment for up to eight weeks per year with no fee. Longer pauses are handled case by case, always in your favour."),
            ("Is there homework?",
             "Yes, but it is designed as rehearsal, not drill. Each session ends with a small Italian-life task and a written or spoken assignment of 20 to 40 minutes."),
        ]),
        ("Certification", [
            ("Do I receive a certificate?",
             "Yes. On completion of every CEFR track you receive a printed Club Italia certificate stating your level, teacher, and cohort. It is not a state-issued diploma, but it is a formal document from a private language school and is recognized by employers as continuing education."),
            ("Can I sit an official CEFR exam through Club Italia?",
             "We do not administer official CEFR exams (only Italian state institutions can). We prepare you thoroughly and will refer you to the nearest official examination centre in your city or a partner centre online."),
        ]),
        ("Payment and refunds", [
            ("What is the refund policy?",
             "You have seven days from your first live class to request a full refund. No forms, no negotiations. Beyond seven days, monthly plans may cancel at any time; annual and term plans may transfer credit toward future courses."),
            ("How do I pay, and can I split the cost?",
             "We accept every major credit card, PayPal, and bank transfer. Annual enrollments may be paid in three equal instalments at no interest; term and monthly plans are billed on the same day each month."),
            ("Can my employer pay?",
             "Yes. We accept purchase orders and invoicing for employer-funded enrollment. Ask an advisor for the enterprise packet."),
        ]),
        ("For special cases", [
            ("Do you offer courses for children?",
             "Not at this time. Club Italia serves adult learners aged 18 and over, most of whom are between 30 and 70. Our sister brand at eTeacher Group offers Italian for younger learners; ask an advisor for a referral."),
            ("Can I take a class if I already speak Italian well?",
             "Yes. Our CI Avanzato track (A2.1 to A2.2) and Parliamo Confident are for learners who already speak Italian and want to reach cultural fluency. Beyond A2.2, we offer private tutoring on request."),
        ]),
    ]

    def section_block(kicker, items):
        item_html = "".join(f"""<details style="border-bottom:1px solid rgba(0,0,0,.1);padding:1.6rem 0;cursor:pointer">
          <summary style="display:flex;justify-content:space-between;align-items:flex-start;gap:2rem;font-family:'Playfair Display',serif;font-weight:500;font-size:1.35rem;line-height:1.35;color:#0e1a14;list-style:none;cursor:pointer"><span style="flex:1">{q}</span><span style="color:#E6C99B;font-family:'Playfair Display',serif;font-size:1.8rem;line-height:1" class="faq-plus">+</span></summary>
          <div style="padding-top:1.2rem;font-size:1.05rem;line-height:1.65;color:#3a3f3a;max-width:72ch">{a}</div>
        </details>""" for q, a in items)
        return f"""<div style="margin-bottom:3rem">
          <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">{kicker}</div>
          {item_html}
        </div>"""

    all_sections = "".join(section_block(k, its) for k, its in sections)

    html = head("Frequently asked questions · Club Italia",
                "Every important question about Club Italia: placement, teachers, technology, missed classes, certificates, refunds and more.",
                depth=0) + "\n" + NAV + "\n"
    html += hero_cinematic(A_, "bologna-portici.mp4", "hero-italian-life.jpg",
                            "Questions",
                            'Everything worth asking, <span class="accent-ital" style="font-style:italic;color:#E6C99B">before you enroll.</span>',
                            "Twenty-plus real questions from real learners, answered in academic register. If yours is not here, an advisor is a click away.",
                            cta_ghost=("Talk to an advisor", "#advisor"),
                            right_img="zoom-classroom-chiara.jpg",
                            right_caption="Chiara Bianchi · live from Firenze") + "\n"
    html += social_proof_strip() + "\n"
    html += f"""<section class="section-cream" style="padding:clamp(5rem,9vw,8rem) 0">
      <div class="wrap-narrow">{all_sections}</div>
    </section>"""
    html += zoom_class_fold(A_, bg="tint") + "\n"
    html += trustpilot_wall(A_) + "\n"
    html += cta_final(bg="green",
                      headline_html='Still have a question?<br><span class="accent-ital" style="font-style:italic;color:#E6C99B">Ask an advisor.</span>',
                      sub="Twenty minutes with an academic advisor answers what a FAQ cannot.")
    html += FOOT
    (ROOT / "faq.html").write_text(html)
    return len(html)

# ====================================================================
# SAMPLE-CLASS PAGE
# ====================================================================
def build_sample_class():
    html = head("Watch a real Club Italia class · sample class",
                "Sit in on a real Club Italia class, no enrollment required. Watch Marco Rinaldi teach live from Trastevere, with 11 adult learners in the room.",
                depth=0) + "\n" + NAV + "\n"
    html += hero_cinematic(A_, "class-demo.mp4", "hero-teacher-live.jpg",
                            "The sample class",
                            'Sit in on a real class. <span class="accent-ital" style="font-style:italic;color:#E6C99B">Cameras off, if you like.</span>',
                            "This is not a highlight reel or a marketing edit. It is the first twenty minutes of a real Club Italia class, unedited, recorded last Monday from Marco Rinaldi's studio in Trastevere.",
                            cta_ghost=("Reserve a seat instead", "#reserve"),
                            right_img="zoom-classroom-marco.jpg",
                            right_caption="A morning class · this Monday") + "\n"
    html += social_proof_strip() + "\n"
    html += f"""<section class="section-cream" style="padding:clamp(4.5rem,9vw,8rem) 0">
      <div class="wrap">
        <div style="text-align:center;margin-bottom:2.4rem">
          <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">The recording</div>
          <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.4rem,5vw,4rem);line-height:1.05;color:#0e1a14;margin:0 auto;max-width:24ch">Marco Rinaldi, <span class="accent-ital" style="font-style:italic;color:#166A47">live from Trastevere.</span></h2>
        </div>
        <div style="position:relative;aspect-ratio:16/9;overflow:hidden;box-shadow:0 40px 100px -30px rgba(14,26,20,.4)">
          <video controls preload="metadata" poster="{A_}img/zoom-classroom-marco.jpg" style="width:100%;height:100%;object-fit:cover;display:block">
            <source src="{A_}video/class-demo.mp4" type="video/mp4">
          </video>
        </div>
        <p style="font-family:'Playfair Display',serif;font-style:italic;color:#166A47;text-align:center;margin-top:1.4rem;font-size:1.1rem">Twenty unedited minutes · CI Principiante · Monday 7pm ET · 11 students present</p>
      </div>
    </section>"""
    html += two_col_photo_text(A_, "env-marco-desk.jpg", "Marco's studio in Trastevere", "left",
        "The teacher, up close",
        'Marco Rinaldi, <span class="accent-ital" style="font-style:italic;color:#166A47">up close.</span>',
        "<p>Marco is a Sapienza graduate, an adult-education specialist, and a Trastevere native. He has taught Italian to eleven cohorts of Club Italia students since 2021 and believes the first year of Italian is best learned inside a real Roman morning.</p><p>His CI Principiante class fills quickly. If you like the class you see here, an advisor can tell you when the next cohort begins.</p>", bg="cream")
    html += zoom_class_fold(A_, img="zoom-classroom-chiara.jpg",
                            caption="Chiara Bianchi teaches Elementare on Wednesdays — another sample available on request",
                            bg="tint")
    html += trustpilot_wall(A_) + "\n"
    html += cta_final(bg="green",
                      headline_html='Ready for <span class="accent-ital" style="font-style:italic;color:#E6C99B">your own seat?</span>',
                      sub="Twenty minutes with an academic advisor. No aptitude test, no pressure.")
    html += FOOT
    (ROOT / "sample-class.html").write_text(html)
    return len(html)

# ====================================================================
if __name__ == "__main__":
    for name, fn in [
        ("teachers", build_teachers),
        ("biagio", build_biagio),
        ("how-it-works", build_how_it_works),
        ("pricing", build_pricing),
        ("culture", build_culture),
        ("method", build_method),
        ("courses", build_courses_index),
        ("faq", build_faq),
        ("sample-class", build_sample_class),
    ]:
        size = fn()
        print(f"{name}.html · {size} bytes")
