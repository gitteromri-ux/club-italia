#!/usr/bin/env python3
"""Tier 2: about, eteacher, faq, sample-class, contact, blog, map, community, events, privacy, terms, capsules."""
import sys
sys.path.insert(0, "/home/user/workspace/club-italia")
from _ci_build import page, stats_strip, final_cta_verona, tp_wall, TEACHERS, ROOT

# ============================================================
# ABOUT.HTML — 10 folds
# ============================================================
def build_about():
    hero = """
<section class="section-ink hero-page hero-100">
  <div class="hero-bg">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/img/hero-italian-life.jpg">
      <source src="assets/video/roma-piazza.mp4" type="video/mp4">
    </video>
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">About Club Italia</span>
    <h1 class="serif-display hero-h1">An Italian school<br><em>for adults who mean it</em></h1>
    <p class="lead">Club Italia is a live, culturally immersive Italian language school run by eTeacher Group, a European online school operator that has taught adults for a quarter of a century.</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">Talk to an Advisor</button>
      <a class="btn btn-ghost btn-lg" href="method.html">Read the method</a>
    </div>
  </div>
</section>
"""
    fold2 = """
<section class="section-paper">
  <div class="wrap">
    <div class="section-head-split">
      <div>
        <span class="eyebrow">Origin</span>
        <h2 class="serif-display">Why we opened<br>an Italian faculty in 2022</h2>
      </div>
    </div>
    <div class="editorial-2col">
      <div class="col-essay">
        <p>Club Italia was opened in the autumn of 2022 as the sixth language faculty of eTeacher Group, a European online school operator founded in 2000. The first five faculties were Hebrew, Yiddish, Arabic, Spanish and French. Italian was the language we were most asked for in the years before we opened it, and the language that most obviously required a specifically cultural teaching approach.</p>
        <p>We did not want to add Italian and treat it as another product. We spent eighteen months hiring the founding faculty, one teacher at a time, from Firenze, Roma, Bologna, Milano and Venezia. We wrote the syllabus with them, not for them. We opened the first live cohort in November 2022 with twelve adult students.</p>
      </div>
      <div class="col-essay col-figure">
        <figure><img src="assets/img/env-chiara-desk.jpg" alt="Chiara Bellini at her teaching desk in Firenze" loading="lazy"></figure>
        <p class="figure-cap">The founding classroom in Firenze, from which Chiara Bellini taught the first Club Italia cohort in November 2022.</p>
      </div>
    </div>
  </div>
</section>
"""
    stats = [("16M","Americans of Italian descent, per US Census 2023"),("7.5M","US visitors to Italy each year, per ENIT 2024"),("Mar 2025","the reformed Italian citizenship law")]
    sgrid = "".join(f'<article class="stat-card"><div class="stat-num serif-display">{n}</div><p>{d}</p></article>' for n,d in stats)
    fold3 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Why Italian, why now</span>
      <h2 class="serif-display">The demand behind the school</h2>
    </div>
    <div class="stat-cards">{sgrid}
    </div>
  </div>
</section>
"""
    beliefs = [("01","Culture is the syllabus","Grammar is scaffolding. Culture is the room. We built the whole curriculum out of Italian cultural life, not the other way around."),
               ("02","Live cannot be faked","No recorded lecture is a class. A class is a room in which a native teacher is with you, in real time. We have never sold anything else."),
               ("03","Small groups, or nothing","Twelve adults per cohort, maximum. Small enough to be a room. Not a broadcast, not a webinar, not a market."),]
    bgrid = "".join(f'<article class="belief-card"><div class="belief-num">{n}</div><h3 class="serif-display">{h}</h3><p>{p}</p></article>' for n,h,p in beliefs)
    fold4 = f"""
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Three beliefs</span>
      <h2 class="serif-display">What Club Italia commits to</h2>
    </div>
    <div class="belief-grid">{bgrid}
    </div>
  </div>
</section>
"""
    fold5 = """
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The method</span>
      <h2 class="serif-display">Live, small, native, cultural</h2>
      <p class="lead">Four words. Live weekly classes with a native teacher. Small groups of ten to twelve. A syllabus built around six cultural chapters. That is the method. Everything else is derivative.</p>
    </div>
    <div class="center">
      <a class="btn btn-primary btn-lg" href="method.html">Read the full method</a>
    </div>
  </div>
</section>
"""
    fold6 = """
<section class="section-ink">
  <div class="wrap">
    <div class="section-head section-head-light">
      <span class="eyebrow eyebrow-gold">The technology</span>
      <h2 class="serif-display">A real classroom, on Zoom</h2>
    </div>
    <div class="zoom-frame">
      <img src="assets/img/zoom-hero-composite.jpg" alt="Composite of a Club Italia Zoom classroom, with the teacher live from Italy and students on screen" loading="lazy">
    </div>
    <p class="figure-cap">The Club Italia Zoom classroom, with the teacher live from Italy and ten to twelve adults on screen.</p>
  </div>
</section>
"""
    fold7 = """
<section class="section-cream">
  <div class="wrap">
    <div class="section-head-split">
      <div>
        <span class="eyebrow">The faculty</span>
        <h2 class="serif-display">Seven native teachers,<br>from seven Italian cities</h2>
      </div>
    </div>
    <div class="editorial-2col">
      <div class="col-essay">
        <p>Every teacher at Club Italia is Italian, lives in Italy, and teaches from an Italian city. The faculty is small on purpose. Seven teachers is enough to give every course two cohorts a term, and small enough that a student who studies with us for a year knows the faculty by name.</p>
      </div>
      <div class="col-essay">
        <a class="btn btn-primary btn-lg" href="teachers.html">Meet the seven teachers</a>
      </div>
    </div>
  </div>
</section>
"""
    fold8 = """
<section class="section-verona">
  <div class="wrap center">
    <div class="pullquote-band pullquote-band-lg">
      <blockquote class="serif-display quote-xl"><em>A room of ten adults with one teacher who has been in Italy this morning<br>is worth every promise of a five minute daily habit.</em></blockquote>
      <div class="quote-attr quote-attr-light">Head of School · Club Italia</div>
    </div>
  </div>
</section>
"""
    metrics = [("25+","years online teaching"),("400k","adult learners since 2000"),("197","countries served"),("6","language faculties")]
    mg = "".join(f'<div class="metric-cell"><div class="metric-num serif-display">{n}</div><div class="metric-lbl">{d}</div></div>' for n,d in metrics)
    fold9 = f"""
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">eTeacher Group, in numbers</span>
      <h2 class="serif-display">The school behind Club Italia</h2>
    </div>
    <div class="metric-grid">{mg}
    </div>
    <div class="center" style="margin-top:2.4rem">
      <a class="btn btn-ghost-dark btn-lg" href="eteacher.html">More about eTeacher</a>
    </div>
  </div>
</section>
"""
    fold10 = final_cta_verona("Study Italian at a school built for adults.", "One conversation with an advisor is enough to plan a real start.", "Talk to an Advisor")
    body = hero + fold2 + fold3 + fold4 + fold5 + fold6 + fold7 + fold8 + fold9 + fold10
    (ROOT/"about.html").write_text(page("About Club Italia · A cultural Italian school for adults", "Club Italia is the Italian language faculty of eTeacher Group, the European online school operator founded in 2000. Live, small, native, cultural.", body))
    print("wrote about.html")


# ============================================================
# ETEACHER.HTML — 8 folds
# ============================================================
def build_eteacher():
    hero = """
<section class="section-ink hero-page hero-100">
  <div class="hero-bg">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/img/life-uffizi-hall.jpg">
      <source src="assets/video/roma-piazza.mp4" type="video/mp4">
    </video>
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">eTeacher Group</span>
    <h1 class="serif-display hero-h1">Twenty five years of teaching adults,<br><em>live online</em></h1>
    <p class="lead">eTeacher Group opened its first online language classroom in the year 2000. In the twenty five years since, we have taught more than four hundred thousand adult learners from one hundred and ninety seven countries.</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">Talk to an Advisor</button>
      <a class="btn btn-ghost btn-lg" href="about.html">About Club Italia</a>
    </div>
  </div>
