"""Sales-shape rebuild generator — homepage + 4 CI + 4 PS + 3 CAP + pricing."""
import os, textwrap, pathlib

ROOT = pathlib.Path("/home/user/workspace/club-italia")

# --- Shared inline component CSS (dropped into every rebuilt page) ---
SALES_CSS = """
<style>
/* ============ SALES-SHAPE INLINE COMPONENTS ============ */
:root{
  --sales-bordeaux:#3A0E12; --sales-bordeaux-deep:#22080B;
  --sales-ivory:#F3EDDF; --sales-cream:#FAF5EA;
  --sales-terra:#B65538; --sales-terra-deep:#8E3D22;
  --sales-gold:#C9A24B; --sales-gold-soft:#DDB86A;
  --sales-verde:#1E6B4A; --sales-rosso:#B8232E;
  --sales-navy-hero:linear-gradient(160deg,#1A0507 0%,#3A0E12 60%,#5A1A22 100%);
}
/* Sticky top urgency bar */
.sales-urgency{position:fixed;top:0;left:0;right:0;z-index:1000;background:linear-gradient(90deg,#3A0E12,#5A1A22);color:#F3EDDF;font-family:'Inter',sans-serif;font-size:.92rem;padding:.55rem 1.4rem;display:flex;align-items:center;justify-content:center;gap:1rem;border-bottom:1px solid rgba(201,162,75,.35);letter-spacing:.01em}
.sales-urgency .dot{width:8px;height:8px;border-radius:50%;background:#C9A24B;box-shadow:0 0 0 0 rgba(201,162,75,.7);animation:pulseDot 1.6s infinite}
.sales-urgency b{color:#DDB86A;font-weight:600}
.sales-urgency a{color:#DDB86A;text-decoration:underline;margin-left:.4rem}
@keyframes pulseDot{0%{box-shadow:0 0 0 0 rgba(201,162,75,.7)}70%{box-shadow:0 0 0 10px rgba(201,162,75,0)}100%{box-shadow:0 0 0 0 rgba(201,162,75,0)}}
body{padding-top:38px}
.site-header{top:38px !important}

/* Sales hero (video full-viewport, huge type) */
.sales-hero{position:relative;min-height:96vh;display:flex;align-items:center;overflow:hidden;background:var(--sales-navy-hero);color:#F3EDDF}
.sales-hero-bg{position:absolute;inset:0;z-index:0}
.sales-hero-bg video{width:100%;height:100%;object-fit:cover;opacity:.55}
.sales-hero-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(26,5,7,.55) 0%,rgba(26,5,7,.35) 40%,rgba(26,5,7,.85) 100%)}
.sales-hero-inner{position:relative;z-index:2;max-width:1240px;margin:0 auto;padding:8rem 1.6rem 6rem;width:100%}
.sales-trust-strip{position:absolute;top:1.6rem;right:1.6rem;z-index:3;background:rgba(26,5,7,.55);backdrop-filter:blur(8px);padding:.7rem 1.1rem;border:1px solid rgba(221,184,106,.4);border-radius:4px;display:flex;align-items:center;gap:.6rem;color:#F3EDDF;font-family:'Inter',sans-serif;font-size:.86rem}
.sales-trust-strip .stars{color:#DDB86A;letter-spacing:2px}
.sales-live-ticker{position:absolute;bottom:2rem;left:2rem;z-index:3;background:rgba(26,5,7,.72);backdrop-filter:blur(8px);padding:.75rem 1.15rem;border-radius:4px;color:#F3EDDF;font-family:'Inter',sans-serif;font-size:.88rem;display:flex;align-items:center;gap:.65rem;border:1px solid rgba(221,184,106,.3)}
.sales-live-ticker .live-dot{width:10px;height:10px;border-radius:50%;background:#B8232E;box-shadow:0 0 0 0 rgba(184,35,46,.6);animation:pulseDot 1.4s infinite}
.sales-hero h1{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(4rem,10vw,9rem);line-height:.98;letter-spacing:-.02em;margin:1.4rem 0 1.8rem;max-width:16ch}
.sales-hero .hero-sub{font-family:'Inter',sans-serif;font-size:clamp(1.15rem,1.6vw,1.5rem);line-height:1.5;max-width:56ch;color:rgba(243,238,227,.9);font-weight:300;margin-bottom:2.4rem}
.sales-hero .price-chip{display:inline-flex;align-items:center;gap:.5rem;background:rgba(201,162,75,.15);border:1px solid rgba(221,184,106,.5);color:#DDB86A;font-family:'Inter',sans-serif;font-size:.95rem;font-weight:500;padding:.55rem 1rem;border-radius:3px;letter-spacing:.02em;margin-bottom:1.8rem}
.sales-hero .level-badge{display:inline-block;background:#C9A24B;color:#22080B;font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1.4rem;font-weight:600;padding:.35rem 1.1rem;border-radius:3px;margin-bottom:1rem}
.sales-cta-row{display:flex;flex-wrap:wrap;gap:1rem;margin-top:2rem}
.btn-sales-primary{background:linear-gradient(180deg,#DDB86A,#C9A24B);color:#22080B;font-family:'Inter',sans-serif;font-weight:600;font-size:1.05rem;padding:1.15rem 2rem;border-radius:3px;letter-spacing:.02em;box-shadow:0 8px 24px rgba(201,162,75,.35);transition:transform .2s,box-shadow .2s;display:inline-flex;align-items:center;gap:.5rem;text-transform:none;border:none;cursor:pointer}
.btn-sales-primary:hover{transform:translateY(-2px);box-shadow:0 12px 32px rgba(201,162,75,.5)}
.btn-sales-ghost{background:transparent;color:#F3EDDF;font-family:'Inter',sans-serif;font-weight:500;font-size:1.05rem;padding:1.1rem 2rem;border-radius:3px;letter-spacing:.02em;border:1px solid rgba(243,238,227,.55);display:inline-flex;align-items:center;gap:.5rem;transition:all .2s;cursor:pointer}
.btn-sales-ghost:hover{background:rgba(243,238,227,.08);border-color:#DDB86A;color:#DDB86A}

/* Tricolor rule */
.tricolor-rule{display:flex;height:4px;max-width:280px;margin:2.4rem 0}
.tricolor-rule span{flex:1}
.tricolor-rule span:nth-child(1){background:#1E6B4A}
.tricolor-rule span:nth-child(2){background:#F3EDDF}
.tricolor-rule span:nth-child(3){background:#B8232E}

/* Instant social proof strip */
.sales-proof-strip{background:var(--sales-ivory);padding:2.4rem 1.6rem;border-top:1px solid rgba(42,10,13,.1);border-bottom:1px solid rgba(42,10,13,.1)}
.sales-proof-strip .wrap-in{max-width:1240px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:1.4rem;text-align:center}
.sales-proof-strip .pi{padding:0 1rem;border-right:1px solid rgba(42,10,13,.1)}
.sales-proof-strip .pi:last-child{border-right:none}
.sales-proof-strip .pi b{display:block;font-family:'Cormorant Garamond',serif;font-size:2.2rem;font-weight:600;color:#3A0E12;line-height:1.1;margin-bottom:.3rem}
.sales-proof-strip .pi span{display:block;font-family:'Inter',sans-serif;font-size:.9rem;color:rgba(42,10,13,.7);letter-spacing:.04em;text-transform:uppercase}
.sales-proof-strip .pi .stars{color:#C9A24B;letter-spacing:2px;font-size:1.1rem;margin-bottom:.2rem}
@media(max-width:800px){.sales-proof-strip .wrap-in{grid-template-columns:repeat(2,1fr)}.sales-proof-strip .pi{border-right:none;border-bottom:1px solid rgba(42,10,13,.1);padding-bottom:1rem}}

/* Section grounds */
.sales-section{padding:clamp(5rem,9vw,9rem) 1.6rem;position:relative}
.sales-section .wrap-in{max-width:1240px;margin:0 auto}
.ground-bordeaux{background:linear-gradient(180deg,#3A0E12,#22080B);color:#F3EDDF}
.ground-ivory{background:var(--sales-ivory);color:#22080B}
.ground-cream{background:var(--sales-cream);color:#22080B}
.ground-terra{background:linear-gradient(140deg,#B65538 0%,#8E3D22 100%);color:#F3EDDF}
.ground-navy{background:var(--sales-navy-hero);color:#F3EDDF}

.sales-section h2{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(2.8rem,5.5vw,5rem);line-height:1.02;letter-spacing:-.015em;margin-bottom:1.4rem;max-width:22ch}
.sales-section h3{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(1.6rem,2.6vw,2.4rem);line-height:1.1;margin-bottom:.9rem}
.sales-section .lead{font-family:'Inter',sans-serif;font-size:1.25rem;line-height:1.55;max-width:64ch;font-weight:300;opacity:.88;margin-bottom:2rem}
.sales-section p{font-family:'Inter',sans-serif;font-size:1.05rem;line-height:1.65}
.gold-ital{font-family:'Cormorant Garamond',serif;font-style:italic;color:#C9A24B;font-weight:500}
.ground-ivory .gold-ital,.ground-cream .gold-ital{color:#8E3D22}
.eyebrow-sm{display:inline-block;font-family:'Inter',sans-serif;font-size:.78rem;letter-spacing:.22em;text-transform:uppercase;color:#C9A24B;font-weight:600;margin-bottom:1rem}
.ground-ivory .eyebrow-sm,.ground-cream .eyebrow-sm{color:#8E3D22}

/* Problem / solution two-col editorial */
.editorial-two{display:grid;grid-template-columns:1.1fr 1fr;gap:4rem;align-items:center}
.editorial-two img{width:100%;border-radius:3px;box-shadow:0 20px 60px rgba(0,0,0,.35)}
@media(max-width:900px){.editorial-two{grid-template-columns:1fr;gap:2rem}}

/* Solution 6-icon grid */
.solution-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2.4rem;margin-top:3rem}
.solution-grid .cell{padding:1.6rem;border:1px solid rgba(243,238,227,.15);border-radius:3px;background:rgba(243,238,227,.03)}
.solution-grid .cell .ico{width:44px;height:44px;border-radius:50%;background:rgba(201,162,75,.15);color:#DDB86A;display:flex;align-items:center;justify-content:center;font-size:1.4rem;margin-bottom:1rem;border:1px solid rgba(201,162,75,.4)}
.solution-grid .cell h3{font-size:1.4rem;color:#F3EDDF}
.solution-grid .cell p{color:rgba(243,238,227,.7);font-size:1rem}
@media(max-width:900px){.solution-grid{grid-template-columns:1fr}}

/* Zoom mockup fold */
.zoom-fold{padding:clamp(4rem,7vw,7rem) 1.6rem;background:linear-gradient(180deg,#1A0507,#3A0E12 60%,#1A0507);color:#F3EDDF;text-align:center}
.zoom-fold .cap{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(1.8rem,3vw,2.8rem);color:#DDB86A;margin-bottom:2rem;max-width:22ch;margin-left:auto;margin-right:auto}
.zoom-fold img{max-width:1180px;width:100%;margin:0 auto;border-radius:6px;box-shadow:0 30px 90px rgba(0,0,0,.6),0 0 0 1px rgba(221,184,106,.15)}
.zoom-fold .sub{margin-top:1.6rem;font-family:'Inter',sans-serif;font-size:1rem;color:rgba(243,238,227,.7);letter-spacing:.05em}

/* Course showcase */
.track-header{display:flex;align-items:baseline;gap:1.2rem;margin:3rem 0 1.6rem;padding-bottom:1rem;border-bottom:1px solid rgba(42,10,13,.15)}
.track-header .num{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:2.4rem;color:#8E3D22}
.track-header h3{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:500;font-size:clamp(2rem,3.6vw,3rem);color:#3A0E12;margin:0}
.track-header .kicker{margin-left:auto;font-family:'Inter',sans-serif;font-size:.86rem;color:rgba(42,10,13,.6);letter-spacing:.05em}
.course-cards{display:grid;grid-template-columns:repeat(4,1fr);gap:1.4rem}
@media(max-width:1100px){.course-cards{grid-template-columns:repeat(2,1fr)}}
@media(max-width:600px){.course-cards{grid-template-columns:1fr}}
.course-card{background:#FFFFFF;border-radius:4px;overflow:hidden;box-shadow:0 8px 30px rgba(42,10,13,.12);display:flex;flex-direction:column;transition:transform .25s,box-shadow .25s}
.course-card:hover{transform:translateY(-4px);box-shadow:0 20px 50px rgba(42,10,13,.2)}
.course-card .cc-img{position:relative;aspect-ratio:16/10;overflow:hidden}
.course-card .cc-img img{width:100%;height:100%;object-fit:cover}
.course-card .cc-badge{position:absolute;top:.8rem;left:.8rem;background:#22080B;color:#DDB86A;font-family:'Inter',sans-serif;font-size:.75rem;padding:.3rem .65rem;border-radius:3px;letter-spacing:.05em}
.course-card .cc-price{position:absolute;top:.8rem;right:.8rem;background:#C9A24B;color:#22080B;font-family:'Inter',sans-serif;font-size:.85rem;font-weight:600;padding:.35rem .7rem;border-radius:3px}
.course-card .cc-body{padding:1.4rem 1.4rem 1.6rem;flex:1;display:flex;flex-direction:column}
.course-card .cc-cefr{font-family:'Inter',sans-serif;font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:#8E3D22;font-weight:600;margin-bottom:.4rem}
.course-card h4{font-family:'Cormorant Garamond',serif;font-size:1.6rem;font-weight:600;color:#22080B;line-height:1.1;margin-bottom:.5rem}
.course-card .cc-promise{font-family:'Inter',sans-serif;font-size:.98rem;color:rgba(42,10,13,.72);line-height:1.4;margin-bottom:1rem}
.course-card .cc-stats{display:flex;flex-wrap:wrap;gap:.8rem;font-family:'Inter',sans-serif;font-size:.8rem;color:rgba(42,10,13,.6);margin-bottom:1.2rem;padding-top:.8rem;border-top:1px solid rgba(42,10,13,.08)}
.course-card .cc-cta{margin-top:auto;background:#3A0E12;color:#DDB86A;font-family:'Inter',sans-serif;font-weight:500;font-size:.95rem;padding:.85rem 1rem;border-radius:3px;text-align:center;border:1px solid rgba(221,184,106,.4);transition:all .2s}
.course-card .cc-cta:hover{background:#C9A24B;color:#22080B;border-color:#C9A24B}

/* How it works 5-step */
.hiw-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:1.6rem;margin-top:3rem}
@media(max-width:1000px){.hiw-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:600px){.hiw-grid{grid-template-columns:1fr}}
.hiw-step{padding:1.6rem;background:rgba(243,238,227,.04);border:1px solid rgba(243,238,227,.12);border-radius:4px}
.hiw-step .n{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:2.4rem;color:#DDB86A;line-height:1;margin-bottom:.6rem}
.hiw-step h3{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1.5rem;font-weight:500;color:#F3EDDF;margin-bottom:.6rem}
.hiw-step p{font-family:'Inter',sans-serif;font-size:.98rem;color:rgba(243,238,227,.75);margin-bottom:1rem}
.hiw-step .ss{background:#22080B;border-radius:3px;aspect-ratio:16/10;display:flex;align-items:center;justify-content:center;color:rgba(221,184,106,.4);font-family:'Cormorant Garamond',serif;font-style:italic;font-size:.9rem;padding:.6rem;text-align:center;border:1px solid rgba(243,238,227,.08);overflow:hidden}
.hiw-step .ss img{width:100%;height:100%;object-fit:cover}

/* Teacher wall */
.teacher-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:.9rem;margin-top:3rem}
@media(max-width:1100px){.teacher-grid{grid-template-columns:repeat(4,1fr)}}
@media(max-width:600px){.teacher-grid{grid-template-columns:repeat(2,1fr)}}
.teacher-tile{position:relative;aspect-ratio:3/4;overflow:hidden;border-radius:4px;cursor:pointer;background:#22080B}
.teacher-tile img{width:100%;height:100%;object-fit:cover;transition:transform .5s,filter .5s;filter:brightness(.85)}
.teacher-tile:hover img{transform:scale(1.06);filter:brightness(1)}
.teacher-tile .name{position:absolute;bottom:0;left:0;right:0;padding:1rem .8rem;background:linear-gradient(180deg,transparent,rgba(26,5,7,.9));color:#F3EDDF;font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:500}
.teacher-tile .hover-card{position:absolute;inset:auto 0 0 0;transform:translateY(100%);transition:transform .3s;background:rgba(26,5,7,.94);color:#F3EDDF;padding:1.2rem .9rem;font-family:'Inter',sans-serif}
.teacher-tile:hover .hover-card{transform:translateY(0)}
.teacher-tile .hover-card h4{font-family:'Cormorant Garamond',serif;font-size:1.2rem;color:#DDB86A;margin-bottom:.3rem}
.teacher-tile .hover-card p{font-size:.8rem;color:rgba(243,238,227,.75);line-height:1.4;margin:0}

/* Method 4-quadrant */
.method-quad{display:grid;grid-template-columns:1fr 1fr;gap:0;margin-top:3rem;border:1px solid rgba(42,10,13,.12);border-radius:4px;overflow:hidden}
.method-quad .q{padding:3rem 2rem;background:#F3EDDF;border-right:1px solid rgba(42,10,13,.1);border-bottom:1px solid rgba(42,10,13,.1)}
.method-quad .q:nth-child(2){border-right:none}
.method-quad .q:nth-child(3),.method-quad .q:nth-child(4){border-bottom:none}
.method-quad .q:nth-child(2){background:#FAF5EA}
.method-quad .q:nth-child(3){background:#FAF5EA}
.method-quad .q .num{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1.4rem;color:#8E3D22;margin-bottom:.5rem}
.method-quad .q h3{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:2.2rem;color:#3A0E12;margin-bottom:.6rem}
.method-quad .q p{font-family:'Inter',sans-serif;font-size:1rem;color:rgba(42,10,13,.75);line-height:1.5}
@media(max-width:800px){.method-quad{grid-template-columns:1fr}.method-quad .q{border-right:none !important}}

/* Biagio dark fold */
.biagio-fold{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center}
.biagio-fold .portrait img{width:100%;border-radius:4px;box-shadow:0 30px 80px rgba(0,0,0,.5)}
.chat-mock{background:#0F0304;border:1px solid rgba(221,184,106,.25);border-radius:6px;padding:1.4rem;box-shadow:0 20px 60px rgba(0,0,0,.5)}
.chat-mock .bubble{padding:.85rem 1.1rem;border-radius:14px;font-family:'Inter',sans-serif;font-size:.98rem;line-height:1.4;margin-bottom:.8rem;max-width:82%}
.chat-mock .b-user{background:#3A0E12;color:#F3EDDF;margin-left:auto;border-bottom-right-radius:3px}
.chat-mock .b-biagio{background:linear-gradient(180deg,#C9A24B,#A88536);color:#22080B;border-bottom-left-radius:3px}
.chat-mock .b-biagio .who{display:block;font-size:.7rem;text-transform:uppercase;letter-spacing:.12em;opacity:.7;margin-bottom:.2rem;font-weight:600}
@media(max-width:900px){.biagio-fold{grid-template-columns:1fr;gap:2rem}}

/* Trustpilot wall */
.tp-header{text-align:center;margin-bottom:3rem}
.tp-header .agg{font-family:'Cormorant Garamond',serif;font-size:5rem;font-weight:500;color:#DDB86A;line-height:1;margin-bottom:.4rem}
.tp-header .stars{color:#C9A24B;font-size:1.8rem;letter-spacing:6px;margin-bottom:.6rem}
.tp-header .of{font-family:'Inter',sans-serif;color:rgba(243,238,227,.7);letter-spacing:.05em}
.tp-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem}
@media(max-width:900px){.tp-grid{grid-template-columns:1fr}}
.tp-card{background:#F3EDDF;color:#22080B;padding:1.8rem;border-radius:4px;border-top:3px solid #B65538}
.tp-card .who{display:flex;align-items:center;gap:.7rem;margin-bottom:1rem}
.tp-card .who .av{width:38px;height:38px;border-radius:50%;background:linear-gradient(135deg,#B65538,#8E3D22);color:#F3EDDF;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-weight:600}
.tp-card .who b{font-family:'Inter',sans-serif;font-size:.95rem}
.tp-card .who .verified{font-size:.72rem;color:#1E6B4A;font-weight:600;letter-spacing:.05em}
.tp-card .stars{color:#C9A24B;font-size:1.05rem;letter-spacing:3px;margin-bottom:.6rem}
.tp-card h4{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:1.35rem;line-height:1.2;color:#22080B;margin-bottom:.6rem}
.tp-card p{font-family:'Inter',sans-serif;font-size:.95rem;line-height:1.5;color:rgba(42,10,13,.8);margin-bottom:1rem}
.tp-card .tp-foot{font-family:'Inter',sans-serif;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:rgba(42,10,13,.5);padding-top:.8rem;border-top:1px solid rgba(42,10,13,.1)}

/* Pricing */
.pricing-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem;margin-top:3rem}
@media(max-width:900px){.pricing-cards{grid-template-columns:1fr}}
.p-card{background:#F3EDDF;color:#22080B;border-radius:6px;padding:2.4rem 2rem;position:relative;box-shadow:0 10px 40px rgba(42,10,13,.15);display:flex;flex-direction:column}
.p-card.highlight{background:linear-gradient(180deg,#3A0E12,#22080B);color:#F3EDDF;border:2px solid #C9A24B;box-shadow:0 20px 60px rgba(201,162,75,.3);transform:scale(1.03)}
.p-card .p-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:#C9A24B;color:#22080B;font-family:'Inter',sans-serif;font-weight:600;font-size:.78rem;padding:.4rem 1rem;border-radius:3px;letter-spacing:.05em;white-space:nowrap}
.p-card .p-name{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1.6rem;margin-bottom:.4rem;color:#8E3D22}
.p-card.highlight .p-name{color:#DDB86A}
.p-card .p-price{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:4rem;line-height:1;margin-bottom:.3rem}
.p-card.highlight .p-price{color:#DDB86A}
.p-card .p-unit{font-family:'Inter',sans-serif;font-size:.9rem;opacity:.7;margin-bottom:1.6rem}
.p-card ul{list-style:none;padding:0;margin:0 0 2rem;flex:1}
.p-card ul li{font-family:'Inter',sans-serif;font-size:.98rem;padding:.55rem 0;border-bottom:1px solid rgba(42,10,13,.1);display:flex;gap:.6rem;align-items:flex-start}
.p-card.highlight ul li{border-color:rgba(243,238,227,.12)}
.p-card ul li::before{content:"✓";color:#1E6B4A;font-weight:600;flex-shrink:0}
.p-card.highlight ul li::before{color:#DDB86A}
.p-card .btn-sales-primary{width:100%;justify-content:center}
.p-card:not(.highlight) .btn-sales-primary{background:#3A0E12;color:#DDB86A;box-shadow:none}
.p-card:not(.highlight) .btn-sales-primary:hover{background:#22080B}

/* Guarantee */
.guarantee-band{text-align:center;padding:clamp(4rem,7vw,7rem) 1.6rem;background:linear-gradient(140deg,#B65538,#8E3D22);color:#F3EDDF}
.guarantee-band h2{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:clamp(2.6rem,5vw,4.4rem);line-height:1.05;margin-bottom:1rem;max-width:22ch;margin-left:auto;margin-right:auto}
.guarantee-band .badge{width:96px;height:96px;margin:0 auto 1.4rem;display:flex;align-items:center;justify-content:center}
.guarantee-band .pays{display:flex;justify-content:center;gap:1.6rem;margin-top:2rem;font-family:'Inter',sans-serif;font-size:.85rem;letter-spacing:.08em;text-transform:uppercase;opacity:.85;flex-wrap:wrap}
.guarantee-band .pays span{padding:.4rem .8rem;border:1px solid rgba(243,238,227,.35);border-radius:3px}

/* FAQ */
.faq-list-sales{max-width:820px;margin:3rem auto 0;display:flex;flex-direction:column;gap:.8rem}
.faq-list-sales details{background:#FAF5EA;border:1px solid rgba(42,10,13,.1);border-radius:4px;padding:0;overflow:hidden}
.ground-bordeaux .faq-list-sales details{background:rgba(243,238,227,.04);border-color:rgba(243,238,227,.14)}
.faq-list-sales summary{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:1.35rem;padding:1.2rem 1.4rem;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center}
.ground-bordeaux .faq-list-sales summary{color:#F3EDDF}
.faq-list-sales summary::-webkit-details-marker{display:none}
.faq-list-sales summary::after{content:"+";font-family:'Cormorant Garamond',serif;font-size:1.6rem;color:#C9A24B;transition:transform .2s}
.faq-list-sales details[open] summary::after{content:"−"}
.faq-list-sales .fbody{padding:0 1.4rem 1.4rem;font-family:'Inter',sans-serif;font-size:1rem;line-height:1.55;color:rgba(42,10,13,.78)}
.ground-bordeaux .faq-list-sales .fbody{color:rgba(243,238,227,.78)}

/* Final CTA form */
.final-cta{padding:clamp(5rem,8vw,8rem) 1.6rem;background:linear-gradient(160deg,#22080B,#3A0E12);color:#F3EDDF;text-align:center}
.final-cta form{max-width:640px;margin:2.4rem auto 0;display:grid;grid-template-columns:1fr 1fr;gap:.9rem}
.final-cta form input,.final-cta form select{grid-column:span 1;padding:1rem 1.1rem;background:rgba(243,238,227,.06);border:1px solid rgba(243,238,227,.2);color:#F3EDDF;font-family:'Inter',sans-serif;font-size:1rem;border-radius:3px}
.final-cta form input:focus,.final-cta form select:focus{outline:none;border-color:#DDB86A}
.final-cta form input::placeholder{color:rgba(243,238,227,.5)}
.final-cta form .full{grid-column:span 2}
.final-cta form button{grid-column:span 2}

/* Sticky bottom bar */
.sales-sticky-bottom{position:fixed;bottom:-100px;left:0;right:0;z-index:999;background:linear-gradient(90deg,#22080B,#3A0E12);color:#DDB86A;padding:.9rem 1.4rem;border-top:1px solid #C9A24B;display:flex;align-items:center justify-content:space-between;gap:1.4rem;transition:bottom .35s cubic-bezier(.22,.61,.36,1);box-shadow:0 -10px 30px rgba(0,0,0,.4);flex-wrap:wrap;justify-content:center}
.sales-sticky-bottom.on{bottom:0}
.sales-sticky-bottom span{font-family:'Inter',sans-serif;font-size:.95rem;letter-spacing:.02em}
.sales-sticky-bottom span b{color:#F3EDDF}
.sales-sticky-bottom .stars{color:#C9A24B}
.sales-sticky-bottom .btn-sales-primary{padding:.7rem 1.2rem;font-size:.9rem}

/* Course outcomes checklist */
.outcomes-grid{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem 2rem;margin-top:2.4rem}
@media(max-width:800px){.outcomes-grid{grid-template-columns:1fr}}
.outcome{display:flex;gap:1rem;align-items:flex-start;padding:1rem 0;border-bottom:1px solid rgba(42,10,13,.1)}
.ground-bordeaux .outcome{border-color:rgba(243,238,227,.1)}
.outcome .ck{width:32px;height:32px;border-radius:50%;background:rgba(201,162,75,.15);color:#8E3D22;display:flex;align-items:center;justify-content:center;font-weight:600;flex-shrink:0;border:1px solid rgba(201,162,75,.4)}
.ground-bordeaux .outcome .ck{color:#DDB86A;background:rgba(221,184,106,.14)}
.outcome b{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:1.3rem;display:block;margin-bottom:.2rem}
.outcome span{font-family:'Inter',sans-serif;font-size:.98rem;opacity:.8;display:block}

/* Syllabus table */
.syllabus-table{width:100%;border-collapse:collapse;margin-top:2rem;font-family:'Inter',sans-serif;font-size:.95rem;background:#FAF5EA;border-radius:6px;overflow:hidden;box-shadow:0 10px 40px rgba(42,10,13,.1)}
.syllabus-table th{background:#3A0E12;color:#DDB86A;text-align:left;padding:1rem 1.2rem;font-weight:600;font-size:.82rem;letter-spacing:.08em;text-transform:uppercase}
.syllabus-table td{padding:1rem 1.2rem;border-bottom:1px solid rgba(42,10,13,.08);vertical-align:top}
.syllabus-table tr:last-child td{border-bottom:none}
.syllabus-table td:first-child{font-family:'Cormorant Garamond',serif;font-style:italic;color:#8E3D22;font-size:1.2rem;font-weight:600;width:80px}
.syllabus-table td b{display:block;color:#22080B;margin-bottom:.15rem;font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:600}
.syllabus-table tbody tr:nth-child(even){background:rgba(233,222,199,.35)}

/* Teacher spotlight (course page) */
.teacher-spot{display:grid;grid-template-columns:.9fr 1.1fr;gap:3.4rem;align-items:center}
.teacher-spot img{width:100%;border-radius:6px;box-shadow:0 20px 60px rgba(42,10,13,.3)}
.teacher-spot .eyebrow-sm{color:#8E3D22}
.teacher-spot h2{font-size:clamp(3rem,6vw,5rem);margin-bottom:1.4rem}
.teacher-spot .creds{display:flex;flex-wrap:wrap;gap:.6rem;margin:1.4rem 0}
.teacher-spot .creds span{background:rgba(42,10,13,.06);color:#3A0E12;font-family:'Inter',sans-serif;font-size:.82rem;padding:.4rem .8rem;border-radius:3px;letter-spacing:.03em}
@media(max-width:900px){.teacher-spot{grid-template-columns:1fr;gap:2rem}}

/* Video player mockup */
.video-mockup{position:relative;max-width:960px;margin:0 auto;border-radius:6px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.5);aspect-ratio:16/9;background:#22080B}
.video-mockup img{width:100%;height:100%;object-fit:cover;opacity:.85}
.video-mockup .play{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:96px;height:96px;border-radius:50%;background:rgba(201,162,75,.94);color:#22080B;display:flex;align-items:center;justify-content:center;font-size:2.4rem;box-shadow:0 12px 40px rgba(0,0,0,.5);cursor:pointer;border:3px solid #F3EDDF}
.video-mockup .cap-over{position:absolute;bottom:0;left:0;right:0;padding:1.4rem 1.6rem;background:linear-gradient(180deg,transparent,rgba(0,0,0,.7));color:#F3EDDF;font-family:'Inter',sans-serif;font-size:1rem}

/* Trust strip small (below hero) */
.trust-strip-mini{background:#22080B;color:#F3EDDF;padding:1.4rem 1.6rem;text-align:center}
.trust-strip-mini .wrap-in{max-width:1240px;margin:0 auto;display:flex;justify-content:center;align-items:center;gap:2rem;flex-wrap:wrap;font-family:'Inter',sans-serif;font-size:.95rem}
.trust-strip-mini .stars{color:#DDB86A;letter-spacing:2px}
.trust-strip-mini .sep{opacity:.4}

/* Certificate fold */
.cert-fold{display:grid;grid-template-columns:1.1fr 1fr;gap:4rem;align-items:center}
.cert-fold img{width:100%;border-radius:6px;box-shadow:0 30px 80px rgba(0,0,0,.4)}
@media(max-width:900px){.cert-fold{grid-template-columns:1fr}}
</style>
"""

