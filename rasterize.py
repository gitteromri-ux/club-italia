#!/usr/bin/env python3
"""Rasterize each SVG to a sibling PNG using cairosvg."""
import os, glob
import cairosvg

SRC = "/home/user/workspace/club-italia/assets/img"
targets = [
    "zoom-mockup.svg", "zoom-mockup-2.svg", "dashboard-mockup.svg",
    "certificate-mockup.svg", "checkout-mockup.svg",
    "screen-placement.svg", "screen-platform.svg", "screen-liveclass.svg",
    "screen-biagio.svg", "screen-certificate.svg",
    "trustpilot-logo.svg", "cefr-logo.svg", "eteacher-logo.svg",
    "guarantee-badge.svg", "paymethods.svg", "tricolor-rule.svg",
]

for name in targets:
    src = os.path.join(SRC, name)
    dst = os.path.join(SRC, name.replace(".svg", ".png"))
    try:
        cairosvg.svg2png(url=src, write_to=dst, output_width=None)
        size = os.path.getsize(dst)
        print(f"OK  {dst} ({size} bytes)")
    except Exception as e:
        print(f"ERR {name}: {e}")
