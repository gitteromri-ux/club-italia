import json,re,html,os
D=json.load(open('research/course-data.json'));T=json.load(open('/workspace/teachers.json'));M=json.load(open('/workspace/italy_svg.json'))
E=html.escape
def cl(s): return re.sub(r'\s*[—–]\s*',', ',str(s)).replace('→','to').replace('×','x')
TN={'marco':('Marco Rinaldi','Roma'),'chiara':('Chiara Bellini','Firenze'),'giulia':('Giulia Moretti','Bologna'),'alessandro':('Alessandro Ferri','Milano'),'francesca':('Francesca Zeno','Venezia'),'luca':('Luca De Simone','Napoli'),'sofia':('Sofia Mazzara','Palermo')}
CO={ # key: (collection, name, url, img, teacher, hover video, start, tuition)
'ci1':('ci','CI Principiante','pages/courses/ci1.html','course-ci1.jpg','marco','roma-piazza','Oct 6, 2026','$62 a week'),
'ci2':('ci','CI Elementare','pages/courses/ci2.html','course-ci2.jpg','chiara','firenze-arno','Oct 6, 2026','$62 a week'),
'ci3':('ci','CI Intermedio','pages/courses/ci3.html','course-ci3.jpg','giulia','bologna-portici','Oct 6, 2026','$62 a week'),
'ci4':('ci','CI Avanzato','pages/courses/ci4.html','course-ci4.jpg','luca','napoli-mare','Oct 6, 2026','$62 a week'),
'ps1':('ps','Al Caffè','pages/spoken/ps1.html','spoken-ps1.jpg','marco','ag-market-produce','Oct 6, 2026','$62 a week'),
'ps2':('ps','A Tavola','pages/spoken/ps2.html','spoken-ps2.jpg','chiara','cucina-pasta','Oct 6, 2026','$62 a week'),
'ps3':('ps','In Viaggio','pages/spoken/ps3.html','spoken-ps3.jpg','francesca','venezia-canal','Oct 6, 2026','$62 a week'),
'ps4':('ps','Chiacchierando','pages/spoken/ps4.html','spoken-ps4.jpg','alessandro','ag-luxury-car','Oct 6, 2026','$62 a week'),
'cap-food':('cap','La Cucina','pages/culture/cap-food.html','cap-food.jpg','giulia','ag-pizza-oven','Oct 20, 2026','$390'),
'cap-art':('cap',"L'Arte",'pages/culture/cap-art.html','cap-art.jpg','chiara','ag-medieval-aerial','Oct 20, 2026','$390'),
'cap-opera':('cap',"L'Opera",'pages/culture/cap-opera.html','cap-opera.jpg','alessandro','opera-scala','Oct 20, 2026','$390')}
ORDER=list(CO)
NEXT={'ci1':'ci2','ci2':'ci3','ci3':'ci4','ps1':'ps2','ps2':'ps3','ps3':'ps4'}
def V(n,P,cls='grade',auto=True,poster=None,hover=False):
    p=poster or f'{P}assets/img/{n}-poster.jpg'
    return f'<video class="{cls}" muted loop playsinline preload="none" poster="{p}" data-src="{P}assets/video/{n}.mp4"{" data-hover" if hover else ""} aria-hidden="true"></video>'
def head(title,desc,P):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{E(desc)}"><meta name="theme-color" content="#0b1220">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{P}css/home17.css"><link rel="stylesheet" href="{P}css/v18.css"></head><body>
<div class="curtain" aria-hidden="true"><span>Club Italia</span></div><a class="skip" href="#main">Skip to content</a>
<header class="hdr"><div class="w"><a class="brand" href="{P}index.html" aria-label="Club Italia home"><span class="bn">Club Italia</span><span class="by">by <img src="{P}assets/img/eteacher-real-logo-white.png" alt="eTeacher Group"></span></a>
<nav class="nav" aria-label="Primary"><a href="{P}courses.html">Courses</a><a href="{P}curriculum.html">Curriculum</a><a href="{P}method.html">Method</a><a href="{P}teachers.html">Faculty</a><a href="{P}map.html">Map</a><a href="{P}biagio.html">Biagio AI</a><a href="{P}pricing.html">Tuition</a><a href="{P}index.html#enrol" class="btn btn-gold">Enrol now</a></nav>
<button class="burger" aria-label="Open menu" aria-expanded="false"><i></i><i></i><i></i></button></div></header><main id="main">'''
def foot(P):
    return f'''</main><footer class="ftr"><div class="w"><div class="g"><div><span class="bn">Club Italia</span><p style="margin-top:1rem">A culturally immersive, live Italian school for adult learners, by eTeacher Group.</p><img src="{P}assets/img/eteacher-real-logo-white.png" alt="eTeacher Group" style="height:22px;margin-top:1.4rem"><p style="margin-top:1rem"><a href="mailto:advisor@eTeacherGroup.com">advisor@eTeacherGroup.com</a></p></div>