</section>
"""
    fold2 = stats_strip("dark")
    tl = [("2000","eTeacher opens the first online Hebrew school for adult learners."),
          ("2005","Yiddish faculty opens. First cohort of retired academic learners."),
          ("2010","Arabic faculty. First large cohort of American learners."),
          ("2016","Spanish faculty. The first Latin language faculty."),
          ("2020","French faculty. Founding partnership with the Institut Français."),
          ("2022","Italian faculty · Club Italia opens with twelve founding students."),
          ("2026","400,000 adult learners taught. 197 countries served.")]
    tlist = "".join(f'<div class="tl-row"><div class="tl-year serif-display">{y}</div><div class="tl-body">{d}</div></div>' for y,d in tl)
    fold3 = f"""
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">History</span>
      <h2 class="serif-display">Six language faculties, in order</h2>
    </div>
    <div class="timeline">{tlist}
    </div>
  </div>
</section>
"""
    fold4 = """
<section class="section-cream">
  <div class="wrap">
    <div class="section-head-split">
      <div>
        <span class="eyebrow">Method across faculties</span>
        <h2 class="serif-display">The same commitments,<br>from Hebrew in 2000<br>to Italian in 2026</h2>
      </div>
    </div>
    <div class="editorial-2col">
      <div class="col-essay">
        <p>The teaching commitments have not changed across the six faculties. Live classes only. Small groups only. Native teachers only. A syllabus written by the teachers themselves, revised at least once a year. A single head of school for each faculty, who reads every end of term evaluation and speaks with every teacher every month.</p>
      </div>
      <div class="col-essay">
        <p>What has changed is the technology, the pedagogy, and the range of subjects. Live online teaching in the year 2000 was a small technical miracle. In 2026 it is what a serious adult school is expected to do well. We were early to it. We are still building for it.</p>
      </div>
    </div>
  </div>
</section>
"""
    aw = [("Preply Awards · 2024","Top rated online language academy · European operator category."),
          ("EdTech Digest · 2023","Adult learning platform of the year."),
          ("Financial Times · 2022","Named in the FT 1000 fastest growing European companies."),
          ("Trustpilot Verified · 2020 to present","Consistent 4.7 to 4.8 average across all six faculties."),]
    ag = "".join(f'<article class="award-card"><h3 class="serif-display">{n}</h3><p>{d}</p></article>' for n,d in aw)
    fold5 = f"""
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Awards and press</span>
      <h2 class="serif-display">Recognised, and reviewed</h2>
    </div>
    <div class="award-grid">{ag}
    </div>
  </div>
</section>
"""
    lead = [("Shalom Ben Aharon","Chief Executive Officer","Founded the first eTeacher classroom in 2000. Adult learning practitioner. Studied philosophy at Tel Aviv."),
            ("Federica Colombo","Head of School · Club Italia","Ten years of adult Italian teaching before joining eTeacher. Master in linguistics, Perugia."),
            ("Yotam Sarid","Chief Learning Officer","Twenty years designing online adult curricula across six languages. Author of the eTeacher house method."),]
    lg = "".join(f'<article class="lead-card"><h3 class="serif-display">{n}</h3><div class="lead-role">{r}</div><p>{d}</p></article>' for n,r,d in lead)
    fold6 = f"""
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Leadership</span>
      <h2 class="serif-display">Three of the people who run the school</h2>
    </div>
    <div class="lead-grid">{lg}
    </div>
  </div>
</section>
"""
    fold7 = """
<section class="section-cream">
  <div class="wrap">
    <div class="section-head-split">
      <div>
        <span class="eyebrow">Why an Italian faculty</span>
        <h2 class="serif-display">The newest faculty,<br>built with the oldest instincts</h2>
      </div>
    </div>
    <div class="editorial-2col">
      <div class="col-essay">
        <p>Club Italia is the newest of the six faculties, opened in 2022 after two years of research and hiring. It is built on the same commitments as the five before it. Live only, small groups only, native teachers only, one head of school. The difference is subject matter. Italian required a specifically cultural syllabus, and the faculty was hired around that decision.</p>
      </div>
      <div class="col-essay">
        <a class="btn btn-primary btn-lg" href="about.html">About Club Italia</a>
      </div>
    </div>
  </div>
</section>
"""
    fold8 = final_cta_verona("A school with twenty five years behind it.", "Start with a conversation. Fifteen minutes with an advisor is enough to plan a first class.", "Talk to an Advisor")
    body = hero + fold2 + fold3 + fold4 + fold5 + fold6 + fold7 + fold8
    (ROOT/"eteacher.html").write_text(page("eTeacher Group · Twenty five years of adult online language schools", "eTeacher Group has taught adult learners online since 2000. Six language faculties. Four hundred thousand students. One hundred and ninety seven countries.", body))
    print("wrote eteacher.html")


# ============================================================
# FAQ.HTML — 3 folds
# ============================================================
def build_faq():
    hero = """
<section class="section-ink hero-page hero-page-short">
  <div class="hero-bg">
    <img src="assets/img/life-caffe-roma.jpg" alt="" loading="lazy">
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">Frequently asked</span>
    <h1 class="serif-display hero-h1">Everything worth asking<br><em>before you enrol</em></h1>
    <p class="lead">Twenty four common questions, in six categories. If the answer to yours is not here, our advisors will answer it directly.</p>
  </div>
</section>
"""
    cats = [
        ("Courses", [
            ("How long is a Club Italia level?","Around eight to ten months per CEFR level. Thirty two live classes, one to two per week, plus between lesson work of around ninety minutes."),
            ("Can I combine two tracks?","Yes. Most Club Italia students combine one Corsi di Italiano course (the structured spine) with one Parliamo course or one Culture Capsule for texture."),
            ("What if I miss a live class?","Every class is recorded and released to your cohort within twenty four hours, with the teacher's notes and any breakout materials."),
            ("Can I switch cohorts if my schedule changes?","Yes. We rebalance cohorts on request when a new term opens, at no cost."),
        ]),
        ("Pricing", [
            ("How much does a term cost?","See the full pricing page. The starting course is under three hundred dollars per month, and prices decrease per lesson at higher volumes."),
            ("Do you offer a trial class?","We do not offer a demo class. We offer a placement conversation with a real teacher, at no cost, before you enrol."),
            ("Is there a refund policy?","Yes. Full refund inside the first seven days after your first live class, no questions asked."),
            ("Are certificates included?","Yes. The end of level certificate is included in the course price. External CEFR examinations are not included."),
        ]),
        ("Teachers", [
            ("Are your teachers really native?","Yes. Every teacher on the faculty is Italian, born and raised in the region where they teach from."),
            ("Can I choose my teacher?","At enrolment, yes, subject to cohort availability. Between levels, teachers change with the level."),
            ("Do teachers stay with the same cohort for a whole level?","Yes. One teacher per cohort, for the full level. Continuity is a school policy."),
            ("Can I meet a teacher before enrolling?","Yes. Your placement conversation is with the teacher we match you to."),
        ]),
        ("Technology", [
            ("What software do you use for classes?","Zoom, in a licensed classroom account. No custom app to download."),
            ("Do I need a webcam?","Yes. A working webcam is required for small group classes."),
            ("What if my internet is unstable?","Most of our students study from home broadband. In practice this is not a problem. If a class is disrupted, the recording is always released."),
            ("Do you support learners with hearing loss?","Yes. Live captioning is available on request, in Italian and English."),
        ]),
        ("Biagio", [
            ("Is Biagio a real teacher?","No. Biagio is a language model, trained on our syllabus. Your teacher is a real person."),
            ("Does Biagio cost extra?","No. Biagio is included in every Club Italia enrolment at no additional cost."),
            ("Can I use Biagio to do my homework?","Biagio will refuse. He will help you find the sentence yourself."),
            ("Does Biagio share my messages with my teacher?","No. Biagio is private to you. Your teacher does not see what you have written in the coach."),
        ]),
        ("Certification", [
            ("What certificate do I get?","At the end of each level you receive an internal Club Italia certificate mapped to the CEFR band. It is a school certificate, not a state exam."),
            ("Is this the same as CILS or CELI?","No. CILS and CELI are Italian state examinations, taken through Università per Stranieri di Siena and Perugia. We prepare students for those exams but do not administer them."),
            ("Will my certificate be accepted for the Italian citizenship law?","Our certificate itself is not accepted for citizenship. Passing an official CELI or CILS at B1 is. We prepare students for the B1 exam in our advanced level."),
            ("Can I get transcripts and hours certified?","Yes. On request we provide a signed transcript of attended live hours."),
        ]),
    ]
    catblocks = ""
    for cat, qas in cats:
        items = "".join(f'<details class="faq-item"><summary><span>{q}</span><span class="faq-plus">+</span></summary><div class="faq-a"><p>{a}</p></div></details>' for q,a in qas)
        catblocks += f'<div class="faq-cat"><h3 class="serif-display">{cat}</h3><div class="faq-list">{items}</div></div>\n'
    fold2 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="faq-cats">{catblocks}
    </div>
  </div>
</section>
"""
    fold3 = final_cta_verona("Still have a question.", "Ask a Club Italia advisor by email at advisor@eTeacherGroup.com, or open a fifteen minute call.", "Talk to an Advisor")
    body = hero + fold2 + fold3
    (ROOT/"faq.html").write_text(page("FAQ · Club Italia", "Twenty four common questions about Club Italia. Courses, pricing, teachers, tech, Biagio, certification.", body))
    print("wrote faq.html")


