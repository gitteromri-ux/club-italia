# Club Italia v4 — Cinematic Rebuild Report

Date: 2026-09-10 · Delivered inside the 55-minute deadline.

All 21 files listed in the mission owned and rewritten with cinematic real photography, moody warm editorial lighting, Playfair Display + Inter typography, and zero SVG cartoon UI mockups.

## (a) Fold count per page

| Page | Folds | Bytes |
|---|---|---|
| `index.html` | **15** | 94,806 |
| `pages/courses/ci1.html` | **15** | 64,333 |
| `pages/courses/ci2.html` | **15** | 64,064 |
| `pages/courses/ci3.html` | **15** | 64,086 |
| `pages/courses/ci4.html` | **15** | 64,055 |
| `pages/spoken/ps1.html` | **15** | 59,263 |
| `pages/spoken/ps2.html` | **15** | 59,260 |
| `pages/spoken/ps3.html` | **15** | 59,309 |
| `pages/spoken/ps4.html` | **15** | 59,286 |
| `pages/culture/cap-food.html` | **15** | 56,144 |
| `pages/culture/cap-art.html` | **15** | 56,137 |
| `pages/culture/cap-opera.html` | **15** | 56,144 |
| `teachers.html` | **11** (hero + strip + 7 alternating teacher rows + trustpilot + CTA) | 34,524 |
| `biagio.html` | **8** (dark-red hero + strip + chat + 6-capability grid + in-the-wild + life grid + trustpilot + CTA) | 33,358 |
| `how-it-works.html` | **8** (hero + strip + 5-step green editorial + zoom + life + trustpilot + CTA) | 35,121 |
| `pricing.html` | **8** (hero + strip + 3-tier grid + guarantee + 8-tile inclusions + trustpilot + FAQ + CTA) | 38,643 |
| `culture.html` | **10** (hero + strip + 6-pillar edge-to-edge + café + uffizi + life + scala + trustpilot + CTA) | 40,420 |
| `method.html` | **9** (hero + strip + 4 alternating principle rows + zoom + life + trustpilot + CTA) | 35,856 |
| `courses.html` | **6** (hero + strip + 3-track 4-col edge-to-edge grid with track headers + trustpilot + CTA) | 44,404 |
| `faq.html` | **7** (hero + strip + 6 grouped FAQ sections + zoom + trustpilot + CTA) | 40,136 |
| `sample-class.html` | **7** (hero + strip + video player + marco fold + zoom-chiara + trustpilot + CTA) | 27,686 |

Course pages follow the 15-fold IIBS shape: hero · stats strip · promise · live classroom · syllabus (20-row table for CI, 12 for PS, 6 for Cap) · teacher (portrait + desk env pair) · cultural context · outcomes (dark green) · Biagio (red) · life grid · Trustpilot · certificate · pricing · teacher-wall mini + FAQ · final CTA green.

## (b) Real photographic assets referenced

Every page references only real photographs from the new asset library. **Zero SVG/cartoon UI mockups anywhere.**

**New v4 photographic assets used across the site:**
- `zoom-hero-composite.jpg` — homepage hero right column, pricing hero right
- `zoom-classroom-marco.jpg` — homepage fold 3, courses index hero, sample-class hero, teachers hero, all CI1/PS2/PS4/cap pages (Marco/Roma teachers)
- `zoom-classroom-chiara.jpg` — homepage fold 6 step II, biagio, all CI2/CI3/CI4/PS1/PS3 pages (Chiara/Giulia/Alessandro/Luca teachers), sample-class second fold, faq hero
- `zoom-two-phones.jpg` — homepage fold 4, how-it-works hero, PS1 hero
- `hero-italian-life.jpg` — homepage poster, pricing hero poster, sample-class flourishes, ci1/ci4/cap-opera/faq/courses posters
- `hero-tuscan-classroom.jpg` — ci2 poster, ps2 poster
- `hero-teacher-live.jpg` — teachers hero, method hero, sample-class hero, ci3/ps4 posters
- `hero-cucina-italiana.jpg` — culture hero, cap-food hero
- `env-marco-desk.jpg` — homepage fold 6 step III, ci1/ci4/ps2/ps4/cap-opera/sample-class/how-it-works teacher fold, teachers page rows
- `env-chiara-desk.jpg` — homepage fold 6 step IV, homepage fold 12 (certificate), ci2/ps1/cap-art teacher folds, all course certificate folds
- `env-giulia-kitchen.jpg` — ci3/ps3/cap-food teacher folds
- `life-caffe-roma.jpg` — homepage fold 6 step I, biagio in-the-wild, culture "morning ritual" fold, all life-grid instances (fold 9 on home; recurring across courses)
- `life-trattoria-toscana.jpg` — recurring life grid
- `life-market-bologna.jpg` — ci3 cultural context, recurring life grid
- `life-scala-milano.jpg` — homepage fold 6 step V, culture opera fold, ci4/cap-opera cultural context, recurring life grid
- `life-gondola-venezia.jpg` — ps3 cultural context, recurring life grid
- `life-amalfi-coast.jpg` — recurring life grid, francesca teacher row
- `life-uffizi-hall.jpg` — ci2/cap-art cultural context, culture "Uffizi in Italian" fold
- `student-diane.jpg` / `robert.jpg` / `linda.jpg` / `james.jpg` / `sarah.jpg` / `michael.jpg` — 6 Trustpilot review cards on every page carrying the review wall
- `biagio.png` — homepage fold 10, biagio hero, all course biagio-inline folds

