"""Build the remaining pages: events index, community, sample-class, eteacher, about, contact."""
import os
from _build_new_pages import shell

# ================= EVENTS INDEX =================
EVENTS_INDEX_STYLE = '''<style>
.evx-hero{min-height:78vh;position:relative;display:flex;align-items:flex-end;color:var(--on-dark);overflow:hidden;background:var(--navy-deep)}
.evx-hero-bg{position:absolute;inset:0;z-index:0}
.evx-hero-bg img{width:100%;height:100%;object-fit:cover}
.evx-hero-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(34,8,11,.45),rgba(34,8,11,.92))}
.evx-hero .wrap{position:relative;z-index:2;padding:10rem 0 4rem}
.evx-hero h1{font-family:var(--serif);font-weight:500;font-size:clamp(3rem,6vw,5.8rem);line-height:1.02;max-width:18ch;margin:1.4rem 0}
.evx-hero .lede{max-width:60ch;color:var(--on-dark-soft);font-weight:300;font-size:clamp(1.1rem,1.4vw,1.35rem);line-height:1.62}

.evx-tri{height:6px;background:linear-gradient(90deg,#009246 33.33%,#F6F1E6 33.33% 66.66%,#CE2B37 66.66%)}

.evx-grid{padding:6rem 0;background:var(--paper)}
.evx-cards{display:grid;grid-template-columns:1fr;gap:2.4rem;margin-top:3rem}
.evx-card{display:grid;grid-template-columns:1.05fr 1fr;background:var(--white);border:1px solid var(--gold-line-soft);overflow:hidden;box-shadow:0 20px 40px -30px rgba(58,14,18,.4);transition:box-shadow .35s ease,transform .35s ease}
.evx-card:hover{box-shadow:0 30px 60px -30px rgba(58,14,18,.45);transform:translateY(-3px)}
.evx-card:nth-child(even){grid-template-columns:1fr 1.05fr}
.evx-card:nth-child(even) .evx-media{order:2}
@media (max-width:900px){.evx-card,.evx-card:nth-child(even){grid-template-columns:1fr}.evx-card:nth-child(even) .evx-media{order:0}}
.evx-media{aspect-ratio:5/4;overflow:hidden;background:var(--navy);position:relative}
.evx-media img{width:100%;height:100%;object-fit:cover;transition:transform 1.1s ease}
.evx-card:hover .evx-media img{transform:scale(1.05)}
.evx-media .colors{position:absolute;top:0;left:0;right:0;height:5px}
.evx-body{padding:3rem 2.8rem;display:flex;flex-direction:column}
.evx-date{font-family:var(--serif);font-style:italic;font-size:1.35rem;color:var(--gold-deep);margin-bottom:.6rem}
.evx-body h2{font-family:var(--serif);font-size:2.4rem;line-height:1.06;margin-bottom:.6rem}
.evx-body .place{font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;color:var(--on-light-faint);margin-bottom:1.2rem}
.evx-body p{color:var(--on-light-soft);line-height:1.7;margin-bottom:1.4rem;font-size:1rem}
.evx-body .go{margin-top:auto;padding-top:1rem;border-top:1px solid var(--light-line);display:flex;justify-content:space-between;align-items:center}
.evx-body .go a{font-family:var(--serif);font-style:italic;color:var(--gold-deep);font-size:1.2rem}
.evx-body .go a::after{content:" ›";transition:transform .3s}
.evx-body .go small{font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:var(--on-light-faint)}

.evx-cal{background:var(--navy);color:var(--on-dark);padding:6rem 0}
.evx-cal h2{color:var(--on-dark);font-family:var(--serif);font-size:clamp(2rem,3.6vw,3.2rem);margin-bottom:1rem}
.evx-cal p{color:var(--on-dark-soft);line-height:1.62;margin-bottom:1.4rem;font-size:1.05rem}
.evx-cal .cal-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.2rem;margin-top:2.4rem}
@media (max-width:820px){.evx-cal .cal-grid{grid-template-columns:1fr 1fr}}
.evx-cal .cal-row{padding:1.6rem 1.4rem;background:var(--navy-mid);border:1px solid var(--dark-line-soft)}
.evx-cal .cal-row .m{font-family:var(--serif);font-style:italic;font-size:1.6rem;color:var(--gold-soft);margin-bottom:.5rem;line-height:1}
.evx-cal .cal-row h4{font-family:var(--serif);font-size:1.1rem;color:var(--on-dark);margin-bottom:.3rem;line-height:1.2}
.evx-cal .cal-row p{font-size:.82rem;color:var(--on-dark-soft);margin:0}

.evx-quote{background:var(--paper);padding:6rem 0;text-align:center}
.evx-quote .q{font-family:var(--serif);font-style:italic;font-size:clamp(1.8rem,3.4vw,2.8rem);line-height:1.22;max-width:34ch;margin:0 auto;color:var(--navy)}
.evx-quote .s{margin-top:1.4rem;font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-deep)}

.evx-cta{background:linear-gradient(140deg,var(--navy) 0%,var(--terra-deep) 130%);color:var(--on-dark);padding:6rem 0;text-align:center}
.evx-cta h2{color:var(--on-dark);font-family:var(--serif);font-size:clamp(2rem,4vw,3.4rem)}
.evx-cta p{color:var(--on-dark-soft);max-width:54ch;margin:1rem auto 2rem;font-size:1.1rem}
</style>'''

