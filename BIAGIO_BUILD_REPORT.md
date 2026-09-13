# Biagio AI Tutor Build Report

## 1. TTS model used

- **Model:** `gemini-2.5-pro-tts` (via `asi-text-to-speech` — the only supported TTS model after ElevenLabs discontinuation)
- **Voice:** `charon` (calm, professional, deep steady male tone)
- **Language:** Italian (native-Italian text supplied verbatim; Gemini TTS is multilingual and reads Italian natively without an explicit language flag)
- **Post-processing:** re-encoded each MP3 with `ffmpeg -b:a 128k -ac 1 -ar 44100` to hit the requested 128 kbps mono target
- **Fallback path attempted:** `fal_ai__pipedream` and `replicate__pipedream` connectors were surveyed first — neither exposed a submit tool (fal.ai connector only offers queue-status endpoints, not model submission). Went straight to the Gemini TTS path, which succeeded on the first pass for all six clips.

## 2. Audio files (mono, 128 kbps, 44.1 kHz)

| File | Path | Duration | Size |
|---|---|---|---|
| Intro (`biagio-intro.mp3`) | `assets/audio/biagio-intro.mp3` | 11.25 s | 181 KB |
| Al caffè (`biagio-line-caffe.mp3`) | `assets/audio/biagio-line-caffe.mp3` | 3.05 s | 49 KB |
| A tavola (`biagio-line-tavola.mp3`) | `assets/audio/biagio-line-tavola.mp3` | 2.89 s | 47 KB |
| Per strada (`biagio-line-strada.mp3`) | `assets/audio/biagio-line-strada.mp3` | 3.33 s | 54 KB |
| Piacere (`biagio-line-piacere.mp3`) | `assets/audio/biagio-line-piacere.mp3` | 2.65 s | 43 KB |
| Correzione (`biagio-line-corregge.mp3`) | `assets/audio/biagio-line-corregge.mp3` | 7.01 s | 113 KB |

All six verified with `ffprobe`, all served 200 from local static HTTP.

## 3. Portrait photos (real Unsplash images, not AI)

| Slot | Path | Source URL | Photographer / License |
|---|---|---|---|
| Hero (pose1) | `assets/img/biagio-pose1.jpg` (1600×2133) | https://images.unsplash.com/photo-1603570112520-fdc514048979 | Unsplash — [free-to-use Unsplash License](https://unsplash.com/license) |
| Mid-conversation (pose2) | `assets/img/biagio-pose2.jpg` (1600×2133) | https://images.unsplash.com/photo-1598627446792-5d89ab3e3540 | Unsplash — free-to-use Unsplash License |
| Thoughtful (pose3) | `assets/img/biagio-pose3.jpg` (1600×2400) | https://images.unsplash.com/photo-1615851947829-3641ababa187 | Unsplash — free-to-use Unsplash License |

All three depict a mid-40s Mediterranean man with dark hair and salt-and-pepper beard. Consistent enough to plausibly read as the same person "Biagio" across the page. Search was via `pplx_sdk.search.images` with the queries the brief supplied, downloaded via `pplx_sdk.content.fetch_image`.

## 4. biagio.html

- **Final line count:** 379 lines (30,515 bytes)
- **Structure ported from `/tmp/fa2/julien.html` section-for-section:**
  1. `.biagio-hero` — dark navy full-bleed 100 svh, cutout right, gold-italic accent, "Hear Biagio speak" (plays intro)
  2. "Who is Biagio" ivory fold (portrait + biography + facts list)
  3. 6 showcase cards in a navy-r fold (Al caffè · A tavola · Per strada · Piacere · Correzione · Chiacchierata libera) — each with Italian phrase in gold serif italic + English translation + Hear button wired to the matching MP3
  4. Live transcript dark-navy fold with user/Biagio bubbles including a real ho-andato → sono-andato correction with grammar explanation
  5. 6 feature cards (Conversation · Grammar · Pronunciation · Vocabulary · Culture · Homework)
  6. Availability/pricing strip (gold, 3 items)
  7. 6-question FAQ accordion (button-based)
  8. Sibling nav fold back to `courses.html` with second portrait
- **Zero em (—) or en (–) dashes** in body copy — verified programmatically (`grep -c` returns 0)
- All Italian phrases use « » guillemets like FA does

## 5. CSS

- **Appended to `css/ci.css`:** ~425 lines (file grew 1943 → 2368 lines)
- New classes: `.biagio-hero`, `.biagio-hero-grid`, `.biagio-hero-glow`, `.biagio-cutout-wrap`, `.biagio-cutout`, `.biagio-cutout-badge`, `.biagio-say`, `.biagio-say-it`, `.biagio-say-en`, `.biagio-say-btn` (pill with speaker SVG, `[aria-pressed="true"]` gold-fill state), `.biagio-head`, `.biagio-intro-grid`, `.biagio-facts`, `.biagio-showcase-grid`, `.biagio-showcase-card` (hover lift), `.biagio-transcript`, `.msg.user` / `.msg.biagio` (right-aligned ivory vs left-aligned navy with gold border-left), `.msg-correction`, `.biagio-features-grid`, `.biagio-feature-card`, `.biagio-avail-strip`, `.biagio-faq` (button accordion), `.biagio-sibling`, `.biagio-float` (fixed-bottom-right widget) + responsive breakpoints at 960 / 640 px

## 6. JS

- **Appended to `js/ci.js`:** ~55 lines (168 → 228 lines total)
- Three pieces of behaviour:
  1. `.biagio-say-btn` click handler — plays the `data-audio` URL, stops sibling clips, toggles `aria-pressed`, resets on `ended`
  2. `.biagio-faq .faq-q` accordion — toggles `.is-open` and `aria-expanded`
  3. `.biagio-float-play` — plays intro audio without triggering the parent `<a>` navigation (`preventDefault` + `stopPropagation`)

## 7. Homepage update (index.html)

- Added a full **Biagio hero-preview fold** before Pricing: navy-r background, portrait + Italian phrase + Hear button + "Meet Biagio" CTA linking to `/biagio.html`
- Added a **floating "Try Biagio" widget** fixed bottom-right (`.biagio-float`) — Biagio avatar + label + gold play button that fires `biagio-intro.mp3`, wraps a link to `biagio.html`

## 8. Failures / fallbacks

- **fal.ai / Replicate TTS:** the connected `fal_ai__pipedream` and `replicate__pipedream` connectors exposed *no* submit tool — only queue-status/response tools that require a pre-existing request id. Went to Gemini TTS (the built-in supported model) which succeeded on the first attempt for all six clips. No retry needed.
- **Visual QA in cloud browser:** cloud transport cannot reach `127.0.0.1:8117` in the sandbox. HTTP 200s and file-level structural checks were used in place of an in-browser screenshot. Main agent can preview via `deploy_website` if desired.

## 9. Verification summary

- 6/6 audio files: exist, valid MP3, correct duration (2.6-11.3 s), 43-181 KB, HTTP 200
- 3/3 portraits: real Unsplash JPEGs, 1600×2133+, HTTP 200
- 10 `.biagio-say-btn` occurrences in `biagio.html` — every one wired to a real audio file
- 6 `.biagio-showcase-card` blocks — one per showcase
- 2 `.msg.user` + 2 `.msg.biagio` bubbles in transcript
- 6 `.biagio-feature-card` blocks
- 6 `.faq-item` accordion rows
- 14 `«` guillemet openings — consistent Italian typography
- 0 em/en dashes anywhere in the file