<div><h5>Il Corso</h5><ul>{''.join(f'<li><a href="{P}{CO[k][2]}">{CO[k][1]}</a></li>' for k in ['ci1','ci2','ci3','ci4'])}</ul></div>
<div><h5>Parliamo</h5><ul>{''.join(f'<li><a href="{P}{CO[k][2]}">{CO[k][1]}</a></li>' for k in ['ps1','ps2','ps3','ps4'])}</ul></div>
<div><h5>Capsule</h5><ul>{''.join(f'<li><a href="{P}{CO[k][2]}">{CO[k][1]}</a></li>' for k in ['cap-food','cap-art','cap-opera'])}</ul></div>
<div><h5>School</h5><ul><li><a href="{P}curriculum.html">Curriculum</a></li><li><a href="{P}certifications.html">CILS and CELI</a></li><li><a href="{P}teachers.html">Faculty</a></li><li><a href="{P}pricing.html">Tuition</a></li><li><a href="{P}faq.html">FAQ</a></li><li><a href="{P}contact.html">Contact</a></li></ul></div></div>
<div class="lg"><span>© 2026 eTeacher Group. Club Italia is a trading style of eTeacher Group.</span><span><a href="{P}privacy.html">Privacy</a> · <a href="{P}terms.html">Terms</a></span></div>
<p style="font-size:.7rem;margin-top:1rem;opacity:.6">Footage licensed via Artgrid. Map outline: Natural Earth (public domain). Hero music: Vivaldi, «La primavera», CC BY-SA 3.0. CILS and CELI are administered by the Università per Stranieri di Siena and di Perugia; Club Italia is not an examination centre.</p></div></footer>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script><script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script><script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js" defer></script>
<script src="{P}js/v18.js" defer></script></body></html>'''
def lvl(k): return cl(D[k]['cefr'])
def rc(k,P):
    t,n,u,img,te,hv,st,tu=CO[k];d=D[k]
    pr=cl(d['promise']).split('. ')[0].rstrip('.')+'.'
    return f'''<a class="rc" href="{P}{u}" data-cursor="View"><img loading="lazy" src="{P}assets/img/{img}" alt="">{V(hv,P,poster=P+'assets/img/'+img,hover=True)}<span class="lv chip g">{lvl(k)}</span>
