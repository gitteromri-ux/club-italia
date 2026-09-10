#!/usr/bin/env python3
"""Build all Club Italia SVG mockups."""
import os

OUT = "/home/user/workspace/club-italia/assets/img"

# Palette
BORDEAUX = "#3A0E12"
GOLD = "#C9A24B"
IVORY = "#F3EDDF"
TERRA = "#B65538"
NAVY = "#22080B"
DARK = "#1a0508"
GREEN_IT = "#008C45"
WHITE_IT = "#F4F5F0"
RED_IT = "#CD212A"
TRUSTGREEN = "#00B67A"

SERIF = "Cormorant Garamond, Georgia, serif"
SANS = "Inter, Arial, sans-serif"

# ------- Avatars -------
# Warm illustrated avatars: colored circle background, simple face
def avatar(cx, cy, r, skin="#E8B896", hair="#2C1810", initials="", name_label=None):
    # Circular face with hair silhouette
    parts = []
    # Background circle (soft warm)
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{skin}"/>')
    # Hair cap
    parts.append(f'<path d="M {cx-r*0.9} {cy-r*0.1} Q {cx-r} {cy-r*1.05} {cx} {cy-r*1.05} Q {cx+r} {cy-r*1.05} {cx+r*0.9} {cy-r*0.1} L {cx+r*0.85} {cy-r*0.35} Q {cx} {cy-r*0.75} {cx-r*0.85} {cy-r*0.35} Z" fill="{hair}"/>')
    # Eyes
    parts.append(f'<circle cx="{cx-r*0.28}" cy="{cy-r*0.05}" r="{r*0.06}" fill="#2C1810"/>')
    parts.append(f'<circle cx="{cx+r*0.28}" cy="{cy-r*0.05}" r="{r*0.06}" fill="#2C1810"/>')
    # Smile
    parts.append(f'<path d="M {cx-r*0.22} {cy+r*0.28} Q {cx} {cy+r*0.42} {cx+r*0.22} {cy+r*0.28}" stroke="#7a3020" stroke-width="{r*0.05}" fill="none" stroke-linecap="round"/>')
    return "".join(parts)


# Tile with avatar + name strip for Zoom gallery
def zoom_tile(x, y, w, h, name, city, skin, hair, is_teacher=False, speaking=False, hand=False, big=False):
    parts = []
    stroke = GOLD if is_teacher else "#3a1a1c"
    sw = 4 if is_teacher else 1.5
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#1a0508" stroke="{stroke}" stroke-width="{sw}"/>')
    # Face area
    face_r = min(w, h) * 0.22
    fcx = x + w/2
    fcy = y + h*0.42
    parts.append(avatar(fcx, fcy, face_r, skin=skin, hair=hair))
    # Bottom name strip
    parts.append(f'<rect x="{x}" y="{y+h-28}" width="{w}" height="28" fill="rgba(0,0,0,0.55)" rx="0"/>')
    fs = 13 if not big else 16
    parts.append(f'<text x="{x+10}" y="{y+h-10}" font-family="{SANS}" font-size="{fs}" fill="#F3EDDF" font-weight="600">{name}</text>')
    parts.append(f'<text x="{x+w-10}" y="{y+h-10}" font-family="{SANS}" font-size="{fs-2}" fill="#C9A24B" text-anchor="end">{city}</text>')
    # Mic icon
    parts.append(f'<circle cx="{x+w-16}" cy="{y+16}" r="10" fill="rgba(0,0,0,0.6)"/>')
    parts.append(f'<rect x="{x+w-19}" y="{y+11}" width="6" height="10" rx="3" fill="#F3EDDF"/>')
    if speaking:
        parts.append(f'<rect x="{x+8}" y="{y+8}" width="90" height="22" rx="4" fill="{GOLD}"/>')
        parts.append(f'<text x="{x+53}" y="{y+23}" font-family="{SANS}" font-size="12" font-weight="700" fill="{BORDEAUX}" text-anchor="middle">SPEAKING</text>')
    if hand:
        parts.append(f'<circle cx="{x+22}" cy="{y+22}" r="14" fill="{GOLD}"/>')
        parts.append(f'<text x="{x+22}" y="{y+27}" font-family="{SANS}" font-size="16" text-anchor="middle">✋</text>')
    return "".join(parts)


def browser_chrome(x, y, w, url):
    return f'''<g>
  <rect x="{x}" y="{y}" width="{w}" height="44" rx="10" fill="#EAE4D6"/>
  <rect x="{x}" y="{y+18}" width="{w}" height="26" fill="#EAE4D6"/>
  <circle cx="{x+18}" cy="{y+22}" r="6" fill="#FF5F57"/>
  <circle cx="{x+38}" cy="{y+22}" r="6" fill="#FEBC2E"/>
  <circle cx="{x+58}" cy="{y+22}" r="6" fill="#28C840"/>
  <rect x="{x+140}" y="{y+10}" width="{w-280}" height="24" rx="12" fill="#F7F2E6" stroke="#c9c0ac"/>
  <text x="{x+w/2}" y="{y+27}" font-family="{SANS}" font-size="13" fill="#3A0E12" text-anchor="middle">🔒 {url}</text>
</g>'''


# ============================================================
# 1. ZOOM MOCKUP
# ============================================================
def zoom_mockup():
    W, H = 1600, 900
    students = [
        ("Diane", "Boston", "#F0C9A8", "#8B4513"),
        ("Robert", "Chicago", "#D9A47A", "#3C2415"),
        ("Sarah", "San Diego", "#F5D5B8", "#C08040"),
        ("James", "NYC", "#B8845C", "#1a0f08"),
        ("Linda", "Seattle", "#EFC8A5", "#6B3410"),
        ("Michael", "Miami", "#C89670", "#2a1810"),
        ("Karen", "Phoenix", "#F0C8A0", "#5C2E0F"),
        ("Steven", "Denver", "#D8A075", "#302010"),
        ("Nancy", "Atlanta", "#B87850", "#1a0808"),
        ("Paul", "Portland", "#E8B896", "#4a2818"),
        ("Betty", "Nashville", "#F2CDA8", "#8B5A2B"),
    ]

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    svg.append(f'<rect width="{W}" height="{H}" fill="#0a0203"/>')
    # Browser chrome
    svg.append(browser_chrome(0, 0, W, "clubitalia.live/classroom/marco-A0"))
    # Classroom bg
    svg.append(f'<rect x="0" y="44" width="{W}" height="{H-44}" fill="{NAVY}"/>')

    # Top-right timer
    svg.append(f'<rect x="{W-220}" y="60" width="200" height="36" rx="18" fill="rgba(58,14,18,0.85)" stroke="{GOLD}"/>')
    svg.append(f'<circle cx="{W-200}" cy="78" r="6" fill="#e74c3c"><animate attributeName="opacity" values="1;0.3;1" dur="1.5s" repeatCount="indefinite"/></circle>')
    svg.append(f'<text x="{W-185}" y="83" font-family="{SANS}" font-size="14" font-weight="700" fill="{IVORY}">LIVE · 47:23 / 85:00</text>')

    # Participant chip top-left
    svg.append(f'<rect x="20" y="60" width="140" height="32" rx="16" fill="rgba(201,162,75,0.15)" stroke="{GOLD}"/>')
    svg.append(f'<text x="90" y="81" font-family="{SANS}" font-size="13" fill="{GOLD}" text-anchor="middle" font-weight="600">12 partecipanti</text>')

    # Gallery area: left region up to chat sidebar
    chat_w = 320
    gallery_x = 20
    gallery_y = 110
    gallery_w = W - chat_w - 60
    gallery_h = 620
    # 4 cols x 3 rows but teacher tile is 2x2 in top-left
    cols, rows = 4, 3
    gap = 12
    tile_w = (gallery_w - gap*(cols-1)) / cols
    tile_h = (gallery_h - gap*(rows-1)) / rows

    # Teacher tile 2x2
    tw2 = tile_w*2 + gap
    th2 = tile_h*2 + gap
    svg.append(zoom_tile(gallery_x, gallery_y, tw2, th2, "Marco Rinaldi", "Roma · Teacher", "#E8A87C", "#2a1005", is_teacher=True, speaking=True, big=True))

    # Remaining tiles positions (skip the 2x2 area cells)
    # Cells: (r,c). Occupied by teacher: (0,0),(0,1),(1,0),(1,1)
    remaining_cells = [(r, c) for r in range(rows) for c in range(cols) if not (r < 2 and c < 2)]
    # We have 8 remaining cells; we need 11 students. So we'll make the tile grid include an additional column on the right of the teacher? Instead, use 5 cols x 3 rows minus 2x2 teacher = 15-4 = 11. Redo.
    # Redo with cols=5
    svg = svg[:-1]  # remove teacher tile add? actually keep. Recompute grid
    # Simpler: recompute
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
    svg.append(f'<rect width="{W}" height="{H}" fill="#0a0203"/>')
    svg.append(browser_chrome(0, 0, W, "clubitalia.live/classroom/marco-A0"))
    svg.append(f'<rect x="0" y="44" width="{W}" height="{H-44}" fill="{NAVY}"/>')
    svg.append(f'<rect x="{W-220}" y="60" width="200" height="36" rx="18" fill="rgba(58,14,18,0.85)" stroke="{GOLD}"/>')
    svg.append(f'<circle cx="{W-200}" cy="78" r="6" fill="#e74c3c"/>')
    svg.append(f'<text x="{W-185}" y="83" font-family="{SANS}" font-size="14" font-weight="700" fill="{IVORY}">LIVE · 47:23 / 85:00</text>')
    svg.append(f'<rect x="20" y="60" width="140" height="32" rx="16" fill="rgba(201,162,75,0.15)" stroke="{GOLD}"/>')
    svg.append(f'<text x="90" y="81" font-family="{SANS}" font-size="13" fill="{GOLD}" text-anchor="middle" font-weight="600">12 partecipanti</text>')

    cols, rows = 5, 3
    gap = 10
    gallery_x = 20
    gallery_y = 110
    gallery_w = W - chat_w - 60
    gallery_h = 620
    tile_w = (gallery_w - gap*(cols-1)) / cols
    tile_h = (gallery_h - gap*(rows-1)) / rows
    tw2 = tile_w*2 + gap
    th2 = tile_h*2 + gap

    # Teacher tile
    svg.append(zoom_tile(gallery_x, gallery_y, tw2, th2, "Marco Rinaldi", "Roma · Teacher", "#E8A87C", "#2a1005", is_teacher=True, speaking=True, big=True))

    remaining_cells = [(r, c) for r in range(rows) for c in range(cols) if not (r < 2 and c < 2)]
    # Should be 15-4=11 cells for 11 students
    for i, (r, c) in enumerate(remaining_cells):
        if i >= len(students): break
        n, ci, skin, hair = students[i]
        tx = gallery_x + c*(tile_w+gap)
        ty = gallery_y + r*(tile_h+gap)
        hand = (n == "James")
        svg.append(zoom_tile(tx, ty, tile_w, tile_h, n, ci, skin, hair, hand=hand))

    # Chat sidebar
    cx = W - chat_w - 20
    cy = 110
    ch = gallery_h
    svg.append(f'<rect x="{cx}" y="{cy}" width="{chat_w}" height="{ch}" rx="12" fill="#150406" stroke="#3a1a1c"/>')
    svg.append(f'<rect x="{cx}" y="{cy}" width="{chat_w}" height="44" rx="12" fill="#22080B"/>')
    svg.append(f'<text x="{cx+16}" y="{cy+28}" font-family="{SANS}" font-size="14" fill="{GOLD}" font-weight="700">Chat · 3 messages</text>')

    msgs = [
        ("Diane · 8:47pm", "Grazie mille!"),
        ("James · 8:48pm", "Come si dice water?"),
        ("Marco · 8:48pm", "Un bicchiere d'acqua"),
    ]
    my = cy + 60
    for who, txt in msgs:
        svg.append(f'<text x="{cx+16}" y="{my}" font-family="{SANS}" font-size="11" fill="#8a7860">{who}</text>')
        svg.append(f'<rect x="{cx+16}" y="{my+8}" width="{chat_w-32}" height="42" rx="8" fill="rgba(201,162,75,0.08)"/>')
        svg.append(f'<text x="{cx+26}" y="{my+34}" font-family="{SANS}" font-size="13" fill="{IVORY}">{txt}</text>')
        my += 68

    # Captions bar bottom center
    cap_y = 750
    cap_w = 1000
    cap_x = (W - cap_w) / 2
    svg.append(f'<rect x="{cap_x}" y="{cap_y}" width="{cap_w}" height="60" rx="8" fill="rgba(0,0,0,0.85)" stroke="{GOLD}" stroke-width="1"/>')
    svg.append(f'<text x="{cap_x+cap_w/2}" y="{cap_y+25}" font-family="{SANS}" font-size="12" fill="{GOLD}" text-anchor="middle" font-weight="700">LIVE CAPTIONS · IT</text>')
    svg.append(f'<text x="{cap_x+cap_w/2}" y="{cap_y+48}" font-family="{SANS}" font-size="16" fill="{IVORY}" text-anchor="middle">MARCO: "Allora, ripetiamo insieme. Al bar io prendo... un caffè."</text>')

    # Bottom toolbar
    tb_y = 830
    tb_h = 60
    svg.append(f'<rect x="0" y="{tb_y}" width="{W}" height="{tb_h}" fill="#0a0203"/>')
    tools = [
        ("🎙", "Mute"), ("📹", "Video"), ("💬", "Chat"),
        ("👥", "Participants (12)"), ("✋", "Raise Hand"), ("📞", "Leave"),
    ]
    tb_start = 40
    tspacing = 200
    for i, (ic, lbl) in enumerate(tools):
        bx = tb_start + i*tspacing
        bcolor = "#B72020" if lbl == "Leave" else "rgba(255,255,255,0.08)"
        tcolor = IVORY if lbl != "Leave" else "#fff"
        svg.append(f'<rect x="{bx}" y="{tb_y+10}" width="180" height="40" rx="20" fill="{bcolor}"/>')
        svg.append(f'<text x="{bx+20}" y="{tb_y+35}" font-family="{SANS}" font-size="16" fill="{tcolor}">{ic}</text>')
        svg.append(f'<text x="{bx+50}" y="{tb_y+35}" font-family="{SANS}" font-size="13" fill="{tcolor}" font-weight="600">{lbl}</text>')

    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 2. ZOOM MOCKUP 2 - shared screen mode
