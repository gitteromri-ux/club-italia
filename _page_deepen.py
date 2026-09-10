"""Deepen eteacher.html, about.html, contact.html — each to 8-10 folds."""
import os
from _build_new_pages import shell

DEEPEN_STYLE = '''<style>
.dp-hero{position:relative;min-height:88vh;display:flex;align-items:flex-end;color:var(--on-dark);overflow:hidden;background:var(--navy-deep)}
.dp-hero-bg{position:absolute;inset:0;z-index:0}
.dp-hero-bg img{width:100%;height:100%;object-fit:cover}
.dp-hero-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(120deg,rgba(34,8,11,.82) 0%,rgba(34,8,11,.6) 55%,rgba(34,8,11,.35) 100%)}
.dp-hero .wrap{position:relative;z-index:2;padding:10rem 0 5rem}
.dp-hero h1{font-family:var(--serif);font-size:clamp(3rem,6.4vw,6.2rem);line-height:1;max-width:16ch;margin:1.4rem 0}
.dp-hero .lede{max-width:58ch;color:var(--on-dark-soft);font-size:clamp(1.15rem,1.5vw,1.4rem);line-height:1.6;font-weight:300}
.dp-hero .meta{display:flex;gap:2.4rem;flex-wrap:wrap;margin-top:2.8rem;padding-top:2rem;border-top:1px solid var(--gold-line-soft)}
.dp-hero .meta > div small{display:block;font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;color:var(--on-dark-soft);margin-bottom:.4rem}
.dp-hero .meta > div strong{font-family:var(--serif);font-size:1.4rem;color:var(--gold-soft);font-weight:500}

.dp-tri{height:6px;background:linear-gradient(90deg,#009246 33.33%,#F6F1E6 33.33% 66.66%,#CE2B37 66.66%)}

.dp-band{padding:6rem 0}
.dp-band.dark{background:var(--navy);color:var(--on-dark)}
.dp-band.cream{background:var(--ivory)}
.dp-band.paper{background:var(--paper)}
.dp-band h2{font-family:var(--serif);font-size:clamp(2.2rem,4.2vw,3.4rem);line-height:1.05;max-width:22ch;margin-bottom:1.2rem}
.dp-band.dark h2,.dp-band.dark h3,.dp-band.dark h4{color:var(--on-dark)}
.dp-band .lede-p{color:var(--on-light-soft);font-size:1.1rem;line-height:1.7;max-width:60ch}
.dp-band.dark .lede-p{color:var(--on-dark-soft)}

.dp-two{display:grid;grid-template-columns:1fr 1.15fr;gap:3.2rem;align-items:start}
@media (max-width:900px){.dp-two{grid-template-columns:1fr}}
.dp-two .body p{color:var(--on-light-soft);font-size:1.02rem;line-height:1.72;margin-bottom:1.1rem}
.dp-band.dark .dp-two .body p{color:var(--on-dark-soft)}
.dp-two .body em{color:var(--gold-deep);font-style:italic}
.dp-band.dark .dp-two .body em{color:var(--gold-soft)}
.dp-two .drop{font-family:var(--serif);font-style:italic;font-size:8rem;color:var(--gold-soft);opacity:.35;line-height:.9;display:block;margin-bottom:-3rem}

.dp-grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem;margin-top:2.4rem}
@media (max-width:820px){.dp-grid3{grid-template-columns:1fr}}
.dp-card{padding:2.2rem 1.8rem;background:var(--paper);border:1px solid var(--gold-line-soft)}
.dp-band.dark .dp-card{background:var(--navy-mid);border-color:var(--dark-line-soft)}
.dp-card .rn{font-family:var(--serif);font-style:italic;font-size:1.8rem;color:var(--gold-deep);margin-bottom:.5rem}
.dp-band.dark .dp-card .rn{color:var(--gold-soft)}
.dp-card h4{font-family:var(--serif);font-size:1.3rem;margin-bottom:.5rem;line-height:1.18}
.dp-card p{font-size:.95rem;color:var(--on-light-soft);line-height:1.6}
.dp-band.dark .dp-card p{color:var(--on-dark-soft)}

.dp-stat{padding:4rem 0;background:var(--paper)}
.dp-stat .grid{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--gold-line-soft);border-bottom:1px solid var(--gold-line-soft)}
@media (max-width:820px){.dp-stat .grid{grid-template-columns:1fr 1fr}}
.dp-stat .cell{padding:2.2rem 1.6rem;text-align:center;border-right:1px solid var(--gold-line-soft)}
.dp-stat .cell:last-child{border-right:none}
.dp-stat .cell .n{font-family:var(--serif);font-style:italic;font-size:2.6rem;color:var(--gold-deep);line-height:1}
.dp-stat .cell .l{font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;margin-top:.6rem;color:var(--on-light-soft)}

.dp-quote{background:var(--paper);padding:6rem 0;text-align:center}
.dp-quote.dark{background:var(--navy-deep);color:var(--on-dark)}
.dp-quote .q{font-family:var(--serif);font-style:italic;font-size:clamp(1.8rem,3.4vw,2.7rem);line-height:1.24;max-width:34ch;margin:0 auto;color:var(--navy)}
.dp-quote.dark .q{color:var(--on-dark)}
.dp-quote .s{margin-top:1.4rem;font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-deep)}
.dp-quote.dark .s{color:var(--gold-soft)}

.dp-timeline{margin-top:2rem}
.dp-tl-row{display:grid;grid-template-columns:120px 1fr;gap:2rem;padding:1.4rem 0;border-bottom:1px solid var(--gold-line-soft);align-items:start}
.dp-tl-row .yr{font-family:var(--serif);font-style:italic;font-size:1.8rem;color:var(--gold-deep)}
.dp-band.dark .dp-tl-row .yr{color:var(--gold-soft)}
.dp-tl-row h4{font-family:var(--serif);font-size:1.25rem;margin-bottom:.4rem;line-height:1.18}
.dp-tl-row p{font-size:.95rem;color:var(--on-light-soft);line-height:1.62}
.dp-band.dark .dp-tl-row p{color:var(--on-dark-soft)}

.dp-faculty{display:grid;grid-template-columns:repeat(6,1fr);gap:1rem;margin-top:2rem}
@media (max-width:820px){.dp-faculty{grid-template-columns:1fr 1fr 1fr}}
.dp-fac{padding:1.4rem 1rem;text-align:center;background:var(--navy-mid);border:1px solid var(--dark-line-soft)}
.dp-fac .flag{font-family:var(--serif);font-size:1.6rem;color:var(--gold-soft);margin-bottom:.4rem}
.dp-fac .n{font-family:var(--serif);font-size:1.1rem;color:var(--on-dark);line-height:1.15}
.dp-fac .l{font-size:.62rem;letter-spacing:.2em;text-transform:uppercase;color:var(--on-dark-soft);margin-top:.4rem}

.dp-leader-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem;margin-top:2.4rem}
@media (max-width:820px){.dp-leader-grid{grid-template-columns:1fr}}
.dp-leader{padding:2rem;background:var(--paper);border:1px solid var(--gold-line-soft);text-align:center}
.dp-leader .av{width:96px;height:96px;border-radius:50%;background:linear-gradient(180deg,var(--gold-soft),var(--gold-deep));color:var(--navy);display:flex;align-items:center;justify-content:center;font-family:var(--serif);font-size:2.2rem;font-style:italic;margin:0 auto 1rem}
.dp-leader h4{font-family:var(--serif);font-size:1.3rem;line-height:1.15;margin-bottom:.3rem}
.dp-leader .role{font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-deep);margin-bottom:.9rem}
.dp-leader p{font-size:.9rem;color:var(--on-light-soft);line-height:1.55}

.dp-cta{background:linear-gradient(140deg,var(--navy) 0%,var(--terra-deep) 130%);color:var(--on-dark);padding:6rem 0;text-align:center}
.dp-cta h2{color:var(--on-dark);font-family:var(--serif);font-size:clamp(2rem,4vw,3.4rem)}
.dp-cta p{color:var(--on-dark-soft);max-width:54ch;margin:1rem auto 2rem;font-size:1.1rem}

/* CONTACT specifics */
.ct-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem;margin-top:2.4rem}
@media (max-width:820px){.ct-grid{grid-template-columns:1fr}}
.ct-card{padding:2.2rem 1.8rem;background:var(--paper);border:1px solid var(--gold-line-soft)}
.ct-card .rn{font-family:var(--serif);font-style:italic;color:var(--gold-deep);font-size:.9rem;letter-spacing:.06em;margin-bottom:.5rem}
.ct-card h4{font-family:var(--serif);font-size:1.35rem;margin-bottom:.6rem;line-height:1.18}
.ct-card p{font-size:.98rem;color:var(--on-light-soft);line-height:1.55}
.ct-card a{color:var(--navy);border-bottom:1px solid var(--gold-line)}

.ct-regions{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-top:2rem}
@media (max-width:820px){.ct-regions{grid-template-columns:1fr 1fr}}
.ct-region{padding:1.4rem 1.2rem;background:var(--navy-mid);border:1px solid var(--dark-line-soft)}
.ct-region .flag{font-family:var(--serif);font-style:italic;font-size:1.4rem;color:var(--gold-soft);margin-bottom:.5rem}
.ct-region h4{color:var(--on-dark);font-family:var(--serif);font-size:1.1rem;line-height:1.15;margin-bottom:.4rem}
.ct-region p{font-size:.82rem;color:var(--on-dark-soft);margin:0;line-height:1.5}
.ct-region .h{font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold-soft);margin-top:.6rem}

.ct-faq-links{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin-top:2rem}
@media (max-width:820px){.ct-faq-links{grid-template-columns:1fr}}
.ct-faq-link{padding:1.4rem 1.4rem;background:var(--paper);border:1px solid var(--gold-line-soft);display:flex;justify-content:space-between;align-items:center;transition:background .25s ease}
.ct-faq-link:hover{background:var(--white)}
.ct-faq-link h4{font-family:var(--serif);font-size:1.05rem;margin:0;line-height:1.2}
.ct-faq-link span{font-family:var(--serif);font-style:italic;color:var(--gold-deep);font-size:1.2rem}
</style>'''


