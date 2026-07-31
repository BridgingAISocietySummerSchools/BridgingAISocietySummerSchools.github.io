#!/usr/bin/env python3
"""Regenerate the raster brand assets from the mark in _includes/bas-mark.html.

Favicons, manifest icons, the social card and the schema.org logo can't read
CSS, so they are baked here from the same geometry, on a fixed opaque light
tile matching the manifest's theme_color / background_color.

    python3 tools/build-brand-assets.py

Requires rsvg-convert (brew install librsvg) and Pillow.
"""
import io
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FAVICON_DIR = ROOT / "assets" / "favicon"
IMG_DIR = ROOT / "assets" / "img"

# The light skin's values. Keep in step with the contrast skin and
# $bas-brand-red in _sass/_bas-theme.scss.
GROUND = "#ffffff"  # $background-color
INK = "#000000"  # $text-color, i.e. --bas-heading
ACCENT = "#b60000"  # $bas-brand-red
MUTED = "#4d4d4d"  # --bas-muted: mix($background-color, $text-color, 30%)

# Two optical cuts of the same drawing; the small one thickens the bars below
# roughly 28px, where the corner gaps otherwise close.
DISPLAY = dict(x=16, y=41.5, w=32, h=11, rx=5.5)
SMALL = dict(x=15, y=41, w=34, h=12, rx=6)


def bars(cut, ink=INK, accent=ACCENT):
    """The three bars of the mark, on a 0 0 64 64 viewBox."""
    return "".join(
        '<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
        'fill="{fill}" transform="rotate({angle} 32 32)"/>'.format(
            fill=accent if i == 2 else ink, angle=i * 120, **cut)
        for i in range(3))


def mark_svg(px, *, tile="rounded", scale=0.78, cut=None):
    """A square icon: the mark centred on a ground tile.

    tile="rounded" for tab and bookmark contexts, "square" for maskable icons
    and the Apple touch icon, where the platform applies its own mask.
    """
    cut = cut or (SMALL if px < 48 else DISPLAY)
    radius = 14 if tile == "rounded" else 0
    inner = bars(cut)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{px}" height="{px}" '
        f'viewBox="0 0 64 64">'
        f'<rect width="64" height="64" rx="{radius}" fill="{GROUND}"/>'
        f'<g transform="translate(32 32) scale({scale}) translate(-32 -32)">{inner}</g>'
        f'</svg>')


def og_svg():
    """1200x630 social card. Text is baked, so it needs a real font here."""
    face = "Helvetica Neue, Helvetica, Arial, sans-serif"
    mark = bars(DISPLAY)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630"
     viewBox="0 0 1200 630" font-family="{face}">
  <rect width="1200" height="630" fill="{GROUND}"/>
  <g transform="translate(96 142) scale(1.5)">{mark}</g>
  <text x="96" y="316" font-size="66" font-weight="700" fill="{INK}"
        letter-spacing="-2">Bridging AI <tspan fill="{ACCENT}">&amp;</tspan> Society</text>
  <rect x="96" y="360" width="72" height="7" rx="3.5" fill="{ACCENT}"/>
  <text x="96" y="436" font-size="32" fill="{MUTED}">Interdisciplinary machine learning education</text>
  <text x="96" y="482" font-size="32" fill="{MUTED}">Dr. Christoph Weisser &amp; Dr. Knut Zoch</text>
</svg>'''


def render(svg, out_path):
    """SVG source -> PNG on disk, via rsvg-convert."""
    png = subprocess.run(
        ["rsvg-convert", "-o", str(out_path)],
        input=svg.encode(), check=True, capture_output=True)
    if png.stderr:
        print(png.stderr.decode(), file=sys.stderr)
    return out_path


def main():
    from PIL import Image

    FAVICON_DIR.mkdir(parents=True, exist_ok=True)
    written = []

    svg_path = FAVICON_DIR / "favicon.svg"
    svg_path.write_text(mark_svg(64, tile="rounded", cut=SMALL) + "\n")
    written.append(svg_path)

    written.append(render(mark_svg(96), FAVICON_DIR / "favicon-96x96.png"))
    written.append(render(mark_svg(180, tile="square", scale=0.66),
                          FAVICON_DIR / "apple-touch-icon.png"))

    # Maskable icons: full-bleed, mark held inside the centre 80% safe zone so
    # a circular mask can't clip it.
    for px in (192, 512):
        written.append(render(mark_svg(px, tile="square", scale=0.55),
                              FAVICON_DIR / f"web-app-manifest-{px}x{px}.png"))

    # "any" icon for contexts that apply no mask, so they get the corner
    # radius. Doubles as the schema.org Organization logo (_includes/schema.html).
    written.append(render(mark_svg(512),
                          FAVICON_DIR / "web-app-icon-512x512.png"))

    written.append(render(og_svg(), IMG_DIR / "og-card.png"))

    # Multi-resolution .ico, each size rendered from its own optical cut
    # rather than downsampled from one bitmap.
    frames = []
    for px in (16, 32, 48):
        buf = io.BytesIO(
            subprocess.run(["rsvg-convert"], input=mark_svg(px).encode(),
                           check=True, capture_output=True).stdout)
        frames.append(Image.open(buf).convert("RGBA"))
    ico_path = FAVICON_DIR / "favicon.ico"
    frames[0].save(ico_path, format="ICO",
                   sizes=[(f.width, f.height) for f in frames],
                   append_images=frames[1:])
    written.append(ico_path)

    for p in written:
        print(f"{p.relative_to(ROOT)}  {p.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
