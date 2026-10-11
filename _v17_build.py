# Club Italia v17 build: core pages in the new editorial system
import json, re, html
D = json.load(open('research/course-data.json'))
def clean(s): return re.sub(r'\s*[—–]\s*', ', ', s).replace('→','to')
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
NAV = [('courses.html','Courses'),('curriculum.html','Curriculum'),('method.html','Method'),('certifications.html','Certification'),('teachers.html','Faculty'),('culture.html','Culture'),('biagio.html','AI Tutor'),('pricing.html','Tuition')]
def head(title, desc, light=False, active=''):
    nav = ''.join(f'<a href="{h}"{" aria-current=page" if h==active else ""}>{t}</a>' for h,t in NAV)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#14171f">
{FONTS}<link rel="stylesheet" href="css/v17.css"></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="hdr{' light' if light else ''}"><div class="wrap">
<a class="brand" href="index.html" aria-label="Club Italia home"><span class="brand-name">Club Italia</span><span class="brand-by">by <img class="logo-light" src="assets/img/eteacher-real-logo-white.png" alt="eTeacher Group"><img class="logo-dark" src="assets/img/eteacher-real-logo.png" alt="eTeacher Group"></span></a>
<nav class="nav" aria-label="Primary">{nav}<a class="btn btn-primary" href="contact.html">Talk to an advisor</a></nav>
<button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span></button></div></header><main id="main">'''
FOOT = '''</main><footer class="ftr"><div class="wrap"><div class="cols">
<div><span class="brand-name">Club Italia</span><p class="mt1">A live, culturally immersive Italian school for adult learners. Taught by native teachers, broadcast from Italy.</p>
<img src="assets/img/eteacher-real-logo-white.png" alt="eTeacher Group" style="height:22px;margin-top:1.6rem"><p class="mt1"><a href="mailto:advisor@eTeacherGroup.com">advisor@eTeacherGroup.com</a></p></div>
<div><h5>Study</h5><ul><li><a href="courses.html">All courses</a></li><li><a href="curriculum.html">Curriculum A1 to C2</a></li><li><a href="certifications.html">CILS and CELI preparation</a></li><li><a href="capsules.html">Cultural capsules</a></li><li><a href="biagio.html">Biagio, AI tutor</a></li><li><a href="sample-class.html">Sample class</a></li></ul></div>
<div><h5>The school</h5><ul><li><a href="method.html">Method</a></li><li><a href="teachers.html">Faculty</a></li><li><a href="how-it-works.html">How it works</a></li><li><a href="about.html">About</a></li><li><a href="eteacher.html">eTeacher Group</a></li><li><a href="events.html">Events</a></li></ul></div>
<div><h5>Culture</h5><ul><li><a href="culture.html">Culture hub</a></li><li><a href="map.html">Map of Italy</a></li><li><a href="blog.html">Journal</a></li><li><a href="community.html">Community</a></li><li><a href="faq.html">FAQ</a></li><li><a href="contact.html">Contact</a></li></ul></div>
</div><div class="legal"><span>© 2026 eTeacher Group. Club Italia is a trading style of eTeacher Group.</span><span><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a></span></div>
<p style="font-size:.72rem;margin-top:1rem;opacity:.6">Club Italia is independent and is not an official CILS or CELI examination centre. CILS is administered by the Università per Stranieri di Siena; CELI by the Università per Stranieri di Perugia. Opt-in hero music: Vivaldi, «La primavera», CC BY-SA 3.0.</p>
</div></footer><script src="js/v17.js" defer></script></body></html>'''
def page(fn, title, desc, body, light=False):
    out = head(title, desc, light, fn) + body + FOOT
    out = out.replace('—', ', ').replace('–', ' to ')
    open(fn,'w').write(out)

def vid(name, cls=''):
    return f'<video class="{cls}" autoplay muted loop playsinline webkit-playsinline preload="metadata" poster="assets/img/{name}-poster.jpg" aria-hidden="true"><source src="assets/video/{name}.mp4" type="video/mp4"></video>'

COURSES = {
 'ci':[('ci1','CI Principiante','A0 to A1.1','Marco Rinaldi','Roma','course-ci1.jpg','pages/courses/ci1.html'),
       ('ci2','CI Elementare','A1.1 to A1.2','Chiara Bellini','Firenze','course-ci2.jpg','pages/courses/ci2.html'),
       ('ci3','CI Intermedio','A1.2 to A2.1','Giulia Moretti','Bologna','course-ci3.jpg','pages/courses/ci3.html'),
       ('ci4','CI Avanzato','A2.1 to A2.2','Luca De Simone','Napoli','course-ci4.jpg','pages/courses/ci4.html')],
 'ps':[('ps1','Al Caffè','Spoken A0 to A1','Marco Rinaldi','Roma','spoken-ps1.jpg','pages/spoken/ps1.html'),
       ('ps2','A Tavola','Spoken A1 to A2','Chiara Bellini','Firenze','spoken-ps2.jpg','pages/spoken/ps2.html'),
       ('ps3','In Viaggio','Spoken A2','Francesca Zeno','Venezia','spoken-ps3.jpg','pages/spoken/ps3.html'),
       ('ps4','Chiacchierando','Spoken A2 to B1','Alessandro Ferri','Milano','spoken-ps4.jpg','pages/spoken/ps4.html')],
 'cap':[('cap-food','La Cucina','Cultural, any level','Giulia Moretti','Bologna','cap-food.jpg','pages/culture/cap-food.html'),
        ('cap-art',"L'Arte",'Cultural, any level','Chiara Bellini','Firenze','cap-art.jpg','pages/culture/cap-art.html'),
        ('cap-opera',"L'Opera",'Cultural, any level','Alessandro Ferri','Milano','cap-opera.jpg','pages/culture/cap-opera.html')]}
def card(c, start='Oct 6, 2026', tuition='$62 a week'):
    k,t,lv,tch,city,img,href = c; d = D[k]
    fmt = clean(d['hours']).replace(' × ',' of ')
    if k.startswith('cap'): start, tuition = 'Oct 20, 2026', '$390'
    return f'''<a class="card rv" href="{href}"><div class="ph"><img loading="lazy" src="assets/img/{img}" alt="{html.escape(t)} course, {city}"></div><div class="bd">
