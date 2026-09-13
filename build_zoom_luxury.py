"""Build luxury Zoom classroom mockup — Julie pattern, Club Italia branding."""
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os

IMG_DIR = "/home/user/workspace/club-italia/assets/img"
OUT = os.path.join(IMG_DIR, "zoom-classroom-luxury.jpg")

W, H = 2400, 1350
BG = (5, 7, 13)              # #05070d
BAR = (13, 17, 25)           # #0d1119
ACCENT_BLUE = (94, 182, 255) # #5EB6FF
GOLD = (204, 168, 92)
PALE_GREEN = (170, 240, 190)
REC_RED = (255, 80, 80)
LEAVE_BURGUNDY = (140, 45, 65)

# Fonts
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_ITAL = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"

def font(size, bold=False, italic=False):
    if bold: return ImageFont.truetype(FONT_BOLD, size)
    if italic: return ImageFont.truetype(FONT_ITAL, size)
    return ImageFont.truetype(FONT_REG, size)


def rounded_mask(size, radius):
    """Return an L-mode rounded-rect mask of given size."""
    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle([(0, 0), (size[0] - 1, size[1] - 1)], radius=radius, fill=255)
    return mask


def paste_photo(canvas, src_path, box, radius=14, border=None, face_bias=0.30,
                mode="cover", inner_bg=(20, 24, 34)):
    """Paste `src_path` into `box`=(x,y,w,h), rounded corners.
    mode: "cover" fills the box; "contain" fits with letterbox using inner_bg.
    face_bias: 0.0=top of image, 1.0=bottom (used for cover-mode vertical bias).
    border = (color, width) draws a border on top."""
    x, y, w, h = box
    im = Image.open(src_path).convert("RGB")
    sw, sh = im.size
    target_ratio = w / h
    src_ratio = sw / sh

    tile = Image.new("RGB", (w, h), inner_bg)

    if mode == "cover":
        if src_ratio > target_ratio:
            new_w = int(sh * target_ratio)
            left = (sw - new_w) // 2
            im = im.crop((left, 0, left + new_w, sh))
        else:
            new_h = int(sw / target_ratio)
            top = int((sh - new_h) * face_bias)
            top = max(0, min(top, sh - new_h))
            im = im.crop((0, top, sw, top + new_h))
        im = im.resize((w, h), Image.LANCZOS)
        tile.paste(im, (0, 0))
    else:  # contain
        if src_ratio > target_ratio:
            nw, nh = w, int(w / src_ratio)
        else:
            nh, nw = h, int(h * src_ratio)
        im = im.resize((nw, nh), Image.LANCZOS)
        tile.paste(im, ((w - nw) // 2, (h - nh) // 2))

    mask = rounded_mask((w, h), radius)
    canvas.paste(tile, (x, y), mask)

    if border:
        color, bw = border
        d = ImageDraw.Draw(canvas)
        for i in range(bw):
            d.rounded_rectangle(
                [(x - i, y - i), (x + w - 1 + i, y + h - 1 + i)],
                radius=radius + i, outline=color, width=1)


def draw_name_label(canvas, xy, text, font_obj, pad_x=16, pad_y=8):
    """Draw name label pill (dark rgba)."""
    x, y = xy
    # measure text
    tmp_d = ImageDraw.Draw(canvas)
    bbox = tmp_d.textbbox((0, 0), text, font=font_obj)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pw = tw + pad_x * 2
    ph = th + pad_y * 2 + 6
    # translucent pill via a temp RGBA layer
    pill = Image.new("RGBA", (pw, ph), (2, 4, 9, 220))
    pill_mask = rounded_mask((pw, ph), 6)
    canvas.paste(pill, (x, y), pill_mask)
    d = ImageDraw.Draw(canvas)
    d.text((x + pad_x - bbox[0], y + pad_y - bbox[1] + 2), text, font=font_obj, fill=(255, 255, 255))


def draw_chip(canvas, xy, icon, label, font_obj, w=None, tint=None):
    """Draw a bottom control chip. Returns width used."""
    x, y = xy
    text = f"{icon}  {label}"
    tmp_d = ImageDraw.Draw(canvas)
    bbox = tmp_d.textbbox((0, 0), text, font=font_obj)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pad_x, pad_y = 22, 12
    pw = (w or tw + pad_x * 2)
    ph = 46
    bg_color = (26, 33, 46, 235) if tint is None else (tint[0], tint[1], tint[2], 235)
    pill = Image.new("RGBA", (pw, ph), bg_color)
    pill_mask = rounded_mask((pw, ph), 12)
    canvas.paste(pill, (x, y), pill_mask)
    d = ImageDraw.Draw(canvas)
    txt_color = (255, 235, 235) if tint else (232, 236, 244)
    d.text((x + (pw - tw) // 2 - bbox[0], y + (ph - th) // 2 - bbox[1]), text, font=font_obj, fill=txt_color)
    return pw


def _render_host_tile(canvas, box, src_path):
    """Draw the host tile: contain Marco centered on a soft gradient panel,
    then add left/right decorative branding blocks and the accent blue border."""
    x, y, w, h = box
    # base dark panel with subtle vertical gradient
    panel = Image.new("RGB", (w, h), (10, 12, 20))
    pdraw = ImageDraw.Draw(panel)
    # Radial-ish gradient via concentric ellipses (fake vignette center)
    for i in range(40, 0, -1):
        alpha = int(120 * (i / 40))
        overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        odraw = ImageDraw.Draw(overlay)
        rw = int(w * (0.55 + i * 0.02))
        rh = int(h * (0.55 + i * 0.02))
        odraw.ellipse([((w - rw) // 2, (h - rh) // 2), ((w + rw) // 2, (h + rh) // 2)],
                      fill=(30, 36, 58, alpha // 6))
        panel = Image.alpha_composite(panel.convert("RGBA"), overlay).convert("RGB")
    # place Marco centered
    im = Image.open(src_path).convert("RGB")
    sw, sh = im.size
    src_ratio = sw / sh
    target_ratio = w / h
    if src_ratio > target_ratio:
        nw, nh = w, int(w / src_ratio)
    else:
        nh, nw = h, int(h * src_ratio)
    im = im.resize((nw, nh), Image.LANCZOS)
    panel.paste(im, ((w - nw) // 2, (h - nh) // 2))

    # Add subtle side branding: "LIVE FROM ROMA" left, "CLUB ITALIA" right
    left_x = 60
    right_x = w - 60
    center_y = h // 2
    pdraw = ImageDraw.Draw(panel)
    brand_font_lg = font(44, bold=True)
    brand_font_sm = font(20, bold=True)
    tag_font = font(16)
    # Left column — live indicator
    live_col_x = 40
    # small pulsing dot
    pdraw.ellipse([(live_col_x, center_y - 100), (live_col_x + 14, center_y - 86)], fill=(120, 220, 150))
    pdraw.text((live_col_x + 24, center_y - 104), "LIVE", font=brand_font_sm, fill=(180, 230, 200))
    pdraw.text((live_col_x, center_y - 70), "from Rome", font=tag_font, fill=(170, 180, 200))
    pdraw.text((live_col_x, center_y - 40), "\u2022 Faculty broadcast", font=tag_font, fill=(130, 140, 160))
    # Right column — course meta
    right_col_x = w - 260
    pdraw.text((right_col_x, center_y - 104), "CI \u2022 PRINCIPIANTE", font=brand_font_sm, fill=(200, 180, 130))
    pdraw.text((right_col_x, center_y - 70), "Lesson 4 \u2014 Il caff\u00e8", font=tag_font, fill=(170, 180, 200))
    pdraw.text((right_col_x, center_y - 40), "Cohort of 12 \u2022 CEFR A1", font=tag_font, fill=(130, 140, 160))

    # Round corners + border
    mask = rounded_mask((w, h), 14)
    canvas.paste(panel, (x, y), mask)
    d = ImageDraw.Draw(canvas)
    for i in range(2):
        d.rounded_rectangle(
            [(x - i, y - i), (x + w - 1 + i, y + h - 1 + i)],
            radius=14 + i, outline=ACCENT_BLUE, width=1)


def main():
    canvas = Image.new("RGB", (W, H), BG)

    # --- TOP BAR ---
    top_h = 80
    d = ImageDraw.Draw(canvas)
    d.rectangle([(0, 0), (W, top_h)], fill=BAR)
    # subtle bottom hairline
    d.line([(0, top_h), (W, top_h)], fill=(30, 38, 55), width=1)

    top_font = font(24, bold=True)
    small_font = font(20)
    ital_font = font(20, italic=True)

    # Left side title
    left_title = "Club Italia"
    course = "CI Principiante · Lesson 4 · Roma"
    d.text((36, 26), left_title, font=top_font, fill=(255, 255, 255))
    # gold divider dot
    bbox = d.textbbox((36, 26), left_title, font=top_font)
    dot_x = bbox[2] + 14
    d.ellipse([(dot_x, 40), (dot_x + 8, 48)], fill=GOLD)
    d.text((dot_x + 20, 28), course, font=small_font, fill=(210, 218, 232))

    # Right: pulsing REC + timestamp
    rec_text = "REC"
    time_text = "01:14:22"
    # timestamp
    tbox = d.textbbox((0, 0), time_text, font=small_font)
    tw = tbox[2] - tbox[0]
    d.text((W - 36 - tw, 28), time_text, font=small_font, fill=(210, 218, 232))
    # REC block
    rec_bbox = d.textbbox((0, 0), rec_text, font=ital_font)
    rec_w = rec_bbox[2] - rec_bbox[0]
    rec_x = W - 36 - tw - 24 - rec_w
    d.text((rec_x, 28), rec_text, font=ital_font, fill=PALE_GREEN)
    # pulsing dot (with soft glow)
    dot_cx = rec_x - 18
    dot_cy = 44
    # glow
    glow = Image.new("RGBA", (60, 60), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse([(20, 20), (40, 40)], fill=(255, 60, 60, 120))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=6))
    canvas.paste(glow, (dot_cx - 30, dot_cy - 30), glow)
    d.ellipse([(dot_cx - 7, dot_cy - 7), (dot_cx + 7, dot_cy + 7)], fill=REC_RED)

    # --- MAIN AREA ---
    pad = 24
    bottom_h = 82
    main_top = top_h + pad
    main_bottom = H - bottom_h - pad
    main_w = W - pad * 2

    # HOST TILE (Marco) — dominates upper 2/3, Julie-style
    host_x = pad
    host_w = main_w
    gap = 16
    tiles_gap = 12
    tile_w = (main_w - 4 * tiles_gap) // 5
    tile_h = int(tile_w * 9 / 16)
    available = main_bottom - main_top
    host_h = available - tile_h - gap   # host takes remainder

    host_box = (host_x, main_top, host_w, host_h)
    # Marco is portrait 1200x1600. Use contain so his face + shoulders stay
    # fully visible; letterbox with a soft dark-navy gradient so pillarboxing
    # feels like an intentional Zoom "virtual background" panel.
    _render_host_tile(canvas, host_box, os.path.join(IMG_DIR, "teacher-marco.jpg"))

    # Name label for host — bottom-left of tile
    host_name_font = font(26, bold=True)
    draw_name_label(canvas, (host_x + 20, main_top + host_h - 60),
                    "Marco Rinaldi · Rome", host_name_font)

    # STUDENT ROW
    students = [
        ("student-01-sarah.jpg",   "Sarah · Boston"),
        ("student-02-david.jpg",   "David · London"),
        ("student-03-elena.jpg",   "Elena · Toronto"),
        ("student-04-michael.jpg", "Michael · Sydney"),
        ("student-05-anna.jpg",    "Anna · Berlin"),
    ]
    row_y = main_top + host_h + gap
    label_font = font(20, bold=True)
    for i, (fname, label) in enumerate(students):
        x = pad + i * (tile_w + tiles_gap)
        paste_photo(canvas, os.path.join(IMG_DIR, fname),
                    (x, row_y, tile_w, tile_h), radius=12)
        draw_name_label(canvas, (x + 12, row_y + tile_h - 44),
                        label, label_font, pad_x=12, pad_y=6)

    # --- BOTTOM CONTROL BAR ---
    d = ImageDraw.Draw(canvas)
    bar_top = H - bottom_h
    d.rectangle([(0, bar_top), (W, H)], fill=BAR)
    d.line([(0, bar_top), (W, bar_top)], fill=(30, 38, 55), width=1)

    chip_font = font(20, bold=True)
    # Use geometric Unicode shapes reliably in LiberationSans-Bold
    chips = [
        ("\u25CF", "Mute"),          # ● filled circle
        ("\u25A0", "Video"),         # ■ square
        ("\u25B2", "Share"),         # ▲ triangle up
        ("\u2666", "Participants (12)"),  # ♦ diamond
        ("\u2665", "Reactions"),     # ♥ heart
        ("\u25CF", "Leave"),         # circle (tinted burgundy)
    ]
    # measure total width
    tmp = ImageDraw.Draw(canvas)
    widths = []
    for icon, lbl in chips:
        text = f"{icon}  {lbl}"
        b = tmp.textbbox((0, 0), text, font=chip_font)
        widths.append(b[2] - b[0] + 44)
    chip_gap = 14
    total = sum(widths) + chip_gap * (len(chips) - 1)
    start_x = (W - total) // 2
    y = bar_top + (bottom_h - 46) // 2
    for i, (icon, lbl) in enumerate(chips):
        tint = LEAVE_BURGUNDY if lbl == "Leave" else None
        draw_chip(canvas, (start_x, y), icon, lbl, chip_font, w=widths[i], tint=tint)
        start_x += widths[i] + chip_gap

    # Save
    canvas.save(OUT, "JPEG", quality=82, optimize=True, progressive=True)
    size = os.path.getsize(OUT)
    print(f"Saved {OUT} — {W}x{H} — {size:,} bytes ({size/1024:.1f} KB)")


if __name__ == "__main__":
    main()
