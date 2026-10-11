import re,json,html
exec(open('_v18_build.py').read().split('# ================= HOME')[0])
E=html.escape
def cl(s):
    s=str(s);s=re.sub(r'\s*[—–]\s*',', ',s);s=re.sub(r'\s+-\s+',', ',s);s=s.replace('→',' to ').replace('×','x').replace('  ',' ')
    return s.strip()
def lv(k): return cl(D[k]['cefr']).replace('Spoken ','').replace('Cultural, ','')
LL={'roma':[12.4823,41.8955],'firenze':[11.2558,43.7696],'bologna':[11.3426,44.4949],'venezia':[12.3355,45.4375],'milano':[9.19,45.4642],'napoli':[14.2681,40.8518],'palermo':[13.3615,38.1157]}
CITY=[('roma','Roma','marco','ag-roma-statue','ci1',-25),('firenze','Firenze','chiara','firenze-arno','ci2',20),('bologna','Bologna','giulia','bologna-portici','ci3',-10),('venezia','Venezia','francesca','ag-venice-gondola','ps3',30),('milano','Milano','alessandro','opera-scala','ps4',-35),('napoli','Napoli','luca','napoli-mare','ci4',40),('palermo','Palermo','sofia','ag-catania-statues','ci4',-15)]
def vid(n,P,keep=False,manual=False,cls='grade'):
    return f'<video class="{cls}" muted loop playsinline preload="none" poster="{P}assets/img/{n}-poster.jpg" data-src="{P}assets/video/{n}.mp4"{" data-manual" if manual else ""} aria-hidden="true"></video>'
def bg(n,P,wash='wl',par=True): return f'<div class="bg"{" data-par" if par else ""}>{vid(n,P)}</div><div class="wash {wash}"></div><div class="wash warm"></div>'
def head(title,desc,P,extra=''):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{E(desc)}"><meta name="theme-color" content="#0b1622">
<link rel="preconnect" href="https://api.fontshare.com"><link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=zodiak@300,400,301,401,500&f[]=satoshi@400,500,700&display=swap">{extra}<link rel="stylesheet" href="{P}css/v19.css"></head><body>
<div class="curtain" aria-hidden="true"><b>Club Italia</b></div><a class="skip" href="#main">Skip to content</a>
<header class="hd"><div class="w"><a class="logo" href="{P}index.html" aria-label="Club Italia home"><b>Club Italia</b><img src="{P}assets/img/eteacher-real-logo-white.png" alt="by eTeacher Group"></a>
<nav class="nv" aria-label="Primary"><a href="{P}courses.html">Courses</a><a href="{P}curriculum.html">Curriculum</a><a href="{P}method.html">Method</a><a href="{P}teachers.html">Teachers</a><a href="{P}biagio.html">Biagio</a><a href="{P}pricing.html">Tuition</a><a class="cta" href="{P}index.html#enrol">Enrol</a></nav><button class="menu" aria-expanded="false">Menu</button></div></header><main id="main">'''
def foot(P,mods=''):
    col=lambda t,ks: f'<div><h4>{t}</h4><ul>'+''.join(f'<li><a href="{P}{CO[k][2]}">{CO[k][1]}</a></li>' for k in ks)+'</ul></div>'
    return f'''</main><footer class="ft"><div class="w"><p class="big">Ci vediamo <em>in classe.</em></p><div class="g"><div><p>Live Italian for adults, taught from seven Italian cities. A school of eTeacher Group.</p><img src="{P}assets/img/eteacher-real-logo-white.png" alt="eTeacher Group" style="height:24px;margin-top:1.4rem"><p style="margin-top:1rem"><a href="mailto:advisor@eTeacherGroup.com">advisor@eTeacherGroup.com</a></p></div>
{col('Il Corso',['ci1','ci2','ci3','ci4'])}{col('Parliamo',['ps1','ps2','ps3','ps4'])}{col('Capsule',['cap-food','cap-art','cap-opera'])}<div><h4>School</h4><ul><li><a href="{P}curriculum.html">Curriculum</a></li><li><a href="{P}certifications.html">Certification</a></li><li><a href="{P}teachers.html">Teachers</a></li><li><a href="{P}faq.html">Questions</a></li><li><a href="{P}contact.html">Contact</a></li></ul></div></div>
<div class="legal"><span>© 2026 eTeacher Group. Club Italia is a school of eTeacher Group. <a href="{P}privacy.html">Privacy</a> · <a href="{P}terms.html">Terms</a></span><span>Footage licensed via Artgrid. Map data © OpenStreetMap contributors, OpenMapTiles, OpenFreeMap; terrain from Mapzen open elevation data; outline Natural Earth. Music: Vivaldi, «La primavera», CC BY SA 3.0. CILS and CELI are run by the Università per Stranieri di Siena and di Perugia. Club Italia is not an exam centre.</span></div></div></footer>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script><script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script><script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js" defer></script><script src="{P}js/v19.js" defer></script>{mods}</body></html>'''
def promise(k): return cl(D[k]['promise']).split('. ')[0].rstrip('.')+'.'
def tuition(k): return CO[k][7].replace(' a week',' a week')
def fmt(k): c=CO[k][0];return ('20 lessons','85 minutes') if c!='cap' else ('6 sessions','60 minutes')
def hours(k): c=CO[k][0];return '28 h 20' if c!='cap' else '6 h'
CVID={'ci1':'roma-piazza','ci2':'firenze-arno','ci3':'bologna-portici','ci4':'napoli-mare','ps1':'ag-market-produce','ps2':'cucina-pasta','ps3':'venezia-canal','ps4':'ag-luxury-car','cap-food':'ag-pizza-oven','cap-art':'ag-medieval-aerial','cap-opera':'opera-scala'}
import os
for k,v in CVID.items():
    if not os.path.exists(f'assets/img/{v}-poster.jpg'): os.system(f'ffmpeg -loglevel error -y -ss 1 -i assets/video/{v}.mp4 -frames:v 1 -vf scale=1600:-2 -q:v 4 assets/img/{v}-poster.jpg')