# ============================================================
def zoom_mockup_2():
    W, H = 1600, 900
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
    svg.append(f'<rect width="{W}" height="{H}" fill="#0a0203"/>')
    svg.append(browser_chrome(0, 0, W, "clubitalia.live/classroom/chiara-B1"))
    svg.append(f'<rect x="0" y="44" width="{W}" height="{H-44}" fill="{NAVY}"/>')

    # Top bar
    svg.append(f'<rect x="{W-220}" y="60" width="200" height="36" rx="18" fill="rgba(58,14,18,0.85)" stroke="{GOLD}"/>')
    svg.append(f'<circle cx="{W-200}" cy="78" r="6" fill="#e74c3c"/>')
    svg.append(f'<text x="{W-185}" y="83" font-family="{SANS}" font-size="14" font-weight="700" fill="{IVORY}">LIVE · 32:11 / 85:00</text>')
    svg.append(f'<rect x="20" y="60" width="180" height="32" rx="16" fill="rgba(201,162,75,0.15)" stroke="{GOLD}"/>')
    svg.append(f'<text x="110" y="81" font-family="{SANS}" font-size="13" fill="{GOLD}" text-anchor="middle" font-weight="600">🖥 Chiara is presenting</text>')

    # Shared screen — Renaissance painting area
    ss_x, ss_y, ss_w, ss_h = 20, 110, 1240, 570
    svg.append(f'<rect x="{ss_x}" y="{ss_y}" width="{ss_w}" height="{ss_h}" rx="10" fill="#2a1810" stroke="{GOLD}" stroke-width="3"/>')
    # Simulated Renaissance painting: warm gradient + arch composition
    svg.append(f'''<defs>
      <linearGradient id="paintGrad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#c9a06a"/>
        <stop offset="0.5" stop-color="#8b5a3c"/>
        <stop offset="1" stop-color="#3a2010"/>
      </linearGradient>
    </defs>''')
    svg.append(f'<rect x="{ss_x+20}" y="{ss_y+20}" width="{ss_w-40}" height="{ss_h-40}" fill="url(#paintGrad)"/>')
    # Silhouettes: two figures
    svg.append(f'<ellipse cx="{ss_x+400}" cy="{ss_y+340}" rx="80" ry="130" fill="rgba(255,240,200,0.4)"/>')
    svg.append(f'<circle cx="{ss_x+400}" cy="{ss_y+200}" r="45" fill="rgba(255,240,200,0.5)"/>')
    svg.append(f'<ellipse cx="{ss_x+700}" cy="{ss_y+340}" rx="80" ry="130" fill="rgba(200,120,80,0.5)"/>')
    svg.append(f'<circle cx="{ss_x+700}" cy="{ss_y+200}" r="45" fill="rgba(255,220,180,0.5)"/>')
    # Halo
    svg.append(f'<circle cx="{ss_x+400}" cy="{ss_y+195}" r="55" fill="none" stroke="{GOLD}" stroke-width="2" opacity="0.7"/>')
    # Title overlay
    svg.append(f'<text x="{ss_x+40}" y="{ss_y+70}" font-family="{SERIF}" font-size="34" fill="{IVORY}" font-style="italic">L\'Annunciazione</text>')
    svg.append(f'<text x="{ss_x+40}" y="{ss_y+100}" font-family="{SANS}" font-size="16" fill="{GOLD}">Leonardo da Vinci · 1472 · Uffizi, Firenze</text>')

    # Italian labels with lines pointing to features
    labels = [
        (ss_x+520, ss_y+180, "l\'angelo"),
        (ss_x+820, ss_y+230, "Maria"),
        (ss_x+310, ss_y+400, "il giglio"),
        (ss_x+830, ss_y+430, "il libro"),
        (ss_x+520, ss_y+490, "il paesaggio toscano"),
    ]
    for lx, ly, txt in labels:
        svg.append(f'<rect x="{lx-8}" y="{ly-18}" width="{len(txt)*9+20}" height="26" rx="13" fill="rgba(58,14,18,0.9)" stroke="{GOLD}"/>')
        svg.append(f'<text x="{lx+2}" y="{ly}" font-family="{SANS}" font-size="14" fill="{IVORY}" font-style="italic">{txt}</text>')

    # Side panel: teacher tile
    tp_x = 1280
    tp_y = 110
    svg.append(zoom_tile(tp_x, tp_y, 300, 200, "Chiara Bellini", "Firenze · Teacher", "#F0C8A0", "#3a2010", is_teacher=True, speaking=True, big=True))

    # Chat below teacher
    ch_x = 1280
    ch_y = 330
    ch_w = 300
    ch_h = 350
    svg.append(f'<rect x="{ch_x}" y="{ch_y}" width="{ch_w}" height="{ch_h}" rx="12" fill="#150406" stroke="#3a1a1c"/>')
    svg.append(f'<rect x="{ch_x}" y="{ch_y}" width="{ch_w}" height="40" rx="12" fill="#22080B"/>')
    svg.append(f'<text x="{ch_x+14}" y="{ch_y+26}" font-family="{SANS}" font-size="13" fill="{GOLD}" font-weight="700">Chat</text>')
    msgs = [
        ("Emma · Denver", "Bellissima!"),
        ("Tom · Austin", "Cosa significa 'giglio'?"),
        ("Chiara · Teacher", "Lily flower — simbolo di purezza"),
        ("Anna · Portland", "Grazie, molto interessante"),
    ]
    my = ch_y + 56
    for who, txt in msgs:
        svg.append(f'<text x="{ch_x+14}" y="{my}" font-family="{SANS}" font-size="10" fill="#8a7860">{who}</text>')
        svg.append(f'<rect x="{ch_x+14}" y="{my+6}" width="{ch_w-28}" height="46" rx="6" fill="rgba(201,162,75,0.08)"/>')
        svg.append(f'<text x="{ch_x+22}" y="{my+32}" font-family="{SANS}" font-size="12" fill="{IVORY}">{txt}</text>')
        my += 70

    # Student tile strip at bottom
    strip_y = 700
    strip_h = 90
    strip_names = [
        ("Emma", "Denver", "#F0C9A8", "#7a4020"),
        ("Tom", "Austin", "#D9A47A", "#2a1005"),
        ("Anna", "Portland", "#F5D5B8", "#8B5A2B"),
        ("Kevin", "Boston", "#B8845C", "#1a0808"),
        ("Rachel", "SF", "#EFC8A5", "#6B3410"),
        ("David", "Miami", "#C89670", "#1a0808"),
        ("Julie", "Seattle", "#F0C8A0", "#5C2E0F"),
        ("Mark", "Dallas", "#D8A075", "#302010"),
    ]
    stx = 20
    stile_w = 190
    for i, (n, ci, sk, hr) in enumerate(strip_names):
        svg.append(zoom_tile(stx + i*(stile_w+8), strip_y, stile_w, strip_h, n, ci, sk, hr))

    # Captions bar
    cap_y = 800
    cap_w = 1000
    cap_x = (W - cap_w) / 2
    svg.append(f'<rect x="{cap_x}" y="{cap_y}" width="{cap_w}" height="24" rx="0" fill="rgba(0,0,0,0)"/>')
    # Bottom toolbar reduced
    tb_y = 828
    tb_h = 62
    svg.append(f'<rect x="0" y="{tb_y}" width="{W}" height="{tb_h}" fill="#0a0203"/>')
    svg.append(f'<rect x="{(W-1000)/2}" y="{tb_y+16}" width="1000" height="36" rx="8" fill="rgba(0,0,0,0.9)" stroke="{GOLD}"/>')
    svg.append(f'<text x="{W/2}" y="{tb_y+40}" font-family="{SANS}" font-size="15" fill="{IVORY}" text-anchor="middle">CHIARA: "Guardate il gesto dell\'angelo — è così delicato, così rinascimentale."</text>')

    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 3. DASHBOARD MOCKUP
