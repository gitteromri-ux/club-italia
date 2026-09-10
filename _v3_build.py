#!/usr/bin/env python3
"""
Club Italia v3 builder — IIBS-quality academic pages.
Red / White / Green / Black + gold hairline accent.
Playfair Display + Inter. Edge-to-edge course grid.
"""
import json, os, re, pathlib
ROOT = pathlib.Path("/home/user/workspace/club-italia")
DATA = json.loads((ROOT/"research/course-data.json").read_text())
NAV = (ROOT/"_partials/nav.html").read_text()
FOOT = (ROOT/"_partials/footer.html").read_text()

# ---- shared: <head>, top strip, JS shim, inline critical CSS ----
INLINE_CRITICAL = r"""
<style>
/* v3 palette override — applied globally until ci.css rebuild lands */
:root{
  --red:#B01823; --red-deep:#8B0F1D; --red-bright:#C7202E;
  --green:#166A47; --green-deep:#0C3B2E; --green-bright:#1E8A5E;
  --paper:#FBFAF6; --cream:#F3F0E7; --ink:#0B0B0D; --ink-2:#1A1A1E;
  --gold:#B08640; --gold-line:rgba(176,134,64,.45);
  --cream-accent:#E6C99B;
  --serif:'Playfair Display','Cormorant Garamond',Georgia,serif;
  --sans:'Inter',system-ui,-apple-system,sans-serif;
}
html,body{background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:17px;line-height:1.55;margin:0;padding:0;}
*{box-sizing:border-box;}
img{max-width:100%;display:block;}
a{color:inherit;text-decoration:none;}
h1,h2,h3,h4{font-family:var(--serif);font-weight:600;letter-spacing:-.01em;line-height:1.05;margin:0;}
p{margin:0 0 1em 0;}
.wrap{max-width:1360px;margin:0 auto;padding:0 clamp(1rem,3vw,2.4rem);}
.wrap-narrow{max-width:960px;margin:0 auto;padding:0 clamp(1rem,3vw,2.4rem);}
/* sections alternate */
section{padding:clamp(4rem,8vw,7rem) 0;position:relative;}
.section-white{background:var(--paper);color:var(--ink);}
.section-cream{background:var(--cream);color:var(--ink);}
.section-green{background:var(--green-deep);color:var(--paper);}
.section-red{background:var(--red-deep);color:var(--paper);}
.section-black{background:var(--ink);color:var(--paper);}
.section-green h1,.section-green h2,.section-green h3,
.section-red h1,.section-red h2,.section-red h3,
.section-black h1,.section-black h2,.section-black h3{color:var(--paper);}
.section-eyebrow{font-family:var(--sans);font-size:.72rem;letter-spacing:.34em;text-transform:uppercase;color:var(--gold);margin-bottom:1.2rem;font-weight:500;}
.section-black .section-eyebrow,.section-red .section-eyebrow,.section-green .section-eyebrow{color:var(--cream-accent);}
.h-display{font-family:var(--serif);font-weight:700;font-size:clamp(2.6rem,5.4vw,4.6rem);line-height:1.02;letter-spacing:-.015em;margin-bottom:1.4rem;}
.h-display .ital{font-style:italic;font-weight:500;color:var(--red);}
.section-black .h-display .ital,.section-red .h-display .ital,.section-green .h-display .ital{color:var(--cream-accent);}
.h-eyebrow{font-family:var(--sans);font-size:.72rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);margin-bottom:1.1rem;font-weight:500;}
.lede{font-size:1.24rem;line-height:1.55;color:var(--ink-2);max-width:62ch;font-weight:300;}
.section-green .lede,.section-red .lede,.section-black .lede{color:rgba(251,250,246,.86);}

/* Gold hairline rule */
.rule-gold{width:64px;height:1px;background:var(--gold);margin:0 0 1.4rem 0;}

/* Top urgency strip */
.top-strip{background:var(--ink);color:var(--paper);font-family:var(--sans);font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;padding:.55rem 0;text-align:center;border-bottom:1px solid var(--gold-line);}
.top-strip .dot{display:inline-block;width:6px;height:6px;background:var(--red-bright);border-radius:50%;margin:0 .8rem;vertical-align:middle;}

/* HERO */
.hero{position:relative;min-height:100vh;display:flex;align-items:flex-end;overflow:hidden;color:var(--paper);background:var(--ink);}
.hero .hero-video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;}
.hero .hero-scrim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,11,13,.55) 0%,rgba(11,11,13,.35) 40%,rgba(11,11,13,.82) 100%);z-index:1;}
.hero .hero-wrap{position:relative;z-index:2;width:100%;padding:0 clamp(1.2rem,4vw,3rem) clamp(3rem,7vw,6rem);}
.hero-eyebrow{font-family:var(--sans);font-size:.75rem;letter-spacing:.42em;text-transform:uppercase;color:var(--cream-accent);margin-bottom:1.4rem;}
.hero-h1{font-family:var(--serif);font-weight:700;font-size:clamp(4.4rem,10vw,9.2rem);line-height:.94;letter-spacing:-.025em;margin:0 0 1.6rem 0;max-width:16ch;}
.hero-h1 .ital{font-style:italic;font-weight:500;color:var(--cream-accent);}
.hero-sub{font-size:clamp(1.15rem,1.6vw,1.5rem);line-height:1.5;max-width:56ch;color:rgba(251,250,246,.88);font-weight:300;margin:0 0 2rem 0;}
.hero-ctas{display:flex;gap:1rem;flex-wrap:wrap;margin-top:2rem;}
.hero-trust{position:absolute;top:clamp(1rem,3vw,2rem);right:clamp(1rem,3vw,2.4rem);z-index:3;display:flex;align-items:center;gap:.7rem;font-size:.82rem;color:var(--paper);background:rgba(11,11,13,.4);backdrop-filter:blur(6px);padding:.55rem .95rem;border:1px solid rgba(255,255,255,.15);border-radius:2px;}
.hero-trust .stars{color:#F5B93B;letter-spacing:.05em;}
.hero-live{position:absolute;bottom:clamp(1rem,3vw,2rem);left:clamp(1.2rem,4vw,3rem);z-index:3;display:inline-flex;align-items:center;gap:.55rem;font-size:.72rem;letter-spacing:.24em;text-transform:uppercase;color:var(--paper);}
.hero-live .live-dot{width:8px;height:8px;background:var(--red-bright);border-radius:50%;box-shadow:0 0 0 0 rgba(199,32,46,.6);animation:pulse 2s infinite;}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(199,32,46,.6);}70%{box-shadow:0 0 0 14px rgba(199,32,46,0);}100%{box-shadow:0 0 0 0 rgba(199,32,46,0);}}

/* Buttons */
.btn{display:inline-flex;align-items:center;gap:.6rem;padding:1rem 1.6rem;font-family:var(--sans);font-weight:500;font-size:.92rem;letter-spacing:.06em;text-transform:uppercase;border:1px solid transparent;border-radius:0;cursor:pointer;transition:transform .18s ease,background .18s ease,color .18s ease;}
.btn-primary{background:var(--green);color:var(--paper);}
.btn-primary:hover{background:var(--green-deep);transform:translateY(-1px);}
.btn-red{background:var(--red);color:var(--paper);}
.btn-red:hover{background:var(--red-deep);}
.btn-ghost{background:transparent;color:var(--paper);border-color:rgba(255,255,255,.5);}
.btn-ghost:hover{background:rgba(255,255,255,.08);}
.btn-ghost-dark{background:transparent;color:var(--ink);border-color:var(--ink);}
.btn-ghost-dark:hover{background:var(--ink);color:var(--paper);}
.btn-lg{padding:1.2rem 2rem;font-size:1rem;}

/* Course card GRID — edge-to-edge, hairline borders */
.cg{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--ink);border-left:1px solid var(--ink);}
@media (max-width:1100px){.cg{grid-template-columns:repeat(2,1fr);}}
@media (max-width:640px){.cg{grid-template-columns:1fr;}}
.cg-track{grid-column:1/-1;background:var(--ink);color:var(--paper);padding:1.4rem clamp(1.2rem,3vw,2rem);font-family:var(--serif);font-style:italic;font-size:1.4rem;letter-spacing:.02em;border-right:1px solid var(--ink);border-bottom:1px solid var(--ink);display:flex;align-items:baseline;justify-content:space-between;gap:1.4rem;}
.cg-track .track-meta{font-family:var(--sans);font-style:normal;font-size:.72rem;letter-spacing:.28em;text-transform:uppercase;color:var(--cream-accent);}
.cc{background:var(--paper);color:var(--ink);border-right:1px solid var(--ink);border-bottom:1px solid var(--ink);padding:2rem clamp(1.2rem,2vw,1.7rem) 1.6rem;display:flex;flex-direction:column;min-height:380px;position:relative;transition:background .18s ease;}
.cc:hover{background:var(--cream);}
.cc-price{font-family:var(--serif);font-size:2.2rem;font-weight:600;color:var(--red);margin-bottom:.15rem;letter-spacing:-.01em;}
.cc-price small{font-family:var(--sans);font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-2);font-weight:400;margin-left:.35rem;}
.cc-badge{display:inline-block;font-family:var(--sans);font-size:.65rem;letter-spacing:.22em;text-transform:uppercase;color:var(--green-deep);border:1px solid var(--green);padding:.28rem .55rem;margin-bottom:1rem;align-self:flex-start;}
.cc-title{font-family:var(--serif);font-size:1.65rem;font-weight:600;line-height:1.05;margin-bottom:.35rem;letter-spacing:-.01em;}
.cc-sub{font-family:var(--serif);font-style:italic;font-size:1rem;color:var(--red-deep);margin-bottom:.9rem;line-height:1.3;}
.cc-meta{font-family:var(--sans);font-size:.78rem;color:var(--ink-2);letter-spacing:.01em;margin-bottom:1.6rem;line-height:1.55;flex-grow:1;}
.cc-meta .meta-row{display:block;padding:.28rem 0;border-bottom:1px dotted rgba(11,11,13,.15);}
.cc-meta .meta-row:last-child{border:0;}
.cc-enroll{display:inline-flex;align-items:center;justify-content:space-between;background:var(--green);color:var(--paper);padding:.85rem 1.1rem;font-family:var(--sans);font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;font-weight:500;margin-top:auto;transition:background .18s ease;}
.cc-enroll:hover{background:var(--green-deep);}
.cc-enroll .arrow{font-family:var(--serif);font-style:italic;font-size:1.2rem;}

/* Stats row */
.stats{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--gold-line);border-bottom:1px solid var(--gold-line);}
@media (max-width:800px){.stats{grid-template-columns:repeat(2,1fr);}}
.stat{padding:1.6rem 1.2rem;text-align:center;border-right:1px solid var(--gold-line);}
.stat:last-child{border-right:0;}
.stat-num{font-family:var(--serif);font-size:2.4rem;font-weight:600;color:var(--red);line-height:1;margin-bottom:.35rem;}
.stat-lab{font-family:var(--sans);font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;color:var(--ink-2);}
.section-black .stat-num,.section-green .stat-num,.section-red .stat-num{color:var(--cream-accent);}
.section-black .stat-lab,.section-green .stat-lab,.section-red .stat-lab{color:rgba(251,250,246,.65);}

/* Syllabus table (IIBS academic register) */
.syllabus-table{width:100%;border-collapse:collapse;font-family:var(--sans);font-size:.92rem;border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);margin-top:2rem;}
.syllabus-table thead th{background:var(--ink);color:var(--paper);font-family:var(--sans);font-weight:500;font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;text-align:left;padding:1rem 1.1rem;border-right:1px solid rgba(255,255,255,.1);}
.syllabus-table tbody td{padding:1.1rem 1.1rem;border-bottom:1px solid rgba(11,11,13,.1);border-right:1px solid rgba(11,11,13,.08);vertical-align:top;line-height:1.5;}
.syllabus-table tbody tr:nth-child(even) td{background:var(--cream);}
.syllabus-table .lesson-num{font-family:var(--serif);font-size:1.4rem;color:var(--red);font-weight:600;width:70px;}
.syllabus-table .topic{font-family:var(--serif);font-size:1.15rem;font-style:italic;color:var(--ink);width:22%;}
.syllabus-table .grammar{font-family:var(--sans);font-size:.9rem;color:var(--ink-2);}
.syllabus-table .culture{font-family:var(--sans);font-size:.88rem;color:var(--green-deep);font-style:italic;width:26%;}

/* At-a-glance academic table */
.glance{width:100%;border-collapse:collapse;font-family:var(--sans);font-size:.98rem;border-top:2px solid var(--ink);}
.glance tr td{padding:1.05rem 0;border-bottom:1px solid rgba(11,11,13,.14);vertical-align:top;}
.glance tr td:first-child{font-family:var(--sans);font-size:.74rem;letter-spacing:.22em;text-transform:uppercase;color:var(--red);font-weight:500;width:38%;padding-right:1.4rem;}
.glance tr td:last-child{font-family:var(--serif);font-size:1.1rem;color:var(--ink);line-height:1.45;}

/* Outcomes list */
.outcomes{list-style:none;padding:0;margin:2rem 0 0 0;counter-reset:o;}
.outcomes li{counter-increment:o;padding:1.1rem 0 1.1rem 3.6rem;border-bottom:1px solid rgba(11,11,13,.12);position:relative;font-family:var(--serif);font-size:1.15rem;font-style:italic;line-height:1.4;color:var(--ink);}
.outcomes li::before{content:counter(o,decimal-leading-zero);position:absolute;left:0;top:1.1rem;font-family:var(--sans);font-size:.72rem;letter-spacing:.18em;color:var(--gold);font-style:normal;font-weight:500;}

/* Frames */
.zoom-frame{background:var(--ink-2);border:1px solid rgba(255,255,255,.1);border-radius:6px;padding:.6rem;box-shadow:0 30px 70px -20px rgba(0,0,0,.6);}
.zoom-frame img{width:100%;display:block;border-radius:3px;}
.cert-frame{background:var(--paper);border:1px solid rgba(11,11,13,.12);padding:1rem;box-shadow:0 40px 80px -30px rgba(11,11,13,.35);}
.browser-frame{border:1px solid rgba(11,11,13,.15);border-radius:6px;overflow:hidden;box-shadow:0 30px 70px -20px rgba(11,11,13,.25);background:#fff;}
.browser-chrome{background:#EEE;padding:.55rem .9rem;border-bottom:1px solid rgba(0,0,0,.08);display:flex;gap:.4rem;align-items:center;}
.browser-chrome span{width:10px;height:10px;border-radius:50%;background:#ccc;}
.browser-chrome span:first-child{background:#F35B5B;}
.browser-chrome span:nth-child(2){background:#F5B93B;}
.browser-chrome span:nth-child(3){background:#4CC26A;}
.browser-chrome .url{margin-left:.9rem;font-family:var(--sans);font-size:.74rem;color:#666;}

/* Teacher tiles */
.teacher-wall{display:grid;grid-template-columns:repeat(7,1fr);border-top:1px solid rgba(255,255,255,.14);border-left:1px solid rgba(255,255,255,.14);}
@media (max-width:1100px){.teacher-wall{grid-template-columns:repeat(4,1fr);}}
@media (max-width:640px){.teacher-wall{grid-template-columns:repeat(2,1fr);}}
.tt{border-right:1px solid rgba(255,255,255,.14);border-bottom:1px solid rgba(255,255,255,.14);padding:1.5rem 1.1rem;text-align:center;}
.tt img{width:100%;aspect-ratio:1/1;object-fit:cover;filter:grayscale(.15);margin-bottom:.9rem;}
.tt .tt-region{font-family:var(--sans);font-size:.62rem;letter-spacing:.28em;text-transform:uppercase;color:var(--cream-accent);}
.tt .tt-name{font-family:var(--serif);font-size:1.25rem;margin:.35rem 0 .25rem;color:var(--paper);}
.tt .tt-cred{font-family:var(--sans);font-size:.75rem;color:rgba(251,250,246,.65);}

/* Two-col editorial */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:clamp(2rem,5vw,5rem);align-items:start;}
@media (max-width:900px){.two-col{grid-template-columns:1fr;}}

/* Pricing */
.pricing{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--ink);border-left:1px solid var(--ink);}
@media (max-width:900px){.pricing{grid-template-columns:1fr;}}
.tier{background:var(--paper);border-right:1px solid var(--ink);border-bottom:1px solid var(--ink);padding:2.4rem 1.8rem 2rem;position:relative;}
.tier.featured{border:2px solid var(--green);background:linear-gradient(180deg,var(--paper) 0%,#EFF6F1 100%);}
.tier .tier-badge{position:absolute;top:-13px;left:1.8rem;background:var(--green);color:var(--paper);font-family:var(--sans);font-size:.65rem;letter-spacing:.22em;text-transform:uppercase;padding:.35rem .75rem;font-weight:500;}
.tier-name{font-family:var(--serif);font-size:1.5rem;margin-bottom:.4rem;}
.tier-price{font-family:var(--serif);font-size:3rem;font-weight:600;color:var(--red);line-height:1;margin-bottom:.2rem;}
.tier-price small{font-family:var(--sans);font-size:.75rem;color:var(--ink-2);letter-spacing:.14em;text-transform:uppercase;font-weight:400;margin-left:.35rem;}
.tier-sub{font-family:var(--sans);font-size:.85rem;color:var(--ink-2);margin-bottom:1.4rem;}
.tier ul{list-style:none;padding:0;margin:0 0 1.6rem 0;}
.tier ul li{padding:.55rem 0 .55rem 1.5rem;border-bottom:1px dotted rgba(11,11,13,.14);font-size:.92rem;position:relative;}
.tier ul li::before{content:"✓";position:absolute;left:0;color:var(--green);font-weight:600;}

/* FAQ */
.faq{border-top:1px solid var(--ink);}
.faq details{border-bottom:1px solid rgba(11,11,13,.15);padding:1.4rem 0;}
.faq summary{list-style:none;cursor:pointer;font-family:var(--serif);font-size:1.35rem;font-weight:500;display:flex;justify-content:space-between;align-items:center;color:var(--ink);}
.faq summary::-webkit-details-marker{display:none;}
.faq summary::after{content:"+";font-family:var(--sans);font-size:1.6rem;color:var(--gold);font-weight:300;}
.faq details[open] summary::after{content:"−";}
.faq details p{margin-top:1rem;font-size:1rem;color:var(--ink-2);line-height:1.65;max-width:70ch;}

/* Culture tile grid */
.tiles{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--ink);border-left:1px solid var(--ink);}
@media (max-width:900px){.tiles{grid-template-columns:1fr 1fr;}}
@media (max-width:600px){.tiles{grid-template-columns:1fr;}}
.tile{position:relative;aspect-ratio:1/1;overflow:hidden;border-right:1px solid var(--ink);border-bottom:1px solid var(--ink);}
.tile img{width:100%;height:100%;object-fit:cover;filter:grayscale(.08);transition:transform .5s ease;}
.tile:hover img{transform:scale(1.04);}
.tile .tile-content{position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,11,13,0) 40%,rgba(11,11,13,.75) 100%);padding:1.4rem;display:flex;flex-direction:column;justify-content:flex-end;color:var(--paper);}
.tile .tile-title{font-family:var(--serif);font-style:italic;font-size:1.9rem;line-height:1.05;margin-bottom:.2rem;}
.tile .tile-sub{font-family:var(--sans);font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;color:var(--cream-accent);}

/* Trustpilot review card grid */
.reviews{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(11,11,13,.14);border:1px solid rgba(11,11,13,.14);}
@media (max-width:900px){.reviews{grid-template-columns:1fr 1fr;}}
@media (max-width:600px){.reviews{grid-template-columns:1fr;}}
.review{background:var(--paper);padding:1.6rem;}
.review .stars{color:#F5B93B;letter-spacing:.06em;font-size:.95rem;margin-bottom:.6rem;}
.review .rev-title{font-family:var(--serif);font-size:1.15rem;margin-bottom:.6rem;}
.review .rev-body{font-size:.92rem;color:var(--ink-2);line-height:1.55;margin-bottom:.9rem;}
.review .rev-author{font-family:var(--sans);font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:var(--ink);}

/* Alumni cards */
.alumni{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--ink);border-left:1px solid var(--ink);}
@media (max-width:900px){.alumni{grid-template-columns:1fr;}}
.alum{padding:1.8rem;border-right:1px solid var(--ink);border-bottom:1px solid var(--ink);background:var(--paper);}
.alum img{width:72px;height:72px;border-radius:50%;object-fit:cover;margin-bottom:1rem;}
.alum .quote{font-family:var(--serif);font-style:italic;font-size:1.1rem;line-height:1.4;color:var(--ink);margin-bottom:.9rem;}
.alum .attr{font-family:var(--sans);font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--red);}

/* Sticky bottom enroll bar */
.enroll-bar{position:fixed;bottom:0;left:0;right:0;background:var(--ink);color:var(--paper);padding:.85rem clamp(1rem,3vw,2rem);display:flex;align-items:center;justify-content:space-between;gap:1rem;z-index:80;border-top:1px solid var(--gold-line);transform:translateY(100%);transition:transform .35s ease;}
.enroll-bar.show{transform:translateY(0);}
.enroll-bar .eb-left{font-family:var(--serif);font-style:italic;font-size:1rem;}
.enroll-bar .eb-price{font-family:var(--serif);font-weight:600;color:var(--cream-accent);margin:0 .8rem;}
.enroll-bar .btn{padding:.7rem 1.2rem;font-size:.8rem;}

/* Includes list */
.includes{display:grid;grid-template-columns:1fr 1fr;gap:0 2rem;list-style:none;padding:0;margin:2rem 0 0;}
@media (max-width:700px){.includes{grid-template-columns:1fr;}}
.includes li{padding:.9rem 0 .9rem 1.8rem;border-bottom:1px solid rgba(11,11,13,.1);font-family:var(--sans);font-size:.98rem;position:relative;}
.includes li::before{content:"✓";position:absolute;left:0;color:var(--green);font-weight:600;font-size:1.1rem;}

/* Section head */
.section-head{max-width:820px;margin:0 0 3rem 0;}
.section-head.center{margin:0 auto 3rem;text-align:center;}

/* Utility */
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;}
.grid-4{display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;}
.grid-5{display:grid;grid-template-columns:repeat(5,1fr);gap:1.4rem;}
@media (max-width:900px){.grid-3,.grid-4,.grid-5{grid-template-columns:1fr 1fr;}}
@media (max-width:600px){.grid-3,.grid-4,.grid-5{grid-template-columns:1fr;}}

/* Related courses */
.related{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--ink);border-left:1px solid var(--ink);}
@media (max-width:900px){.related{grid-template-columns:1fr;}}

/* Small badge */
.chip{display:inline-flex;align-items:center;gap:.5rem;padding:.42rem .75rem;background:transparent;border:1px solid var(--gold);color:var(--gold);font-family:var(--sans);font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;}
.chip-green{border-color:var(--green-bright);color:var(--green);background:rgba(30,138,94,.06);}
.chip-red{border-color:var(--red);color:var(--red);background:rgba(199,32,46,.06);}

/* Video bg utility for non-hero sections */
.video-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;opacity:.25;}

/* Nav override (works with existing partial) */
.site-header{background:var(--paper);border-bottom:1px solid rgba(11,11,13,.1);position:sticky;top:0;z-index:70;}
.site-header .nav{display:flex;align-items:center;justify-content:space-between;padding:1rem 0;}
.site-header .nav-menu{display:flex;gap:1.4rem;}
.site-header .nav-link{font-family:var(--sans);font-size:.86rem;color:var(--ink);letter-spacing:.02em;}
.site-header .nav-link:hover{color:var(--red);}
.site-header .lt-main{font-family:var(--serif);font-size:1.5rem;color:var(--red);font-weight:600;}
.site-header .lt-sub{font-family:var(--sans);font-size:.58rem;letter-spacing:.28em;text-transform:uppercase;color:var(--ink-2);display:block;margin-top:2px;}
.site-header .nav-cta{background:var(--green);color:var(--paper);border:0;padding:.7rem 1.2rem;font-family:var(--sans);font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;cursor:pointer;}
.site-header .nav-toggle{display:none;background:transparent;border:0;flex-direction:column;gap:4px;cursor:pointer;padding:.4rem;}
.site-header .nav-toggle span{width:24px;height:2px;background:var(--ink);display:block;}
@media (max-width:900px){.site-header .nav-menu{display:none;}.site-header .nav-toggle{display:flex;}}
.nav-drawer{display:none;}

.site-footer{background:var(--ink);color:var(--paper);padding:4rem 0 2rem;margin-top:0;}
.site-footer a{color:rgba(251,250,246,.7);display:block;padding:.28rem 0;font-size:.88rem;}
.site-footer a:hover{color:var(--cream-accent);}
.site-footer .footer-top{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:2rem;padding-bottom:2.4rem;border-bottom:1px solid rgba(255,255,255,.08);}
@media (max-width:900px){.site-footer .footer-top{grid-template-columns:1fr 1fr;}}
.site-footer h4{font-family:var(--sans);font-size:.74rem;letter-spacing:.24em;text-transform:uppercase;color:var(--cream-accent);margin-bottom:1rem;}
.site-footer p{color:rgba(251,250,246,.72);font-size:.9rem;}
</style>
"""

