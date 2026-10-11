import re
def brand(out,P):
  out=re.sub(r'<span class="ci-lock">.*?</span></span>',lambda m:f'<img class="ci-lockup" src="{P}assets/brand/club-italia-lockup-dark.svg" alt="Club Italia by eTeacher Group" width="176" height="83">',out,flags=re.S)
  out=re.sub(r'family=Cormorant\+Garamond[^&"]*','family=Instrument+Serif:ital@0;1',out)
  out=out.replace('family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&amp;family=Inter','family=Instrument+Serif:ital@0;1&amp;family=Inter')
  out=re.sub(r'(<link href="[^"]*fa/css/ci-calm.css" rel="stylesheet"/>)',lambda m:m.group(1)+f'<link href="{P}fa/css/ci-brand.css" rel="stylesheet"/>',out,1)
  if False: out=out.replace('fa/css/ci-calm.css">',f'fa/css/ci-calm.css"><link rel="stylesheet" href="{P}fa/css/ci-brand.css">',1).replace('fa/css/ci-calm.css"/>',f'fa/css/ci-calm.css"/><link rel="stylesheet" href="{P}fa/css/ci-brand.css"/>',1)
  return out