<div class="tx"><span class="code">{cl(d['code'])} · {TN[te][1]}</span><h4>{E(n)}</h4><p>{E(pr)}</p><dl><div>Teacher<dd>{TN[te][0].split()[0]}</dd></div><div>Format<dd>{cl(d['hours']).replace(' x 85 min','')}</dd></div><div>Tuition<dd>{tu}</dd></div></dl></div></a>'''
def h2(txt,em): return f'<h2 data-split>{txt} <em>{em}</em></h2>'
FAQ=[('Are the classes live?','Every class is live, taught by a native teacher broadcasting from Italy. Recordings are for revision, never a substitute.'),
('How big are the groups?','Ten to twelve adults. Everyone speaks in every lesson and the teacher corrects each learner personally.'),
('What does a course include?','Twenty live lessons of 85 minutes (six sessions of 60 minutes for a capsule), the PDF syllabus, recordings, Biagio the AI tutor and a CEFR-mapped Club Italia certificate.'),
('Do you prepare for CILS and CELI?','Yes, from A2 upward. You sit the exam at an authorised centre of the Università per Stranieri di Siena (CILS) or di Perugia (CELI). Club Italia is not an exam centre.'),
('How much does it cost?','From $62 a week on the annual plan, $73 a week by term, $84 a week monthly. Seven day full refund from your first live lesson.'),
('Who teaches?','Native Italian teachers holding the DITALS qualification for teaching Italian as a foreign language, each in their own city.')]
def faqh(): return '<div class="faq" data-acc>'+''.join(f'<details><summary><span class="i">0{i+1}.</span>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(FAQ))+'</div>'

# ================= HOME =================
P=''
CITY=[('roma','Roma','marco','ag-roma-statue','ci1'),('firenze','Firenze','chiara','firenze-arno','ci2'),('bologna','Bologna','giulia','bologna-portici','ci3'),('venezia','Venezia','francesca','ag-venice-gondola','ps3'),('milano','Milano','alessandro','opera-scala','ps4'),('napoli','Napoli','luca','napoli-mare','ci4'),('palermo','Palermo','sofia','ag-catania-statues','ci4')]
POST={'firenze-arno':'assets/img/city-firenze.jpg' ,'bologna-portici':'assets/img/v17/city-bologna.jpg','opera-scala':'assets/img/cap-opera.jpg','napoli-mare':'assets/img/v17/city-napoli.jpg'}
cdata=[]
for k,n,te,v,c in CITY:
    d=D[c];q=T[te]['quote'].split('. ')[0]+'.'
    cdata.append({'k':k,'n':n,'t':TN[te][0],'ti':f'assets/img/teacher-{te}.jpg','q':'«'+cl(q)+'»','c':CO[c][1]+' · '+lvl(c),'l':cl(d['promise']).split('. ')[0]+'.','v':f'assets/video/{v}.mp4','p':POST.get(v,f'assets/img/{v}-poster.jpg'),'h':CO[c][2],'u':[[i+1,cl(s[0]),cl(s[1]).split('. ')[0]+'.'] for i,s in enumerate(d['syllabus'][:3])]})
if True:
    # Sofia: Palermo, shares top level
    cdata[-1]['c']='CI Avanzato · A2.1 to A2.2 (with Luca)'
pts=' '.join(f'{M["c"][k][0]},{M["c"][k][1]}' for k in ['milano','venezia','bologna','firenze','roma','napoli','palermo'])
nodes=''.join(f'<g class="node" data-k="{k}" tabindex="0" role="button" aria-label="{n}: teacher {TN[te][0]}"><circle class="p" cx="{M["c"][k][0]}" cy="{M["c"][k][1]}" r="7"/><circle class="d" cx="{M["c"][k][0]}" cy="{M["c"][k][1]}" r="6"/><text x="{M["c"][k][0]+(12 if k not in ("milano","firenze") else -12)}" y="{M["c"][k][1]+4}" text-anchor="{"start" if k not in ("milano","firenze") else "end"}">{n.upper()}</text></g>' for k,n,te,v,c in CITY)
LAD=[{'k':'A1 · Breakthrough','h':'You can <em>introduce yourself</em> and get by.','u':['Greet, introduce yourself and others','Order at a bar, a trattoria, a market','Ask the way and understand simple directions','Handle numbers, prices, dates and times'],'r':'Club Italia: CI Principiante and CI Elementare, Al Caffè. Guide: about 90 to 100 guided hours (approx.).'},
{'k':'A2 · Waystage','h':'You can <em>talk about your life</em> and your past.','u':['Narrate past events with passato prossimo and imperfetto','Make plans, invitations and bookings','Describe people, places and routines','Deal with travel, shops and problems'],'r':'Club Italia: CI Intermedio and CI Avanzato, A Tavola, In Viaggio. Guide: about 180 to 200 cumulative hours (approx.).'},
{'k':'B1 · Threshold','h':'You can <em>hold a real conversation</em>.','u':['Follow the main points of clear standard speech','Give and justify opinions','Cope with most situations while travelling','Write connected text on familiar topics'],'r':'Club Italia: Chiacchierando, CILS / CELI B1 preparation. Guide: about 350 to 400 cumulative hours (approx.).'},
{'k':'B2 · Vantage','h':'You can <em>argue, read and follow the news</em>.','u':['Understand complex texts and debates','Interact with fluency and spontaneity','Write clear, detailed argued text','Required by many Italian universities'],'r':'Advanced cohorts on the same framework. <!-- TODO(owner): confirm B2 availability -->'},
{'k':'C1 · Effective operational proficiency','h':'You can <em>work and study</em> in Italian.','u':['Express ideas fluently without searching for words','Use language flexibly for social, academic and professional purposes','Produce well-structured detailed text'],'r':'Advanced cohorts. TODO owner: confirm.'},
{'k':'C2 · Mastery','h':'You can <em>understand virtually everything</em>.','u':['Summarise and reconstruct arguments','Express yourself precisely with fine shades of meaning','Read literature and specialised texts with ease'],'r':'Advanced cohorts. TODO owner: confirm.'}]
for l in LAD: l['r']=re.sub(r'<!--.*?-->','',l['r'])
VO=[('biagio-line-caffe','Al caffè','«Un cappuccino e un cornetto, per favore.»','A cappuccino and a cornetto, please.'),('biagio-line-tavola','A tavola','«Prendo la pasta alla carbonara. Grazie.»',"I'll have the pasta alla carbonara. Thank you."),('biagio-line-strada','Per strada',"«Mi scusi, dov'è la stazione della metropolitana?»",'Excuse me, where is the metro station?'),('biagio-line-corregge','Correzione',"«Si dice 'sono andato', non 'ho andato'.»","It's sono andato, not ho andato. With essere, the participle agrees.")]
TS=[('student-01-sarah.jpg','Sarah T.','Verified learner','Marco is a great teacher. Small class, everyone speaks, and you actually leave every lesson able to say something new.'),('student-diane.jpg','Diane Weller','Chicago · CI Principiante','In three months I ordered dinner in Trastevere and the waiter answered in Italian for the whole meal.'),('student-03-elena.jpg','Elena R.','Verified learner','Chiara teaches from a Florentine studio. You hear the city. The accent training is unreal.'),('student-robert.jpg','Robert Hensley','Austin · A Tavola','The teacher cooks while she teaches. That single fact changed how I hear the language.'),('student-02-david.jpg','David L.','Verified learner','Twelve people in class, all adults, all serious. Best language school I have used, and I have tried a few.'),('student-sarah.jpg','Sarah Kim',"San Francisco · L'Opera",'I read the libretto of La Bohème with Alessandro over six sessions. I now understand why Italians cry at the third act.'),('student-james.jpg','James Whitaker','London · CI Elementare','Small classes, real corrections, no drills. It felt like being tutored at a Florentine institute.'),('student-linda.jpg','Linda Bauer','Toronto · CI Intermedio','Chiara caught a mistake I had been making since 2014. In one live class.')]
tcards=''.join(f'<figure class="tc"><span class="stars"><i>★</i><i>★</i><i>★</i><i>★</i><i>★</i></span><q>{E(q)}</q><figcaption class="who"><img loading="lazy" src="assets/img/{i}" alt=""><span><b>{n}</b><small>{c}</small></span></figcaption></figure>' for i,n,c,q in TS)
mani='Italian is not learned from a screen. It is learned at the counter of a Roman bar, under the porticoes of Bologna, in a Florentine studio where the light has not changed in five hundred years. So that is where we teach it.'
home=head('Club Italia · Learn Italian, live from Italy','Live Italian classes with native teachers broadcasting from seven Italian cities. Ten to twelve learners, a CEFR-aligned syllabus, CILS and CELI preparation, and Biagio the AI tutor.',P)+f'''
<section class="h18"><div class="vwrap"><video class="grade" autoplay muted loop playsinline preload="auto" poster="assets/img/ag-roma-statue-poster.jpg"><source src="assets/video/ag-roma-statue.mp4" type="video/mp4"></video><div class="tint"></div><div class="side"></div></div>
<div class="w"><div class="copy"><div class="hero-badges"><span class="chip g">Live from Italy</span><span class="chip">by eTeacher Group</span><span class="chip">Autumn cohort · Oct 6</span></div>
<h1 data-split>Learn Italian. <em>Live from Italy.</em></h1>
<p class="lede">An exclusive, culturally immersive academy for adult learners. Native teachers in seven Italian cities, ten to twelve learners per class, a CEFR syllabus from your first «ciao» to B1.</p>
<div class="ctas"><a class="btn btn-gold" href="#enrol">Reserve my seat · $62 a week <span class="arr">→</span></a><a class="btn btn-line" href="#level">Find my level</a></div></div>
<div class="after" style="position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);text-align:center;opacity:0;pointer-events:none"><h2 style="color:#fff;font-size:clamp(2.4rem,6vw,5.4rem);text-shadow:0 2px 40px rgba(0,0,0,.5)">Seven cities. <em style="color:var(--oro2)">One language.</em></h2></div></div>
<div class="meta"><div class="w"><div class="facts"><div><b>7</b>Italian cities</div><div><b>10 to 12</b>per class</div><div><b>85 min</b>live lessons</div><div><b>A0 to B1</b>CEFR</div></div><button class="music" id="music" style="position:static">♪ Music off</button></div></div>
<audio id="theme" src="assets/audio/hero-italian-theme.mp3" preload="none" loop></audio></section>
<a class="pill" href="#enrol"><span><small>Open enrolment</small>Autumn cohorts · live from Italy</span><span class="btn btn-gold">Enrol</span></a>
<section class="mani"><div class="w"><p>{' '.join(f'<span class="wd">{w}</span>' for w in mani.split())}</p><small>The Club Italia method</small></div></section>