TOP_STRIP = """<div class="top-strip"><span>Fall Cohort · Enrolment closes Oct 3</span><span class="dot"></span><span>Founder Rate · Save $220 on Annual</span><span class="dot"></span><span>7-Day Money-Back Guarantee</span></div>"""

ENROLL_BAR_JS = """
<script>
(function(){
  var bar=document.querySelector('.enroll-bar');if(!bar)return;
  var shown=false;
  function on(){var y=window.scrollY;if(y>600&&!shown){bar.classList.add('show');shown=true;}else if(y<=400&&shown){bar.classList.remove('show');shown=false;}}
  window.addEventListener('scroll',on,{passive:true});
})();
</script>
"""

def head(title, desc, prefix=""):
    fp = prefix  # e.g. "../../" for pages/courses/
    return f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{fp}css/ci.css">
{INLINE_CRITICAL}
</head><body>
{TOP_STRIP}
{prefix_nav(prefix)}
"""

def prefix_nav(prefix):
    """Adjust href prefixes on nav for subfolder pages."""
    n = NAV
    if prefix:
        # replace hrefs on internal .html links
        def rep(m):
            href = m.group(1)
            if href.startswith("http") or href.startswith("#") or href.startswith(prefix):
                return m.group(0)
            return f'href="{prefix}{href}"'
        n = re.sub(r'href="([^"]+\.html)"', rep, n)
    return n

def foot(prefix=""):
    f = FOOT
    if prefix:
        def rep(m):
            href = m.group(1)
            if href.startswith("http") or href.startswith("#") or href.startswith(prefix):
                return m.group(0)
            return f'href="{prefix}{href}"'
        f = re.sub(r'href="([^"]+\.html)"', rep, f)
    return f + ENROLL_BAR_JS + "\n</body></html>"

# ---- helpers ----

TRUST = '<div class="hero-trust"><span class="stars">★★★★★</span> <strong>4.8</strong> · Trustpilot · 1,284 reviews</div>'

def hero(video, poster, eyebrow, h1_html, sub, ctas_html, live_text="Live class in session · 12 learners"):
    return f"""
