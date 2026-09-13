# Club Italia — Real photos + Italian music (report)

_Delivered by the "real human photos + Italian music" subagent — 2026‑09‑13._

All human-face imagery is a **real photograph from Unsplash** (regular Unsplash Photos, `source="Unsplash"`, standard [Unsplash License](https://unsplash.com/license) — free for commercial and non-commercial use, no attribution required, credit encouraged). **Zero AI-generated faces.** Music is a public-recording excerpt of Vivaldi's _Four Seasons — Spring_ under CC BY-SA 3.0.

---

## 1 · Assets table

| File | Dim (px) | Size | Source URL (CDN) | Provider page (attribution) | License |
|---|---|---|---|---|---|
| `assets/img/teacher-chiara.jpg` | 1200×1800 | 254 KB | https://images.unsplash.com/photo-1508978644997-53cc5bfb8a03 | https://unsplash.com/photos/photo-1508978644997-53cc5bfb8a03 | Unsplash License |
| `assets/img/teacher-marco.jpg` | 1200×1600 | 461 KB | https://images.unsplash.com/photo-1603570112520-fdc514048979 | https://unsplash.com/photos/photo-1603570112520-fdc514048979 | Unsplash License |
| `assets/img/teacher-giulia.jpg` | 1200×1769 | 304 KB | https://images.unsplash.com/photo-1592621385645-e41659e8aabe | https://unsplash.com/photos/photo-1592621385645-e41659e8aabe | Unsplash License |
| `assets/img/teacher-alessandro.jpg` | 1200×1800 | 207 KB | https://images.unsplash.com/photo-1560250097-0b93528c311a | https://unsplash.com/photos/photo-1560250097-0b93528c311a | Unsplash License |
| `assets/img/teacher-francesca.jpg` | 1200×1798 | 443 KB | https://images.unsplash.com/photo-1544005313-94ddf0286df2 | https://unsplash.com/photos/photo-1544005313-94ddf0286df2 | Unsplash License |
| `assets/img/teacher-luca.jpg` | 1200×1200 | 135 KB | https://images.unsplash.com/photo-1595152772835-219674b2a8a6 | https://unsplash.com/photos/photo-1595152772835-219674b2a8a6 | Unsplash License |
| `assets/img/teacher-sofia.jpg` | 1200×1500 | 298 KB | https://images.unsplash.com/photo-1568739253582-afa48fbcea47 | https://unsplash.com/photos/photo-1568739253582-afa48fbcea47 | Unsplash License |
| `assets/img/zoom-classroom-masterclass.jpg` | 1920×1080 | 454 KB | (composite built with PIL) | 7 real Unsplash photos listed below | Unsplash License (per-source) |
| `assets/img/poster-roma-golden.jpg` | 3840×2560 | 1.82 MB | https://images.unsplash.com/photo-1636804907108-fa8d2e0f7a90 | https://unsplash.com/photos/photo-1636804907108-fa8d2e0f7a90 | Unsplash License |
| `assets/img/poster-tuscany-cypress.jpg` | 3840×2560 | 2.70 MB | https://images.unsplash.com/photo-1745506979034-1caeb8c76c32 | https://unsplash.com/photos/photo-1745506979034-1caeb8c76c32 | Unsplash License |
| `assets/img/poster-venice-canal.jpg` | 3840×2560 | 2.28 MB | https://images.unsplash.com/photo-1769522354640-5e725ca18125 | https://unsplash.com/photos/photo-1769522354640-5e725ca18125 | Unsplash License |
| `assets/img/poster-firenze-duomo.jpg` | 3840×2560 | 2.08 MB | https://images.unsplash.com/photo-1775343970007-d70d54e86526 | https://unsplash.com/photos/photo-1775343970007-d70d54e86526 | Unsplash License |
| `assets/img/poster-napoli-amalfi.jpg` | 3840×2560 | 3.69 MB | https://images.unsplash.com/photo-1612698093158-e07ac200d44e | https://unsplash.com/photos/photo-1612698093158-e07ac200d44e | Unsplash License |
| `assets/audio/hero-italian-theme.mp3` | 75.00 s · 128 kbps · 44.1 kHz stereo | 1.14 MB | https://www.classicals.de/s/Classicalsde-Vivaldi-The-Four-Seasons-01-John-Harrison-with-the-Wichita-State-University-Chamber-Pla.mp3 | https://www.classicals.de/vivaldi-seasons | CC BY-SA 3.0 |

### Note on photographer credit
Unsplash photo pages block direct access from the crawler used here, so specific photographer names were not extracted programmatically inside the deadline. Every image comes from `source="Unsplash"` in the search results (verified in `/tmp/teacher_candidates.json`, `/tmp/poster_candidates.json`, `/tmp/zoom_candidates.json`), which means each is a regular Unsplash Photos upload — attribution string can be pulled with a `GET https://api.unsplash.com/photos/<slug>` call using an Unsplash API key. The Unsplash License permits commercial use without attribution but credit is recommended.

### Zoom composite — 6 student tiles + 1 teacher
The teacher tile reuses `teacher-marco.jpg`. The 6 student webcam tiles are:

| Label in composite | Source URL |
|---|---|
| Sarah · Boston | https://images.unsplash.com/photo-1758522484827-7fc4957acfc3 |
| David · London | https://images.unsplash.com/photo-1758611971329-94fa9d6aa8a5 |
| Elena · Toronto | https://images.unsplash.com/photo-1758611974775-39e307bc3da9 |
| Michael · Sydney | https://images.unsplash.com/photo-1758612898691-afe3e1d08a0a |
| Anna · Berlin | https://images.unsplash.com/photo-1758598307034-e42c1fa33441 |
| Jonathan · NYC | https://images.unsplash.com/photo-1758598307007-99d0dca21288 |

All fetched from `images.unsplash.com`, `source="Unsplash"` in search results.

The composite was **not** built with Playwright (not installed in the sandbox). It was built with Pillow: 1920×1080 canvas, dark‑navy top bar with "Club Italia · CI Principiante · Lesson 4 · Roma" + "● LIVE" pill top-right, big Marco tile top-left with active‑speaker yellow border, 3×2 gallery of the 6 real student webcam photos on the right, per-tile dark rounded name pills with a mic glyph, and a bottom control bar with Mute / Stop Video / Participants / Chat / Share / red Leave phone icon. Build script: `/tmp/build_zoom_composite.py`.

---

## 2 · Music details
- **Piece:** Antonio Vivaldi — _The Four Seasons — Concerto No. 1 in E major RV 269 ("Spring"), Mvt 1 (Allegro)_ — the iconic opening
- **Performer:** John Harrison with the Wichita State University Chamber Players
- **Master source:** https://www.classicals.de/vivaldi-seasons (John Harrison recording, filename `01-John-Harrison-...`)
- **License stated in ID3 tag of the source file:** `Attribution-ShareAlike: http://creativecommons.org/licenses/by-sa/3.0/` (CC BY-SA 3.0)
- **Delivered file:** first 75 s of Mvt 1, re‑encoded to 128 kbps CBR, 44.1 kHz stereo, 1 s fade in / 2 s fade out. Filesize 1.14 MB. Verified with `ffprobe`.
- **ID3 tags embedded** in the delivered mp3:
  - `title = Spring Mvt 1 Allegro (CI hero excerpt)`
  - `artist = John Harrison with the Wichita State University Chamber Players`
  - `comment = Antonio Vivaldi — The Four Seasons, Spring RV 269 Mvt 1. Source: https://www.classicals.de/vivaldi-seasons. License: CC BY-SA 3.0. Excerpt for Club Italia hero.`

**Attribution to include on site (recommended footer/credits line):**

> Hero music: _Vivaldi – Spring (RV 269), Mvt 1_ performed by John Harrison with the Wichita State University Chamber Players, via classicals.de, licensed under CC BY-SA 3.0.

**Sources investigated / rejected:**
- Pixabay music (mandolin, guitar, tarantella listing pages) — Pixabay returns HTTP 403 to the sandbox crawler; couldn't extract direct MP3 URLs.
- Musopen — HTTP 403 to the sandbox crawler.
- Classicals.de "Spring RV 269" (non-Harrison) file was tagged `© 2024 Gregor Quendel. All rights reserved.` and CC BY-NC 4.0 — rejected as non-commercial. Switched to the John Harrison master (CC BY-SA).

Character check: warm baroque strings, no vocals, cinematic Italian instrumental — matches "Nino Rota / Ennio Morricone opening credits vibe" better than any of the generic royalty-free options that were reachable.

---

## 3 · Wiring confirmation (index.html · css/ci.css · js/ci.js)

**index.html** — first `<section class="hero">` at line 57, closing `</section>` at line 85. Added just before the closing tag (already present from a prior sibling; SVG path was patched to match the required snippet exactly with both speaker + waves):

```html
<audio id="hero-audio" loop preload="metadata">
  <source src="assets/audio/hero-italian-theme.mp3" type="audio/mpeg">
</audio>
<button id="hero-sound-toggle" class="hero-sound-btn" aria-label="Toggle Italian music" data-state="off">
  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
  <span class="hero-sound-label">Music on</span>
</button>
```

**css/ci.css** — appended a `HERO MUSIC TOGGLE` block containing:
- `.hero-sound-btn` — glass pill, absolute top-right of hero, gold accent border
- `.hero-sound-btn:hover` — solid dark, brighter gold border, lift on Y
- `.hero-sound-btn[data-state="on"]` — gold background, dark ink
- responsive `@media(max-width:860px)` — smaller pill, label hidden

(Byte-identical to the required snippet.)

**js/ci.js** — appended IIFE that:
- looks up `#hero-sound-toggle` and `#hero-audio`
- sets `audio.volume = 0.35`
- on click, toggles `play()`/`pause()`, mirrors state on the button's `data-state` attribute, flips the visible label between "Music on" / "Music off"

(Byte-identical to the required snippet.)

Verified with `grep`:
```
css/ci.css:1364-1367  ← .hero-sound-btn selectors present
js/ci.js:150          ← IIFE toggle present
index.html:78-84      ← audio + button present
```

---

## 4 · Files summary

- 7 × `teacher-*.jpg` — real Italian‑look Unsplash portraits, replaced
- 1 × `zoom-classroom-masterclass.jpg` — 1920×1080 Zoom‑style composite built from 7 real Unsplash photos
- 5 × `poster-*.jpg` — 3840×2560 Unsplash city photos
- 1 × `hero-italian-theme.mp3` — 75 s / 128 kbps Vivaldi Spring excerpt (CC BY-SA 3.0)
- 3 × in-repo edits: `index.html`, `css/ci.css`, `js/ci.js`

**Not committed** — parent agent handles git.

**Nothing blocked / no fallback to AI.** All human faces are real photographer-taken photos.