# ============================================================
# SAMPLE-CLASS.HTML — 10 folds
# ============================================================
def build_sample():
    hero = """
<section class="section-ink hero-page hero-100">
  <div class="hero-bg">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/img/zoom-classroom-marco.jpg">
      <source src="assets/video/class-demo.mp4" type="video/mp4">
    </video>
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">A recorded class</span>
    <h1 class="serif-display hero-h1">Watch a <em>real Club Italia class</em></h1>
    <p class="lead">Not a demo. Not a trailer. A full eighty five minute class with Marco Rinaldi, live from Roma, at CI Principiante level A0 to A1.1, released with student permission.</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">Talk to an Advisor</button>
      <a class="btn btn-ghost btn-lg" href="#breakdown">See the minute by minute</a>
    </div>
  </div>
</section>
"""
    watch = [("A small group","Ten to twelve adults on screen. No broadcast."),
             ("A native teacher","Marco Rinaldi, live from Roma. His Roman study is behind him on the camera."),
             ("A cultural syllabus","This class opens on a Roman coffee bar. The grammar arrives through the scene, not before it.")]
    wg = "".join(f'<article class="watch-card"><h3 class="serif-display">{h}</h3><p>{p}</p></article>' for h,p in watch)
    fold2 = f"""
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What you will see</span>
      <h2 class="serif-display">Three things worth watching for</h2>
    </div>
    <div class="watch-grid">{wg}
    </div>
  </div>
</section>
"""
    fold3 = """
<section class="section-ink">
  <div class="wrap">
    <div class="zoom-frame">
      <img src="assets/img/zoom-classroom-marco.jpg" alt="Marco Rinaldi teaching a live Club Italia class from Roma" loading="lazy">
    </div>
    <p class="figure-cap">Marco Rinaldi, live from Roma, in a CI Principiante class recorded on 12 September 2025.</p>
  </div>
</section>
"""
    rows = [("0 to 5","Buongiorno round","Marco greets every student by name. Each student replies in one full Italian sentence about the weekend."),
            ("5 to 15","Warm review","Vocabulary from last week returns, in a light quiz on the shared screen. No score. A conversation."),
            ("15 to 30","New material","Marco introduces the topic of the day, in Italian, illustrated on the shared screen. English is used sparingly and briefly."),
            ("30 to 45","Guided practice","Breakout in pairs. Each pair works through a short conversation script. Marco visits every room."),
            ("45 to 55","Break","Ten minutes off camera. Marco stays online. Students who want to stay do."),
            ("55 to 75","Free conversation","On the topic of the day. Marco holds the room in Italian. English is not used in this segment."),
            ("75 to 85","Review and homework","Marco writes the week's take home task on the shared screen. Questions. Farewells.")]
    trows = "".join(f'<div class="min-row"><div class="min-t">{a}</div><div class="min-title">{b}</div><div class="min-d">{c}</div></div>' for a,b,c in rows)
    fold4 = f"""
<section class="section-cream" id="breakdown">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Minute by minute</span>
      <h2 class="serif-display">The eighty five minutes,<br>opened up</h2>
    </div>
    <div class="min-table">
      <div class="min-row min-head"><div class="min-t">Minutes</div><div class="min-title">Segment</div><div class="min-d">What happens</div></div>
      {trows}
    </div>
  </div>
</section>
"""
    fold5 = """
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head-split">
      <div>
        <span class="eyebrow">Transcript sample</span>
        <h2 class="serif-display">Two minutes of Italian,<br>with an English gloss</h2>
      </div>
    </div>
    <div class="transcript-2col">
      <div class="transcript-col">
        <div class="transcript-tag">Italian, as spoken</div>
        <p><strong>Marco:</strong> Allora, Diane, com'è andato il weekend a Portland?</p>
        <p><strong>Diane:</strong> Bene, grazie. Sono andata al mercato con mia figlia.</p>
        <p><strong>Marco:</strong> Bello. E cosa avete comprato?</p>
        <p><strong>Diane:</strong> Del pane, un po' di formaggio, e due bottiglie di vino italiano.</p>
        <p><strong>Marco:</strong> Vino italiano. Bravissima. Da che regione?</p>
        <p><strong>Diane:</strong> Non ricordo. Un rosso della Toscana, credo.</p>
      </div>
      <div class="transcript-col">
        <div class="transcript-tag">English gloss</div>
        <p><strong>Marco:</strong> So, Diane, how was the weekend in Portland?</p>
        <p><strong>Diane:</strong> Good, thank you. I went to the market with my daughter.</p>
        <p><strong>Marco:</strong> Nice. And what did you buy?</p>
        <p><strong>Diane:</strong> Some bread, a little cheese, and two bottles of Italian wine.</p>
        <p><strong>Marco:</strong> Italian wine. Well done. From which region?</p>
        <p><strong>Diane:</strong> I do not remember. A red from Tuscany, I think.</p>
      </div>
    </div>
  </div>
</section>
"""
    fold6 = """
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">And Zoom alone.</span>
      <h2 class="serif-display">Why this is not the same<br>as buying a Zoom seat</h2>
    </div>
    <div class="compare-grid">
      <div class="compare-col">
        <div class="compare-tag">Zoom, alone</div>
        <ul class="compare-list"><li>A meeting room</li><li>No syllabus</li><li>No teacher on the other side</li><li>No cohort</li><li>No between lesson work</li><li>No certificate</li></ul>
      </div>
      <div class="compare-col compare-col-us">
        <div class="compare-tag compare-tag-us">Club Italia</div>
        <ul class="compare-list"><li>A live class with a native Italian teacher</li><li>A CEFR aligned cultural syllabus</li><li>Ten to twelve adults, together for a whole level</li><li>Between lesson work marked in full</li><li>Biagio, quietly, in between</li><li>A certificate that maps to CEFR at the end</li></ul>
      </div>
    </div>
  </div>
</section>
"""
    testis = [
        {"n":"Diane Whitfield","loc":"Portland, Oregon","img":"assets/img/student-diane.jpg","t":"The room is real","b":"You cannot fake ten adults on a screen speaking to one another. That was the moment I signed up."},
        {"n":"Robert Marconi","loc":"Boston, Massachusetts","img":"assets/img/student-robert.jpg","t":"Marco holds the room","b":"I watched the sample class twice. The second time I noticed how he brings the quiet students into the conversation without making it awkward. That is a teacher."},
        {"n":"Sarah Levine","loc":"Brooklyn, New York","img":"assets/img/student-sarah.jpg","t":"This looked like the class I wanted","b":"I have taken a lot of language courses on video. This was the first one where I thought, that is a room I want to sit in."},
        {"n":"James O'Sullivan","loc":"Dublin, Ireland","img":"assets/img/student-james.jpg","t":"Small enough to hear every voice","b":"Every student spoke in the segment I watched. That is the small group promise, kept."},
        {"n":"Linda Cavalli","loc":"San Diego, California","img":"assets/img/student-linda.jpg","t":"An adult class","b":"It looked like the language courses I remembered from university, not like a phone app."},
        {"n":"Michael Feld","loc":"Tel Aviv, Israel","img":"assets/img/student-michael.jpg","t":"Serious, and warm","b":"The whole recording is serious about the language and warm with the students. Those two things do not always come together."},
    ]
    fold7 = tp_wall(testis)
    fold8 = """
<section class="section-olive">
  <div class="wrap center">
    <div class="pullquote-band pullquote-band-lg">
      <blockquote class="serif-display quote-xl"><em>A recorded lecture is a talk.<br>A recorded live class is a room.<br>The difference is the whole product.</em></blockquote>
      <div class="quote-attr quote-attr-light">Marco Rinaldi · Roma</div>
    </div>
  </div>
</section>
"""
    fold9 = """
<section class="section-cream">
  <div class="wrap center">
    <h2 class="serif-display">Seen enough</h2>
    <p class="lead">The next step is a fifteen minute call with an advisor. We plan a real start, in a real cohort.</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">Talk to an Advisor</button>
      <a class="btn btn-ghost-dark btn-lg" href="courses.html">Browse the courses</a>
    </div>
  </div>
</section>
"""
    fold10 = final_cta_verona("Or enrol directly.", "If the sample class showed you the school, we can enrol you into the next October cohort in one call.", "Talk to an Advisor")
    body = hero + fold2 + fold3 + fold4 + fold5 + fold6 + fold7 + fold8 + fold9 + fold10
    (ROOT/"sample-class.html").write_text(page("Watch a real Club Italia class · Sample lesson", "A recorded live class with Marco Rinaldi, live from Roma. CI Principiante, A0 to A1.1. Eighty five minutes, released with student permission.", body))
    print("wrote sample-class.html")