<section class="rail" id="courses"><div class="w top"><span class="eb">Our courses</span>{h2('Eleven courses.','Three ways into Italian.')}<p style="max-width:56ch;margin-top:1rem;color:#bdb7aa">Every course is live, small-group, CEFR-aligned and anchored in an Italian city. Scroll to travel through the collections; hover a card to see its city.</p></div>
<div class="track">
<div class="cset"><div class="clabel"><span class="k">Collection 01 · Structured · Best seller</span><h3>Il Corso</h3><p>Language and culture, city by city. Grammar, vocabulary and the four skills, in twenty live lessons per level.</p><div class="st"><div><b>4</b>courses</div><div><b>A0 to A2.2</b>CEFR</div><div><b>20</b>lessons</div></div></div>{''.join(rc(k,P) for k in ['ci1','ci2','ci3','ci4'])}</div>
<div class="cset"><div class="clabel"><span class="k">Collection 02 · Spoken</span><h3>Parliamo</h3><p>Spoken fluency first. Four Italian scenes, from the bar counter to the dinner table to the open road.</p><div class="st"><div><b>4</b>courses</div><div><b>A0 to B1</b>CEFR</div><div><b>20</b>sessions</div></div></div>{''.join(rc(k,P) for k in ['ps1','ps2','ps3','ps4'])}</div>
<div class="cset"><div class="clabel"><span class="k">Collection 03 · Culture</span><h3>Capsule culturali</h3><p>Six sessions inside one Italian passion: the table, the Renaissance, the opera. Open to every level.</p><div class="st"><div><b>3</b>capsules</div><div><b>Any</b>level</div><div><b>6</b>sessions</div></div></div>{''.join(rc(k,P) for k in ['cap-food','cap-art','cap-opera'])}</div>
</div><div class="prog"><i></i></div></section>

<section class="mapsec" id="map"><div class="w"><div class="head rv"><span class="eb">The map of Club Italia</span>{h2('Follow your teacher','across Italy.')}<p>Seven cities, seven native teachers. Hover or tap a city to meet its teacher, open its course and see the first units of the syllabus.</p></div>
<div class="mapgrid"><svg id="italy" class="italy" viewBox="-40 -20 {M['w']+80} {M['h']+40}" role="group" aria-label="Interactive map of Italy with seven Club Italia cities">
<defs><linearGradient id="landg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1d3f74"/><stop offset="1" stop-color="#0f2246"/></linearGradient><filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter><filter id="blur"><feGaussianBlur stdDeviation="6"/></filter></defs>
<path class="halo" d="{M['d']}"/><path class="land" d="{M['d']}"/><polyline class="route" points="{pts}"/><circle class="comet" r="3.2" cx="0" cy="0"/>{nodes}</svg>
<div><div class="mpanel glass" id="mpanel" aria-live="polite"><div class="mv"><video class="grade" muted loop playsinline autoplay preload="none"></video><span class="city"></span></div>
<div class="bd"><div class="tp"><img alt="" src=""></div><div><span class="k">Your teacher</span><h4 id="mt"></h4><p id="mq" style="font-style:italic;font-family:var(--serif)"></p><p style="margin-top:.5rem"><b style="color:#fff" id="mc"></b><br><span id="ml"></span></p></div>
<ol></ol><a class="btn btn-gold go" href="#" style="justify-self:start">Open the course <span class="arr">→</span></a></div></div>
<div class="mtabs" role="group" aria-label="Choose a city">{''.join(f'<button data-k="{k}" aria-pressed="false">{n}</button>' for k,n,*_ in CITY)}</div></div></div></div>
<script type="application/json" id="citydata">{json.dumps(cdata,ensure_ascii=False)}</script></section>

<section class="lad18" id="ladder">{V('ag-tuscany-drone',P)}<div class="tint"></div><div class="w"><div class="glass" style="padding:2.2rem"><span class="eb">The CEFR ladder</span><h2 style="font-size:clamp(2rem,3.6vw,3rem)">Six levels. <em>One framework.</em> Every lesson mapped.</h2>
<div class="cando" style="margin-top:1.6rem"><span class="lvk" id="lvk"></span><h3 id="lvh"></h3><ul id="lvu"></ul><p class="hrs" id="lvr"></p></div>
<p style="font-size:.74rem;opacity:.8;margin-top:1rem">Descriptors paraphrased from the Council of Europe CEFR Companion Volume (2020). Guided-hour figures are common published guides, not Club Italia claims.</p><p style="margin-top:1rem"><a class="lnk" href="curriculum.html" style="color:var(--oro2)">Full A1 to C2 curriculum</a></p></div>
<div class="rungs" aria-hidden="true">{''.join(f'<div class="rg" style="height:{30+i*14}%"><b>{c}</b><span>{n}</span></div>' for i,(c,n) in enumerate([('A1','Breakthrough'),('A2','Waystage'),('B1','Threshold'),('B2','Vantage'),('C1','Effective'),('C2','Mastery')]))}</div></div>
<script type="application/json" id="laddata">{json.dumps(LAD,ensure_ascii=False)}</script></section>

<section class="sec paper" id="method"><div class="w"><div class="head rv"><span class="eb">A structured, CEFR-aligned curriculum</span>{h2('Written by Italian language specialists,','against the European framework.')}<p>Action-oriented, communicative learning aligned with the Common European Framework of Reference. You do not study Italian. You act in it.</p></div>
<div class="pill3">{''.join(f'<div class="panel rv"><span class="dots">0{i+1}</span><p style="font:italic 400 1rem var(--serif);color:var(--oro3);margin:.8rem 0 .2rem">{a}</p><h3>{b}</h3><p style="color:var(--mut)">{c}</p></div>' for i,(a,b,c) in enumerate([('Imparare facendo','You act, you speak','The CEFR treats the learner as a social agent. Every lesson is a task: ordering, booking, negotiating, persuading.'),('Lingua in situ','Learned where it is lived','Every unit is set in a real Italian place: a Roman bar, a Florentine workshop, a Bolognese market.'),('La cultura al centro','Culture at the core','Art, food, opera and cinema are the material the language is taught through, assessed with can-do statements at every milestone.')]))}</div>
<div class="refs" style="color:var(--ink2)"><span>2020 · Council of Europe, CEFR Companion Volume</span><span>2019 · Piccardo and North, The Action-oriented Approach</span><span>CILS · Università per Stranieri di Siena</span><span>CELI · Università per Stranieri di Perugia</span></div>
<p class="disc" style="color:var(--mut)">Club Italia is independent and not affiliated with, nor endorsed by, the institutions cited.</p></div></section>

