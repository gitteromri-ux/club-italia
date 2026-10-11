import re,glob,os
from bs4 import BeautifulSoup
exec(open('_v19_build.py').read().replace("open('index.html','w').write(home)","").replace("    open(u,'w').write(pg)","    pass"))
SKIP={'index.html'}|{CO[k][2] for k in ORDER}
files=[f for f in glob.glob('*.html')+glob.glob('pages/*/*.html') if f not in SKIP]
VID={'about':'ag-rome-basilica','blog':'ag-chefs-street','community':'ag-tradition-festival','contact':'ag-venice-docked','culture':'ag-medieval-aerial','eteacher':'ag-zoom-student','events':'ag-tradition-festival','sample-class':'class-demo','privacy':'ag-cypress-road','terms':'ag-cypress-road','courses':'ag-tuscany-drone','curriculum':'ag-medieval-aerial','method':'ag-camogli-coast','certifications':'ag-san-gimignano','teachers':'ag-traveler-woman','biagio':'ag-roma-statue','pricing':'ag-wine-bottles','faq':'ag-venice-docked','map':'ag-tuscany-drone','how-it-works':'ag-zoom-student','capsules':'ag-pizza-oven',
'pillar-art':'ag-medieval-aerial','pillar-cinema':'ag-catania-statues','pillar-food':'ag-chefs-street','pillar-opera':'ag-rome-basilica','pillar-tradition':'ag-tradition-festival','pillar-travel':'ag-venice-gondola','carnevale':'ag-venice-gondola','festa-repubblica':'ag-rome-basilica','palio-siena':'ag-san-gimignano'}
VID.update(FACV)
ROTF=['ag-tuscany-drone','ag-camogli-coast','ag-san-gimignano','ag-venice-docked','ag-cypress-road','ag-medieval-aerial','ag-wine-bottles','ag-market-produce','ag-rome-basilica','firenze-arno','bologna-portici','napoli-mare']
ROT=['ag-market-produce','ag-pizza-toppings','ag-wine-bottles','ag-camogli-coast','ag-tuscany-drone','ag-traveler-man','ag-cypress-road']
EMO=re.compile('[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u2190-\u21FF\u2605\u2606\u2713\u2714\u25B6\u266A\u266B\u275A]')
def clean_text(t):
    t=re.sub(r'FOLD \d+ ·[^\n]*','',t)
    t=re.sub(r'\b([A-Z]{3,}(?:\s+[A-Z]{3,})+)\b',lambda m:m.group(1) if all(w in ('CILS','CELI','PLIDA','CEFR','DITALS','CEDILS') for w in m.group(1).split()) else m.group(1).title(),t)
    t=re.sub(r'(\d)\s*[–—]\s*(\d)',r'\1 to \2',t);t=re.sub(r'\s*[—–]\s*',', ',t);t=re.sub(r'\s+-\s+',', ',t);t=t.replace(' -- ',', ');t=EMO.sub('',t);return t