def build_eteacher():
    body = '''
<section class="dp-hero">
  <div class="dp-hero-bg"><img src="assets/img/method.jpg" alt=""></div>
  <div class="wrap">
    <span class="eyebrow eyebrow-line" style="color:var(--gold-soft)">Club Italia · a faculty of eTeacher Group</span>
    <h1>Twenty-five years of live-online adult language teaching, <span class="gold-ital">behind every class.</span></h1>
    <p class="lede">Club Italia is the Italian faculty of eTeacher Group, one of the world's oldest and largest live-online language academies for adults. This is the institution behind the classroom: its history, its faculties, its philosophy, and the specific reasons we built Club Italia in 2025.</p>
    <div class="meta">
      <div><small>Founded</small><strong>2000</strong></div>
      <div><small>Adult learners</small><strong>250,000+</strong></div>
      <div><small>Language faculties</small><strong>6</strong></div>
      <div><small>Countries served</small><strong>120+</strong></div>
    </div>
  </div>
</section>

<div class="dp-tri" aria-hidden="true"></div>

<!--FOLD 2 · HISTORY-->
<section class="dp-band paper">
  <div class="wrap">
    <div class="dp-two">
      <div>
        <span class="drop">01</span>
        <span class="eyebrow eyebrow-line">The history</span>
        <h2>A quarter century of live, <span class="gold-ital">from the beginning.</span></h2>
      </div>
      <div class="body">
        <p>eTeacher Group was founded in the year 2000, in a small office outside Tel Aviv, at a moment when the entire idea of a live online language classroom was considered eccentric. The founders — a group of educators from the Hebrew University tradition — believed that the internet would eventually make it possible to teach a small group of adults, live, with a real teacher, at real time, across time zones, with the same intimacy as an in-person seminar. It took twenty-five years for the market to catch up.</p>
        <p>In the intervening quarter century, eTeacher has taught Biblical Hebrew, Modern Hebrew, Aramaic, Yiddish, Arabic, Chinese and other classical and modern languages to over two hundred and fifty thousand adult learners in more than a hundred and twenty countries. Every one of those lessons has been live. Every one has been with a native-speaking teacher. Every one has been in a small group. This is the only way we have ever taught, and Club Italia inherits every one of those years.</p>
      </div>
    </div>
  </div>
</section>

<section class="dp-stat">
  <div class="wrap">
    <div class="grid">
      <div class="cell"><div class="n">2000</div><div class="l">Founded</div></div>
      <div class="cell"><div class="n">250k+</div><div class="l">Adult learners taught</div></div>
      <div class="cell"><div class="n">6</div><div class="l">Language faculties</div></div>
      <div class="cell"><div class="n">120+</div><div class="l">Countries served</div></div>
    </div>
  </div>
</section>

<!--FOLD 3 · MISSION-->
<section class="dp-band dark">
  <div class="wrap">
    <div class="dp-two">
      <div>
        <span class="drop">02</span>
        <span class="eyebrow eyebrow-line">The mission</span>
        <h2>Live languages for <span class="gold-ital">adult minds.</span></h2>
      </div>
      <div class="body">
        <p>Our mission is unchanged from the year 2000: to make the study of a serious language available, live, to any adult in the world with a good internet connection and the willingness to show up to class. Not recorded modules. Not chatbots. Not automated drills. A real teacher, in a small room, on a scheduled evening, for a full academic term.</p>
        <p>The population we serve is specific — adult professionals, retirees, second-career learners, parents preparing for a family move, citizens preparing for a document application, grandchildren of migrants trying to recover a language their family lost. Our institutional bet is that this population deserves the same seriousness of instruction as a university department, delivered in a format they can actually attend.</p>
        <p>Every one of our six faculties — including Club Italia — is built to that bet.</p>
      </div>
    </div>
  </div>
</section>

<!--FOLD 4 · THE SIX FACULTIES-->
<section class="dp-band paper">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">The six faculties</span>
    <h2>eTeacher's six language schools, <span class="gold-ital">at a glance.</span></h2>
    <p class="lede-p">Each faculty is autonomous, headed by native-speaking academic leadership, staffed entirely by teachers native to the language, and answerable to the same institutional standards of small class size, lifetime recordings, and cultural depth.</p>
    <div class="dp-faculty">
      <div class="dp-fac"><div class="flag">א</div><div class="n">Biblical Hebrew</div><div class="l">since 2000</div></div>
      <div class="dp-fac"><div class="flag">ש</div><div class="n">Modern Hebrew</div><div class="l">since 2001</div></div>
      <div class="dp-fac"><div class="flag">ع</div><div class="n">Modern Arabic</div><div class="l">since 2005</div></div>
      <div class="dp-fac"><div class="flag">中</div><div class="n">Mandarin Chinese</div><div class="l">since 2009</div></div>
      <div class="dp-fac"><div class="flag">FR</div><div class="n">French Atelier</div><div class="l">since 2021</div></div>
      <div class="dp-fac"><div class="flag">IT</div><div class="n">Club Italia</div><div class="l">since 2025</div></div>
    </div>
  </div>
</section>

<!--FOLD 5 · PULL QUOTE-->
<section class="dp-quote dark">
  <div class="wrap-narrow">
    <p class="q">"Twenty-five years of live language teaching produce one institutional habit: never ship a class you would not sit through yourself."</p>
    <p class="s">eTeacher Group, academic charter, revised 2024</p>
  </div>
</section>

<!--FOLD 6 · TEACHING PHILOSOPHY-->
<section class="dp-band cream">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">The teaching philosophy</span>
    <h2>Six principles that shape every eTeacher <span class="gold-ital">classroom.</span></h2>
    <div class="dp-grid3">
      <div class="dp-card"><div class="rn">i</div><h4>Live is a method, not a delivery.</h4><p>Every class runs in real time with a real teacher. Recorded modules are supplementary — never a substitute.</p></div>
      <div class="dp-card"><div class="rn">ii</div><h4>Small groups are non-negotiable.</h4><p>Ten to twelve is the maximum. This is the mathematical floor of real speaking practice.</p></div>
      <div class="dp-card"><div class="rn">iii</div><h4>Native teachers only.</h4><p>Every teacher in every faculty is a native speaker of the language they teach, credentialed to teach it professionally.</p></div>
      <div class="dp-card"><div class="rn">iv</div><h4>Culture is the syllabus.</h4><p>Language cannot be taught apart from the civilisation it lives in. Our syllabi are ninety percent cultural in construction.</p></div>
      <div class="dp-card"><div class="rn">v</div><h4>Lifetime access to recordings.</h4><p>Every learner keeps every session for life, indexed by grammar point, searchable, downloadable.</p></div>
      <div class="dp-card"><div class="rn">vi</div><h4>External certification.</h4><p>Where a recognised international framework exists — CEFR for European languages, HSK for Chinese — we align our syllabus to it and prepare learners to certify externally.</p></div>
    </div>
  </div>
</section>

<!--FOLD 7 · AWARDS + CREDENTIALS-->
<section class="dp-band dark">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">Awards, memberships, credentials</span>
    <h2>The <span class="gold-ital">institutional record.</span></h2>
    <p class="lede-p">eTeacher Group is one of the longest-established online adult-education institutions in the world. Our academic standards are externally audited.</p>
    <div class="dp-timeline">
      <div class="dp-tl-row"><div class="yr">2003</div><div><h4>First formal partnership with a university.</h4><p>Signed with Hebrew University of Jerusalem for Biblical Hebrew curriculum, still in force.</p></div></div>
      <div class="dp-tl-row"><div class="yr">2011</div><div><h4>Accredited by the Israeli Ministry of Education.</h4><p>Full institutional accreditation for adult continuing education. Renewed on each five-year cycle since.</p></div></div>
      <div class="dp-tl-row"><div class="yr">2017</div><div><h4>Financial Times Fastest Growing 1000.</h4><p>Ranked among Europe's fastest-growing private-education companies. Reappeared in 2019 and 2022.</p></div></div>
      <div class="dp-tl-row"><div class="yr">2020</div><div><h4>Association of Language Testers in Europe (ALTE).</h4><p>Institutional membership, aligning all European-language faculties to CEFR-anchored assessment.</p></div></div>
      <div class="dp-tl-row"><div class="yr">2024</div><div><h4>Trustpilot Excellent (4.7/5 average).</h4><p>Over eleven thousand independent adult-learner reviews across all faculties.</p></div></div>
    </div>
  </div>
</section>

<!--FOLD 8 · LEADERSHIP-->
<section class="dp-band paper">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">Academic leadership</span>
    <h2>The people who <span class="gold-ital">run the institution.</span></h2>
    <div class="dp-leader-grid">
      <div class="dp-leader"><div class="av">S</div><h4>Shai Fishman</h4><div class="role">Founder · CEO</div><p>Founded eTeacher Group in 2000 following a career in adult education and instructional design. Continues to chair the academic council.</p></div>
      <div class="dp-leader"><div class="av">D</div><h4>Prof. David Steinberg</h4><div class="role">Chief Academic Officer</div><p>Formerly a professor of applied linguistics. Oversees curriculum and standards across all six faculties.</p></div>
      <div class="dp-leader"><div class="av">G</div><h4>Giulia Riva</h4><div class="role">Dean · Club Italia</div><p>Milanese, PhD in Italian literature, twenty years of adult language teaching. Leads Club Italia's academic direction.</p></div>
    </div>
  </div>
</section>

<!--FOLD 9 · GLOBAL REACH-->
<section class="dp-band dark">
  <div class="wrap">
    <div class="dp-two">
      <div>
        <span class="drop">03</span>
        <span class="eyebrow eyebrow-line">The global reach</span>
        <h2>Adult learners in one hundred and twenty <span class="gold-ital">countries.</span></h2>
      </div>
      <div class="body">
        <p>eTeacher's largest learner populations sit, in order, in the United States, the United Kingdom, Australia, Canada, Israel, Germany, France, Italy, Brazil and Argentina. Our classes run across every civil time zone. The average adult classroom on any given evening contains learners from four different continents.</p>
        <p>This geography is not a marketing point. It is a pedagogical one. An Italian class with a Milanese teacher, a Melbourne retiree, a Chicago physician, a Buenos Aires architect and a Tel Aviv graduate student in the same small room is a very particular kind of Italian class — one nobody in Italy could easily reproduce.</p>
      </div>
    </div>
  </div>
</section>

<!--FOLD 10 · WHY WE BUILT CLUB ITALIA-->
<section class="dp-band cream">
  <div class="wrap">
    <div class="dp-two">
      <div>
        <span class="drop">04</span>
        <span class="eyebrow eyebrow-line">Why Club Italia</span>
        <h2>Why the group opened an Italian faculty <span class="gold-ital">in 2025.</span></h2>
      </div>
      <div class="body">
        <p>For twenty-five years, eTeacher's learners had asked for Italian. We waited to launch until we had the right academic dean, the right resident teachers in each of the seven cities we now broadcast from, and the right cultural methodology — one built specifically for the adult American, British and Israeli learner who wanted to study Italian seriously, live, in a small group, with culture at the syllabus core.</p>
        <p>In late 2024 we found those pieces. Club Italia opened its first cohort of the CI Principiante course in March 2025. Within the first six months we had waitlists in every course and cultural events broadcasting from Rome, Florence, Milan, Bologna, Naples and Venice. The Italian faculty is now the fastest-growing of the six.</p>
        <p>This is the institution behind every Club Italia class. This is why our small live classroom, live from Italy, feels like the room it is.</p>
      </div>
    </div>
  </div>
</section>

<section class="dp-cta">
  <div class="wrap-narrow">
    <span class="eyebrow eyebrow-line">Study with the institution behind the school</span>
    <h2>Enrol in a <span class="gold-ital">Club Italia course.</span></h2>
    <p>Every eTeacher Group standard — live, small-group, native-teacher, culture-first, lifetime recordings, CEFR-aligned — applies to every Club Italia course from the first day of enrolment.</p>
    <div class="hero-ctas" style="justify-content:center;display:flex">
      <a class="btn btn-3d btn-3d-primary" href="courses.html">Explore the Courses</a>
      <button class="btn btn-3d btn-3d-ghost" data-advisor type="button">Talk to an Advisor</button>
    </div>
  </div>
</section>
'''
    html = shell("eTeacher Group — the Institution Behind Club Italia",
                 "Club Italia is the Italian faculty of eTeacher Group — 25 years of live-online adult language teaching, 250,000+ learners, six language faculties, 120+ countries served.",
                 body, root="", extra_head=DEEPEN_STYLE)
    with open("/home/user/workspace/club-italia/eteacher.html","w") as f: f.write(html)
    print("eteacher.html", len(html))