def panel(k,P,i):
    t,n,u,img,te,hv,st,tu=CO[k];a,b=fmt(k)
    return f'''<a class="panel" href="{P}{u}">{bg(CVID[k],P,'wb',False)}<div class="w"><span class="n">{i:02d} · {lv(k)}</span><h3>{E(n)}</h3><p>{E(promise(k))}</p><dl><div><dt>Teacher</dt><dd>{TN[te][0].split()[0]}, {TN[te][1]}</dd></div><div><dt>Format</dt><dd>{a}</dd></div><div><dt>Tuition</dt><dd>{tu}</dd></div></dl></div></a>'''
def intro(t,em,p,c): return f'<div class="panel intro" style="--c:{c}"><div class="w"><h3>{t} <em>{em}</em></h3><p>{p}</p></div></div>'
FAQ=[('Are the classes live?','Yes. Every class is taught live by a native teacher in Italy. Recordings are there for review.'),('How big is a class?','Ten to twelve adults. Everyone speaks in every lesson.'),('What is included?','Twenty live lessons of 85 minutes, the syllabus, recordings, Biagio and a Club Italia certificate. A capsule is six sessions of 60 minutes.'),('Do you prepare for CILS and CELI?','Yes, from A2. You sit the exam at an authorised centre of the Università per Stranieri di Siena or di Perugia.'),('What does it cost?','From $62 a week on the annual plan. Full refund within seven days of your first lesson.'),('Who are the teachers?','Native Italians qualified to teach Italian as a foreign language, each in their own city.')]
def faqh(): return '<div class="faq" data-acc>'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)+'</div>'
LAD=[{'k':'A1','h':'You can <em>introduce yourself</em> and get by.','u':['Greet and introduce yourself','Order at a bar or a trattoria','Ask the way','Handle prices, dates and times'],'r':'CI Principiante, CI Elementare, Al Caffè'},
{'k':'A2','h':'You can <em>talk about your life.</em>','u':['Tell what happened yesterday','Make plans and bookings','Describe people and places','Solve problems while travelling'],'r':'CI Intermedio, CI Avanzato, A Tavola, In Viaggio'},
{'k':'B1','h':'You can <em>hold a real conversation.</em>','u':['Follow clear everyday speech','Give and explain opinions','Handle most travel situations','Write connected text'],'r':'Chiacchierando and CILS or CELI B1 preparation'},
{'k':'B2','h':'You can <em>argue and read the news.</em>','u':['Follow complex texts','Speak with fluency','Write a clear argument'],'r':'Advanced cohorts on request'},
{'k':'C1','h':'You can <em>work and study</em> in Italian.','u':['Speak without searching for words','Use Italian at work and university','Write well structured detail'],'r':'Advanced cohorts on request'},
{'k':'C2','h':'You can <em>understand nearly everything.</em>','u':['Read literature with ease','Express fine shades of meaning','Summarise from many sources'],'r':'Advanced cohorts on request'}]
VO=[('biagio-line-caffe','Al caffè','«Un cappuccino e un cornetto, per favore.»','A cappuccino and a cornetto, please.'),('biagio-line-tavola','A tavola','«Prendo la pasta alla carbonara. Grazie.»',"I'll have the carbonara. Thank you."),('biagio-line-strada','Per strada',"«Mi scusi, dov'è la metropolitana?»",'Excuse me, where is the metro?'),('biagio-line-corregge','Correzione',"«Si dice sono andato, non ho andato.»",'With andare, use essere.')]
QS=[('Diane Weller','Chicago, CI Principiante','In three months I ordered dinner in Trastevere and the waiter answered in Italian all night.'),('Robert Hensley','Austin, A Tavola','The teacher cooks while she teaches. That changed how I hear the language.'),('Sarah Kim',"San Francisco, L'Opera",'Six sessions on La Bohème. Now I understand why Italians cry in the third act.'),('James Whitaker','London, CI Elementare','Small classes, real corrections, no drills. Like a Florentine institute.'),('Linda Bauer','Toronto, CI Intermedio','Chiara fixed a mistake I had made since 2014. In one class.')]
POST={}
P=''
cdata=[]
for k,n,te,v,c,b in CITY:
    d=D[c];cdata.append({'k':k,'n':n,'ll':LL[k],'b':b,'t':TN[te][0],'ti':f'assets/img/teacher-{te}.jpg','c':CO[c][1]+', '+lv(c),'v':f'assets/video/{v}.mp4','p':f'assets/img/{v}-poster.jpg','h':CO[c][2],'u':[[i+1,cl(s[0])] for i,s in enumerate(d['syllabus'][:4])]})