<section class="hero">
  <video class="hero-video" autoplay muted loop playsinline poster="{poster}"><source src="{video}" type="video/mp4"></video>
  <div class="hero-scrim"></div>
  {TRUST}
  <div class="hero-live"><span class="live-dot"></span> {live_text}</div>
  <div class="hero-wrap">
    <div class="hero-eyebrow">{eyebrow}</div>
    <h1 class="hero-h1">{h1_html}</h1>
    <p class="hero-sub">{sub}</p>
    <div class="hero-ctas">{ctas_html}</div>
  </div>
</section>
"""

def stats(items, cls=""):
    inner = "".join(f'<div class="stat"><div class="stat-num">{n}</div><div class="stat-lab">{l}</div></div>' for n,l in items)
    return f'<div class="stats {cls}">{inner}</div>'

TEACHERS = [
    ("Chiara","Firenze","DITALS II · Università per Stranieri di Perugia","teacher-chiara.jpg","chiara"),
    ("Marco","Roma","Master FLE · Roma Tre · Certified DITALS","teacher-marco.jpg","marco"),
    ("Giulia","Bologna","DITALS I · Alma Mater Studiorum","teacher-giulia.jpg","giulia"),
    ("Alessandro","Milano","CEDILS · Ca' Foscari · CEFR Examiner","teacher-alessandro.jpg","alessandro"),
    ("Francesca","Venezia","DITALS II · Ca' Foscari","teacher-francesca.jpg","francesca"),
    ("Luca","Napoli","Master FLE · Federico II · DITALS I","teacher-luca.jpg","luca"),
    ("Sofia","Palermo","DITALS II · Università di Palermo","teacher-sofia.jpg","sofia"),
]

def teacher_wall(prefix=""):
    tiles=""
    for name,region,cred,img,slug in TEACHERS:
        tiles += f'<a class="tt" href="{prefix}pages/teachers/{slug}.html"><img src="{prefix}assets/img/{img}" alt="{name}, teacher in {region}"><div class="tt-region">{region}</div><div class="tt-name">{name}</div><div class="tt-cred">{cred}</div></a>'
    return f'<div class="teacher-wall">{tiles}</div>'

def course_card(cid, code, title, cefr, sub, meta, price, prefix=""):
    meta_lines = meta
    href = f"{prefix}pages/{'courses' if cid.startswith('ci') else ('spoken' if cid.startswith('ps') else 'culture')}/{cid}.html"
    meta = "".join(f'<span class="meta-row">{m}</span>' for m in meta_lines)
    return f"""<a class="cc" href="{href}">
  <div class="cc-price">${price}<small>/wk · annual</small></div>
  <div class="cc-badge">{code} · {cefr}</div>
  <h3 class="cc-title">{title}</h3>
  <div class="cc-sub">{sub}</div>
  <div class="cc-meta">{meta}</div>
  <span class="cc-enroll">Reserve My Spot <span class="arrow">→</span></span>
</a>"""

# Course card meta config used across cards
CARDS = {
  "ci1":{"code":"CI 01","title":"Principiante","cefr":"A0 → A1.1","sub":"First Italian, taught from Rome.","meta":["20 lessons × 85 min","Live · 10-12 learners","Marco · Roma","Next: Oct 6"],"price":62},
  "ci2":{"code":"CI 02","title":"Elementare","cefr":"A1.1 → A1.2","sub":"Elementary Italian in Florence.","meta":["20 lessons × 85 min","Live · 10-12 learners","Chiara · Firenze","Next: Oct 8"],"price":62},
  "ci3":{"code":"CI 03","title":"Intermedio","cefr":"A1.2 → A2.1","sub":"Intermediate Italian in Bologna.","meta":["20 lessons × 85 min","Live · 10-12 learners","Giulia · Bologna","Next: Oct 13"],"price":62},
  "ci4":{"code":"CI 04","title":"Avanzato","cefr":"A2.1 → A2.2","sub":"Advanced Italian across Naples and Milan.","meta":["20 lessons × 85 min","Live · 10-12 learners","Luca & Alessandro","Next: Oct 15"],"price":62},
  "ps1":{"code":"PS 01","title":"Al Caffè","cefr":"Spoken A0 → A1","sub":"Say your first sentences aloud.","meta":["20 lessons × 60 min","Live · 6-8 learners","Marco · Roma","Next: Oct 7"],"price":48},
  "ps2":{"code":"PS 02","title":"A Tavola","cefr":"Spoken A1 → A2","sub":"Talk through a Tuscan meal.","meta":["20 lessons × 60 min","Live · 6-8 learners","Chiara · Firenze","Next: Oct 9"],"price":48},
  "ps3":{"code":"PS 03","title":"In Viaggio","cefr":"Spoken A2","sub":"Speak your way across Italy.","meta":["20 lessons × 60 min","Live · 6-8 learners","Francesca · Venezia","Next: Oct 14"],"price":48},
  "ps4":{"code":"PS 04","title":"Chiacchierando","cefr":"Spoken A2 → B1","sub":"Chat like an Italian.","meta":["20 lessons × 60 min","Live · 6-8 learners","Alessandro · Milano","Next: Oct 16"],"price":48},
  "cap-food":{"code":"CAP · Food","title":"La Cucina","cefr":"Any level · English support","sub":"The language of the Italian table.","meta":["6 lessons × 75 min","Live · unlimited seats","Giulia · Bologna","Next: Oct 20"],"price":29},
  "cap-art":{"code":"CAP · Art","title":"L'Arte","cefr":"Any level · English support","sub":"Renaissance in the words that made it.","meta":["6 lessons × 75 min","Live · unlimited seats","Chiara · Firenze","Next: Oct 22"],"price":29},
  "cap-opera":{"code":"CAP · Opera","title":"L'Opera","cefr":"Any level · English support","sub":"Opera as a second language.","meta":["6 lessons × 75 min","Live · unlimited seats","Alessandro · Milano","Next: Oct 24"],"price":29},
}

def all_course_grid(prefix=""):
    order_ci = ["ci1","ci2","ci3","ci4"]
    order_ps = ["ps1","ps2","ps3","ps4"]
    order_cap = ["cap-food","cap-art","cap-opera"]
    out = ['<div class="cg">']
    out.append('<div class="cg-track"><span>Corso Italiano <span style="font-style:normal;color:var(--cream-accent)">· the full CEFR ladder</span></span><span class="track-meta">A0 · A1 · A2 · B1</span></div>')
    for cid in order_ci: out.append(course_card(cid, **CARDS[cid], prefix=prefix))
    out.append('<div class="cg-track"><span>Parliamo Sempre <span style="font-style:normal;color:var(--cream-accent)">· spoken confidence, small circles</span></span><span class="track-meta">Spoken A0 · A1 · A2 · B1</span></div>')
    for cid in order_ps: out.append(course_card(cid, **CARDS[cid], prefix=prefix))
    out.append('<div class="cg-track"><span>Capsule d\'Autore <span style="font-style:normal;color:var(--cream-accent)">· cultural short courses in English + Italian</span></span><span class="track-meta">Any level</span></div>')
    for cid in order_cap: out.append(course_card(cid, **CARDS[cid], prefix=prefix))
    out.append('</div>')
    return "\n".join(out)

# ---- HOMEPAGE ----

def build_home():
    prefix = ""
    h = head("Club Italia by eTeacher · Learn Italian, Live From Italy",
             "Live, culturally immersive Italian courses taught by certified teachers based in Italy. CEFR-aligned, 10 to 12 learners per class, from Rome to Naples.",
             prefix)

    hero_html = hero(
        "assets/video/roma-piazza.mp4",
        "assets/img/hero-poster.jpg",
        "Est. 2016 · Live from Italy · CEFR aligned",
        'Learn Italian,<br><span class="ital">live from Italy.</span>',
        "Twelve people. One teacher standing in Rome. Twenty weeks that take you from ciao to conversation, without leaving your kitchen.",
        '<a href="#pricing" class="btn btn-primary btn-lg">Reserve My Placement Call</a><a href="sample-class.html" class="btn btn-ghost btn-lg">See a Sample Class</a>'
    )

    fold2 = f"""
