"""Builds 'The No-Pick Night Routine + 30-Day Tracker' — a 5-page printable PDF (US Letter)."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

W, H = letter
M = 48
INK = HexColor("#2B2433")
ROSE = HexColor("#C98B9A")
ROSE_LT = HexColor("#F7ECEF")
PLUM = HexColor("#6E5A7E")
LINE = HexColor("#E2D3D8")
MUTED = HexColor("#7D7285")
TITLE = "The No-Pick Night Routine"
OUT = "No_Pick_Night_Routine.pdf"
c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle(TITLE + " + 30-Day Tracker")
c.setAuthor("QFS")
y = [0]
page = [0]


def header(title, sub):
    page[0] += 1
    c.setFillColor(ROSE)
    c.rect(0, H - 82, W, 82, fill=1, stroke=0)
    c.setFillColor(PLUM)
    c.rect(0, H - 86, W, 4, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 23)
    c.drawString(M, H - 48, title.upper())
    c.setFont("Helvetica", 10.5)
    c.drawString(M, H - 68, sub)
    y[0] = H - 116


def footer():
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 7.5)
    c.drawString(M, 24, "Cosmetic routine guide, not medical advice. For persistent, painful or cystic breakouts, see a dermatologist.")
    c.drawRightString(W - M, 24, str(page[0]))
    c.showPage()


def para(text, size=10.5, color=INK, bold=False, gap=6):
    font = "Helvetica-Bold" if bold else "Helvetica"
    for ln in simpleSplit(text, font, size, W - 2 * M):
        c.setFillColor(color)
        c.setFont(font, size)
        c.drawString(M, y[0], ln)
        y[0] -= size * 1.42
    y[0] -= gap


def h2(text):
    y[0] -= 2
    c.setFillColor(PLUM)
    c.setFont("Helvetica-Bold", 12.5)
    c.drawString(M, y[0], text.upper())
    y[0] -= 6
    c.setStrokeColor(ROSE)
    c.setLineWidth(1.5)
    c.line(M, y[0], M + 54, y[0])
    y[0] -= 16


def step(num, title, body):
    lines = simpleSplit(body, "Helvetica", 10, W - 2 * M - 90)
    h = 30 + len(lines) * 14
    top = y[0] + 10
    c.setFillColor(ROSE_LT)
    c.roundRect(M, top - h, W - 2 * M, h, 8, fill=1, stroke=0)
    c.setFillColor(ROSE)
    c.circle(M + 24, top - 22, 13, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(M + 24, top - 26, str(num))
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(M + 50, top - 20, title)
    c.setFont("Helvetica", 10)
    yy = top - 36
    for ln in lines:
        c.drawString(M + 50, yy, ln)
        yy -= 14
    c.setStrokeColor(PLUM)
    c.setLineWidth(1)
    c.rect(W - M - 26, top - 28, 13, 13, fill=0, stroke=1)
    y[0] = top - h - 8


def bullets(items, mark="•", color=None):
    for it in items:
        lines = simpleSplit(it, "Helvetica", 10.3, W - 2 * M - 16)
        c.setFillColor(color or ROSE)
        c.setFont("Helvetica-Bold", 10.3)
        c.drawString(M + 2, y[0], mark)
        c.setFillColor(INK)
        c.setFont("Helvetica", 10.3)
        for ln in lines:
            c.drawString(M + 16, y[0], ln)
            y[0] -= 14.5
        y[0] -= 3
    y[0] -= 4


# ---------- Page 1: Start here ----------
header("Start here", "The routine that goes with your patches. Print it, or fill it in on your phone.")
c.setFillColor(INK)
c.setFont("Helvetica-Bold", 30)
c.drawString(M, y[0] - 10, "The No-Pick")
c.drawString(M, y[0] - 46, "Night Routine")
c.setFont("Helvetica", 14)
c.setFillColor(PLUM)
c.drawString(M, y[0] - 74, "+ 30-Day Tracker")
y[0] -= 112
para("Picking turns a small spot into a bigger, longer-lasting mark. This guide gives you a short, gentle routine for "
     "every night, a 2-week plan to break the picking habit, and a tracker so you can see your streak grow.")
h2("What's inside")
bullets(["Page 2: The 5-minute night routine (check it off every night)",
         "Page 3: The 2-week no-picking plan: notice, block, replace, and the mirror rule",
         "Page 4: Pimple patch guide: when to use one, which size, how long, and when not to",
         "Page 5: Your 30-day tracker for routine, picking, patches, sleep and notes"])
h2("How to use it")
bullets(["Tonight: read page 3 and set up your 'block' (step 2 of the plan).",
         "Every night: do the routine on page 2, then fill in one row on page 5. It takes 10 seconds.",
         "Every Sunday: look at your week. Notice when and where picking happened, and adjust one thing.",
         "Be patient. Skin takes weeks to show changes. The goal for month one is the habit, not perfect skin."])
h2("Keep it gentle")
para("New products can irritate skin. Patch-test anything new on a small area first, change one thing at a time, "
     "and stop using anything that burns or stings badly. If you use a prescription, follow your prescriber's directions "
     "over anything in this guide.", size=10)
footer()

# ---------- Page 2: Night routine ----------
header("The 5-minute night routine", "Simple, gentle and boring in a good way. Check each step off.")
step(1, "Hands first", "Wash your hands with soap before you touch your face. Clean hands mean fewer germs on your skin.")
step(2, "Gentle cleanse", "Lukewarm water and a mild, fragrance-free cleanser. Massage for about 30 seconds with your fingertips. No scrubs, no rough washcloth.")
step(3, "Pat dry", "Use a clean towel and pat, don't rub. Swap face towels often, or use a fresh paper towel.")
step(4, "Treat (only if you use one)", "If you use an acne treatment, apply a thin layer as its label or your doctor directs. More doesn't work faster; it just irritates.")
step(5, "Moisturize", "A light, non-comedogenic (won't clog pores) moisturizer, even if your skin is oily. Skip it only where a patch is going.")
step(6, "Patch it", "Put a patch on any spot with a white head, or one you've already opened. Skin must be clean and dry so it sticks. See page 4.")
step(7, "Hands off, lights out", "Hair off your face, a clean pillowcase (swap it 1-2 times a week), and your phone out of reach so you're not mirror-checking in bed.")
y[0] -= 4
para("About 5 minutes. Do it even on tired nights. A short routine you actually do beats a long one you skip.",
     size=10, color=PLUM, bold=True)
footer()

# ---------- Page 3: 2-week plan ----------
header("The 2-week no-picking plan", "Picking is a habit loop. Break the loop, not yourself.")
h2("Step 1: Notice (days 1-3)")
para("Don't try to stop yet. Just track it. Every time you pick or catch yourself about to, mark it on your tracker and "
     "note where you were and how you felt: bored, stressed, tired, in front of a mirror? Most people find 1-2 main triggers.")
h2("Step 2: Block (days 4-7)")
bullets(["Put a patch on any spot you're tempted by. You can't pick what you can't touch.",
         "Cover or avoid the mirror you pick at most. Move any magnifying mirror out of the bathroom.",
         "Keep nails short and smooth.",
         "Use softer light at night. Harsh overhead light makes every pore look like a target."])
h2("Step 3: Replace (days 8-14)")
para("Your hands want something to do. Give them a substitute for the moment you'd normally pick:")
bullets(["Squeeze a stress ball, fidget toy or hair tie.",
         "Put on hand lotion, or a patch, instead.",
         "Leave the room for 2 minutes. The urge usually passes.",
         "Text a friend or start your next task."])
h2("The mirror rule")
para("Check your skin once a day, in normal light, at arm's length. If you're closer than that, you're inspecting, "
     "and inspecting leads to picking. Walk away.", bold=True)
h2("If you slip")
para("It happens. Wash your hands, gently clean the spot, put a patch on it and leave it alone. Mark it on the tracker "
     "and keep going. One slip doesn't erase your progress.")
footer()

# ---------- Page 4: Patch guide ----------
header("Pimple patch guide", "When to use them, which size, how long, and when not to.")
h2("When patches work best")
bullets(["Spots with a visible white head (surface spots).",
         "A spot that has already opened or that you've picked: the patch covers it and soaks up fluid while it heals.",
         "Any spot you keep touching. The patch is a physical barrier."])
h2("Which size")
para("Pick a patch that covers the whole spot with a small border of clear skin around it. Too small and the edges "
     "lift; much too big and it can peel off overnight.")
h2("How to apply")
bullets(["Clean and dry the skin first. No moisturizer, oil or treatment right under the patch, or it won't stick.",
         "Press it on with clean fingers and hold for a few seconds.",
         "Leave it on overnight, or about 6-8 hours."])
h2("How long and when to change")
bullets(["Change it when it turns white or cloudy. That means it has absorbed fluid.",
         "Peel it off slowly, starting at one edge. Don't rip it off.",
         "Use a fresh patch each time. Never reuse one."])
h2("When NOT to use a patch")
bullets(["Deep, hard, painful lumps under the skin with no head (cystic or nodular acne). Patches can't reach them; see a dermatologist.",
         "Skin that looks infected: spreading redness, warmth, swelling, or fever. See a doctor.",
         "Irritated, cracked or sunburned skin that isn't a pimple.",
         "If your skin reacts to the patch (itching, rash), stop using it."], mark="!", color=PLUM)
footer()

# ---------- Page 5: 30-day tracker ----------
header("30-day tracker", "One row a night. Check what you did. Be honest; this is just for you.")
cols = [("Day", 36), ("Routine", 56), ("Picked?", 60), ("Patches", 52), ("Sleep (hrs)", 66)]
cols.append(("Notes / trigger", W - 2 * M - sum(w for _, w in cols)))
top = y[0] + 14
rh = 19
c.setFillColor(INK)
c.rect(M, top - rh, W - 2 * M, rh, fill=1, stroke=0)
c.setFillColor(white)
c.setFont("Helvetica-Bold", 8.5)
xx = M
for name, w in cols:
    c.drawString(xx + 5, top - 13, name.upper())
    xx += w
c.setLineWidth(0.6)
yy = top - rh
for i in range(30):
    if i % 2 == 0:
        c.setFillColor(ROSE_LT)
        c.rect(M, yy - rh, W - 2 * M, rh, fill=1, stroke=0)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8.5)
    c.drawString(M + 10, yy - 13, str(i + 1))
    c.setStrokeColor(PLUM)
    c.rect(M + 36 + 23, yy - 14, 9, 9, fill=0, stroke=1)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(M + 92 + 14, yy - 13, "Y  /  N")
    c.setStrokeColor(LINE)
    yy -= rh
    c.line(M, yy, W - M, yy)
xx = M
for name, w in cols[:-1]:
    xx += w
    c.line(xx, top - rh, xx, yy)
c.rect(M, yy, W - 2 * M, top - yy, fill=0, stroke=1)
c.setFillColor(INK)
c.setFont("Helvetica-Bold", 10)
c.drawString(M, yy - 22, "Longest no-pick streak: ______ days      My #1 trigger: ________________________")
footer()

c.save()
print("saved", OUT, "pages:", page[0])
