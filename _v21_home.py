import re,json,html as H
from bs4 import BeautifulSoup
exec(open('_v20_build.py').read().split("home=head(")[0])
src=open('/workspace/faport/index.html').read()
S=BeautifulSoup(src,'html.parser')
def F(h): return BeautifulSoup(h,'html.parser')
def put(sel,h,root=None):
    e=(root or S).select_one(sel); e.clear(); e.append(F(h)); return e
def swap(e,h): e.replace_with(F(h))
SVG_ARROW='<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
def V(n,attrs='autoplay loop muted playsinline preload="metadata"'): return f'<video {attrs} poster="assets/img/{n}-poster.jpg"><source src="assets/video/{n}.mp4" type="video/mp4"></video>'
# ---------- head
S.title.string='Club Italia by eTeacher · Italian, taught live from Italy'
S.find('meta',attrs={'name':'description'})['content']='Live Italian courses for adults, taught by DITALS certified native teachers in seven Italian cities. CEFR aligned, groups of ten to twelve.'
for l in S.find_all('link',href=True):
    h=l['href']
    if h.startswith('css/'): l['href']='fa/'+h.split('?')[0]
    if 'favicon' in h: l.decompose()
for sc in S.find_all('script'):
    s=sc.get('src','')
    if 'eteacher-leads' in s or 'serviceWorker' in (sc.string or ''): sc.decompose(); continue
    if s.startswith('js/'): sc['src']='fa/'+s.split('?')[0]
for m in S.find_all('meta',attrs={'http-equiv':True}): m.decompose()
S.head.append(F('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Inter:wght@300;400;500;600;700&display=swap"><link rel="stylesheet" href="fa/css/ci.css"><link rel="stylesheet" href="fa/css/ci-light.css">'))
# ---------- header / nav
LOCK='<span class="ci-lock"><span class="ci-name">Club Italia</span><span class="ci-by">by <img src="assets/img/eteacher-real-logo-white.png" alt="eTeacher Group"></span></span>'
for a in S.select('a.nav-logo'): a.clear(); a.append(F(LOCK)); a['aria-label']='Club Italia by eTeacher, home'
NAV=[('courses.html','Courses'),('how-it-works.html','How it works'),('pricing.html','Pricing'),('method.html','Our method'),('biagio.html','Biagio AI tutor'),('culture.html','Italian culture'),('about.html','About us')]
nm=S.select_one('nav.nav-menu'); cta=nm.select_one('a.nav-cta')
items=''.join(f'<div class="nav-item"><a class="nav-link" href="{u}">{t}</a></div>' for u,t in NAV)
nm.clear(); nm.append(F(items)); cta['href']='pricing.html'; cta.string='Enrol now'; nm.append(cta)
dr=S.select_one('div.nav-drawer'); close=dr.select_one('button')
dr.clear(); dr.append(close); dr.append(F(''.join(f'<a href="{u}">{t}</a>' for u,t in NAV)+'<a class="btn btn-gold" href="pricing.html">Enrol now</a>'))
secs=S.body.find_all('section',recursive=False)
byc=lambda c:[x for x in secs if c in (x.get('class') or [])+[x.get('id') or '']][0]
# ---------- hero
hero=secs[0]
put('.hero-bg',V('ag-roma-statue','autoplay loop muted playsinline preload="auto"'),hero)
hero.select_one('h1').clear(); hero.select_one('h1').append(F('Italian, taught<br>live <span class="gold-ital">from Italy</span>'))
hero.select_one('.hero-sub').string='Club Italia by eTeacher. Live Italian courses for adults, taught by DITALS certified teachers from seven Italian cities.'
b=hero.select_one('.hero-ctas a.btn'); b.string='Talk to an advisor'
for t in hero.select('img[src*=trustpilot]'): t['src']='assets/img/'+('trustpilot-logo.svg' if 'logo' in t['src'] else 'trustpilot-logo.svg')
tp=hero.select_one('.hero-trustpilot'); swap(tp,'<div class="ci-hero-note">CEFR A0 to B1 &nbsp;·&nbsp; Groups of ten to twelve &nbsp;·&nbsp; Twenty live lessons per level</div>')
# ---------- courses
cs=secs[1]
cs.select_one('p.eyebrow').string='Our courses'
h=cs.select_one('h2'); h.clear(); h.append(F('Choose your path.<br>Start speaking <span class="gold-ital">Italian</span>.'))
cs.select_one('p.lede').string='Two collections of CEFR aligned courses, each taught live by one teacher from one Italian city.'
def ccard(btn,eb,title,sub,n,lv_,act):
    btn.select_one('.cls-card-eyebrow').string=eb; btn.select_one('.cls-card-title').string=title; btn.select_one('.cls-card-sub').string=sub
    vals=btn.select('.cls-meta-val'); vals[0].string=str(n); vals[1].string=lv_; vals[2].string='20'; vals[3].string='85 min'
    btn.select_one('.cls-card-action-text').string=act