<section class="section-cream" style="padding:2.2rem 0;">
  <div class="wrap">{stats([
      ("12,847","Learners since 2016"),
      ("★ 4.8","1,284 Trustpilot reviews"),
      ("CEFR","Aligned A0 → B2"),
      ("#1","US Italian school · 2026"),
  ])}</div>
</section>
"""

    fold3 = f"""
<section class="section-black">
  <div class="wrap">
    <div class="section-eyebrow">The Classroom</div>
    <div class="two-col" style="align-items:center;">
      <div class="zoom-frame"><img src="assets/img/zoom-mockup.svg" alt="A Club Italia live Zoom classroom, ten learners on screen with teacher Marco in Rome"></div>
      <div>
        <h2 class="h-display">This is a real Club Italia <span class="ital">classroom.</span></h2>
        <p class="lede">Twelve seats. One teacher standing in an Italian city. No app, no green owl, no video that pauses when you look away. You show up on Monday at 7pm ET and the door opens on Rome.</p>
      </div>
    </div>
  </div>
</section>
"""

    fold4 = f"""
<section class="section-white">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">The Course Catalogue</div>
      <h2 class="h-display">Eleven courses, one <span class="ital">ladder.</span></h2>
      <p class="lede">Every course is CEFR-aligned, taught live from Italy, and capped at twelve learners. Start where you are; graduate to the next level, or step across into a spoken circle or a cultural capsule when the mood strikes.</p>
    </div>
  </div>
  {all_course_grid()}
</section>
"""

    fold5 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="two-col">
      <div>
        <div class="section-eyebrow">The problem</div>
        <h2 class="h-display" style="color:var(--red)"><em>Duolingo will not get you to fluent.</em></h2>
        <p class="lede">Streaks, gems and cartoon owls train you to open an app. They do not train you to answer when an Italian looks at you across a table and asks a real question. That is a skill, and it only grows when a human being on the other side of the screen expects you to speak.</p>
      </div>
      <div>
        <div class="section-eyebrow">The Club Italia way</div>
        <h2 class="h-display" style="color:var(--green)"><em>Live from Italy. Ten to twelve. CEFR certified.</em></h2>
        <p class="lede">A single teacher, a small circle of adult learners, and twenty structured weeks aligned to the Common European Framework. You leave every lesson having spoken. You leave every level with a certificate that means something.</p>
      </div>
    </div>
  </div>
</section>
"""

    fold6 = f"""
<section class="section-white">
  <div class="wrap">
    <div class="section-head center">
      <div class="section-eyebrow">How it works</div>
      <h2 class="h-display">Five steps, twenty <span class="ital">weeks.</span></h2>
    </div>
    <div class="grid-5">
      {"".join(f'''<figure style="margin:0;">
        <div class="browser-frame"><img src="assets/img/screen-{s}.svg" alt="Step {i}: {t}"></div>
        <figcaption style="margin-top:1rem;"><div class="section-eyebrow" style="font-size:.62rem;margin-bottom:.35rem;">Step {i:02d}</div><div style="font-family:var(--serif);font-size:1.25rem;font-style:italic;">{t}</div><p style="font-size:.9rem;color:var(--ink-2);margin-top:.4rem;">{d}</p></figcaption>
      </figure>''' for i,(s,t,d) in enumerate([
          ("placement","Placement","A 20-minute call with a Club Italia advisor. We hear you speak, then we place you on the CEFR ladder."),
          ("platform","Your dashboard","Every lesson, every recording, every homework thread lives in one dashboard you open in a browser."),
          ("liveclass","Live from Italy","Monday and Thursday evenings, US time. Twelve seats. One teacher standing in an Italian city."),
          ("biagio","Biagio, on demand","Between classes, our AI tutor Biagio corrects your writing and drills your grammar in Italian."),
          ("certificate","Certificate","At the end of each level you sit an oral assessment. A signed, CEFR-aligned certificate follows."),
      ],1))}
    </div>
  </div>
</section>
"""

    fold7 = f"""
<section class="section-green">
  <div class="wrap">
    <div class="section-eyebrow">The Cultural Method</div>
    <h2 class="h-display">Language is a way of being <span class="ital">Italian.</span></h2>
    <div class="grid-4" style="margin-top:3rem;">
      {"".join(f'<div style="border-top:1px solid rgba(230,201,155,.35);padding:1.6rem 1.2rem 0;"><div style="font-family:var(--serif);font-size:3rem;color:var(--cream-accent);">{i:02d}</div><h3 style="font-family:var(--serif);font-size:1.5rem;margin:.4rem 0 .6rem;color:var(--paper);">{t}</h3><p style="font-size:.95rem;color:rgba(251,250,246,.78);line-height:1.55;">{d}</p></div>' for i,(t,d) in enumerate([
        ("City-anchored","Every level is set in a specific Italian city. Rome for beginners; Florence for A1; Bologna for A2; Naples for B1. The city teaches the register."),
        ("Human first","Grammar lives inside dialogue. We do not conjugate verbs on a chart until a real Italian has already used them in front of you."),
        ("CEFR structured","Every syllabus follows the 2020 Companion Volume of the Common European Framework. Every certificate references the descriptor you passed."),
        ("Small by design","No class over twelve learners. No lesson recorded and left. Your teacher knows your name, your work, and the sentence you tripped on last week."),
      ],1))}
    </div>
  </div>
</section>
"""

    fold8 = f"""
<section class="section-black">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">Your Teachers</div>
      <h2 class="h-display">Seven certified teachers,<br>each in <span class="ital">their own city.</span></h2>
    </div>
  </div>
  {teacher_wall()}
</section>
"""

    fold9 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="two-col" style="align-items:center;">
      <div>
        <div class="section-eyebrow">The Dashboard</div>
        <h2 class="h-display">Everything runs in your <span class="ital">browser.</span></h2>
        <p class="lede">One tab. Your calendar of live classes, every recording, homework threads with your teacher, your progress on the CEFR ladder, and Biagio, our AI tutor, always ready to correct a sentence.</p>
        <ul class="includes" style="margin-top:2rem;">
          <li>Live class calendar and recordings</li>
          <li>Homework threads with your teacher</li>
          <li>CEFR progress tracking</li>
          <li>Downloadable syllabus and PDFs</li>
          <li>Biagio AI tutor, 24/7</li>
          <li>Peer chat within your cohort</li>
        </ul>
      </div>
      <div class="browser-frame"><div class="browser-chrome"><span></span><span></span><span></span><span class="url">clubitalia.eteacher.com/dashboard</span></div><img src="assets/img/dashboard-mockup.svg" alt="Club Italia student dashboard mockup"></div>
    </div>
  </div>
</section>
"""

    fold10 = f"""
<section class="section-red">
  <div class="wrap">
    <div class="two-col" style="align-items:center;">
      <div>
        <div class="section-eyebrow">Meet Biagio</div>
        <h2 class="h-display">Between classes,<br>Italian <span class="ital">on demand.</span></h2>
        <p class="lede">Biagio is our in-house AI tutor. Trained on the Club Italia syllabus, corrective on your exact grammar gaps, and always in Italian. Ask a question at midnight in Chicago; get the answer in three seconds, with the CEFR descriptor you just practiced.</p>
        <div style="margin-top:2rem;"><a href="biagio.html" class="btn btn-ghost btn-lg">See Biagio in action</a></div>
      </div>
      <div class="zoom-frame"><img src="assets/img/screen-biagio.svg" alt="Chat with Biagio, the Club Italia AI tutor"></div>
    </div>
  </div>
</section>
"""

    reviews = [
      ("Beyond anything I tried before","I did six months of Duolingo. Two lessons with Marco in Rome and I understood more of a real conversation than I did in a year of the app.","Emily R. · Chicago"),
      ("The teacher makes it","Chiara stops and corrects the exact word you got wrong. It feels like a real class, because it is a real class.","David M. · Austin"),
      ("Small enough to be seen","Twelve of us. Everyone talks every lesson. I have never had that in a language class before.","Rachel S. · New York"),
      ("Culture, not just grammar","The Rome anchor made the whole course feel like a place, not a textbook.","John P. · Denver"),
      ("A certificate that means something","I put the CEFR A2 certificate on my LinkedIn and my Italian client asked me a question in Italian on the next call. I answered.","Maria G. · Miami"),
      ("Worth every dollar","I priced Berlitz. I looked at Rosetta Stone. This is a proper school, not an app, and it costs less.","Thomas W. · Seattle"),
    ]
    fold11 = f"""
<section class="section-white">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">Trustpilot · ★ 4.8 · 1,284 reviews</div>
      <h2 class="h-display">Real learners, real <span class="ital">Italian.</span></h2>
    </div>
    <div class="reviews">
      {"".join(f'<div class="review"><div class="stars">★★★★★</div><div class="rev-title">{t}</div><p class="rev-body">{b}</p><div class="rev-author">{a}</div></div>' for t,b,a in reviews)}
    </div>
  </div>