# ============================================================
def dashboard_mockup():
    W, H = 1600, 1000
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    svg.append(f'<rect width="{W}" height="{H}" fill="{IVORY}"/>')
    # Sidebar
    sb_w = 260
    svg.append(f'<rect x="0" y="0" width="{sb_w}" height="{H}" fill="{BORDEAUX}"/>')
    # Logo
    svg.append(f'<text x="30" y="60" font-family="{SERIF}" font-size="26" fill="{GOLD}" font-style="italic">Club</text>')
    svg.append(f'<text x="30" y="90" font-family="{SERIF}" font-size="26" fill="{IVORY}" font-style="italic">Italia</text>')
    svg.append(f'<line x1="30" y1="110" x2="{sb_w-30}" y2="110" stroke="{GOLD}" stroke-width="1"/>')

    nav = [("📚", "My Courses", True), ("🔴", "Live Now", False), ("🎬", "Recordings", False),
           ("🤖", "Biagio", False), ("📈", "Progress", False), ("👥", "Community", False),
           ("🏆", "Certificates", False), ("⚙", "Settings", False)]
    ny = 160
    for ic, lbl, active in nav:
        if active:
            svg.append(f'<rect x="0" y="{ny-24}" width="{sb_w}" height="44" fill="rgba(201,162,75,0.2)"/>')
            svg.append(f'<rect x="0" y="{ny-24}" width="4" height="44" fill="{GOLD}"/>')
        color = GOLD if active else IVORY
        svg.append(f'<text x="30" y="{ny}" font-family="{SANS}" font-size="16" fill="{color}">{ic}</text>')
        svg.append(f'<text x="66" y="{ny}" font-family="{SANS}" font-size="15" fill="{color}" font-weight="{"600" if active else "400"}">{lbl}</text>')
        ny += 52

    # Bottom user card
    svg.append(f'<rect x="20" y="{H-100}" width="{sb_w-40}" height="80" rx="10" fill="rgba(0,0,0,0.25)"/>')
    svg.append(f'<circle cx="60" cy="{H-60}" r="22" fill="#F0C9A8"/>')
    svg.append(f'<text x="60" y="{H-55}" font-family="{SANS}" font-size="14" fill="{BORDEAUX}" text-anchor="middle" font-weight="700">DC</text>')
    svg.append(f'<text x="95" y="{H-65}" font-family="{SANS}" font-size="14" fill="{IVORY}" font-weight="600">Diane Costanza</text>')
    svg.append(f'<text x="95" y="{H-45}" font-family="{SANS}" font-size="11" fill="{GOLD}">CI Elementare · A1.1</text>')

    # Main content
    mx = sb_w + 40
    # Top bar
    svg.append(f'<text x="{mx}" y="60" font-family="{SERIF}" font-size="38" fill="{BORDEAUX}" font-style="italic">Welcome back, Diane</text>')
    svg.append(f'<text x="{mx}" y="90" font-family="{SANS}" font-size="15" fill="#5a3a3d">Thursday, September 10 · You\'re on a 6-week streak 🔥</text>')

    # Top-right search
    svg.append(f'<rect x="{W-340}" y="40" width="280" height="40" rx="20" fill="#fff" stroke="#d9c8a8"/>')
    svg.append(f'<text x="{W-320}" y="65" font-family="{SANS}" font-size="14" fill="#8a7860">🔍 Search lessons, teachers...</text>')

    # Big next-class card
    ncx, ncy, ncw, nch = mx, 130, W - mx - 60, 160
    svg.append(f'<rect x="{ncx}" y="{ncy}" width="{ncw}" height="{nch}" rx="14" fill="{BORDEAUX}"/>')
    svg.append(f'<text x="{ncx+30}" y="{ncy+40}" font-family="{SANS}" font-size="12" fill="{GOLD}" font-weight="700" letter-spacing="2">YOUR NEXT CLASS</text>')
    svg.append(f'<text x="{ncx+30}" y="{ncy+80}" font-family="{SERIF}" font-size="30" fill="{IVORY}" font-style="italic">Marco · CI Elementare · Lesson 07</text>')
    svg.append(f'<text x="{ncx+30}" y="{ncy+110}" font-family="{SANS}" font-size="15" fill="{IVORY}">Wednesday 7pm ET · in 3 days 4 hrs</text>')
    svg.append(f'<text x="{ncx+30}" y="{ncy+134}" font-family="{SANS}" font-size="13" fill="{GOLD}">Topic: "Al ristorante — ordering food"</text>')
    # CTA
    svg.append(f'<rect x="{ncx+ncw-220}" y="{ncy+50}" width="180" height="50" rx="25" fill="{GOLD}"/>')
    svg.append(f'<text x="{ncx+ncw-130}" y="{ncy+82}" font-family="{SANS}" font-size="15" font-weight="700" fill="{BORDEAUX}" text-anchor="middle">Join Live Class</text>')
    svg.append(f'<text x="{ncx+ncw-130}" y="{ncy+120}" font-family="{SANS}" font-size="11" fill="{IVORY}" text-anchor="middle">Reminder set · Add to calendar</text>')

    # Progress bar section
    py = 320
    svg.append(f'<text x="{mx}" y="{py}" font-family="{SANS}" font-size="12" fill="{BORDEAUX}" font-weight="700" letter-spacing="2">YOUR PROGRESS</text>')
    svg.append(f'<text x="{mx}" y="{py+30}" font-family="{SERIF}" font-size="22" fill="{BORDEAUX}" font-style="italic">CI Elementare · 6 of 20 lessons complete</text>')
    svg.append(f'<text x="{mx}" y="{py+52}" font-family="{SANS}" font-size="13" fill="#7a5a5d">CEFR A1.1 → A1.2 (30% complete)</text>')
    # Bar
    bw = ncw
    svg.append(f'<rect x="{mx}" y="{py+70}" width="{bw}" height="14" rx="7" fill="#e5d8c0"/>')
    svg.append(f'<rect x="{mx}" y="{py+70}" width="{bw*0.3}" height="14" rx="7" fill="{GOLD}"/>')
    # Ticks
    for i in range(1, 20):
        tx = mx + (bw*i/20)
        svg.append(f'<line x1="{tx}" y1="{py+70}" x2="{tx}" y2="{py+84}" stroke="{IVORY}" stroke-width="1"/>')

    # Recent activity
    ay = 440
    svg.append(f'<text x="{mx}" y="{ay}" font-family="{SANS}" font-size="12" fill="{BORDEAUX}" font-weight="700" letter-spacing="2">RECENT ACTIVITY</text>')
    acts = [
        ("✓", "Completed Lesson 06 — Al Bar", "Yesterday · 85 min · with Marco"),
        ("💬", "Chatted with Biagio", "2 days ago · 24 messages · practicing greetings"),
        ("🎬", "Watched recording — Lesson 05", "4 days ago · 42 min"),
    ]
    for i, (ic, ttl, sub) in enumerate(acts):
        iy = ay + 30 + i*70
        svg.append(f'<rect x="{mx}" y="{iy}" width="{bw}" height="60" rx="10" fill="#fff" stroke="#e5d8c0"/>')
        svg.append(f'<circle cx="{mx+30}" cy="{iy+30}" r="18" fill="{IVORY}"/>')
        svg.append(f'<text x="{mx+30}" y="{iy+36}" font-family="{SANS}" font-size="16" text-anchor="middle">{ic}</text>')
        svg.append(f'<text x="{mx+60}" y="{iy+27}" font-family="{SANS}" font-size="14" fill="{BORDEAUX}" font-weight="600">{ttl}</text>')
        svg.append(f'<text x="{mx+60}" y="{iy+48}" font-family="{SANS}" font-size="12" fill="#7a5a5d">{sub}</text>')

    # Recommended + study group columns
    ry = 690
    col_w = (bw - 20) / 2
    # Recommended
    svg.append(f'<text x="{mx}" y="{ry}" font-family="{SANS}" font-size="12" fill="{BORDEAUX}" font-weight="700" letter-spacing="2">RECOMMENDED</text>')
    recs = [
        ("Culture: Italian Cinema", "Fri 6pm ET · Free preview"),
        ("Pronunciation Lab", "Sat 11am ET · with Sofia"),
    ]
    for i, (t, s) in enumerate(recs):
        cx_ = mx + i*((col_w/2)+10)
        cw_ = (col_w-10)/2
        svg.append(f'<rect x="{cx_}" y="{ry+20}" width="{cw_}" height="140" rx="12" fill="{TERRA}"/>')
        svg.append(f'<rect x="{cx_}" y="{ry+20}" width="{cw_}" height="80" rx="12" fill="#8B3820"/>')
        svg.append(f'<text x="{cx_+20}" y="{ry+112}" font-family="{SERIF}" font-size="18" fill="{IVORY}" font-style="italic">{t}</text>')
        svg.append(f'<text x="{cx_+20}" y="{ry+135}" font-family="{SANS}" font-size="12" fill="{GOLD}">{s}</text>')

    # Study group
    sgx = mx + col_w + 20
    svg.append(f'<text x="{sgx}" y="{ry}" font-family="{SANS}" font-size="12" fill="{BORDEAUX}" font-weight="700" letter-spacing="2">STUDY GROUP</text>')
    svg.append(f'<rect x="{sgx}" y="{ry+20}" width="{col_w}" height="140" rx="12" fill="{BORDEAUX}"/>')
    svg.append(f'<text x="{sgx+20}" y="{ry+55}" font-family="{SERIF}" font-size="22" fill="{IVORY}" font-style="italic">Conversation Practice</text>')
    svg.append(f'<text x="{sgx+20}" y="{ry+80}" font-family="{SANS}" font-size="14" fill="{GOLD}">Wed 8pm ET · 4 seats left</text>')
    svg.append(f'<text x="{sgx+20}" y="{ry+103}" font-family="{SANS}" font-size="12" fill="{IVORY}">Small group · A1 level · 45 min</text>')
    # Avatars
    for i, sk in enumerate(["#F0C9A8", "#D9A47A", "#B8845C", "#E8B896"]):
        svg.append(f'<circle cx="{sgx+30+i*24}" cy="{ry+130}" r="12" fill="{sk}" stroke="{BORDEAUX}" stroke-width="2"/>')
    svg.append(f'<rect x="{sgx+col_w-140}" y="{ry+110}" width="120" height="36" rx="18" fill="{GOLD}"/>')
    svg.append(f'<text x="{sgx+col_w-80}" y="{ry+133}" font-family="{SANS}" font-size="13" font-weight="700" fill="{BORDEAUX}" text-anchor="middle">Reserve seat</text>')

    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 4. CERTIFICATE MOCKUP