BAD=re.compile(r'\b(chip|badge|pill|eyebrow|eyebrow-line|eb|tag|tag-script|lvk|code|k|stars|tp2|hero-badges)\b')
for i,f in enumerate(files):
    src=open(f).read();s=BeautifulSoup(src,'html.parser');depth=f.count('/');P='../'*depth;name=os.path.basename(f)[:-5]
    v_=VID.get(name,ROT[i%len(ROT)])
    oldcss=''.join(str(x) for x in s.head.find_all('style'))+''.join(f'<link rel="stylesheet" href="{x["href"]}">' for x in s.head.find_all('link',rel='stylesheet') if 'fonts.' not in x.get('href','') and 'v19' not in x.get('href',''))
    title=s.title.get_text(strip=True) if s.title else 'Club Italia';md=s.find('meta',attrs={'name':'description'});desc=md.get('content','') if md else ''
    body=s.find('main') or s.body
    for x in body.find_all(['header','footer','nav','script']):
        if x.name=='script' and x.get('type')=='application/json': continue
        x.decompose()
    for x in body.find_all('aside'):
        if x.find('button',attrs={'data-advisor':True}) or len(x.find_all('a'))>6: x.decompose()
    for x in body.select('.curtain,.skip,.cur,.cur-r,.band,.pill,.stars'): x.decompose()
    h1=body.find('h1');h1t=clean_text(h1.get_text(' ',strip=True)) if h1 else title.split('·')[0].strip()
    lede=''
    if h1:
        blk=h1
        while blk.parent is not None and blk.parent is not body and blk.parent.name not in('main','body'): blk=blk.parent
        p=blk.find('p',class_=lambda c:c!='crumbs') ;lede=clean_text(p.get_text(' ',strip=True)) if p else ''
        if 'crumbs' in (p.get('class') or []) if p else False: lede=''
        blk.decompose()
    # replace v18 map / ladder sections with v19 ones
    hasmap=hasl=False
    for sec in body.select('section.mapsec'): sec.replace_with(BeautifulSoup(MAPF(P),'html.parser'));hasmap=True
    for sec in body.select('section.lad18'): sec.replace_with(BeautifulSoup(CEFRF(P),'html.parser'));hasl=True
    for tag in body.find_all(class_=True):
        cls=[c for c in tag['class'] if not (BAD.fullmatch(c) or re.search(r'eyebrow|badge|chip|pill|(^|-)tag(-|$)',c))]
        if len(cls)!=len(tag['class']): cls.append('kick')
        tag['class']=cls
    for tn in body.find_all(string=True):
        if tn.parent.name in('script','style'): continue
        nt=clean_text(str(tn))
        if nt!=str(tn): tn.replace_with(nt)
    for b in body.select('.voice .pl'): b.string=''
    from bs4 import Comment
    for cm in body.find_all(string=lambda t:isinstance(t,Comment)):
        if 'TODO' not in cm: cm.extract()
    # ===== fold-ify: every top-level block becomes a full-bleed video fold
    top=[c for c in body.children if getattr(c,'name',None)]
    while len(top)==1 and top[0].name in('div','article') and len([c for c in top[0].children if getattr(c,'name',None)])>1:
        top=[c for c in top[0].children if getattr(c,'name',None)]
    POOL=[v_]+[x for x in ROTF if x!=v_]
    out=[];n=0
    for c in top:
        cls=' '.join(c.get('class') or [])
        if c.name=='script' or re.search(r'\b(mapf|cefr|stage|vfold|fold)\b',cls) or c.find('video') is not None and re.search(r'vfold|band|hero',cls):
            out.append(str(c));continue
        if not c.get_text(strip=True) and not c.find('img'): continue
        dark=bool(re.search(r'dark|navy|notte',cls))
        n+=1;vv=POOL[(n+i)%len(POOL)]
        inner_html=''.join(str(x) for x in c.children) if c.name in('section','div') else str(c)
        out.append(f'<section class="fold lf">{bg(vv,P,"wt" if not dark else "wl")}<div class="w"><div class="fp {"glass" if dark else "paper"} rv">{inner_html}</div></div></section>')
    inner=''.join(out)
    a,b=(h1t.split('. ',1)+[''])[:2] if '. ' in h1t else ((' '.join(h1t.split()[:-2]),' '.join(h1t.split()[-2:])) if len(h1t.split())>3 else (h1t,''))
    if b and not a.endswith('.') and '. ' in h1t: a+='.'
    extra=oldcss+(MAPHEAD if hasmap else '')
    hd=head(title,desc,P,extra).replace(f'<link rel="stylesheet" href="{P}css/v19.css">',f'<link rel="stylesheet" href="{P}css/v19.css"><link rel="stylesheet" href="{P}css/v19-legacy.css">')
    hero=f'''<section class="fold hero">{bg(v_,P,'wl',False).replace('<video','<video autoplay data-keep',1)}<div class="w"><h1 class="d2" data-split>{E(a)} <em>{E(b)}</em></h1>{f'<p class="lead" style="margin-top:1.6rem">{E(lede)}</p>' if lede else ''}<div class="row"><a class="cta" href="{P}index.html#enrol">Reserve your seat <i></i></a><a class="cta ghost" href="{P}courses.html">See the courses</a></div></div></section>'''
    end=f'''<section class="fold">{bg('ag-cypress-road',P,'wt')}<div class="w" style="text-align:center"><h2 class="d2" data-split>Culture speaks Italian. <em>Do you?</em></h2><div class="row" style="display:flex;justify-content:center;margin-top:2.4rem"><a class="cta" href="{P}index.html#enrol">Begin <i></i></a></div></div></section>'''
    mods=(MODSF(P) if (hasmap or hasl) else '')
    if hasmap and not hasl: mods=mods.replace(f'<script type="module" src="{P}js/v19-3d.js"></script>','')
    if hasl and not hasmap: mods=f'<script type="module" src="{P}js/v19-3d.js"></script>'
    open(f,'w').write(hd+hero+f'<div class="legacy">{inner}</div>'+end+foot(P,mods))
print(len(files),'legacy pages on v19 shell')
