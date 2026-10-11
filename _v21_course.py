import re,json,html as H
from bs4 import BeautifulSoup, Comment
exec(open('_v20_build.py').read().split("home=head(")[0])
exec(open('_v20_build.py').read().split("# ===== course template")[1].split("for k in ORDER:")[0])
def F(h): return BeautifulSoup(h,'html.parser')
P='../../'
def build(k):
    S=BeautifulSoup(open('/workspace/faport/courses/fa-beginner.html').read(),'html.parser')
    hi=BeautifulSoup(open('index.html').read(),'html.parser')
    t,n,u,img,te,hv,st,tu=CO[k]; d=D[k]; tn,city=TN[te]; L=lv(k); a_,b_=L.split(' to ') if ' to ' in L else (L,L)
    S.title.string=f'{n} · {L} · Club Italia by eTeacher'
    md=S.find('meta',attrs={'name':'description'}); md and md.__setitem__('content',f'{n}: twenty live Italian lessons, CEFR {L}, taught from {city} by {tn}.')
    for m in S.find_all('meta',attrs={'http-equiv':True}): m.decompose()
    for l in S.find_all('link',href=True):
        h=l['href']
        if h.startswith('../css/'): l['href']=P+'fa/css/'+h[7:].split('?')[0]
        if 'favicon' in h or 'fonts.googleapis.com/css2' in h: l.decompose()
    S.head.append(F(f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Inter:wght@300;400;500;600;700&display=swap"><link rel="stylesheet" href="{P}fa/css/ci.css"><link rel="stylesheet" href="{P}fa/css/ci-light.css">'))
    for sc in S.find_all('script'):
        s=sc.get('src','')
        if 'eteacher-leads' in s or 'serviceWorker' in (sc.string or '') or 'CRM' in (sc.string or ''): sc.decompose(); continue
        if s.startswith('../js/'): sc['src']=P+'fa/js/'+s[6:].split('?')[0]
    for c_ in S.find_all(string=lambda x:isinstance(x,Comment)): c_.extract()
    # header, drawer, footer, modal, console from our ported home (rebase links)
    def rebase(e):
        for a in e.find_all(['a','img','source','audio','video']):
            for at in ['href','src','poster']:
                v=a.get(at)
                if v and not re.match(r'(https?:|mailto:|#|/)',v): a[at]=P+v
        return e
    for sel in ['header.site-header','div.nav-drawer','footer.site-footer','div.advisor-modal','aside.enroll-console']:
        o=S.select_one(sel); nw=hi.select_one(sel)
        if o and nw: o.replace_with(rebase(F(str(nw))))
    S.body['data-course']=k; S.body['id']='ci'
    secs=S.body.find_all('section',recursive=False)
    # hero
    h=secs[0]; v=h.select_one('.hero-media video'); v['poster']=f'{P}assets/img/{hv}-poster.jpg'; v.source['src']=f'{P}assets/video/{hv}.mp4'
    bd=h.select_one('.hero-badges'); bd.clear(); bd.append(F(f'<span class="h-badge lvl">CEFR {L}</span><span class="h-badge"><span class="live-dot"></span>Live from {city}</span><span class="h-badge">DITALS certified teacher</span><span class="h-badge">Biagio · AI tutor</span>'))
    h.h1.clear(); h.h1.append(F(f'{E(n.replace("CI ",""))}. <span class="gold-ital">Italian begins in {city}.</span>' if k=='ci1' else f'{E(n)} <span class="gold-ital">in {city}</span>'))
    h.select_one('.hero-sub').string=cl(d['promise'])
    cs=h.select('.hero-ctas a'); cs[0].string='Enrol now'; cs[0]['href']=P+'pricing.html'; cs[1].string='Explore the 20 units'
    for hm,(kk,vv) in zip(h.select('.hm'),[('Format','20 live lessons · 85 min'),('Contact hours','28 h 20 live'),('Live groups','10 to 12 learners'),('Certificate','CEFR '+b_)]):
        hm.select_one('.hm-k').string=kk; hm.select_one('.hm-v').string=vv
    # DNA
    s1=secs[1]; s1.select_one('.eyebrow').string='The structure of this course'
    s1.h2.string='Where the language begins: sound, words, first exchanges'
    s1.select_one('.sec-head p').string=f'{n} takes a true beginner from A0 to {b_}. {CEFRD.get(b_,CEFRD.get("A1"))}'
    DNA=[('Hear it first','The sound system of Italian, open vowels and double consonants, from the first lesson.'),('Rome as the classroom','Each unit is set in a real Roman place, from Fiumicino to a bar in Prati.'),('Live small groups','Every unit is an 85 minute live class of ten to twelve, with constant speaking practice.'),(f'Documented to {b_}','Can-do checkpoints through the course and a certificate stating your CEFR level.')]
    for c,(t1,t2) in zip(s1.select('.pillar-card'),DNA): c.h3.string=t1; c.p.string=t2
    # learn
    s2=secs[2]; s2.select_one('.eyebrow').string='Learning outcomes'; s2.h2.string='By unit 20, you will be able to'
    s2.select_one('.sec-head p').string='Can-do statements aligned with the CEFR descriptors for '+b_+'.'
    ul=s2.select_one('ul.learn-list'); tick=str(ul.select_one('.tick')); ul.clear()
    ul.append(F(''.join(f'<li>{tick}<span>{E(cl(o))}</span></li>' for o in d['outcomes'])))
    for it,im_ in zip(s2.select('.img-trio img'),['city-roma.jpg','life-caffe-roma.jpg','course-ci1.jpg']):
        im_ = im_ if k=='ci1' else img
        it['src']=P+'assets/img/'+im_; it['alt']='Rome, the setting of '+n
    # region band
    rb=secs[3]; v=rb.video; v['poster']=f'{P}assets/img/ag-roma-statue-poster.jpg'; v.source['src']=f'{P}assets/video/ag-roma-statue.mp4'
    rb.select_one('.eyebrow').string=f'Filmed in {city}'; rb.h2.string='From Fiumicino to the seven hills'
    rb.p.string='The course is a journey through Rome. Arrival, the bar, the market, the piazza, the trattoria: your Italian grows with every stop.'
    # syllabus
    sy=secs[4]; sy.select_one('.eyebrow').string='The full syllabus'; sy.h2.string='Twenty units, one city'
    sy.select_one('.sec-head p').string=f'A structured {L} syllabus. Each 85 minute live unit pairs one communicative goal with the grammar and vocabulary it needs.'
    g=sy.select_one('.unit-grid'); g.clear()
    g.append(F(''.join(f'<div class="unit-card" data-reveal><div class="u-no">{i+1:02d}</div><div class="u-body"><h4>{E(cl(a))}</h4><p>{E(cl(b))}</p></div></div>' for i,(a,b) in enumerate(d['syllabus']))))
    # assessment block (added, FA vocabulary)
    asm=F(f'''<section class="sec bg-beige-grad"><div class="cw"><div class="sec-head" data-reveal><span class="eyebrow eyebrow-line">Hours, assessment and certificate</span><h2>Stated plainly, before you enrol</h2><hr class="gold-rule"></div>
<div class="pillar-grid">{''.join(f'<div class="pillar-card glass" data-reveal><div class="p-num">{i+1:02d}</div><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate([('Contact hours','Twenty live lessons of 85 minutes: 28 hours 20 minutes of teaching, plus recordings and Biagio practice.'),('Prerequisite',PRE[k]),('Assessment','Feedback in every lesson, a progress check at unit 10, and a final spoken and written task in unit 20.'),('Certificate',f'A certificate of completion stating CEFR {b_}, issued by Club Italia.')]))}</div>
<!-- TODO(owner): confirm assessment points and certificate wording --></div></section>''')
    sy.insert_after(asm)
    # teacher
    tb=[x for x in secs if x.select_one('.teacher-block')][0]
    im=tb.select_one('.teacher-photo img'); im['src']=f'{P}assets/img/teacher-{te}.jpg'; im['alt']=f'{tn}, Italian teacher from {city}'
    tb.select_one('.tp-badge').string=city
    tb.select_one('.teacher-info .eyebrow').string='Your teacher'; tb.h3.string=tn
    tb.select_one('.ti-role').string=' · '.join(x.strip() for x in T[te]['cred'])
    tb.select_one('.teacher-info p').string=T[te]['bio'].split('. ')[0]+'. '+T[te]['bio'].split('. ')[1]+'.'
    q=T[te]['quote'].split('. ');tb.select_one('.teacher-quote').string='«'+'. '.join(q[:2])+'.»'
    # acadomia band -> eTeacher
    ab=[x for x in secs if 'acadomia-band' in (x.get('class') or [])][0]
    ab.select_one('.eyebrow').string='Presented by eTeacher Group'; ab.h2.string='Twenty years of live language teaching'
    ab.select_one('.sec-head p').string='The teaching platform of eTeacher Group, with native teachers broadcasting live from Italy.'
    for c,(nn,sf,lb) in zip(ab.select('.counter-card'),[('1','M+','Learners taught'),('20','+','Years of live teaching'),('190','+','Countries reached')]):
        x=c.select_one('.c-num'); x['data-count']=nn; x['data-suffix']=sf; x.attrs.pop('data-prefix',None); x.string=nn+sf; c.select_one('.c-label').string=lb
    ps=ab.select_one('.power-strip'); ps and ps.decompose()
    # pricing
    pr=S.select_one('#pricing'); pr.select_one('.eyebrow').string='Tuition'; pr.h2.string='One curriculum. A plan for your rhythm.'
    pr.select_one('.sec-head p').string=f'Every plan includes the live lessons from {city}, recordings, Biagio and your certificate.'
    pc=pr.select('.price-card')
    pc[0].select_one('.pc-tag').string='Annual · best value'; pc[0].select_one('.pc-amt').contents[0].replace_with('$62')
    pc[0].select_one('.pc-sub').string=f'$3,224 billed yearly · full {n} programme'
    tk=str(pc[0].select_one('.tick'))
    def lis(card,items): ul=card.ul; ul.clear(); ul.append(F(''.join(f'<li>{tk}<span>{E(i)}</span></li>' for i in items)))
    lis(pc[0],['20 live lessons · 85 minutes each','Small live groups of 10 to 12','Every lesson recorded for review','Certificate of completion, CEFR '+b_,'Biagio, your AI tutor at any hour'])
    pc[0].select_one('a').string='Enrol now'; pc[0].select_one('a')['href']=P+'pricing.html'
    pc[1].select_one('.pc-tag').string='Monthly · flexible'; pc[1].select_one('.pc-amt').contents[0].replace_with('$84'); pc[1].select_one('.pc-sub').string='Billed $336 a month · cancel any time'
    lis(pc[1],['Pay month to month','The same live small group classes','Recordings and Biagio included','Switch to annual at any time'])
    pc[1].select_one('a').string='Start monthly'; pc[1].select_one('a')['href']=P+'pricing.html'
    dc=pr.select_one('.disclaimer'); dc.string='Club Italia is independent and is not affiliated with or endorsed by the Università per Stranieri di Siena. DITALS refers to the qualification held by the teacher.'
    # faq
    fq=[x for x in secs if x.select_one('.faq-list')][0]; fq.select_one('.eyebrow').string='Questions'; fq.h2.string='Everything you might be wondering'
    QA=[(f'Is {n} right for me?','Yes, if you are starting from zero or know only a few words. The course assumes no Italian.'),('How big are the groups?','Ten to twelve adults per live class, so you speak in every lesson.'),('How many hours is the course?','Twenty live lessons of 85 minutes: 28 hours 20 minutes of contact time.'),('Will I get a certificate?',f'Yes. A certificate of completion stating CEFR {b_}.'),('What comes next?',f'{CO["ci2"][1]}, taught from Florence by {TN["chiara"][0]}.')]
    for it,(qq,aa) in zip(fq.select('.faq-item'),QA): it.select_one('.faq-q span').string=qq; it.select_one('.faq-a-inner').string=aa
    # siblings
    sb=S.select_one('.sibling-nav'); sb.clear()
    sb.append(F(f'<a class="sib-card glass-light" href="{P}courses.html"><span class="sib-dir">All courses</span><span class="sib-title">The full collection</span><span class="sib-cefr">Il Corso and Parliamo</span></a><a class="sib-card glass-light" href="ci2.html"><span class="sib-dir">Next level</span><span class="sib-title">{CO["ci2"][1]}</span><span class="sib-cefr">{lv("ci2")} · Firenze</span></a>'))
    fc=S.select_one('.final-cta'); fc.select_one('.eyebrow').string='Live Italian, from Italy'
    fc.h2.clear(); fc.h2.append(F('Say your first <span class="gold-ital">buongiorno</span>.'))
    fc.p.string=f'Twenty live lessons in {city}, with {tn.split()[0]}. Join a small group and begin.'
    a=fc.select('a'); a[0].string='Enrol now'; a[0]['href']=P+'pricing.html'; a[1].string='See how it works'; a[1]['href']=P+'how-it-works.html'
    out=str(S).replace('../assets/',P+'assets/') if False else str(S)
    out=re.sub(r'Merci\W*!','Grazie.',out).replace(' — ',', ').replace('—',', ').replace('–',' to ').replace('→',' to ')
    out=out.replace('View course  to ','View course →')
    open(f'pages/courses/{k}.html','w').write(out)
    left=re.findall(r'[^<>]{0,40}(?:French|France|Acadomia|Atelier|Julien|Paris|Normandy)[^<>]{0,40}',BeautifulSoup(out,'html.parser').get_text(' '))
    print(k,'leftovers',left[:8])
build('ci1')