<span class="tag">{clean(d['code'])} · {lv}</span><h3>{html.escape(t)}</h3><p>{html.escape(clean(d['promise']).split('. ')[0])}.</p>
<dl class="meta"><dt>Faculty</dt><dd>{tch}, {city}</dd><dt>Format</dt><dd>{fmt}, live</dd><dt>Starts</dt><dd>{start}</dd><dt>Tuition</dt><dd>{tuition}</dd></dl></div></a>'''
# <!-- pitch placeholders retained from v16 -->
STATS = '''<!-- TODO(owner): learner count, Trustpilot rating and founding year are v16 pitch placeholders; v16 pages disagree (12,847 since 2004 vs 400k since 2000). Confirm real eTeacher figures. -->
<div class="stats rv"><div><b>2004</b><span>eTeacher teaching live online</span></div><div><b>12,847</b><span>Learners taught</span></div><div><b>4.8</b><span>Trustpilot average</span></div><div><b>7</b><span>Italian cities on the faculty</span></div></div>'''

LADDER = [('A1','Breakthrough','Introduce yourself, order, ask the way. Present tense, articles, essere and avere.',17),
 ('A2','Waystage','Narrate the past, make plans, handle travel and shops. Passato prossimo and imperfetto.',34),
 ('B1','Threshold','Hold a conversation on familiar topics, give opinions, write a coherent letter. Futuro, condizionale, pronouns.',50),
 ('B2','Vantage','Argue a point, follow the news, read contemporary fiction. Congiuntivo and complex syntax.',67),
 ('C1','Effective','Use Italian flexibly for work and study. Register, idiom, academic writing.',84),
 ('C2','Mastery','Understand virtually everything. Literary Italian, nuance, regional variety.',100)]
def ladder():
    return '<div class="ladder rv">'+''.join(f'<div><span class="lv">{a}</span><h4>{b}</h4><p>{c}</p><div class="bar"><i style="width:{w}%"></i></div></div>' for a,b,c,w in LADDER)+'</div>'

FAQ = [('Courses',[('How is this different from an app?','Club Italia is a live small group class with a native teacher broadcasting from Italy. You speak in every lesson, and a teacher hears and corrects you. Apps are a useful supplement. They are not a classroom.'),
 ('I already speak some Italian. Where do I start?','Book a placement conversation. A teacher assesses your spoken and written Italian against the CEFR descriptors and places you on the correct rung, so you neither repeat nor drown.'),
 ('How large are the groups?','Ten to twelve adult learners per class. Small enough that everyone speaks in every lesson.'),
 ('What if I miss a class?','Every class is recorded and added to your library, with the teacher\'s notes.')]),
 ('Levels and certification',[('Which CEFR levels do you teach?','The current catalog runs from A0 to B1: four structured courses from A0 to A2.2 and a spoken track that reaches B1. The curriculum framework continues to C2, and advanced cohorts open on demand.'),
 ('What certificate do I receive?','At the end of each course you receive a Club Italia certificate stating the CEFR level you have reached. It is a school certificate, not a state examination.'),
 ('Do you prepare for CILS and CELI?','Yes. From A2 upward, lessons can include exam technique for the CILS (Università per Stranieri di Siena) and CELI (Università per Stranieri di Perugia) papers. You sit the exam itself at an authorised exam centre.'),
 ('Can a certificate help with Italian citizenship?','Italian citizenship by naturalisation or marriage requires B1 Italian certified by a recognised body such as CILS or CELI. Our B1 path prepares you for that exam; the school certificate itself is not a substitute.')]),
 ('Practical',[('What do I need?','A computer with a webcam, headphones and a stable internet connection. Classes run on Zoom; there is nothing to install beyond that.'),
 ('Is there a refund?','Seven day full refund from your first live lesson.'),
 ('Is Biagio a real teacher?','No. Biagio is an AI conversation tutor trained on our syllabus, included with every course for practice between lessons. Your teacher is a real person.')])]
def faq_html(groups):
    s=''
    for g,qs in groups:
        s+=f'<h3>{g}</h3>'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in qs)
    return f'<div class="faq">{s}</div>'

def band(title, text, poster='ag-cypress-road', video=True):
    media = vid(poster) if video else f'<img src="assets/img/{poster}" alt="">'
    return f'''<section class="band">{media}<div class="wrap narrow rv"><span class="eyebrow">Autumn 2026 cohorts</span><h2>{title}</h2><p class="lede">{text}</p>