CUL=[('ag-medieval-aerial','Arte.','From Roman forums to Renaissance domes.','pillar-art'),('ag-chefs-street','Cucina.','A Bolognese market, a Neapolitan oven, a Tuscan table.','pillar-food'),('ag-venice-gondola','Viaggio.','From the canals of Venice to the Amalfi coast.','pillar-travel'),('ag-catania-statues','Cinema.','Fellini, Sorrentino, the piazza on screen.','pillar-cinema'),('ag-rome-basilica','Opera.','Verdi, Puccini, Rossini, in the original.','pillar-opera'),('ag-tradition-festival','Tradizione.','Carnevale, the Palio, the feast days.','pillar-tradition')]
FACV={'marco':'ag-roma-statue','chiara':'firenze-arno','giulia':'bologna-portici','alessandro':'opera-scala','francesca':'ag-venice-gondola','luca':'napoli-mare','sofia':'ag-catania-statues'}
def MAPF(P):
    cd=[dict(c,ti=P+c['ti'],v=P+c['v'],p=P+c['p'],h=P+c['h']) for c in cdata]
    return f'''<section class="mapf" id="atlas"><div id="map" data-base="{P}"></div><div class="mapui"><div class="w"><div><h2 class="d3" data-split>Fly to your <em>teacher.</em></h2>
<div class="jlist" role="group" aria-label="Choose a city"><button data-k="all" aria-pressed="true">All of Italy<span>7 cities</span></button>{''.join(f'<button data-k="{k}" aria-pressed="false">{n}<span>{CO[c][1]}</span></button>' for k,n,te,v,c,b in CITY)}</div></div><div></div>
<div class="mcard glass" id="mcard" aria-live="polite"><div class="mv"><video class="grade" muted loop playsinline autoplay></video></div><div class="bd"><h3></h3><div class="t"><img alt="" src="{P}assets/img/teacher-marco.jpg"><div><b id="mt"></b><span id="mc"></span></div></div><ol></ol><p style="margin-top:1.4rem"><a class="cta" href="#">Open the course <i></i></a></p></div></div></div></div>
<script type="application/json" id="citydata">{json.dumps(cd,ensure_ascii=False)}</script></section>'''
def CEFRF(P):
    return f'''<section class="cefr" id="levels"><div class="pin"><canvas id="gl3d" aria-hidden="true"></canvas><div class="w"><div class="txt"><span class="lv" id="lvk">A1</span><h3 id="lvh"></h3><ul id="lvu"></ul><p class="note"><span id="lvr"></span>. Levels follow the Council of Europe CEFR.</p><p style="margin-top:1.4rem"><a class="lk" href="{P}curriculum.html">The full curriculum</a></p></div></div></div>
<script type="application/json" id="laddata">{json.dumps(LAD,ensure_ascii=False)}</script></section>'''
mani='Seven cities. Seven teachers. One language, learned where it is spoken.'
MAPHEAD='<link rel="stylesheet" href="https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.css">'
MODSF=lambda P:f'<script src="https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.js" defer></script><script src="{P}js/v19-map.js" defer></script><script type="module" src="{P}js/v19-3d.js"></script>'
MODS=MODSF('')
home=head('Club Italia · Italian, taught live from Italy','Live Italian classes for adults with native teachers in seven Italian cities.',P,MAPHEAD)+f'''
<section class="fold hero"><div class="bg"><video id="herovid" class="grade" autoplay muted loop playsinline preload="auto" poster="assets/img/ag-roma-statue-poster.jpg" crossorigin="anonymous" src="assets/video/ag-roma-statue.mp4" data-keep></video><canvas id="glhero" style="opacity:0;transition:opacity 1.2s;position:absolute;inset:0"></canvas></div><div class="wash wl"></div>
<div class="w"><h1 class="d1" data-split>Italian, <em>live from Italy.</em></h1><p class="lead" style="margin-top:2rem">Small live classes with native teachers in seven Italian cities.</p>
<div class="row"><a class="cta" href="#enrol">Reserve your seat <i></i></a><a class="cta ghost" href="#courses">See the courses</a><button class="cta ghost" id="music">Music off</button></div>
<div class="facts"><div><b>7</b>cities</div><div><b>12</b>learners at most</div><div><b>85</b>minutes, live</div><div><b>A1 to B1</b>on the CEFR</div></div></div><audio id="theme" src="assets/audio/hero-italian-theme.mp3" preload="none" loop></audio></section>

<section class="fold stmt">{bg('ag-tuscany-drone',P,'wt')}<div class="w"><p>{' '.join(f'<span class="wd">{w}</span>' for w in mani.split())}</p></div></section>

<section class="rail" id="courses"><div class="track">
{intro('Il Corso.','Four steps to A2.','The structured course. Grammar, vocabulary and conversation, twenty live lessons per level.','#0f4c5c')}{''.join(panel(k,P,i+1) for i,k in enumerate(['ci1','ci2','ci3','ci4']))}
{intro('Parliamo.','Speak first.','The spoken track. Four Italian scenes, from the bar to the open road.','#9e2b25')}{''.join(panel(k,P,i+5) for i,k in enumerate(['ps1','ps2','ps3','ps4']))}
{intro('Capsule.','One passion.','Six evenings inside food, art or opera. Any level.','#7a5a2a')}{''.join(panel(k,P,i+9) for i,k in enumerate(['cap-food','cap-art','cap-opera']))}
</div><div class="rprog"></div></section>

'''+MAPF(P)+f'''

<section class="stage" id="culture"><div class="pin">{''.join(f'<div class="bgv{" on" if i==0 else ""}">{vid(v,P,manual=True)}</div>' for i,(v,t,p,u) in enumerate(CUL))}<div class="wash wb"></div><div class="wash warm"></div>
<div class="w" style="position:relative"><h2 class="d3 top">Culture speaks Italian. <em>Do you?</em></h2><span class="count">01</span>{''.join(f'<a class="ch" href="pages/culture/{u}.html" style="text-decoration:none"><h3>{t}</h3><p>{p}</p></a>' for v,t,p,u in CUL)}</div></div></section>

'''+CEFRF(P)+f'''

<section class="fold" id="classroom">{bg('class-demo',P,'wl')}<div class="w"><span class="kick">Inside a lesson</span><h2 class="d2" data-split>A real classroom. <em>At home.</em></h2><p class="lead" style="margin-top:2rem">Your teacher is in Rome or Venice. You are on your sofa. Twelve adults, eighty five minutes, and you speak the whole time.</p><p style="margin-top:2.4rem"><a class="cta" href="sample-class.html">Watch a sample class <i></i></a></p></div></section>

<section class="fold fac" id="faculty">{''.join(f'<div class="bgv{" on" if i==0 else ""}" data-k="{t}">{vid(FACV[t],P,manual=True)}</div>' for i,t in enumerate(TN))}<div class="wash wl"></div><div class="wash warm"></div>
<img class="port" src="assets/img/teacher-marco.jpg" alt="Marco Rinaldi"><div class="w"><span class="kick">The teachers</span><h2 class="d3" data-split>Seven Italians. <em>Seven cities.</em></h2>
<div class="names">{''.join(f'<a class="nm{" on" if i==0 else ""}" href="pages/teachers/{t}.html" data-k="{t}" data-img="assets/img/teacher-{t}.jpg" data-alt="{n}"><b>{n}</b><span>{c}</span></a>' for i,(t,(n,c)) in enumerate(TN.items()))}</div></div></section>

<section class="fold bia" id="biagio">{bg('ag-rome-basilica',P,'wl')}<div class="w"><div class="fig"><img src="assets/img/biagio-3d-hero.png" alt="Biagio, the Club Italia AI tutor"></div>
<div><span class="kick">Between classes</span><h2 class="d3" data-split>Meet Biagio. <em>He never sleeps.</em></h2><p class="lead" style="margin-top:1.4rem">An AI tutor trained on your syllabus. Practise any hour, in a warm Roman voice.</p>
<div class="wave" aria-hidden="true">{'<i></i>'*32}</div><p id="bcap" style="font:italic 300 1.5rem var(--serif);min-height:2em">Press a line to hear him.</p>
<div class="voices">{''.join(f'<button class="voice" data-audio="assets/audio/{a}.mp3" data-line="{E(q)}<br><small>{E(tr)}</small>"><span class="pl"></span><span><b>{t}</b><small>{q}</small></span></button>' for a,t,q,tr in VO)}</div><p style="margin-top:2rem"><a class="cta" href="biagio.html">Discover Biagio <i></i></a></p></div></div></section>

<!-- TODO(owner): learner quotes are v16 pitch placeholders -->
<section class="fold" id="voices">{bg('ag-venice-docked',P,'wl')}<div class="w"><span class="kick">Learners</span><div class="qs">{''.join(f'<figure><blockquote>«{E(q)}»</blockquote><figcaption>{n}, {c}</figcaption></figure>' for n,c,q in QS)}</div></div></section>

<!-- TODO(owner): tuition is a v16 placeholder -->
<section class="fold" id="tuition">{bg('ag-wine-bottles',P,'wt')}<div class="w"><h2 class="d3" data-split>One curriculum. <em>Three ways to pay.</em></h2>
<div class="plans"><div class="plan glass rv"><h3>Monthly</h3><div class="p">$84<small> a week</small></div><p>Billed $336 a month.</p><ul><li>Every live lesson on your track</li><li>Biagio</li><li>Recordings</li></ul><a class="cta ghost" href="#enrol">Start monthly</a></div>
<div class="plan glass f rv"><h3>Annual <em>best value</em></h3><div class="p">$62<small> a week</small></div><p>Billed $3,224 once.</p><ul><li>Everything in monthly</li><li>Two capsule sessions</li><li>Priority teacher placement</li><li>Printed certificate</li></ul><a class="cta" href="#enrol">Start annual</a></div>
<div class="plan glass rv"><h3>Term</h3><div class="p">$73<small> a week</small></div><p>Billed $876 for twelve weeks.</p><ul><li>All lessons of one term</li><li>Biagio for the term</li><li>Placement included</li></ul><a class="cta ghost" href="#enrol">Start a term</a></div></div>
<p style="margin-top:2rem;font-size:1.1rem">Full refund within seven days of your first lesson.</p></div></section>

<section class="fold enrol" id="enrol">{bg('ag-cypress-road',P,'wl')}<div class="w"><div><h2 class="d2" data-split>Your road <em>starts here.</em></h2><p class="lead" style="margin-top:2rem">Tell us where you are. An advisor finds your level, your teacher and your start date, and replies within one working day.</p></div>
<!-- TODO(owner): connect to eTeacher CRM --><form class="form paper" id="lead"><h3>Book a free consultation</h3><label>First name<input required autocomplete="given-name"></label><label>Last name<input required autocomplete="family-name"></label><label class="full">Email<input type="email" required autocomplete="email"></label><label>Your Italian<select><option>None yet</option><option>A few words</option><option>Basic conversation</option><option>I get by</option><option>Not sure</option></select></label><label>Start<select><option>Autumn, from 6 October</option><option>Capsules, from 20 October</option><option>Next term</option></select></label><button class="cta" type="submit">Request my consultation <i></i></button></form></div></section>

<section class="fold" id="faq">{bg('ag-camogli-coast',P,'wt')}<div class="w"><div class="paper" style="padding:clamp(2rem,4vw,4rem);max-width:980px"><h2 class="d3" style="margin-bottom:1.6rem">Good <em>questions.</em></h2>{faqh()}<p style="margin-top:1.6rem"><a class="lk" href="faq.html">All questions</a></p></div></div></section>
'''+foot(P,MODS)
open('index.html','w').write(home)

