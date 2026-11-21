#!/usr/bin/env python3
"""Build entry.png for the-catalogue-photo-of-an-impossible-gadget.

Loads the photorealistic SPOONBENDER base image, resizes it to 1024x1024,
and prints the brand name on the machine's flat front panel, centred on
the panel so it reads as printed on the product.
Deterministic: same input -> same output bytes.
"""
import hashlib
import os

from PIL import Image, ImageDraw, ImageFont

BASE = "media-generation-spoon-bender-base-v2-0-019e742d-6169-4d14-87b2-b46abbd8c968.png"
OUT = "entry.png"
SIZE = 1024
BRAND = "SPOONBENDER"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
# Front panel of the machine, as fractions of the 1024x1024 canvas.
PANEL_LEFT = 0.339
PANEL_RIGHT = 0.684
PANEL_TOP = 0.404
PANEL_BOTTOM = 0.814
INK = (38, 56, 76)  # dark slate navy


def letterspaced_width(draw, font, text, tracking):
    widths = [draw.textlength(ch, font=font) for ch in text]
    return sum(widths) + tracking * (len(text) - 1)


def draw_letterspaced(draw, centre_x, centre_y, font, text, tracking, fill):
    widths = [draw.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = centre_x - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, centre_y), ch, font=font, fill=fill, anchor="lm")
        x += w + tracking


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    img = Image.open(os.path.join(here, BASE)).convert("RGB")
    if img.size != (SIZE, SIZE):
        img = img.resize((SIZE, SIZE), Image.LANCZOS)
    draw = ImageDraw.Draw(img)
    panel_cx = (PANEL_LEFT + PANEL_RIGHT) / 2 * SIZE
    panel_cy = (PANEL_TOP + PANEL_BOTTOM) / 2 * SIZE
    # Fit the brand inside the panel with a margin.
    max_w = (PANEL_RIGHT - PANEL_LEFT) * SIZE * 0.88
    size = 40
    while size > 10:
        font = ImageFont.truetype(FONT_PATH, size)
        tracking = max(2, int(size * 0.22))
        if letterspaced_width(draw, font, BRAND, tracking) <= max_w:
            break
        size -= 1
    font = ImageFont.truetype(FONT_PATH, size)
    tracking = max(2, int(size * 0.22))
    draw_letterspaced(draw, panel_cx, panel_cy, font, BRAND, tracking, INK)
    img.save(os.path.join(here, OUT), format="PNG")
    with open(os.path.join(here, OUT), "rb") as f:
        data = f.read()
    print(
        f"entry.png: {img.size[0]}x{img.size[1]}, "
        f"{len(data)} bytes, sha256 {hashlib.sha256(data).hexdigest()}"
    )


if __name__ == "__main__":
    main()
