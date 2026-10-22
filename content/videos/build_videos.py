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
PLANNER = ROOT / "products/money-planner/listing_cover.png"
BUNDLE = ROOT / "products/bundle/listing_cover.png"

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

VIDEOS += [
    # ---- Week 2: the tracker ----
    ("day08_where_money_went", [
        ("hook", "I thought my side hustle was making money", 2.8),
        ("beat", "Then I tracked the fees, the gas and the supplies.", 2.8),
        ("beat", "Real profit was way less.", 2.2),
        ("beat", "Now every number goes in one sheet that does the math for me.", 3.2),
    ], TRACKER, "Side Hustle Profit Tracker (Excel + Google Sheets)"),
    ("day09_flip_roi", [
        ("hook", "Which flips are actually worth it?", 2.6),
        ("quote", "Example: bought $25 + $18 paint, sold $125", 3.2),
        ("list", "Profit: $82\nROI: 191%\nSold in: 9 days", 3.2),
        ("beat", "The tracker works it out the second you type the sold price.", 3.0),
    ], TRACKER, "Flip tracker included in the Profit Tracker"),
    ("day10_subscription_audit", [
        ("hook", "Add up your subscriptions. I'll wait.", 2.6),
        ("beat", "List every recurring charge.", 2.2),
        ("beat", "See what each one costs per YEAR.", 2.4),
        ("beat", "Mark the ones you don't use. Cancel them today.", 2.8),
        ("beat", "Do this once a month.", 2.0),
    ], TRACKER, "Subscription audit in the Profit Tracker"),
    ("day11_tax_set_aside", [
        ("hook", "Your side hustle money isn't all yours", 2.6),
        ("beat", "Side hustle income is taxable.", 2.2),
        ("beat", "Move a set % of profit into savings every month.", 2.8),
        ("beat", "No surprise bill in April.", 2.2),
        ("beat", "Not tax advice. Ask a tax pro what % fits you.", 2.8),
    ], TRACKER, "Monthly tax set-aside in the Profit Tracker"),
    ("day12_mileage", [
        ("hook", "Driving for your hustle? Log every mile.", 2.6),
        ("beat", "Pickups. Post office. Deliveries. Supply runs.", 2.8),
        ("beat", "Write down the odometer before and after.", 2.6),
        ("beat", "Business miles may be deductible. Ask a tax pro what you can claim.", 3.4),
    ], TRACKER, "Mileage log in the Profit Tracker"),
    ("day13_google_sheets", [
        ("hook", "Track your hustle from your phone. Free.", 2.6),
        ("beat", "Upload the tracker to Google Drive once.", 2.4),
        ("beat", "Open it in Google Sheets on your phone.", 2.4),
        ("beat", "Log a sale in the parking lot, right after pickup.", 2.8),
    ], TRACKER, "Works in Excel and Google Sheets"),
    ("day14_sunday_routine", [
        ("hook", "My 10-minute Sunday money routine", 2.6),
        ("list", "1. Log income\n2. Log expenses\n3. Mark sold flips\n4. Check the dashboard\n5. Move the tax money", 4.4),
        ("beat", "10 minutes. Every week. That's it.", 2.4),
    ], TRACKER, "Side Hustle Profit Tracker"),
    # ---- Week 3: flipping habits ----
    ("day15_start_with_zero", [
        ("hook", "No money to start flipping? Start here.", 2.6),
        ("beat", "Walk around your house.", 2.0),
        ("beat", "Find 10 things you don't use.", 2.2),
        ("beat", "List them tonight with good photos and a real title.", 2.8),
        ("beat", "That money buys your first flip.", 2.4),
    ], KIT, "25 listing templates in the Flipper Kit"),
    ("day16_relist_rules", [
        ("hook", "It didn't sell. Here's what to change.", 2.6),
        ("beat", "No messages in 3 days → new first photo.", 2.8),
        ("beat", "No sale in 7 days → drop 10% and renew.", 2.8),
        ("beat", "Most items move after one fix.", 2.4),
    ], KIT, "Relist rules in the Flipper Kit"),
    ("day17_no_show", [
        ("hook", "Buyer didn't show? Send this.", 2.4),
        ("quote", "\"No worries! I'm offering it to the next person. Message me if you still want it.\"", 4.2),
        ("beat", "Then message the next person in line. Don't wait around.", 3.0),
    ], KIT, "30 buyer scripts in the Flipper Kit"),
    ("day18_safe_meetups", [
        ("hook", "Where to meet every Marketplace buyer", 2.6),
        ("beat", "A police station safe exchange zone, or a busy parking lot.", 3.0),
        ("beat", "Daylight.", 1.6),
        ("beat", "Big items stay on the porch. Someone home with you.", 2.8),
        ("beat", "Trust your gut. Cancel if it feels off.", 2.4),
    ], KIT, "Safe meetup rules in the Flipper Kit"),
    ("day19_garage_sales", [
        ("hook", "Go to garage sales twice", 2.2),
        ("beat", "Early: the best stuff.", 2.0),
        ("beat", "Late: the best prices.", 2.0),
        ("quote", "\"What do you want for this whole table?\"", 3.0),
        ("beat", "They don't want to carry it back inside.", 2.4),
    ], KIT, "Full sourcing guide in the Flipper Kit"),
    ("day20_what_to_avoid", [
        ("hook", "Don't flip these", 2.0),
        ("list", "• Recalled items (check cpsc.gov)\n• Car seats\n• Stained mattresses\n• Fake brand-name stuff\n• Anything you can't test", 4.6),
        ("beat", "Not worth the risk.", 2.0),
    ], KIT, "What to avoid: in the Flipper Kit"),
    ("day21_hold_request", [
        ("hook", "\"Can you hold it for me?\"", 2.4),
        ("quote", "\"I don't hold items without a pickup time, sorry! When could you come?\"", 4.0),
        ("beat", "No time = no hold. The first person to show up gets it.", 2.8),
    ], KIT, "30 buyer scripts in the Flipper Kit"),
    # ---- Week 4: money habits + selling ----
    ("day22_budget_3_numbers", [
        ("hook", "Your whole budget is 3 numbers", 2.4),
        ("list", "1. What came in\n2. What went out\n3. What's left", 3.4),
        ("beat", "Know these every week and you're ahead of most people.", 3.0),
    ], PLANNER, "Hustle Money Planner ($4.99 printable)"),
    ("day23_fees_eat_profit", [
        ("hook", "That $50 sale wasn't $50", 2.4),
        ("beat", "Platform fees. Shipping. Gas to get there.", 2.6),
        ("beat", "Log gross and fees separately.", 2.4),
        ("beat", "Then you'll see what you really keep.", 2.4),
    ], TRACKER, "Side Hustle Profit Tracker"),
    ("day24_money_tied_up", [
        ("hook", "Unsold stuff is cash you can't use", 2.6),
        ("beat", "Add up what you paid for everything still in your garage.", 3.0),
        ("beat", "That's money tied up.", 2.0),
        ("beat", "Sell before you buy more.", 2.2),
    ], TRACKER, "Profit Tracker shows money tied up"),
    ("day25_monthly_goal", [
        ("hook", "Set a monthly profit goal. Watch it.", 2.6),
        ("beat", "Pick one number for the month.", 2.2),
        ("beat", "Check your progress every Sunday.", 2.4),
        ("beat", "A goal you can see is a goal you hit.", 2.4),
    ], TRACKER, "Goal tracking in the Profit Tracker"),
    ("day26_bundle", [
        ("hook", "Everything to flip and track your money, in one download", 3.0),
        ("list", "• Flipper Kit: templates + scripts\n• Profit Tracker: auto math\n• Money Planner: budget", 4.0),
        ("beat", "All 3 for $24.", 2.2),
    ], BUNDLE, "Side Hustle Money Kit: all 3 for $24"),
    ("day27_fill_in_template", [
        ("hook", "List any item in under 2 minutes", 2.6),
        ("list", "1. Take 8 photos\n2. Paste the template\n3. Fill in the [brackets]\n4. Post", 3.8),
        ("beat", "No staring at a blank box.", 2.2),
    ], KIT, "25 listing templates in the Flipper Kit"),
    ("day28_haggle_at_pickup", [
        ("hook", "They tried to haggle at pickup", 2.4),
        ("quote", "\"We agreed on $___ in messages. That's the price. If it doesn't work, no problem.\"", 4.2),
        ("beat", "Say it calmly. Then stop talking.", 2.4),
    ], KIT, "30 buyer scripts in the Flipper Kit"),
    ("day29_fake_payment_email", [
        ("hook", "Got a \"payment pending\" email from a buyer?", 2.8),
        ("beat", "Payment apps don't email you to \"unlock\" money.", 2.8),
        ("beat", "Only trust your actual app balance.", 2.4),
        ("beat", "No money in the app = no item.", 2.4),
    ], KIT, "Scam red flags in the Flipper Kit"),
    ("day30_price_drop_message", [
        ("hook", "Lowered your price? Send this.", 2.4),
        ("quote", "\"Hi! You asked about the ___ earlier. I dropped it to $___. Still interested?\"", 4.0),
        ("beat", "The people who asked before are your warmest buyers.", 2.8),
    ], KIT, "30 buyer scripts in the Flipper Kit"),
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
    c = Image.open(cover).convert("RGB")
    c.thumbnail((size, size))  # keep aspect ratio (the planner cover is portrait)
    y = 360 + int((1 - e) * 80)
    im.paste(c, ((W - c.width) // 2 - 40, y + (size - c.height) // 2))
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
