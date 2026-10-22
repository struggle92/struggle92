"""Renders faceless text Shorts (1080x1920, 30fps MP4) from the scripts in ../shorts_scripts.md.

Each video: hook slide, 3-5 beat slides, end card with the product cover. Text stays inside the
platform safe zone (clear of the top bar, the caption/buttons area at the bottom and the right rail).
Run: python3 build_videos.py   (needs ffmpeg and Pillow)
"""
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
W, H, FPS = 1080, 1920, 30
SAGE, SAGE_DK, GOLD, INK, CREAM = (94, 140, 122), (62, 99, 85), (217, 164, 65), (31, 42, 46), (246, 243, 236)
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SAFE_L, SAFE_R, SAFE_T, SAFE_B = 90, W - 170, 300, H - 480  # text box inside safe zone

KIT = ROOT / "products/flipper-kit/listing_cover.png"
TRACKER = ROOT / "products/profit-tracker/listing_cover.png"

# (file, slides[(kind, text, seconds)], end-card product, end-card line)
VIDEOS = [
    ("day01_is_this_available", [
        ("hook", "Stop replying \"yes\" to \"Is this still available?\"", 2.8),
        ("beat", "Just \"yes\" gets you ghosted.", 2.4),
        ("beat", "Answer + a pickup time. Every time.", 2.6),
        ("quote", "\"Yes, it's available! I can do pickup today after 5. What time works?\"", 4.2),
        ("beat", "Now they have to commit to a time.", 2.6),
    ], KIT, "30 buyer scripts in the Flipper Kit"),
    ("day02_3x_rule", [
        ("hook", "Never pay more than THIS for a flip", 2.6),
        ("beat", "1. Look up what it actually sells for", 2.6),
        ("beat", "2. Divide by 3", 2.0),
        ("beat", "3. That's your max price. Repairs included.", 2.8),
        ("quote", "Sells for $150 → pay $50 max, all in.", 3.4),
    ], KIT, "Profit Check + math table in the Flipper Kit"),
    ("day03_lowball_reply", [
        ("hook", "How to answer a lowballer without losing the sale", 3.0),
        ("beat", "Don't get mad. Counter.", 2.2),
        ("quote", "\"Thanks for the offer! I can't go that low. Lowest I can do is $___.\"", 4.2),
        ("beat", "Polite. Firm. They often say yes.", 2.6),
    ], KIT, "30 buyer scripts in the Flipper Kit"),
    ("day04_8_photos", [
        ("hook", "Your photos are why it's not selling", 2.6),
        ("list", "1. Hero shot, daylight\n2. 45° angle\n3. Brand label\n4. Item working", 3.8),
        ("list", "5. Tape measure for size\n6. Details & extras\n7. Every flaw\n8. Everything together", 3.8),
        ("beat", "8 photos. Fewer questions. Faster sales.", 2.6),
    ], KIT, "Photo checklist in the Flipper Kit"),
    ("day05_title_formula", [
        ("hook", "Nobody searches for \"Dresser\"", 2.4),
        ("beat", "Brand + Item + Key feature + Condition", 3.0),
        ("quote", "\"Solid Wood 6-Drawer Dresser – Refinished Matte Black, New Hardware\"", 4.0),
        ("beat", "More words buyers search = more views.", 2.6),
    ], KIT, "25 listing templates in the Flipper Kit"),
    ("day06_free_section", [
        ("hook", "My best flips cost $0", 2.4),
        ("beat", "Check the Marketplace Free section every day", 2.8),
        ("beat", "End of the month = people moving out", 2.6),
        ("beat", "Clean it. Photograph it. List it.", 2.6),
        ("beat", "Zero dollars in.", 2.0),
    ], KIT, "Full sourcing guide in the Flipper Kit"),
    ("day07_code_scam", [
        ("hook", "If a buyer asks for a code, block them", 2.8),
        ("quote", "\"Send me the code so I know you're real.\"", 3.2),
        ("beat", "That code can set up a phone number in YOUR name.", 3.2),
        ("beat", "Never send any code to a buyer. Ever.", 2.8),
        ("beat", "Share this with someone who sells online.", 2.6),
    ], KIT, "Scam red flags + safe meetups in the Flipper Kit"),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, width):
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for w in words:
            t = (cur + " " + w).strip()
            if d.textlength(t, font=f) <= width:
                cur = t
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def fit(d, text, kind):
    """Largest font size whose wrapped text fits the safe box."""
    path = REG if kind == "list" else BOLD
    for size in range(104 if kind == "hook" else 86, 40, -2):
        f = font(path, size)
        lines = wrap(d, text, f, SAFE_R - SAFE_L)
        lh = int(size * 1.28)
        if lh * len(lines) <= (SAFE_B - SAFE_T) * 0.8:
            return f, lines, lh
    return f, lines, lh