# ============================================================
def certificate_mockup():
    W, H = 1400, 1000
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    # Paper
    svg.append(f'<rect width="{W}" height="{H}" fill="{IVORY}"/>')
    # Subtle noise via pattern
    svg.append(f'<rect width="{W}" height="{H}" fill="url(#paper)" opacity="0.4"/>')
    svg.append(f'''<defs>
      <pattern id="paper" width="4" height="4" patternUnits="userSpaceOnUse">
        <rect width="4" height="4" fill="{IVORY}"/>
        <circle cx="1" cy="2" r="0.4" fill="#d9c8a8" opacity="0.5"/>
      </pattern>
    </defs>''')

    # Outer border
    svg.append(f'<rect x="40" y="40" width="{W-80}" height="{H-80}" fill="none" stroke="{GOLD}" stroke-width="3"/>')
    svg.append(f'<rect x="52" y="52" width="{W-104}" height="{H-104}" fill="none" stroke="{GOLD}" stroke-width="1"/>')

    # Ornamental corners
    for cx, cy in [(70, 70), (W-70, 70), (70, H-70), (W-70, H-70)]:
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="16" fill="none" stroke="{GOLD}" stroke-width="1.5"/>')
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="{GOLD}"/>')

    # Ornamental flourishes top and bottom
    for y in [110, H-110]:
        svg.append(f'<line x1="200" y1="{y}" x2="{W-200}" y2="{y}" stroke="{GOLD}" stroke-width="0.6"/>')
        svg.append(f'<circle cx="{W/2}" cy="{y}" r="4" fill="{GOLD}"/>')
        svg.append(f'<circle cx="{W/2-20}" cy="{y}" r="2" fill="{GOLD}"/>')
        svg.append(f'<circle cx="{W/2+20}" cy="{y}" r="2" fill="{GOLD}"/>')

    # Brand
    svg.append(f'<text x="{W/2}" y="180" font-family="{SANS}" font-size="14" fill="{BORDEAUX}" text-anchor="middle" letter-spacing="6" font-weight="700">CLUB ITALIA BY ETEACHER</text>')

    # Title
    svg.append(f'<text x="{W/2}" y="270" font-family="{SERIF}" font-size="64" fill="{BORDEAUX}" text-anchor="middle" font-style="italic">Certificate of Completion</text>')

    # Divider tricolor
    svg.append(f'<rect x="{W/2-60}" y="300" width="40" height="4" fill="{GREEN_IT}"/>')
    svg.append(f'<rect x="{W/2-20}" y="300" width="40" height="4" fill="{WHITE_IT}" stroke="#d9c8a8" stroke-width="0.5"/>')
    svg.append(f'<rect x="{W/2+20}" y="300" width="40" height="4" fill="{RED_IT}"/>')

    # Awarded to
    svg.append(f'<text x="{W/2}" y="370" font-family="{SANS}" font-size="16" fill="#7a5a5d" text-anchor="middle" letter-spacing="4">AWARDED TO</text>')
    svg.append(f'<text x="{W/2}" y="450" font-family="{SERIF}" font-size="72" fill="{BORDEAUX}" text-anchor="middle" font-style="italic">Diane Costanza</text>')
    # Underline
    svg.append(f'<line x1="{W/2-260}" y1="475" x2="{W/2+260}" y2="475" stroke="{GOLD}" stroke-width="1"/>')

    # For successful completion
    svg.append(f'<text x="{W/2}" y="525" font-family="{SANS}" font-size="16" fill="#5a3a3d" text-anchor="middle">For successful completion of</text>')
    svg.append(f'<text x="{W/2}" y="580" font-family="{SERIF}" font-size="40" fill="{BORDEAUX}" text-anchor="middle" font-style="italic">CI Elementare</text>')
    svg.append(f'<text x="{W/2}" y="615" font-family="{SANS}" font-size="15" fill="{TERRA}" text-anchor="middle" letter-spacing="3">CEFR A1.1 → A1.2</text>')

    # Details
    svg.append(f'<text x="{W/2}" y="665" font-family="{SANS}" font-size="13" fill="#7a5a5d" text-anchor="middle">85 hours of live instruction · 20 lessons · 6 cultural modules</text>')

    # Signature area (left) + Date (right) + Seal (center-bottom)
    # Signature
    svg.append(f'<line x1="180" y1="810" x2="480" y2="810" stroke="{BORDEAUX}" stroke-width="1"/>')
    svg.append(f'<text x="330" y="805" font-family="{SERIF}" font-size="26" fill="{BORDEAUX}" text-anchor="middle" font-style="italic">Alessandro Ferri</text>')
    svg.append(f'<text x="330" y="835" font-family="{SANS}" font-size="12" fill="#5a3a3d" text-anchor="middle" letter-spacing="2">HEAD OF FACULTY</text>')

    # Date
    svg.append(f'<line x1="{W-480}" y1="810" x2="{W-180}" y2="810" stroke="{BORDEAUX}" stroke-width="1"/>')
    svg.append(f'<text x="{W-330}" y="805" font-family="{SERIF}" font-size="24" fill="{BORDEAUX}" text-anchor="middle" font-style="italic">15 December 2026</text>')
    svg.append(f'<text x="{W-330}" y="835" font-family="{SANS}" font-size="12" fill="#5a3a3d" text-anchor="middle" letter-spacing="2">DATE ISSUED</text>')

    # eTeacher seal (center)
    scx, scy = W/2, 810
    svg.append(f'<circle cx="{scx}" cy="{scy}" r="60" fill="none" stroke="{GOLD}" stroke-width="2"/>')
    svg.append(f'<circle cx="{scx}" cy="{scy}" r="52" fill="none" stroke="{GOLD}" stroke-width="0.5"/>')
    # Curved text (approximate)
    svg.append(f'<defs><path id="sealTop" d="M {scx-46} {scy} A 46 46 0 0 1 {scx+46} {scy}"/></defs>')
    svg.append(f'<text font-family="{SANS}" font-size="9" fill="{BORDEAUX}" letter-spacing="3"><textPath href="#sealTop" startOffset="50%" text-anchor="middle">ETEACHER GROUP · EST. 2000</textPath></text>')
    svg.append(f'<text x="{scx}" y="{scy}" font-family="{SERIF}" font-size="22" fill="{BORDEAUX}" text-anchor="middle" font-style="italic">eT</text>')
    svg.append(f'<text x="{scx}" y="{scy+18}" font-family="{SANS}" font-size="8" fill="{GOLD}" text-anchor="middle" letter-spacing="2">VERIFIED</text>')

    # CEFR stamp (top-right small)
    tx, ty = W-260, 200
    svg.append(f'<rect x="{tx}" y="{ty}" width="200" height="70" rx="6" fill="none" stroke="{TERRA}" stroke-width="1.5" transform="rotate(-4 {tx+100} {ty+35})"/>')
    svg.append(f'<text x="{tx+100}" y="{ty+30}" font-family="{SANS}" font-size="10" fill="{TERRA}" text-anchor="middle" letter-spacing="3" transform="rotate(-4 {tx+100} {ty+35})">CEFR ALIGNED</text>')
    svg.append(f'<text x="{tx+100}" y="{ty+50}" font-family="{SERIF}" font-size="20" fill="{TERRA}" text-anchor="middle" font-style="italic" transform="rotate(-4 {tx+100} {ty+35})">Council of Europe</text>')

    # Cert ID footer
    svg.append(f'<text x="{W/2}" y="{H-70}" font-family="{SANS}" font-size="10" fill="#9a8a80" text-anchor="middle" letter-spacing="2">CERTIFICATE ID · CI-ELE-2026-4720 · verify at clubitalia.live/verify</text>')

    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 5. CHECKOUT MOCKUP