def build_events_index():
    events = [
      {"slug":"festa-repubblica","name":"Festa della Repubblica","date":"2 giugno · every year","place":"Roma · Via dei Fori Imperiali","img":"assets/img/pillar-tradition.jpg","tri":"linear-gradient(90deg,#009246 33.33%,#F6F1E6 33.33% 66.66%,#CE2B37 66.66%)",
       "essay":"Italy's national day. Every second of June since 1946, the Republic celebrates the referendum that abolished the monarchy — the parade at the Fori Imperiali, the Frecce Tricolori over the Altare della Patria, the Quirinale gardens open to the public. A single day of civic memory shared across the whole peninsula."},
      {"slug":"carnevale","name":"Il Carnevale di Venezia","date":"February · ten days before Lent","place":"Venezia · Piazza San Marco","img":"assets/img/pillar-tradition.jpg","tri":"linear-gradient(90deg,#22080B 33.33%,#C9A24B 33.33% 66.66%,#F6F1E6 66.66%)",
       "essay":"Ten days of masked baroque theatre across the Venetian lagoon. The Flight of the Angel from the Campanile, the private balls at Ca' Pisani-Moretta, the frittelle in every pastry window, the six historical masks — bautà, moretta, medico della peste, gnaga, volto, Colombina. Venice returns to the eighteenth century for a fortnight every winter."},
      {"slug":"palio-siena","name":"Il Palio di Siena","date":"2 luglio · 16 agosto","place":"Siena · Piazza del Campo","img":"assets/img/pillar-tradition.jpg","tri":"linear-gradient(90deg,#B65538 33.33%,#F6F1E6 33.33% 66.66%,#22080B 66.66%)",
       "essay":"Ninety seconds of bareback horse racing around a shell-shaped square in the middle of Tuscany. Seventeen medieval contrade, ten horses, three laps of the tufo, a painted silk banner. A race whose preparation lasts a lifetime — twice a year, on the second of July and the sixteenth of August."}
    ]
    cards = ""
    for e in events:
        cards += f'''
      <article class="evx-card">
        <div class="evx-media">
          <div class="colors" style="background:{e['tri']}"></div>
          <img src="{e['img']}" alt="{e['name']}">
        </div>
        <div class="evx-body">
          <p class="evx-date">{e['date']}</p>
          <h2>{e['name']}</h2>
          <p class="place">{e['place']}</p>
          <p>{e['essay']}</p>
          <div class="go">
            <a href="pages/events/{e['slug']}.html">Read the essay</a>
            <small>Cultural file · 10 folds</small>
          </div>
        </div>
      </article>'''

    cal_rows = ""
    for m,evt,pl in [
      ("Feb","Il Carnevale","Venezia · 10 days"),
      ("Apr","La Liberazione","Nazionale · 25 April"),
      ("May","Festa dei Ceri","Gubbio · 15 May"),
      ("Jun","Festa della Repubblica","Roma · 2 June"),
      ("Jul","Il Palio di Provenzano","Siena · 2 July"),
      ("Aug","Il Palio dell'Assunta","Siena · 16 August"),
      ("Sep","Regata Storica","Venezia · first Sunday"),
      ("Dec","La Prima della Scala","Milano · 7 December")
    ]:
        cal_rows += f'<div class="cal-row"><p class="m">{m}</p><h4>{evt}</h4><p>{pl}</p></div>'

    body = f'''
<section class="evx-hero">
  <div class="evx-hero-bg"><img src="assets/img/pillar-tradition.jpg" alt=""></div>
  <div class="wrap">
    <span class="eyebrow eyebrow-line" style="color:var(--gold-soft)">The Club Italia cultural calendar</span>
    <h1>The great days of the <span class="gold-ital">Italian year.</span></h1>
    <p class="lede">Every Club Italia course is anchored to Italy's living cultural calendar. National holidays, regional festivals, historical anniversaries, saints' days that stop entire towns for a weekend. Our teachers broadcast from the piazza on the day itself — the language, in situ, unscripted, in real time.</p>
  </div>
</section>

<div class="evx-tri" aria-hidden="true"></div>

<section class="evx-grid">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow eyebrow-line">Featured event essays</span>
      <h2 class="display-md">Three full cultural files, <span class="gold-ital">to begin with.</span></h2>
      <p class="lead">Each essay carries the history, the traditions, the recipe of the day, the vocabulary a learner will hear, and a live broadcast pass.</p>
    </div>
    <div class="evx-cards">
      {cards}
    </div>
  </div>
</section>

<section class="evx-quote">
  <div class="wrap-narrow">
    <p class="q">"In Italy you do not need a museum. You need a calendar."</p>
    <p class="s">Attributed to the historian Fernand Braudel</p>
  </div>
</section>

<section class="evx-cal">
  <div class="wrap">
    <div style="max-width:60ch">
      <span class="eyebrow eyebrow-line">The full Italian year</span>
      <h2>A short calendar of the <span class="gold-ital">Italian holidays.</span></h2>
      <p>Beyond the three featured cultural files, our academic year weaves in twenty-two further national and regional dates. New event essays are added every term, following the Italian holiday calendar.</p>
    </div>
    <div class="cal-grid">{cal_rows}</div>
  </div>
</section>

<section class="evx-cta">
  <div class="wrap-narrow">
    <span class="eyebrow eyebrow-line">Join the calendar</span>
    <h2>Live Italian culture, <span class="gold-ital">on the day itself.</span></h2>
    <p>Every Club Italia course includes access to the live cultural calendar, our teachers' broadcasts from the piazza, and the recorded archive of every past event for lifetime review.</p>
    <div class="hero-ctas" style="justify-content:center;display:flex">
      <a class="btn btn-3d btn-3d-primary" href="courses.html">Explore the Courses</a>
      <button class="btn btn-3d btn-3d-ghost" data-advisor type="button">Talk to an Advisor</button>
    </div>
  </div>
</section>
'''
    html = shell(
        "Cultural Events Calendar — Club Italia by eTeacher",
        "The Club Italia cultural events calendar. Live broadcasts from the piazza for Festa della Repubblica, Carnevale di Venezia, Palio di Siena and more, taught in real Italian by our resident teachers.",
        body, root="", extra_head=EVENTS_INDEX_STYLE
    )
    with open("/home/user/workspace/club-italia/events.html","w") as f:
        f.write(html)
    print("events.html", len(html))