<section class="vfold sec" id="classroom">{V('ag-camogli-coast',P)}<div class="tint"></div><div class="w split"><div class="glass rv" style="padding:2.2rem"><span class="eb">Inside a live class</span>{h2('A real Italian classroom.','In your living room.')}
<p style="margin-top:1rem;color:#f1ece2">Your teacher is in Rome, Florence or Venice. You are at home. Twelve adults, one native teacher, eighty-five minutes of Italian that you speak, not watch.</p>
<div class="feat6">{''.join(f'<div style="border-color:rgba(255,255,255,.2)"><h4 style="color:#fff">{a}</h4><p style="color:#e6e0d4">{b}</p></div>' for a,b in [('Live from Italy',"Broadcast from the teacher's own city."),('Small groups','Ten to twelve learners.'),('Breakout rooms','Pairs and trios, every lesson.'),('Recordings','Every class, in your library.')])}</div>
<p class="mt"><a class="btn btn-gold" href="sample-class.html">Watch a sample class <span class="arr">→</span></a></p></div>
<div class="laptop rv"><div class="zbar"><span class="rec">REC</span><span>CI Principiante · Lezione 07 «A che ora?»</span><span>12 participants</span></div>
<div class="zgrid"><div class="zt host"><img src="assets/img/teacher-marco.jpg" alt="Marco Rinaldi teaching live from Rome"><span>Marco · Roma (host)</span><div class="zcap">«Allora, a che ora ti svegli la mattina?»</div></div>{''.join(f'<div class="zt"><img loading="lazy" src="assets/img/{s}.jpg" alt=""><span>{n}</span></div>' for s,n in zip(['student-01-sarah','student-02-david','student-03-elena','student-04-michael','student-05-anna','student-06-jonathan'],['Sarah','David','Elena','Michael','Anna','Jonathan']))}</div>
<div class="zctl"><i>Mute</i><i>Video</i><i>Breakout rooms</i><i>Chat</i><i class="leave">Leave</i></div></div></div></section>

<section class="sec dark" id="culture"><div class="w"><div class="head rv"><span class="eb">Culture</span>{h2('Culture speaks Italian.','What about you?')}<p>Six pillars, filmed in Italy. The material every lesson is built from.</p></div>
<div class="vgrid">{''.join(f'<a class="vt rv" href="pages/culture/{u}.html" data-cursor="Explore">{V(v,P)}<div class="tint"></div><div class="tx"><span class="n">0{i+1}</span><h3>{t}</h3><p>{p}</p></div></a>' for i,(v,t,p,u) in enumerate([('ag-medieval-aerial','Arte e architettura','From Roman forums to Renaissance cupolas.','pillar-art'),('ag-chefs-street','La cucina','A Bolognese market, a Neapolitan oven, a Tuscan table.','pillar-food'),('ag-venice-gondola','Il viaggio','From the canals of Venice to the Amalfi coast.','pillar-travel'),('ag-catania-statues','Il cinema','Fellini, Sorrentino, the piazza on screen.','pillar-cinema'),('ag-rome-basilica',"L'opera",'Verdi, Puccini, Rossini.','pillar-opera'),('ag-tradition-festival','Le tradizioni','Carnevale, the Palio, the Festa della Repubblica.','pillar-tradition')]))}</div></div></section>

<!-- TODO(owner): group figures are v16 placeholders; confirm with eTeacher. -->
<section class="power"><div class="w rv"><span class="eb">Presented by eTeacher Group</span><h2>A serious school, <em>not an app.</em></h2>
<div class="pst"><div><b>2004</b><span>Teaching live online</span></div><div><b data-count="200000">200,000</b><span>Alumni</span></div><div><b data-count="16">16</b><span>Languages taught</span></div><div><b>CEFR</b><span>Aligned outcomes</span></div></div>
<div class="logos"><img src="assets/img/eteacher-real-logo-white.png" alt="eTeacher Group"><span>CILS preparation</span><span>CELI preparation</span></div></div></section>

<section class="sec ivory" id="faculty"><div class="w"><div class="head rv"><span class="eb">Meet our faculty</span>{h2('Native teachers,','from every corner of Italy.')}<p>Each teacher lives and broadcasts from a different Italian city. DITALS qualified. Real accents, real kitchens, real streets.</p></div>
<!-- TODO(owner): faculty are v16 composites; replace with real teachers. -->
<div class="fac">{''.join(f'<a class="ft rv" href="pages/teachers/{s}.html" data-cursor="Meet"><img loading="lazy" src="assets/img/teacher-{s}.jpg" alt="{n}"><div><b>{n}</b><small>{c}</small></div></a>' for s,(n,c) in TN.items())}</div>
<p class="center mt"><a class="btn btn-ghost" href="teachers.html">Meet the full faculty <span class="arr">→</span></a></p></div></section>