NAV = """<!--NAV-->
<header class="site-header">
  <div class="wrap nav">
    <a class="nav-logo" href="{root}index.html" aria-label="Club Italia · home">
      <span class="logo-text"><span class="lt-main">Club Italia</span><span class="lt-sub">by eTeacher</span></span>
    </a>
    <nav class="nav-menu" aria-label="Primary">
      <span class="nav-item"><a class="nav-link" href="{root}courses.html">Courses</a></span>
      <span class="nav-item"><a class="nav-link" href="{root}how-it-works.html">How It Works</a></span>
      <span class="nav-item"><a class="nav-link" href="{root}method.html">Method</a></span>
      <span class="nav-item"><a class="nav-link" href="{root}teachers.html">Teachers</a></span>
      <span class="nav-item"><a class="nav-link" href="{root}culture.html">Culture</a></span>
      <span class="nav-item"><a class="nav-link" href="{root}biagio.html">AI Tutor</a></span>
      <span class="nav-item"><a class="nav-link" href="{root}pricing.html">Pricing</a></span>
    </nav>
    <button class="btn btn-3d btn-3d-primary nav-cta" data-advisor type="button">Reserve My Placement Call</button>
    <button class="nav-toggle" aria-label="Open menu" aria-controls="navDrawer" type="button"><span></span><span></span><span></span></button>
  </div>
</header>
<aside class="nav-drawer" id="navDrawer" aria-label="Mobile menu">
  <button class="nav-drawer-close" aria-label="Close menu" type="button">&times;</button>
  <a href="{root}courses.html">Courses</a><a href="{root}how-it-works.html">How It Works</a><a href="{root}method.html">Method</a>
  <a href="{root}teachers.html">Teachers</a><a href="{root}culture.html">Culture</a><a href="{root}capsules.html">Culture Capsules</a>
  <a href="{root}biagio.html">AI Tutor</a><a href="{root}pricing.html">Pricing</a><a href="{root}faq.html">FAQ</a>
  <a href="{root}about.html">About</a><a href="{root}contact.html">Contact</a>
  <button class="btn btn-3d btn-3d-primary" data-advisor type="button" style="width:100%;margin-top:1.6rem">Reserve My Placement Call</button>
</aside>
"""

