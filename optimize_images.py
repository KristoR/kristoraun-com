#!/usr/bin/env python3
"""Resize photos, convert them to WebP and print figure markup.

    python optimize_images.py photo.jpg "Caption"
"""
import sys
import pathlib
from PIL import Image, ImageOps

MAX_WIDTH = 1400
QUALITY = 82
OUT_DIR = pathlib.Path("content/images")


def optimise(src_path: str, caption: str | None = None) -> None:
    src = pathlib.Path(src_path)
    if not src.exists():
        print(f"skip (not found): {src}")
        return

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img = Image.open(src)

    # Rotate as the camera intended. EXIF, location included, is not saved.
    img = ImageOps.exif_transpose(img)
    if img.mode != "RGB":
        img = img.convert("RGB")

    w, h = img.size
    if w > MAX_WIDTH:
        h = round(h * MAX_WIDTH / w)
        w = MAX_WIDTH
        img = img.resize((w, h), Image.LANCZOS)

    out = OUT_DIR / (src.stem + ".webp")
    img.save(out, "WEBP", quality=QUALITY, method=6)

    before = src.stat().st_size / 1024
    after = out.stat().st_size / 1024
    print(f"  {src.name}: {before:.0f} KB -> {after:.0f} KB  ({w}x{h})  ->  {out}")

    rel = f"{{static}}/images/{out.name}"
    alt = caption or src.stem.replace("-", " ")
    print("\n  Paste into the post:\n")
    print(f'  <figure>')
    print(f'    <img src="{rel}" alt="{alt}" width="{w}" height="{h}" loading="lazy">')
    if caption:
        print(f"    <figcaption>{caption}</figcaption>")
    print(f"  </figure>\n")


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    args = sys.argv[1:]
    caption = None
    if len(args) >= 2 and not pathlib.Path(args[-1]).exists():
        caption = args[-1]
        args = args[:-1]
    for path in args:
        optimise(path, caption)


if __name__ == "__main__":
    main()