# ================= COMMUNITY =================
COMM_STYLE = '''<style>
.cm-hero{min-height:80vh;position:relative;display:flex;align-items:flex-end;color:var(--on-dark);overflow:hidden;background:var(--navy-deep)}
.cm-hero-bg{position:absolute;inset:0;z-index:0}
.cm-hero-bg img{width:100%;height:100%;object-fit:cover;opacity:.55}
.cm-hero-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(34,8,11,.35),rgba(34,8,11,.92))}
.cm-hero .wrap{position:relative;z-index:2;padding:10rem 0 4rem}
.cm-hero h1{font-family:var(--serif);font-size:clamp(3rem,6vw,5.6rem);line-height:1.02;max-width:18ch;margin:1.4rem 0}
.cm-hero .lede{max-width:60ch;color:var(--on-dark-soft);font-weight:300;font-size:clamp(1.1rem,1.4vw,1.32rem);line-height:1.62}

.cm-stat{padding:5rem 0;background:var(--paper)}
.cm-stat .grid{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--gold-line-soft);border-bottom:1px solid var(--gold-line-soft)}
@media (max-width:820px){.cm-stat .grid{grid-template-columns:1fr 1fr}}
.cm-stat .cell{padding:2.4rem 1.6rem;text-align:center;border-right:1px solid var(--gold-line-soft)}
.cm-stat .cell:last-child{border-right:none}
.cm-stat .cell .n{font-family:var(--serif);font-style:italic;font-size:3rem;color:var(--gold-deep);line-height:1}
.cm-stat .cell .l{font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;margin-top:.6rem;color:var(--on-light-soft)}

.cm-band{padding:6rem 0}
.cm-band.dark{background:var(--navy);color:var(--on-dark)}
.cm-band.cream{background:var(--ivory)}
.cm-band.paper{background:var(--paper)}
.cm-band h2{font-family:var(--serif);font-size:clamp(2.2rem,4vw,3.4rem);line-height:1.05;max-width:22ch;margin-bottom:1.2rem}
.cm-band.dark h2,.cm-band.dark h3{color:var(--on-dark)}
.cm-band .lede-p{font-size:1.1rem;line-height:1.7;color:var(--on-light-soft);max-width:60ch}
.cm-band.dark .lede-p{color:var(--on-dark-soft)}

.cm-two{display:grid;grid-template-columns:1fr 1.15fr;gap:3.2rem;align-items:start}
@media (max-width:900px){.cm-two{grid-template-columns:1fr}}
.cm-two .body p{font-size:1rem;line-height:1.72;margin-bottom:1.1rem;color:var(--on-light-soft)}
.cm-band.dark .cm-two .body p{color:var(--on-dark-soft)}

.cm-pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem;margin-top:2.4rem}
@media (max-width:820px){.cm-pillars{grid-template-columns:1fr}}
.cm-pillar{padding:2.2rem 1.8rem;background:var(--paper);border:1px solid var(--gold-line-soft)}
.cm-band.dark .cm-pillar{background:var(--navy-mid);border-color:var(--dark-line-soft)}
.cm-pillar .rn{font-family:var(--serif);font-style:italic;font-size:1.8rem;color:var(--gold-deep);margin-bottom:.5rem}
.cm-band.dark .cm-pillar .rn{color:var(--gold-soft)}
.cm-pillar h4{font-family:var(--serif);font-size:1.35rem;margin-bottom:.5rem;line-height:1.18}
.cm-pillar p{font-size:.95rem;color:var(--on-light-soft);line-height:1.6}
.cm-band.dark .cm-pillar p{color:var(--on-dark-soft)}

.cm-quote{background:var(--paper);padding:6rem 0;text-align:center}
.cm-quote.dark{background:var(--navy-deep);color:var(--on-dark)}
.cm-quote .q{font-family:var(--serif);font-style:italic;font-size:clamp(1.8rem,3.4vw,2.6rem);line-height:1.24;max-width:34ch;margin:0 auto;color:var(--navy)}
.cm-quote.dark .q{color:var(--on-dark)}
.cm-quote .s{margin-top:1.4rem;font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-deep)}
.cm-quote.dark .s{color:var(--gold-soft)}

.cm-alumni{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem;margin-top:2.4rem}
@media (max-width:820px){.cm-alumni{grid-template-columns:1fr}}
.cm-alumni .a-card{background:var(--white);border:1px solid var(--gold-line-soft);padding:2rem 1.8rem}
.cm-alumni .a-card .stars{color:var(--gold-deep);letter-spacing:.15em;margin-bottom:.7rem}
.cm-alumni .a-card p{font-family:var(--serif);font-style:italic;font-size:1.2rem;line-height:1.4;color:var(--on-light);margin-bottom:1.2rem}
.cm-alumni .a-card .who{font-weight:600;font-size:.9rem}
.cm-alumni .a-card .loc{font-size:.75rem;color:var(--on-light-soft)}

.cm-forum{background:var(--navy-deep);color:var(--on-dark);padding:6rem 0;position:relative;overflow:hidden}
.cm-forum::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 20% 30%,rgba(201,162,75,.15),transparent 55%)}
.cm-forum .wrap{position:relative;z-index:1}
.cm-forum .thread-list{display:grid;grid-template-columns:1fr;gap:.9rem;margin-top:2rem}
.cm-forum .thread{display:grid;grid-template-columns:56px 1fr auto;gap:1.2rem;align-items:center;padding:1.2rem 1.6rem;background:var(--navy-mid);border:1px solid var(--dark-line-soft)}
.cm-forum .thread .av{width:52px;height:52px;border-radius:50%;background:var(--gold-deep);color:var(--navy);display:flex;align-items:center;justify-content:center;font-family:var(--serif);font-size:1.4rem}
.cm-forum .thread h4{font-family:var(--serif);color:var(--on-dark);font-size:1.15rem;margin-bottom:.2rem;line-height:1.2}
.cm-forum .thread p{color:var(--on-dark-soft);font-size:.85rem;margin:0}
.cm-forum .thread .replies{font-family:var(--serif);font-style:italic;color:var(--gold-soft);font-size:1.1rem}

.cm-cta{background:linear-gradient(140deg,var(--navy) 0%,var(--terra-deep) 130%);color:var(--on-dark);padding:6rem 0;text-align:center}
.cm-cta h2{color:var(--on-dark);font-family:var(--serif);font-size:clamp(2rem,4vw,3.4rem)}
.cm-cta p{color:var(--on-dark-soft);max-width:54ch;margin:1rem auto 2rem;font-size:1.1rem}
</style>'''

