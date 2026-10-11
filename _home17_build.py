import json,re,html
D=json.load(open('research/course-data.json'))
def cl(s): return re.sub(r'\s*[—–]\s*',', ',s).replace('→','to')
E=html.escape
def V(n,pre='none',auto=True,cls='',poster=None):
    p=poster or f'assets/img/{n}-poster.jpg'
    return f'<video class="{cls}" {"autoplay " if auto else ""}muted loop playsinline webkit-playsinline preload="{pre}" poster="{p}" data-src="assets/video/{n}.mp4" aria-hidden="true"></video>'
C=[('ci','ci1','CI Principiante','A0 to A1.1','Marco Rinaldi','Roma','course-ci1.jpg','pages/courses/ci1.html','Oct 6, 2026','$62 a week'),
('ci','ci2','CI Elementare','A1.1 to A1.2','Chiara Bellini','Firenze','course-ci2.jpg','pages/courses/ci2.html','Oct 6, 2026','$62 a week'),
('ci','ci3','CI Intermedio','A1.2 to A2.1','Giulia Moretti','Bologna','course-ci3.jpg','pages/courses/ci3.html','Oct 6, 2026','$62 a week'),
('ci','ci4','CI Avanzato','A2.1 to A2.2','Luca De Simone','Napoli','course-ci4.jpg','pages/courses/ci4.html','Oct 6, 2026','$62 a week'),
('ps','ps1','Al Caffè','Spoken A0 to A1','Marco Rinaldi','Roma','spoken-ps1.jpg','pages/spoken/ps1.html','Oct 6, 2026','$62 a week'),
('ps','ps2','A Tavola','Spoken A1 to A2','Chiara Bellini','Firenze','spoken-ps2.jpg','pages/spoken/ps2.html','Oct 6, 2026','$62 a week'),
('ps','ps3','In Viaggio','Spoken A2','Francesca Zeno','Venezia','spoken-ps3.jpg','pages/spoken/ps3.html','Oct 6, 2026','$62 a week'),
('ps','ps4','Chiacchierando','Spoken A2 to B1','Alessandro Ferri','Milano','spoken-ps4.jpg','pages/spoken/ps4.html','Oct 6, 2026','$62 a week'),
('cap','cap-food','La Cucina','Any level','Giulia Moretti','Bologna','cap-food.jpg','pages/culture/cap-food.html','Oct 20, 2026','$390'),
('cap','cap-art',"L'Arte",'Any level','Chiara Bellini','Firenze','cap-art.jpg','pages/culture/cap-art.html','Oct 20, 2026','$390'),
('cap','cap-opera',"L'Opera",'Any level','Alessandro Ferri','Milano','cap-opera.jpg','pages/culture/cap-opera.html','Oct 20, 2026','$390')]
def cc(c):
    t,k,n,lv,f,city,img,href,st,tu=c;d=D[k]
    fmt=cl(d['hours']).replace(' × ',' of ')
    pr=cl(d['promise']).split('. ')[0].rstrip('.')+'.'
    return f'''<a class="cc rv" data-t="{t}" href="{href}"><div class="ph"><img loading="lazy" src="assets/img/{img}" alt="{E(n)}, taught from {city}"><span class="lv">{lv}</span><span class="city">{city}</span></div>
<div class="bd"><span class="code">{cl(d['code'])}</span><h3>{E(n)}</h3><p>{E(pr)}</p><dl><dt>Faculty</dt><dd>{f}</dd><dt>Format</dt><dd>{fmt}</dd><dt>Starts</dt><dd>{st}</dd><dt>Tuition</dt><dd>{tu}</dd></dl>
<div class="go"><span>View course</span><span>→</span></div></div></a>'''
T=[('marco','Marco Rinaldi','Roma'),('chiara','Chiara Bellini','Firenze'),('giulia','Giulia Moretti','Bologna'),('alessandro','Alessandro Ferri','Milano'),('francesca','Francesca Zeno','Venezia'),('luca','Luca De Simone','Napoli'),('sofia','Sofia Mazzara','Palermo')]
TS=[('student-01-sarah.jpg','Sarah T.','Verified learner','Marco is a great teacher. Small class, everyone speaks, and you actually leave every lesson able to say something new.'),
('student-diane.jpg','Diane Weller','Chicago · CI Principiante','In three months I ordered dinner in Trastevere and the waiter answered in Italian for the whole meal.'),
('student-03-elena.jpg','Elena R.','Verified learner','Chiara teaches from a Florentine studio. You hear the city. The accent training is unreal.'),
('student-robert.jpg','Robert Hensley','Austin · A Tavola','The teacher cooks while she teaches. That single fact changed how I hear the language.'),
('student-02-david.jpg','David L.','Verified learner','Twelve people in class, all adults, all serious. Best language school I have used, and I have tried a few.'),
('student-sarah.jpg','Sarah Kim',"San Francisco · L'Opera",'I read the libretto of La Bohème with Alessandro over six sessions. I now understand why Italians cry at the third act.'),
('student-james.jpg','James Whitaker','London · CI Elementare','Small classes, real corrections, no drills. It felt like being tutored at a Florentine institute.'),
('student-linda.jpg','Linda Bauer','Toronto · CI Intermedio','Chiara caught a mistake I had been making since 2014. In one live class.')]
CITIES=[('roma','Roma','Al Caffè · CI Principiante'),('firenze','Firenze','A Tavola · CI Elementare · L\'Arte'),('bologna','Bologna','CI Intermedio · La Cucina'),('milano','Milano',"Chiacchierando · L'Opera"),('venezia','Venezia','In Viaggio'),('napoli','Napoli','CI Avanzato'),('palermo','Palermo','Sicilian culture')]
VO=[('biagio-line-caffe','Al caffè','«Un cappuccino e un cornetto, per favore.»'),('biagio-line-tavola','A tavola','«Prendo la pasta alla carbonara. Grazie.»'),('biagio-line-strada','Per strada',"«Mi scusi, dov'è la stazione della metropolitana?»"),('biagio-line-corregge','Correzione',"«Si dice "+"'sono andato', non 'ho andato'.»")]
FAQ=[('Are the classes live or pre-recorded?','Every class is live, with a native teacher broadcasting from Italy. Recordings are a revision tool, never a substitute.'),
('How big are the groups?','Ten to twelve adult learners. Small enough that everyone speaks in every lesson and the teacher corrects each learner individually.'),
('Can I watch classes later?','Yes. Every class is recorded and added to your library, so a missed lesson is never lost.'),
('What does a full course include?','Twenty live lessons (six for a cultural capsule), the PDF syllabus, class recordings, Biagio the AI tutor between lessons, and a CEFR-mapped certificate at the end.'),
('Do you prepare for CILS and CELI?','Yes. From A2 upward, courses can include exam technique for CILS (Università per Stranieri di Siena) and CELI (Università per Stranieri di Perugia). You sit the exam at an authorised exam centre; Club Italia is not one.'),
('How much does it cost?','From $62 a week on the annual plan, $73 a week by term, or $84 a week monthly. Seven day full refund from your first live lesson.'),
('Who teaches the classes?','Native Italian teachers qualified to teach Italian as a foreign language, each broadcasting from their own city.')]