# ============================================================
def checkout_mockup():
    W, H = 1600, 1000
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    svg.append(f'<rect width="{W}" height="{H}" fill="{IVORY}"/>')
    # Top nav
    svg.append(f'<rect x="0" y="0" width="{W}" height="70" fill="{BORDEAUX}"/>')
    svg.append(f'<text x="40" y="45" font-family="{SERIF}" font-size="26" fill="{GOLD}" font-style="italic">Club Italia</text>')
    svg.append(f'<text x="{W-40}" y="43" font-family="{SANS}" font-size="13" fill="{IVORY}" text-anchor="end">🔒 Secure checkout</text>')

    # Page title
    svg.append(f'<text x="{W/2}" y="130" font-family="{SERIF}" font-size="42" fill="{BORDEAUX}" text-anchor="middle" font-style="italic">Complete your enrollment</text>')
    svg.append(f'<text x="{W/2}" y="160" font-family="{SANS}" font-size="14" fill="#7a5a5d" text-anchor="middle">Step 2 of 2 · Payment</text>')

    # Two column layout
    left_x = 100
    right_x = 840
    col_w = 660
    top_y = 210

    # LEFT — Order summary
    svg.append(f'<rect x="{left_x}" y="{top_y}" width="{col_w}" height="640" rx="14" fill="#fff" stroke="#e5d8c0"/>')
    svg.append(f'<text x="{left_x+30}" y="{top_y+40}" font-family="{SANS}" font-size="12" fill="{BORDEAUX}" font-weight="700" letter-spacing="3">ORDER SUMMARY</text>')

    # Course line
    svg.append(f'<rect x="{left_x+30}" y="{top_y+70}" width="90" height="90" rx="8" fill="{TERRA}"/>')
    svg.append(f'<text x="{left_x+75}" y="{top_y+120}" font-family="{SERIF}" font-size="30" fill="{IVORY}" text-anchor="middle" font-style="italic">CI</text>')
    svg.append(f'<text x="{left_x+140}" y="{top_y+100}" font-family="{SERIF}" font-size="26" fill="{BORDEAUX}" font-style="italic">CI Principiante</text>')
    svg.append(f'<text x="{left_x+140}" y="{top_y+125}" font-family="{SANS}" font-size="14" fill="#5a3a3d">Annual Plan · A0 → A1</text>')
    svg.append(f'<text x="{left_x+140}" y="{top_y+148}" font-family="{SANS}" font-size="13" fill="#7a5a5d">80 live lessons · Biagio AI · Community · Certificate</text>')
    svg.append(f'<text x="{left_x+col_w-30}" y="{top_y+125}" font-family="{SERIF}" font-size="30" fill="{BORDEAUX}" text-anchor="end" font-style="italic">$1,240</text>')

    # Divider
    svg.append(f'<line x1="{left_x+30}" y1="{top_y+200}" x2="{left_x+col_w-30}" y2="{top_y+200}" stroke="#e5d8c0"/>')

    # Line items
    items = [
        ("Annual subscription (12 months)", "$1,240.00"),
        ("Early enrollment discount", "-$120.00"),
        ("Placement call", "included"),
        ("Certificate of completion", "included"),
    ]
    iy = top_y + 240
    for lbl, amt in items:
        svg.append(f'<text x="{left_x+30}" y="{iy}" font-family="{SANS}" font-size="14" fill="#5a3a3d">{lbl}</text>')
        color = TERRA if amt.startswith("-") else "#5a3a3d"
        svg.append(f'<text x="{left_x+col_w-30}" y="{iy}" font-family="{SANS}" font-size="14" fill="{color}" text-anchor="end">{amt}</text>')
        iy += 36

    svg.append(f'<line x1="{left_x+30}" y1="{iy+10}" x2="{left_x+col_w-30}" y2="{iy+10}" stroke="#c9c0ac"/>')
    iy += 50
    svg.append(f'<text x="{left_x+30}" y="{iy}" font-family="{SANS}" font-size="18" fill="{BORDEAUX}" font-weight="700">Total (USD)</text>')
    svg.append(f'<text x="{left_x+col_w-30}" y="{iy}" font-family="{SERIF}" font-size="38" fill="{BORDEAUX}" text-anchor="end" font-style="italic">$1,120</text>')
    svg.append(f'<text x="{left_x+col_w-30}" y="{iy+22}" font-family="{SANS}" font-size="12" fill="#7a5a5d" text-anchor="end">or $103/mo × 12 with 0% APR</text>')

    # Trust badges block bottom of left
    tby = top_y + 540
    svg.append(f'<rect x="{left_x+30}" y="{tby}" width="{col_w-60}" height="80" rx="8" fill="{IVORY}"/>')
    trust = [
        ("🔒", "SSL · 256-bit"),
        ("💳", "Stripe secure"),
        ("↩", "7-day refund"),
    ]
    for i, (ic, lbl) in enumerate(trust):
        tx = left_x + 60 + i * ((col_w-120)/3)
        svg.append(f'<text x="{tx}" y="{tby+35}" font-family="{SANS}" font-size="24" fill="{GOLD}">{ic}</text>')
        svg.append(f'<text x="{tx+40}" y="{tby+30}" font-family="{SANS}" font-size="12" fill="{BORDEAUX}" font-weight="700">{lbl}</text>')
        svg.append(f'<text x="{tx+40}" y="{tby+50}" font-family="{SANS}" font-size="10" fill="#7a5a5d">Guaranteed</text>')

    # RIGHT — Payment form
    svg.append(f'<rect x="{right_x}" y="{top_y}" width="{col_w}" height="640" rx="14" fill="#fff" stroke="#e5d8c0"/>')
    svg.append(f'<text x="{right_x+30}" y="{top_y+40}" font-family="{SANS}" font-size="12" fill="{BORDEAUX}" font-weight="700" letter-spacing="3">PAYMENT DETAILS</text>')

    # Payment method tabs
    py = top_y + 70
    tabs = [("Card", True), ("Apple Pay", False), ("Google Pay", False), ("PayPal", False)]
    tx = right_x + 30
    for lbl, active in tabs:
        tw = 130
        fill = BORDEAUX if active else "#fff"
        color = IVORY if active else "#5a3a3d"
        svg.append(f'<rect x="{tx}" y="{py}" width="{tw}" height="40" rx="8" fill="{fill}" stroke="#c9c0ac"/>')
        svg.append(f'<text x="{tx+tw/2}" y="{py+26}" font-family="{SANS}" font-size="13" fill="{color}" text-anchor="middle" font-weight="600">{lbl}</text>')
        tx += tw + 10

    # Card holder name
    fy = py + 70
    svg.append(f'<text x="{right_x+30}" y="{fy}" font-family="{SANS}" font-size="12" fill="#5a3a3d" font-weight="600">CARDHOLDER NAME</text>')
    svg.append(f'<rect x="{right_x+30}" y="{fy+10}" width="{col_w-60}" height="46" rx="8" fill="{IVORY}" stroke="#c9c0ac"/>')
    svg.append(f'<text x="{right_x+45}" y="{fy+40}" font-family="{SANS}" font-size="15" fill="{BORDEAUX}">Diane Costanza</text>')

    # Card number
    fy += 90
    svg.append(f'<text x="{right_x+30}" y="{fy}" font-family="{SANS}" font-size="12" fill="#5a3a3d" font-weight="600">CARD NUMBER</text>')
    svg.append(f'<rect x="{right_x+30}" y="{fy+10}" width="{col_w-60}" height="46" rx="8" fill="{IVORY}" stroke="#c9c0ac"/>')
    svg.append(f'<text x="{right_x+45}" y="{fy+40}" font-family="{SANS}" font-size="15" fill="{BORDEAUX}" letter-spacing="3">4242  4242  4242  4242</text>')
    # Card icons
    svg.append(f'<rect x="{right_x+col_w-140}" y="{fy+20}" width="30" height="20" rx="3" fill="#1a1f71"/>')
    svg.append(f'<text x="{right_x+col_w-125}" y="{fy+35}" font-family="{SANS}" font-size="9" fill="#fff" text-anchor="middle" font-weight="700">VISA</text>')
    svg.append(f'<circle cx="{right_x+col_w-90}" cy="{fy+30}" r="10" fill="#EB001B"/>')
    svg.append(f'<circle cx="{right_x+col_w-78}" cy="{fy+30}" r="10" fill="#F79E1B" opacity="0.85"/>')
    svg.append(f'<rect x="{right_x+col_w-60}" y="{fy+20}" width="30" height="20" rx="3" fill="#006FCF"/>')
    svg.append(f'<text x="{right_x+col_w-45}" y="{fy+35}" font-family="{SANS}" font-size="9" fill="#fff" text-anchor="middle" font-weight="700">AMEX</text>')

    # Expiry + CVV
    fy += 90
    svg.append(f'<text x="{right_x+30}" y="{fy}" font-family="{SANS}" font-size="12" fill="#5a3a3d" font-weight="600">EXPIRY</text>')
    svg.append(f'<rect x="{right_x+30}" y="{fy+10}" width="{(col_w-80)/2}" height="46" rx="8" fill="{IVORY}" stroke="#c9c0ac"/>')
    svg.append(f'<text x="{right_x+45}" y="{fy+40}" font-family="{SANS}" font-size="15" fill="{BORDEAUX}">MM / YY</text>')

    cvx = right_x + 30 + (col_w-80)/2 + 20
    svg.append(f'<text x="{cvx}" y="{fy}" font-family="{SANS}" font-size="12" fill="#5a3a3d" font-weight="600">CVV</text>')
    svg.append(f'<rect x="{cvx}" y="{fy+10}" width="{(col_w-80)/2}" height="46" rx="8" fill="{IVORY}" stroke="#c9c0ac"/>')
    svg.append(f'<text x="{cvx+15}" y="{fy+40}" font-family="{SANS}" font-size="15" fill="{BORDEAUX}">•••</text>')

    # ZIP
    fy += 90
    svg.append(f'<text x="{right_x+30}" y="{fy}" font-family="{SANS}" font-size="12" fill="#5a3a3d" font-weight="600">BILLING ZIP</text>')
    svg.append(f'<rect x="{right_x+30}" y="{fy+10}" width="{col_w-60}" height="46" rx="8" fill="{IVORY}" stroke="#c9c0ac"/>')
    svg.append(f'<text x="{right_x+45}" y="{fy+40}" font-family="{SANS}" font-size="15" fill="{BORDEAUX}">02116</text>')

    # CTA
    cta_y = top_y + 560
    svg.append(f'<rect x="{right_x+30}" y="{cta_y}" width="{col_w-60}" height="60" rx="30" fill="{GOLD}"/>')
    svg.append(f'<text x="{right_x+col_w/2}" y="{cta_y+38}" font-family="{SANS}" font-size="17" font-weight="700" fill="{BORDEAUX}" text-anchor="middle">Complete purchase · $1,120</text>')

    svg.append(f'<text x="{right_x+col_w/2}" y="{cta_y+90}" font-family="{SANS}" font-size="11" fill="#7a5a5d" text-anchor="middle">By purchasing, you agree to our Terms of Service and Privacy Policy.</text>')

    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 6. SCREEN — PLACEMENT
