# The French Atelier — Design System Extraction

Extracted from https://www.frenchatelierlive.com/ (home, `cultural-resources.html`, `course-fa1.html`) and the linked stylesheet `https://www.frenchatelierlive.com/css/fa.css?v=1789022625`.

The FA CSS is self-describing: it declares itself as an *"Editorial luxury: ivory + navy/black, gold accents. Cormorant Garamond (display, ital emphasis) + Inter (UI/body)"* design system. Tokens are locked to a brand deck and organized as CSS custom properties on `:root`.

---

## 1. Fonts

**Loader** — Google Fonts `<link rel="preconnect">` + a single `@import` inside `fa.css`:

```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=Inter:wght@300;400;500;600;700&display=swap');
```

Preconnect hints in `<head>`:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

**Font stack tokens**
```css
--serif: 'Cormorant Garamond', Georgia, serif;    /* display + italic emphasis */
--sans : 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;  /* UI + body */
```

- **Display**: Cormorant Garamond, weights 400–700, both roman + italic. Used for `h1–h4`, section titles, editorial pullquotes. Italics are the signature accent (e.g. "*live from France*").
- **Body/UI**: Inter, weights 300–700. Used for body, buttons, nav, eyebrows.
- **No script font** — the "French" feel comes from Cormorant italics + gold rules + navy, not a script face.

---

## 2. Color Palette — official brand tokens

All from `:root`. Comments in the CSS mark them as "OFFICIAL BRAND PALETTE (locked to brand deck)".

| Role | Token | Hex | Notes |
|---|---|---|---|
| Anchor navy (primary) | `--navy` / `--ink` | `#000034` | Primary anchor, dark bg, headline color on light |
| Deepest navy | `--navy-deep` | `#00001F` | Gradient base, footer bg |
| Lifted navy | `--navy-soft` | `#1C2238` | Card bg on dark |
| Mid navy | `--navy-mid` | `#00003E` | |
| Navy line | `--navy-line` | `#000049` | |
| Ink soft | `--ink-soft` | `#3A3F5C` | Muted text on light |
| **Gold** (primary accent) | `--gold` | `#C8A96B` | Buttons, dividers, hover |
| Gold soft | `--gold-soft` | `#D8BC85` | Nav hover, on-dark eyebrow |
| Gold deep | `--gold-deep` | `#A98D52` | Eyebrow on light |
| Gold line | `--gold-line` | `rgba(200,169,107,.45)` | Borders on frames |
| Gold line soft | `--gold-line-soft` | `rgba(200,169,107,.22)` | Very faint dividers |
| **Ivory** (main light bg) | `--ivory` | `#F3EFE9` | Main warm beige page bg |
| Paper | `--paper` | `#FAF7F1` | Lifted beige — actual `body{background}` |
| Cream | `--cream` | `#E9E1D2` | |
| Cream deep / taupe | `--cream-deep` | `#D8CAB5` | Supportive |
| Parisian pink | `--pink` | `#F3D3D9` | Bullets, icons, chips |
| Pink soft | `--pink-soft` | `#FBEFF2` | Lightest pink bg |
| Pink mid | `--pink-mid` | `#E498A6` | |
| Pink deep | `--pink-deep` | `#C77E94` | |
| Terracotta | `--terra` | `#C76F50` | Decorative headings, quote marks |
| Terracotta soft | `--terra-soft` | `#E2B5A5` | |
| Terracotta deep | `--terra-deep` | `#A95436` | |
| Burgundy | `--burgundy` | `#6B1E2C` | Rare accent |
| White | `--white` | `#FFFFFF` | |

**On-dark text tokens**
```css
--on-dark:      #F3EEE3;
--on-dark-soft: rgba(243,238,227,.66);
--on-dark-faint:rgba(243,238,227,.40);
--dark-line:    rgba(243,238,227,.18);
--dark-line-soft:rgba(243,238,227,.10);
```

**On-light text tokens**
```css
--on-light:      #1A1E33;
--on-light-soft: rgba(26,30,51,.66);
--on-light-faint:rgba(26,30,51,.42);
--light-line:    rgba(26,30,51,.14);
```