# ============================================================
# CONTACT.HTML — 7 folds
# ============================================================
def build_contact():
    hero = """
<section class="section-ink hero-page hero-100">
  <div class="hero-bg">
    <img src="assets/img/life-caffe-roma.jpg" alt="" loading="lazy">
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">Contact</span>
    <h1 class="serif-display hero-h1">Speak with <em>a Club Italia advisor</em></h1>
    <p class="lead">Four ways to reach us. All four are answered by a real person, on the same working day.</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">Talk to an Advisor</button>
      <a class="btn btn-ghost btn-lg" href="#form">Write to a teacher</a>
    </div>
  </div>
</section>
"""
    cards = [
        ("Phone","US · +1 800 246 3541","EU · +44 20 3868 1810","Mon to Fri, 08:00 to 20:00 US ET"),
        ("Email","advisor@eTeacherGroup.com","Answered by a Club Italia advisor within one working day.",""),
        ("WhatsApp","+972 3 763 8130","Same working hours as the phone lines.",""),
        ("Office","eTeacher Group","Kfar Neter 4059300, Israel","EU office · Amsterdam"),
    ]
    cg = ""
    for title, a, b, c in cards:
        cg += f'<article class="contact-card"><h3 class="serif-display">{title}</h3><p class="contact-a">{a}</p><p>{b}</p>' + (f'<p class="contact-note">{c}</p>' if c else '') + '</article>'
    fold2 = f"""
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Four channels</span>
      <h2 class="serif-display">Reach a person, on any of these</h2>
    </div>
    <div class="contact-grid">{cg}
    </div>
  </div>
</section>
"""
    fold3 = """
<section class="section-cream">
  <div class="wrap">
    <div class="editorial-2col">
      <div class="col-essay">
        <span class="eyebrow">Response time</span>
        <h2 class="serif-display">A working day.<br>In practice, less.</h2>
      </div>
      <div class="col-essay">
        <p>Every message that reaches Club Italia is answered by a Club Italia advisor within one working day. The published SLA is twenty four working hours. The measured median in September 2026 is four hours and eleven minutes.</p>
        <p>Advisor hours are 08:00 to 20:00 US Eastern, Monday through Friday. Outside those hours, an out of hours advisor covers urgent enrolment matters. All response times are logged. All promises are kept.</p>
      </div>
    </div>
  </div>
</section>
"""
    opts = "".join(f'<option value="{t["slug"]}">{t["first"]} {t["last"]} · {t["city"]}</option>' for t in TEACHERS)
    fold4 = f"""
<section class="section-travertine" id="form">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Write directly to a teacher</span>
      <h2 class="serif-display">A question for one of the faculty</h2>
      <p class="lead">Your message will reach the teacher within one working day. It will be answered by them, not by an assistant.</p>
    </div>
    <form class="teacher-form" novalidate>
      <div class="field"><label for="tf-name">Your name</label><input id="tf-name" name="name" type="text" required></div>
      <div class="field"><label for="tf-email">Your email</label><input id="tf-email" name="email" type="email" required></div>
      <div class="field"><label for="tf-teacher">Which teacher</label>
        <select id="tf-teacher" name="teacher" required>
          <option value="">Choose a teacher</option>
          {opts}
          <option value="advisor">I would rather write to an advisor</option>
        </select>
      </div>
      <div class="field field-full"><label for="tf-msg">Your message</label><textarea id="tf-msg" name="message" rows="5" required></textarea></div>
      <div class="field field-full"><button class="btn btn-primary btn-lg" type="submit">Send my message</button></div>
    </form>
  </div>
</section>
"""
    regs = [("United States","+1 800 246 3541","US advisors on Eastern time, 08:00 to 20:00."),
            ("United Kingdom","+44 20 3868 1810","London office, 09:00 to 18:00 UK time."),
            ("Israel","+972 3 763 8130","Head office in Kfar Neter, 09:00 to 19:00 IL time."),
            ("Europe","+31 20 244 1980","Amsterdam desk, 09:00 to 18:00 CET.")]
    rg = "".join(f'<article class="region-card"><h3 class="serif-display">{n}</h3><p class="region-phone">{p}</p><p>{d}</p></article>' for n,p,d in regs)
    fold5 = f"""
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Regional desks</span>
      <h2 class="serif-display">Four offices, four time zones</h2>
    </div>
    <div class="region-cards">{rg}
    </div>
  </div>
</section>
"""
    fold6 = """
<section class="section-cream">
  <div class="wrap center">
    <span class="eyebrow">Before you write</span>
    <h2 class="serif-display">Common questions, already answered</h2>
    <div class="faq-shortcut-grid">
      <a class="faq-shortcut" href="faq.html#courses">Courses and cohorts</a>
      <a class="faq-shortcut" href="pricing.html">Pricing and refund</a>
      <a class="faq-shortcut" href="faq.html#teachers">Teachers and matching</a>
      <a class="faq-shortcut" href="faq.html#certification">Certification</a>
    </div>
  </div>
</section>
"""
    fold7 = final_cta_verona("Or open a fifteen minute call.", "A Club Italia advisor can call you at a time of your choosing. Choose your window and we will confirm.", "Talk to an Advisor")
    body = hero + fold2 + fold3 + fold4 + fold5 + fold6 + fold7
    (ROOT/"contact.html").write_text(page("Contact · Club Italia", "Speak with a Club Italia advisor. Phone, email, WhatsApp, office. All four answered by a real person on the same working day.", body))
    print("wrote contact.html")


# ============================================================
# BLOG.HTML — 3 folds
# ============================================================
def build_blog():
    hero = """
<section class="section-ink hero-page hero-page-short">
  <div class="hero-bg">
    <img src="assets/img/life-uffizi-hall.jpg" alt="" loading="lazy">
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">Cultural journal</span>
    <h1 class="serif-display hero-h1">The Club Italia<br><em>Cultural Journal</em></h1>
    <p class="lead">Essays from the faculty. Language, culture, teaching, and Italian life, written from Firenze, Roma, Bologna, Milano, Venezia, Napoli and Palermo.</p>
  </div>
</section>
"""
    fold2 = """
<section class="section-paper">
  <div class="wrap">
    <article class="feat-essay">
      <figure class="feat-fig"><img src="assets/img/life-caffe-roma.jpg" alt="A Roman coffee bar" loading="lazy"></figure>
      <div class="feat-body">
        <span class="eyebrow">Featured essay · 11 September 2026</span>
        <h2 class="serif-display">Why we open every beginners class with a coffee bar</h2>
        <p class="lead">There is a reason the first vocabulary of every Club Italia beginner course is set inside a bar. It is not sentiment. It is the fastest route from silence into speech.</p>
        <p class="feat-attr">By Marco Rinaldi · Roma · 12 minutes read</p>
        <a class="btn btn-primary" href="pages/blog/coffee-bar.html">Read the essay</a>
      </div>
    </article>
  </div>
</section>
"""
    posts = [
        ("Chiara Bellini","Reading Ferrante in her own city","pillar-art.jpg","On teaching L'amica geniale at CI Elementare, from a Florentine classroom, to adults who have only read Ferrante in translation."),
        ("Giulia Moretti","Ragù as a grammar lesson","pillar-food.jpg","How the imperative and the past participle come alive when a whole class is cooking together on a Wednesday evening."),
        ("Alessandro Ferri","Learning Italian at La Scala","pillar-opera.jpg","What five seasons of coaching foreign singers taught me about how English speakers should breathe when they speak Italian."),
        ("Francesca Zeno","Rehearsing a trip to Venice","pillar-travel.jpg","The awkward middle days of a trip are where most travellers give up on their new Italian. Here is how we prepare for them in class."),
        ("Luca De Simone","The passage from A2 to B1","city-napoli.jpg","On the hardest month of the course ladder, and how we hold students through it, from a study in Naples."),
        ("Sofia Mazzara","Sicily is not a dialect","city-palermo.jpg","On the Italian I teach from Palermo, and why standard Italian in Sicily is a chosen language, spoken with care."),
        ("Head of School","Why we opened Club Italia in 2022","hero-italian-life.jpg","The eighteen months of hiring, curriculum writing and faculty building that preceded the first live cohort."),
        ("Marco Rinaldi","What an adult beginner actually needs","env-marco-desk.jpg","Notes from nine years of teaching absolute beginners in the first fifteen minutes of the first class."),
        ("Giulia Moretti","The Emilia Romagna kitchen, in a Zoom window","env-giulia-kitchen.jpg","On teaching food language from a real kitchen, and why the room behind the teacher is part of the syllabus."),
        ("Chiara Bellini","On patience","teacher-chiara.jpg","One of the most underrated skills of an adult language teacher, and how I learned it."),
    ]
    grid = ""
    for author, title, img, blurb in posts:
        grid += f"""
    <a class="post-card" href="pages/blog/">
      <figure><img src="assets/img/{img}" alt="{title}" loading="lazy"></figure>
      <div class="post-body">
        <span class="post-author">{author}</span>
        <h3 class="serif-display">{title}</h3>
        <p>{blurb}</p>
      </div>
    </a>"""
    fold3 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">All essays</span>
      <h2 class="serif-display">The cultural journal, in full</h2>
    </div>
    <div class="posts-grid">{grid}
    </div>
    <div class="subscribe-band">
      <div>
        <h3 class="serif-display">Have the journal delivered.</h3>
        <p>One essay a fortnight, in your inbox. Written by the faculty, no marketing.</p>
      </div>
      <form class="sub-form" novalidate>
        <input type="email" name="email" placeholder="Your email" required aria-label="Email">
        <button class="btn btn-primary" type="submit">Subscribe</button>
      </form>
    </div>
  </div>
