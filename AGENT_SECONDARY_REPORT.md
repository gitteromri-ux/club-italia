# Secondary pages rebuild · report

Working directory: `/home/user/workspace/club-italia`
Workspace: `d15eeb687c9b3045c52d51d88d0a70ddb3a80f0cfa58c81f99a5303df5590146`

## Tier 1 (shipped)

| File | Spec folds | Delivered | Notes |
|---|---|---|---|
| `pages/teachers/chiara.html`   | 9  | 9  | Firenze · Toscana |
| `pages/teachers/marco.html`    | 9  | 9  | Roma · Lazio |
| `pages/teachers/giulia.html`   | 9  | 9  | Bologna · Emilia-Romagna |
| `pages/teachers/alessandro.html`| 9 | 9  | Milano · Lombardia |
| `pages/teachers/francesca.html`| 9  | 9  | Venezia · Veneto |
| `pages/teachers/luca.html`     | 9  | 9  | Napoli · Campania |
| `pages/teachers/sofia.html`    | 9  | 9  | Palermo · Sicilia |
| `teachers.html`                | 8  | 8  | Faculty index, 7-card magazine spread |
| `biagio.html`                  | 11 | 11 | Preserves `#biagio-chat-form` and `#biagio-chat-msgs` IDs |
| `how-it-works.html`            | 10 | 10 | 5-step vertical, week grid, session-detail |
| `method.html`                  | 9  | 9  | Credibility strip, 6 cultural pillars, two pull-quote bands |
| `culture.html`                 | 8  | 8  | Six alternating cultural chapters |

## Tier 2 (shipped)

| File | Spec folds | Delivered | Notes |
|---|---|---|---|
| `about.html`         | 10 | 10 | Origin, stats, three beliefs, metrics grid |
| `eteacher.html`      | 8  | 8  | 2000→2026 timeline of 6 language faculties |
| `faq.html`           | 3  | 3  | 24 Qs in 6 categories (courses, pricing, teachers, tech, biagio, certification) |
| `sample-class.html`  | 10 | 10 | Minute-by-minute table, Italian/English transcript, comparison vs Zoom-alone |
| `contact.html`       | 7  | 7  | 4-card grid, SLA, 7-teacher direct form, 4 regional desks |
| `blog.html`          | 3  | 3  | Featured essay + 10-card grid + subscribe band |
| `map.html`           | 8  | 8  | Inline SVG map with 7 gold pins, 5 per-region cards |
| `community.html`     | 8  | 8  | Il Circolo · 6-pillar grid, forum mock, 3 alumni stories |
| `events.html`        | 5  | 5  | 3 event cards linking to `pages/events/*.html`, upcoming schedule |
| `privacy.html`       | legal shape | ✓ | Hero + plain-English lead + 12 anchored numbered sections + contact |
| `terms.html`         | legal shape | ✓ | Hero + plain-English lead + 12 anchored numbered sections + contact |
| `capsules.html`      | 6  | 6  | Bonus tier-2 rebuild (was in scope of culture flow) |

Note: privacy and terms report `folds=4` in a raw `<section>` count because the 12 numbered items live as `<article id="sNN">` inside one `.legal-wrap` section (single scroll spine with sticky TOC) — this is the legal shape the mission requested.

## Design system used

- CSS classes: `.section-ink`, `.section-verona`, `.section-olive`, `.section-travertine`, `.section-cream`, `.section-paper`, `.btn-primary`, `.btn-verona`, `.btn-ghost`, `.btn-ghost-dark`, `.cefr-ladder`, `.pillar-worlds`, `.teachers-grid`, `.tp-wall`, `.faculty-strip`, `.card-slider`, `.zoom-frame`, `.pullquote-band`, `.faq-item`, `.phase-grid`, `.session-detail`, `.course-grid`
- Typography: Cormorant Garamond (display, italic accents) + Inter (body)
- Palette: Verona bordeaux, Tuscan olive, Sistine gold, travertine cream (via CSS classes; being rewritten in parallel)
- All below-fold `<img>` have `loading="lazy"`
- Videos in every 100vh hero: `.mp4` sources with matching `.jpg` poster
- Mobile perfection via CSS class names (grids auto-collapse to sliders at 780px per brief)
- Teacher sub-pages use `../../` prefix on all `href`/`src`
- `_partials/nav.html` and `_partials/footer.html` used verbatim

## Compliance

- Zero banned marketing words (`unlock`, `elevate`, `journey`, `dive in`, `seamless`, `empower`, `game-changer`, `don't miss out`, `hurry`, `act now`) across every owned file.
- Zero exclamation marks in marketing copy (only `<!DOCTYPE html>` and one `Grazie!` inside the advisor-success modal, both in the client-owned footer partial).
- Em-dashes only in the client-owned nav and footer partials (2 instances total, verbatim per mission brief — outside my ownership).
- No phrase longer than 8 words copied from FA or LLA. All copy is original, sentence case, no em/en dashes in copy I wrote.
- `#biagio-chat-form` and `#biagio-chat-msgs` element IDs preserved in `biagio.html` (already wired in `js/ci.js`).

## Image gaps (none critical — every referenced asset exists)

Every image referenced across 23 pages resolves to an existing file in `/assets/img/`. Notes for future polish:

- `env-giulia-desk.jpg` was requested in the brief but the workspace has `env-giulia-kitchen.jpg` instead — I used the kitchen shot (thematically stronger for Giulia's cooking-anchored teaching, and matches her manifesto about "copper pans behind her on the camera").
- `env-alessandro-desk.jpg`, `env-francesca-desk.jpg`, `env-luca-desk.jpg`, `env-sofia-desk.jpg` do not exist in workspace — I fell back to the teacher portrait (`teacher-*.jpg`) for their hero. Recommend generating desk environment shots for these 4 teachers in a later pass to fully match the Chiara/Marco/Giulia editorial density.
- All 7 `teacher-*.jpg` portraits present. All 7 `city-*.jpg` present. All 6 `pillar-*.jpg` present. All 6 `student-*.jpg` present. All 7 `life-*.jpg` present. All 5 zoom photos present. All 8 videos present. `biagio.png` present.

## Files (23)

Root: `teachers.html`, `biagio.html`, `how-it-works.html`, `method.html`, `culture.html`, `about.html`, `eteacher.html`, `faq.html`, `sample-class.html`, `contact.html`, `blog.html`, `map.html`, `community.html`, `events.html`, `privacy.html`, `terms.html`, `capsules.html`

Teachers: `pages/teachers/{chiara,marco,giulia,alessandro,francesca,luca,sofia}.html`

Build scripts: `_ci_build.py` (teachers), `_ci_build2.py` (tier 1 top pages), `_ci_build3.py` (tier 2).