def build_community():
    body = '''
<section class="cm-hero">
  <div class="cm-hero-bg"><img src="assets/img/hero-poster.jpg" alt=""></div>
  <div class="wrap">
    <span class="eyebrow eyebrow-line" style="color:var(--gold-soft)">Il Circolo · the Club Italia community</span>
    <h1>A worldwide community of <span class="gold-ital">Italian learners.</span></h1>
    <p class="lede">Two thousand three hundred adult learners in one hundred and twenty countries, all living the Italian language in slightly different weather. Forums in three languages, weekly study groups on Zoom, an alumni network with two decades of stories, and Italian teachers in every time zone.</p>
  </div>
</section>

<section class="cm-stat">
  <div class="wrap">
    <div class="grid">
      <div class="cell"><div class="n">2,300</div><div class="l">Active learners</div></div>
      <div class="cell"><div class="n">120</div><div class="l">Countries</div></div>
      <div class="cell"><div class="n">17</div><div class="l">Weekly study groups</div></div>
      <div class="cell"><div class="n">3</div><div class="l">Forum languages</div></div>
    </div>
  </div>
</section>

<section class="cm-band paper">
  <div class="wrap">
    <div class="cm-two">
      <div>
        <span class="eyebrow eyebrow-line">Why community matters</span>
        <h2>A live language is a <span class="gold-ital">social language.</span></h2>
      </div>
      <div class="body">
        <p>Italian is a language you speak with someone else. It moves in dialogue, in the passing of a bottle across a table, in the small hospitality of a repeated greeting. The alone-with-an-app model of language learning has always been the wrong model for Italian, and we have said so from the first day of Club Italia.</p>
        <p>The classroom of twelve gives a learner peers. Il Circolo gives a learner peers everywhere else. Between one live lesson and the next, our members meet in study rooms, exchange voice notes, argue about a preposition on the forum, watch films together on Friday nights, and travel to Italy in groups organised over the alumni Slack.</p>
        <p>This is the ecology in which our best learners have always thrived. It is not a bonus feature. It is a load-bearing part of the method.</p>
      </div>
    </div>
  </div>
</section>

<section class="cm-quote">
  <div class="wrap-narrow">
    <p class="q">"You do not learn a language. You join one."</p>
    <p class="s">Attributed to the philologist Roman Jakobson</p>
  </div>
</section>

<section class="cm-band dark">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">The pillars of Il Circolo</span>
    <h2>Six places where Italian happens <span class="gold-ital">between the classes.</span></h2>
    <p class="lede-p">Every Club Italia member automatically joins Il Circolo on the first day of their first course. Access is included for life, even for graduates who have long since finished the programme.</p>
    <div class="cm-pillars">
      <div class="cm-pillar"><div class="rn">i</div><h4>The forum.</h4><p>Long-form threads on grammar puzzles, cultural questions, film club, travel tips, dual citizenship paperwork. Moderated by our teachers, in three languages: Italian, English, and a slower Italian for beginners.</p></div>
      <div class="cm-pillar"><div class="rn">ii</div><h4>The study groups.</h4><p>Seventeen weekly small-group Zoom sessions, learner-led, organised by level and by interest — opera, cinema, business Italian, dual citizenship, cooking, travel prep. Free to attend.</p></div>
      <div class="cm-pillar"><div class="rn">iii</div><h4>The alumni network.</h4><p>Over five thousand graduates on the private Slack, sharing job openings that need Italian, apartments in Italy for a month's stay, dinner-party invitations in New York, London, Tel Aviv, Melbourne.</p></div>
      <div class="cm-pillar"><div class="rn">iv</div><h4>The film club.</h4><p>One Italian film every second Friday, watched simultaneously by three hundred members, with a live subtitled thread and a debrief lesson the following week in slow Italian. Neorealism to Sorrentino.</p></div>
      <div class="cm-pillar"><div class="rn">v</div><h4>The travel circle.</h4><p>Small group trips organised by alumni to Rome, Florence, Puglia and Sicily every year, timed to the great cultural events, hosted in part by our resident teachers on the ground.</p></div>
      <div class="cm-pillar"><div class="rn">vi</div><h4>The reading room.</h4><p>A monthly Italian text — a short story, a poem, an essay from Corriere — chosen by our editorial team, annotated for learners, and discussed at all levels on the forum.</p></div>
    </div>
  </div>
</section>

<section class="cm-forum">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">Live from the forum</span>
    <h2>What the community is talking about <span class="gold-ital">this week.</span></h2>
    <div class="thread-list">
      <div class="thread"><div class="av">C</div><div><h4>Il congiuntivo dopo "non credo che" — quando è davvero necessario?</h4><p>Chiara · Milano · 24 replies · in Italiano</p></div><div class="replies">24 ›</div></div>
      <div class="thread"><div class="av">D</div><div><h4>Best month for a first trip to Puglia?</h4><p>David from Boston · 41 replies · in English</p></div><div class="replies">41 ›</div></div>
      <div class="thread"><div class="av">M</div><div><h4>Dual citizenship — sending documents from the US, timeline for 2026?</h4><p>Maria · Los Angeles · 63 replies · in English</p></div><div class="replies">63 ›</div></div>
      <div class="thread"><div class="av">A</div><div><h4>Aperitivo tips for a group of six in Rome — Trastevere or Monti?</h4><p>Alessandro (teacher) · Roma · 19 replies · in italiano lento</p></div><div class="replies">19 ›</div></div>
      <div class="thread"><div class="av">R</div><div><h4>Book club: this month La coscienza di Zeno — chapter 3 discussion</h4><p>Rachel · London · 12 replies · in English + italiano</p></div><div class="replies">12 ›</div></div>
      <div class="thread"><div class="av">L</div><div><h4>Perché i napoletani dicono "guaglione"? Storia della parola.</h4><p>Luca · Napoli · 8 replies · in Italiano</p></div><div class="replies">8 ›</div></div>
    </div>
  </div>
</section>

<section class="cm-band cream">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">Alumni stories</span>
    <h2>The learners who <span class="gold-ital">kept going.</span></h2>
    <p class="lede-p">Every year, dozens of Club Italia alumni turn their Italian into a real chapter in life — a move to Bologna, a business in Milan, a passport in the mail, a first novel written in Italian for their own children.</p>
    <div class="cm-alumni">
      <div class="a-card"><div class="stars">★★★★★</div><p>"I started Club Italia in 2022 at fifty-eight to prepare for my father's citizenship application. Three years later I bought an apartment in Bologna and my grandchildren visit in the summer. Their Italian is now better than my Duolingo streak ever was."</p><div class="who">Deborah K.</div><div class="loc">Bologna, Italy · began New York, 2022</div></div>
      <div class="a-card"><div class="stars">★★★★★</div><p>"After the second term I started running my design agency's Milanese client meetings in Italian. My retention rate on Italian accounts went from sixty-two to ninety-four percent. Il Circolo alumni Slack was where I found my first local hire."</p><div class="who">Michael T.</div><div class="loc">London / Milano · began 2023</div></div>
      <div class="a-card"><div class="stars">★★★★★</div><p>"I met my study-group partner in the CI Elementare course. We are getting married in September in her family's village outside Perugia. The whole ceremony will be in Italian and I will not need subtitles."</p><div class="who">Jonathan R.</div><div class="loc">Umbria, Italy · began Tel Aviv, 2024</div></div>
    </div>
  </div>
</section>

<section class="cm-quote dark">
  <div class="wrap-narrow">
    <p class="q">"Italian is not a subject to study. It is a house to move into."</p>
    <p class="s">Chiara Foschi, Club Italia teacher, Bologna</p>
  </div>
</section>

<section class="cm-cta">
  <div class="wrap-narrow">
    <span class="eyebrow eyebrow-line">Join Il Circolo</span>
    <h2>Every course includes <span class="gold-ital">the community.</span></h2>
    <p>Enrolment in any Club Italia course opens Il Circolo automatically — the forum, the study groups, the alumni network, the film club, the reading room, the travel circle. Membership continues after the course ends, for life.</p>
    <div class="hero-ctas" style="justify-content:center;display:flex">
      <a class="btn btn-3d btn-3d-primary" href="courses.html">Explore the Courses</a>
      <button class="btn btn-3d btn-3d-ghost" data-advisor type="button">Talk to an Advisor</button>
    </div>
  </div>
</section>
'''
    html = shell("Il Circolo — Club Italia Community",
                 "Il Circolo is the Club Italia community: 2,300 adult Italian learners across 120 countries, weekly study groups, an alumni network, forums, film club, reading room and travel circle.",
                 body, root="", extra_head=COMM_STYLE)
    with open("/home/user/workspace/club-italia/community.html","w") as f: f.write(html)
    print("community.html", len(html))


