/* Club Italia — global JS: nav scroll, drawer, modal, reveal, form */
(function(){
  const header = document.querySelector('.site-header');
  const onScroll = () => { if (!header) return; window.scrollY > 30 ? header.classList.add('scrolled') : header.classList.remove('scrolled'); };
  window.addEventListener('scroll', onScroll, {passive:true}); onScroll();

  const toggle = document.querySelector('.nav-toggle');
  const drawer = document.getElementById('navDrawer');
  const closeDr = document.querySelector('.nav-drawer-close');
  if (toggle && drawer) toggle.addEventListener('click', () => drawer.classList.add('open'));
  if (closeDr && drawer) closeDr.addEventListener('click', () => drawer.classList.remove('open'));

  const modal = document.querySelector('.advisor-modal');
  const modalClose = document.querySelector('.advisor-modal-close');
  document.querySelectorAll('[data-advisor]').forEach(el => el.addEventListener('click', e => { e.preventDefault(); modal && modal.classList.add('open'); }));
  if (modalClose && modal) modalClose.addEventListener('click', () => modal.classList.remove('open'));
  if (modal) modal.addEventListener('click', e => { if (e.target === modal) modal.classList.remove('open'); });

  // Reveal on scroll
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, {threshold:.12, rootMargin:'0px 0px -8% 0px'});
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  // Advisor form — collects lead, prints to console, shows success
  const form = document.querySelector('.advisor-form');
  const success = document.querySelector('.advisor-success');
  if (form) form.addEventListener('submit', e => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(form).entries());
    let ok = true;
    form.querySelectorAll('input[required], select[required]').forEach(inp => {
      const err = inp.parentElement.querySelector('.err-msg');
      if (!inp.value.trim()) { if (err) err.textContent = 'Required'; ok = false; }
      else if (err) err.textContent = '';
    });
    if (!ok) return;
    console.log('[Club Italia lead]', data);
    form.style.display = 'none';
    if (success) success.classList.add('show');
  });

  // FAQ accordion — details tag native, nothing needed

  // Biagio AI Tutor chat demo
  const bChatForm = document.getElementById('biagio-chat-form');
  const bChatMsgs = document.getElementById('biagio-chat-msgs');
  const bReplies = [
    "Perfetto! Ripetiamo: 'Vorrei un espresso, per favore.' — try it out loud.",
    "Bravissimo. Now the same, but at a caffè in Firenze — order for two.",
    "Ottimo lavoro. Small correction: it's 'due caffè', not 'dos caffè'. Try again.",
    "Now let's practice ordering something to eat. Repeat: 'Un cornetto, grazie.'",
    "That's exactly how a Roman would say it. Andiamo — one more."
  ];
  let bStep = 0;
  if (bChatForm && bChatMsgs) bChatForm.addEventListener('submit', e => {
    e.preventDefault();
    const input = bChatForm.querySelector('input');
    const text = input.value.trim(); if (!text) return;
    const u = document.createElement('div'); u.className = 'chat-msg user'; u.textContent = text; bChatMsgs.appendChild(u);
    input.value = '';
    setTimeout(() => {
      const b = document.createElement('div'); b.className = 'chat-msg bot';
      b.textContent = bReplies[bStep % bReplies.length]; bStep++;
      bChatMsgs.appendChild(b); bChatMsgs.scrollTop = bChatMsgs.scrollHeight;
    }, 500);
    bChatMsgs.scrollTop = bChatMsgs.scrollHeight;
  });
})();