FOOTER = """<!--FOOTER-->
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="lt-main" style="font-family:var(--serif);font-size:1.5rem;color:var(--gold-soft);margin-bottom:.4rem">Club Italia</div>
        <div class="lt-sub" style="font-size:.6rem;letter-spacing:.28em;text-transform:uppercase;color:var(--on-dark-soft);margin-bottom:1.2rem">by eTeacher</div>
        <p>Club Italia by eTeacher, a culturally immersive, certified, live Italian language school for adult lifelong learners in the United States and around the world.</p>
        <p style="margin-top:1.2rem"><a href="mailto:advisor@eTeacherGroup.com" style="color:var(--gold-soft)">&#9993; advisor@eTeacherGroup.com</a></p>
      </div>
      <div class="footer-col"><h4>Courses</h4><a href="{root}courses.html">All Courses</a><a href="{root}pages/courses/ci1.html">CI Principiante</a><a href="{root}pages/courses/ci2.html">CI Elementare</a><a href="{root}pages/courses/ci3.html">CI Intermedio</a><a href="{root}pages/courses/ci4.html">CI Avanzato</a><a href="{root}pages/spoken/ps1.html">Parliamo Foundation</a><a href="{root}pages/spoken/ps4.html">Parliamo Confident</a></div>
      <div class="footer-col"><h4>Explore</h4><a href="{root}how-it-works.html">How It Works</a><a href="{root}method.html">Our Method</a><a href="{root}teachers.html">Teachers</a><a href="{root}culture.html">Culture</a><a href="{root}capsules.html">Culture Capsules</a><a href="{root}biagio.html">Biagio AI Tutor</a></div>
      <div class="footer-col"><h4>Company</h4><a href="{root}about.html">About Us</a><a href="{root}eteacher.html">eTeacher Group</a><a href="{root}pricing.html">Pricing</a><a href="{root}faq.html">FAQ</a><a href="{root}contact.html">Contact</a></div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 eTeacher Group. All rights reserved. Club Italia is a trading style of eTeacher Group.</p>
      <div class="footer-social"><a href="#" aria-label="Facebook">f</a><a href="#" aria-label="Instagram">&#9673;</a><a href="#" aria-label="YouTube">&#9654;</a></div>
    </div>
  </div>
</footer>
"""