bs=cs.select('button.cls-card')
ccard(bs[0],'Collection 01 · Structured','Il Corso','Grammar, vocabulary and culture, city by city.',4,'A0 to A2.2','Explore the four courses')
bs[0].select_one('.cls-bestseller').string='Most chosen'
ccard(bs[1],'Collection 02 · Spoken','Parliamo','Speaking first. Four Italian scenes, one per course.',4,'A1 to B1','Explore the four courses')
def course_art(art,k,cls):
    t,n,u,img,te,hv,st,tu=CO[k]
    art.clear(); art.append(F(f'<div class="cls-course-media"><img loading="lazy" decoding="async" src="assets/img/{img}" alt="{E(n)}, taught live from {TN[te][1]}"></div><div class="cls-course-body"><span class="cls-course-level">{lv(k)}</span><h4 class="cls-course-name">{E(n)}</h4><span class="cls-course-region">{TN[te][1]} · with {TN[te][0].split()[0]}</span><p class="cls-course-hook">{E(promise(k))}</p><a class="cls-course-link" href="{u}">View course <span aria-hidden="true"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.6" style="vertical-align:-2px"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span></a></div>'))
rails=cs.select('.cls-rail')
for rail,keys,cls in [(rails[0],['ci1','ci2','ci3','ci4'],'cls-course-fa'),(rails[1],['ps1','ps2','ps3','ps4'],'cls-course-lsf')]:
    arts=rail.select('article'); tmpl=str(arts[0])
    for a in arts: a.decompose()
    for k in keys:
        a=F(tmpl).article; course_art(a,k,cls); rail.append(a)
# ---------- journey hiw3
j=byc('hiw3-section')
j.select_one('p.eyebrow').string='The learning journey'
j.select_one('h2').clear(); j.select_one('h2').append(F('From <span class="gold-ital">buongiorno</span> to your CEFR certificate'))
j.select_one('p.lede').string='One clear route, from your first lesson to a documented CEFR level.'
for e,(lv_,cap) in zip(j.select('.han'),[('A0','Buongiorno'),('A1.1','First words'),('A1.2','Everyday Italian'),('A2.1','Confident'),('A2.2','Certified')]):
    e.select_one('.han-lvl').string=lv_; e.select_one('.han-cap').string=cap
ST=[('Step one','Placement and enrolment','A short placement conversation with an advisor places you at the right CEFR level.','Free placement'),
('Step two','Live lessons','Twenty live lessons of 85 minutes, in a group of ten to twelve, with one DITALS certified teacher.','28 contact hours per level'),
('Step three','Practice with Biagio','Between lessons, Biagio drills pronunciation and the week\'s structures, at any hour.','Always available'),
('Step four','Review and assessment','Every lesson is recorded. Progress is checked against the can-do descriptors of each unit.','Can-do checkpoints'),
('The finish','Certificate of completion','Complete the level and receive a certificate stating your CEFR level.','CEFR aligned')]
for e,(k_,n_,d_,t_) in zip(j.select('.hiw3-card'),ST):
    e.select_one('.hiw3-kick').string=k_; e.select_one('.hiw3-name').string=n_; e.select_one('.hiw3-desc').string=d_; e.select_one('.hiw3-tag').string=t_
