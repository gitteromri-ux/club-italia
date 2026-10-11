(()=>{const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches,MOB=matchMedia('(max-width:900px)').matches,G=window.gsap,ST=window.ScrollTrigger;
if(RM)document.documentElement.classList.add('rm');
const hd=$('.hd');const sc=()=>hd&&hd.classList.toggle('solid',scrollY>60);addEventListener('scroll',sc,{passive:true});sc();
const mb=$('.menu'),nv=$('.nv');if(mb)mb.onclick=()=>{const o=nv.classList.toggle('open');mb.setAttribute('aria-expanded',o);mb.textContent=o?'Close':'Menu'};
// lazy video
const vo=new IntersectionObserver(es=>es.forEach(e=>{const v=e.target;if(e.isIntersecting){if(!v.getAttribute('src')&&v.dataset.src)v.src=v.dataset.src;if(!RM&&!v.hasAttribute('data-manual'))v.play().catch(()=>{})}else if(v.getAttribute('src')&&!v.hasAttribute('data-keep'))v.pause()}),{rootMargin:'400px'});
$$('video[data-src]').forEach(v=>vo.observe(v));
const load=v=>{if(v&&!v.getAttribute('src')&&v.dataset.src)v.src=v.dataset.src;return v};
// curtain
const cu=$('.curtain');if(cu&&G&&!RM){G.to(cu,{scaleY:0,duration:1,ease:'expo.inOut',delay:.1});
$$('a[href]').forEach(a=>{const h=a.getAttribute('href');if(!h||h[0]=='#'||/^(https?:|mailto|tel)/.test(h)||a.target)return;a.addEventListener('click',e=>{if(e.metaKey||e.ctrlKey)return;e.preventDefault();G.fromTo(cu,{scaleY:0,transformOrigin:'bottom'},{scaleY:1,duration:.65,ease:'expo.in',onComplete:()=>location.href=h})})});addEventListener('pageshow',e=>{if(e.persisted)G.set(cu,{scaleY:0})})}else if(cu)cu.remove();
// cursor
if(!MOB&&!RM&&matchMedia('(hover:hover)').matches){const c=document.createElement('div');c.className='cur';document.body.append(c);let x=0,y=0,cx=0,cy=0;addEventListener('pointermove',e=>{x=e.clientX;y=e.clientY});(function l(){cx+=(x-cx)*.2;cy+=(y-cy)*.2;c.style.transform=`translate(${cx-c.offsetWidth/2}px,${cy-c.offsetHeight/2}px)`;requestAnimationFrame(l)})();
$$('a,button').forEach(el=>{el.addEventListener('mouseenter',()=>c.classList.add('big'));el.addEventListener('mouseleave',()=>c.classList.remove('big'))});
$$('.cta').forEach(el=>{el.addEventListener('pointermove',e=>{const b=el.getBoundingClientRect();el.style.transform=`translate(${(e.clientX-b.left-b.width/2)*.22}px,${(e.clientY-b.top-b.height/2)*.3}px)`});el.addEventListener('pointerleave',()=>el.style.transform='')})}
// music
const mu=$('#music'),th=$('#theme');if(mu)mu.onclick=()=>{if(th.paused){th.volume=.4;th.play();mu.textContent='Music on'}else{th.pause();mu.textContent='Music off'}};
// voices + waveform
let ac,an,cur=null;const bars=$$('.wave i');const viz=()=>{if(!an||!cur){bars.forEach(b=>b.style.height='10%');return}const a=new Uint8Array(an.frequencyBinCount);an.getByteFrequencyData(a);bars.forEach((b,i)=>b.style.height=(10+a[(i*2)%a.length]/255*90)+'%');requestAnimationFrame(viz)};
$$('.voice').forEach(btn=>btn.onclick=()=>{if(cur){cur.a.pause();cur.b.classList.remove('playing');const s=cur.b===btn;cur=null;if(s)return}const a=new Audio(btn.dataset.audio);try{ac=ac||new(window.AudioContext||window.webkitAudioContext)();const s=ac.createMediaElementSource(a);an=ac.createAnalyser();an.fftSize=64;s.connect(an);an.connect(ac.destination);ac.resume()}catch(e){}
a.play();btn.classList.add('playing');cur={a,b:btn};const cp=$('#bcap');if(cp)cp.innerHTML=btn.dataset.line;viz();a.onended=()=>{btn.classList.remove('playing');cur=null}});
// biagio tilt
const bf=$('.bia .fig img');if(bf&&!RM)addEventListener('pointermove',e=>{const rx=(e.clientY/innerHeight-.5)*-14,ry=(e.clientX/innerWidth-.5)*18;bf.style.transform=`rotateX(${rx}deg) rotateY(${ry}deg) translateZ(30px)`});
// quotes
const qf=$$('.qs figure');if(qf.length){let qi=0;qf[0].classList.add('on');setInterval(()=>{qf[qi].classList.remove('on');qi=(qi+1)%qf.length;qf[qi].classList.add('on')},6000)}
// faculty
$$('.fac .nm').forEach(n=>{const go=()=>{$$('.fac .nm').forEach(x=>x.classList.toggle('on',x===n));$$('.fac .bgv').forEach(b=>{const on=b.dataset.k===n.dataset.k;b.classList.toggle('on',on);const v=b.querySelector('video');if(on){load(v);v.play().catch(()=>{})}else v.pause()});const p=$('.fac .port');if(p){p.src=n.dataset.img;p.alt=n.dataset.alt}};n.addEventListener('mouseenter',go);n.addEventListener('focus',go)});
// details single open
$$('[data-acc]').forEach(g=>g.addEventListener('toggle',e=>{if(e.target.open)$$('details',g).forEach(d=>d!==e.target&&(d.open=false))},true));
const lead=$('#lead');if(lead)lead.onsubmit=e=>{e.preventDefault();lead.innerHTML='<h3>Grazie.</h3><p class="full">We have your request. An advisor will reply within one working day.</p>'};
// counters for skills bars
// ===== GSAP
if(!G||!ST||RM){$$('.stmt .wd').forEach(w=>w.style.opacity=1);initStage(null);return}
G.registerPlugin(ST);
if(window.Lenis&&!MOB){const l=new Lenis({lerp:.09});l.on('scroll',ST.update);G.ticker.add(t=>l.raf(t*1000));G.ticker.lagSmoothing(0);window.__lenis=l;$$('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{const t=$(a.getAttribute('href'));if(t){e.preventDefault();l.scrollTo(t)}}))}
$$('.rv').forEach(el=>G.to(el,{y:0,opacity:1,duration:1.3,ease:'expo.out',scrollTrigger:{trigger:el,start:'top 90%'}}));
$$('[data-split]').forEach(h=>{const walk=n=>[...n.childNodes].forEach(c=>{if(c.nodeType==3){const f=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(w=>{if(!w)return;if(/^\s+$/.test(w)){f.append(w);return}const o=document.createElement('span');o.className='sl';const i=document.createElement('span');i.textContent=w;o.append(i);f.append(o)});c.replaceWith(f)}else if(c.nodeType==1)walk(c)});walk(h);
G.from($$('.sl>span',h),{yPercent:110,duration:1.4,ease:'expo.out',stagger:.05,delay:h.tagName=='H1'?.7:0,scrollTrigger:h.tagName=='H1'?null:{trigger:h,start:'top 88%'}})});
const hero=$('.hero');if(hero){G.from('.hero .lead,.hero .row,.hero .facts',{y:30,opacity:0,duration:1.3,ease:'expo.out',stagger:.12,delay:1.2});G.to('.hero .w',{yPercent:-18,opacity:.2,ease:'none',scrollTrigger:{trigger:hero,start:'top top',end:'bottom top',scrub:true}})}
const wd=$$('.stmt .wd');if(wd.length)G.to(wd,{opacity:1,stagger:.06,ease:'none',scrollTrigger:{trigger:'.stmt',start:'top 65%',end:'bottom 70%',scrub:true}});
$$('[data-par] video').forEach(v=>G.fromTo(v,{scale:1.15,yPercent:-4},{scale:1.02,yPercent:4,ease:'none',scrollTrigger:{trigger:v.closest('[data-par]'),start:'top bottom',end:'bottom top',scrub:true}}));
// rail
const tr=$('.track');if(tr&&!MOB){const d=()=>tr.scrollWidth-innerWidth;const panels=$$('.panel',tr);
G.to(tr,{x:()=>-d(),ease:'none',scrollTrigger:{trigger:'.rail',start:'top top',end:()=>'+='+d(),pin:true,scrub:1,invalidateOnRefresh:true,onUpdate:s=>{$('.rprog').style.width=s.progress*100+'%';const i=Math.round(s.progress*(panels.length-1));panels.forEach((p,j)=>{const v=p.querySelector('video');if(!v)return;if(Math.abs(j-i)<=1){load(v);v.play().catch(()=>{})}else v.pause()})}}});
panels.forEach(p=>{const h=p.querySelector('h3');if(h)G.from(h,{xPercent:20,ease:'none',scrollTrigger:{trigger:p,containerAnimation:ST.getAll().slice(-1)[0].animation,start:'left right',end:'left left',scrub:true}})})}
$$('.skills i').forEach(i=>G.from(i,{scaleX:0,duration:1.4,ease:'expo.out',scrollTrigger:{trigger:i,start:'top 92%'}}));
initStage(ST);
function initStage(ST){const st=$('.stage');if(!st)return;const ch=$$('.ch',st),bg=$$('.bgv',st),ct=$('.count',st);let cur=-1;const set=i=>{if(i===cur)return;cur=i;ch.forEach((c,j)=>c.classList.toggle('on',j===i));bg.forEach((b,j)=>{const v=b.querySelector('video');b.classList.toggle('on',j===i);if(Math.abs(j-i)<=1)load(v);if(j===i)v.play().catch(()=>{});else v.pause()});if(ct)ct.textContent='0'+(i+1)};set(0);
if(ST)ST.create({trigger:st,start:'top top',end:'bottom bottom',onUpdate:s=>set(Math.min(ch.length-1,Math.floor(s.progress*ch.length)))});else{ch.forEach(c=>c.classList.add('on'))}}
addEventListener('load',()=>ST.refresh());
})();