def build_sticky_js(root=""):
    return '''<script src="''' + root + '''js/ci.js" defer></script>
<script>
document.addEventListener("DOMContentLoaded",()=>{
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add("in")}),{threshold:.14});
  document.querySelectorAll(".reveal").forEach(el=>io.observe(el));
  const h=document.querySelector(".site-header");
  const sb=document.querySelector(".sales-sticky-bottom");
  window.addEventListener("scroll",()=>{
    if(h)h.classList.toggle("scrolled",window.scrollY>40);
    if(sb)sb.classList.toggle("on",window.scrollY>400);
  });
  const drawer=document.getElementById("navDrawer");
  document.querySelector(".nav-toggle")?.addEventListener("click",()=>drawer.classList.add("open"));
  document.querySelector(".nav-drawer-close")?.addEventListener("click",()=>drawer.classList.remove("open"));
  const rot=["Autumn cohort opens Oct 6. 4 seats left in Chiara\\'s group.","Book a placement call this week and skip the $50 registration fee.","Marco\\'s Roma group filled in 48 hours. Next opens Oct 13.","Reserve now: 7-day full refund, no questions asked."];
  const rEl=document.getElementById("urg-rot");let ri=0;
  if(rEl)setInterval(()=>{ri=(ri+1)%rot.length;rEl.style.opacity=0;setTimeout(()=>{rEl.textContent=rot[ri];rEl.style.opacity=1},250)},4200);
});
</script>
</body></html>'''

def urgency(msg="Autumn cohort opens Oct 6. 4 seats left in Chiara's group."):
    return f'<div class="sales-urgency"><span class="dot"></span><b>LIVE</b><span id="urg-rot" style="transition:opacity .25s">{msg}</span> <a href="pricing.html">See pricing →</a></div>'

def sticky_bottom(price="$62/week"):
    return f'''<div class="sales-sticky-bottom">
      <span><b>{price}</b></span><span class="sep">·</span>
      <span class="stars">★★★★★</span> <span>4.8 on Trustpilot</span><span class="sep">·</span>
      <span><b>12 seats</b> left in October cohort</span>
      <button class="btn-sales-primary" data-advisor type="button">Reserve My Spot →</button>
    </div>'''

def head(title, desc, root=""):
    return f'''<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{root}css/ci.css">
{SALES_CSS}
</head><body>'''

print("OK helpers loaded")