a=j.select_one('a.btn'); a.string='See the full journey'; a['href']='how-it-works.html'
# ---------- method s5
m=byc('s5')
m.select_one('.s5-eyebrow').string='A structured, CEFR aligned curriculum'
m.select_one('.s5-title').clear(); m.select_one('.s5-title').append(F('A curriculum written by specialists in <span class="gold-ital">Italian as a foreign language</span>'))
m.select_one('.s5-lede').string='Action oriented and communicative, aligned with the Council of Europe framework. Every unit states what you will be able to do, then teaches it.'
for c,(fr,tt,tx) in zip(m.select('.s5-card'),[('Imparare facendo','You act, you speak','Each unit ends in a real task: ordering, asking, booking, explaining. Grammar serves the task.'),
('Lingua in contesto','Learned where it is lived','Every unit is set in a real Italian place, taught by a teacher who lives there.'),
('La cultura al centro','Culture at the core','Can-do descriptors from A0 to B1, with the art, food and manners that give the words their meaning.')]):
    c.select_one('.s5-fr').string=fr; c.select_one('.s5-cardtt').string=tt; c.select_one('.s5-cardtx').string=tx
put('.s5-cred-list',''.join(f'<a class="s5-cite" href="{u}" target="_blank" rel="noopener"><span class="s5-cite-yr">{y}</span><span class="s5-cite-tx">{t}</span><span class="s5-cite-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M7 17L17 7M9 7h8v8"/></svg></span></a>' for y,t,u in [
 ('2020','Council of Europe, CEFR Companion Volume','https://www.coe.int/en/web/common-european-framework-reference-languages'),('2019','Piccardo and North, The Action Oriented Approach','https://channelviewpublications.wordpress.com/2019/07/31/what-is-the-action-oriented-approach-to-language-education/'),
 ('DITALS','Università per Stranieri di Siena','https://ditals.unistrasi.it/'),('CILS','Certificazione di Italiano come Lingua Straniera','https://cils.unistrasi.it/')]),m)
m.select_one('.s5-disc').string='Club Italia is independent and is not affiliated with or endorsed by the Università per Stranieri di Siena. DITALS refers to the individual qualifications held by our teachers. CILS and CELI preparation is offered; examinations are taken at accredited centres.'
# ---------- culture pillars
c=byc('culture-dark')
c.select_one('h2').clear(); c.select_one('h2').append(F('Culture speaks Italian.<br><span class="gold-ital">What about you?</span>'))
c.select_one('p.lede').string='Six pillars of Italian life run through every course, taught by people who live them.'
PIL=[('ag-medieval-aerial','Arte e architettura','From the Roman forum to the Renaissance dome.'),('ag-wine-bottles','Cucina e vino','A Bolognese market, a Neapolitan oven, a Tuscan cellar.'),('ag-venice-gondola','Viaggio','From the canals of Venice to the Amalfi coast.'),('ag-luxury-car','Moda e cinema','Milanese tailoring, Roman cinema, la bella figura.'),('opera-scala','Musica e opera','Verdi, Puccini and Rossini, in the language they wrote in.'),('ag-tradition-festival','Tradizione','Carnevale, the Palio and the feast days of each city.')]
for i,(p_,(v,t,d)) in enumerate(zip(c.select('a.pillar'),PIL)):
    p_['href']='culture.html'; vv=p_.select_one('video'); vv['poster']=f'assets/img/{v}-poster.jpg'; vv.source['src']=f'assets/video/{v}.mp4'
    p_.select_one('.pillar-title').string=t; p_.select_one('.pillar-desc').string=d