> Note — there is **no French tricolor** anywhere. The "French" cue is navy + gold + Parisian pink + terracotta + Cormorant italics, not blue-white-red flag colors.

---

## 3. Type Scale

```css
body { font-family: var(--sans); font-size: 17px; line-height: 1.7; font-weight: 400; }
h1   { font-family: var(--serif); font-size: clamp(2.6rem, 6vw, 4.8rem);  line-height: 1.00; }
h2   { font-family: var(--serif); font-size: clamp(1.8rem, 3.2vw, 2.8rem); line-height: 1.06; font-weight: 600; }
h3   { font-family: var(--serif); font-size: clamp(1.7rem, 2.6vw, 2.3rem); line-height: 1.08; font-weight: 600; }
.eyebrow { font-family: var(--sans); font-size: .72rem; font-weight: 600;
           letter-spacing: .28em; text-transform: uppercase; color: var(--gold-deep); }
```

Notes: eyebrow is the signature — small gold uppercase kicker above every section title, tracked at `.28em`.

---

## 4. Layout Tokens

```css
--maxw:        1240px;   /* .wrap max width */
--maxw-narrow: 880px;
--radius:      3px;      /* buttons, cards — extremely subtle */
--ease:        cubic-bezier(.22,.61,.36,1);

/* Spacing scale */
--sp-1:.5rem;  --sp-2:1rem;  --sp-3:1.5rem; --sp-4:2rem; --sp-5:3rem;
--sp-6:4rem;   --sp-7:6rem;  --sp-8:8rem;   --sp-9:11rem;

.wrap { max-width: var(--maxw); margin: 0 auto; padding: 0 2rem; }
```

`--radius: 3px` is deliberately near-square — nothing pillowy.

---

## 5. Buttons

```css
.btn {
  display: inline-flex; align-items: center; gap: .6rem;
  font-family: var(--sans); font-size: .8rem; font-weight: 600;
  letter-spacing: .16em; text-transform: uppercase;
  padding: 1.05rem 2.1rem;
  border-radius: var(--radius); /* 3px */
  transition: all .4s var(--ease);
  cursor: pointer;
}

.btn-gold    { background: var(--gold); color: var(--navy-deep); }
.btn-gold:hover { background: var(--gold-soft);
                  transform: translateY(-2px);
                  box-shadow: 0 12px 30px rgba(200,165,96,.28); }

.btn-outline { border: 1px solid var(--gold-line);
               color: var(--gold-deep); background: transparent; }
/* On dark surfaces, outline uses lighter tokens: */
.on-dark .btn-outline { color: var(--gold-soft);
                        border-color: rgba(200,165,96,.5); }
```

Signatures: uppercase, 0.16em tracking, tiny radius, gold-on-navy primary, subtle lift + gold-glow shadow on hover.

---

## 6. Navigation

```css
.site-header {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  padding: 1.5rem 0;
  transition: background .45s var(--ease), padding .45s var(--ease), box-shadow .45s var(--ease);
}
.site-header.scrolled {
  background: rgba(0,0,31,.94);
  backdrop-filter: blur(16px);
  padding: .95rem 0;
  box-shadow: 0 1px 0 var(--dark-line-soft),
              0 18px 40px -28px rgba(0,0,0,.6);
}

.nav      { display: flex; align-items: center; justify-content: space-between; gap: 1.5rem; }
.nav-logo-img { height: 56px; transition: height .45s var(--ease); }

.nav-link {
  font-family: var(--sans); font-size: .8rem; font-weight: 500;
  letter-spacing: .06em; color: var(--on-dark);
  padding: .7rem .95rem; border-radius: 8px;
}
.nav-link::after {          /* gold underline reveal on hover */
  content:""; position: absolute; left:.95rem; right:.95rem; bottom:.42rem;
  height: 1.5px; background: var(--gold-soft);
  transform: scaleX(0); transform-origin: left;
  transition: transform .32s var(--ease); border-radius: 2px;
}
.nav-link:hover { color: var(--gold-soft); background: rgba(243,238,227,.05); }
.nav-link:hover::after,
.nav-link.active::after { transform: scaleX(1); }
```

