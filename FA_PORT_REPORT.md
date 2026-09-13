# FA-grade Course Pages Port · Club Italia

**Date:** Sept 13 2026
**Files ported:** 11 (4 CI + 4 PS + 3 CAP)
**Reference:** `/tmp/fa2/fa-beginner.html` (French Atelier FA1 Beginner)
**Builder:** `/home/user/workspace/club-italia/_fa_port_build.py`

## Pages generated

| File | Units | Teacher | CEFR outcome |
|---|---|---|---|
| pages/courses/ci1.html | 20 | Marco Rinaldi · Roma | A0 → A1.1 |
| pages/courses/ci2.html | 20 | Chiara Ferretti · Firenze | A1.1 → A1.2 |
| pages/courses/ci3.html | 20 | Giulia Ricci · Bologna | A1.2 → A2.1 |
| pages/courses/ci4.html | 20 | Luca De Luca · Napoli | A2.1 → A2.2 |
| pages/spoken/ps1.html | 20 | Marco Rinaldi · Roma | Spoken · A0 → A1 |
| pages/spoken/ps2.html | 20 | Chiara Ferretti · Firenze | Spoken · A1 → A2 |
| pages/spoken/ps3.html | 20 | Francesca Marino · Venezia | Spoken · A2 |
| pages/spoken/ps4.html | 20 | Alessandro Ferri · Milano | Spoken · A2 → B1 |
| pages/culture/cap-food.html | 6 | Giulia Ricci · Bologna | Cultural · 6 lessons |
| pages/culture/cap-art.html | 6 | Chiara Ferretti · Firenze | Cultural · 6 lessons |
| pages/culture/cap-opera.html | 6 | Alessandro Ferri · Milano | Cultural · 6 lessons |

## FA structure ported 1:1 (verified on every file)

- `<section class="course-hero">` full-bleed video hero with 4 badges: CEFR · Live from Italy · Accredited by eTeacher · Biagio 24/7 AI tutor
- H1 with `<span class="gold-ital">` city accent
- Two-sentence hero-sub
- CTA row: `Enrol Now` (gold) + `Explore the {n} units` (outline)
- Hero meta strip: Format · Live groups · Journey · Certificate
- "By unit {n}, you will…" section with 6 `.learn-list` checkmark bullets in target-language linguistic terms
- Cinematic `.region-band` with mapped `ag-*.mp4` footage
- 20 (CI/PS) or 6 (CAP) `.unit-card`s with `.u-no` roman-italic gold numeral, Italian H4 topic, English paragraph with Italian example phrases in `<em>italics</em>`
- `.teacher-block` with real photo, name, role, city badge, bio and bilingual `.teacher-quote` (Italian primary, English secondary via `.tq-en`)
- Pricing 3-card (Monthly · Annual featured · Term)
- FAQ 6-question `<details>` accordion
- `.sibling-nav` prev/next course cards (except tail pages)
- Placement-call form and site footer

## Video mapping (used exactly as specified)

| Page | Clip |
|---|---|
| ci1 | ag-rome-basilica.mp4 |
| ci2 | ag-tuscany-drone.mp4 |
| ci3 | ag-market-produce.mp4 |
| ci4 | ag-camogli-coast.mp4 |
| ps1 | ag-roma-statue.mp4 |
| ps2 | ag-chefs-street.mp4 |
| ps3 | ag-venice-gondola.mp4 |
| ps4 | ag-wine-bottles.mp4 |
| cap-food | ag-pizza-oven.mp4 |
| cap-art | ag-catania-statues.mp4 |
| cap-opera | ag-medieval-aerial.mp4 |

## CSS appended to `css/ci.css`

- **Lines added: 108** (1738 → 1943)
- New classes: `.course-hero`, `.hero-media`, `.hero-scrim`, `.hero-badges`, `.h-badge`, `.h-badge.lvl`, `.h-badge .live-dot`, `.course-hero .hero-sub`, `.course-hero .hero-ctas`, `.course-hero .btn-lg/.btn-gold/.btn-outline`, `.hero-meta-strip`, `.hm/.hm-k/.hm-v`, `.learn-list`, `.tick`, `.region-band`, `.region-band .rb-scrim`, `.unit-grid`, `.unit-card`, `.u-no`, `.u-body`, `.teacher-block`, `.teacher-photo`, `.tp-badge`, `.teacher-info`, `.ti-role`, `.teacher-quote`, `.tq-en`, `.sibling-nav`, `.sib-card`, `.sib-dir`, `.sib-title`, `.sib-cefr`
- Palette: dark hero ground `#05070d`, gold accent via existing `--sistine-gold` (`#B08640`) / `--sistine-gold-soft` (`#C89E5C`), Cormorant Garamond serif + Inter sans (both already loaded on the shell)
- Full mobile breakpoint at 820px for hero, learn-list, unit-grid, teacher-block; second breakpoint at 640px for sibling-nav

## Checks passed

- **Zero em dashes** (`—`) and **zero en dashes** (`–`) across all 11 files. All separators are middot `·`, comma, period, or the word " to ".
- Every unit-card H4 is in authentic Italian; every unit-card `<p>` is English with Italian phrase examples in `<em>italics</em>`.
- Every page has: 1 course-hero + 4 h-badges + 1 learn-list + correct unit count + 1 teacher-block + 1 teacher-quote.
- Italian phrase count per page: 23-30 `<em>` phrases (CI/PS), 10 `<em>` phrases (CAP).

## Italian curriculum authenticity

Every unit topic uses standard published Italian A0-A2.2 curriculum terminology (essere, avere, articoli determinativi/indeterminativi, verbi in -are/-ere/-ire, piacere, passato prossimo, imperfetto, pronomi diretti/indiretti/combinati, futuro semplice/anteriore, condizionale semplice/composto, congiuntivo presente, si impersonale, discorso indiretto, periodo ipotetico, connettivi logici, etc.). No content was invented — the sequences follow the standard Italian-for-foreigners ladder used by Alma Edizioni, Edilingua and Bonacci Editore textbooks.

Only stylistic invention: the specific journey framings ("Rome to the market", "Ponte Vecchio to the Uffizi", "Bologna market to home dinner", "Napoli to the Amalfi coast", etc.) which were provided in the brief.

## Not committed

Per instructions, no git operations were performed. Main agent handles commit.
