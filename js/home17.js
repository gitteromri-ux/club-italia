(()=>{const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
const h=$('.hdr');const sc=()=>h.classList.toggle('solid',scrollY>40);addEventListener('scroll',sc,{passive:true});sc();
const b=$('.burger'),n=$('.nav');b.onclick=()=>{const o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)};$$('.nav a').forEach(a=>a.onclick=()=>n.classList.remove('open'));
const rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.1});$$('.rv').forEach(x=>io.observe(x));
// lazy videos: load + play in view, pause out of view
const vo=new IntersectionObserver(es=>es.forEach(e=>{const v=e.target;if(e.isIntersecting){if(!v.src&&v.dataset.src){v.src=v.dataset.src}if(!rm)v.play().catch(()=>{})}else if(v.src)v.pause()}),{rootMargin:'200px'});
$$('video[data-src]').forEach(v=>vo.observe(v));
// course tabs
const tabs=$$('#ctabs button');function f(t){tabs.forEach(x=>x.setAttribute('aria-pressed',x.dataset.f==t));$$('#cgrid .cc').forEach(c=>c.hidden=!(t=='all'||c.dataset.t==t))}
tabs.forEach(x=>x.onclick=()=>f(x.dataset.f));$$('[data-go]').forEach(x=>x.onclick=()=>{f(x.dataset.go);$('#ctabs').scrollIntoView({behavior:'smooth',block:'start'})});
// sound toggles
$$('[data-snd]').forEach(btn=>btn.onclick=()=>{const v=btn.parentElement.querySelector('video');if(!v.src)v.src=v.dataset.src;v.muted=!v.muted;v.play();btn.textContent=v.muted?'🔈 Sound on':'🔇 Mute'});
// biagio voices
let cur=null;$$('.voice').forEach(btn=>btn.onclick=()=>{if(cur){cur.a.pause();cur.b.classList.remove('playing');cur.b.querySelector('.pl').textContent='▶';if(cur.b===btn){cur=null;return}}
const a=new Audio(btn.dataset.audio);a.play();btn.classList.add('playing');btn.querySelector('.pl').textContent='❚❚';cur={a,b:btn};a.onended=()=>{btn.classList.remove('playing');btn.querySelector('.pl').textContent='▶';cur=null}});
// music
const m=$('#music'),t=$('#theme');m.onclick=()=>{if(t.paused){t.volume=.4;t.play();m.textContent='♪ Music on';m.setAttribute('aria-pressed','true')}else{t.pause();m.textContent='♪ Music off';m.setAttribute('aria-pressed','false')}};
// level finder
const R={0:['CI Principiante','pages/courses/ci1.html','A0 to A1.1'],1:['CI Elementare','pages/courses/ci2.html','A1.1 to A1.2'],2:['CI Intermedio','pages/courses/ci3.html','A1.2 to A2.1'],3:['CI Avanzato','pages/courses/ci4.html','A2.1 to A2.2']};
const S={0:['Al Caffè','pages/spoken/ps1.html'],1:['A Tavola','pages/spoken/ps2.html'],2:['In Viaggio','pages/spoken/ps3.html'],3:['Chiacchierando','pages/spoken/ps4.html']};
$('#qz').onchange=()=>{const d=new FormData($('#qz'));const lv=d.get('lv'),g=d.get('g');if(lv==null||!g)return;let html;
if(g=='s'){const s=S[lv];html=`Recommended: <b>${s[0]}</b>, our spoken track. <a class="lnk" href="${s[1]}">View course</a>`}
else if(g=='c'){html=`Recommended: a <b>cultural capsule</b> (La Cucina, L'Arte or L'Opera), alongside <b>${R[lv][0]}</b>. <a class="lnk" href="capsules.html">See capsules</a>`}
else if(g=='x'){html=`Recommended: <b>${R[lv][0]}</b> (${R[lv][2]}), then onward to B1 with CILS or CELI preparation. <a class="lnk" href="certifications.html">Certification path</a>`}
else{html=`Recommended: <b>${R[lv][0]}</b> (${R[lv][2]}). <a class="lnk" href="${R[lv][1]}">View course</a>`}
const p=d.get('p');if(p=='2')html+=' Twice a week completes the course in about ten weeks.';
const r=$('#res');r.innerHTML=html;r.classList.add('on')};
$('#lead').onsubmit=e=>{e.preventDefault();e.target.innerHTML='<h4>Grazie.</h4><p style="grid-column:1/-1;color:#cfc8b8">Your request is on its way. A Club Italia advisor will be in touch within one working day.</p>'};
})();
