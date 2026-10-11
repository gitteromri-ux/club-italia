(()=>{const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;if(RM)document.documentElement.classList.add('rm');
const hd=$('.hd');const sc=()=>hd&&hd.classList.toggle('solid',scrollY>60);addEventListener('scroll',sc,{passive:true});sc();
const mb=$('.menu'),nv=$('.nv');if(mb)mb.onclick=()=>{const o=nv.classList.toggle('open');mb.setAttribute('aria-expanded',o);mb.textContent=o?'Close':'Menu'};
const vo=new IntersectionObserver(es=>es.forEach(e=>{const v=e.target;if(e.isIntersecting){if(!v.getAttribute('src')&&v.dataset.src)v.src=v.dataset.src;if(!RM)v.play().catch(()=>{})}else if(v.getAttribute('src'))v.pause()}),{rootMargin:'300px'});$$('video[data-src]').forEach(v=>vo.observe(v));
const ro=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');ro.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});$$('.rv').forEach(x=>ro.observe(x));
let cur=null;$$('.voice').forEach(b=>b.onclick=()=>{if(cur){cur.a.pause();cur.b.classList.remove('playing');const s=cur.b===b;cur=null;if(s)return}const a=new Audio(b.dataset.audio);a.play();b.classList.add('playing');cur={a,b};const c=$('#bcap');if(c)c.innerHTML=b.dataset.line;a.onended=()=>{b.classList.remove('playing');cur=null}});
$$('[data-acc]').forEach(g=>g.addEventListener('toggle',e=>{if(e.target.open)$$('details',g).forEach(d=>d!==e.target&&(d.open=false))},true));
const l=$('#lead');if(l)l.onsubmit=e=>{e.preventDefault();l.innerHTML='<h3>Grazie.</h3><p class="full">We have your request. An advisor will reply within one working day.</p>'};
})();
