"""Generate elegant SVG placeholder images for every referenced img — so the site renders now.
Style: warm gradient Bordeaux/gold/ivory with subtle serif label. Real fal images will overwrite."""
from pathlib import Path
import os, re

IMG_DIR = Path("assets/img")
IMG_DIR.mkdir(parents=True, exist_ok=True)

# Discover every referenced image path in the html
needed = set()
for html in Path(".").rglob("*.html"):
    for m in re.finditer(r'assets/img/([\w\-\.]+)', html.read_text()):
        needed.add(m.group(1))

# Palette variants
themes = {
    'hero':      ('#3A0E12','#8E3D22','#C9A24B'),
    'course':    ('#5A1520','#B65538','#DDB86A'),
    'pillar':    ('#22080B','#3A0E12','#C9A24B'),
    'cap':       ('#4A1A20','#8E3D22','#DDB86A'),
    'spoken':    ('#3A0E12','#B65538','#C9A24B'),
    'teacher':   ('#4A1A20','#7A1F2B','#DDB86A'),
    'biagio':    ('#3A0E12','#4A1A20','#C9A24B'),
    'class':     ('#22080B','#4A1A20','#DDB86A'),
}
def theme_of(name):
    for k in themes:
        if name.startswith(k): return themes[k]
    return themes['hero']

for name in sorted(needed):
    out = IMG_DIR / name
    if out.exists() and out.stat().st_size > 500:  # keep real images
        continue
    c1,c2,c3 = theme_of(name)
    label = name.rsplit('.',1)[0].replace('-',' ').replace('_',' ').title()
    # Aspect
    is_portrait = name.startswith(('pillar','teacher','biagio'))
    w, h = (900, 1125) if is_portrait else (1600, 900)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice">
<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
<stop offset="0%" stop-color="{c1}"/><stop offset="60%" stop-color="{c2}"/><stop offset="100%" stop-color="{c3}" stop-opacity=".85"/>
</linearGradient>
<radialGradient id="r" cx="30%" cy="30%" r="70%">
<stop offset="0%" stop-color="{c3}" stop-opacity=".35"/><stop offset="100%" stop-color="{c1}" stop-opacity="0"/>
</radialGradient>
<pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse">
<path d="M60 0H0V60" fill="none" stroke="{c3}" stroke-opacity=".05" stroke-width="1"/>
</pattern>
</defs>
<rect width="100%" height="100%" fill="url(#g)"/>
<rect width="100%" height="100%" fill="url(#r)"/>
<rect width="100%" height="100%" fill="url(#grid)"/>
<text x="50%" y="45%" font-family="Georgia, serif" font-style="italic" font-size="{int(h/12)}" fill="{c3}" fill-opacity=".85" text-anchor="middle">Club Italia</text>
<text x="50%" y="55%" font-family="Georgia, serif" font-size="{int(h/18)}" fill="#F3EEE3" fill-opacity=".9" text-anchor="middle">{label}</text>
<line x1="35%" y1="63%" x2="65%" y2="63%" stroke="{c3}" stroke-opacity=".5"/>
<text x="50%" y="70%" font-family="Arial, sans-serif" font-size="{int(h/40)}" fill="#F3EEE3" fill-opacity=".55" text-anchor="middle" letter-spacing="6">LIVE FROM ITALY</text>
</svg>'''
    # Save as .svg and also copy under the requested .jpg/.png filename (browsers serve svg content-type based on ext)
    # Better: save as actual svg, then create html-side redirect via same filename. Simpler: save as .svg file too, but html references .jpg/.png.
    # Trick: write the svg data to the .jpg/.png filename — browsers WILL render it if we serve with correct MIME.
    # For GitHub Pages / most static hosts, .jpg extension gets image/jpeg mime and browser will NOT render svg.
    # Solution: write proper svg content but ALSO patch every html to use the .svg. Easier: convert SVG to PNG.
    # We use cairosvg for real raster.
    (IMG_DIR / (name.rsplit('.',1)[0] + '.svg')).write_text(svg)

# Now convert every .svg → matching raster file
try:
    import cairosvg
    for svg_file in IMG_DIR.glob("*.svg"):
        base = svg_file.stem
        for ext in ('.jpg','.png'):
            target = IMG_DIR / (base + ext)
            if target.exists() and target.stat().st_size > 2000:
                continue  # keep fal-generated real image
            if ext == '.png':
                cairosvg.svg2png(bytestring=svg_file.read_bytes(), write_to=str(target), output_width=900 if 'pillar' in base or 'teacher' in base or 'biagio' in base else 1600)
            else:
                # convert to png then rely on filename mime — actually make it a real jpg
                png_bytes = cairosvg.svg2png(bytestring=svg_file.read_bytes(), output_width=1600 if not ('pillar' in base or 'teacher' in base) else 900)
                from PIL import Image
                import io
                Image.open(io.BytesIO(png_bytes)).convert('RGB').save(target, 'JPEG', quality=82)
    print(f"generated placeholders for {len(needed)} slots")
except ImportError as e:
    print(f"missing lib: {e}")