# ============================================================
def screen_placement():
    W, H = 800, 600
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    svg.append(f'<rect width="{W}" height="{H}" fill="{IVORY}"/>')
    # Header
    svg.append(f'<rect x="0" y="0" width="{W}" height="60" fill="{BORDEAUX}"/>')
    svg.append(f'<text x="30" y="38" font-family="{SERIF}" font-size="20" fill="{GOLD}" font-style="italic">Club Italia · Book your placement call</text>')

    # Left: mini calendar
    svg.append(f'<text x="30" y="100" font-family="{SANS}" font-size="12" fill="{BORDEAUX}" font-weight="700" letter-spacing="2">THIS WEEK · SEP 14–20</text>')

    # 6 slot cards
    slots = [
        ("Mon 15", "9:00am ET", "Alessandro"),
        ("Mon 15", "2:00pm ET", "Sofia"),
        ("Tue 16", "10:00am ET", "Chiara"),
        ("Wed 17", "1:00pm ET", "Marco"),
        ("Thu 18", "4:00pm ET", "Luca"),
        ("Fri 19", "11:00am ET", "Francesca"),
    ]
    cx = 30
    cy = 130
    cw = 240
    ch = 130
    gap = 15
    for i, (day, time, teacher) in enumerate(slots):
        row = i // 3
        col = i % 3
        x = cx + col*(cw+gap)
        y = cy + row*(ch+gap)
        svg.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="12" fill="#fff" stroke="#e5d8c0"/>')
        svg.append(f'<text x="{x+20}" y="{y+30}" font-family="{SANS}" font-size="11" fill="{TERRA}" font-weight="700" letter-spacing="2">{day.upper()}</text>')
        svg.append(f'<text x="{x+20}" y="{y+62}" font-family="{SERIF}" font-size="24" fill="{BORDEAUX}" font-style="italic">{time}</text>')
        svg.append(f'<text x="{x+20}" y="{y+85}" font-family="{SANS}" font-size="12" fill="#7a5a5d">with {teacher}</text>')
        svg.append(f'<rect x="{x+20}" y="{y+ch-40}" width="{cw-40}" height="30" rx="15" fill="{GOLD}"/>')
        svg.append(f'<text x="{x+cw/2}" y="{y+ch-20}" font-family="{SANS}" font-size="12" font-weight="700" fill="{BORDEAUX}" text-anchor="middle">Reserve · 25 min</text>')

    # Footer note
    svg.append(f'<text x="{W/2}" y="{H-40}" font-family="{SANS}" font-size="12" fill="#5a3a3d" text-anchor="middle">Free · Video call · No commitment · Discover your level</text>')

    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 7. SCREEN — PLATFORM