- **Fixed** (not sticky) header, transparent at top of the page and turning to a translucent navy `rgba(0,0,31,.94)` with `blur(16px)` after ~scroll.
- Logo shrinks from 56 px → smaller on scroll via the same easing.
- Nav links: uppercase-ish (`.06em` tracking), gold underline reveals on hover, active link keeps underline.
- On light-hero pages, `body.light-hero .site-header` uses the tinted navy at rest too.

---

## 7. Video / Hero / Scrim System

The CSS documents three canonical video roles:

```
1. .video-bg    — full-bleed ambient bg inside any .hero / .page-hero / .video-section
2. .video-frame — a bordered editorial video block (in splits/cards)
3. .sound-video — click-to-unmute (for FA class footage with real audio)
All ambient videos: autoplay muted loop playsinline (handled in fa.js).
```

```css
.hero        { position: relative; min-height: 100vh;
               display: flex; align-items: center;
               color: var(--on-dark); overflow: hidden; }

.video-bg    { position: absolute; inset: 0; z-index: 0; overflow: hidden; }
.video-frame { position: relative; border: 1px solid var(--gold-line-soft);
               overflow: hidden; background: var(--navy-deep); }

/* Editorial gradient scrims — always over navy-deep #08 0E 2B ≈ rgba(8,14,43,x) */
.hero-bg::after      { content:""; position:absolute; inset:0;
  background: linear-gradient(105deg,
    rgba(8,14,43,.86) 0%,
    rgba(8,14,43,.62) 42%,
    rgba(8,14,43,.28) 100%); }

.page-hero::after    { background: linear-gradient(180deg,
    rgba(8,14,43,.70), rgba(8,14,43,.92)); }

.video-bg::after     { background: linear-gradient(180deg,
    rgba(8,14,43,.55), rgba(8,14,43,.78)); }

.video-bg.tint-soft::after { background: linear-gradient(180deg,
    rgba(8,14,43,.35), rgba(8,14,43,.60)); }

.video-band .video-bg::after {
    background: linear-gradient(90deg,
      rgba(8,14,43,.90) 0%, rgba(8,14,43,.78) 45%,
      rgba(8,14,43,.50) 72%, rgba(8,14,43,.25) 100%); }

.wrap        { position: relative; z-index: 3; }  /* content sits above scrim */

.page-hero   { padding: 11rem 0 5rem; background: var(--navy);
               color: var(--on-dark); overflow: hidden; }
```

**Formula** — full-bleed `<video autoplay muted loop playsinline>` inside `.video-bg`, an `::after` linear-gradient scrim in navy-deep at 55–92% opacity for legibility, then content in `.wrap` at `z-index: 3`. The 105° diagonal on the home hero is the signature — it darkens the left where the headline sits and lets the video breathe on the right.

Sound toggle for `.sound-video`:
```css
.sound-toggle {
  position: absolute; bottom: 1rem; right: 1rem;
  background: rgba(8,14,43,.82); color: var(--gold-soft);
  border: 1px solid var(--gold-line);
  padding: .6rem 1.1rem; font-size: .7rem;
  letter-spacing: .14em; text-transform: uppercase;
  border-radius: 2px; backdrop-filter: blur(6px);
}
```

Hero content pulled left with `padding-left: clamp(8rem, 20.5vw, 18rem)` so the headline aligns under "Courses" in the nav.

---

## 8. Footer

```css
footer {
  background: var(--navy-deep);          /* #00001F */
  color: var(--on-dark);
  padding: 5rem 0 2.5rem;
  position: relative;
}
.footer-top   { display: grid;
                grid-template-columns: 1.4fr 1fr 1fr 1fr;
                gap: 2.5rem; padding-bottom: 3rem;
                border-bottom: 1px solid var(--dark-line-soft); }
.footer-bottom{ display: flex; justify-content: space-between;
                align-items: center; flex-wrap: wrap; gap: 1rem;
                padding-top: 2rem; }
.footer-social{ display: flex; gap: 1rem; }
```

