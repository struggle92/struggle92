"""Render each post in posts.py to a 1080x1350 card (cards/dayNN.png) and write queue.json.
Run: python3 build_posts.py   (needs Pillow). Keeps the 'scheduled' flags already in queue.json."""
import json
import os
from PIL import Image, ImageDraw, ImageFont

from posts import POSTS, NAMES, PRICES, SHOP, caption

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, PAD = 1080, 1350, 90
BG, INK, MUTED, ACCENT, GOOD = "#131a2a", "#f6f7f9", "#9aa4ba", "#ff7a33", "#4cc38a"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def wrap(draw, text, font, width):
    lines, line = [], ""
    for word in text.split():
        test = f"{line} {word}".strip()
        if draw.textlength(test, font=font) <= width:
            line = test
        else:
            lines.append(line)
            line = word
    return lines + [line]


def card(day, post, path):
    hook, points, _, product = post
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for x in range(-H, W, 46):  # faint diagonal texture
        d.line([(x, H), (x + H * 0.47, 0)], fill="#18203a", width=2)

    d.text((PAD, PAD), f"DAY {day:02d} / 30", font=ImageFont.truetype(FONT_MONO, 30), fill=ACCENT)

    size = 84
    while True:  # shrink the hook until it fits in 4 lines
        f_hook = ImageFont.truetype(FONT_BOLD, size)
        lines = wrap(d, hook, f_hook, W - 2 * PAD)
        if len(lines) <= 4 or size <= 56:
            break
        size -= 6
    y = PAD + 80
    for ln in lines:
        d.text((PAD, y), ln, font=f_hook, fill=INK)
        y += int(size * 1.18)

    y += 50
    f_pt = ImageFont.truetype(FONT, 50)
    for p in points:
        d.ellipse([PAD, y + 16, PAD + 30, y + 46], outline=GOOD, width=5)
        for i, ln in enumerate(wrap(d, p, f_pt, W - 2 * PAD - 56)):
            d.text((PAD + 56, y), ln, font=f_pt, fill=INK)
            y += 66
        y += 34

    d.rectangle([0, H - 170, W, H], fill=ACCENT)
    d.text((PAD, H - 140), f"{NAMES[product]}  ·  {PRICES[product]}", font=ImageFont.truetype(FONT_BOLD, 38), fill=BG)
    d.text((PAD, H - 86), SHOP, font=ImageFont.truetype(FONT_MONO, 34), fill=BG)
    img.save(path, optimize=True)


def main():
    os.makedirs(os.path.join(HERE, "cards"), exist_ok=True)
    qpath = os.path.join(HERE, "queue.json")
    old = {}
    if os.path.exists(qpath):
        old = {p["day"]: p for p in json.load(open(qpath))}
    queue = []
    for day, post in enumerate(POSTS, 1):
        name = f"cards/day{day:02d}.png"
        card(day, post, os.path.join(HERE, name))
        queue.append({
            "day": day,
            "image": f"https://{SHOP}/content/{name}",
            "hook": post[0],
            "caption": caption(post),
            "product": post[3],
            "scheduled": old.get(day, {}).get("scheduled", False),
        })
    json.dump(queue, open(qpath, "w"), indent=2)
    print(f"{len(queue)} posts -> cards/, queue.json")


if __name__ == "__main__":
    main()