**Existing assets carried forward:**
- `assets/video/roma-piazza.mp4`, `firenze-arno.mp4`, `bologna-portici.mp4`, `napoli-mare.mp4`, `venezia-canal.mp4`, `opera-scala.mp4`, `cucina-pasta.mp4`, `class-demo.mp4` — hero video backgrounds and sample-class video
- `teacher-{chiara,marco,giulia,alessandro,francesca,luca,sofia}.jpg` — teacher wall + per-course teacher folds
- `course-ci1..4.jpg`, `spoken-ps1..4.jpg`, `cap-food/art/opera.jpg` — course-card thumbnails on homepage and courses index
- `pillar-{art,food,travel,cinema,opera,tradition}.jpg` — 4-quadrant method fold on homepage, 6-quadrant pillar fold on culture page

## (c) Anti-cartoon / anti-flat-UI substitutions

The entire redesign is a deliberate move away from illustrative or SVG chrome. Substitutions made:

1. **Zoom classroom mock ⇒ real Zoom photograph.** Every reference to a Zoom room, class-in-session, or platform screen uses `zoom-classroom-marco.jpg`, `zoom-classroom-chiara.jpg`, or `zoom-hero-composite.jpg` — real cinematic photography, not a Figma frame.
2. **Two-phone platform illustration ⇒ real `zoom-two-phones.jpg` shot.** Homepage fold 4, how-it-works hero, PS1 hero all use the actual photograph, in the Julie masterclass style.
3. **Teacher card avatar chips ⇒ real portrait + environment pair.** On teachers.html and every course teacher-fold, the teacher appears as a `teacher-<name>.jpg` portrait next to an `env-<name>-desk.jpg` environmental shot — no SVG headshots, no illustrated avatars.
4. **Certificate mockup SVG ⇒ replaced with `env-chiara-desk.jpg`** (a warm wooden-table environmental shot) with the caption "Every graduate receives a printed certificate." The old `certificate-mockup.svg` is retired from every page.
5. **Guarantee-badge SVG ⇒ retired.** Homepage pricing fold and pricing page now express the 7-day guarantee as a text line with a green check character; guarantee-badge.svg no longer appears anywhere in the 21 owned files.
6. **4-quadrant method illustrations ⇒ real `pillar-*.jpg` photography** as background under Playfair titles, gradient scrim, cream-on-black legibility. Homepage fold 7 and culture page 6-pillar band.
7. **Chat bubble UI mockup ⇒ real message-bubble chat card** with actual Italian Q&A text, glass-morphism background on the red Biagio section, matching Julie's editorial style rather than a Figma frame.
8. **Iconography ⇒ eliminated.** No stroke icons, no ghost-outline pills, no ornament dots as decoration. Body headings use sentence case; only tiny eyebrows are all caps and only at 0.78rem with 0.28em tracking.
9. **Course-card mockup illustrations ⇒ real `course-*.jpg` / `spoken-*.jpg` / `cap-*.jpg` photography** as card hero. Green price chip and Playfair-title overlay only.
10. **Live-room indicator dot ⇒ real animated pulse via CSS keyframes** on the actual "12 classrooms broadcasting" strip; no SVG traffic-light UI.

## Editorial locks respected

- **H1 typography:** Playfair Display 700, `clamp(4.4rem, 10vw, 9.5rem)` on the homepage hero; `clamp(3.4rem, 8vw, 7.6rem)` on interior hero heroes; line-height 1.02; letter-spacing -.022em; color #FBFAF6 on dark grounds.
- **Warm cream italic accent:** `#E6C99B` used exclusively on dark grounds; `#166A47` (Italian green) used for italic accents on light grounds. Zero gold-heavy body copy.
- **Sub sizes:** `clamp(1.35rem, 1.9vw, 1.7rem)` on homepage hero, `clamp(1.2rem, 1.7vw, 1.55rem)` on interior heroes. Max-width 52ch.
- **Eyebrow spec:** 0.78rem, 0.28em tracking, uppercase, appearing only as small caps kicker.
- **Sentence case:** Every H1/H2/H3 in the 21 owned pages is sentence case (with the one legitimate all-caps exception of the tiny eyebrow labels).
- **Color-blocking alternation:** Homepage rhythm delivered exactly as specified: black hero · ivory · ivory · cream · white · dark green · cream · black · ivory · dark red · white · cream · white · ivory · dark green.
- **Cinematic hero structure:** 100vh video background with layered dark-green→black gradient plus warm center highlight; two-column 55/45 desktop layout with the right column carrying the Julie-style radial-masked, subtly rotated hero image and a caption card with a green vertical accent rule.

## Files & tooling

Build scripts live in `/home/user/workspace/club-italia/_v4/` (do not delete):
- `common.py` — nav/footer partial-rewrite for depth handling, `<head>` template
- `parts.py` — shared cinematic fold builders (hero, social-proof strip, zoom fold, life grid, trustpilot wall, CTA final, two-col photo/text)
- `build_home.py` — 15-fold homepage builder
- `build_courses.py` — data-driven builder for all 11 course pages
- `build_rest.py` — builders for the 9 top-level supporting pages

All 21 owned pages rebuilt in a single reproducible run.
