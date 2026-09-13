# Club Italia — Luxury Zoom Mockup (Julie-pattern) — Delivery Notes

Generated 2026-09-13 by the mockup subagent. Uses the eTeacher / Longevity Life Academy visual grammar established on Julie Gibson Clark's masterclass page: dark navy Zoom room, big host tile with light-blue accent border, row of student tiles, subtle dark chip control bar.

## Deliverable

- **File:** `/home/user/workspace/club-italia/assets/img/zoom-classroom-luxury.jpg`
- **Dimensions:** 2400 × 1350 px (16:9)
- **File size:** 308,852 bytes (≈ 301.6 KB) — well under the 500 KB target
- **Method:** Python + Pillow composite. No AI generation of the mockup itself; all portraits are real photographs from Unsplash.

## Student portraits (all real Unsplash photos, free-license)

| File | Caption used | Unsplash URL | License |
|---|---|---|---|
| `student-01-sarah.jpg` | "Sarah · Boston" | https://unsplash.com/photos/woman-smiling-in-a-modern-office-setting-lrBU-bSbAdw | Unsplash License (free, commercial use, no attribution required) |
| `student-02-david.jpg` | "David · London" | https://unsplash.com/photos/man-with-beard-and-glasses-sitting-at-desk-LxV5zDxV2B4 | Unsplash License |
| `student-03-elena.jpg` | "Elena · Toronto" | https://unsplash.com/s/photos/woman-headshot (asset ID `photo-1573497019940-1c28c88b4f3e`, Christina @ wocintechchat.com) | Unsplash License |
| `student-04-michael.jpg` | "Michael · Sydney" | https://unsplash.com/photos/man-with-glasses-in-a-modern-office-setting-grbDcbyo9nU | Unsplash License |
| `student-05-anna.jpg` | "Anna · Berlin" | https://unsplash.com/photos/a-smiling-woman-with-short-blonde-hair-using-her-phone-c9Gd7Pl4iCI | Unsplash License |
| `student-06-jonathan.jpg` | (reserved — not in this frame; Julie pattern uses 5 tiles) | https://unsplash.com/s/photos/professional-man (asset ID `photo-1560250097-0b93528c311a`) | Unsplash License |

All images downloaded via `pplx_sdk.content.fetch_image()` from `images.unsplash.com` at `w=1600&q=85&fit=crop`, saved as JPEG. Every photo is a real photograph of an adult (≈ 35–55 y.o.), not AI-generated. Photographer names are surfaced through the Unsplash page-URL slug; attribution is not legally required under the Unsplash License but the URLs above are the canonical source pages if the design team wants to credit inline.

## Reformulated queries

- The initial searches for `student-03-elena.jpg` returned (a) an Unsplash+ paywall shot with a big "Unsplash+" watermark and (b) a young woman clearly under 30. **Reformulated twice** before landing on Christina @ wocintechchat.com's clearly 40-something Latina professional (final download).
- The initial `student-05-anna.jpg` returned an elderly woman (≈ 65+). **Reformulated once** with "middle-aged blonde video call" and picked a 40-something blonde-highlighted professional in a home office.
- Two image-search queries returned 500s from the search service; the retries with adjusted wording succeeded.

## Teacher (Marco Rinaldi)

Uses the existing `teacher-marco.jpg` in the assets folder — real photographed Italian man (curly dark hair, salt-pepper beard, patterned zip cardigan, stone-wall background). Since the source is a portrait crop (1200×1600) and the host tile is wide (≈ 2352 × 1093), the tile uses **contain-mode fitting with intentional letterboxing**: Marco's face + shoulders are fully visible, centered over a soft dark-navy radial gradient, flanked by course-branding text ("LIVE from Rome · Faculty broadcast" on the left; "CI · PRINCIPIANTE · Lesson 4 — Il caffè · Cohort of 12 · CEFR A1" on the right). This reads as a deliberate eTeacher-brand "live faculty broadcast" panel rather than a bad crop.

## Layout (matches Julie pattern)

- **Canvas:** 2400×1350, `#05070d` background
- **Top bar (80 px, `#0d1119`):** "Club Italia · CI Principiante · Lesson 4 · Roma" (white, 24 px bold, with gold divider dot) + right side pulsing red REC dot + italic pale-green "REC" + timestamp "01:14:22"
- **Main area (padding 24 px):**
  - Host tile (full-width, ~2352×1093), 2 px `#5EB6FF` accent border, radius 14 px, subtle bottom-left name pill "Marco Rinaldi · Rome"
  - Row of **5 student tiles** at 16:9 (Sarah, David, Elena, Michael, Anna) — Julie's frame also shows 5 in the primary row; Jonathan sits out this frame
  - Each tile has a dark 86%-opacity name pill bottom-left: "Sarah · Boston", "David · London", "Elena · Toronto", "Michael · Sydney", "Anna · Berlin"
- **Bottom control bar (82 px, `#0d1119`):** centered chip strip — Mute ● / Video ■ / Share ▲ / Participants (12) ♦ / Reactions ♥ / Leave ● (burgundy-tinted)

## Notes for git

Not committed — per task instructions the main agent handles git.

## Files touched

- `/home/user/workspace/club-italia/assets/img/student-01-sarah.jpg` (new, 206 KB)
- `/home/user/workspace/club-italia/assets/img/student-02-david.jpg` (new, 177 KB)
- `/home/user/workspace/club-italia/assets/img/student-03-elena.jpg` (new, 711 KB)
- `/home/user/workspace/club-italia/assets/img/student-04-michael.jpg` (new, 137 KB)
- `/home/user/workspace/club-italia/assets/img/student-05-anna.jpg` (new, 331 KB)
- `/home/user/workspace/club-italia/assets/img/student-06-jonathan.jpg` (new, 350 KB)
- `/home/user/workspace/club-italia/assets/img/zoom-classroom-luxury.jpg` (new, 302 KB) — **the deliverable**
- `/home/user/workspace/club-italia/build_zoom_luxury.py` (new, build script)