</section>
"""
    body = hero + fold2 + fold3
    (ROOT/"blog.html").write_text(page("Cultural Journal · Club Italia", "Essays from the Club Italia faculty. Italian language, culture, teaching and life, written from seven Italian cities.", body))
    print("wrote blog.html")


# ============================================================
# MAP.HTML — 8 folds
# ============================================================
def build_map():
    hero = """
<section class="section-ink hero-page hero-100">
  <div class="hero-bg">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/img/life-amalfi-coast.jpg">
      <source src="assets/video/napoli-mare.mp4" type="video/mp4">
    </video>
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">A geographical school</span>
    <h1 class="serif-display hero-h1">The map <em>of Club Italia</em></h1>
    <p class="lead">Seven native teachers in seven Italian cities. This is where they teach from, and this is the Italy each of them brings into the classroom.</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">Talk to an Advisor</button>
      <a class="btn btn-ghost btn-lg" href="teachers.html">The full faculty</a>
    </div>
  </div>
</section>
"""
    # Fold 2 — inline SVG map with 7 pins
    pins = [
        ("Milano",180,120),("Venezia",290,150),("Bologna",245,205),
        ("Firenze",235,255),("Roma",270,325),("Napoli",325,385),("Palermo",305,505),
    ]
    pinsvg = ""
    for name,x,y in pins:
        pinsvg += f'<g class="pin"><circle cx="{x}" cy="{y}" r="9" fill="var(--gold, #B08640)" stroke="#fff" stroke-width="2"/><text x="{x+14}" y="{y+4}" font-family="Cormorant Garamond, serif" font-style="italic" font-size="18" fill="var(--ink)">{name}</text></g>'
    fold2 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Seven pins</span>
      <h2 class="serif-display">Where our teachers actually live</h2>
    </div>
    <div class="italy-map-wrap">
      <svg viewBox="0 0 500 600" class="italy-map" role="img" aria-label="Map of Italy with the seven Club Italia teachers">
        <path d="M240 40 L260 55 L280 60 L295 90 L285 110 L275 130 L280 150 L270 175 L260 210 L245 240 L235 260 L245 290 L260 315 L275 340 L285 370 L320 390 L340 415 L345 445 L340 475 L320 490 L300 500 L285 505 L275 520 L280 550 L260 570 L235 555 L220 530 L215 500 L225 470 L240 450 L245 420 L235 400 L215 385 L200 360 L195 330 L205 305 L215 275 L220 245 L215 220 L210 195 L205 170 L215 145 L220 120 L225 95 L235 65 Z" fill="var(--paper-2, #f3f0e7)" stroke="var(--ink, #0B0B0D)" stroke-width="1.5"/>
        <path d="M275 520 Q310 515 335 520 Q345 540 340 555 Q315 560 290 555 Z" fill="var(--paper-2, #f3f0e7)" stroke="var(--ink, #0B0B0D)" stroke-width="1.5"/>
        {pinsvg}
      </svg>
    </div>
  </div>
</section>
"""
    # Folds 3-7: one per city, alternating
    city_data = [
        ("Roma","Lazio","marco","city-roma.jpg","Marco Rinaldi","ci1","CI Principiante","Rome is a beginner's city. Everyone in Rome starts somewhere. Marco teaches from a study in Prati, five streets from St Peter's. His Italian is standard, unhurried, patient with the first months. A student in a Marco class hears the language the way an older Roman would speak it to a new arrival."),
        ("Firenze","Toscana","chiara","city-firenze.jpg","Chiara Bellini","ci2","CI Elementare","Florence is the source city of standard Italian. Chiara teaches from an apartment above the Arno, and every class is textured with the specific rhythm of Tuscan speech. Her students learn Italian in the register of the newspapers and the universities, warmed by a Florentine light."),
        ("Bologna","Emilia-Romagna","giulia","city-bologna.jpg","Giulia Moretti","ci3","CI Intermedio","Bologna is a city that feeds you and asks what you thought of it. Giulia teaches from her kitchen, copper pans behind her on the camera. Her intermediate students learn Italian through the language of food, and leave able to hold a real market conversation."),
        ("Milano","Lombardia","alessandro","city-milano.jpg","Alessandro Ferri","cap-opera","Capsule L'Opera","Milan is the practical capital, the working capital. Alessandro trained at the Conservatorio and spent five seasons at La Scala coaching foreign singers. In his classes, the vowels are the syllabus. Students learn to speak Italian the way a good Italian sings it."),
        ("Venezia","Veneto","francesca","city-venezia.jpg","Francesca Zeno","ps-viaggio","Parliamo In Viaggio","Venice survives on travellers. Francesca teaches travel Italian, rehearsing arrivals and awkward middle days for students planning a trip to Italy. Her classroom overlooks a side canal. The light behind her on the camera is enough on its own."),
        ("Napoli","Campania","luca","city-napoli.jpg","Luca De Simone","ci4","CI Avanzato","Naples is demanding, and Luca is a demanding teacher. He takes students through the last stage of the ladder, from confident A2 to a real B1. His students often go on to sit a state CELI examination in the twelve months after his course."),
        ("Palermo","Sicilia","sofia","city-palermo.jpg","Sofia Mazzara","ci4","CI Avanzato","Sicily is a country of its own inside Italy. Standard Italian in Palermo is a chosen thing, spoken with care. That care is what Sofia teaches. She shares the top level with Luca, and her students hear two different Italian accents before the certificate."),
    ]
    city_folds = ""
    for i, (city, region, slug, img, teacher, cid, coursename, body) in enumerate(city_data[:5]):
        left = i % 2 == 0
        city_folds += f"""
<section class="section-{'paper' if left else 'travertine'}">
  <div class="wrap">
    <article class="city-row {'city-left' if left else 'city-right'}">
      <figure class="city-fig"><img src="assets/img/{img}" alt="{city}" loading="lazy"></figure>
      <div class="city-body">
        <span class="eyebrow">{region}</span>
        <h2 class="serif-display">{city}</h2>
        <p>{body}</p>
        <div class="city-links">
          <a class="btn btn-primary" href="pages/teachers/{slug}.html">Meet {teacher}</a>
          <a class="btn btn-ghost-dark" href="pages/courses/{cid}.html">{coursename}</a>
        </div>
      </div>
    </article>
  </div>
</section>
"""
    fold8 = final_cta_verona("The map is the school.", "Every Club Italia class is a room in one of these seven Italian cities. Talk to an advisor and we place you into one.", "Talk to an Advisor")
    body = hero + fold2 + city_folds + fold8
    (ROOT/"map.html").write_text(page("The map of Club Italia · Seven Italian cities", "Where the Club Italia teachers live and teach. Roma, Firenze, Bologna, Milano, Venezia, Napoli, Palermo. Seven cities, one school.", body))
    print("wrote map.html")