# ================= SAMPLE CLASS =================
SC_STYLE = '''<style>
.sc-hero{position:relative;min-height:100vh;display:flex;align-items:center;overflow:hidden;color:var(--on-dark);background:var(--navy-deep)}
.sc-hero-bg{position:absolute;inset:0;z-index:0}
.sc-hero-bg img{width:100%;height:100%;object-fit:cover}
.sc-hero-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(120deg,rgba(34,8,11,.85) 0%,rgba(34,8,11,.55) 55%,rgba(34,8,11,.35) 100%)}
.sc-hero .wrap{position:relative;z-index:2}
.sc-hero h1{font-family:var(--serif);font-size:clamp(3rem,6vw,5.8rem);line-height:1.02;max-width:18ch;margin:1.4rem 0}
.sc-hero .lede{max-width:56ch;color:var(--on-dark-soft);font-size:clamp(1.15rem,1.45vw,1.38rem);line-height:1.62;font-weight:300}
.sc-hero .play-wrap{margin-top:2.4rem;display:flex;align-items:center;gap:1.4rem}
.sc-hero .play{width:88px;height:88px;border-radius:50%;background:var(--gold-deep);color:var(--navy);display:flex;align-items:center;justify-content:center;font-size:1.6rem;padding-left:6px;box-shadow:0 12px 40px rgba(0,0,0,.45)}
.sc-hero .play-l{font-family:var(--serif);font-style:italic;color:var(--on-dark-soft)}

.sc-tri{height:6px;background:linear-gradient(90deg,#009246 33.33%,#F6F1E6 33.33% 66.66%,#CE2B37 66.66%)}

.sc-band{padding:6rem 0}
.sc-band.dark{background:var(--navy);color:var(--on-dark)}
.sc-band.cream{background:var(--ivory)}
.sc-band.paper{background:var(--paper)}
.sc-band h2{font-family:var(--serif);font-size:clamp(2.2rem,4vw,3.4rem);line-height:1.05;max-width:22ch;margin-bottom:1.2rem}
.sc-band.dark h2,.sc-band.dark h3,.sc-band.dark h4{color:var(--on-dark)}
.sc-band .lede-p{color:var(--on-light-soft);font-size:1.1rem;line-height:1.7;max-width:60ch}
.sc-band.dark .lede-p{color:var(--on-dark-soft)}

.sc-format{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-top:2.4rem}
@media (max-width:820px){.sc-format{grid-template-columns:1fr 1fr}}
.sc-format .cell{padding:2rem 1.6rem;background:var(--white);border:1px solid var(--gold-line-soft);text-align:center}
.sc-band.dark .sc-format .cell{background:var(--navy-mid);border-color:var(--dark-line-soft)}
.sc-format .cell .n{font-family:var(--serif);font-style:italic;font-size:2.6rem;color:var(--gold-deep);line-height:1}
.sc-band.dark .sc-format .cell .n{color:var(--gold-soft)}
.sc-format .cell .l{font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;margin-top:.6rem;color:var(--on-light-soft)}
.sc-band.dark .sc-format .cell .l{color:var(--on-dark-soft)}

.sc-minute{margin-top:2rem}
.sc-min-row{display:grid;grid-template-columns:120px 1fr;gap:2rem;padding:1.4rem 0;border-bottom:1px solid var(--gold-line-soft);align-items:start}
.sc-min-row .t{font-family:var(--serif);font-style:italic;font-size:1.4rem;color:var(--gold-deep)}
.sc-band.dark .sc-min-row .t{color:var(--gold-soft)}
.sc-min-row .b h4{font-family:var(--serif);font-size:1.2rem;margin-bottom:.4rem;line-height:1.2}
.sc-min-row .b p{font-size:.95rem;color:var(--on-light-soft);line-height:1.62}
.sc-band.dark .sc-min-row .b p{color:var(--on-dark-soft)}

.sc-snip{display:grid;grid-template-columns:1fr 1fr;gap:1.6rem;margin-top:2rem}
@media (max-width:820px){.sc-snip{grid-template-columns:1fr}}
.sc-snip .card{padding:2rem;background:var(--paper);border-left:3px solid var(--gold-deep)}
.sc-band.dark .sc-snip .card{background:var(--navy-mid);border-left-color:var(--gold-soft)}
.sc-snip .card .who{font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-deep);margin-bottom:.6rem}
.sc-band.dark .sc-snip .card .who{color:var(--gold-soft)}
.sc-snip .card .it{font-family:var(--serif);font-style:italic;font-size:1.3rem;color:var(--navy);margin-bottom:.5rem;line-height:1.3}
.sc-band.dark .sc-snip .card .it{color:var(--on-dark)}
.sc-snip .card .en{font-size:.95rem;color:var(--on-light-soft)}
.sc-band.dark .sc-snip .card .en{color:var(--on-dark-soft)}

.sc-quote{background:var(--paper);padding:6rem 0;text-align:center}
.sc-quote.dark{background:var(--navy-deep);color:var(--on-dark)}
.sc-quote .q{font-family:var(--serif);font-style:italic;font-size:clamp(1.8rem,3.4vw,2.6rem);line-height:1.24;max-width:34ch;margin:0 auto;color:var(--navy)}
.sc-quote.dark .q{color:var(--on-dark)}
.sc-quote .s{margin-top:1.4rem;font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-deep)}
.sc-quote.dark .s{color:var(--gold-soft)}

.sc-vs{display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:2rem}
@media (max-width:820px){.sc-vs{grid-template-columns:1fr}}
.sc-vs .col{padding:2.2rem;background:var(--paper);border:1px solid var(--gold-line-soft)}
.sc-band.dark .sc-vs .col{background:var(--navy-mid);border-color:var(--dark-line-soft)}
.sc-vs .col.us{border-top:4px solid var(--gold-deep)}
.sc-vs .col.zoom{opacity:.85}
.sc-vs h4{font-family:var(--serif);font-size:1.4rem;margin-bottom:1rem}
.sc-vs ul{list-style:none;padding:0;margin:0}
.sc-vs li{padding:.7rem 0;border-bottom:1px dotted var(--gold-line-soft);color:var(--on-light-soft);font-size:.95rem;padding-left:1.4rem;position:relative}
.sc-band.dark .sc-vs li{color:var(--on-dark-soft)}
.sc-vs li::before{content:"›";position:absolute;left:0;color:var(--gold-deep)}
.sc-vs .zoom li::before{content:"×";color:var(--terra-deep)}

.sc-feel{display:grid;grid-template-columns:1fr 1.15fr;gap:3.2rem;align-items:start}
@media (max-width:900px){.sc-feel{grid-template-columns:1fr}}
.sc-feel .body p{color:var(--on-light-soft);font-size:1.02rem;line-height:1.72;margin-bottom:1.1rem}
.sc-band.dark .sc-feel .body p{color:var(--on-dark-soft)}

.sc-cta{background:linear-gradient(140deg,var(--navy) 0%,var(--terra-deep) 130%);color:var(--on-dark);padding:6rem 0;text-align:center}
.sc-cta h2{color:var(--on-dark);font-family:var(--serif);font-size:clamp(2rem,4vw,3.4rem)}
.sc-cta p{color:var(--on-dark-soft);max-width:54ch;margin:1rem auto 2rem;font-size:1.1rem}
</style>'''