<div class="ctas"><a class="btn btn-gold" href="contact.html">Book a placement conversation <span class="arr">→</span></a><a class="btn btn-ghost" href="sample-class.html">See a real class</a></div></div></section>'''

# ================= HOME =================
home = f'''
<section class="hero">{vid('ag-roma-statue')}<div class="wrap">
<span class="eyebrow">Live from Italy · CEFR A0 to B1</span>
<h1>Learn Italian. <em>Live from Italy.</em></h1>
<p class="lede">Live classes with a native teacher in Italy. Ten to twelve learners in your class. Twenty lessons per course, built on the Common European Framework. A CEFR certificate at the end.</p>
<div class="ctas"><a class="btn btn-gold" href="contact.html">Reserve my seat. $62 a week <span class="arr">→</span></a><a class="btn btn-ghost" href="sample-class.html">See a real class</a></div>
<div class="hero-meta"><div><b>10 to 12</b>learners per class</div><div><b>20</b>live lessons per course</div><div><b>7</b>Italian cities</div><div><b>A0 to B1</b>CEFR ladder</div></div>
</div></section>

<div class="marquee" aria-hidden="true"><div>{''.join(f'<span>{w}</span>' for w in ['«Benvenuti»','Roma','Firenze','Bologna','Milano','Venezia','Napoli','Palermo','«Parliamo italiano»']*2)}</div></div>

<section><div class="wrap split">
<div class="rv"><span class="eyebrow">The school</span><h2>A serious school. <em>Not an app.</em></h2>
<p class="lede mt2">Club Italia is the Italian faculty of eTeacher Group. Every lesson is live, every teacher is a native Italian, and every course sits on a defined rung of the Common European Framework of Reference for Languages.</p>
<p class="mt1">You do not study Italian here. You use it: to order, to argue, to tell a story, to read a menu in Bologna and an inscription in Rome. Grammar is taught precisely, then put to work in the situations where Italians actually use it.</p>
<div class="ctas"><a class="link" href="method.html">Read the method</a><a class="link" href="about.html">About the school</a></div></div>
<figure class="frame rv"><img src="assets/img/v17/zoom-classroom-luxury.jpg" alt="A Club Italia live class on Zoom, teacher in Italy and adult learners on screen"><figcaption>A live Club Italia class. The teacher is in Italy; the learners are at home.</figcaption></figure>
</div><div class="wrap mt3">{STATS}</div></section>

<section class="bg-ivory"><div class="wrap"><div class="sec-head"><span class="eyebrow">What you get</span><h2>Six commitments, <em>in every course.</em></h2></div>
<div class="grid g3">
{''.join(f'<div class="pillar rv"><div class="num">0{i+1}</div><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate([
('Live from Italy','Your teacher broadcasts from Rome, Florence, Bologna, Milan, Venice, Naples or Palermo. You hear the Italian that lives there.'),
('Small groups','Ten to twelve adult learners. You speak in every lesson, not once a term.'),
('A defined syllabus','Twenty lessons per course, each with stated objectives, grammar, vocabulary and a cultural setting. Published in advance as a PDF.'),
('Teacher-led, not self-serve','A qualified native teacher plans, teaches and corrects. Feedback is personal and immediate.'),
('Practice between lessons','Biagio, the AI conversation tutor, is available at any hour to rehearse what you learned in class.'),
('Measured progress','Can-do assessment at every milestone and a CEFR-mapped certificate at the end of each course.')]))}
</div></div></section>

<section><div class="wrap"><div class="sec-head"><span class="eyebrow">Autumn 2026 catalog</span><h2>Eleven courses. <em>Three tracks.</em> One ladder.</h2>
<p class="lede">Every card shows the CEFR level, faculty, format, start date and tuition. Nothing hidden.</p></div>
<h3 class="mt2" style="margin-bottom:1.4rem">Il Corso · <em>structured, A0 to A2.2</em></h3><div class="grid g4">{''.join(card(c) for c in COURSES['ci'])}</div>
<h3 class="mt3" style="margin-bottom:1.4rem">Parliamo · <em>spoken, A0 to B1</em></h3><div class="grid g4">{''.join(card(c) for c in COURSES['ps'])}</div>
<h3 class="mt3" style="margin-bottom:1.4rem">Capsule culturali · <em>any level</em></h3><div class="grid g3">{''.join(card(c) for c in COURSES['cap'])}</div>
<div class="ctas center" style="justify-content:center"><a class="btn btn-ghost" href="courses.html">Compare every course <span class="arr">→</span></a></div></div></section>

<section class="dark"><div class="wrap"><div class="sec-head"><span class="eyebrow">The CEFR ladder</span><h2>From «ciao» to <em>full fluency.</em></h2>
<p class="lede">The Council of Europe's Common European Framework defines six levels by what you can do. Our syllabus is written against those descriptors, rung by rung.</p></div>
{ladder()}<p class="note">The current catalog covers A0 to B1. B2 to C2 follow the same framework and are taught in advanced cohorts. <!-- TODO(owner): confirm whether B2, C1, C2 cohorts are offered, and when. --> <a class="link" href="curriculum.html">Read the full curriculum</a></p></div></section>

<section class="hero" style="min-height:86svh">{vid('ag-tuscany-drone')}<div class="wrap"><span class="eyebrow">Method</span>
<h2 style="color:#fff;max-width:16ch">The city is part of <em style="color:var(--oro-soft)">the syllabus.</em></h2>
<p class="lede">Each unit is anchored in a real Italian place: a Roman bar, a Florentine workshop, a Bolognese market. Language is learned where it is lived.</p>
<div class="ctas"><a class="btn btn-ghost" href="method.html">How we teach <span class="arr">→</span></a></div></div></section>

