"""Build the 10 new/deepened pages for Club Italia — Agent D."""
import os, textwrap
BASE = "/home/user/workspace/club-italia"

# ---------- shared chrome ----------

NAV = '''<header class="site-header">
  <div class="wrap nav">
    <a class="nav-logo" href="{root}index.html" aria-label="Club Italia — home">
      <span class="logo-text">
        <span class="lt-main">Club Italia</span>
        <span class="lt-sub">by eTeacher</span>
      </span>
    </a>
    <nav class="nav-menu" aria-label="Primary">
      <span class="nav-item"><a class="nav-link" href="{root}courses.html">Courses</a></span>
      <span class="nav-item"><a class="nav-link" href="{root}how-it-works.html">How It Works</a></span>
      <span class="nav-item"><a class="nav-link" href="{root}method.html">Method</a></span>
      <span class="nav-item"><a class="nav-link" href="{root}teachers.html">Teachers</a></span>
      <span class="nav-item"><a class="nav-link" href="{root}culture.html">Culture</a></span>
      <span class="nav-item"><a class="nav-link" href="{root}events.html">Events</a></span>
      <span class="nav-item"><a class="nav-link" href="{root}map.html">Map</a></span>
      <span class="nav-item"><a class="nav-link" href="{root}pricing.html">Pricing</a></span>
    </nav>
    <button class="btn btn-3d btn-3d-primary nav-cta" data-advisor type="button">Talk to an Advisor</button>
    <button class="nav-toggle" aria-label="Open menu" aria-controls="navDrawer" type="button"><span></span><span></span><span></span></button>
  </div>
</header>
<aside class="nav-drawer" id="navDrawer" aria-label="Mobile menu">
  <button class="nav-drawer-close" aria-label="Close menu" type="button">&times;</button>
  <a href="{root}courses.html">Courses</a><a href="{root}how-it-works.html">How It Works</a><a href="{root}method.html">Method</a>
  <a href="{root}teachers.html">Teachers</a><a href="{root}culture.html">Culture</a><a href="{root}events.html">Events</a>
  <a href="{root}map.html">Map</a><a href="{root}community.html">Community</a><a href="{root}sample-class.html">Sample Class</a>
  <a href="{root}biagio.html">AI Tutor</a><a href="{root}pricing.html">Pricing</a><a href="{root}about.html">About</a>
  <a href="{root}contact.html">Contact</a>
  <button class="btn btn-3d btn-3d-primary" data-advisor type="button" style="width:100%;margin-top:1.6rem">Talk to an Advisor</button>
</aside>'''

FOOTER = '''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="lt-main" style="font-family:var(--serif);font-size:1.5rem;color:var(--gold-soft);margin-bottom:.4rem">Club Italia</div>
        <div class="lt-sub" style="font-size:.6rem;letter-spacing:.28em;text-transform:uppercase;color:var(--on-dark-soft);margin-bottom:1.2rem">by eTeacher</div>
        <p>Club Italia by eTeacher, a culturally immersive, certified, live Italian language school for adult lifelong learners in the United States and around the world.</p>
        <p style="margin-top:1.2rem"><a href="mailto:advisor@eTeacherGroup.com" style="display:inline-flex;align-items:center;gap:.55rem;color:var(--gold-soft)">✉ advisor@eTeacherGroup.com</a></p>
      </div>
      <div class="footer-col">
        <h4>Learn</h4>
        <a href="{root}courses.html">All Courses</a>
        <a href="{root}how-it-works.html">How It Works</a>
        <a href="{root}method.html">Method</a>
        <a href="{root}sample-class.html">Watch a Class</a>
        <a href="{root}teachers.html">Teachers</a>
        <a href="{root}map.html">Map of Italy</a>
      </div>
      <div class="footer-col">
        <h4>Culture</h4>
        <a href="{root}culture.html">Culture</a>
        <a href="{root}capsules.html">Capsules</a>
        <a href="{root}events.html">Cultural Events</a>
        <a href="{root}community.html">Community</a>
        <a href="{root}blog.html">Journal</a>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <a href="{root}about.html">About</a>
        <a href="{root}eteacher.html">eTeacher Group</a>
        <a href="{root}pricing.html">Pricing</a>
        <a href="{root}faq.html">FAQ</a>
        <a href="{root}contact.html">Contact</a>
        <a href="{root}privacy.html">Privacy</a>
        <a href="{root}terms.html">Terms</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 eTeacher Group. All rights reserved. Club Italia is a trading style of eTeacher Group.</p>
      <div class="footer-social">
        <a href="#" aria-label="Facebook">f</a>
        <a href="#" aria-label="Instagram">◉</a>
        <a href="#" aria-label="YouTube">▶</a>
      </div>
    </div>
  </div>
</footer>
<script src="{root}js/ci.js" defer></script>'''

def shell(title, desc, body, root="", extra_head=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{root}css/ci.css">
{extra_head}
</head>
<body>
{NAV.format(root=root)}
{body}
{FOOTER.format(root=root)}
</body>
</html>
'''