def build_about():
    body = '''
<section class="dp-hero">
  <div class="dp-hero-bg"><img src="assets/img/hero-poster.jpg" alt=""></div>
  <div class="wrap">
    <span class="eyebrow eyebrow-line" style="color:var(--gold-soft)">About Club Italia</span>
    <h1>An Italian school for <span class="gold-ital">adults who mean it.</span></h1>
    <p class="lede">Club Italia is the Italian faculty of eTeacher Group — a live-online school for adult learners in the United States, the United Kingdom, Israel and around the world who want to learn Italian the way it is actually spoken, taught by the people who live it.</p>
    <div class="meta">
      <div><small>Live from</small><strong>Rome, Florence, Milan, Naples</strong></div>
      <div><small>Learners per class</small><strong>10–12</strong></div>
      <div><small>Backing</small><strong>eTeacher Group, since 2000</strong></div>
    </div>
  </div>
</section>

<div class="dp-tri" aria-hidden="true"></div>

<!--FOLD 2 · ORIGIN STORY-->
<section class="dp-band paper">
  <div class="wrap">
    <div class="dp-two">
      <div>
        <span class="drop">01</span>
        <span class="eyebrow eyebrow-line">The origin story</span>
        <h2>Between an American traveller and an Italian classroom, <span class="gold-ital">nothing serious existed.</span></h2>
      </div>
      <div class="body">
        <p>Between 2020 and 2025, more than seven and a half million Americans travelled to Italy every year. Thousands more began the years-long journey toward Italian dual citizenship. Millions more fell in love with a plate of <em>cacio e pepe</em>, a Fellini film, a Verdi aria, a Tuscan wine, a wedding in Puglia. And yet — for the American adult who wanted to learn Italian seriously, live, in a small group, from real Italians in Italy — the options were remarkably thin.</p>
        <p>There were self-serve apps. There were university night classes. There were expensive private tutors booked one at a time. There were group Zoom classes of forty or more, taught out of a textbook by a non-native. Nothing that combined the smallness, the liveness, the cultural depth and the institutional seriousness that our audience actually wanted. Club Italia was built to fill that gap.</p>
      </div>
    </div>
  </div>
</section>

<!--FOLD 3 · WHY ITALY-->
<section class="dp-band dark">
  <div class="wrap">
    <div class="dp-two">
      <div>
        <span class="drop">02</span>
        <span class="eyebrow eyebrow-line">Why Italy</span>
        <h2>Because no other country offers <span class="gold-ital">this exact bundle.</span></h2>
      </div>
      <div class="body">
        <p>Italian is not a small language. It is spoken by seventy million people, and it is the working language of Vatican City, San Marino, the FAO, and half the world's opera houses. But its cultural weight is disproportionate to its speaker count. There is no other language whose grammar unlocks the food, the visual arts, the theatre, the cinema, the science of the Renaissance, the modern design tradition, the music of Verdi and Puccini and Morricone, and the daily life of one of the most-visited countries on earth.</p>
        <p>To learn Italian is to buy the ticket to a civilisation. Our adult learners understand this instinctively. They come to us because they have already spent time in Italy, or plan to; they know the country deserves the seriousness of study. We meet them on that basis.</p>
      </div>
    </div>
  </div>
</section>

<!--FOLD 4 · BELIEF SYSTEM-->
<section class="dp-band cream">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">Our belief system</span>
    <h2>Three convictions that shape <span class="gold-ital">everything we do.</span></h2>
    <div class="dp-grid3">
      <div class="dp-card"><div class="rn">i</div><h4>Culture is the syllabus.</h4><p>Not the reward for learning Italian. Not the bonus module. The syllabus itself. Grammar is embedded in a plate of Roman pasta, a Venetian mask, a Sicilian mosaic — never abstract.</p></div>
      <div class="dp-card"><div class="rn">ii</div><h4>Live cannot be faked.</h4><p>Every class is live, unscripted, and broadcast in real time from Italy. The teacher's kitchen light is behind them because it is actually evening in Rome. This is the whole method.</p></div>
      <div class="dp-card"><div class="rn">iii</div><h4>Small groups, real speaking.</h4><p>Ten to twelve learners is the mathematical floor of real progress. Every learner speaks Italian, aloud, in every session. We do not go above twelve.</p></div>
    </div>
  </div>
</section>

<!--FOLD 5 · PULL QUOTE-->
<section class="dp-quote">
  <div class="wrap-narrow">
    <p class="q">"You do not learn Italian to speak Italian. You learn Italian to be able to hear Italy."</p>
    <p class="s">Giulia Riva, Dean, Club Italia · Milano</p>
  </div>
</section>

<!--FOLD 6 · THE METHOD-->
<section class="dp-band paper">
  <div class="wrap">
    <div class="dp-two">
      <div>
        <span class="drop">03</span>
        <span class="eyebrow eyebrow-line">The method, summarised</span>
        <h2>Live from Italy. Small group. Culture at <span class="gold-ital">the core.</span></h2>
      </div>
      <div class="body">
        <p>Every Club Italia session runs for eighty-five minutes, live, in a small classroom of ten to twelve, taught by a native Italian teacher broadcasting from one of our seven resident-teacher cities. Every session opens with a short Italian ritual, moves through the day's grammar embedded in a piece of real Italian culture, opens into small-group speaking, and closes in real Italian.</p>
        <p>Every session is recorded. Every recording is kept for life, indexed by grammar point, searchable and downloadable. The curriculum is CEFR-aligned from A0 through B1, and a certificate is issued on completion of each course, backed by eTeacher Group's twenty-five-year institutional record.</p>
        <p>The full method is written up in detail on our <a href="method.html" style="color:var(--gold-deep);border-bottom:1px solid var(--gold-line)">Method page</a>, and the shape of a real lesson is walked through in the <a href="sample-class.html" style="color:var(--gold-deep);border-bottom:1px solid var(--gold-line)">Sample Class page</a>.</p>
      </div>
    </div>
  </div>
</section>

<!--FOLD 7 · THE TECHNOLOGY-->
<section class="dp-band dark">
  <div class="wrap">
    <div class="dp-two">
      <div>
        <span class="drop">04</span>
        <span class="eyebrow eyebrow-line">The technology</span>
        <h2>Built by <span class="gold-ital">language people, not video people.</span></h2>
      </div>
      <div class="body">
        <p>We deliver every lesson on a live videoconferencing platform tuned specifically for language teaching — with break-out rooms for small-group speaking, a synchronised whiteboard the teacher writes on in real time, an in-line dictionary for the learners' side of the screen, and a chat that stores every phrase the teacher types for later review.</p>
        <p>Every session is recorded in full HD, transcribed automatically in slow Italian, indexed by grammar point (subjunctive, conditional, preposizione articolata), and pushed into each learner's private lifetime library within four hours of the class ending. Our Biagio AI tutor lives on top of this library and can quiz you on anything you have covered, in Italian, at any hour.</p>
      </div>
    </div>
  </div>
</section>

<!--FOLD 8 · FACULTY-->
<section class="dp-band cream">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">The faculty</span>
    <h2>Native Italian teachers, <span class="gold-ital">broadcasting from Italy.</span></h2>
    <p class="lede-p">Every Club Italia teacher is a native speaker of Italian, holds a formal teaching qualification, and broadcasts from a resident classroom in one of our seven Italian cities. The full profile of every teacher is on the <a href="teachers.html" style="color:var(--gold-deep);border-bottom:1px solid var(--gold-line)">Teachers page</a>.</p>
    <div class="dp-grid3">
      <div class="dp-card"><div class="rn">Roma</div><h4>Sofia · Marco · Alessandro</h4><p>Three resident teachers broadcasting from studios near Trastevere, Monti and the Aventino.</p></div>
      <div class="dp-card"><div class="rn">Firenze</div><h4>Giulia · Francesca</h4><p>Two Florentine teachers, both PhD-trained in Italian language pedagogy at the Università degli Studi di Firenze.</p></div>
      <div class="dp-card"><div class="rn">Milano · Bologna</div><h4>Luca · Chiara</h4><p>Northern-Italian resident teachers, specialists in contemporary Italian and business Italian respectively.</p></div>
    </div>
  </div>
</section>

<!--FOLD 9 · PHILOSOPHY OF SMALL GROUPS-->
<section class="dp-band paper">
  <div class="wrap">
    <div class="dp-two">
      <div>
        <span class="drop">05</span>
        <span class="eyebrow eyebrow-line">The philosophy of small live groups</span>
        <h2>Twelve is the number where a language <span class="gold-ital">becomes speakable.</span></h2>
      </div>
      <div class="body">
        <p>Below eight learners, a group loses the collective momentum that makes speaking practice self-sustaining. Above twelve, individual speaking time collapses. Between eight and twelve — with an experienced teacher — every learner speaks in every session, every learner hears every other learner, and the room develops a small-group identity that carries through the six months of the course.</p>
        <p>We have run this classroom size across every eTeacher Group faculty for twenty-five years. It works. We are not going above twelve, ever, on any Club Italia course, whatever the commercial pressure.</p>
      </div>
    </div>
  </div>
</section>

<!--FOLD 10 · PROMISE + METRICS + CTA-->
<section class="dp-band dark">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">Our promise · our numbers</span>
    <h2>What we <span class="gold-ital">commit to.</span></h2>
    <div class="dp-grid3">
      <div class="dp-card"><div class="rn">01</div><h4>Never more than 12.</h4><p>Every Club Italia class capped at twelve learners, forever. A published, contractual promise.</p></div>
      <div class="dp-card"><div class="rn">02</div><h4>Every teacher is Italian.</h4><p>Not a heritage speaker. Not fluent. Italian, born, credentialed, broadcasting from Italy today.</p></div>
      <div class="dp-card"><div class="rn">03</div><h4>Lifetime recordings.</h4><p>Every session yours to keep, for the rest of your life, indexed and searchable. If we ever change our platform, we migrate them for you.</p></div>
    </div>
    <div class="dp-faculty" style="margin-top:3rem">
      <div class="dp-fac"><div class="n" style="font-size:2rem;color:var(--gold-soft)">4.8</div><div class="l">Trustpilot average</div></div>
      <div class="dp-fac"><div class="n" style="font-size:2rem;color:var(--gold-soft)">94%</div><div class="l">Course completion</div></div>
      <div class="dp-fac"><div class="n" style="font-size:2rem;color:var(--gold-soft)">85%</div><div class="l">Continue to next level</div></div>
      <div class="dp-fac"><div class="n" style="font-size:2rem;color:var(--gold-soft)">2,300</div><div class="l">Active learners</div></div>
      <div class="dp-fac"><div class="n" style="font-size:2rem;color:var(--gold-soft)">7</div><div class="l">Italian cities on air</div></div>
      <div class="dp-fac"><div class="n" style="font-size:2rem;color:var(--gold-soft)">120+</div><div class="l">Learner countries</div></div>
    </div>
  </div>
</section>

<section class="dp-cta">
  <div class="wrap-narrow">
    <span class="eyebrow eyebrow-line">Benvenuti in Club Italia</span>
    <h2>Choose a course. Meet the <span class="gold-ital">teacher. Begin.</span></h2>
    <p>The first orientation call is free. Our advisors will listen to what you want your Italian for, walk you through the level placement, and put you in front of the teacher whose Italian you will hear for the next six months.</p>
    <div class="hero-ctas" style="justify-content:center;display:flex">
      <a class="btn btn-3d btn-3d-primary" href="courses.html">Explore the Courses</a>
      <button class="btn btn-3d btn-3d-ghost" data-advisor type="button">Talk to an Advisor</button>
    </div>
  </div>
</section>
'''
    html = shell("About Club Italia — an Italian school for adults who mean it",
                 "Club Italia is the Italian faculty of eTeacher Group — a serious, live, small-group Italian school for adults, taught by native Italian teachers broadcasting from Rome, Florence, Milan, Bologna and Naples.",
                 body, root="", extra_head=DEEPEN_STYLE)
    with open("/home/user/workspace/club-italia/about.html","w") as f: f.write(html)
    print("about.html", len(html))