<section class="vfold sec" id="biagio">{V('ag-rome-basilica',P)}<div class="tint"></div><div class="w bia"><div class="bimg rv"><span class="badge">Biagio · AI tutor</span><img src="assets/img/biagio-3d-hero.png" alt="Biagio, the Club Italia AI tutor"></div>
<div class="glass rv" style="padding:2.2rem"><span class="eb">Practise between classes</span>{h2('Meet Biagio,','your Italian coach, always online.')}
<p style="margin-top:1rem;color:#f1ece2">Not a chatbot. A language coach trained on the Club Italia syllabus. He prepares you before class, consolidates after, and never replaces your teacher.</p>
<div class="wave" aria-hidden="true">{'<i></i>'*28}</div><p id="bcap" style="font:italic 400 1.1rem var(--serif);color:#fff;min-height:1.6em">Press a line to hear Biagio.</p>
<div class="voices">{''.join(f'<button class="voice" data-audio="assets/audio/{a}.mp3" data-line="{E(q)}<br><small style=&quot;color:#cfc8b8;font-family:Inter&quot;>{E(tr)}</small>"><span class="pl">▶</span><span><b>{t}</b><small>{q}</small></span></button>' for a,t,q,tr in VO)}</div>
<div class="chat"><p class="u">You: Ieri <del>ho andato</del> al mercato.</p><p class="b">Biagio: Quasi! «Ieri <ins>sono andato</ins> al mercato.» With andare, use essere.</p></div>
<p style="margin-top:1.4rem"><a class="btn btn-gold" href="biagio.html">Discover Biagio <span class="arr">→</span></a></p></div></div></section>

<!-- TODO(owner): testimonials are v16 pitch placeholders. -->
<section class="sec dark" id="stories" style="background:#0a0f1b"><div class="w"><div class="head rv"><span class="tp2"><span class="stars"><i>★</i><i>★</i><i>★</i><i>★</i><i>★</i></span> Excellent on Trustpilot</span>{h2('Learner stories.','Real progress.')}</div></div>
<div class="tmq"><div class="row">{tcards}{tcards}</div></div></section>

<section class="sec ivory" id="tuition"><div class="w"><div class="head rv"><span class="eb">Tuition</span>{h2('One live curriculum.','Three ways to pay.')}<p>Every plan includes live lessons, recordings, Biagio and the certificate. Billed in US dollars. Seven day full refund.</p></div>
<!-- TODO(owner): tuition figures are v16 placeholders. -->
<div class="plans"><div class="plan rv"><span class="k">Monthly</span><h3>Monthly</h3><div class="p">$84 <small>/ week</small></div><p>Billed $336 monthly.</p><ul><li>All live lessons on your track</li><li>Biagio, the AI tutor</li><li>Class recordings</li></ul><a class="btn btn-ghost" href="#enrol">Start monthly</a></div>
<div class="plan f rv"><span class="best">Best value · save 26%</span><span class="k">Annual</span><h3>Annual</h3><div class="p">$62 <small>/ week</small></div><p>Billed once at $3,224.</p><ul><li>Everything in monthly</li><li>Two cultural capsule sessions</li><li>Priority teacher placement</li><li>Printed CEFR certificate</li></ul><a class="btn btn-gold" href="#enrol">Start annual</a></div>
<div class="plan rv"><span class="k">Term</span><h3>One term</h3><div class="p">$73 <small>/ week</small></div><p>Billed $876 for twelve weeks.</p><ul><li>All lessons of one term</li><li>Biagio for the term</li><li>Placement included</li></ul><a class="btn btn-ghost" href="#enrol">Start a term</a></div></div></div></section>

<section class="sec paper" id="level"><div class="w"><div class="lm rv"><div class="vis">{V('ag-venice-docked',P)}<span class="chip">Free · 1 minute</span></div>
<div class="q"><span class="eb">Find your level</span><h2>Which Italian course is <em>right for you?</em></h2><p style="margin-top:.8rem;color:#bdb7aa">Three questions, an instant recommendation. Your teacher confirms it in a free placement conversation.</p>
<form class="qz" id="qz"><fieldset><legend>1 · Your Italian today</legend><div class="opts">{''.join(f'<label><input type="radio" name="lv" value="{v}"><span>{t}</span></label>' for v,t in [('0','None yet'),('1','A few words'),('2','Basic conversations'),('3','I get by')])}</div></fieldset>
<fieldset><legend>2 · Your goal</legend><div class="opts">{''.join(f'<label><input type="radio" name="g" value="{v}"><span>{t}</span></label>' for v,t in [('s','Speak with confidence'),('g','Grammar and structure'),('c','Food, art or opera'),('x','CILS or CELI')])}</div></fieldset>
<fieldset><legend>3 · Your pace</legend><div class="opts">{''.join(f'<label><input type="radio" name="p" value="{v}"><span>{t}</span></label>' for v,t in [('1','Once a week'),('2','Twice a week')])}</div></fieldset></form><div class="result" id="res" aria-live="polite"></div></div></div></div></section>

<section class="sec dark" id="enrol"><div class="w lead"><div class="rv"><span class="eb">Begin your journey</span>{h2('Request your personal','enrolment consultation.')}
<p style="margin-top:1rem;color:#cfc8b8">Tell us about your Italian and your goals. An advisor will walk you through the courses, the live classes and the plan that fits you.</p>
<ul class="checks"><li>A real, human consultation</li><li>Your recommended course and start date</li><li>Reply within one working day</li></ul></div>
<!-- TODO(owner): connect form to eTeacher CRM. -->
<form class="form rv" id="lead"><h4>Personal consultation request</h4><label>First name<input required name="first" autocomplete="given-name"></label><label>Last name<input required name="last" autocomplete="family-name"></label><label class="full">Email<input required type="email" name="email" autocomplete="email"></label><label>Phone<input name="phone" autocomplete="tel"></label><label>Italian level<select name="level"><option>Absolute beginner</option><option>Beginner (A1)</option><option>Elementary (A2)</option><option>Intermediate (B1)</option><option>I am not sure</option></select></label><label>When to start<select><option>Autumn cohort (Oct 6)</option><option>Capsules (Oct 20)</option><option>Next term</option></select></label><label>Country<input name="country" autocomplete="country-name"></label><button class="btn btn-gold" type="submit">Request my consultation <span class="arr">→</span></button></form></div></section>