# ---------- presented by eTeacher (ac-power)
ap=byc('ac-power')
lg=ap.select_one('img.ac-power-logo'); lg['src']='assets/img/eteacher-real-logo-white.png'; lg['alt']='eTeacher Group'; del lg['width']; del lg['height']
ap.select_one('.ac-power-eyebrow').clear(); ap.select_one('.ac-power-eyebrow').append(F('Presented by <span>eTeacher Group</span>'))
ap.select_one('h2').clear(); ap.select_one('h2').append(F('Twenty years of <em>live</em> language teaching.'))
for f_,(n_,s_,l_) in zip(ap.select('.apf'),[('1','M+','Learners taught'),('20','+','Years of live teaching'),('190','+','Countries reached')]):
    num=f_.select_one('.apf-num'); num['data-count']=n_; num['data-suffix']=s_; num.string=n_+s_; f_.select_one('.apf-lab').string=l_
ap.select_one('.ac-power-marquee').decompose()
# ---------- faculty
fsec=[x for x in secs if x.select_one('.fac-gallery')][0]
fsec.select_one('p.eyebrow').string='Meet our faculty'
fsec.select_one('h2').clear(); fsec.select_one('h2').append(F('Native teachers, from every corner of <span class="gold-ital">Italy</span>'))
fsec.select_one('p.lede').string='Rome, Florence, Bologna, Venice, Milan, Naples and Palermo. Each teacher holds the DITALS certification in teaching Italian as a foreign language.'
swap(fsec.select_one('.tctr-badges'),'<p class="ci-facts reveal reveal-d1">DITALS II certified &nbsp;·&nbsp; Live from Italy &nbsp;·&nbsp; Groups of ten to twelve &nbsp;·&nbsp; Seven cities</p>')
g=fsec.select_one('.fac-gallery'); tm=str(g.select_one('a.fac-card'))
for x in g.select('a.fac-card'): x.decompose()
for t_,(n_,ct) in TN.items():
    a=F(tm).a; a['class']=['fac-card']; a['href']=f'pages/teachers/{t_}.html'
    im=a.img; im['src']=f'assets/img/teacher-{t_}.jpg'; im['alt']=f'{n_}, Italian teacher from {ct}'
    a.select_one('.fac-name').string=n_.split()[0]; a.select_one('.fac-region').string=ct; g.append(a)
a=fsec.select_one('a.btn'); a.string='Meet the full faculty'; a['href']='teachers.html'
# ---------- taste -> inside a lesson
ts=[x for x in secs if x.select_one('.taste-grid')][0]
ts.select_one('p.eyebrow').string='Inside a live lesson'
ts.select_one('h2').clear(); ts.select_one('h2').append(F('A real classroom, <span class="gold-ital">live from Italy</span>'))
ts.select_one('p.lede').string='Your teacher is in Rome or Venice. You are at home. Twelve adults, eighty five minutes, and everyone speaks.'
for card,(v,l,w) in zip(ts.select('.taste-card'),[('class-demo','Every lesson is live, never pre-recorded.','A lesson in progress · Club Italia classroom'),('ag-zoom-student','Recordings stay with you for review.','Between lessons · at home')]):
    vv=card.video; vv['poster']=f'assets/img/{v}-poster.jpg'; vv.source['src']=f'assets/video/{v}.mp4'
    b_=card.select_one('.sound-toggle'); b_ and b_.decompose()
    card.select_one('.taste-line').string=l; card.select_one('.taste-who').string=w
