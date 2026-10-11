import re,os,glob,html
from bs4 import BeautifulSoup
exec(open("_v18_pages.py").read().split("# ---------- courses")[0])
VID={'about':'ag-rome-basilica','blog':'ag-chefs-street','community':'ag-tradition-festival','contact':'ag-venice-docked','culture':'ag-medieval-aerial','eteacher':'ag-zoom-student','events':'ag-tradition-festival','sample-class':'ag-zoom-student','privacy':'ag-cypress-road','terms':'ag-cypress-road',
'pillar-art':'ag-medieval-aerial','pillar-cinema':'ag-catania-statues','pillar-food':'ag-chefs-street','pillar-opera':'ag-rome-basilica','pillar-tradition':'ag-tradition-festival','pillar-travel':'ag-venice-gondola',
'carnevale':'ag-venice-gondola','festa-repubblica':'ag-rome-basilica','palio-siena':'ag-san-gimignano','marco':'ag-roma-statue','chiara':'firenze-arno','giulia':'bologna-portici','alessandro':'opera-scala','francesca':'ag-venice-gondola','luca':'napoli-mare','sofia':'ag-catania-statues'}
BLOGV=['ag-market-produce','ag-pizza-toppings','ag-wine-bottles','ag-camogli-coast','ag-tuscany-drone','ag-traveler-man']
files=['about.html','blog.html','community.html','contact.html','culture.html','eteacher.html','events.html','sample-class.html','privacy.html','terms.html']+sorted(glob.glob('pages/blog/*.html')+glob.glob('pages/culture/pillar-*.html')+glob.glob('pages/events/*.html')+glob.glob('pages/teachers/*.html'))
for i,f in enumerate(files):
    src=open(f).read();s=BeautifulSoup(src,'html.parser');depth=f.count('/');Pp='../'*depth
    name=os.path.basename(f)[:-5];vid=VID.get(name,BLOGV[i%len(BLOGV)])
    styles=''.join(str(x) for x in s.head.find_all('style'))+''.join(str(x) for x in s.head.find_all('link',rel='stylesheet') if 'fonts.googleapis' not in x.get('href','') and 'home17' not in x.get('href','') and 'v18' not in x.get('href',''))
    title=s.title.get_text(strip=True) if s.title else 'Club Italia';desc=(s.find('meta',attrs={'name':'description'}) or {}).get('content','') if s.find('meta',attrs={'name':'description'}) else ''
    body=s.find('main') or s.body
    for x in body.find_all(['header','footer','nav','script']): x.decompose()
    for x in body.select('.curtain,.skip,.cur,.cur-r'): x.decompose()
    h1=body.find('h1');h1t=h1.get_text(' ',strip=True) if h1 else title.split('·')[0]
    # remove the first hero-like block containing the h1
    lede=''
    if h1:
        blk=h1
        while blk.parent and blk.parent is not body and blk.parent.name not in ('main','body'): blk=blk.parent
        p=blk.find('p');lede=p.get_text(' ',strip=True) if p else ''
        eb=blk.find(class_=re.compile('eyebrow|eb|kicker'));ebt=eb.get_text(' ',strip=True) if eb else 'Club Italia'
        blk.decompose()
    else: ebt='Club Italia'
    parts=h1t.split('. ',1) if '. ' in h1t else (h1t.rsplit(' ',2)[0], ' '.join(h1t.split()[-2:])) if len(h1t.split())>3 else (h1t,'')
    a,b=parts[0],parts[1]
    if not a.endswith('.') and '. ' in h1t: a+='.'
    inner=''.join(str(c) for c in body.contents)
    hd=head(title,desc,Pp).replace('</head>',styles+'</head>',1)
    # old styles must come before v18: move them
    hd=hd.replace(f'<link rel="stylesheet" href="{Pp}css/home17.css">',styles+f'<link rel="stylesheet" href="{Pp}css/home17.css">',1).replace(styles+'</head>','</head>',1)
    hr=f'''<section class="ch">{V(vid,Pp)}<div class="tint"></div><div class="w"><div class="glass"><div class="crumbs"><a href="{Pp}index.html">Club Italia</a> / {E(ebt)}</div><h1 data-split>{E(a)} <em>{E(b)}</em></h1>{f'<p class="lede">{E(lede)}</p>' if lede else ''}<div style="display:flex;gap:.8rem;flex-wrap:wrap;margin-top:1.4rem"><a class="btn btn-gold" href="{Pp}index.html#enrol">Enrol now</a><a class="btn btn-line" href="{Pp}courses.html">See the courses</a></div></div></div></section>'''
    out=hd+hr+f'<div class="legacy">{inner}</div>'+BAND('Culture speaks Italian.','What about you?','Join a live class broadcasting from Italy.').replace('href="index.html','href="'+Pp+'index.html').replace('assets/',Pp+'assets/')+foot(Pp)
    open(f,'w').write(fix(out))
print(len(files),'reskinned')
