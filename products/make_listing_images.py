"""Square 2000x2000 store images for the tracker, flipper kit and bundle."""
import subprocess, tempfile, glob, os
from PIL import Image, ImageDraw, ImageFont

SAGE, GOLD, INK, LT = (94, 140, 122), (217, 164, 65), (31, 42, 46), (230, 239, 235)
B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
f = lambda p, s: ImageFont.truetype(p, s)


def thumbs(pdf, pages, width):
    d = tempfile.mkdtemp()
    out = []
    for p in pages:
        subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "80", "-png", pdf, f"{d}/p{p}"], check=True)
        im = Image.open(glob.glob(f"{d}/p{p}*.png")[0]).convert("RGB")
        out.append(im.resize((width, int(im.height * width / im.width))))
    return out


def base(kicker, title_lines, sub):
    im = Image.new("RGB", (2000, 2000), SAGE)
    d = ImageDraw.Draw(im)
    d.text((120, 120), kicker, font=f(B, 46), fill=(255, 255, 255))
    y = 210
    for t in title_lines:
        d.text((120, y), t, font=f(B, 132), fill=(255, 255, 255))
        y += 150
    d.rectangle([120, y + 20, 360, y + 34], fill=GOLD)
    d.text((120, y + 70), sub, font=f(R, 52), fill=(255, 255, 255))
    return im, d, y + 170


def bullets(d, items, x, y, size=50, color=(255, 255, 255)):
    for it in items:
        d.text((x, y), "✓", font=f(B, size), fill=GOLD)
        d.text((x + 75, y), it, font=f(R, size), fill=color)
        y += int(size * 1.6)
    return y


def badge(d, text):
    d.rounded_rectangle([1420, 1740, 1880, 1880], 30, fill=GOLD)
    w = d.textlength(text, font=f(B, 58))
    d.text((1650 - w / 2, 1775), text, font=f(B, 58), fill=INK)


# --- Tracker ---
im, d, y = base("EXCEL + GOOGLE SHEETS", ["Side Hustle", "Profit Tracker"], "Know exactly what you made. Automatically.")
# mini dashboard mock drawn from the template's real layout
x0, y0, w, h = 120, y + 10, 1760, 900
d.rounded_rectangle([x0, y0, x0 + w, y0 + h], 30, fill=(255, 255, 255))
cards = [("PROFIT THIS YEAR", "$4,812"), ("SET ASIDE FOR TAXES", "$1,203"), ("SUBSCRIPTIONS / MO", "$86"), ("AVG FLIP ROI", "164%")]
cw = (w - 100) / 4
for i, (k, v) in enumerate(cards):
    cx = x0 + 40 + i * (cw + 7)
    d.rounded_rectangle([cx, y0 + 40, cx + cw - 20, y0 + 230], 18, fill=LT)
    d.text((cx + 25, y0 + 65), k, font=f(B, 28), fill=(107, 122, 128))
    d.text((cx + 25, y0 + 125), v, font=f(B, 72), fill=INK)
vals = [180, 260, 240, 390, 420, 510, 470, 600, 560, 650, 610, 720]
bw = (w - 160) / 12
base_y = y0 + h - 80
for i, v in enumerate(vals):
    bx = x0 + 80 + i * bw
    d.rounded_rectangle([bx + 12, base_y - v * 0.72, bx + bw - 12, base_y], 10, fill=SAGE if i < 11 else GOLD)
    d.text((bx + bw / 2 - 18, base_y + 15), "JFMAMJJASOND"[i], font=f(B, 34), fill=(107, 122, 128))
d.text((120, 1900), "Example numbers shown. Instant download. Not tax advice.", font=f(R, 34), fill=(225, 235, 230))
badge(d, "INSTANT")
im.save("profit-tracker/listing_cover.png")

im, d, y = base("WHAT'S INSIDE", ["8 Tabs.", "Zero Math."], "Type it in. Everything else fills itself in.")
bullets(d, ["Dashboard: monthly profit, goal progress, YTD",
            "Income log with platform fees",
            "Expense log (business vs personal)",
            "Flip tracker: profit, ROI, days to sell",
            "Subscription audit: find forgotten charges",
            "Mileage log with deduction math",
            "Tax set-aside estimate every month",
            "Dropdowns + step-by-step Start Here tab"], 120, y + 20, 52)
im.save("profit-tracker/listing_inside.png")

# --- Flipper kit ---
pdf = "flipper-kit/Marketplace_Flipper_Kit.pdf"
im, d, y = base("FACEBOOK MARKETPLACE • OFFERUP", ["Marketplace", "Flipper Kit"], "Find it cheap. List it right. Sell it fast.")
ts = thumbs(pdf, [4, 6, 9], 540)
for i, t in enumerate(ts):
    t = t.crop((0, 0, t.width, min(t.height, 700)))
    im.paste(t, (120 + i * 600, y + 40))
d.text((120, y + 790), "25 listing templates  •  30 buyer scripts  •  scam guide", font=f(B, 50), fill=(255, 255, 255))
badge(d, "14 PAGES")
im.save("flipper-kit/listing_cover.png")

# --- Bundle ---
im, d, y = base("3-IN-1 BUNDLE  •  SAVE $10", ["Side Hustle", "Money Kit"], "Everything to start flipping and track every dollar.")
y = bullets(d, ["Side Hustle Profit Tracker (spreadsheet)",
                "Marketplace Flipper Kit (14-page PDF)",
                "Hustle Money Planner (16-page printable)"], 120, y + 20, 58)
ts = thumbs(pdf, [1], 420) + thumbs("money-planner/Hustle_Money_Planner.pdf", [1], 420)
for i, t in enumerate(ts):
    im.paste(t.crop((0, 0, 420, min(t.height, 560))), (120 + i * 470, y + 40))
tr = Image.open("profit-tracker/listing_cover.png").resize((560, 560))
im.paste(tr, (1080, y + 40))
badge(d, "$24")
im.save("bundle/listing_cover.png")
print("done")