def build_sample():
    body = '''
<section class="sc-hero">
  <div class="sc-hero-bg"><img src="assets/img/class-demo-poster.jpg" alt="A Club Italia class in session"></div>
  <div class="wrap">
    <span class="eyebrow eyebrow-line" style="color:var(--gold-soft)">Watch a real class · Roma · CI Principiante · Session 07</span>
    <h1>Eighty-five minutes inside a <span class="gold-ital">real Club Italia lesson.</span></h1>
    <p class="lede">A full editorial walk-through of one of our beginner sessions — the format, the minute-by-minute rhythm, the small talk before class begins, the moment somebody speaks Italian for the first time, and the reasons every learner tells us it feels nothing like a Zoom class.</p>
    <div class="play-wrap">
      <a href="#" class="play" aria-label="Play the recording">▶</a>
      <span class="play-l">Watch the 14-minute editorial reel</span>
    </div>
  </div>
</section>

<div class="sc-tri" aria-hidden="true"></div>

<section class="sc-band paper">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">The format</span>
    <h2>The shape of every Club Italia lesson, <span class="gold-ital">at a glance.</span></h2>
    <p class="lede-p">Every course session runs to the same architecture. The teacher varies. The city varies. The exact material varies. The rhythm — arrival, opening ritual, the day's language, the culture window, the guided speaking, the closing — never varies.</p>
    <div class="sc-format">
      <div class="cell"><div class="n">85</div><div class="l">minutes per lesson</div></div>
      <div class="cell"><div class="n">10–12</div><div class="l">learners in the room</div></div>
      <div class="cell"><div class="n">1</div><div class="l">teacher, live from Italy</div></div>
      <div class="cell"><div class="n">∞</div><div class="l">lifetime recording access</div></div>
    </div>
  </div>
</section>

<section class="sc-band dark">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">Minute by minute</span>
    <h2>What happens in the eighty-five minutes, <span class="gold-ital">in order.</span></h2>
    <p class="lede-p">Recorded from a real session of CI Principiante, taught by Sofia broadcasting from Rome, on the seventh Tuesday of the term.</p>
    <div class="sc-minute">
      <div class="sc-min-row"><div class="t">−05:00</div><div class="b"><h4>The room opens.</h4><p>Sofia joins from her Roman studio. Learners arrive in twos and threes; there is small talk in English and hesitant Italian; the coffee cup on Sofia's desk is a Bialetti moka. This is on purpose. The classroom is a place, not a screen.</p></div></div>
      <div class="sc-min-row"><div class="t">00:00</div><div class="b"><h4>The ritual of the greeting.</h4><p>Sofia takes attendance in Italian and asks each learner one small personal question — the weather, the weekend, the pasta of last night. Nobody gets it wrong. Everybody speaks a full sentence. Five minutes.</p></div></div>
      <div class="sc-min-row"><div class="t">00:05</div><div class="b"><h4>La parola del giorno.</h4><p>The word of the day. Today: <em>vicino</em>. Sofia writes it on her side of the whiteboard, uses it in six spoken sentences, then puts it into the chat for saving. Learners repeat aloud, unmuted. Three minutes.</p></div></div>
      <div class="sc-min-row"><div class="t">00:08</div><div class="b"><h4>Review of last session.</h4><p>Five minutes of quick-fire recall. Sofia calls names in Italian; the room answers in Italian. If nobody remembers the verb <em>abitare</em>, she draws it, mimes it, sings it. The whole session moves in Italian by the ninth minute.</p></div></div>
      <div class="sc-min-row"><div class="t">00:13</div><div class="b"><h4>The new material.</h4><p>Twenty-five minutes on the day's structure. Today: the difference between <em>c'è</em> and <em>ci sono</em>. Grammar is embedded in a real Roman story — Sofia describes her walk to the bar this morning and the room reconstructs the walk in Italian.</p></div></div>
      <div class="sc-min-row"><div class="t">00:38</div><div class="b"><h4>La finestra sull'Italia.</h4><p>The culture window. Fifteen minutes of live Italian input — a short film clip, a menu from a Roman trattoria, a photo of Piazza Navona at seven in the morning. Sofia narrates in slow Italian. Learners listen. No English.</p></div></div>
      <div class="sc-min-row"><div class="t">00:53</div><div class="b"><h4>Breakout rooms.</h4><p>Twenty minutes in threes. Sofia rotates. Each breakout works on a real task — reserve a table by phone, order two courses, ask for the check, refuse coffee politely. The tasks are Roman-specific, not generic.</p></div></div>
      <div class="sc-min-row"><div class="t">01:13</div><div class="b"><h4>Whole-group debrief.</h4><p>Ten minutes. Every breakout reports back in Italian. Sofia corrects lightly — never breaks flow. Common errors are logged on the shared board and become homework prompts.</p></div></div>
      <div class="sc-min-row"><div class="t">01:23</div><div class="b"><h4>The closing.</h4><p>Two minutes. Sofia announces next week's cultural fold, wishes the room <em>buona serata</em>, and lingers on video for as long as anyone wants to stay and talk — often another fifteen minutes, off the clock.</p></div></div>
    </div>
  </div>
</section>

<section class="sc-quote">
  <div class="wrap-narrow">
    <p class="q">"I have taken online courses for twelve years. This is the first one where I speak more Italian than my teacher does."</p>
    <p class="s">Deborah K., alumna · New York, cohort 2022</p>
  </div>
</section>

<section class="sc-band cream">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">Live snippets</span>
    <h2>Four things you will hear in the <span class="gold-ital">first lesson.</span></h2>
    <p class="lede-p">A real transcript from a Roman session of CI Principiante, session one. The greetings, the first correction, the first laugh.</p>
    <div class="sc-snip">
      <div class="card"><div class="who">Sofia · Roma · 00:04</div><p class="it">"Buonasera a tutti. Prima di iniziare, un giro veloce — come state stasera?"</p><p class="en">Good evening everyone. Before we start, a quick round — how is everyone this evening?</p></div>
      <div class="card"><div class="who">Michael · Boston · 00:06</div><p class="it">"Io sto bene, grazie. E tu? È una bella giornata a Roma?"</p><p class="en">I am well, thank you. And you? Is it a nice day in Rome? (First sentence spoken by a beginner.)</p></div>
      <div class="card"><div class="who">Sofia · 00:37</div><p class="it">"Attenzione: si dice <em>c'è un caffè</em> — un solo caffè — ma <em>ci sono due caffè</em>. Provate voi."</p><p class="en">Careful: you say <em>c'è un caffè</em> — one coffee — but <em>ci sono due caffè</em>. Now try yourselves.</p></div>
      <div class="card"><div class="who">Rachel · London · 01:12</div><p class="it">"Ho prenotato un tavolo per due, per venerdì sera, alle otto. Va bene così?"</p><p class="en">I have booked a table for two, for Friday evening, at eight. Is that alright? (Breakout task, first phone call.)</p></div>
    </div>
  </div>
</section>

<section class="sc-quote dark">
  <div class="wrap-narrow">
    <p class="q">"The eighty-fifth minute is what separates a lesson from a class."</p>
    <p class="s">Sofia Marino, Club Italia teacher, Roma</p>
  </div>
</section>

<section class="sc-band paper">
  <div class="wrap">
    <div class="sc-feel">
      <div>
        <span class="eyebrow eyebrow-line">How it feels the first time</span>
        <h2>What a first-time learner actually <span class="gold-ital">experiences.</span></h2>
      </div>
      <div class="body">
        <p>The first Club Italia lesson is not a lecture. It is a room. The teacher greets each learner by name. The other learners nod. Within four minutes the whole conversation is in Italian, at a pace slow enough for a beginner to catch every fifth word — which is enough.</p>
        <p>You will make mistakes in front of the room within the first ten minutes. This is by design. The teacher will correct one of them, warmly, and move on. Nobody laughs. Everybody has done the same. By the fortieth minute, most learners have forgotten to feel self-conscious. By the eighty-fifth, most stay on video for another ten just to keep talking.</p>
        <p>The recording arrives in the inbox that night. Learners re-watch on the commute, catch the phrases they missed, and come back the following week already fluent in five things they were not fluent in before. It is a compounding format.</p>
      </div>
    </div>
  </div>
</section>

<section class="sc-band dark">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">Not a Zoom class</span>
    <h2>Why this feels nothing like the <span class="gold-ital">online school you tried before.</span></h2>
    <div class="sc-vs">
      <div class="col us">
        <h4>Club Italia · live from Italy</h4>
        <ul>
          <li>Ten to twelve learners, every speaks in every session</li>
          <li>Native Italian teacher, broadcasting from Rome, Florence, Milan or Naples</li>
          <li>Culture at the core, not decoration — a live cultural fold every lesson</li>
          <li>Real tasks: order in a bar, book by phone, argue about the bill</li>
          <li>Recording of every session, kept for life, indexed by grammar point</li>
          <li>Il Circolo community forum for the six days between classes</li>
          <li>CEFR-aligned certificate on completion, issued by eTeacher Group</li>
        </ul>
      </div>
      <div class="col zoom">
        <h4>Typical online class</h4>
        <ul>
          <li>Forty to two hundred learners in the room, one microphone</li>
          <li>Teacher location and native-speaker status varies from session to session</li>
          <li>Grammar drills first, culture as an occasional bonus PDF</li>
          <li>Generic worksheets, textbook exercises, fill-in-the-blank at pace</li>
          <li>Recording available for thirty days, then removed</li>
          <li>Community is a Facebook page moderated by an intern</li>
          <li>No formal certification, or a private certificate of doubtful value</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sc-band cream">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">What alumni told us</span>
    <h2>The three things every alumnus <span class="gold-ital">says first.</span></h2>
    <div class="sc-snip">
      <div class="card"><div class="who">On the small group size</div><p class="it">"Ten people. Ten. I could not hide."</p><p class="en">— Amir S., Tel Aviv · CI Elementare, 2024</p></div>
      <div class="card"><div class="who">On the teacher being in Italy</div><p class="it">"When Chiara said <em>oggi piove a Bologna</em>, we knew she meant it. That changed how we listened."</p><p class="en">— Kirsten L., Sydney · CI Intermedio, 2025</p></div>
      <div class="card"><div class="who">On the pace</div><p class="it">"Eighty-five minutes goes by like fifteen. Then I want to book another one."</p><p class="en">— Paul M., Boston · CI Principiante, 2025</p></div>
      <div class="card"><div class="who">On the community</div><p class="it">"The class ends. Il Circolo does not. I met my two best friends in Italy on the alumni Slack."</p><p class="en">— Nadia B., London · Parliamo Elementary, 2023</p></div>
    </div>
  </div>
</section>

<section class="sc-cta">
  <div class="wrap-narrow">
    <span class="eyebrow eyebrow-line">Reserve a seat</span>
    <h2>Book a seat in a real, <span class="gold-ital">not a sample.</span></h2>
    <p>You are welcome to sit in as a silent observer for the first ten minutes of any new-cohort session, free, before enrolment. Our advisors book the observation and take you through the first-week reading.</p>
    <div class="hero-ctas" style="justify-content:center;display:flex">
      <a class="btn btn-3d btn-3d-primary" href="courses.html">See This Term's Courses</a>
      <button class="btn btn-3d btn-3d-ghost" data-advisor type="button">Book My Observation</button>
    </div>
  </div>
</section>
'''
    html = shell("Watch a Real Class — Club Italia by eTeacher",
                 "An editorial walk-through of a real Club Italia beginner lesson broadcast live from Rome — the 85-minute format, minute-by-minute rhythm, live transcripts, and why it feels nothing like a Zoom class.",
                 body, root="", extra_head=SC_STYLE)
    with open("/home/user/workspace/club-italia/sample-class.html","w") as f: f.write(html)
    print("sample-class.html", len(html))


if __name__ == "__main__":
    build_events_index()
    build_community()
    build_sample()
