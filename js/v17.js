(()=>{const h=document.querySelector('.hdr');const onS=()=>h&&h.classList.toggle('solid',scrollY>40);addEventListener('scroll',onS,{passive:true});onS();
const b=document.querySelector('.burger'),n=document.querySelector('.nav');b&&b.addEventListener('click',()=>{const o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);h.classList.add('solid')});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});document.querySelectorAll('.rv').forEach(el=>io.observe(el));
if(matchMedia('(prefers-reduced-motion: reduce)').matches)document.querySelectorAll('video[autoplay]').forEach(v=>v.pause());
document.querySelectorAll('form[data-demo]').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();f.innerHTML='<p class="lede">Grazie. An advisor will be in touch within one working day.</p>'}));})();