a=ts.select_one('a.btn'); a.string='How classes work'; a['href']='how-it-works.html'
# ---------- map
mp=S.select_one('#mapstr'); mp['aria-label']='Interactive map of Italy'
# ---------- Biagio
jb=S.select_one('#julien-fold'); jb['id']='biagio-fold'
v=jb.select_one('video.jul-paris-video'); v['poster']='assets/img/ag-rome-basilica-poster.jpg'; v.source['src']='assets/video/ag-rome-basilica.mp4'
w=jb.select_one('.jul-cutout-wrap'); w.clear()
w.append(F('<span class="jul-cutout-badge"><span class="jul-cutout-dot"></span> Biagio · AI tutor</span><img class="jul-cutout" id="jul-home-video" src="assets/img/biagio-3d-hero.png" alt="Biagio, the Club Italia AI tutor" width="1024" height="1536"><audio id="jul-home-audio" preload="none" src="assets/audio/biagio-intro.mp3"></audio><button class="jul-home-sound" id="ci-bia-btn" type="button" aria-pressed="false"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 9v6h4l5 4V5L8 9H4z"/><path d="M16 9a4 4 0 0 1 0 6"/></svg><span class="jhs-label">Hear Biagio</span></button>'))
for sc in jb.find_all('script'): sc.decompose()
tx=jb.select_one('.jul-home-text')
tx.select_one('p.eyebrow').string='Practice between classes'
tx.select_one('h2').clear(); tx.select_one('h2').append(F('Meet <span class="gold-ital">Biagio</span>, your Italian coach at any hour'))
tx.select_one('p.lede').string='Between live lessons, Biagio works inside the platform on exactly what your teacher covered that week.'
for li,t_ in zip(tx.select('li'),['Pronunciation, sound by sound','Patient, immediate corrections','Conversation practice on demand','Available day and night, always in Italian']):
    sv=li.svg; li.clear(); sv and li.append(sv); li.append(' '+t_)
a=tx.select_one('a.btn'); a.string='Discover Biagio'; a['href']='biagio.html'
# ---------- testimonials
tf=byc('tst-fold')
tt=tf.select_one('.tst-trust'); tt and tt.decompose()
tf.select_one('h2').clear(); tf.select_one('h2').append(F('Learner stories, <span class="gold-ital">real progress.</span>'))
tf.select_one('.tst-head p').string='What adults say after a level with Club Italia.'
tr=tf.select_one('.tst-track'); tr.clear()
QQ=QS+[(n,r,q) for (_,n,r,q) in [(a_,b_,c_,d_) for a_,b_,c_,d_ in TS]][:2] if 'TS' in dir() else QS
PH={'Diane Weller':'student-diane.jpg','Robert Hensley':'student-robert.jpg','Sarah Kim':'student-sarah.jpg'}
for n_,r_,q_ in QS[:3]:
    tr.append(F(f'<article class="tst-card ci-q"><div class="ci-q-top"><img src="assets/img/{PH.get(n_,"student-sarah.jpg")}" alt="{E(n_)}" loading="lazy"></div><p class="ci-q-who">{E(n_)}</p><p class="ci-q-ctx">{E(r_)}</p><blockquote>«{E(q_)}»</blockquote></article>'))
tf.select_one('.tst-source').string='Learner placeholders for the presentation.'
tf.select_one('.tst-source').insert_before(F('<!-- TODO: replace with real, verified learner reviews -->'))
# ---------- platform etg2
e2=byc('etg2-section')
im=e2.select_one('img.etg2-brand-logo'); im['src']='assets/img/eteacher-real-logo-white.png'; im['alt']='eTeacher Group'
e2.select_one('h2').string='One learning platform, built by eTeacher Group'
e2.select_one('p.lede').string='Club Italia runs on the live teaching platform eTeacher Group has refined for over twenty years.'
e2.select_one('.etg2-trust').decompose()
PL=[('Live HD lessons','Eighty five minute live lessons with a native teacher, broadcast from an Italian city.','Live from Italy'),('The learning platform','Schedule, lessons, worksheets and progress in one place.','Dashboard'),('Lesson recordings','Every live lesson is recorded for review.','Always available'),('Biagio AI tutor','Pronunciation drills and conversation practice between lessons.','Day and night'),('CEFR progress','Can-do checkpoints in every unit, a certificate at the end of each level.','A0 to B1'),('Small live groups','Ten to twelve learners per class, so everyone speaks.','Ten to twelve'),('Placement','A conversation with an advisor before you enrol, to find your level.','Free')]
for card,(h_,p__,t_) in zip(e2.select('article.etg3-card'),PL):
    card.h3.string=h_; card.p.string=p__; card.select_one('.etg3-pill').string=t_