h=[]
h.append('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Club Italia · Learn Italian, live from Italy</title>
<meta name="description" content="Club Italia by eTeacher: live Italian classes with native teachers broadcasting from seven Italian cities. Small groups, CEFR-aligned syllabus, CILS and CELI preparation, Biagio AI tutor.">
<meta name="theme-color" content="#0b1220"><meta property="og:title" content="Club Italia · Learn Italian, live from Italy"><meta property="og:image" content="assets/img/ag-roma-statue-poster.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="preload" as="image" href="assets/img/ag-roma-statue-poster.jpg"><link rel="stylesheet" href="css/home17.css"></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="hdr"><div class="w"><a class="brand" href="index.html" aria-label="Club Italia home"><span class="bn">Club Italia</span><span class="by">by <img src="assets/img/eteacher-real-logo-white.png" alt="eTeacher Group"></span></a>
<nav class="nav" aria-label="Primary"><a href="courses.html">Courses</a><a href="how-it-works.html">How it works</a><a href="method.html">Method</a><a href="teachers.html">Faculty</a><a href="culture.html">Culture</a><a href="biagio.html">Biagio AI</a><a href="pricing.html">Tuition</a><a href="#enrol" class="btn btn-gold">Enrol now</a></nav>
<button class="burger" aria-label="Open menu" aria-expanded="false"><i></i><i></i><i></i></button></div></header>
<main id="main">''')
# HERO
h.append(f'''<section class="hero">
<video autoplay muted loop playsinline webkit-playsinline preload="auto" poster="assets/img/ag-roma-statue-poster.jpg" aria-hidden="true"><source src="assets/video/ag-roma-statue.mp4" type="video/mp4"></video>
<div class="w"><div class="hero-badges"><span class="chip g">Live from Italy</span><span class="chip">by eTeacher Group</span><span class="chip">Autumn cohort · Oct 6</span></div>
<h1>Learn Italian. <em>Live from Italy.</em></h1>
<p class="lede">An exclusive, culturally immersive, live Italian school for adult learners. Native teachers in seven Italian cities. Ten to twelve learners per class. A CEFR-aligned syllabus and a certificate at the end.</p>
<div class="ctas"><a class="btn btn-gold" href="#enrol">Reserve my seat · $62 a week <span class="arr">→</span></a><a class="btn btn-line" href="#level">Find my level</a></div>
<!-- TODO(owner): Trustpilot score is a v16 pitch placeholder. -->
<div class="tp"><span class="stars"><i>★</i><i>★</i><i>★</i><i>★</i><i>★</i></span><span><b>Excellent</b> · 4.8 on Trustpilot</span></div></div>
<button class="music" id="music" aria-pressed="false">♪ Music off</button><audio id="theme" src="assets/audio/hero-italian-theme.mp3" preload="none" loop></audio>
<span class="scrollcue">Scroll</span></section>
<a class="pill" href="#enrol"><span><small>Open enrolment</small>Autumn cohorts · live from Italy</span><span class="btn btn-gold">Enrol</span></a>
<!-- TODO(owner): founding year, learner count and review score are v16 placeholders; confirm with eTeacher. -->
<div class="trust"><div class="w"><div><b>2004</b>eTeacher since</div><div><b>12,847</b>learners</div><div><b>4.8 ★</b>Trustpilot</div><div><b>7</b>Italian cities</div><div><b>10 to 12</b>per class</div><div><b>A0 to B1</b>CEFR ladder</div></div></div>''')
# COURSES
h.append(f'''<section class="sec ivory" id="courses"><div class="w"><div class="head rv"><span class="eb">Our courses</span><h2>Choose your path. <em>Start speaking Italian.</em></h2>
<p>Eleven CEFR-aligned courses in three collections. Live, small group, certified, broadcast from Italy.</p></div>
<div class="cols2">
<div class="coll a rv"><span class="best">Best seller</span><span class="big">01</span><span class="k">Collection 01 · Structured</span><h3>Il Corso</h3><p>Structured language and culture, city by city.</p><div class="st"><div><b>4</b><span>Courses</span></div><div><b>A0 to A2.2</b><span>CEFR</span></div><div><b>20</b><span>Lessons</span></div><div><b>85 min</b><span>Live</span></div></div><button class="btn" data-go="ci">Explore the 4 courses ↓</button></div>
<div class="coll b rv"><span class="big">02</span><span class="k">Collection 02 · Spoken</span><h3>Parliamo</h3><p>Spoken fluency first, on four Italian scenes.</p><div class="st"><div><b>4</b><span>Courses</span></div><div><b>A0 to B1</b><span>CEFR</span></div><div><b>20</b><span>Sessions</span></div><div><b>85 min</b><span>Live</span></div></div><button class="btn" data-go="ps">Explore the 4 courses ↓</button></div>
<div class="coll c rv"><span class="big">03</span><span class="k">Collection 03 · Culture</span><h3>Capsule culturali</h3><p>Six sessions inside the table, the Renaissance, the opera.</p><div class="st"><div><b>3</b><span>Capsules</span></div><div><b>Any</b><span>Level</span></div><div><b>6</b><span>Sessions</span></div><div><b>60 min</b><span>Live</span></div></div><button class="btn" data-go="cap">Explore the 3 capsules ↓</button></div></div>
<!-- TODO(owner): lesson length 85 min (course data, PDFs) vs ninety minutes (old v16 hero). Confirm. -->
<div class="tabs" role="group" aria-label="Filter courses" id="ctabs"><button aria-pressed="true" data-f="all">All 11 courses</button><button aria-pressed="false" data-f="ci">Il Corso</button><button aria-pressed="false" data-f="ps">Parliamo</button><button aria-pressed="false" data-f="cap">Capsule</button></div>
<div class="cgrid" id="cgrid">{''.join(cc(c) for c in C)}</div><p class="swipe c">Swipe the courses →</p>
<p class="center mt"><a class="btn btn-ghost" href="courses.html">Compare every course and syllabus <span class="arr">→</span></a></p></div></section>''')
# JOURNEY
steps=[('01','Step one','Assess and enrol','A short spoken placement conversation with a teacher, then an advisor call, puts you on the right rung.','Free placement'),
('02','Step two','Your syllabus','Receive the PDF syllabus: twenty lessons, each with objectives, grammar, vocabulary and a city setting.','Published in advance'),
('03','Step three','Live classes','Live lessons with a native teacher broadcasting from a real Italian city, in a group of ten to twelve.','Live from Italy'),
('04','Step four','Practise with Biagio','Between lessons, rehearse with Biagio, the AI tutor with a real Italian voice, and the recording library.','Always online'),
('05','The finish','CEFR certificate','Oral and written can-do assessment and a CEFR-mapped Club Italia certificate. CILS or CELI preparation from A2.','Certified')]
h.append(f'''<section class="sec paper" id="journey"><div class="w"><div class="head rv"><span class="eb">The learning journey</span><h2>From «Ciao» to <em>your CEFR certificate.</em></h2><p>Six named milestones, one clear arc of progress. You are placed by a spoken conversation, never a form.</p></div>
<div class="milestones rv">{''.join(f'<div>{a}<small>{b}</small></div>' for a,b in [('A0','«Ciao»'),('A1.1','Prime parole'),('A1.2','Vita quotidiana'),('A2.1','Sicuro'),('A2.2','Certificato'),('B1','Fluente')])}</div>
<div class="slider">{''.join(f'<article class="step rv"><span class="n">{a}</span><span class="s">{b}</span><h4>{c}</h4><p>{d}</p><span class="tag">{e}</span></article>' for a,b,c,d,e in steps)}</div><p class="swipe">Swipe the five steps →</p>
<p class="center mt"><a class="lnk" href="how-it-works.html">See the full journey</a></p></div></section>''')
# METHOD + LADDER
L=[('A1','Breakthrough','Introduce yourself, order, ask the way',38,True),('A2','Waystage','Narrate the past, travel, make plans',56,True),('B1','Threshold','Hold a conversation, give opinions',74,True),('B2','Vantage','Argue, follow the news, read fiction',92,False),('C1','Effective','Work and study in Italian',110,False),('C2','Mastery','Literary and specialised Italian',128,False)]
h.append(f'''<section class="sec dark" id="method"><div class="w"><div class="head rv"><span class="eb">A structured, CEFR-aligned curriculum</span><h2>A curriculum written by Italian language specialists, <em>against the European framework.</em></h2>
<p>Action-oriented, communicative learning, aligned with the Common European Framework of Reference. You do not study Italian. You act in it.</p></div>
<div class="pill3">{''.join(f'<div class="gcard rv"><span class="n">0{i+1}</span><p class="i">{a}</p><h3>{b}</h3><p>{c}</p></div>' for i,(a,b,c) in enumerate([('Imparare facendo','You act, you speak','The CEFR treats the learner as a social agent. Every lesson is a task: ordering, booking, negotiating, persuading.'),('Lingua in situ','Learned where it is lived','Every unit is anchored in a real Italian place: a Roman bar, a Florentine workshop, a Bolognese market.'),('La cultura al centro','Culture at the core','Art, food, opera and cinema are the material the language is taught through, with can-do assessment at every milestone.')]))}</div>
<div class="ladder rv" aria-label="CEFR levels A1 to C2">{''.join(f'<div class="rung{" on" if on else ""}" style="height:{ht+60}px"><b>{a}</b><span>{b}</span><small>{c}</small></div>' for a,b,c,ht,on in L)}</div>
<div class="ladder-legend"><span>■ Gold: current catalog (A0 to B1)</span><span>B2 to C2: advanced cohorts on the same framework <!-- TODO(owner): confirm B2-C2 availability --></span><a class="lnk" href="curriculum.html">Full A1 to C2 curriculum</a></div>
<div class="refs rv"><span>2020 · Council of Europe, CEFR Companion Volume</span><span>2019 · Piccardo and North, The Action-oriented Approach</span><span>CILS · Università per Stranieri di Siena</span><span>CELI · Università per Stranieri di Perugia</span></div>
<p class="disc">Club Italia is independent and is not affiliated with, nor endorsed by, the institutions cited. Club Italia prepares learners for CILS and CELI but is not an official examination centre.</p></div></section>''')
# ZOOM MOCKUP
stu=['student-01-sarah','student-02-david','student-03-elena','student-04-michael','student-05-anna','student-06-jonathan']
names=['Sarah','David','Elena','Michael','Anna','Jonathan']
h.append(f'''<section class="sec paper" id="classroom"><div class="w split">
<div class="rv"><span class="eb">Inside a live class</span><h2>A real Italian classroom. <em>In your living room.</em></h2>
<p style="margin-top:1.2rem;font-size:1.06rem">Your teacher is in Rome, Florence or Venice. You are at home. Twelve adults, one native teacher, eighty-five minutes of Italian that you speak, not watch.</p>
<div class="feat6">{''.join(f'<div><h4>{a}</h4><p>{b}</p></div>' for a,b in [('Live from Italy','Broadcast from the teacher\'s own city.'),('Small groups','Ten to twelve learners. No exception.'),('Twenty lessons','Once or twice a week, at your pace.'),('Real Italian, lesson one','You order, argue, tell a story.'),('Recordings','Every class, added to your library.'),('CEFR certificate','Signed by eTeacher Group.')])}</div>
<p class="mt"><a class="btn btn-ink" href="sample-class.html">Watch a sample class <span class="arr">→</span></a></p></div>
<div class="laptop rv" aria-label="Illustration of a live Club Italia class on Zoom"><div class="zbar"><span class="rec">REC</span><span>Club Italia · CI Principiante · Lezione 07 «A che ora?»</span><span>12 participants</span></div>
<div class="zgrid"><div class="zt host"><img src="assets/img/teacher-marco.jpg" alt="Teacher Marco Rinaldi, live from Rome"><span>Marco · Roma (host)</span><div class="zcap">«Allora, a che ora ti svegli la mattina?»</div></div>
{''.join(f'<div class="zt"><img loading="lazy" src="assets/img/{s}.jpg" alt=""><span>{n}</span></div>' for s,n in zip(stu,names))}</div>
<div class="zctl"><i>Mute</i><i>Video</i><i>Breakout rooms</i><i>Chat</i><i>eTeacher</i><i class="leave">Leave</i></div></div></div></section>''')
# CULTURE VIDEO GRID
CU=[('ag-medieval-aerial','Arte e architettura','From Roman forums to Renaissance cupolas, learn the language inside the art that shaped it.','pages/culture/pillar-art.html'),
('ag-chefs-street','La cucina','A Bolognese market, a Neapolitan oven, a Tuscan table. Italian as it is lived and shared.','pages/culture/pillar-food.html'),
('ag-venice-gondola','Il viaggio','From the canals of Venice to the Amalfi coast, speak Italian where it is unforgettable.','pages/culture/pillar-travel.html'),
('ag-catania-statues','Il cinema','Fellini, Sorrentino and the piazza on screen. The stories at the heart of Italian culture.','pages/culture/pillar-cinema.html'),
('ag-rome-basilica',"L'opera e la musica",'Verdi, Puccini and Rossini. The music that carries the Italian language.','pages/culture/pillar-opera.html'),
('ag-tradition-festival','Le tradizioni','Carnevale, the Palio, the Festa della Repubblica. The heritage behind every word.','pages/culture/pillar-tradition.html')]
h.append(f'''<section class="sec dark" id="culture"><div class="w"><div class="head rv"><span class="eb">Culture</span><h2>Culture speaks Italian. <em>What about you?</em></h2>
<p>Club Italia teaches Italian through deep cultural engagement: art, the table, travel, cinema, opera and tradition, filmed in Italy.</p></div>
<div class="vgrid">{''.join(f'<a class="vt rv" href="{u}">{V(v)}<div class="tx"><span class="n">0{i+1}</span><h3>{t}</h3><p>{p}</p></div></a>' for i,(v,t,p,u) in enumerate(CU))}</div>
<p class="center mt"><a class="btn btn-ghost" href="culture.html">Explore the culture hub <span class="arr">→</span></a></p></div></section>''')
h.append('<div class="marq" aria-hidden="true"><div>'+''.join(f'<span>{w}</span>' for w in ['«Benvenuti»','Roma','Firenze','Bologna','Milano','Venezia','Napoli','Palermo','«Parliamo italiano»']*2)+'</div></div>')
# POWER STRIP
h.append('''<!-- TODO(owner): eTeacher group figures are v16 placeholders (v16 pages also cite 400,000 learners since 2000). Confirm one set. -->
<section class="power"><div class="w rv"><span class="eb">Presented by eTeacher Group</span><h2>A serious school, <em>not an app.</em> Twenty years of live teaching.</h2>
<div class="pst"><div><b>2004</b><span>Teaching live online</span></div><div><b>200,000</b><span>Alumni</span></div><div><b>16</b><span>Languages taught</span></div><div><b>CEFR</b><span>Aligned outcomes</span></div></div>
<div class="logos"><img src="assets/img/eteacher-real-logo-white.png" alt="eTeacher Group"><img src="assets/img/cefr-logo.png" alt="CEFR" onerror="this.remove()"><span>CILS preparation</span><span>CELI preparation</span></div></div></section>''')
# FACULTY
h.append(f'''<section class="sec ivory" id="faculty"><div class="w"><div class="head rv"><span class="eb">Meet our faculty</span><h2>Native teachers, <em>from every corner</em> of Italy.</h2>
<p>Rome, Florence, Bologna, Milan, Venice, Naples, Palermo. Each teacher lives and broadcasts from a different Italian city. Real accents, real kitchens, real streets.</p></div>
<div class="fchips rv"><span>✦ Native Italian teachers</span><span>✦ DITALS qualified</span><span>✦ Live from Italy</span><span>✦ Groups of 10 to 12</span></div>
<!-- TODO(owner): faculty are v16 composites; replace with real teachers and credentials. -->
<div class="fac">{''.join(f'<a class="ft rv" href="pages/teachers/{s}.html"><img loading="lazy" src="assets/img/teacher-{s}.jpg" alt="{n}"><div><b>{n}</b><small>{c}</small></div></a>' for s,n,c in T)}</div>
<p class="center mt"><a class="btn btn-ghost" href="teachers.html">Meet the full faculty <span class="arr">→</span></a></p></div></section>''')
# HEAR
h.append('''<section class="sec dark" id="taste"><div class="w"><div class="head rv"><span class="eb">Get a taste of Club Italia</span><h2>Hear a real class, <em>live from Italy.</em></h2><p>Turn the sound on and hear Club Italia for yourself.</p></div>
<div class="hear"><figure class="rv"><div class="hv"><video muted loop playsinline preload="none" poster="assets/img/class-demo-poster.jpg" data-src="assets/video/class-demo.mp4" data-autoplay></video><button class="snd" data-snd>🔈 Sound on</button></div><figcaption class="hcap"><p>«Allora, ragazzi, parliamo del fine settimana.»</p><small>A recorded Club Italia lesson</small></figcaption></figure>
<figure class="rv"><div class="hv"><video muted loop playsinline preload="none" poster="assets/img/ag-zoom-student-poster.jpg" data-src="assets/video/ag-zoom-student.mp4" data-autoplay></video><button class="snd" data-snd>🔈 Sound on</button></div><figcaption class="hcap"><p>Study from home. Speak like you live there.</p><small>A learner in a live class</small></figcaption></figure></div>
<p class="center mt"><a class="btn btn-ghost" href="sample-class.html">How classes work <span class="arr">→</span></a></p></div></section>''')
# CITIES
h.append(f'''<section class="sec paper" id="cities"><div class="w"><div class="head rv"><span class="eb">Seven cities, one Italian</span><h2>Follow your journey <em>across Italy.</em></h2><p>Italian is learned where it is lived: at the counter, in the market, on the vaporetto. Every course is anchored in a city.</p></div>
<div class="cities">{''.join(f'<a class="city rv" href="map.html"><img loading="lazy" src="assets/img/v17/city-{s}.jpg" alt="{n}"><div><b>{n}</b><small>{c}</small></div></a>' for s,n,c in CITIES)}</div>
<p class="center mt"><a class="btn btn-ink" href="map.html">Open the interactive map of Italy <span class="arr">→</span></a></p></div></section>''')
# BIAGIO
h.append(f'''<section class="sec dark" id="biagio" style="background:radial-gradient(900px 600px at 25% 50%,rgba(201,164,92,.18),transparent 60%),linear-gradient(180deg,#121b2e,#0b1220)"><div class="w bia">
<div class="bimg rv"><span class="badge">Biagio · AI tutor</span><img src="assets/img/biagio-3d-hero.png" alt="Biagio, the Club Italia AI tutor, a 3D animated Italian character"></div>
<div class="rv"><span class="eb">Practise between classes</span><h2>Meet <em>Biagio,</em> your Italian coach, always online.</h2>
<p style="margin-top:1.1rem;color:#cfc8b8">Between live classes, Biagio is your AI Italian tutor, trained on the Club Italia syllabus. Ready the moment inspiration or insomnia strikes, in any time zone. He supports your teacher; he never replaces one.</p>
<ul class="checks"><li>Pronunciation coaching, sound by sound</li><li>Instant, non-judgemental grammar corrections</li><li>Real conversation practice on the week\'s topics</li><li>Included with every course</li></ul>
<div class="voices">{''.join(f'<button class="voice" data-audio="assets/audio/{a}.mp3"><span class="pl">▶</span><span><b>{t}</b><small>{q}</small></span></button>' for a,t,q in VO)}</div>
<div class="chat"><p class="u">You: Ieri <del>ho andato</del> al mercato.</p><p class="b">Biagio: Quasi! Si dice «Ieri <ins>sono andato</ins> al mercato.» With andare, use essere.</p></div>
<p class="mt" style="margin-top:1.6rem"><a class="btn btn-gold" href="biagio.html">Discover Biagio <span class="arr">→</span></a></p></div></div></section>''')
# TESTIMONIALS
h.append(f'''<!-- TODO(owner): testimonials and portraits are v16 pitch placeholders, not verified reviews. Replace with real Trustpilot reviews before launch. -->
<section class="sec dark" id="stories" style="background:#0a0f1b"><div class="w"><div class="head rv"><span class="tp2"><span class="stars"><i>★</i><i>★</i><i>★</i><i>★</i><i>★</i></span> Excellent on Trustpilot</span><h2>Learner stories. <em>Real progress.</em></h2><p>Adult learners, live classrooms, broadcast from Italy.</p></div>
<div class="tgrid">{''.join(f'<figure class="tc rv"><span class="stars"><i>★</i><i>★</i><i>★</i><i>★</i><i>★</i></span><q>{E(q)}</q><figcaption class="who"><img loading="lazy" src="assets/img/{i}" alt=""><span><b>{n}</b><small>{c}</small></span></figcaption></figure>' for i,n,c,q in TS)}</div></div></section>''')
# PLATFORM
PL=[('▶','01','Live HD classes','Live lessons with a native teacher broadcasting from a real Italian city.','Live from Italy'),('▦','02','Your syllabus','Twenty lessons per course, each with stated objectives, published as a PDF before you start.','PDF syllabus'),('●','03','Class recordings','Missed a class or want to revise? Every lesson is recorded and added to your library.','Your library'),('✦','04','Biagio AI tutor','Pronunciation, grammar and conversation practice between classes, in a real Italian voice.','Always online'),('◆','05','Small groups','Ten to twelve adults, so you speak in every lesson and the teacher corrects you personally.','10 to 12 learners'),('★','06','CEFR certificate','Oral and written can-do assessment, a CEFR-mapped certificate, and CILS or CELI preparation.','Certified')]
h.append(f'''<section class="sec dark" id="platform"><div class="w"><div class="head rv"><span class="eb">One learning platform</span><h2>Built on eTeacher\'s <em>live teaching platform.</em></h2><p>Club Italia runs on the live classroom technology eTeacher Group has used to teach adults online for two decades.</p></div>
<div class="plat">{''.join(f'<article class="pc rv"><span class="n">{n}</span><span class="ic">{ic}</span><h4>{t}</h4><p>{p}</p><span class="tag">{g}</span></article>' for ic,n,t,p,g in PL)}</div><p class="swipe">Swipe the platform →</p></div></section>''')
# PRICING
h.append('''<!-- TODO(owner): tuition figures are v16 pitch placeholders pending eTeacher sign-off. -->
<section class="sec ivory" id="tuition"><div class="w"><div class="head rv"><span class="eb">Tuition</span><h2>One live curriculum. <em>Three ways to pay.</em></h2><p>Every plan includes live lessons on your track, recordings, Biagio and the certificate. Billed in US dollars. Seven day full refund.</p></div>
<div class="plans"><div class="plan rv"><span class="k">Monthly</span><h3>Monthly</h3><div class="p">$84 <small>/ week</small></div><p>Billed $336 monthly. Cancel any time after the first month.</p><ul><li>All live lessons on your track</li><li>Biagio, the AI tutor</li><li>Class recordings</li><li>Cultural library</li></ul><a class="btn btn-ghost" href="#enrol">Start monthly</a></div>
<div class="plan f rv"><span class="best">Best value · save 26%</span><span class="k">Annual</span><h3>Annual</h3><div class="p">$62 <small>/ week</small></div><p>Billed once at $3,224 for the year.</p><ul><li>Everything in monthly</li><li>Two cultural capsule sessions</li><li>Priority teacher placement</li><li>Printed CEFR certificate</li></ul><a class="btn btn-gold" href="#enrol">Start annual</a></div>
<div class="plan rv"><span class="k">Term</span><h3>One term</h3><div class="p">$73 <small>/ week</small></div><p>Billed $876 for a twelve-week term. No auto-renewal.</p><ul><li>All lessons of one term</li><li>Biagio for the term</li><li>Placement included</li><li>End of stage certificate</li></ul><a class="btn btn-ghost" href="#enrol">Start a term</a></div></div>
<p class="center mt"><a class="lnk" href="pricing.html">Full tuition details</a></p></div></section>''')
# LEVEL FINDER
h.append(f'''<section class="sec paper" id="level"><div class="w"><div class="lm rv"><div class="vis">{V('ag-venice-docked')}<span class="chip">Free · 1 minute</span></div>
<div class="q"><span class="eb">Find your level</span><h2>Which Italian course is <em>right for you?</em></h2><p style="margin-top:.8rem;color:#bdb7aa">Answer three questions and get an instant course recommendation. Your teacher confirms it in a free placement conversation.</p>
<form class="qz" id="qz"><fieldset><legend>1 · Your Italian today</legend><div class="opts">{''.join(f'<label><input type="radio" name="lv" value="{v}"><span>{t}</span></label>' for v,t in [('0','None yet'),('1','A few words'),('2','Basic conversations'),('3','I get by')])}</div></fieldset>
<fieldset><legend>2 · Your goal</legend><div class="opts">{''.join(f'<label><input type="radio" name="g" value="{v}"><span>{t}</span></label>' for v,t in [('s','Speak with confidence'),('g','Grammar and structure'),('c','Food, art or opera'),('x','CILS, CELI or citizenship')])}</div></fieldset>
<fieldset><legend>3 · Your pace</legend><div class="opts">{''.join(f'<label><input type="radio" name="p" value="{v}"><span>{t}</span></label>' for v,t in [('1','Once a week'),('2','Twice a week')])}</div></fieldset></form>
<div class="result" id="res" aria-live="polite"></div>
<p style="margin-top:1.2rem"><a class="lnk" href="#enrol">Talk to an advisor instead</a></p></div></div></div></section>''')
# LEAD FORM
h.append('''<section class="sec dark" id="enrol"><div class="w lead"><div class="rv"><span class="eb">Begin your journey</span><h2>Request your personal <em>enrolment consultation.</em></h2>
<p style="margin-top:1.1rem;color:#cfc8b8">Tell us about your Italian and your goals. A Club Italia advisor will reach out personally to walk you through the courses, the live classes and the plan that fits you.</p>
<ul class="checks"><li>No pressure, a real human consultation</li><li>Your recommended course and start date</li><li>Reply within one working day</li><li>Seven day full refund from your first lesson</li></ul>
<p style="color:#9a9486;font-size:.86rem">Prefer email? <a class="lnk" href="mailto:advisor@eTeacherGroup.com">advisor@eTeacherGroup.com</a></p></div>
<!-- TODO(owner): form is front-end only; connect to eTeacher CRM. -->
<form class="form rv" id="lead"><h4>Personal consultation request</h4><label>First name<input required name="first" autocomplete="given-name"></label><label>Last name<input required name="last" autocomplete="family-name"></label>
<label class="full">Email<input required type="email" name="email" autocomplete="email"></label><label>Phone<input name="phone" autocomplete="tel"></label>
<label>Italian level<select name="level"><option>Absolute beginner</option><option>Beginner (A1)</option><option>Elementary (A2)</option><option>Intermediate (B1)</option><option>Upper intermediate (B2) or above</option><option>I am not sure</option></select></label>
<label>When to start<select name="when"><option>Autumn cohort (Oct 6)</option><option>Capsules (Oct 20)</option><option>Next term</option><option>Just exploring</option></select></label>
<label>Country<input name="country" autocomplete="country-name" placeholder="United States"></label>
<button class="btn btn-gold" type="submit">Request my consultation <span class="arr">→</span></button><p class="note">Your information is private and never shared.</p></form></div></section>''')
# FAQ
h.append(f'''<section class="sec ivory" id="faq"><div class="w"><div class="head rv"><span class="eb">Your questions, answered</span><h2>Everything worth asking <em>before you enrol.</em></h2></div>
<div class="faq">{''.join(f'<details class="rv"><summary><span class="i">0{i+1}.</span>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(FAQ))}</div>
<p class="center mt"><a class="btn btn-ghost" href="faq.html">See all questions</a></p></div></section>''')
# CTA
h.append(f'''<section class="band">{V('ag-cypress-road')}<span class="frame"></span><div class="w rv"><span class="eb">Autumn cohorts · Oct 6</span><h2>Culture speaks Italian. <em>What about you?</em></h2><p>Join a live class broadcasting from Italy and begin your Italian with a conversation.</p>
<a class="btn btn-gold" href="#enrol">Begin your journey <span class="arr">→</span></a></div></section></main>''')
# FOOTER
h.append('''<footer class="ftr"><div class="w"><div class="g"><div><span class="bn">Club Italia</span><p style="margin-top:1rem">A culturally immersive, certified, live Italian language school for adult lifelong learners, by eTeacher Group.</p><img src="assets/img/eteacher-real-logo-white.png" alt="eTeacher Group" style="height:22px;margin-top:1.4rem"><p style="margin-top:1rem"><a href="mailto:advisor@eTeacherGroup.com">advisor@eTeacherGroup.com</a></p></div>
<div><h5>Courses</h5><ul><li><a href="courses.html">All courses</a></li><li><a href="pages/courses/ci1.html">CI Principiante</a></li><li><a href="pages/courses/ci2.html">CI Elementare</a></li><li><a href="pages/courses/ci3.html">CI Intermedio</a></li><li><a href="pages/courses/ci4.html">CI Avanzato</a></li><li><a href="capsules.html">Capsules</a></li></ul></div>
<div><h5>Study</h5><ul><li><a href="curriculum.html">Curriculum A1 to C2</a></li><li><a href="certifications.html">CILS and CELI</a></li><li><a href="method.html">Method</a></li><li><a href="how-it-works.html">How it works</a></li><li><a href="biagio.html">Biagio AI tutor</a></li><li><a href="sample-class.html">Sample class</a></li></ul></div>
<div><h5>Culture</h5><ul><li><a href="culture.html">Culture hub</a></li><li><a href="map.html">Map of Italy</a></li><li><a href="events.html">Events</a></li><li><a href="blog.html">Journal</a></li><li><a href="community.html">Community</a></li></ul></div>
<div><h5>School</h5><ul><li><a href="about.html">About</a></li><li><a href="eteacher.html">eTeacher Group</a></li><li><a href="teachers.html">Faculty</a></li><li><a href="pricing.html">Tuition</a></li><li><a href="faq.html">FAQ</a></li><li><a href="contact.html">Contact</a></li></ul></div></div>
<div class="lg"><span>© 2026 eTeacher Group. Club Italia is a trading style of eTeacher Group.</span><span><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a></span></div>
<p style="font-size:.7rem;margin-top:1rem;opacity:.6">Footage licensed via Artgrid. Hero music: Vivaldi, «La primavera», CC BY-SA 3.0. CILS and CELI are administered by the Università per Stranieri di Siena and di Perugia; Club Italia is not an examination centre.</p></div></footer>
<script src="js/home17.js" defer></script></body></html>''')
out='\n'.join(h).replace('—',', ').replace('–',' to ')
open('index.html','w').write(out);print(len(out))