4-column grid — first column (brand/blurb) is wider (1.4fr), the next three are link columns, then a bottom bar with legal + socials.

---

## 9. Signature Visual Elements (rebuild checklist)

1. **Navy anchor + gold accent** — `#000034` and `#C8A96B` do all the heavy lifting.
2. **Cormorant Garamond italics** for emotive words ("*live*", "*France*", "*maîtrise*").
3. **Gold-uppercase eyebrows** at `.28em` tracking over every section title.
4. **Diagonal 105° navy scrim** over hero video — this is the visual signature.
5. **Ambient full-bleed muted looping video** in every hero and several bands.
6. **Bordered `.video-frame` blocks** with `1px solid var(--gold-line-soft)` — editorial "framed" videos inside content sections.
7. **Warm beige page bg** (`--paper #FAF7F1`) not pure white — the "ivory" feel.
8. **Parisian pink + terracotta** as decorative accents (chips, icons, quote glyphs, small illustrations), sparse.
9. **3 px radius everywhere** — barely rounded, editorial.
10. **Fixed nav that condenses on scroll**, logo shrinks, gold underline reveal.
11. **Uppercase, wide-tracked buttons** with subtle gold shadow on hover.
12. Radial-gradient warm washes on light sections (see below).

Warm radial washes on light sections use color-mixed accents:
```css
background:
  radial-gradient(125% 150% at 10%  4%, color-mix(in srgb, var(--w-accent)  34%, transparent), transparent 52%),
  radial-gradient(120% 130% at 92% 100%, color-mix(in srgb, var(--w-accent2) 40%, transparent), transparent 56%),
  radial-gradient(130%  90% at 18%  0%, rgba(196,122,78,.16) 0%, transparent 46%),
  radial-gradient(120%  90% at 88% 14%, rgba(228,166,184,.14) 0%, transparent 44%),
  radial-gradient(140% 120% at 50% 120%, rgba(200,165,96,.10)  0%, transparent 55%);
```

---

# Italian Adaptation — Club Italia Palette & Font Proposal

Same architecture, warmer Mediterranean skin. Keep the FA layout DNA (Cormorant italics, eyebrow + rule, diagonal video scrim, gold-on-dark primary button, 3 px radius, warm ivory bg) — swap the anchor color and second accent for an Italian palette.

## Italian Font Stack