e2.select_one('.etg2-foot').string='Live lessons, recordings, practice and progress, in one home.'
# ---------- lead magnet
lm=byc('lead-magnet')
lm.select_one('.lm-cover-badge').string='Free · five minutes'
im=lm.select_one('.lm-cover img'); im['src']='assets/img/life-amalfi-coast.jpg'; im['alt']='The Amalfi coast at golden hour'
lm.select_one('.lm-eyebrow').string='Find your level'
lm.select_one('h2').clear(); lm.select_one('h2').append(F('Which Italian course is <em>right for you?</em>'))
lm.select_one('.lm-body > p:not(.eyebrow)').clear(); lm.select_one('.lm-body > p:not(.eyebrow)').append(F('A short placement conversation finds your CEFR level and the right course, from your first <em>buongiorno</em> to confident conversation.'))
for s_,t_ in zip(lm.select('.lm-meta span'),['CEFR aligned','A personal recommendation','No commitment']): s_.string=t_
b_=lm.select_one('.lm-actions button'); sv=b_.svg; b_.clear(); b_.append('Find my Italian level '); sv and b_.append(sv)
a=lm.select_one('.lm-actions a'); sv=a.svg; a.clear(); a.append('Talk to an advisor instead '); sv and a.append(sv)
# ---------- consultation
lgf=byc('lg-fold')
lgf.select_one('.lg-eyebrow').string='Begin your journey'
lgf.select_one('#lg-title').clear(); lgf.select_one('#lg-title').append(F('Request your personal <span class="gold-ital">enrolment consultation.</span>'))
lgf.select_one('.lg-lede').string='Tell us your goals. An advisor will reply personally with your level, the right course and a start date.'
for it,t_ in zip(lgf.select('.lg-trust-item'),['A real conversation, never a sales script','Plan options and a recommended start date','A reply within one working day']):
    sv=it.svg; it.clear(); sv and it.append(sv); it.append(t_)
for i_ in lgf.select('input[placeholder]'):
    i_['placeholder']={'Marie':'Giulia','Laurent':'Rossi'}.get(i_['placeholder'],i_['placeholder'].replace('French','Italian'))
from bs4 import Comment
for c_ in S.find_all(string=lambda x:isinstance(x,Comment)): c_.extract()
for t in lgf.find_all(string=re.compile('French|France|Acadomia|Atelier|Merci')): t.replace_with(t.replace('French','Italian').replace('France','Italy').replace('Acadomia','eTeacher Group').replace('The Italian Atelier','Club Italia').replace('French Atelier','Club Italia').replace('Merci.','Grazie.'))
# ---------- FAQ
fq=[x for x in secs if x.select_one('.faq-list')][0]
fq.select_one('p.eyebrow').string='Your questions, answered'
FQ=[('Are the classes live or pre-recorded?','Every class is live, taught by a native teacher in Italy. Recordings are there for review, never as a substitute.'),('How big are the groups?','Ten to twelve adults, so everyone speaks in every lesson.'),('What does a level include?','Twenty live lessons of 85 minutes, about 28 contact hours, with the syllabus, recordings, Biagio and a certificate of completion.'),('Who teaches the classes?','Native Italian teachers living in Italy, each holding the DITALS certification for teaching Italian as a foreign language.'),('Do you prepare for CILS and CELI?','Yes. The upper levels include preparation for the CILS and CELI examinations. The examinations themselves are taken at accredited centres.'),('How much does it cost?','From $62 a week on the annual plan. Monthly and term plans are also available.')]
for it,(q_,a_) in zip(fq.select('.faq-item'),FQ):
    sp=it.select_one('.faq-btn > span'); sp.clear(); sp.append(F(f'<span class="faq-num">{FQ.index((q_,a_))+1:02d}.</span>{E(q_)}')); it.select_one('.faq-body p').string=a_
