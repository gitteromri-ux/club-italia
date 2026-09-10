"""Common HTML fragments and helpers for v4 rebuild."""
from pathlib import Path

ROOT = Path("/home/user/workspace/club-italia")
NAV = (ROOT / "_partials/nav.html").read_text()
FOOTER = (ROOT / "_partials/footer.html").read_text()

CSS_HREF_ROOT = "css/ci.css?v=v4"
CSS_HREF_SUB1 = "../../css/ci.css?v=v4"
JS_HREF_ROOT = "js/ci.js?v=v4"
JS_HREF_SUB1 = "../../js/ci.js?v=v4"

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,500;1,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">"""

def rewrite_partial(partial: str, depth: int) -> str:
    """Rewrite hrefs in nav/footer for nested pages."""
    if depth == 0:
        return partial
    prefix = "../" * depth
    out = partial
    import re
    def sub_href(m):
        val = m.group(2)
        if val.startswith(("http", "mailto:", "#", "/")):
            return m.group(0)
        return f'{m.group(1)}="{prefix}{val}"'
    out = re.sub(r'(href|src)="([^"]+)"', sub_href, out)
    return out

def head(title, desc, depth=0):
    css = CSS_HREF_ROOT if depth == 0 else "../" * depth + "css/ci.css?v=v4"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{FONTS}
<link rel="stylesheet" href="{css}">
<link rel="icon" type="image/svg+xml" href="{'' if depth == 0 else '../' * depth}assets/img/cefr-logo.svg">
</head>
<body class="v4">"""

def footer_scripts(depth=0):
    js = JS_HREF_ROOT if depth == 0 else "../" * depth + "js/ci.js?v=v4"
    return f"""{rewrite_partial(FOOTER, depth)}
<script src="{js}" defer></script>
</body></html>"""

def nav_html(depth=0):
    return rewrite_partial(NAV, depth)

# Path prefix for assets
def A(depth=0):
    return ("../" * depth) + "assets/"