<section class="sec ivory" id="faq"><div class="w"><div class="head rv"><span class="eb">Your questions, answered</span>{h2('Everything worth asking','before you enrol.')}</div>{faqh()}<p class="center mt"><a class="btn btn-ghost" href="faq.html">See all questions</a></p></div></section>
<section class="band">{V('ag-cypress-road',P)}<div class="tint"></div><span class="frame"></span><div class="w rv"><span class="eb">Autumn cohorts · Oct 6</span>{h2('Culture speaks Italian.','What about you?')}<p>Join a live class broadcasting from Italy and begin with a conversation.</p><a class="btn btn-gold" href="#enrol">Begin your journey <span class="arr">→</span></a></div></section>
'''+foot(P)

# ================= COURSE PAGES =================
CEFR_TARGET={'A1.1':'Can understand and use familiar everyday expressions and very basic phrases, introduce themselves and interact in a simple way if the other person speaks slowly and clearly.',
'A1':'Can understand and use familiar everyday expressions and very basic phrases, introduce themselves and interact in a simple way if the other person speaks slowly and clearly.',
'A1.2':'Can ask and answer simple questions about personal details, where they live, people they know and things they have, and handle numbers, quantities, cost and time.',
'A2.1':'Can understand sentences and frequently used expressions related to areas of immediate relevance and communicate in simple, routine tasks.',
'A2':'Can understand sentences and frequently used expressions related to areas of immediate relevance and communicate in simple, routine tasks.',
'A2.2':'Can describe in simple terms aspects of their background, immediate environment and matters of immediate need, and narrate past events.',
'B1':'Can understand the main points of clear standard input on familiar matters, deal with most situations while travelling, and describe experiences, events, hopes and ambitions.'}
SK={'ci':[('Speaking','●●●●○'),('Listening','●●●●○'),('Reading','●●●○○'),('Writing','●●●○○'),('Grammar','●●●●●'),('Vocabulary','●●●●○'),('Culture','●●●○○')],
'ps':[('Speaking','●●●●●'),('Listening','●●●●●'),('Reading','●●○○○'),('Writing','●○○○○'),('Grammar','●●○○○'),('Vocabulary','●●●●○'),('Culture','●●●○○')],
'cap':[('Speaking','●●●○○'),('Listening','●●●●○'),('Reading','●●●○○'),('Writing','●○○○○'),('Grammar','●○○○○'),('Vocabulary','●●●●●'),('Culture','●●●●●')]}
PREREQ={'ci1':'None. Built for true beginners (A0).','ci2':'A1.1, or completion of CI Principiante. Placement conversation for newcomers.','ci3':'A1.2, or completion of CI Elementare.','ci4':'A2.1, or completion of CI Intermedio.',
'ps1':'None. Built for absolute beginners.','ps2':'A1, or completion of Al Caffè.','ps3':'A2, or completion of A Tavola.','ps4':'A2 secure, or completion of In Viaggio.','cap-food':'Open to every level. Sessions adapt to the group.','cap-art':'Open to every level. Sessions adapt to the group.','cap-opera':'Open to every level. Sessions adapt to the group.'}
def course(k):
    t,n,u,img,te,hv,st,tu=CO[k];d=D[k];P='../../';tn,tc=TN[te]
    cap=t=='cap';nl=20 if not cap else 6;mins=85 if not cap else 60
    tot=nl*mins;hrs=f'{tot//60} h {tot%60} min' if tot%60 else f'{tot//60} h'
    cefr=lvl(k);tgt=re.findall(r'(A\d(?:\.\d)?|B1)',cefr);tdesc=CEFR_TARGET.get(tgt[-1],'') if tgt and not cap else ''
    outs=[cl(o) for o in d['outcomes']]
    units=''.join(f'<details><summary><span class="n">{i+1:02d}</span><span class="t">{E(cl(s[0]))}</span><span class="m">{"Lesson" if not cap else "Session"} {i+1} · {mins} min</span></summary><p>{E(cl(s[1]))}</p></details>' for i,s in enumerate(d['syllabus']))
    pdf=f'{P}pdf/{k}-syllabus.pdf'
    nx=NEXT.get(k)
    tq=cl(T[te]['quote']);tq='. '.join(tq.split('. ')[:3]).rstrip('.')+'.'
    body=head(f'{n} · {cefr} · Club Italia',cl(d['promise']),P)+f'''
<section class="ch">{V(hv,P,poster=P+'assets/img/'+img)}<div class="tint"></div><div class="w"><div class="glass">
<div class="crumbs"><a href="{P}index.html">Club Italia</a> / <a href="{P}courses.html">Courses</a> / {E(n)}</div>
<div class="hero-badges"><span class="chip g">CEFR {cefr}</span><span class="chip">Live from {tc}</span><span class="chip">Biagio AI tutor included</span></div>
<h1 data-split>{E(n)}. <em>{E(cl(d['tag']).split(' · ')[-1])}.</em></h1><p class="lede">{E(cl(d['promise']))}</p>
<div class="ctas" style="display:flex;gap:.8rem;flex-wrap:wrap;margin-top:1.4rem"><a class="btn btn-gold" href="{P}index.html#enrol">Enrol now <span class="arr">→</span></a><a class="btn btn-line" href="#syllabus">Explore the {nl} units</a></div></div>
<div class="facts18 glass">{''.join(f'<div><span>{a}</span><b>{b}</b></div>' for a,b in [('CEFR',cefr),('Format',f'{nl} x {mins} min'),('Contact hours',hrs),('Group','10 to 12 adults'),('Teacher',tn),('Starts',st),('Tuition',tu)])}</div></div></section>