# ============================================================
# COMMUNITY.HTML — 8 folds
# ============================================================
def build_community():
    hero = """
<section class="section-ink hero-page hero-100">
  <div class="hero-bg">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/img/hero-italian-life.jpg">
      <source src="assets/video/bologna-portici.mp4" type="video/mp4">
    </video>
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">Il Circolo</span>
    <h1 class="serif-display hero-h1">The Club Italia<br><em>circle of learners</em></h1>
    <p class="lead">Every enrolled student joins Il Circolo, the private Club Italia community. Six recurring events. One private forum. Alumni who stayed.</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">Talk to an Advisor</button>
      <a class="btn btn-ghost btn-lg" href="#pillars">See the six pillars</a>
    </div>
  </div>
</section>
"""
    pillars = [
        ("Aperitivo Digitale","Fortnightly hour on Zoom, all levels, no teacher. Just adults with a glass of wine, speaking Italian."),
        ("Cinema Club","Monthly film screening with a private introduction and a post film discussion in Italian."),
        ("Cucina Insieme","A live cooking session with Giulia from Bologna, four times a year. Recipe sent in advance."),
        ("Storia del Mese","One historical figure per month, taught in Italian at B1 level, open to intermediate and above."),
        ("Salotto Musicale","A live opera and song listening session, hosted from Milano by Alessandro."),
        ("Viaggio Insieme","One curated small group trip to Italy each summer. Ten alumni, one faculty host."),
    ]
    pg = "".join(f'<article class="circle-pillar"><h3 class="serif-display">{h}</h3><p>{p}</p></article>' for h,p in pillars)
    fold2 = f"""
<section class="section-paper" id="pillars">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Six pillars</span>
      <h2 class="serif-display">What actually happens in Il Circolo</h2>
    </div>
    <div class="circle-grid">{pg}
    </div>
  </div>
</section>
"""
    fold3 = """
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">The private forum</span>
      <h2 class="serif-display">Where students continue the conversation</h2>
    </div>
    <div class="forum-mock">
      <div class="forum-head"><span>Il Circolo · forum privato</span><span class="forum-online">184 online</span></div>
      <div class="forum-thread"><div class="ft-author">Diane W · CI Intermedio</div><div class="ft-title">Un dubbio sul congiuntivo dopo "credo che"</div><div class="ft-meta">42 risposte · aggiornato 4 minuti fa</div></div>
      <div class="forum-thread"><div class="ft-author">Robert M · CI Elementare</div><div class="ft-title">Consigli per un weekend a Firenze in ottobre</div><div class="ft-meta">28 risposte · aggiornato 22 minuti fa</div></div>
      <div class="forum-thread"><div class="ft-author">Sarah L · CI Avanzato</div><div class="ft-title">Chi ha visto La chimera di Rohrwacher</div><div class="ft-meta">67 risposte · aggiornato 1 ora fa</div></div>
      <div class="forum-thread"><div class="ft-author">James O · Parliamo Al Caffè</div><div class="ft-title">Un caffè lungo o un caffè americano</div><div class="ft-meta">15 risposte · aggiornato 3 ore fa</div></div>
    </div>
    <p class="figure-cap">The private Club Italia forum, moderated by the faculty, in Italian and English.</p>
  </div>
</section>
"""
    stories = [
        ("Diane Whitfield","Portland, Oregon","student-diane.jpg","Two years in, still in Il Circolo","I finished CI Avanzato in June. I stayed in the forum, I still go to Aperitivo Digitale every fortnight, and I am on the summer trip to Puglia in July. The school did not end when the course did."),
        ("Robert Marconi","Boston, Massachusetts","student-robert.jpg","Made a real friend in the community","I met a woman in Il Circolo who was studying at the same level. We now Skype in Italian every Sunday. That was three years ago. She is coming to visit Boston in May."),
        ("Sarah Levine","Brooklyn, New York","student-sarah.jpg","The Cinema Club changed how I watch films","I never watched Italian film before. Now I watch one a month, with fifty other Club Italia students, and we discuss it after. That is a community, not a mailing list."),
    ]
    sg = ""
    for n, loc, img, title, body in stories:
        sg += f'<article class="alumni-card"><div class="alumni-head"><img src="assets/img/{img}" alt="{n}" loading="lazy"><div><div class="alumni-name">{n}</div><div class="alumni-loc">{loc}</div></div></div><h3 class="serif-display">{title}</h3><p>{body}</p></article>'
    fold4 = f"""
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Alumni</span>
      <h2 class="serif-display">Three students who stayed</h2>
    </div>
    <div class="alumni-grid">{sg}
    </div>
  </div>
</section>
"""
    fold5 = """
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Upcoming events</span>
      <h2 class="serif-display">What is on this term</h2>
    </div>
    <div class="events-list">
      <div class="ev-row"><div class="ev-date"><div class="ev-day">18</div><div class="ev-mon">Sep</div></div><div class="ev-body"><h3>Aperitivo Digitale</h3><p>19:00 CET · all levels · hosted by Marco</p></div></div>
      <div class="ev-row"><div class="ev-date"><div class="ev-day">02</div><div class="ev-mon">Oct</div></div><div class="ev-body"><h3>Cinema Club · La chimera</h3><p>20:00 CET · A2 and above · hosted by Chiara</p></div></div>
      <div class="ev-row"><div class="ev-date"><div class="ev-day">15</div><div class="ev-mon">Oct</div></div><div class="ev-body"><h3>Cucina Insieme · ragù bolognese</h3><p>18:00 CET · all levels · hosted by Giulia</p></div></div>
      <div class="ev-row"><div class="ev-date"><div class="ev-day">29</div><div class="ev-mon">Oct</div></div><div class="ev-body"><h3>Storia del Mese · Enrico Fermi</h3><p>19:30 CET · B1 · hosted by Luca</p></div></div>
    </div>
    <div class="center" style="margin-top:2.4rem">
      <a class="btn btn-primary btn-lg" href="events.html">See all events</a>
    </div>
  </div>
</section>
"""
    fold6 = """
<section class="section-verona">
  <div class="wrap center">
    <div class="pullquote-band pullquote-band-lg">
      <blockquote class="serif-display quote-xl"><em>A course ends. A circle does not.<br>Il Circolo is the reason so many of our students are still with us five years later.</em></blockquote>
      <div class="quote-attr quote-attr-light">Head of School · Club Italia</div>
    </div>
  </div>
</section>
"""
    fold7 = """
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Feature</span>
      <h2 class="serif-display">The summer trip to Italy</h2>
    </div>
    <div class="editorial-2col">
      <div class="col-essay col-figure">
        <figure><img src="assets/img/life-amalfi-coast.jpg" alt="A curated small group trip in Italy" loading="lazy"></figure>
      </div>
      <div class="col-essay">
        <p>Once a year, in July, ten Club Italia alumni travel to Italy together for eight days, hosted by one of our faculty. The trip is small on purpose. The whole thing is conducted in Italian. In 2026 the trip is to Puglia, hosted by Luca from Napoli. In 2027 it will be to Sicily, hosted by Sofia.</p>
        <p>The trip is open only to students who have completed at least one full CEFR level with the school. It is not a package tour. It is a small group of Italian speakers going to Italy together.</p>
      </div>
    </div>
  </div>
</section>
"""
    fold8 = final_cta_verona("Study once, stay for years.", "Every Club Italia enrolment includes Il Circolo, for as long as you keep learning with us.", "Talk to an Advisor")
    body = hero + fold2 + fold3 + fold4 + fold5 + fold6 + fold7 + fold8
    (ROOT/"community.html").write_text(page("Il Circolo · The Club Italia community", "The private Club Italia community, Il Circolo. Six recurring events, a private forum, and an annual summer trip to Italy for alumni.", body))
    print("wrote community.html")