</section>
"""

    fold12 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="two-col" style="align-items:center;">
      <div class="cert-frame"><img src="assets/img/certificate-mockup.svg" alt="Sample Club Italia CEFR-aligned certificate"></div>
      <div>
        <div class="section-eyebrow">The Certificate</div>
        <h2 class="h-display">A CEFR-aligned certificate,<br>signed and <span class="ital">dated.</span></h2>
        <p class="lede">On successful completion of each level, the learner will be able to:</p>
        <ol class="outcomes">
          <li>Introduce themselves, family and work in Italian at the CEFR descriptor level attained.</li>
          <li>Understand slow, clearly-articulated Italian on familiar topics.</li>
          <li>Handle a short, structured exchange in a shop, café or ticket office.</li>
          <li>Write a short, coherent text on a familiar topic using the target grammar.</li>
          <li>Read and extract the main idea from a short authentic Italian source.</li>
        </ol>
      </div>
    </div>
  </div>
</section>
"""

    fold13 = f"""
<section id="pricing" class="section-white">
  <div class="wrap">
    <div class="section-head center">
      <div class="section-eyebrow">Tuition</div>
      <h2 class="h-display">One tuition, three <span class="ital">rhythms.</span></h2>
      <p class="lede" style="margin:0 auto;">Every plan includes the full live-class programme, the dashboard, Biagio, and the CEFR-aligned certificate. Only the payment rhythm changes.</p>
    </div>
    <div class="pricing">
      <div class="tier">
        <div class="tier-name">Monthly</div>
        <div class="tier-price">$84<small>/wk</small></div>
        <div class="tier-sub">Billed $364 per month. No annual commitment.</div>
        <ul>
          <li>All live classes at your level</li>
          <li>Full dashboard, recordings, PDFs</li>
          <li>Biagio, AI tutor, 24/7</li>
          <li>CEFR certificate on completion</li>
          <li>Cancel any time after month one</li>
        </ul>
        <a href="#lead" class="btn btn-ghost-dark btn-lg" style="width:100%;justify-content:center;">Choose Monthly</a>
      </div>
      <div class="tier featured">
        <div class="tier-badge">Best value · Save $440</div>
        <div class="tier-name">Annual</div>
        <div class="tier-price">$62<small>/wk</small></div>
        <div class="tier-sub">Billed $3,224 once per year. Locked founder rate.</div>
        <ul>
          <li>Everything in Monthly</li>
          <li>Free level upgrade mid-year if you finish early</li>
          <li>Two capsule courses (La Cucina + L'Arte) included</li>
          <li>Priority placement into the next cohort</li>
          <li>Founder-rate locked for life</li>
        </ul>
        <a href="#lead" class="btn btn-primary btn-lg" style="width:100%;justify-content:center;">Reserve Annual</a>
      </div>
      <div class="tier">
        <div class="tier-name">Term (4 mo.)</div>
        <div class="tier-price">$73<small>/wk</small></div>
        <div class="tier-sub">Billed $1,169 per term. One CEFR level.</div>
        <ul>
          <li>Everything in Monthly</li>
          <li>One full CEFR level (20 live lessons)</li>
          <li>Certificate on completion</li>
          <li>Upgrade credit toward Annual within 30 days</li>
        </ul>
        <a href="#lead" class="btn btn-ghost-dark btn-lg" style="width:100%;justify-content:center;">Choose Term</a>
      </div>
    </div>
  </div>
</section>
"""

    fold14 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="two-col" style="align-items:center;">
      <div style="text-align:center;">
        <img src="assets/img/guarantee-badge.svg" alt="7-day money-back guarantee" style="max-width:180px;margin:0 auto;">
      </div>
      <div>
        <div class="section-eyebrow">Guarantee & payment</div>
        <h2 class="h-display">Seven days,<br>your money <span class="ital">back.</span></h2>
        <p class="lede">If your first live class is not the school we describe, tell your advisor within seven days and we return the full tuition. No form, no argument.</p>
        <div style="margin-top:2rem;"><img src="assets/img/paymethods.svg" alt="Accepted payment methods" style="max-width:340px;"></div>
      </div>
    </div>
  </div>
</section>
"""

    pillars = [
      ("food","La Cucina","The Italian Table"),
      ("art","L'Arte","Renaissance & Baroque"),
      ("opera","L'Opera","La Scala to Verona"),
      ("cinema","Il Cinema","Neorealism to Sorrentino"),
      ("tradition","La Tradizione","Festa, family, Ferragosto"),
      ("travel","Il Viaggio","City by city, region by region"),
    ]
    fold15 = f"""
<section class="section-white">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">Culture Library</div>
      <h2 class="h-display">Six pillars of <span class="ital">italianità.</span></h2>
    </div>
  </div>
  <div class="tiles">
    {"".join(f'<a class="tile" href="pages/culture/pillar-{s}.html"><img src="assets/img/pillar-{s}.jpg" alt="{t}"><div class="tile-content"><div class="tile-sub">{sub}</div><div class="tile-title">{t}</div></div></a>' for s,t,sub in pillars)}
  </div>
</section>
"""

    faqs = [
      ("Is this a real school or a course platform?","Club Italia by eTeacher is a live school. Every class is taught by a certified Italian teacher, from Italy, at a set time. There are no pre-recorded 'watch when you want' lessons in the CI programme."),
      ("Which CEFR levels do you cover?","The Corso Italiano ladder runs from A0 (absolute beginner) through B1. The Parliamo Sempre spoken track covers A0 through B1. Capsules are level-independent with English support."),
      ("How large is a class?","Corso Italiano classes are capped at twelve learners; Parliamo Sempre spoken circles at eight; capsules run open-audience."),
      ("Where do the teachers live?","In Italy. Every teacher on staff lives and works in the Italian city that anchors their course."),
      ("What if I miss a class?","Every live class is recorded to your dashboard. Your teacher will also flag anything the recording cannot cover in your weekly homework thread."),
      ("Do you issue a certificate?","Yes. On successful completion of each CEFR level you sit an oral assessment. A signed, CEFR-aligned certificate is issued within seven days."),
      ("Is Club Italia the same as eTeacher Group?","Club Italia is the Italian language school built by eTeacher Group, the online-schools operator that has taught Hebrew, Yiddish, Spanish and Arabic to over four hundred thousand learners since 2000."),
      ("Do you offer a payment plan?","Yes. The Monthly plan is a rolling month-to-month billing; the Term plan covers one full CEFR level; the Annual plan is our best rate."),
      ("Do you accept international students?","Yes. Roughly forty per cent of our student body is outside the United States, joining live from the UK, Australia, Brazil and Israel."),
      ("What happens if I'm not sure of my level?","Every applicant sits a 20-minute placement call with a Club Italia advisor. We place you on the CEFR ladder before you enrol; no self-assessment, no guessing."),
    ]
    fold16 = f"""
<section class="section-white" style="border-top:1px solid rgba(11,11,13,.1);">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">Questions, answered</div>
      <h2 class="h-display">Frequently <span class="ital">asked.</span></h2>
    </div>
    <div class="faq">
      {"".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)}
    </div>
  </div>
</section>
"""

    fold17 = f"""
<section id="lead" class="section-green">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">Reserve your placement call</div>
      <h2 class="h-display">Speak with a Club Italia<br>advisor <span class="ital">this week.</span></h2>
      <p class="lede">Twenty minutes. We hear you speak, we place you on the CEFR ladder, we send a written recommendation and a spot in the next cohort. No card required.</p>
    </div>
    <form style="display:grid;grid-template-columns:repeat(4,1fr);gap:.6rem;max-width:940px;">
      <input type="text" placeholder="First name" style="padding:1rem 1.1rem;border:0;font-family:var(--sans);font-size:.95rem;background:var(--paper);color:var(--ink);">
      <input type="email" placeholder="Email address" style="padding:1rem 1.1rem;border:0;font-family:var(--sans);font-size:.95rem;background:var(--paper);color:var(--ink);">
      <select style="padding:1rem 1.1rem;border:0;font-family:var(--sans);font-size:.95rem;background:var(--paper);color:var(--ink);">
        <option>My current level…</option><option>Absolute beginner</option><option>A little (A1)</option><option>Conversational (A2)</option><option>Advanced (B1+)</option>
      </select>
      <button type="submit" class="btn" style="background:var(--ink);color:var(--paper);border:0;font-size:.85rem;">Book My Call →</button>
    </form>
  </div>
</section>
"""

    body = h + hero_html + fold2 + fold3 + fold4 + fold5 + fold6 + fold7 + fold8 + fold9 + fold10 + fold11 + fold12 + fold13 + fold14 + fold15 + fold16 + fold17 + foot(prefix)
    (ROOT/"index.html").write_text(body)
    return 17  # fold count (hero + 16 below-fold + footer)

# ---- COURSE PAGE (15 folds) ----

# Teacher assignments per course
COURSE_TEACHER = {
  "ci1":"marco","ci2":"chiara","ci3":"giulia","ci4":"luca",
  "ps1":"marco","ps2":"chiara","ps3":"francesca","ps4":"alessandro",
  "cap-food":"giulia","cap-art":"chiara","cap-opera":"alessandro",
}
COURSE_VIDEO = {
  "ci1":"roma-piazza","ci2":"firenze-arno","ci3":"bologna-portici","ci4":"napoli-mare",
  "ps1":"roma-piazza","ps2":"firenze-arno","ps3":"venezia-canal","ps4":"bologna-portici",
  "cap-food":"cucina-pasta","cap-art":"opera-scala","cap-opera":"opera-scala",
}
COURSE_CITY_IMG = {
  "ci1":"city-roma","ci2":"city-firenze","ci3":"city-bologna","ci4":"city-napoli",
  "ps1":"city-roma","ps2":"city-firenze","ps3":"city-venezia","ps4":"city-bologna",
  "cap-food":"city-bologna","cap-art":"city-firenze","cap-opera":"city-milano",
}
TEACHER_MAP = {t[4]:t for t in TEACHERS}
COURSE_CODE = {
  "ci1":"CI-01","ci2":"CI-02","ci3":"CI-03","ci4":"CI-04",
  "ps1":"PS-01","ps2":"PS-02","ps3":"PS-03","ps4":"PS-04",
  "cap-food":"CAP-FD","cap-art":"CAP-AR","cap-opera":"CAP-OP",
}
COURSE_PRICES = {
  "ci":(84,73,62,3224,440),  # (monthly $/wk, term $/wk, annual $/wk, annual $, savings)
  "ps":(64,55,48,2496,332),
  "cap":(39,33,29,899,120),
}

SIBLING_MAP = {
  "ci1":["ci2","ps1","cap-food"],
  "ci2":["ci1","ci3","ps2"],
  "ci3":["ci2","ci4","ps3"],
  "ci4":["ci3","ps4","cap-opera"],
  "ps1":["ci1","ps2","cap-food"],
  "ps2":["ci2","ps3","cap-food"],
  "ps3":["ci3","ps4","cap-art"],
  "ps4":["ci4","ps3","cap-opera"],
  "cap-food":["cap-art","ci1","ps2"],
  "cap-art":["cap-food","ci2","ps3"],
  "cap-opera":["cap-art","ci4","ps4"],
}

ALUMNI_QUOTES = [
  ("Ellen G.","New York","student-ellen","She corrected the exact preposition I had been getting wrong for a year, in the middle of the third lesson. That is why this course works."),
  ("James D.","Los Angeles","student-james","I flew to Rome the week after CI-01 finished and understood the barista. Not a lot. Enough."),
  ("Priya K.","Boston","student-priya","The syllabus is honest. You learn twenty things, not two thousand, and you learn them well enough to use."),
]

def course_page(cid):
    d = DATA[cid]
    prefix = "../../"
    teacher = TEACHER_MAP[COURSE_TEACHER[cid]]
    tname, tregion, tcred, timg, tslug = teacher
    video = COURSE_VIDEO[cid]
    cityimg = COURSE_CITY_IMG[cid]
    code = COURSE_CODE[cid]
    family = "ci" if cid.startswith("ci") else ("ps" if cid.startswith("ps") else "cap")
    p_month, p_term, p_annual, p_annual_full, p_save = COURSE_PRICES[family]
    is_capsule = family=="cap"
    total_lessons = len(d["syllabus"])
    lesson_minutes = 85 if family=="ci" else (60 if family=="ps" else 75)
    contact_hours = round(total_lessons*lesson_minutes/60,1)

    title = f"{d['title']} · {code} · Club Italia by eTeacher"
    desc = f"{d['title']}: {d['cefr']} live from {d['city']}. {total_lessons} lessons, {contact_hours} contact hours, CEFR-aligned."

    h = head(title, desc, prefix)

    # 1) HERO
    hero_html = hero(
        f"{prefix}assets/video/{video}.mp4",
        f"{prefix}assets/img/course-{cid}.jpg" if not is_capsule else f"{prefix}assets/img/{cid}.jpg",
        f"Course {code} · {d['tag']}",
        f'{d["title"]}<br><span class="ital">live from {d["city"]}.</span>',
        d["promise"],
        f'<a href="#pricing" class="btn btn-primary btn-lg">Reserve My Spot</a><a href="{prefix}pdf/{cid}-syllabus.pdf" class="btn btn-red btn-lg">Download Syllabus (PDF)</a>',
        f"Live cohort in session · {12 if family=='ci' else (8 if family=='ps' else 22)} learners"
    )

    # 2) TRUST STRIP
    fold2 = f"""