a=fq.select_one('a.btn'); a.string='See all questions'; a['href']='faq.html'
# ---------- CTA band
cb=byc('cta-band')
cb.select_one('h2').clear(); cb.select_one('h2').append(F('Culture speaks Italian.<br><span class="gold-ital">What about you?</span>'))
cb.select_one('p.lede').string='Join a live class broadcasting from Italy and begin with your first lesson.'
a=cb.select_one('a.btn'); a.string='Begin your journey'
# ---------- footer
ft=S.select_one('footer.site-footer')
fb=ft.select_one('.footer-brand'); fb.clear(); fb.append(F(LOCK.replace('ci-lock','ci-lock ci-lock-ft')+'<p>Italian, taught live from Italy. A school of eTeacher Group, for adults who want the language and the culture together.</p>'))
cols=ft.select('.footer-col')
FC=[('Courses',[(CO[k][2],CO[k][1]) for k in ['ci1','ci2','ci3','ci4']]+[('map.html','Map of Italy')]),('Learn',[('method.html','Our method'),('how-it-works.html','How it works'),('biagio.html','Biagio AI tutor'),('teachers.html','Our teachers'),('culture.html','Italian culture'),('curriculum.html','Curriculum')]),('About',[('about.html','About'),('pricing.html','Pricing'),('faq.html','FAQ'),('contact.html','Contact'),('certifications.html','Certifications')])]
for col,(h_,ls) in zip(cols,FC):
    col.clear(); col.append(F(f'<h4>{h_}</h4>'+''.join(f'<a href="{u}">{E(t)}</a>' for u,t in ls)))
fbm=ft.select_one('.footer-bottom'); fbm.clear(); fbm.append(F('<p>advisor@eTeacherGroup.com</p>'))
for p_ in ft.find_all('p'):
    if 'Copyright' in p_.text: p_.string='© 2026 eTeacher Group. Club Italia is a school of eTeacher Group. Footage licensed via Artgrid.'
# ---------- advisor modal + console
md=S.select_one('.advisor-modal')
for t in md.find_all(string=re.compile('French|France|Atelier|Merci|Acadomia')): t.replace_with(t.replace('Merci !','Grazie.').replace('The French Atelier','Club Italia').replace('French Atelier','Club Italia').replace('French','Italian').replace('France','Italy').replace('Acadomia','eTeacher Group'))
md.select_one('.eyebrow').string='Speak with us'
ec=S.select_one('aside.enroll-console'); ec['aria-label']='Enrol in Club Italia'
ec.select_one('.ec-eyebrow').string='Open enrolment'; ec.select_one('.ec-title').string='Reserve your seat, live from Italy'; ec.select_one('.ec-cta').string='Enrol now'
# ---------- local scripts
S.body.append(F('<!-- TODO: replace learner placeholders with verified reviews; confirm Trustpilot-free hero; confirm eTeacher figures 1M+/20+/190+ -->'))
S.body.append(F('''<script>
(function(){var b=document.getElementById('ci-bia-btn'),a=document.getElementById('jul-home-audio');if(b&&a){b.onclick=function(){if(a.paused){a.play();b.setAttribute('aria-pressed','true');b.querySelector('.jhs-label').textContent='Pause'}else{a.pause();b.setAttribute('aria-pressed','false');b.querySelector('.jhs-label').textContent='Hear Biagio'}};a.onended=function(){b.setAttribute('aria-pressed','false');b.querySelector('.jhs-label').textContent='Hear Biagio'}}
document.querySelectorAll('form').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();var s=f.parentNode.querySelector('.lg-success,.advisor-success');if(s){f.style.display='none';s.style.display='block';s.classList.add('show','is-visible')}})});})();
</script>'''))
out=str(S).replace('assets/gen/hero-original.webp','assets/img/ag-roma-statue-poster.jpg').replace('assets/gen/hero-paris.webp','assets/img/life-amalfi-coast.jpg')
# global clean: dashes, leftover brand words
out=re.sub(r'Merci\W*!','Grazie.',out).replace(' — ',', ').replace('—',', ').replace('–',' to ')
open('index.html','w').write(out)
left=[m for m in re.findall(r'[^<>]{0,40}(?:French|France|Acadomia|Atelier|Julien|Paris)[^<>]{0,40}',BeautifulSoup(out,'html.parser').get_text(' '))]
print('leftovers',len(left),left[:15])