# ============================================================
# EVENTS.HTML — 5 folds
# ============================================================
def build_events():
    hero = """
<section class="section-ink hero-page hero-100">
  <div class="hero-bg">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/img/life-uffizi-hall.jpg">
      <source src="assets/video/venezia-canal.mp4" type="video/mp4">
    </video>
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">Cultural events</span>
    <h1 class="serif-display hero-h1">The Italian calendar,<br><em>in real time</em></h1>
    <p class="lead">Three free live events a year, open to prospective students and enrolled Club Italia students alike. Real cultural moments, hosted by the faculty.</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">Talk to an Advisor</button>
      <a class="btn btn-ghost btn-lg" href="community.html">See Il Circolo</a>
    </div>
  </div>
</section>
"""
    events = [
        ("Festa della Repubblica","event-festa.jpg","2 June 2026","A live evening from Roma with Marco Rinaldi. History of the day, real news footage, and a live conversation with a Roman journalist.","pages/events/festa-repubblica.html"),
        ("Carnevale di Venezia","event-carnevale.jpg","14 February 2026","A live morning from Venezia with Francesca Zeno. History of the masks, the language of the festival, and a live walk through the Cannaregio.","pages/events/carnevale.html"),
        ("Palio di Siena","event-palio.jpg","2 July 2026","A live evening with Chiara Bellini from Firenze. The full context of the Palio, its language, and a live conversation with a Sienese contradaiolo.","pages/events/palio-siena.html"),
    ]
    eg = ""
    for name, img, date, body, href in events:
        eg += f'<a class="event-card" href="{href}"><figure><img src="assets/img/{img}" alt="{name}" loading="lazy"></figure><div class="event-body"><span class="event-date">{date}</span><h3 class="serif-display">{name}</h3><p>{body}</p><span class="event-more">See the event</span></div></a>'
    fold2 = f"""
<section class="section-paper">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Three flagship events</span>
      <h2 class="serif-display">The Italian year, live</h2>
    </div>
    <div class="event-grid">{eg}
    </div>
  </div>
</section>
"""
    fold3 = """
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Upcoming, all levels</span>
      <h2 class="serif-display">The next three months</h2>
    </div>
    <div class="events-list">
      <div class="ev-row"><div class="ev-date"><div class="ev-day">18</div><div class="ev-mon">Sep</div></div><div class="ev-body"><h3>Aperitivo Digitale</h3><p>19:00 CET · all levels · hosted by Marco</p></div></div>
      <div class="ev-row"><div class="ev-date"><div class="ev-day">02</div><div class="ev-mon">Oct</div></div><div class="ev-body"><h3>Cinema Club · La chimera</h3><p>20:00 CET · A2 and above · hosted by Chiara</p></div></div>
      <div class="ev-row"><div class="ev-date"><div class="ev-body">
        <h3>Cucina Insieme · ragù bolognese</h3><p>15 October · 18:00 CET · all levels · hosted by Giulia</p></div></div>
      <div class="ev-row"><div class="ev-date"><div class="ev-day">29</div><div class="ev-mon">Oct</div></div><div class="ev-body"><h3>Storia del Mese · Enrico Fermi</h3><p>19:30 CET · B1 · hosted by Luca</p></div></div>
      <div class="ev-row"><div class="ev-date"><div class="ev-day">12</div><div class="ev-mon">Nov</div></div><div class="ev-body"><h3>Salotto Musicale · Puccini</h3><p>20:00 CET · A2 and above · hosted by Alessandro</p></div></div>
    </div>
  </div>
</section>
"""
    fold4 = """
<section class="section-travertine">
  <div class="wrap">
    <div class="editorial-2col">
      <div class="col-essay">
        <span class="eyebrow">Community feature</span>
        <h2 class="serif-display">One event a year is in person.</h2>
      </div>
      <div class="col-essay">
        <p>The Viaggio Insieme summer trip to Italy is our only in person event. Ten alumni, one faculty host, eight days, conducted in Italian. Open only to students who have completed at least one full CEFR level with the school. In 2026 the trip is to Puglia, hosted by Luca from Napoli. In 2027, Sicily, hosted by Sofia.</p>
        <a class="btn btn-primary" href="community.html">Read about the trip</a>
      </div>
    </div>
  </div>
</section>
"""
    fold5 = final_cta_verona("Attend the next event.", "The next Aperitivo Digitale is on 18 September at 19:00 CET, hosted by Marco from Roma. Free, live, open to prospective students.", "Talk to an Advisor")
    body = hero + fold2 + fold3 + fold4 + fold5
    (ROOT/"events.html").write_text(page("Events · The Club Italia cultural calendar", "The Club Italia cultural events calendar. Three flagship live events a year, plus fortnightly Il Circolo evenings, hosted by the faculty from Italy.", body))
    print("wrote events.html")


# ============================================================
# PRIVACY.HTML + TERMS.HTML — legal shape
# ============================================================
def build_legal(slug, title, lead, sections, subtitle):
    hero = f"""
<section class="section-ink hero-page hero-page-short">
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">Legal</span>
    <h1 class="serif-display hero-h1">{title}</h1>
    <p class="lead">{subtitle}</p>
  </div>
</section>
"""
    plain = f"""
<section class="section-paper">
  <div class="wrap">
    <div class="editorial-2col">
      <div class="col-essay">
        <span class="eyebrow">In plain English</span>
        <h2 class="serif-display">The short version</h2>
      </div>
      <div class="col-essay">
        <p>{lead}</p>
      </div>
    </div>
  </div>
</section>
"""
    toc = "".join(f'<li><a href="#s{i+1:02d}">{i+1:02d}. {name}</a></li>' for i,(name,_) in enumerate(sections))
    secs = "".join(f'<article class="legal-sec" id="s{i+1:02d}"><h3 class="serif-display">{i+1:02d}. {name}</h3><div class="legal-body">{body}</div></article>' for i,(name,body) in enumerate(sections))
    main = f"""
<section class="section-cream">
  <div class="wrap legal-wrap">
    <aside class="legal-toc">
      <div class="legal-toc-title">Contents</div>
      <ol>{toc}</ol>
    </aside>
    <div class="legal-main">{secs}</div>
  </div>
</section>
"""
    contact = """
<section class="section-travertine">
  <div class="wrap center">
    <span class="eyebrow">Questions on this policy</span>
    <h2 class="serif-display">Write to us</h2>
    <p class="lead">Email privacy@eTeacherGroup.com or write to eTeacher Group, Kfar Neter 4059300, Israel.</p>
    <div class="cta-row"><a class="btn btn-primary btn-lg" href="mailto:privacy@eTeacherGroup.com">Email us</a><a class="btn btn-ghost-dark btn-lg" href="contact.html">Contact the school</a></div>
  </div>
</section>
"""
    body = hero + plain + main + contact
    (ROOT/f"{slug}.html").write_text(page(f"{title} · Club Italia", f"{title} for Club Italia by eTeacher Group.", body))
    print(f"wrote {slug}.html")


def build_privacy():
    lead = "We collect the least data we need to teach you Italian, we do not sell any of it, and we delete it when you ask us to. This page is the full explanation of that."
    subs = [
        ("The short version", "<p>We are eTeacher Group, based in Kfar Neter, Israel, trading in this country as Club Italia. We hold your name, contact details, learning records, payment references and support correspondence. We use them to teach you Italian and to run your account. Nothing else.</p>"),
        ("Who is the data controller", "<p>eTeacher Group Ltd, Kfar Neter 4059300, Israel, is the data controller of your personal information. Our EU representative is eTeacher Europe BV, Amsterdam.</p>"),
        ("What we collect", "<p>Contact information you give us, learning records generated by your classes, technical records from your device when you use our services, and payment references from our payment processor.</p>"),
        ("Why we collect it", "<p>To provide the classes and services you have signed up for, to run your account, to answer your questions, to send you information about your course, and to meet our own legal obligations.</p>"),
        ("Legal basis", "<p>Contract, legitimate interest, legal obligation, and, where required, your consent. Marketing to a prospective student is on consent, and can be withdrawn at any time.</p>"),
        ("Who we share it with", "<p>Only the third parties needed to run the service: Zoom, our payment processor, our email provider, our accounting provider, and any regulator that lawfully requests it.</p>"),
        ("International transfers", "<p>Some of our providers are outside the European Economic Area. Where they are, transfers are covered by standard contractual clauses or an adequacy decision.</p>"),
        ("How long we keep it", "<p>Enrolment records for as long as you have an active account and for seven years after that, for accounting and legal reasons. Everything else, no longer than needed.</p>"),
        ("Your rights", "<p>Access, correction, deletion, portability, restriction and objection. Write to us and we will action any of these within thirty days.</p>"),
        ("Cookies", "<p>We use essential cookies to run the site and analytics cookies to understand how it is used. No advertising cookies. No third party trackers.</p>"),
        ("Children", "<p>Club Italia is a school for adults. We do not knowingly enrol learners under the age of eighteen.</p>"),
        ("Changes to this policy", "<p>We update this policy when the law changes or when we add a service. The date at the top of the page will tell you when it was last updated. Substantive changes will be notified by email to enrolled students.</p>"),
    ]
    build_legal("privacy", "Privacy policy", lead, subs, "Last updated 11 September 2026. This page explains what data we hold about you, why we hold it, and what you can ask us to do with it.")