<section><div class="wrap"><div class="sec-head"><span class="eyebrow">How it works</span><h2>Five steps <em>to your certificate.</em></h2></div>
<ol class="steps">{''.join(f'<li class="rv"><h4>{a}</h4><p>{b}</p></li>' for a,b in [('Placement','A short spoken conversation with a teacher places you on the right CEFR rung.'),('Enrol','Choose a course, a cohort and a schedule. Receive the syllabus PDF.'),('Live lessons','Twenty live lessons with your teacher and ten to twelve classmates.'),('Practise','Rehearse with Biagio and the recording library between lessons.'),('Certify','Can-do assessment and a CEFR-mapped certificate. Optional CILS or CELI preparation.')])}</ol></div></section>

<section class="verde"><div class="wrap split rev">
<div class="rv"><span class="eyebrow">Certification</span><h2>Prepared for <em style="color:var(--oro-soft)">CILS and CELI.</em></h2>
<p class="lede mt2">Italy's two major certifications of Italian as a foreign language are CILS, from the Università per Stranieri di Siena, and CELI, from the Università per Stranieri di Perugia. From A2 upward, our courses can include structured exam preparation for both.</p>
<p class="mt1">You sit the exam at an authorised exam centre. We make sure you walk in ready.</p>
<div class="ctas"><a class="btn btn-ghost" href="certifications.html">Certification preparation <span class="arr">→</span></a></div></div>
<figure class="frame wide rv"><img src="assets/img/v17/life-uffizi-hall.jpg" alt="The Uffizi gallery corridor in Florence"></figure></div></section>

<section><div class="wrap"><div class="sec-head"><span class="eyebrow">Faculty</span><h2>Seven native teachers. <em>Seven Italian cities.</em></h2>
<p class="lede">Each teacher teaches from the city they live in, so a year with us is also a year of Italian accents, kitchens and streets.</p></div>
<!-- TODO(owner): teacher names, photos and credentials are v16 pitch composites. Replace with the real eTeacher Italian faculty before launch. -->
<div class="grid g4">{''.join(f'<a class="tch rv" href="pages/teachers/{s}.html"><div class="ph"><img loading="lazy" src="assets/img/teacher-{s}.jpg" alt="{n}"></div><h3>{n}</h3><p>{c}</p></a>' for s,n,c in [('marco','Marco Rinaldi','Roma · DITALS II'),('chiara','Chiara Bellini','Firenze · DITALS II'),('giulia','Giulia Moretti','Bologna · DITALS II'),('alessandro','Alessandro Ferri','Milano · DITALS II')])}</div>
<div class="ctas"><a class="link" href="teachers.html">Meet all seven teachers</a></div></div></section>

<section class="bg-ivory"><div class="wrap split">
<figure class="rv" style="text-align:center"><img src="assets/img/biagio-3d-hero.png" alt="Biagio, the Club Italia AI tutor" style="max-height:520px;margin:auto"></figure>
<div class="rv"><span class="eyebrow">AI tutor · always online</span><h2>Meet <em>Biagio.</em></h2>
<p class="lede mt2">Practise Italian at any hour with an AI conversation tutor trained on the Club Italia syllabus. He speaks with a real Italian voice, corrects your grammar and explains why.</p>
<p class="mt1">Biagio supports your teacher. He never replaces one. Included with every course.</p>
<div class="ctas"><a class="btn btn-primary" href="biagio.html">Meet Biagio <span class="arr">→</span></a></div></div></div></section>

<section><div class="wrap"><div class="sec-head"><span class="eyebrow">Culture</span><h2>Culture speaks Italian. <em>So will you.</em></h2></div>
<div class="mosaic">{''.join(f'<a class="rv" href="{h}"><img src="assets/img/v17/{i}" alt="{t}"><span>{t}</span></a>' for h,i,t in [('pages/culture/pillar-art.html','life-uffizi-hall.jpg','Art and architecture'),('pages/culture/pillar-food.html','life-trattoria-toscana.jpg','La cucina'),('pages/culture/pillar-opera.html','life-scala-milano.jpg',"L'opera"),('pages/culture/pillar-travel.html','life-amalfi-coast.jpg','Il viaggio'),('pages/culture/pillar-cinema.html','life-caffe-roma.jpg','Il cinema'),('pages/culture/pillar-tradition.html','life-gondola-venezia.jpg','Tradizioni')])}</div></div></section>

