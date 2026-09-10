/* Club Italia — global JS: nav scroll, drawer, modal, reveal, form
   v3 additions: sticky enroll, urgency rotator, seats counter,
   auto-inject urgency strip + sticky enroll on every page.
*/

/* ====== v3 · Auto-inject urgency strip + sticky enroll bar ====== */
document.addEventListener('DOMContentLoaded', () => {
  // Top urgency strip
  if (!document.querySelector('.urgency-strip')) {
    const s = document.createElement('div');
    s.className = 'urgency-strip';
    s.innerHTML = '<div class="wrap us-wrap"><span class="us-badge">LIMITED</span><span class="us-msg" data-rotate>Autumn cohort opens Oct 6 · <b>4 seats left</b> in Marco\'s Roma group</span><button class="us-close" aria-label="dismiss">×</button></div>';
    document.body.insertBefore(s, document.body.firstChild);
  }
  // Sticky enroll bottom bar
  if (!document.querySelector('.sticky-enroll')) {
    const b = document.createElement('div');
    b.className = 'sticky-enroll';
    b.innerHTML = '<div class="wrap se-wrap"><div class="se-left"><span class="se-price">$62<small>/week</small></span><span class="se-trust">★★★★★ 4.8 · Trustpilot</span><span class="se-seats"><b class="se-seat-num">4</b> seats left · October cohort</span></div><a class="btn se-cta" href="#" data-advisor>Reserve My Placement Call</a></div>';
    document.body.appendChild(b);
  }

  // ---- initStickyEnroll ----
  const enrollBar = document.querySelector('.sticky-enroll');
  const toggleEnroll = () => {
    if (!enrollBar) return;
    const show = window.scrollY > 400;
    enrollBar.classList.toggle('visible', show);
    document.body.classList.toggle('se-shown', show);
  };
  window.addEventListener('scroll', toggleEnroll, {passive:true});
  toggleEnroll();

  // ---- urgency strip close ----
  const usClose = document.querySelector('.us-close');
  if (usClose) usClose.addEventListener('click', e => {
    const strip = e.target.closest('.urgency-strip');
    if (strip) strip.style.display = 'none';
    // reset nav offset when dismissed
    const hdr = document.querySelector('.site-header');
    if (hdr) hdr.style.top = '0';
  });

  // ---- initUrgencyRotator ----
  const rot = document.querySelector('.urgency-strip [data-rotate]');
  const messages = [
    'Autumn cohort opens Oct 6 · <b>4 seats left</b> in Marco\'s Roma group',
    'Live from Firenze tonight 8pm · <b>Free trial class</b> with Giulia',
    'Founding members: <b>Save $240</b> on your first quarter · Ends Sunday',
    'Certificate cohort forming now · <b>Only 6 placement calls</b> remain this week'
  ];
  let midx = 0;
  if (rot) setInterval(() => {
    midx = (midx + 1) % messages.length;
    rot.style.opacity = '0';
    setTimeout(() => {
      rot.innerHTML = messages[midx];
      rot.style.opacity = '1';
    }, 300);
  }, 6000);

  // ---- initSeatsCounter ----
  const seatEl = document.querySelector('.se-seat-num');
  if (seatEl) {
    let seats = 12;
    seatEl.textContent = seats;
    const decrement = () => {
      if (seats > 4) {
        seats--;
        seatEl.textContent = seats;
        // Random cadence: 45s to 90s
        setTimeout(decrement, 45000 + Math.random() * 45000);
      }
    };
    // First decrement after 30s of viewing
    setTimeout(decrement, 30000);
  }
});

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
    "Perfetto. Ripetiamo: 'Vorrei un espresso, per favore.' — try it out loud.",
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