<section class="section-cream" style="padding:1.8rem 0;">
  <div class="wrap">{stats([
    ("★ 4.8", "1,284 Trustpilot reviews"),
    ("347", "alumni completed this course"),
    ("Oct 6", "next start · seats open"),
    (f"{contact_hours}h", "live contact time"),
  ])}</div>
</section>
"""

    # 3) COURSE AT A GLANCE
    fold3 = f"""
<section class="section-white">
  <div class="wrap">
    <div class="two-col">
      <div>
        <div class="section-eyebrow">Course at a Glance</div>
        <h2 class="h-display">{d["title"]} · <span class="ital">course card.</span></h2>
        <p class="lede">This course is designed for adult learners approaching Italian at the {d["cefr"]} band of the Common European Framework of Reference for Languages. Instruction is live, in Italian, with English support on demand, and follows the communicative-competence model outlined in the 2020 Companion Volume.</p>
      </div>
      <div>
        <table class="glance">
          <tr><td>Course code</td><td>{code}</td></tr>
          <tr><td>CEFR level</td><td>{d["cefr"]}</td></tr>
          <tr><td>Duration</td><td>{'20 weeks · one live class per week' if not is_capsule else '6 weeks · one live class per week'}</td></tr>
          <tr><td>Total contact hours</td><td>{contact_hours} hours</td></tr>
          <tr><td>Recommended study hours</td><td>{'40 – 60 hours over the course' if not is_capsule else '10 – 15 hours over the course'}</td></tr>
          <tr><td>Class size</td><td>{'Capped at 12 learners' if family=='ci' else ('Capped at 8 learners' if family=='ps' else 'Open cohort · up to 40 learners')}</td></tr>
          <tr><td>Format</td><td>Live online · weekly · via Club Italia dashboard</td></tr>
          <tr><td>Language of instruction</td><td>Italian, with English support on demand</td></tr>
          <tr><td>City anchor</td><td>{d["city"]}</td></tr>
          <tr><td>Signature teacher</td><td>{tname}, {tregion}</td></tr>
          <tr><td>Certification</td><td>Club Italia by eTeacher · CEFR-aligned certificate</td></tr>
          <tr><td>Materials</td><td>Included in tuition · downloadable PDFs</td></tr>
        </table>
      </div>
    </div>
  </div>
</section>
"""

    # 4) LEARNING OUTCOMES
    outcomes_li = "".join(f"<li>{o}.</li>" if not o.endswith('.') else f"<li>{o}</li>" for o in d["outcomes"])
    fold4 = f"""
<section class="section-cream">
  <div class="wrap-narrow">
    <div class="section-eyebrow">Learning Outcomes</div>
    <h2 class="h-display">On successful completion,<br>the learner will be <span class="ital">able to.</span></h2>
    <p class="lede">The following outcomes reference the CEFR descriptors for the {d["cefr"]} band and constitute the assessed criteria for course completion.</p>
    <ol class="outcomes">
      {outcomes_li}
    </ol>
  </div>
</section>
"""

    # 5) SYLLABUS TABLE
    rows = ""
    for i,(topic, gram) in enumerate(d["syllabus"],1):
        # split gram at first period into grammar/vocab and cultural setting
        parts = gram.rsplit(". ",1)
        if len(parts)==2 and len(parts[1])<120:
            grammar, cultural = parts[0].rstrip('.') + ".", parts[1].rstrip('.')
        else:
            grammar, cultural = gram, ""
        rows += f'<tr><td class="lesson-num">{i:02d}</td><td class="topic">{topic}</td><td class="grammar">{grammar}</td><td class="culture">{cultural}</td></tr>'
    fold5 = f"""
<section class="section-white">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">The Syllabus</div>
      <h2 class="h-display">{total_lessons} lessons, {contact_hours} contact hours,<br>from {d['city']} to <span class="ital">CEFR {d["cefr"].split(' → ')[-1]}.</span></h2>
      <p class="lede">Every lesson is set in a specific Italian place. Every lesson introduces a defined grammar unit and a defined vocabulary field. Every lesson finishes with fifteen minutes of open conversation, in Italian, with your teacher.</p>
      <p style="margin-top:1rem;"><a href="{prefix}pdf/{cid}-syllabus.pdf" style="color:var(--gold);border-bottom:1px solid var(--gold-line);padding-bottom:2px;font-family:var(--sans);font-size:.9rem;letter-spacing:.02em;">Download the complete syllabus (12-page PDF, 218KB) →</a></p>
    </div>
    <div style="overflow-x:auto;">
    <table class="syllabus-table">
      <thead><tr><th style="width:70px;">Lesson</th><th>Topic</th><th>Grammar & Vocabulary</th><th>Cultural Setting</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
    </div>
  </div>