# ===== course template
CEFRD={'A1.1':'Understands and uses familiar everyday expressions and very basic phrases. Introduces themselves and interacts simply when the other person speaks slowly.','A1.2':'Asks and answers simple questions about where they live, people they know and things they have. Handles numbers, prices and time.','A1':'Understands and uses familiar everyday expressions and very basic phrases. Introduces themselves and interacts simply.','A2.1':'Understands frequent expressions about immediate needs and communicates in simple routine tasks.','A2.2':'Describes their background and surroundings in simple terms, and tells what happened.','A2':'Understands frequent expressions about immediate needs and communicates in simple routine tasks.','B1':'Understands the main points of clear speech on familiar matters, handles most travel situations and explains opinions and plans.'}
SKL={'ci':[('Speaking',80),('Listening',80),('Reading',60),('Writing',60),('Grammar',100),('Vocabulary',80),('Culture',60)],'ps':[('Speaking',100),('Listening',100),('Reading',40),('Writing',20),('Grammar',40),('Vocabulary',80),('Culture',60)],'cap':[('Speaking',60),('Listening',80),('Reading',60),('Writing',20),('Grammar',20),('Vocabulary',100),('Culture',100)]}
PRE={'ci1':'None. Built for true beginners.','ci2':'A1.1, or CI Principiante.','ci3':'A1.2, or CI Elementare.','ci4':'A2.1, or CI Intermedio.','ps1':'None. Built for beginners.','ps2':'A1, or Al Caffè.','ps3':'A2, or A Tavola.','ps4':'A2, or In Viaggio.','cap-food':'None. Any level.','cap-art':'None. Any level.','cap-opera':'None. Any level.'}
for k in ORDER:
    t,n,u,img,te,hv,st,tu=CO[k];P='../../';d=D[k];a,b=fmt(k);cap=t=='cap';tn,tc=TN[te]
    tg=re.findall(r'(A\d(?:\.\d)?|B1)',lv(k));desc=CEFRD.get(tg[-1]) if tg and not cap else None
    units=''.join(f'<li><b>{i+1:02d}</b><div><h4>{E(cl(s[0]))}</h4><p>{E(cl(s[1]))}</p></div></li>' for i,s in enumerate(d['syllabus']))
    nx=NEXT.get(k);q=cl(T[te]['quote']);q='. '.join(q.split('. ')[:2]).rstrip('.')+'.'
    cred=', '.join(c.strip() for c in T[te]['cred'][:2] if len(c)<40)
    pg=head(f'{n} · Club Italia',promise(k),P)+f'''
<section class="fold hero">{bg(CVID[k],P,'wl',False).replace('<video','<video autoplay data-keep',1)}<div class="w"><span class="kick"><a href="{P}courses.html" style="text-decoration:none">Courses</a> · {lv(k)} · taught from {tc}</span><h1 class="d1" data-split>{E(n)}<em>.</em></h1><p class="lead" style="margin-top:1.6rem">{E(cl(d['promise']))}</p>
<div class="row"><a class="cta" href="{P}index.html#enrol">Reserve your seat <i></i></a><a class="cta ghost" href="#syllabus">See all {len(d['syllabus'])} units</a></div>
<dl class="facts"><div><dt>Level</dt><dd>{lv(k)}</dd></div><div><dt>{a}</dt><dd>{b} each</dd></div><div><dt>Teacher</dt><dd>{tn}</dd></div><div><dt>Starts</dt><dd>{st}</dd></div></dl></div></section>

<section class="fold">{bg(hv if hv!=CVID[k] else 'ag-tuscany-drone',P,'wl')}<div class="w two"><div><span class="kick">What you will be able to do</span><h2 class="d3" data-split>By the last {"lesson" if not cap else "session"}, <em>you can:</em></h2>{f'<p class="lead" style="margin-top:2rem;font-family:var(--serif);font-style:italic">«{desc}»</p><p style="margin-top:.8rem;font-size:1rem">CEFR {tg[-1]}, Council of Europe</p>' if desc else ''}</div>
<div class="paper" style="padding:2.6rem"><ul class="can">{''.join(f'<li>{E(cl(o))}</li>' for o in d['outcomes'])}</ul></div></div></section>

<section class="fold" id="syllabus">{bg('ag-medieval-aerial' if k!='cap-art' else 'ag-rome-basilica',P,'wt')}<div class="w"><div class="paper" style="padding:clamp(2rem,4vw,4rem)"><span class="kick" style="color:var(--terra)">Syllabus</span><h2 class="d3" style="margin-bottom:2rem">{len(d['syllabus'])} units. <em>One clear arc.</em></h2><ol class="units">{units}</ol>
<p style="margin-top:2rem"><a class="lk" href="{P}pdf/{k}-syllabus.pdf">Download the syllabus as PDF</a></p></div></div></section>

<section class="fold">{bg('ag-san-gimignano',P,'wl')}<div class="w two"><div><span class="kick">Where the time goes</span><h2 class="d3" data-split>Built for <em>{"structure" if t=="ci" else "speaking" if t=="ps" else "culture"}.</em></h2><p class="lead" style="margin-top:1.6rem">{hours(k)} of live teaching. Entry level: {PRE[k]}</p></div>
<div class="glass" style="padding:2.4rem"><div class="skills">{''.join(f'<div><span>{s}</span><i style="width:{w}%"></i></div>' for s,w in SKL[t])}</div></div></div></section>

<section class="fold">{bg('ag-zoom-student',P,'wl')}<div class="w"><h2 class="d3" data-split style="margin-bottom:2.4rem">How you are <em>assessed.</em></h2><div class="three">
<div class="glass"><h3>Assessment</h3><ul class="can" style="font-size:1.1rem"><li>Feedback in every lesson</li><li>{"A check at lesson 10" if not cap else "A review in session 6"}</li><li>{"A final spoken and written assessment" if not cap else "No exam"}</li></ul><!-- TODO(owner): confirm assessment and attendance rule --></div>
<div class="glass"><h3>Certificate</h3><ul class="can" style="font-size:1.1rem"><li>Club Italia certificate{", CEFR "+lv(k) if not cap else ""}</li><li>Issued by eTeacher Group</li><li>Not an official exam. {"CILS and CELI from A2." if not cap else ""}</li></ul></div>
<div class="glass"><h3>Logistics</h3><ul class="can" style="font-size:1.1rem"><li>Live online, any device</li><li>Every class recorded</li><li>Biagio between classes</li><li>Seven day refund</li></ul><!-- TODO(owner): weekly times and time zones --></div></div></div></section>

<!-- TODO(owner): teacher is a v16 composite profile -->
<section class="fold">{bg(FACV[te],P,'wl')}<div class="w two" style="align-items:center"><img src="{P}assets/img/teacher-{te}.jpg" alt="{tn}" style="width:min(100%,460px);aspect-ratio:3/4;object-fit:cover;border-radius:28px;box-shadow:0 60px 120px -40px rgba(0,0,0,.7)">
<div><span class="kick">Your teacher, in {tc}</span><h2 class="d2">{tn.split()[0]}<em>.</em></h2><p style="margin-top:1rem;font-size:1.1rem">Native Italian. {E(cred)}.</p><p class="lead" style="margin-top:1.4rem;font-family:var(--serif);font-style:italic;max-width:30ch">«{E(q)}»</p><p style="margin-top:2rem"><a class="lk" href="{P}pages/teachers/{te}.html">Read {tn.split()[0]}'s story</a></p></div></div></section>

<section class="fold">{bg('ag-cypress-road',P,'wt')}<div class="w" style="text-align:center"><h2 class="d2" data-split>{E(n)}. <em>{tu}.</em></h2><p class="lead" style="margin:2rem auto 0">{"Included in every plan. From $62 a week on the annual plan." if not cap else "Six sessions, or two sessions included in the annual plan."}</p><div class="row" style="justify-content:center;display:flex;gap:1rem;margin-top:2.4rem;flex-wrap:wrap"><a class="cta" href="{P}index.html#enrol">Reserve your seat <i></i></a>{f'<a class="cta ghost" href="{P}{CO[nx][2]}">Next: {CO[nx][1]}</a>' if nx else ''}</div></div></section>
'''+foot(P)
    open(u,'w').write(pg)
print('built')