def base(bg):
    im = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(im)
    d.rectangle([0, H - 14, W, H], fill=GOLD)
    return im, d


def slide_frame(kind, text, t, idx, total):
    """t: 0..1 progress through the slide's entrance (clamped)."""
    bg = SAGE_DK if kind == "hook" else SAGE
    im, d = base(bg)
    # progress dots
    for i in range(total):
        x = SAFE_L + i * 34
        d.ellipse([x, 220, x + 18, 238], fill=GOLD if i <= idx else (255, 255, 255, 90) if False else (170, 196, 186))
    f, lines, lh = fit(d, text, kind)
    block = lh * len(lines)
    y0 = SAFE_T + (SAFE_B - SAFE_T - block) // 2
    e = 1 - (1 - min(1, t)) ** 3  # ease-out
    rise = int((1 - e) * 60)
    alpha = int(255 * e)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    if kind == "quote":
        pad = 46
        ld.rounded_rectangle([SAFE_L - pad, y0 - pad + rise, SAFE_R + pad - 40, y0 + block + pad + rise],
                             36, fill=CREAM + (alpha,))
        color = INK
    else:
        color = (255, 255, 255)
    for i, ln in enumerate(lines):
        ld.text((SAFE_L, y0 + i * lh + rise), ln, font=f, fill=color + (alpha,))
    if kind == "hook":
        ld.rectangle([SAFE_L, y0 + block + 30 + rise, SAFE_L + 220, y0 + block + 44 + rise], fill=GOLD + (alpha,))
    im.paste(layer, (0, 0), layer)
    return im


def end_frame(cover, line, t):
    im, d = base(SAGE_DK)
    e = 1 - (1 - min(1, t)) ** 3
    size = 760
    c = Image.open(cover).convert("RGB").resize((size, size))
    y = 360 + int((1 - e) * 80)
    im.paste(c, ((W - size) // 2 - 40, y))
    f = font(BOLD, 58)
    for i, ln in enumerate(wrap(d, line, f, SAFE_R - SAFE_L)):
        d.text((SAFE_L, y + size + 60 + i * 74), ln, font=f, fill=(255, 255, 255))
    d.text((SAFE_L, y + size + 230), "Link in bio", font=font(BOLD, 70), fill=GOLD)
    return im


def render(name, slides, cover, line):
    out = HERE / f"{name}.mp4"
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
           "-r", str(FPS), "-i", "-", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
           "-shortest", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(out)]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    total = len(slides)
    for idx, (kind, text, secs) in enumerate(slides):
        n = int(secs * FPS)
        cache = None
        for k in range(n):
            t = k / (0.45 * FPS)
            if t >= 1 and cache is not None:
                p.stdin.write(cache)
                continue
            frame = slide_frame(kind, text, t, idx, total).tobytes()
            if t >= 1:
                cache = frame
            p.stdin.write(frame)
    cache = None
    for k in range(int(3.2 * FPS)):
        t = k / (0.45 * FPS)
        if t >= 1 and cache is not None:
            p.stdin.write(cache)
            continue
        frame = end_frame(cover, line, t).tobytes()
        if t >= 1:
            cache = frame
        p.stdin.write(frame)
    p.stdin.close()
    p.wait()
    return out


if __name__ == "__main__":
    import sys
    only = set(sys.argv[1:])
    for name, slides, cover, line in VIDEOS:
        if only and name not in only:
            continue
        print("rendered", render(name, slides, cover, line))