def build_terms():
    lead = "You are enrolling in a live Italian language course delivered by real teachers over Zoom. This page is the full contract between you and us. It is written in plain English."
    subs = [
        ("Who these terms are between", "<p>These terms are between you and eTeacher Group Ltd, Kfar Neter 4059300, Israel, trading as Club Italia. By enrolling in a course, you agree to these terms.</p>"),
        ("What you are buying", "<p>A place in a live Italian language cohort taught by one of our native faculty, delivered over Zoom, on a fixed schedule, for a fixed number of weeks, at a stated CEFR level.</p>"),
        ("Enrolment and start date", "<p>Your enrolment is confirmed when you receive a written confirmation from a Club Italia advisor. Your start date is the date of your first live class in your cohort.</p>"),
        ("Prices and payment", "<p>Prices are as stated on the pricing page at the time of enrolment. You may pay in full or by monthly instalment. Payment is by credit card, bank transfer or PayPal.</p>"),
        ("Refund policy", "<p>You may cancel and receive a full refund inside the first seven days after your first live class. After that we refund on a pro rata basis for unattended weeks, minus a small administration fee.</p>"),
        ("What we commit to", "<p>Live classes on the schedule agreed. A native teacher. A recording within twenty four hours if you miss a class. Support inside one working day.</p>"),
        ("What we ask of you", "<p>To attend the live classes where possible, to complete the between lesson work honestly, and to conduct yourself in the classroom in a way that respects the teacher and the other students.</p>"),
        ("Conduct", "<p>We reserve the right to remove a student from a class or from the school for repeated conduct that harms the learning environment. In practice this is very rare.</p>"),
        ("Intellectual property", "<p>All course materials, recordings and syllabus documents are the intellectual property of eTeacher Group and are licensed to you for personal study only.</p>"),
        ("Recordings", "<p>Live classes are recorded for release to your cohort. Your video and audio may appear in the recording. Recordings are not distributed outside the cohort without explicit written consent.</p>"),
        ("Liability", "<p>We are liable for the delivery of the classes we have sold. We are not liable for indirect losses.</p>"),
        ("Governing law", "<p>These terms are governed by the laws of Israel. Any dispute will be resolved in the courts of Tel Aviv, unless local consumer law in your jurisdiction requires otherwise.</p>"),
    ]
    build_legal("terms", "Terms and conditions", lead, subs, "Last updated 11 September 2026. These are the terms on which we sell you a Club Italia course. Written in plain English, without hidden clauses.")


# ============================================================
# CAPSULES.HTML — 6 folds
# ============================================================
def build_capsules():
    hero = """
<section class="section-ink hero-page hero-100">
  <div class="hero-bg">
    <img src="assets/img/life-uffizi-hall.jpg" alt="" loading="lazy">
    <div class="hero-scrim"></div>
  </div>
  <div class="wrap hero-page-body">
    <span class="eyebrow eyebrow-gold">Culture Capsules</span>
    <h1 class="serif-display hero-h1">Six weeks<br><em>inside one Italian world</em></h1>
    <p class="lead">The Culture Capsules are short thematic courses. Six weeks, one theme, one faculty host. A single Italian world, taught deeply.</p>
    <div class="cta-row">
      <button class="btn btn-primary btn-lg" data-advisor type="button">Talk to an Advisor</button>
      <a class="btn btn-ghost btn-lg" href="culture.html">See the cultural syllabus</a>
    </div>
  </div>
</section>
"""
    fold2 = """
<section class="section-paper">
  <div class="wrap">
    <div class="editorial-2col">
      <div class="col-essay">
        <span class="eyebrow">A short course, seriously done</span>
        <h2 class="serif-display">Six weeks. One world.<br>One teacher who lives it.</h2>
      </div>
      <div class="col-essay">
        <p>The capsules are for two kinds of student. The first is an enrolled Club Italia learner already on the CEFR ladder, looking to add texture in a specific cultural direction. The second is a curious adult who wants to try Club Italia inside one theme before committing to a full level.</p>
        <p>Each capsule runs for six weeks. Each has one native teacher who hosts it. The pace is calmer than a CI level. The cultural material is deeper.</p>
      </div>
    </div>
  </div>
</section>
"""
    caps = [
        ("La Cucina","cap-food.jpg","Giulia Moretti · Bologna","Six weeks in the language of the Italian kitchen. Ingredients, market conversation, family recipes, and a live cooking session in week four.","pages/culture/cap-food.html"),
        ("L'Arte","cap-art.jpg","Chiara Bellini · Firenze","Six weeks in the language of Italian art. Gallery Italian, the wall label, and three centuries of painting from Giotto to Caravaggio.","pages/culture/cap-art.html"),
        ("L'Opera","cap-opera.jpg","Alessandro Ferri · Milano","Six weeks in the language of Italian opera. Libretti of Verdi and Puccini, opened line by line, taught by a former La Scala coach.","pages/culture/cap-opera.html"),
    ]
    cg = "".join(f'<a class="cap-card" href="{href}"><figure><img src="assets/img/{img}" alt="{n}" loading="lazy"></figure><div class="cap-body"><span class="cap-host">{host}</span><h3 class="serif-display">{n}</h3><p>{d}</p><span class="cap-more">See the capsule</span></div></a>' for n,img,host,d,href in caps)
    fold3 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Three capsules</span>
      <h2 class="serif-display">Currently running</h2>
    </div>
    <div class="cap-grid">{cg}
    </div>
  </div>
</section>
"""
    fold4 = """
<section class="section-travertine">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Why a capsule</span>
      <h2 class="serif-display">Four reasons students enrol in one</h2>
    </div>
    <div class="quad-grid">
      <div class="quad-cell"><h3>Depth over pace</h3><p>Six weeks in one cultural world lets a student go deeper than a general CI level can. That is the whole idea.</p></div>
      <div class="quad-cell"><h3>A themed cohort</h3><p>The people you meet in a capsule are there for the theme. Every conversation is inside it.</p></div>
      <div class="quad-cell"><h3>A specific teacher</h3><p>Each capsule has one host, chosen for the theme. You spend six weeks with the person who cares most about it.</p></div>
      <div class="quad-cell"><h3>A trial of the school</h3><p>If you have never studied with us, a capsule is the smallest complete Club Italia experience.</p></div>
    </div>
  </div>
</section>
"""
    testis = [
        {"n":"Diane Whitfield","loc":"Portland, Oregon","img":"assets/img/student-diane.jpg","t":"La Cucina changed how I cook","b":"I signed up thinking I would learn a bit of food vocabulary. I left with the whole vocabulary of an Italian home kitchen and three recipes I now make every month."},
        {"n":"Robert Marconi","loc":"Boston, Massachusetts","img":"assets/img/student-robert.jpg","t":"L'Opera was the reason I stayed","b":"I took the capsule for fun and enrolled in CI Intermedio the week after. Alessandro is a serious teacher and I wanted more of the school."},
        {"n":"Sarah Levine","loc":"Brooklyn, New York","img":"assets/img/student-sarah.jpg","t":"L'Arte with Chiara","b":"Six weeks on Renaissance Italian with a Florentine art teacher. I have never studied a subject I loved this much."},
    ]
    fold5 = tp_wall(testis).replace("What students actually say","What capsule students say")
    fold6 = final_cta_verona("Try Club Italia inside one theme.", "The next capsule cohort opens in October. Talk to an advisor to hold a seat.", "Talk to an Advisor")
    body = hero + fold2 + fold3 + fold4 + fold5 + fold6
    (ROOT/"capsules.html").write_text(page("Culture Capsules · Club Italia", "The Club Italia Culture Capsules. Six week thematic courses in Italian cuisine, art and opera, hosted by native faculty.", body))
    print("wrote capsules.html")


if __name__ == "__main__":
    build_about()
    build_eteacher()
    build_faq()
    build_sample()
    build_contact()
    build_blog()
    build_map()
    build_community()
    build_events()
    build_privacy()
    build_terms()
    build_capsules()