```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=Inter:wght@300;400;500;600;700&display=swap');

--serif : 'Cormorant Garamond', Georgia, serif;   /* keep — reads Italianate too */
--sans  : 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

Alternative editorial serifs (all Google Fonts, drop-in for `--serif`):
- **Playfair Display** — more geometric, high contrast, luxury Milanese feel.
- **Instrument Serif** — trendier, lower contrast, humanist.
- **Cormorant Garamond** *(default — stays closest to FA rhythm)*.

Alternative humanist sans for `--sans`:
- **Inter** (default, matches FA metrics).
- **DM Sans** — softer, warmer, slightly more Italian.

## Italian Color Palette (drop-in tokens)

```css
:root {
  /* ===== ANCHOR — Deep Bordeaux / Barolo (replaces --navy) ===== */
  --barolo:        #7A1F2B;   /* primary anchor, dark bg, headline on light */
  --barolo-deep:   #5A1520;   /* gradient base, footer */
  --barolo-soft:   #8F2E3B;   /* lifted */
  --barolo-mid:    #6A1924;
  --barolo-line:   #4C1219;
  --ink:           #2A0F14;   /* body text on light (softer than pure black) */
  --ink-soft:      #5A3A40;

  /* ===== GOLD ACCENT — kept (universal luxury cue) ===== */
  --gold:          #C9A24B;
  --gold-soft:     #DDB971;
  --gold-deep:     #A9863A;
  --gold-line:     rgba(201,162,75,.45);
  --gold-line-soft:rgba(201,162,75,.22);

  /* ===== TUSCAN CREAM — main warm bg (replaces --ivory) ===== */
  --cream:         #F5E9D3;   /* main Tuscan cream page bg */
  --paper:         #FBF4E4;   /* lifted cream — use as body bg */
  --sand:          #EADFC6;
  --sand-deep:     #D7C7A2;   /* taupe */

  /* ===== TERRACOTTA — decorative accent (replaces --terra) ===== */
  --terracotta:      #B04A2E;
  --terracotta-soft: #E1A78E;
  --terracotta-deep: #8A3620;

  /* ===== OLIVE — supportive Mediterranean secondary ===== */
  --olive:         #6E7A3A;
  --olive-soft:    #9AA46A;

  /* ===== ITALIAN TRICOLOR — sparingly, badges/flags only ===== */
  --it-green:      #009246;
  --it-white:      #F4F5F0;
  --it-red:        #CE2B37;

  /* On-dark text (over barolo) */
  --on-dark:       #F5E9D3;
  --on-dark-soft:  rgba(245,233,211,.70);
  --on-dark-faint: rgba(245,233,211,.42);
  --dark-line:     rgba(245,233,211,.18);
  --dark-line-soft:rgba(245,233,211,.10);

  /* On-light text (over cream) */
  --on-light:      #2A0F14;
  --on-light-soft: rgba(42,15,20,.66);
  --on-light-faint:rgba(42,15,20,.42);
  --light-line:    rgba(42,15,20,.14);
}
```

## Italian scrim (video hero)

Swap the `rgba(8,14,43,x)` navy scrim for barolo-deep at the same opacities:

```css
.hero-bg::after   { background: linear-gradient(105deg,
   rgba(90,21,32,.88) 0%, rgba(90,21,32,.62) 42%, rgba(90,21,32,.28) 100%); }
.page-hero::after { background: linear-gradient(180deg,
   rgba(90,21,32,.72), rgba(90,21,32,.92)); }
.video-bg::after  { background: linear-gradient(180deg,
   rgba(90,21,32,.55), rgba(90,21,32,.80)); }
```

## Italian button (drop-in replacement)

```css
.btn-gold        { background: var(--gold);      color: var(--barolo-deep); }
.btn-gold:hover  { background: var(--gold-soft);
                   box-shadow: 0 12px 30px rgba(201,162,75,.32);
                   transform: translateY(-2px); }
.btn-outline     { border: 1px solid var(--gold-line);
                   color: var(--gold-deep); background: transparent; }
.on-dark .btn-outline { color: var(--gold-soft);
                        border-color: rgba(221,185,113,.55); }
```

## Tricolor use-guardrails
- Never as page or section background.
- Allowed: a **thin 3-band rule under the logo lockup** (green/white/red at ~4 px total height), a **tiny flag chip** on the "Made in Italy" seal, a **green underline on the primary nav active link** *as an alternative to the gold*.
- Everything else stays Barolo + Gold + Cream + Terracotta + Olive.

## Italian body defaults

```css
body {
  font-family: var(--sans);
  background: var(--paper);       /* #FBF4E4 warm cream */
  color: var(--on-light);         /* #2A0F14 */
  font-size: 17px; line-height: 1.7; font-weight: 400;
}
h1 { font-family: var(--serif); color: var(--on-dark);  /* over barolo hero */ }
h2, h3 { font-family: var(--serif); color: var(--on-light); font-weight: 600; }
.eyebrow { color: var(--gold-deep); letter-spacing: .28em;
           font-size: .72rem; text-transform: uppercase; font-weight: 600; }
```

Layout tokens (`--maxw 1240`, `--radius 3px`, spacing scale, `--ease`), the fixed-header behaviour, the video/scrim/`video-frame` system, the footer 4-column grid, and the eyebrow-plus-title rhythm all carry over unchanged.

---

## Sources

- Home page HTML — https://www.frenchatelierlive.com/
- Cultural resources page — https://www.frenchatelierlive.com/cultural-resources.html
- Course page — https://www.frenchatelierlive.com/course-fa1.html
- Stylesheet (all tokens above are direct quotes) — https://www.frenchatelierlive.com/css/fa.css?v=1789022625