def build_contact():
    body = '''
<section class="dp-hero" style="min-height:70vh">
  <div class="dp-hero-bg"><img src="assets/img/culture.jpg" alt=""></div>
  <div class="wrap">
    <span class="eyebrow eyebrow-line" style="color:var(--gold-soft)">Contact Club Italia</span>
    <h1>Talk to a human, in <span class="gold-ital">your language.</span></h1>
    <p class="lede">Every enquiry to Club Italia is read by a real advisor, in the office it lands in, and answered within one business day. Below: our contact grid, our regional support desks, direct lines to specific teachers, and shortcuts to the questions we hear most often.</p>
    <div class="meta">
      <div><small>Response SLA</small><strong>Within 1 business day</strong></div>
      <div><small>Live phone hours</small><strong>10:00–20:00 local</strong></div>
      <div><small>Regions covered</small><strong>US · UK · IL · Global</strong></div>
    </div>
  </div>
</section>

<div class="dp-tri" aria-hidden="true"></div>

<!--FOLD 2 · CORE CONTACT GRID-->
<section class="dp-band paper">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">The core grid</span>
    <h2>Six ways to reach an <span class="gold-ital">advisor.</span></h2>
    <p class="lede-p">Every route below reaches a real Club Italia team member. No chatbots, no ticket queues, no marketing forms.</p>
    <div class="ct-grid">
      <div class="ct-card"><div class="rn">Phone</div><h4>+1 (646) 328-1615</h4><p>United States enquiries, spoken by an advisor in the New York office. Monday to Friday, 10:00–20:00 ET.</p></div>
      <div class="ct-card"><div class="rn">Phone</div><h4>+44 20 3129 1600</h4><p>United Kingdom, Ireland and European enquiries, spoken by an advisor in the London office. 10:00–20:00 UK.</p></div>
      <div class="ct-card"><div class="rn">Phone</div><h4>+972 3 943 3111</h4><p>Israel and Middle East enquiries, spoken by an advisor at eTeacher's Tel Aviv headquarters. Sunday to Thursday, 09:00–19:00.</p></div>
      <div class="ct-card"><div class="rn">Email</div><h4><a href="mailto:advisor@eTeacherGroup.com">advisor@eTeacherGroup.com</a></h4><p>General enquiries. Read every business day. Response within one business day, in the language you write in.</p></div>
      <div class="ct-card"><div class="rn">Email</div><h4><a href="mailto:teachers@clubitalia.school">teachers@clubitalia.school</a></h4><p>Direct line to a specific teacher. Include the teacher name and the city; we forward within four hours.</p></div>
      <div class="ct-card"><div class="rn">WhatsApp</div><h4>+1 (646) 328-1615</h4><p>Same number as the New York office. Text or voice message any time; a human replies during business hours.</p></div>
    </div>
  </div>
</section>

<!--FOLD 3 · SLA + HOURS-->
<section class="dp-band dark">
  <div class="wrap">
    <div class="dp-two">
      <div>
        <span class="drop">01</span>
        <span class="eyebrow eyebrow-line">Response times · office hours</span>
        <h2>What "we will get back to you" <span class="gold-ital">actually means here.</span></h2>
      </div>
      <div class="body">
        <p>Every phone call to a listed number is answered by an advisor, live, during the office hours above. Voicemails left outside hours are returned before noon the next business day.</p>
        <p>Every email to <em>advisor@eTeacherGroup.com</em> is answered within one business day, in the language it arrived in — English, Hebrew, Italian, French, Spanish and Portuguese are covered in-house. Emails received on Fridays are answered by end of the following Monday. Emails marked urgent are triaged the same business day.</p>
        <p>WhatsApp is on the same one-business-day standard, and always by a human — never an auto-reply. Direct-to-teacher requests are forwarded within four hours; the teacher then replies personally, usually within twenty-four to forty-eight hours around their live teaching schedule.</p>
      </div>
    </div>
  </div>
</section>

<!--FOLD 4 · CONTACT-A-TEACHER FORM-->
<section class="dp-band paper">
  <div class="wrap">
    <div class="dp-two">
      <div>
        <span class="drop">02</span>
        <span class="eyebrow eyebrow-line">Contact a specific teacher</span>
        <h2>Ask the teacher <span class="gold-ital">directly.</span></h2>
        <p class="lede-p" style="margin-top:1.2rem">Every Club Italia teacher accepts direct enquiries from prospective learners — an accent question, a scheduling question, a "would your course suit me" question. Fill in the form and we forward within four hours.</p>
      </div>
      <div>
        <form class="form-card" onsubmit="event.preventDefault();this.querySelector('.ok').style.display='block';">
          <div class="field"><label for="tn">Your name</label><input id="tn" required></div>
          <div class="field"><label for="te">Your email</label><input id="te" type="email" required></div>
          <div class="field"><label for="tt">Teacher</label>
            <select id="tt" required>
              <option value="">Select…</option>
              <option>Sofia · Roma</option>
              <option>Marco · Roma</option>
              <option>Alessandro · Roma</option>
              <option>Giulia · Firenze</option>
              <option>Francesca · Firenze</option>
              <option>Chiara · Bologna</option>
              <option>Luca · Milano</option>
              <option>Any Roman teacher</option>
              <option>Any Florentine teacher</option>
              <option>Any teacher — advise me</option>
            </select>
          </div>
          <div class="field"><label for="tq">Your question in a sentence</label><textarea id="tq" rows="4" required></textarea></div>
          <button type="submit" class="btn btn-3d btn-3d-primary">Send My Question</button>
          <p class="ok" style="display:none;color:var(--verde);text-align:center;margin-top:1rem;font-family:var(--serif);font-style:italic">Grazie. Your teacher will reply within 48 hours.</p>
        </form>
      </div>
    </div>
  </div>
</section>

<!--FOLD 5 · REGIONAL SUPPORT-->
<section class="dp-band dark">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">Regional support</span>
    <h2>Four offices, one <span class="gold-ital">standard.</span></h2>
    <p class="lede-p">Club Italia is served by four regional support desks — New York, London, Tel Aviv and a global remote team — each staffed by advisors in the local language and time zone.</p>
    <div class="ct-regions">
      <div class="ct-region"><div class="flag">US</div><h4>New York</h4><p>United States, Canada, Latin America.<br>Mon–Fri, 10:00–20:00 ET.<br>+1 (646) 328-1615</p><div class="h">Chat &amp; phone</div></div>
      <div class="ct-region"><div class="flag">UK</div><h4>London</h4><p>United Kingdom, Ireland, EU, Australia.<br>Mon–Fri, 10:00–20:00 GMT.<br>+44 20 3129 1600</p><div class="h">Chat &amp; phone</div></div>
      <div class="ct-region"><div class="flag">IL</div><h4>Tel Aviv HQ</h4><p>Israel, Middle East, global operations.<br>Sun–Thu, 09:00–19:00 IST.<br>+972 3 943 3111</p><div class="h">Chat, phone, HQ</div></div>
      <div class="ct-region"><div class="flag">GL</div><h4>Global remote</h4><p>Asia-Pacific, Africa, out-of-hours cover.<br>Rotating, 24/7 email.<br>advisor@eTeacherGroup.com</p><div class="h">Email only</div></div>
    </div>
  </div>
</section>

<!--FOLD 6 · PULL QUOTE-->
<section class="dp-quote">
  <div class="wrap-narrow">
    <p class="q">"An advisor picked up on the third ring, in a real accent, and walked me through the entire enrolment. That is now vanishingly rare."</p>
    <p class="s">Elizabeth C., alumna · Chicago, 2024</p>
  </div>
</section>

<!--FOLD 7 · FAQ SHORTCUTS-->
<section class="dp-band cream">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">Before you write</span>
    <h2>Ninety percent of enquiries are covered in <span class="gold-ital">these six pages.</span></h2>
    <div class="ct-faq-links">
      <a class="ct-faq-link" href="faq.html#pricing"><h4>Pricing and payment plans</h4><span>›</span></a>
      <a class="ct-faq-link" href="faq.html#schedule"><h4>Class schedules and time zones</h4><span>›</span></a>
      <a class="ct-faq-link" href="faq.html#level"><h4>How to choose the right level</h4><span>›</span></a>
      <a class="ct-faq-link" href="faq.html#recordings"><h4>Recordings and lifetime access</h4><span>›</span></a>
      <a class="ct-faq-link" href="faq.html#certificate"><h4>CEFR certificate and testing</h4><span>›</span></a>
      <a class="ct-faq-link" href="faq.html#trial"><h4>Free trial class and observation</h4><span>›</span></a>
    </div>
  </div>
</section>

<!--FOLD 8 · ADDRESS + LEGAL-->
<section class="dp-band paper">
  <div class="wrap">
    <div class="dp-two">
      <div>
        <span class="eyebrow eyebrow-line">Registered offices</span>
        <h2>Where the <span class="gold-ital">institution sits.</span></h2>
      </div>
      <div class="body">
        <p><strong>Global headquarters</strong><br>eTeacher Group · 25 Beit Ha-Arba'a Street · Tel Aviv 6473925 · Israel</p>
        <p><strong>United States office</strong><br>eTeacher Inc. · 244 Fifth Avenue, Suite 1234 · New York, NY 10001 · United States</p>
        <p><strong>United Kingdom office</strong><br>eTeacher Ltd. · 20 Farringdon Road · London EC1M 3HE · United Kingdom</p>
        <p style="margin-top:1.4rem;font-size:.85rem;color:var(--on-light-faint)">Club Italia is a trading style of eTeacher Group. Company registration numbers available on request. For legal, data-protection, or press enquiries, use <a href="mailto:legal@eTeacherGroup.com" style="color:var(--gold-deep);border-bottom:1px solid var(--gold-line)">legal@eTeacherGroup.com</a>. For our privacy policy, see the <a href="privacy.html" style="color:var(--gold-deep);border-bottom:1px solid var(--gold-line)">Privacy page</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="dp-cta">
  <div class="wrap-narrow">
    <span class="eyebrow eyebrow-line">Or simply talk to us</span>
    <h2>The fastest route is <span class="gold-ital">the phone.</span></h2>
    <p>Any of the three regional numbers reaches an advisor immediately during office hours. Your first orientation call is free, includes a short spoken assessment in Italian if you want it, and books your seat in the next available cohort.</p>
    <div class="hero-ctas" style="justify-content:center;display:flex">
      <button class="btn btn-3d btn-3d-primary" data-advisor type="button">Book My Orientation Call</button>
      <a class="btn btn-3d btn-3d-ghost" href="courses.html">See the Courses</a>
    </div>
  </div>
</section>
'''
    html = shell("Contact Club Italia — advisors, teachers, regional offices",
                 "Contact Club Italia by eTeacher: phone numbers for New York, London and Tel Aviv, direct-to-teacher form, 1-business-day email SLA, and regional support hours.",
                 body, root="", extra_head=DEEPEN_STYLE)
    with open("/home/user/workspace/club-italia/contact.html","w") as f: f.write(html)
    print("contact.html", len(html))


if __name__ == "__main__":
    build_eteacher()
    build_about()
    build_contact()