</section>
"""

    # 6) CULTURAL CONTEXT
    context_titles = {
      "ci1":"Rome, where the language began.",
      "ci2":"Florence, where Italian was written.",
      "ci3":"Bologna, where the university invented the seminar.",
      "ci4":"Naples and Milan, the two poles of contemporary Italian.",
      "ps1":"Rome, at the café bar.",
      "ps2":"Tuscany, at the trattoria table.",
      "ps3":"Venice and the road, in transit across Italy.",
      "ps4":"Everywhere Italians talk over each other.",
      "cap-food":"The Italian table, region by region.",
      "cap-art":"Florence and Rome, the two Renaissance capitals.",
      "cap-opera":"La Scala, and the language of the libretto.",
    }
    context_body = {
      "ci1":"The Italian language is a Roman language, and Rome is where its everyday register lives. When you learn to greet, to order, to ask for directions in Roman Italian, you are learning the register that anchors every regional variety of the modern language. Marco lives and teaches in the Prati district; every dialogue in CI-01 is set in a Roman place he could walk to.",
      "ci2":"The literary Italian of Dante, Petrarch and Boccaccio is a Florentine Italian, and the Italian A1 register is the one closest to that written norm. Chiara teaches from a studio in Oltrarno; every lesson in CI-02 draws on the Florentine A1 register that has been the backbone of standard Italian since the fourteenth century.",
      "ci3":"Bologna hosts the oldest university in continuous operation in the Western world, and Bolognese Italian carries a particular formality that suits the intermediate register. Giulia teaches from a studio a short walk from Piazza Maggiore; every lesson in CI-03 is set in the arcaded streets that made the city famous.",
      "ci4":"To move from A2 to B1 you have to hold your ground against real Italians talking at real speed. Naples and Milan are the two poles of contemporary spoken Italian: one southern, warm, elastic; one northern, quick, business-first. Luca teaches from Vomero; Alessandro co-teaches from Brera. CI-04 is deliberately taught by both.",
      "ps1":"Spoken Italian at A0 is a café Italian. You order, you thank, you ask a question, you understand a short answer. Rome is the natural anchor for that register: the espresso ritual is a working laboratory for the first hundred sentences of your Italian life.",
      "ps2":"By A1 spoken you can hold a table. You can order, you can discuss the food in front of you, you can ask a follow-up. Tuscan trattorie are the natural home of that register: small, family-run, and forgiving of the learner who tries.",
      "ps3":"A2 spoken Italian is a travel Italian. You can move across the country and be understood: on the train, in the hotel, at the ticket window. Francesca teaches from Cannaregio in Venice; every PS-03 lesson is set in an Italian in-transit place.",
      "ps4":"Spoken B1 is the point at which you begin to speak like Italians speak: over each other, in fragments, with warmth. Alessandro teaches from Milan; every PS-04 lesson pushes you toward the register you actually hear on an Italian street.",
      "cap-food":"Italian food language is a regional map. Every dish is a place; every place is a dialect; every dialect is a slightly different Italian. Giulia teaches from Bologna, the acknowledged capital of Italian cuisine, and every lesson is a short essay in one regional table.",
      "cap-art":"The Renaissance was written in Italian, and to read Vasari, Alberti, and the letters of Michelangelo you need the vocabulary of the workshop as much as the vocabulary of the museum. Chiara teaches this capsule from Florence.",
      "cap-opera":"Opera is a second Italian: elevated, archaic, sung. Alessandro teaches this capsule from Milan, the city of La Scala, and every lesson unpacks one libretto against the modern Italian equivalent.",
    }
    fold6 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="two-col" style="align-items:center;">
      <div>
        <div class="section-eyebrow">Cultural Context</div>
        <h2 class="h-display">{context_titles[cid].replace(',',',<br>').replace('.','.').split('<br>')[0]},<br><span class="ital">{context_titles[cid].split(', ',1)[1] if ', ' in context_titles[cid] else ''}</span></h2>
        <p class="lede">{context_body[cid]}</p>
      </div>
      <img src="{prefix}assets/img/{cityimg}.jpg" alt="{d['city']}" style="width:100%;filter:grayscale(.1);">
    </div>
  </div>
</section>
"""

    # 7) ZOOM CLASSROOM
    fold7 = f"""
<section class="section-black">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">The Live Classroom</div>
      <h2 class="h-display">Your Monday 7pm ET class<br>with <span class="ital">{tname}.</span></h2>
    </div>
    <div class="zoom-frame"><img src="{prefix}assets/img/zoom-mockup-2.svg" alt="A live Club Italia class with {tname} teaching from {tregion}"></div>
  </div>
</section>
"""

    # 8) TEACHER
    fold8 = f"""
<section class="section-white">
  <div class="wrap">
    <div class="two-col" style="align-items:center;">
      <img src="{prefix}assets/img/{timg}" alt="{tname}, signature teacher of {d['title']}, based in {tregion}" style="width:100%;filter:grayscale(.1);">
      <div>
        <div class="section-eyebrow">{tregion}</div>
        <h2 class="h-display" style="font-size:clamp(2.4rem,4.5vw,3.6rem);">{tname},<br>signature teacher, <span class="ital">{d["title"]}.</span></h2>
        <p style="font-size:1.1rem;line-height:1.6;color:var(--ink);">{tname} was trained in the {tcred.split(' · ')[1] if ' · ' in tcred else 'Italian university system'} and has taught adult learners at Club Italia since 2019. Before joining the school, {tname.split()[0]} taught in-country for the {tregion} branch of the Società Dante Alighieri, the national network of Italian cultural institutes, and served as an examiner for the CELI proficiency examinations issued by the Università per Stranieri di Perugia.</p>
        <p style="font-size:1.1rem;line-height:1.6;color:var(--ink);">In the classroom, {tname.split()[0]} works on the principle that grammar lives inside dialogue. Every unit is opened by a real recorded exchange between Italians; the grammar point that governs it is drawn out only after learners have already tried the exchange themselves. This is the Club Italia house method and {tname.split()[0]} has been one of its early architects.</p>
        <p style="font-size:1.1rem;line-height:1.6;color:var(--ink);">Outside of teaching, {tname.split()[0]} writes for the Club Italia culture library on the language of {tregion} and its region.</p>
        <div style="margin-top:1.4rem;display:flex;flex-wrap:wrap;gap:.6rem;">
          {"".join(f'<span class="chip">{c}</span>' for c in tcred.split(' · '))}
        </div>
        <div style="margin-top:2rem;"><a href="{prefix}pages/teachers/{tslug}.html" class="btn btn-ghost-dark">Read {tname}'s full profile</a></div>
      </div>
    </div>
  </div>
</section>
"""

    # 9) THE PLATFORM
    fold9 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="two-col" style="align-items:center;">
      <div class="browser-frame"><div class="browser-chrome"><span></span><span></span><span></span><span class="url">clubitalia.eteacher.com/dashboard</span></div><img src="{prefix}assets/img/dashboard-mockup.svg" alt="Club Italia dashboard"></div>
      <div>
        <div class="section-eyebrow">The Platform</div>
        <h2 class="h-display">Everything runs in<br>your <span class="ital">browser.</span></h2>
        <p class="lede">Every live class, every recording, every homework thread, every PDF and every conversation with Biagio lives inside a single dashboard you open in Chrome, Safari or Firefox. No downloads. No app.</p>
        <ul class="includes">
          <li>Live class calendar and one-click join</li>
          <li>Recording of every lesson within 30 minutes</li>
          <li>Homework threads with your teacher</li>
          <li>Biagio AI tutor, on demand, in Italian</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

    # 10) ALUMNI OUTCOMES
    alum_cards = "".join(f'''
      <div class="alum">
        <div class="quote">“{q}”</div>
        <div class="attr">{n} · {c} · {code} alumna</div>
      </div>''' for n,c,_,q in ALUMNI_QUOTES)
    fold10 = f"""
<section class="section-white">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">Student Outcomes</div>
      <h2 class="h-display">347 alumni have completed<br>{code} <span class="ital">since 2019.</span></h2>
    </div>
  </div>
  <div class="alumni">{alum_cards}</div>
</section>
"""

    # 11) PRICING for this course
    fold11 = f"""
<section id="pricing" class="section-cream">
  <div class="wrap">
    <div class="section-head center">
      <div class="section-eyebrow">Tuition · {code}</div>
      <h2 class="h-display">One tuition, three <span class="ital">rhythms.</span></h2>
    </div>
    <div class="pricing">
      <div class="tier">
        <div class="tier-name">Monthly</div>
        <div class="tier-price">${p_month}<small>/wk</small></div>
        <div class="tier-sub">Rolling month-to-month billing.</div>
        <ul>
          <li>All {total_lessons} live lessons at your pace</li>
          <li>Recordings, PDFs, Biagio access</li>
          <li>CEFR-aligned certificate on completion</li>
          <li>Cancel any time after month one</li>
        </ul>
        <a href="#final" class="btn btn-ghost-dark btn-lg" style="width:100%;justify-content:center;">Choose Monthly</a>
      </div>
      <div class="tier featured">
        <div class="tier-badge">Best value · Save ${p_save}</div>
        <div class="tier-name">Annual</div>
        <div class="tier-price">${p_annual}<small>/wk</small></div>
        <div class="tier-sub">Billed ${p_annual_full:,} once per year.</div>
        <ul>
          <li>Everything in Monthly</li>
          <li>Free upgrade to the next level when you finish {code}</li>
          <li>Two cultural capsules included</li>
          <li>Priority placement into the next cohort</li>
          <li>Founder rate locked for life</li>
        </ul>
        <a href="#final" class="btn btn-primary btn-lg" style="width:100%;justify-content:center;">Reserve Annual</a>
      </div>
      <div class="tier">
        <div class="tier-name">Term (one level)</div>
        <div class="tier-price">${p_term}<small>/wk</small></div>
        <div class="tier-sub">One full CEFR level, paid upfront.</div>
        <ul>
          <li>All {total_lessons} live lessons</li>
          <li>Certificate on completion</li>
          <li>Upgrade credit toward Annual within 30 days</li>
        </ul>
        <a href="#final" class="btn btn-ghost-dark btn-lg" style="width:100%;justify-content:center;">Choose Term</a>
      </div>
    </div>
    <div style="margin-top:2.4rem;display:flex;align-items:center;gap:1.4rem;flex-wrap:wrap;">
      <img src="{prefix}assets/img/guarantee-badge.svg" alt="7-day money-back guarantee" style="width:88px;">
      <div>
        <strong style="font-family:var(--serif);font-size:1.35rem;">7-day money-back guarantee.</strong><br>
        <span style="font-family:var(--sans);font-size:.92rem;color:var(--ink-2);">Sit your first live class. If Club Italia is not the school we describe, we return the full tuition within seven days.</span>
      </div>
    </div>
  </div>
</section>
"""

    # 12) WHAT'S INCLUDED
    included_items = [
      f"{total_lessons} live classes, taught by {tname} from {tregion}",
      f"{contact_hours} hours of live instruction time",
      "Recording of every class within 30 minutes",
      "Weekly homework thread with your teacher",
      "Downloadable syllabus and lesson PDFs",
      "24/7 access to Biagio, our AI tutor",
      "Placement call before the course begins",
      "CEFR-aligned oral assessment on completion",
      "Signed, dated certificate within 7 days of completion",
      "Priority booking on the next level",
    ]
    fold12 = f"""
<section class="section-white">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">What's Included</div>
      <h2 class="h-display">Everything is in the <span class="ital">tuition.</span></h2>
    </div>
    <ul class="includes">
      {"".join(f'<li>{i}</li>' for i in included_items)}
    </ul>
  </div>
</section>
"""

    # 13) FAQ (course-specific)
    course_faqs = [
      (f"Who is {code} designed for?", f"Adult learners approaching Italian at the {d['cefr']} band of the CEFR. There is no prerequisite beyond a 20-minute placement call with a Club Italia advisor."),
      (f"How long does {code} take?", f"{'Twenty weeks, at one live class per week' if not is_capsule else 'Six weeks, at one live class per week'}, plus {'40 to 60' if not is_capsule else '10 to 15'} recommended study hours over the full course."),
      ("Which certification will I receive?", f"On successful completion of {code} you will sit a short oral assessment. A signed, CEFR-aligned certificate is issued within seven days by Club Italia by eTeacher and references the {d['cefr'].split(' → ')[-1]} descriptor."),
      ("What if I have to miss a live class?", "Every live class is recorded and available on your dashboard within 30 minutes. Your teacher will also post a written recap in the weekly homework thread."),
      ("What technology do I need?", "A modern browser (Chrome, Safari, Firefox or Edge), a working webcam and microphone, and a stable internet connection of at least 5 Mbps. There is no app to install."),
      (f"Can I try {code} before enrolling?", "Yes. You are welcome to sit an open sample class, free of charge, before you enrol. The Club Italia advisor will suggest the closest upcoming session on your placement call."),
    ]
    fold13 = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">Questions About {code}</div>
      <h2 class="h-display">Frequently <span class="ital">asked.</span></h2>
    </div>
    <div class="faq">{"".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in course_faqs)}</div>
  </div>
</section>
"""

    # 14) RELATED COURSES
    siblings = SIBLING_MAP[cid]
    sib_cards = ""
    for sid in siblings:
        cfg = CARDS[sid]
        sib_cards += course_card(sid, **cfg, prefix=prefix)
    fold14 = f"""
<section class="section-white">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">Continue the Ladder</div>
      <h2 class="h-display">Where {code} learners <span class="ital">go next.</span></h2>
    </div>
  </div>
  <div class="related">{sib_cards}</div>
</section>
"""

    # 15) FINAL CTA
    fold15 = f"""
<section id="final" class="section-green">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">Enrolment · {code}</div>
      <h2 class="h-display">Reserve your <span class="ital">placement call.</span></h2>
      <p class="lede">Twenty minutes with a Club Italia advisor. We hear you speak, we place you on the CEFR ladder, we book your first live class with {tname}. No card required.</p>
    </div>
    <div style="margin-top:2rem;">
      <a href="#lead" class="btn btn-primary btn-lg" style="background:var(--paper);color:var(--green-deep);">Reserve My Placement Call →</a>
      <a href="{prefix}pdf/{cid}-syllabus.pdf" class="btn btn-ghost btn-lg" style="margin-left:.8rem;">Download Syllabus PDF</a>
    </div>
  </div>
</section>
"""

    enroll_bar = f'<div class="enroll-bar"><div class="eb-left">{d["title"]} · {code} <span class="eb-price">${p_annual}/wk annual</span> · Next start Oct 6</div><a href="#pricing" class="btn btn-primary">Reserve My Spot →</a></div>'

    body = h + hero_html + fold2 + fold3 + fold4 + fold5 + fold6 + fold7 + fold8 + fold9 + fold10 + fold11 + fold12 + fold13 + fold14 + fold15 + enroll_bar + foot(prefix)
    subdir = "courses" if family=="ci" else ("spoken" if family=="ps" else "culture")
    (ROOT/f"pages/{subdir}/{cid}.html").write_text(body)
    return 15

# ---- PRICING page ----

def build_pricing():
    prefix = ""
    h = head("Pricing · Club Italia by eTeacher","Tuition, plans, and the money-back guarantee. Live Italian courses from $62 per week.",prefix)
    hero_html = hero(
        "assets/video/class-demo.mp4","assets/img/hero-poster.jpg",
        "Tuition · Fall 2026",
        'One tuition,<br>three <span class="ital">rhythms.</span>',
        "Every plan includes the full live-class programme, our dashboard, Biagio our AI tutor, and the CEFR-aligned certificate. The only thing that changes is the payment rhythm.",
        '<a href="#tiers" class="btn btn-primary btn-lg">See The Plans</a><a href="sample-class.html" class="btn btn-ghost btn-lg">Sit a Sample Class</a>'
    )

    tiers = f"""