<section class="bg-cream"><div class="wrap narrow"><div class="sec-head"><span class="eyebrow">Questions</span><h2>The questions <em>we hear most.</em></h2></div>{faq_html(FAQ[:2])}
<div class="ctas"><a class="link" href="faq.html">All questions</a></div></div></section>
{band('Your Italian begins <em>with a conversation.</em>','Fifteen minutes with a teacher is enough to place you and plan your start. Seven day full refund from your first live lesson.')}
'''
page('index.html','Club Italia · Learn Italian, live from Italy','Live Italian classes with native teachers in Italy. Small groups, a CEFR-aligned syllabus from A0 to B1, CILS and CELI preparation.', home)

# ================= COURSES =================
def track(title, sub, text, key, cols):
    return f'<div class="track"><div class="rv"><span class="eyebrow">{sub}</span><h2 style="font-size:2.4rem">{title}</h2><p class="mt1">{text}</p></div><div class="grid {cols}">{"".join(card(c) for c in COURSES[key])}</div></div>'
courses = f'''<section class="page-hero img"><img src="assets/img/ag-san-gimignano-poster.jpg" alt=""><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Courses</div>
<span class="eyebrow">Autumn 2026 · Eleven live courses</span><h1>Every course. <em>Every level.</em></h1><p class="lede">Three tracks, one CEFR ladder. Start with the structured course, add a spoken track, deepen with a cultural capsule.</p></div></section>
<section><div class="wrap">
{track('Il Corso','Track 01 · Structured','The full CEFR arc from A0 to A2.2 in four courses. Grammar, vocabulary, listening, reading and writing, each unit set in a real Italian city.','ci','g2')}
{track('Parliamo','Track 02 · Spoken','Conversation-first sessions on four Italian scenes. For learners who want fluency and confidence, from A0 to B1.','ps','g2')}
{track('Capsule culturali','Track 03 · Culture','Six sessions on a single cultural world: the table, the Renaissance, the opera. Open to any level.','cap','g3')}
</div></section>
<section class="bg-ivory"><div class="wrap"><div class="sec-head"><span class="eyebrow">At a glance</span><h2>Compare <em>the catalog.</em></h2></div><div class="tbl-wrap rv"><table class="syl"><thead><tr><th>Code</th><th>Course</th><th>CEFR</th><th>Format</th><th>Faculty</th><th>Syllabus</th></tr></thead><tbody>
{''.join(f'<tr><td>{clean(D[c[0]]["code"])}</td><td><a href="{c[6]}">{html.escape(c[1])}</a></td><td>{c[2]}</td><td>{clean(D[c[0]]["hours"]).replace(" × "," of ")}</td><td>{c[3]}, {c[4]}</td><td><a class="link" href="pdf/{c[0]}-syllabus.pdf">PDF</a></td></tr>' for k in COURSES for c in COURSES[k])}
</tbody></table></div>
<!-- TODO(owner): lesson length differs across v16 (85 min in course data and PDFs vs ninety minutes on the old homepage). Confirm the real lesson length. -->
<p class="note">Lesson lengths follow the published syllabi. Start dates and tuition are for the Autumn 2026 cohorts.</p></div></section>
{band('Not sure <em>where to start?</em>','A placement conversation with a teacher puts you on the right rung of the ladder.','ag-medieval-aerial')}'''
page('courses.html','Courses · Club Italia','Eleven live Italian courses across three tracks, mapped to the CEFR from A0 to B1.', courses)

# ================= CURRICULUM =================
SYL = [
 ('A1','Breakthrough','Basic user','CI Principiante, CI Elementare, Al Caffè',
  ['Introduce yourself and others','Order food and drink, pay, ask prices','Ask for and follow simple directions','Fill in a form, write a short message'],
  ['Sound system and spelling','Articles, gender and number','Present tense: regular, essere, avere, fare','Possessives, c\'è / ci sono, piacere'],
  ['Greetings and the bar ritual','Family and the Italian home','Rome: piazze, fontane, quartieri']),
 ('A2','Waystage','Basic user','CI Intermedio, CI Avanzato, A Tavola, In Viaggio',
  ['Describe past experiences and routines','Handle travel, hotels, trains, shops','Make arrangements and invitations','Write a simple personal letter'],
  ['Passato prossimo and imperfetto','Reflexive verbs, direct and indirect pronouns','Futuro semplice, comparatives','Polite imperative, ci and ne'],
  ['Florence and the Tuscan table','Bologna: markets and portici','Regional food and festivals']),
 ('B1','Threshold','Independent user','Chiacchierando',
  ['Hold a conversation on familiar topics','Give and justify opinions','Narrate a story, a film, a book','Write a structured letter or short essay'],
  ['Condizionale presente','Introduction to the congiuntivo presente','Combined pronouns, relative pronouns','Trapassato prossimo, connectors'],
  ['Italian cinema and song','Work and daily life in Milan','The language of citizenship and bureaucracy']),
 ('B2','Vantage','Independent user','Advanced cohort',
  ['Argue a position and weigh alternatives','Follow news, podcasts and talk shows','Read contemporary fiction and journalism','Write a reasoned argumentative text'],
  ['Congiuntivo: all tenses and concordance','Periodo ipotetico, all three types','Passive and si passivante','Gerund, participle, infinitive clauses'],
  ['Contemporary Italian literature','Italian press and politics','Design, fashion and industry']),
 ('C1','Effective operational proficiency','Proficient user','Advanced cohort',
  ['Express yourself fluently and spontaneously','Use Italian for professional and academic purposes','Produce clear, detailed, well-structured texts','Recognise implicit meaning and register'],
  ['Passato remoto in narrative','Stylistic word order, discourse markers','Formal and bureaucratic register','Idiom, proverbs, collocation'],
  ['Dante, Petrarca, Boccaccio in context','Art history in Italian','Opera libretti']),
 ('C2','Mastery','Proficient user','Advanced cohort',
  ['Understand virtually everything heard or read','Summarise and reconstruct arguments from multiple sources','Express fine shades of meaning precisely','Work with literary and specialised texts'],
  ['Full command of literary tenses','Regional varieties and dialect awareness','Rhetoric and translation','Academic and legal Italian'],
  ['Literary seminar: Calvino, Morante, Eco','Regional Italy and its dialects','Translation workshop'])]
lv_html=''.join(f'''<details class="level rv"{' open' if i==0 else ''}><summary><span class="lv">{a}</span><div><h3>{b}</h3><small>{c} · {d}</small></div><span class="plus">+</span></summary>
<div class="inner"><div><h4>You can</h4><ul>{''.join(f"<li>{x}</li>" for x in e)}</ul></div><div><h4>Grammar focus</h4><ul>{''.join(f"<li>{x}</li>" for x in f)}</ul></div><div><h4>Culture and themes</h4><ul>{''.join(f"<li>{x}</li>" for x in g)}</ul></div></div></details>''' for i,(a,b,c,d,e,f,g) in enumerate(SYL))
units = D['ci1']['syllabus']
curr = f'''<section class="page-hero"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Curriculum</div><span class="eyebrow">Curriculum · CEFR A1 to C2</span>
<h1>A curriculum written <em>against the framework.</em></h1><p class="lede">The Common European Framework of Reference for Languages describes six levels by what a learner can do. Every Club Italia unit is written to move you one step along those descriptors, with stated objectives, grammar, vocabulary and a cultural setting.</p></div></section>
<section><div class="wrap"><div class="sec-head"><span class="eyebrow">Six levels</span><h2>The syllabus, <em>level by level.</em></h2><p class="lede">Open a level to see its can-do outcomes, grammar focus and cultural themes.</p></div>{lv_html}
<!-- TODO(owner): B2, C1, C2 content is a framework outline only; no live courses exist at those levels in the v16 catalog. Confirm offering, names, faculty and dates. -->
<p class="note">B2 to C2 are taught in advanced cohorts that follow the same framework. Hours per CEFR level vary by learner; the Council of Europe gives no fixed number.</p></div></section>
<section class="bg-ivory"><div class="wrap"><div class="sec-head"><span class="eyebrow">Sample syllabus · CI Principiante</span><h2>Twenty lessons, <em>one city.</em></h2><p class="lede">{html.escape(clean(D['ci1']['promise']))}</p></div>
<div class="tbl-wrap rv"><table class="syl"><thead><tr><th>Lesson</th><th>Unit</th><th>Content and setting</th></tr></thead><tbody>{''.join(f'<tr><td>{i+1:02d}</td><td><strong>«{html.escape(clean(u[0]))}»</strong></td><td>{html.escape(clean(u[1]))}</td></tr>' for i,u in enumerate(units))}</tbody></table></div>
<div class="ctas"><a class="btn btn-primary" href="pdf/ci1-syllabus.pdf">Download the PDF syllabus <span class="arr">→</span></a><a class="btn btn-ghost" href="courses.html">All eleven syllabi</a></div></div></section>
<section class="dark"><div class="wrap"><div class="sec-head"><span class="eyebrow">Assessment</span><h2>How progress <em>is measured.</em></h2></div><div class="grid g4">
{''.join(f'<div class="pillar rv"><div class="num">0{i+1}</div><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate([('Placement','A spoken conversation and short written task, rated against CEFR descriptors.'),('Continuous','Teacher feedback in every lesson and a personal note on your progress.'),('Milestone','A mid-course review lesson with oral presentation and short test.'),('Final','Oral and written can-do assessment, leading to a CEFR-mapped certificate.')]))}</div></div></section>
{band('Find <em>your level.</em>','Book a placement conversation and receive a recommended starting course.','ag-venice-gondola')}'''
page('curriculum.html','Curriculum A1 to C2 · Club Italia','The Club Italia Italian curriculum mapped to the CEFR, from A1 to C2, with can-do outcomes, grammar and culture per level.', curr, light=True)

# ================= METHOD =================
method = f'''<section class="page-hero img"><img src="assets/img/ag-chefs-street-poster.jpg" alt=""><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Method</div><span class="eyebrow">Our method</span>
<h1>You don't study Italian. <em>You act in it.</em></h1><p class="lede">An action-oriented, communicative method aligned with the Common European Framework. Every lesson ends with something you can do in Italian that you could not do before.</p></div></section>
<section><div class="wrap"><div class="grid g3">
{''.join(f'<div class="pillar rv"><div class="num">0{i+1}</div><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate([
('Learning by doing','The CEFR treats the learner as a social agent who uses language to get things done. Each lesson is built around a task: ordering, booking, negotiating, persuading.'),
('Situated in a place','Every unit is anchored in a real Italian city and setting, so vocabulary arrives with its context, its gestures and its manners.'),
('Culture at the core','Art, food, opera, cinema and daily ritual are not extras. They are the material the language is taught through.')]))}
</div></div></section>
<section class="bg-ivory"><div class="wrap split"><figure class="frame rv"><img src="assets/img/v17/zoom-classroom-marco.jpg" alt="A teacher leading a live online Italian class"></figure>
<div class="rv"><span class="eyebrow">Anatomy of a lesson</span><h2>One lesson, <em>five movements.</em></h2>
<ol class="steps mt2" style="grid-template-columns:1fr">{''.join(f'<li><h4>{a}</h4><p>{b}</p></li>' for a,b in [('Riscaldamento','A warm-up conversation that recycles last lesson\'s language.'),('Input','Authentic material from the city: a menu, a clip, a sign, a dialogue.'),('Focus on form','The grammar point, explained precisely and practised in context.'),('Task','Pairs and small groups complete a real-world task in Italian.'),('Feedback','Personal correction from the teacher and a short summary for Biagio practice.')])}</ol></div></div></section>
<section class="dark"><div class="wrap narrow"><div class="sec-head"><span class="eyebrow">References</span><h2>The research <em>behind the method.</em></h2></div>
<ul class="rv" style="list-style:none;display:grid;gap:1rem"><li>Council of Europe (2020). <em>Common European Framework of Reference for Languages: Companion Volume.</em></li><li>Piccardo, E. and North, B. (2019). <em>The Action-oriented Approach.</em> Multilingual Matters.</li><li>Università per Stranieri di Siena. CILS certification descriptors.</li><li>Università per Stranieri di Perugia. CELI certification descriptors.</li></ul>
<p class="note">Club Italia is independent and is not affiliated with, nor endorsed by, the institutions cited.</p></div></section>
{band('See the method <em>in a real class.</em>','Watch a recorded Club Italia lesson, then book your placement.','ag-chefs-street')}'''
page('method.html','Method · Club Italia','The Club Italia action-oriented, CEFR-aligned method for learning Italian live.', method)

# ================= CERTIFICATIONS =================
cert = f'''<section class="page-hero"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Certification</div><span class="eyebrow">Certification</span>
<h1>Certified progress. <em>Exam-ready Italian.</em></h1><p class="lede">Two kinds of certificate matter to our learners: the Club Italia certificate you earn at the end of each course, and the external CILS and CELI examinations that Italian universities and authorities recognise.</p></div></section>
<section><div class="wrap grid g2">
<div class="plan rv"><span class="tag">Included</span><h3>Club Italia certificate</h3><p>Issued at the end of every course, stating the CEFR level reached on the basis of oral and written can-do assessment. A school certificate, signed by eTeacher Group.</p></div>
<div class="plan feat rv"><span class="tag">Preparation</span><h3>CILS and CELI</h3><p>Structured preparation for the two major Italian state-recognised certifications, built into courses from A2 upward and available as focused exam cohorts.</p></div></div>
<!-- TODO(owner): confirm whether dedicated CILS/CELI exam-prep cohorts exist, their price and schedule. -->
</div></section>
<section class="bg-ivory"><div class="wrap"><div class="sec-head"><span class="eyebrow">The exams</span><h2>CILS and CELI, <em>side by side.</em></h2></div><div class="tbl-wrap rv"><table class="syl"><thead><tr><th></th><th>CILS</th><th>CELI</th></tr></thead><tbody>
<tr><td>Issuer</td><td>Università per Stranieri di Siena</td><td>Università per Stranieri di Perugia</td></tr>
<tr><td>Levels</td><td>A1 to C2</td><td>A1 to C2</td></tr>
<tr><td>Skills</td><td>Listening, reading, writing, speaking</td><td>Listening, reading, writing, speaking</td></tr>
<tr><td>Typical use</td><td>University entry, work, citizenship (B1)</td><td>University entry, work, citizenship (B1)</td></tr>
<tr><td>Where</td><td colspan="2">At an authorised exam centre, in Italy or abroad. Club Italia is not an exam centre.</td></tr></tbody></table></div>
<p class="note">Exam rules, dates and fees are set by the issuing universities and change from year to year. Always check the official CILS and CELI websites before booking.</p></div></section>
<section><div class="wrap"><div class="sec-head"><span class="eyebrow">How we prepare you</span><h2>Four parts <em>of exam readiness.</em></h2></div><div class="grid g4">
{''.join(f'<div class="pillar rv"><div class="num">0{i+1}</div><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate([('Format','Each paper explained, with timing and marking criteria.'),('Practice papers','Timed practice on past-style tasks for every skill.'),('Speaking rehearsal','Mock oral exams with your teacher, recorded for review.'),('Written feedback','Corrected essays and letters against the exam rubric.')]))}</div></div></section>
{band('Aiming for <em>B1 citizenship Italian?</em>','Tell an advisor your goal and timeline. We will map the path from your current level.','ag-rome-basilica')}'''
page('certifications.html','CILS and CELI preparation · Club Italia','Club Italia CEFR certificates and preparation for the CILS and CELI Italian examinations.', cert, light=True)

# ================= TEACHERS =================
T=[('marco','Marco Rinaldi','Roma','Lazio'),('chiara','Chiara Bellini','Firenze','Toscana'),('giulia','Giulia Moretti','Bologna','Emilia-Romagna'),('alessandro','Alessandro Ferri','Milano','Lombardia'),('francesca','Francesca Zeno','Venezia','Veneto'),('luca','Luca De Simone','Napoli','Campania'),('sofia','Sofia Mazzara','Palermo','Sicilia')]
teach = f'''<section class="page-hero img"><img src="assets/img/v17/city-firenze.jpg" alt=""><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Faculty</div><span class="eyebrow">The faculty</span>
<h1>Seven native teachers. <em>Seven Italian cities.</em></h1><p class="lede">Every teacher is a native Italian, qualified to teach Italian as a foreign language, and teaches from the city they live in.</p></div></section>
<section><div class="wrap">
<!-- TODO(owner): faculty are v16 pitch composites (names, photos, DITALS credentials). Replace with real teachers and verified qualifications. -->
<div class="grid g4">{''.join(f'<a class="tch rv" href="pages/teachers/{s}.html"><div class="ph"><img loading="lazy" src="assets/img/teacher-{s}.jpg" alt="{n}"></div><span class="tag">{r}</span><h3>{n}</h3><p>{c} · DITALS II</p></a>' for s,n,c,r in T)}</div></div></section>
<section class="bg-ivory"><div class="wrap"><div class="sec-head"><span class="eyebrow">Standards</span><h2>How the faculty <em>is chosen.</em></h2></div><div class="grid g3">
{''.join(f'<div class="pillar rv"><h3>{a}</h3><p>{b}</p></div>' for a,b in [('Qualified','A recognised qualification in teaching Italian to foreigners, such as DITALS or CEDILS.'),('Experienced','Years of teaching adult learners before joining the school.'),('Auditioned','A live audition lesson with real adult learners before hiring.')])}</div></div></section>
{band('Meet your teacher <em>before you enrol.</em>','Your placement conversation is with a member of the faculty.','ag-venice-docked')}'''
page('teachers.html','Faculty · Club Italia','Seven native Italian teachers teaching live from seven Italian cities.', teach)

# ================= PRICING =================
pr = f'''<section class="page-hero"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Tuition</div><span class="eyebrow">Tuition · billed in US dollars</span>
<h1>One curriculum. <em>Three ways to pay.</em></h1><p class="lede">Every plan gives you the full live curriculum on your track. The only choice is the length of your commitment.</p></div></section>
<!-- TODO(owner): all tuition figures are v16 pitch placeholders pending eTeacher sign-off. -->
<section><div class="wrap grid g3">
<div class="plan rv"><span class="tag">Monthly</span><h3>Monthly</h3><div class="price">$84 <small>/ week</small></div><p>Billed $336 monthly. Cancel any time after the first month.</p><ul><li>All live lessons on your track</li><li>Biagio, the AI tutor</li><li>Class recordings</li><li>Cultural library</li></ul><a class="btn btn-ghost" href="contact.html">Start monthly</a></div>
<div class="plan feat rv"><span class="badge">Best value</span><span class="tag">Annual</span><h3>Annual</h3><div class="price">$62 <small>/ week</small></div><p>Billed once at $3,224 for the year. Save 26 percent on the monthly rate.</p><ul><li>Everything in monthly</li><li>Two cultural capsule sessions</li><li>Priority teacher placement</li><li>Printed CEFR certificate</li></ul><a class="btn btn-gold" href="contact.html">Start annual</a></div>
<div class="plan rv"><span class="tag">Term</span><h3>One term</h3><div class="price">$73 <small>/ week</small></div><p>Billed $876 for a twelve-week term. No auto-renewal.</p><ul><li>All lessons of one term</li><li>Biagio for the term</li><li>Placement included</li><li>End of stage certificate</li></ul><a class="btn btn-ghost" href="contact.html">Start a term</a></div>
</div><p class="note wrap" style="margin-inline:auto">Cultural capsules: $390 for six sessions. Seven day full refund from your first live lesson, on every plan.</p></section>
<section class="bg-cream"><div class="wrap narrow">{faq_html([FAQ[2]])}</div></section>
{band('Questions <em>about tuition?</em>','An advisor will walk you through plans and start dates.','ag-wine-bottles')}'''
page('pricing.html','Tuition · Club Italia','Club Italia tuition plans for live Italian classes.', pr, light=True)

# ================= FAQ =================
page('faq.html','FAQ · Club Italia','Answers about Club Italia courses, levels, certification and practicalities.', f'''<section class="page-hero"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / FAQ</div><span class="eyebrow">Frequently asked</span><h1>Everything worth asking <em>before you enrol.</em></h1></div></section>
<section><div class="wrap narrow">{faq_html(FAQ)}</div></section>{band('Still <em>a question?</em>','Write to an advisor. Every message is answered by a person.','ag-camogli-coast')}''', light=True)

# ================= CONTACT =================
page('contact.html','Contact · Club Italia','Speak with a Club Italia advisor.', f'''<section class="page-hero"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Contact</div><span class="eyebrow">Contact</span><h1>Speak with <em>an advisor.</em></h1><p class="lede">Tell us about your Italian and your goals. An advisor will plan your placement conversation.</p></div></section>
<section><div class="wrap split" style="align-items:start">
<!-- TODO(owner): phone numbers, WhatsApp and office addresses are carried over from v16 and should be verified. Form is front-end only (no CRM). -->
<div class="contact-list rv"><div><h4>Email</h4><a href="mailto:advisor@eTeacherGroup.com">advisor@eTeacherGroup.com</a></div><div><h4>Phone, United States</h4><p>+1 800 246 3541</p></div><div><h4>Phone, United Kingdom</h4><p>+44 20 3868 1810</p></div><div><h4>WhatsApp</h4><p>+972 3 763 8130</p></div><div><h4>Office</h4><p>eTeacher Group, Kfar Neter 4059300, Israel</p></div><div><h4>Hours</h4><p>Mon to Fri, 08:00 to 20:00 US Eastern</p></div></div>
<form class="form rv" data-demo><label>Name<input required name="name" autocomplete="name"></label><label>Email<input required type="email" name="email" autocomplete="email"></label><label>Phone<input name="phone" autocomplete="tel"></label>
<label>Your Italian right now<select name="level"><option>I don't speak any Italian yet</option><option>A few words · A1</option><option>Some basics · A2</option><option>Conversational · B1 or above</option></select></label>
<label>Your goal<select name="goal"><option>Travel and culture</option><option>Family and heritage</option><option>Citizenship (B1, CILS or CELI)</option><option>Work or study</option></select></label>
<button class="btn btn-primary" type="submit">Request my consultation <span class="arr">→</span></button></form></div></section>''', light=True)
print('built')