# ============================================================
def screen_platform():
    W, H = 800, 600
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    svg.append(f'<rect width="{W}" height="{H}" fill="{IVORY}"/>')
    # Sidebar
    svg.append(f'<rect x="0" y="0" width="140" height="{H}" fill="{BORDEAUX}"/>')
    svg.append(f'<text x="20" y="40" font-family="{SERIF}" font-size="18" fill="{GOLD}" font-style="italic">Club Italia</text>')
    nav = ["Home", "Live", "Biagio", "Progress", "Community"]
    for i, n in enumerate(nav):
        y = 90 + i*40
        active = (n == "Home")
        color = GOLD if active else IVORY
        if active:
            svg.append(f'<rect x="0" y="{y-20}" width="140" height="34" fill="rgba(201,162,75,0.15)"/>')
            svg.append(f'<rect x="0" y="{y-20}" width="3" height="34" fill="{GOLD}"/>')
        svg.append(f'<text x="20" y="{y}" font-family="{SANS}" font-size="13" fill="{color}">{n}</text>')

    # Main
    mx = 170
    svg.append(f'<text x="{mx}" y="45" font-family="{SERIF}" font-size="24" fill="{BORDEAUX}" font-style="italic">Buongiorno, Diane</text>')
    svg.append(f'<text x="{mx}" y="70" font-family="{SANS}" font-size="12" fill="#7a5a5d">Your Italian journey · A1.1</text>')

    # Next class card
    svg.append(f'<rect x="{mx}" y="90" width="{W-mx-30}" height="90" rx="10" fill="{BORDEAUX}"/>')
    svg.append(f'<text x="{mx+20}" y="115" font-family="{SANS}" font-size="10" fill="{GOLD}" font-weight="700" letter-spacing="2">NEXT LIVE CLASS</text>')
    svg.append(f'<text x="{mx+20}" y="145" font-family="{SERIF}" font-size="20" fill="{IVORY}" font-style="italic">Marco · Lesson 07 · Al Ristorante</text>')
    svg.append(f'<text x="{mx+20}" y="165" font-family="{SANS}" font-size="12" fill="{IVORY}">Wed 7pm ET · in 3 days</text>')
    svg.append(f'<rect x="{W-160}" y="115" width="110" height="40" rx="20" fill="{GOLD}"/>')
    svg.append(f'<text x="{W-105}" y="140" font-family="{SANS}" font-size="12" font-weight="700" fill="{BORDEAUX}" text-anchor="middle">Join class</text>')

    # Tile grid 2x2
    tiles = [
        ("📚", "My Courses", "6/20 lessons"),
        ("🤖", "Biagio Chat", "24 msgs today"),
        ("🎬", "Recordings", "12 available"),
        ("🏆", "Certificates", "1 in progress"),
    ]
    tw = (W - mx - 45) / 2
    th = 130
    for i, (ic, ttl, sub) in enumerate(tiles):
        row = i // 2
        col = i % 2
        x = mx + col*(tw+15)
        y = 210 + row*(th+15)
        svg.append(f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="12" fill="#fff" stroke="#e5d8c0"/>')
        svg.append(f'<text x="{x+20}" y="{y+45}" font-family="{SANS}" font-size="24">{ic}</text>')
        svg.append(f'<text x="{x+20}" y="{y+80}" font-family="{SERIF}" font-size="18" fill="{BORDEAUX}" font-style="italic">{ttl}</text>')
        svg.append(f'<text x="{x+20}" y="{y+105}" font-family="{SANS}" font-size="12" fill="#7a5a5d">{sub}</text>')

    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 8. SCREEN — LIVE CLASS (mini Zoom)
# ============================================================
def screen_liveclass():
    W, H = 800, 600
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    svg.append(f'<rect width="{W}" height="{H}" fill="{NAVY}"/>')
    # Header bar
    svg.append(f'<rect x="0" y="0" width="{W}" height="34" fill="#0a0203"/>')
    svg.append(f'<circle cx="18" cy="17" r="5" fill="#FF5F57"/>')
    svg.append(f'<circle cx="34" cy="17" r="5" fill="#FEBC2E"/>')
    svg.append(f'<circle cx="50" cy="17" r="5" fill="#28C840"/>')
    svg.append(f'<text x="{W/2}" y="22" font-family="{SANS}" font-size="11" fill="{IVORY}" text-anchor="middle">clubitalia.live/classroom</text>')
    svg.append(f'<circle cx="{W-100}" cy="17" r="4" fill="#e74c3c"/>')
    svg.append(f'<text x="{W-90}" y="22" font-family="{SANS}" font-size="11" fill="{GOLD}" font-weight="700">LIVE · 47:23</text>')

    # Grid: teacher big + 8 mini tiles
    # Teacher 2x2
    tx, ty, tw2, th2 = 20, 50, 380, 300
    svg.append(zoom_tile(tx, ty, tw2, th2, "Marco Rinaldi", "Roma", "#E8A87C", "#2a1005", is_teacher=True, speaking=True, big=True))

    # 8 student tiles in 2 cols x 4 rows on right
    students = [
        ("Diane", "#F0C9A8", "#8B4513"),
        ("Robert", "#D9A47A", "#3C2415"),
        ("Sarah", "#F5D5B8", "#C08040"),
        ("James", "#B8845C", "#1a0f08"),
        ("Linda", "#EFC8A5", "#6B3410"),
        ("Michael", "#C89670", "#2a1810"),
        ("Karen", "#F0C8A0", "#5C2E0F"),
        ("Steven", "#D8A075", "#302010"),
    ]
    sw = 180
    sh = 140
    sx = 415
    sy = 50
    gap = 8
    for i, (n, sk, hr) in enumerate(students):
        row = i // 2
        col = i % 2
        x = sx + col*(sw+gap)
        y = sy + row*(sh+gap)
        if row >= 2: continue  # 4 tiles fit; use 2 rows to save space
        svg.append(zoom_tile(x, y, sw, sh, n, "US", sk, hr, hand=(n=="James")))

    # More small tiles in 3rd/4th row
    small_y = 340
    sw2 = 88
    sh2 = 80
    for i, (n, sk, hr) in enumerate(students[4:]):
        x = 415 + i*(sw2+8)
        svg.append(zoom_tile(x, small_y, sw2, sh2, n[:6], "", sk, hr))

    # Captions
    svg.append(f'<rect x="60" y="450" width="{W-120}" height="50" rx="6" fill="rgba(0,0,0,0.9)" stroke="{GOLD}"/>')
    svg.append(f'<text x="{W/2}" y="470" font-family="{SANS}" font-size="9" fill="{GOLD}" text-anchor="middle" font-weight="700">LIVE CAPTIONS · IT</text>')
    svg.append(f'<text x="{W/2}" y="490" font-family="{SANS}" font-size="12" fill="{IVORY}" text-anchor="middle">MARCO: "Allora, ripetiamo insieme. Al bar io prendo un caffè."</text>')

    # Toolbar
    svg.append(f'<rect x="0" y="530" width="{W}" height="70" fill="#0a0203"/>')
    tools = [("🎙", "Mute"), ("📹", "Video"), ("💬", "Chat"), ("✋", "Hand"), ("📞", "Leave")]
    for i, (ic, lbl) in enumerate(tools):
        bx = 100 + i*130
        col = "#B72020" if lbl=="Leave" else "rgba(255,255,255,0.08)"
        svg.append(f'<rect x="{bx}" y="545" width="110" height="40" rx="20" fill="{col}"/>')
        svg.append(f'<text x="{bx+55}" y="570" font-family="{SANS}" font-size="12" fill="{IVORY}" text-anchor="middle">{ic} {lbl}</text>')

    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 9. SCREEN — BIAGIO chat
# ============================================================
def screen_biagio():
    W, H = 800, 600
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    svg.append(f'<rect width="{W}" height="{H}" fill="{IVORY}"/>')
    # Header
    svg.append(f'<rect x="0" y="0" width="{W}" height="72" fill="{BORDEAUX}"/>')
    svg.append(f'<circle cx="40" cy="36" r="22" fill="{GOLD}"/>')
    svg.append(f'<text x="40" y="42" font-family="{SERIF}" font-size="22" fill="{BORDEAUX}" text-anchor="middle" font-style="italic" font-weight="700">B</text>')
    svg.append(f'<text x="80" y="34" font-family="{SERIF}" font-size="20" fill="{IVORY}" font-style="italic">Biagio</text>')
    svg.append(f'<text x="80" y="54" font-family="{SANS}" font-size="12" fill="{GOLD}">Your Italian AI tutor · online</text>')
    svg.append(f'<circle cx="{W-30}" cy="36" r="5" fill="#28C840"/>')

    # Chat conversation
    msgs = [
        ("bot", "Ciao Diane! Come stai oggi?"),
        ("user", "Ciao Biagio! Io sono bene, grazie."),
        ("bot", "Quasi perfetto! Piccola correzione: → \"Io sto bene, grazie.\"  (state of being = STARE, not ESSERE)"),
        ("user", "Ah! Grazie. Io sto bene."),
        ("bot", "Bravissima! Ora, dimmi cosa hai fatto stamattina."),
    ]
    y = 100
    for role, txt in msgs:
        if role == "user":
            # Right-aligned bubble
            bw = min(len(txt)*8 + 40, 500)
            bx = W - 30 - bw
            svg.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="50" rx="16" fill="{BORDEAUX}"/>')
            svg.append(f'<text x="{bx+bw/2}" y="{y+30}" font-family="{SANS}" font-size="14" fill="{IVORY}" text-anchor="middle">{txt}</text>')
            svg.append(f'<text x="{W-30}" y="{y+68}" font-family="{SANS}" font-size="10" fill="#7a5a5d" text-anchor="end">Diane · read</text>')
            y += 90
        else:
            # Left-aligned bubble
            bw = min(len(txt)*7.5 + 40, 560)
            bx = 30
            # Show correction highlighting for message 3
            fill = "#fff"
            stroke = GOLD if "correction" in txt.lower() else "#e5d8c0"
            svg.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="{60 if "→" in txt else 50}" rx="16" fill="{fill}" stroke="{stroke}" stroke-width="{2 if "→" in txt else 1}"/>')
            if "→" in txt:
                # Two lines
                parts = txt.split("→")
                svg.append(f'<text x="{bx+18}" y="{y+25}" font-family="{SANS}" font-size="12" fill="{TERRA}" font-weight="600">✎ {parts[0].strip()}</text>')
                svg.append(f'<text x="{bx+18}" y="{y+48}" font-family="{SERIF}" font-size="14" fill="{BORDEAUX}" font-style="italic">→ {parts[1].strip()}</text>')
            else:
                svg.append(f'<text x="{bx+20}" y="{y+30}" font-family="{SANS}" font-size="14" fill="{BORDEAUX}">{txt}</text>')
            svg.append(f'<text x="{bx+18}" y="{y+80}" font-family="{SANS}" font-size="10" fill="#7a5a5d">Biagio · just now</text>')
            y += 100

    # Input bar
    svg.append(f'<rect x="0" y="{H-60}" width="{W}" height="60" fill="#fff" stroke="#e5d8c0"/>')
    svg.append(f'<rect x="20" y="{H-45}" width="{W-140}" height="34" rx="17" fill="{IVORY}" stroke="#c9c0ac"/>')
    svg.append(f'<text x="35" y="{H-24}" font-family="{SANS}" font-size="13" fill="#8a7860">Rispondi in italiano...</text>')
    svg.append(f'<rect x="{W-110}" y="{H-45}" width="90" height="34" rx="17" fill="{GOLD}"/>')
    svg.append(f'<text x="{W-65}" y="{H-24}" font-family="{SANS}" font-size="13" fill="{BORDEAUX}" text-anchor="middle" font-weight="700">Invia →</text>')

    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 10. SCREEN — CERTIFICATE mini
# ============================================================
def screen_certificate():
    W, H = 800, 600
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    svg.append(f'<rect width="{W}" height="{H}" fill="#f0e6d3"/>')
    # Certificate paper
    svg.append(f'<rect x="60" y="40" width="{W-120}" height="{H-80}" rx="4" fill="{IVORY}" stroke="#c9a24b" stroke-width="1"/>')
    # Border
    svg.append(f'<rect x="80" y="60" width="{W-160}" height="{H-120}" fill="none" stroke="{GOLD}" stroke-width="2"/>')
    svg.append(f'<rect x="88" y="68" width="{W-176}" height="{H-136}" fill="none" stroke="{GOLD}" stroke-width="0.5"/>')

    # Corner ornaments
    for cx, cy in [(100, 80), (W-100, 80), (100, H-80), (W-100, H-80)]:
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="8" fill="none" stroke="{GOLD}"/>')
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{GOLD}"/>')

    svg.append(f'<text x="{W/2}" y="130" font-family="{SANS}" font-size="10" fill="{BORDEAUX}" text-anchor="middle" letter-spacing="4" font-weight="700">CLUB ITALIA · ETEACHER GROUP</text>')

    svg.append(f'<text x="{W/2}" y="200" font-family="{SERIF}" font-size="40" fill="{BORDEAUX}" text-anchor="middle" font-style="italic">Certificate of Completion</text>')

    # Tricolor divider
    svg.append(f'<rect x="{W/2-45}" y="220" width="30" height="3" fill="{GREEN_IT}"/>')
    svg.append(f'<rect x="{W/2-15}" y="220" width="30" height="3" fill="{WHITE_IT}" stroke="#c9c0ac" stroke-width="0.3"/>')
    svg.append(f'<rect x="{W/2+15}" y="220" width="30" height="3" fill="{RED_IT}"/>')

    svg.append(f'<text x="{W/2}" y="270" font-family="{SANS}" font-size="12" fill="#7a5a5d" text-anchor="middle" letter-spacing="3">AWARDED TO</text>')
    svg.append(f'<text x="{W/2}" y="325" font-family="{SERIF}" font-size="46" fill="{BORDEAUX}" text-anchor="middle" font-style="italic">Diane Costanza</text>')
    svg.append(f'<line x1="{W/2-160}" y1="345" x2="{W/2+160}" y2="345" stroke="{GOLD}" stroke-width="0.8"/>')

    svg.append(f'<text x="{W/2}" y="380" font-family="{SANS}" font-size="13" fill="#5a3a3d" text-anchor="middle">For successful completion of</text>')
    svg.append(f'<text x="{W/2}" y="420" font-family="{SERIF}" font-size="26" fill="{BORDEAUX}" text-anchor="middle" font-style="italic">CI Elementare · A1.1 → A1.2</text>')

    # Signature + date
    svg.append(f'<line x1="140" y1="490" x2="320" y2="490" stroke="{BORDEAUX}"/>')
    svg.append(f'<text x="230" y="486" font-family="{SERIF}" font-size="16" fill="{BORDEAUX}" text-anchor="middle" font-style="italic">Alessandro Ferri</text>')
    svg.append(f'<text x="230" y="506" font-family="{SANS}" font-size="9" fill="#7a5a5d" text-anchor="middle" letter-spacing="1">HEAD OF FACULTY</text>')

    # Seal
    svg.append(f'<circle cx="{W/2}" cy="500" r="32" fill="none" stroke="{GOLD}" stroke-width="1.5"/>')
    svg.append(f'<text x="{W/2}" y="500" font-family="{SERIF}" font-size="14" fill="{BORDEAUX}" text-anchor="middle" font-style="italic" font-weight="700">eT</text>')
    svg.append(f'<text x="{W/2}" y="515" font-family="{SANS}" font-size="6" fill="{GOLD}" text-anchor="middle" letter-spacing="1">VERIFIED</text>')

    svg.append(f'<line x1="{W-320}" y1="490" x2="{W-140}" y2="490" stroke="{BORDEAUX}"/>')
    svg.append(f'<text x="{W-230}" y="486" font-family="{SERIF}" font-size="16" fill="{BORDEAUX}" text-anchor="middle" font-style="italic">15 December 2026</text>')
    svg.append(f'<text x="{W-230}" y="506" font-family="{SANS}" font-size="9" fill="#7a5a5d" text-anchor="middle" letter-spacing="1">DATE ISSUED</text>')

    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 11. TRUSTPILOT LOGO
# ============================================================
def trustpilot_logo():
    W, H = 200, 40
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    # 5 stars
    for i in range(5):
        cx = 15 + i*22
        cy = 20
        svg.append(f'<rect x="{cx-10}" y="{cy-10}" width="20" height="20" fill="{TRUSTGREEN}"/>')
        # Star path in white
        star = f"M {cx} {cy-6} L {cx+1.8} {cy-2} L {cx+6} {cy-2} L {cx+2.5} {cy+1} L {cx+4} {cy+6} L {cx} {cy+3.5} L {cx-4} {cy+6} L {cx-2.5} {cy+1} L {cx-6} {cy-2} L {cx-1.8} {cy-2} Z"
        svg.append(f'<path d="{star}" fill="#fff"/>')
    # Wordmark
    svg.append(f'<text x="128" y="26" font-family="{SANS}" font-size="15" font-weight="700" fill="#191919">Trustpilot</text>')
    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 12. CEFR LOGO
# ============================================================
def cefr_logo():
    W, H = 200, 60
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    svg.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="6" fill="none" stroke="#003399" stroke-width="1.5"/>')
    # EU-style star ring on left
    scx, scy = 30, 30
    svg.append(f'<circle cx="{scx}" cy="{scy}" r="20" fill="#003399"/>')
    import math
    for i in range(12):
        a = i * (2*math.pi/12) - math.pi/2
        px = scx + 14*math.cos(a)
        py = scy + 14*math.sin(a)
        svg.append(f'<circle cx="{px}" cy="{py}" r="1.6" fill="#FFCC00"/>')
    # Text
    svg.append(f'<text x="60" y="26" font-family="{SANS}" font-size="14" font-weight="700" fill="#003399">CEFR ALIGNED</text>')
    svg.append(f'<text x="60" y="44" font-family="{SANS}" font-size="10" fill="#003399" letter-spacing="1">Council of Europe · A1–C2</text>')
    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 13. ETEACHER LOGO
# ============================================================
def eteacher_logo():
    W, H = 300, 80
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    # Circle mark
    svg.append(f'<circle cx="42" cy="40" r="28" fill="{BORDEAUX}"/>')
    svg.append(f'<text x="42" y="52" font-family="{SERIF}" font-size="34" font-style="italic" font-weight="700" fill="{GOLD}" text-anchor="middle">eT</text>')
    # Wordmark
    svg.append(f'<text x="85" y="42" font-family="{SERIF}" font-size="30" font-style="italic" fill="{BORDEAUX}">eTeacher</text>')
    svg.append(f'<text x="85" y="63" font-family="{SANS}" font-size="10" fill="#7a5a5d" letter-spacing="6">GROUP · EST. 2000</text>')
    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 14. GUARANTEE BADGE
# ============================================================
def guarantee_badge():
    W, H = 300, 300
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    cx, cy = W/2, H/2
    # Outer scalloped circle
    import math
    scallops = 36
    r_out = 140
    r_in = 130
    pts = []
    for i in range(scallops*2):
        r = r_out if i % 2 == 0 else r_in
        a = i * (2*math.pi / (scallops*2)) - math.pi/2
        pts.append(f"{cx + r*math.cos(a):.1f},{cy + r*math.sin(a):.1f}")
    svg.append(f'<polygon points="{" ".join(pts)}" fill="{GOLD}"/>')
    # Inner circles
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="120" fill="{BORDEAUX}"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="112" fill="none" stroke="{GOLD}" stroke-width="1.5"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="108" fill="none" stroke="{GOLD}" stroke-width="0.5"/>')

    # Curved top text
    svg.append(f'<defs><path id="topArc" d="M {cx-95} {cy} A 95 95 0 0 1 {cx+95} {cy}"/></defs>')
    svg.append(f'<text font-family="{SANS}" font-size="13" fill="{GOLD}" letter-spacing="4" font-weight="700"><textPath href="#topArc" startOffset="50%" text-anchor="middle">7-DAY MONEY-BACK</textPath></text>')

    # Big number
    svg.append(f'<text x="{cx}" y="{cy-5}" font-family="{SERIF}" font-size="70" fill="{GOLD}" text-anchor="middle" font-style="italic" font-weight="700">7</text>')
    svg.append(f'<text x="{cx}" y="{cy+30}" font-family="{SERIF}" font-size="22" fill="{IVORY}" text-anchor="middle" font-style="italic">DAY</text>')
    svg.append(f'<text x="{cx}" y="{cy+55}" font-family="{SANS}" font-size="10" fill="{GOLD}" text-anchor="middle" letter-spacing="3">GUARANTEE</text>')

    # Curved bottom text
    svg.append(f'<defs><path id="botArc" d="M {cx-90} {cy+30} A 90 90 0 0 0 {cx+90} {cy+30}"/></defs>')
    svg.append(f'<text font-family="{SANS}" font-size="11" fill="{GOLD}" letter-spacing="6" font-weight="600"><textPath href="#botArc" startOffset="50%" text-anchor="middle">CLUB ITALIA</textPath></text>')

    # Ribbon accents
    svg.append(f'<circle cx="{cx-95}" cy="{cy}" r="4" fill="{GOLD}"/>')
    svg.append(f'<circle cx="{cx+95}" cy="{cy}" r="4" fill="{GOLD}"/>')

    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 15. PAYMETHODS
# ============================================================
def paymethods():
    W, H = 500, 60
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    # Visa
    svg.append(f'<rect x="10" y="15" width="70" height="30" rx="4" fill="#fff" stroke="#e5d8c0"/>')
    svg.append(f'<text x="45" y="35" font-family="{SANS}" font-size="14" font-weight="900" fill="#1a1f71" text-anchor="middle" font-style="italic">VISA</text>')
    # Mastercard
    svg.append(f'<rect x="95" y="15" width="70" height="30" rx="4" fill="#fff" stroke="#e5d8c0"/>')
    svg.append(f'<circle cx="122" cy="30" r="9" fill="#EB001B"/>')
    svg.append(f'<circle cx="138" cy="30" r="9" fill="#F79E1B" opacity="0.85"/>')
    # Amex
    svg.append(f'<rect x="180" y="15" width="70" height="30" rx="4" fill="#006FCF"/>')
    svg.append(f'<text x="215" y="35" font-family="{SANS}" font-size="13" font-weight="900" fill="#fff" text-anchor="middle">AMEX</text>')
    # Apple Pay
    svg.append(f'<rect x="265" y="15" width="100" height="30" rx="4" fill="#000"/>')
    svg.append(f'<text x="285" y="35" font-family="{SANS}" font-size="16" fill="#fff" text-anchor="middle"></text>')
    svg.append(f'<text x="315" y="35" font-family="{SANS}" font-size="13" font-weight="600" fill="#fff" text-anchor="middle">Pay</text>')
    # Google Pay
    svg.append(f'<rect x="380" y="15" width="110" height="30" rx="4" fill="#fff" stroke="#e5d8c0"/>')
    svg.append(f'<text x="405" y="35" font-family="{SANS}" font-size="13" font-weight="700" fill="#5f6368" text-anchor="middle">G</text>')
    svg.append(f'<text x="440" y="35" font-family="{SANS}" font-size="13" font-weight="500" fill="#5f6368" text-anchor="middle">Pay</text>')
    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# 16. TRICOLOR RULE
# ============================================================
def tricolor_rule():
    W, H = 400, 8
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    svg.append(f'<rect x="0" y="0" width="{W/3}" height="{H}" fill="{GREEN_IT}"/>')
    svg.append(f'<rect x="{W/3}" y="0" width="{W/3}" height="{H}" fill="{WHITE_IT}"/>')
    svg.append(f'<rect x="{2*W/3}" y="0" width="{W/3}" height="{H}" fill="{RED_IT}"/>')
    svg.append('</svg>')
    return "\n".join(svg)


# ============================================================
# BUILD ALL
# ============================================================
def main():
    files = {
        "zoom-mockup.svg": zoom_mockup(),
        "zoom-mockup-2.svg": zoom_mockup_2(),
        "dashboard-mockup.svg": dashboard_mockup(),
        "certificate-mockup.svg": certificate_mockup(),
        "checkout-mockup.svg": checkout_mockup(),
        "screen-placement.svg": screen_placement(),
        "screen-platform.svg": screen_platform(),
        "screen-liveclass.svg": screen_liveclass(),
        "screen-biagio.svg": screen_biagio(),
        "screen-certificate.svg": screen_certificate(),
        "trustpilot-logo.svg": trustpilot_logo(),
        "cefr-logo.svg": cefr_logo(),
        "eteacher-logo.svg": eteacher_logo(),
        "guarantee-badge.svg": guarantee_badge(),
        "paymethods.svg": paymethods(),
        "tricolor-rule.svg": tricolor_rule(),
    }
    for name, content in files.items():
        path = os.path.join(OUT, name)
        with open(path, "w") as f:
            f.write(content)
        print(f"WROTE {path} ({len(content)} bytes)")
    print(f"\nTotal: {len(files)} SVG files")

if __name__ == "__main__":
    main()