<section class="sec dark"><div class="w"><div class="head rv"><span class="eb">The DNA of this course</span><h2 data-split>Built for {"the absolute beginner" if k in ("ci1","ps1") else "your next step"}. <em>Taught from {tc}.</em></h2><p>{E(PREREQ[k])}</p></div>
<div class="dna">{''.join(f'<div class="gcard rv"><span class="n">0{i+1}</span><h3 style="margin:.8rem 0 .5rem">{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate([('Live, never pre-recorded',f'Every {"lesson" if not cap else "session"} is a live {mins}-minute class taught from {tc}.'),('Small by design','Ten to twelve adults, so everyone speaks and is corrected personally.'),('Anchored in a place',f'Each unit is set in a real Italian situation, so the words are the words Italians use.'),('Mapped to the CEFR','Can-do objectives for every unit, assessed at the end of the course.' if not cap else 'Vocabulary and cultural competence, adapted to your level.')]))}</div></div></section>

<section class="sec paper"><div class="w two"><div class="rv"><span class="eb">What you will learn</span><h2 data-split>By {"lesson" if not cap else "session"} {nl}, <em>you will…</em></h2>
{f'<div class="panel" style="margin-top:1.6rem"><span class="k" style="font:600 .62rem var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--oro3)">CEFR target · {tgt[-1]}</span><p style="margin-top:.5rem;font:italic 400 1.1rem var(--serif);color:var(--ink)">«{tdesc}»</p><p style="font-size:.74rem;color:var(--mut);margin-top:.5rem">Global descriptor, paraphrased from the Council of Europe CEFR.</p></div>' if tdesc else ''}</div>
<div class="panel rv"><h3>Can-do outcomes</h3><ul>{''.join(f'<li>{E(o)}</li>' for o in outs)}</ul></div></div></section>

<section class="sec ivory" id="syllabus"><div class="w"><div class="head rv"><span class="eb">The full curriculum</span><h2 data-split>{nl} units. <em>One clear arc.</em></h2><p>Every {"lesson" if not cap else "session"} has a named objective, a grammar or language focus and a setting. Open a unit to read it.</p></div>
<div class="syl rv" data-acc>{units}</div><p class="center mt"><a class="btn btn-ghost" href="{pdf}">Download the PDF syllabus <span class="arr">↓</span></a></p></div></section>

<section class="sec paper"><div class="w two"><div class="rv"><span class="eb">Skills coverage</span><h2 data-split>Where the hours <em>go.</em></h2><p style="margin-top:1rem;color:var(--mut)">Relative emphasis across the {nl} {"lessons" if not cap else "sessions"} of this {"structured" if t=="ci" else "spoken" if t=="ps" else "cultural"} track.</p></div>
<table class="grid-skills rv"><thead><tr><th>Skill</th><th>Emphasis</th></tr></thead><tbody>{''.join(f'<tr><td>{a}</td><td class="dots">{b}</td></tr>' for a,b in SK[t])}</tbody></table></div></section>

<section class="sec ivory"><div class="w"><div class="pill3">
<div class="panel rv"><h3>Assessment</h3><ul><li>Continuous feedback from your teacher in every lesson</li><li>{"Mid-course check at lesson 10" if not cap else "Short review in session 6"}</li><li>{"Final oral and written can-do assessment" if not cap else "No exam; a culture portfolio"}</li></ul><!-- TODO(owner): confirm assessment format and attendance rule --></div>
<div class="panel rv"><h3>Certificate</h3><ul><li>Club Italia certificate {"mapped to CEFR "+cefr if not cap else "of completion"}</li><li>Issued by eTeacher Group</li><li>Not an official exam: {"route to CILS or CELI at an authorised centre from A2" if not cap else "pairs with any Club Italia course"}</li></ul></div>
<div class="panel rv"><h3>Logistics</h3><ul><li>Live online classroom, any device</li><li>Every class recorded</li><li>Biagio AI tutor between classes</li><li>Seven day full refund</li></ul><!-- TODO(owner): weekly schedule and time zones --></div></div></div></section>

<section class="vfold sec">{V('ag-roma-statue' if tc=='Roma' else hv,P,poster=P+'assets/img/'+img)}<div class="tint"></div><div class="w"><div class="glass tprof rv" style="padding:2rem">
<img src="{P}assets/img/teacher-{te}.jpg" alt="{tn}"><div><span class="eb">Your teacher · {tc}</span><h2 style="color:#fff">{tn}</h2><p style="color:var(--oro2);font:600 .74rem var(--sans);letter-spacing:.1em;text-transform:uppercase;margin-top:.4rem">Native teacher · {E(", ".join(c.strip() for c in T[te]["cred"][:2] if len(c)<40))}</p>
<p style="margin-top:1rem;color:#f1ece2">{E(cl(T[te]['bio']))}</p><blockquote>«{E(tq)}»</blockquote><p style="margin-top:1.2rem"><a class="lnk" style="color:var(--oro2)" href="{P}pages/teachers/{te}.html">Full profile</a></p></div></div></div></section>
<!-- TODO(owner): teacher is a v16 composite profile -->

<section class="sec dark"><div class="w"><div class="head rv"><span class="eb">Tuition</span><h2 data-split>{E(n)}, <em>{tu}.</em></h2><p>{"Included in every Club Italia plan: annual from $62 a week, term $73, monthly $84." if not cap else "A six-session capsule, or included as two sessions in the annual plan."}</p></div>
<p class="center"><a class="btn btn-gold" href="{P}index.html#enrol">Reserve my seat <span class="arr">→</span></a></p></div></section>
<section class="sec ivory"><div class="w"><div class="head rv"><span class="eb">Questions</span><h2 data-split>Everything you <em>might be wondering.</em></h2></div>{faqh()}</div></section>
{f'<section class="sec-sm dark" style="padding:60px 0"><div class="w center"><a class="lnk" href="{P}{CO[nx][2]}" style="font-size:1rem">Next level → {CO[nx][1]} · {lvl(nx)}</a></div></section>' if nx else ''}
<section class="band">{V('ag-cypress-road',P)}<div class="tint"></div><span class="frame"></span><div class="w rv"><h2 data-split>Begin in {tc}. <em>Begin this autumn.</em></h2><p>{nl} live {"lessons" if not cap else "sessions"}. One native teacher. Your Italian.</p><a class="btn btn-gold" href="{P}index.html#enrol">Enrol now <span class="arr">→</span></a></div></section>
'''+foot(P)
    return body
def fix(s): return s.replace('—',', ').replace('–',' to ')
open('index.html','w').write(fix(home))
for k in ORDER: open(CO[k][2],'w').write(fix(course(k)))
print('ok')