<section id="tiers" class="section-white">
  <div class="wrap">
    <div class="pricing">
      <div class="tier">
        <div class="tier-name">Monthly</div>
        <div class="tier-price">$84<small>/wk</small></div>
        <div class="tier-sub">Billed $364 per month. Cancel any time.</div>
        <ul>
          <li>All live classes at your CEFR level</li>
          <li>Full dashboard, recordings, PDFs</li>
          <li>Biagio AI tutor, 24/7</li>
          <li>CEFR-aligned certificate</li>
          <li>Rolling monthly billing</li>
        </ul>
        <a href="#lead" class="btn btn-ghost-dark btn-lg" style="width:100%;justify-content:center;">Choose Monthly</a>
      </div>
      <div class="tier featured">
        <div class="tier-badge">Best value · Save $440</div>
        <div class="tier-name">Annual</div>
        <div class="tier-price">$62<small>/wk</small></div>
        <div class="tier-sub">Billed $3,224 once per year. Founder rate.</div>
        <ul>
          <li>Everything in Monthly</li>
          <li>Free level upgrade mid-year if you finish early</li>
          <li>Two capsule courses (La Cucina + L'Arte) included</li>
          <li>Priority placement into the next cohort</li>
          <li>Founder-rate locked for life</li>
          <li>Personal advisor throughout the year</li>
        </ul>
        <a href="#lead" class="btn btn-primary btn-lg" style="width:100%;justify-content:center;">Reserve Annual</a>
      </div>
      <div class="tier">
        <div class="tier-name">Term (four months)</div>
        <div class="tier-price">$73<small>/wk</small></div>
        <div class="tier-sub">Billed $1,169 per term. One CEFR level.</div>
        <ul>
          <li>Everything in Monthly</li>
          <li>One full CEFR level (20 live lessons)</li>
          <li>Certificate on completion</li>
          <li>Upgrade credit toward Annual within 30 days</li>
        </ul>
        <a href="#lead" class="btn btn-ghost-dark btn-lg" style="width:100%;justify-content:center;">Choose Term</a>
      </div>
    </div>
  </div>
</section>
"""

    compare = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">What's included</div>
      <h2 class="h-display">Every plan, side by <span class="ital">side.</span></h2>
    </div>
    <div style="overflow-x:auto;">
    <table class="glance" style="border:1px solid rgba(11,11,13,.14);">
      <tr><td>Live classes with certified teachers</td><td>Monthly · Term · Annual</td></tr>
      <tr><td>Class size</td><td>Capped at 12 (CI) · 8 (PS) · open (CAP)</td></tr>
      <tr><td>Recordings of every class</td><td>All plans</td></tr>
      <tr><td>Biagio AI tutor</td><td>All plans, 24/7</td></tr>
      <tr><td>CEFR-aligned certificate</td><td>All plans, on completion</td></tr>
      <tr><td>Priority cohort placement</td><td>Annual only</td></tr>
      <tr><td>Free capsule courses</td><td>Annual: 2 capsules included · Term: 1 · Monthly: none</td></tr>
      <tr><td>Free level upgrade mid-year</td><td>Annual only</td></tr>
      <tr><td>Founder rate locked for life</td><td>Annual only</td></tr>
    </table>
    </div>
  </div>
</section>
"""

    guarantee = f"""
<section class="section-white">
  <div class="wrap">
    <div class="two-col" style="align-items:center;">
      <div style="text-align:center;"><img src="assets/img/guarantee-badge.svg" alt="7-day money-back guarantee" style="max-width:220px;margin:0 auto;"></div>
      <div>
        <div class="section-eyebrow">The Guarantee</div>
        <h2 class="h-display">Seven days,<br>your money <span class="ital">back.</span></h2>
        <p class="lede">Sit your first live class. If Club Italia is not the school we describe, tell your advisor within seven days of that first class and we return the full tuition. No form, no argument.</p>
        <div style="margin-top:2rem;"><img src="assets/img/paymethods.svg" alt="Accepted payment methods" style="max-width:340px;"></div>
      </div>
    </div>
  </div>
</section>
"""

    faq_data = [
      ("Are there any hidden fees?","No. The tuition includes every live class, every recording, the dashboard, Biagio, all PDFs, the oral assessment, and the certificate. There is no separate registration fee or materials fee."),
      ("Can I switch plans mid-year?","Yes. Term learners who upgrade to Annual within 30 days receive a full credit for the Term tuition already paid."),
      ("Do you offer scholarships?","Yes. Club Italia awards ten need-based scholarships per academic year. Applications open in July and December; ask your advisor for the current cycle."),
      ("What is your refund policy?","A full refund is available within 7 days of your first live class. Beyond that, a pro-rated refund is available for the unused portion of the term or year, less a 10% administrative fee."),
      ("Is Club Italia tuition tax-deductible?","In the United States, professional-development language study is often deductible against self-employment income. Ask your accountant; Club Italia provides an itemised annual receipt on request."),
      ("Which payment methods do you accept?","All major credit cards, debit cards, PayPal, and bank transfer. Annual tuition may also be paid in three installments at no extra cost, at your advisor's discretion."),
    ]
    faq = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">Tuition FAQ</div>
      <h2 class="h-display">Money, plainly <span class="ital">explained.</span></h2>
    </div>
    <div class="faq">{"".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq_data)}</div>
  </div>
</section>
"""

    cta = f"""
<section id="lead" class="section-green">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">Reserve your placement call</div>
      <h2 class="h-display">Speak with a<br>Club Italia <span class="ital">advisor.</span></h2>
      <p class="lede">Twenty minutes. We hear you speak, place you on the CEFR ladder, and confirm the plan and cohort that fit.</p>
    </div>
    <form style="display:grid;grid-template-columns:repeat(4,1fr);gap:.6rem;max-width:940px;">
      <input type="text" placeholder="First name" style="padding:1rem;border:0;background:var(--paper);">
      <input type="email" placeholder="Email address" style="padding:1rem;border:0;background:var(--paper);">
      <select style="padding:1rem;border:0;background:var(--paper);"><option>Preferred plan…</option><option>Monthly</option><option>Term</option><option>Annual</option></select>
      <button type="submit" class="btn" style="background:var(--ink);color:var(--paper);border:0;">Book My Call →</button>
    </form>
  </div>
</section>
"""

    body = h + hero_html + tiers + compare + guarantee + faq + cta + foot(prefix)
    (ROOT/"pricing.html").write_text(body)
    return 6

# ---- COURSES INDEX ----

def build_courses_index():
    prefix = ""
    h = head("Courses · Club Italia by eTeacher","Eleven live Italian courses across the CEFR ladder. Corso Italiano, Parliamo Sempre, and Capsule d'Autore.",prefix)
    hero_html = hero(
        "assets/video/class-demo.mp4","assets/img/hero-poster.jpg",
        "The Catalogue · Fall 2026",
        'Eleven courses,<br>one <span class="ital">ladder.</span>',
        "Corso Italiano is the CEFR ladder, from absolute beginner through intermediate. Parliamo Sempre is the spoken track. Capsule d'Autore is our set of six-week cultural short courses, taught in English and Italian.",
        '<a href="#catalogue" class="btn btn-primary btn-lg">See The Catalogue</a><a href="pricing.html" class="btn btn-ghost btn-lg">See Pricing</a>'
    )

    intro = f"""
<section class="section-cream" style="padding:3rem 0;">
  <div class="wrap">{stats([
    ("11","live courses"),
    ("CEFR","A0 through B1"),
    ("10-12","learners per class"),
    ("★ 4.8","1,284 reviews"),
  ])}</div>
</section>
"""

    catalogue = f"""
<section id="catalogue" class="section-white">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">The Full Catalogue</div>
      <h2 class="h-display">Choose your <span class="ital">rhythm.</span></h2>
    </div>
  </div>
  {all_course_grid()}
</section>
"""

    ladder = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">The CEFR Ladder</div>
      <h2 class="h-display">A0 to B1, in <span class="ital">plain English.</span></h2>
    </div>
    <table class="glance">
      <tr><td>A0 · Absolute beginner</td><td>You have never studied Italian. You will learn the sound system, the greetings, the first hundred verbs. → CI-01 · PS-01</td></tr>
      <tr><td>A1.1 · Emerging</td><td>You can introduce yourself, ask basic questions, and understand a slow speaker on familiar topics. → CI-02 · PS-01</td></tr>
      <tr><td>A1.2 · Elementary</td><td>You handle everyday exchanges at the café, on the phone, in a shop. You use the past tense. → CI-02 → CI-03 · PS-02</td></tr>
      <tr><td>A2.1 · Pre-intermediate</td><td>You can carry a full short conversation, describe your past, express opinions and preferences. → CI-03 · PS-02 → PS-03</td></tr>
      <tr><td>A2.2 · Intermediate</td><td>You cope in most travel situations, follow standard media on familiar topics, and defend a point in Italian. → CI-04 · PS-03</td></tr>
      <tr><td>B1 · Threshold</td><td>You handle the language spontaneously: work, opinion, argument, hypothesis. → PS-04 · continuing capsules</td></tr>
    </table>
  </div>
</section>
"""

    method = f"""
<section class="section-black">
  <div class="wrap">
    <div class="two-col">
      <div>
        <div class="section-eyebrow">The house method</div>
        <h2 class="h-display">Grammar lives inside <span class="ital">dialogue.</span></h2>
        <p class="lede">Every Club Italia unit opens with a real recorded exchange between Italians. Learners try the exchange first; the grammar rule that governs it is drawn out only after they have already used it, wrongly and rightly, in front of the teacher.</p>
      </div>
      <div>
        <div class="section-eyebrow">The house register</div>
        <h2 class="h-display">City-anchored,<br>culturally <span class="ital">specific.</span></h2>
        <p class="lede">Every course is set in a specific Italian city, taught by a teacher who lives in that city. Rome for beginners, Florence for A1, Bologna for A2, Naples and Milan for the B1 push, Venice and the road for the spoken track.</p>
      </div>
    </div>
  </div>
</section>
"""

    body = h + hero_html + intro + catalogue + ladder + method + foot(prefix)
    (ROOT/"courses.html").write_text(body)
    return 5

# ---- CAPSULES INDEX ----
def build_capsules_index():
    prefix = ""
    h = head("Cultural Capsules · Club Italia by eTeacher","Six-week cultural short courses. La Cucina, L'Arte, L'Opera. Any level, English-supported.",prefix)
    hero_html = hero(
        "assets/video/cucina-pasta.mp4","assets/img/hero-poster.jpg",
        "Capsule d'Autore · Any level",
        'Culture as a<br><span class="ital">second Italian.</span>',
        "Six weeks. One theme. Taught in Italian at the pace of the learner, with English support on demand. La Cucina, L'Arte, L'Opera; three short courses at the heart of italianità.",
        '<a href="#list" class="btn btn-primary btn-lg">See the Capsules</a>'
    )

    intro = f"""
<section class="section-cream" style="padding:3rem 0;">
  <div class="wrap">{stats([
    ("3","cultural capsules"),
    ("6 weeks","each capsule"),
    ("Any","level, all welcome"),
    ("$29/wk","annual rate"),
  ])}</div>
</section>
"""

    caps = [
      ("cap-food","La Cucina","The language of the Italian table","cap-food"),
      ("cap-art","L'Arte","The Renaissance in the words that made it","cap-art"),
      ("cap-opera","L'Opera","Opera as a second Italian","cap-opera"),
    ]
    grid = f"""
<section id="list" class="section-white">
  <div class="wrap">
    <div class="section-head">
      <div class="section-eyebrow">The Capsules</div>
      <h2 class="h-display">Three ways to <span class="ital">read Italy.</span></h2>
    </div>
  </div>
  <div class="tiles">
    {"".join(f'<a class="tile" href="pages/culture/{cid}.html" style="aspect-ratio:4/3;"><img src="assets/img/{img}.jpg" alt="{t}"><div class="tile-content"><div class="tile-sub">{sub}</div><div class="tile-title">{t}</div></div></a>' for cid,t,sub,img in caps)}
  </div>
</section>
"""

    included = f"""
<section class="section-cream">
  <div class="wrap">
    <div class="section-head"><div class="section-eyebrow">What's included</div><h2 class="h-display">Every capsule <span class="ital">gives you.</span></h2></div>
    <ul class="includes">
      <li>Six 75-minute live classes over six weeks</li>
      <li>All materials, recordings, and PDFs</li>
      <li>English support on demand for absolute beginners</li>
      <li>A closing conversation dinner (virtual)</li>
      <li>Certificate of attendance</li>
      <li>Access to the Culture Library for six months</li>
    </ul>
  </div>
</section>
"""

    body = h + hero_html + intro + grid + included + foot(prefix)
    (ROOT/"capsules.html").write_text(body)
    return 4


# ==== RUN TIER 1 ====
if __name__ == "__main__":
    n = build_home()
    print(f"index.html · folds={n}")
    for cid in ["ci1","ci2","ci3","ci4","ps1","ps2","ps3","ps4","cap-food","cap-art","cap-opera"]:
        n = course_page(cid)
        print(f"{cid}.html · folds={n}")
    print(f"pricing.html · folds={build_pricing()}")
    print(f"courses.html · folds={build_courses_index()}")
    print(f"capsules.html · folds={build_capsules_index()}")
