"""Builds 'The Hustle Money Planner' — a printable, sellable PDF (US Letter)."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas

W, H = letter
M = 42  # margin
INK = HexColor("#1F2A2E")
SAGE = HexColor("#5E8C7A")
SAGE_LT = HexColor("#E6EFEB")
GOLD = HexColor("#D9A441")
LINE = HexColor("#C9D3CF")
MUTED = HexColor("#6B7A80")

OUT = "Hustle_Money_Planner.pdf"
page_no = [0]


def header(c, title, sub=None, month=True):
    c.setFillColor(SAGE)
    c.rect(0, H - 78, W, 78, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.rect(0, H - 82, W, 4, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(M, H - 48, title.upper())
    if sub:
        c.setFont("Helvetica", 10)
        c.drawString(M, H - 66, sub)
    if month:
        c.setFont("Helvetica", 9)
        c.drawRightString(W - M, H - 48, "MONTH: ____________")


def footer(c):
    page_no[0] += 1
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(M, 22, "The Hustle Money Planner  |  For personal use only")
    c.drawRightString(W - M, 22, str(page_no[0]))


def label(c, x, y, text, size=10, color=INK, bold=True):
    c.setFillColor(color)
    c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
    c.drawString(x, y, text)


def table(c, x, y, widths, headers, rows, row_h=20):
    """Draws a header bar + empty ruled rows. Returns bottom y."""
    total = sum(widths)
    c.setFillColor(INK)
    c.rect(x, y - row_h, total, row_h, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 8.5)
    cx = x
    for w, h in zip(widths, headers):
        c.drawString(cx + 5, y - row_h + 6.5, h.upper())
        cx += w
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    yy = y - row_h
    for i in range(rows):
        if i % 2 == 0:
            c.setFillColor(SAGE_LT)
            c.rect(x, yy - row_h, total, row_h, fill=1, stroke=0)
        yy -= row_h
        c.line(x, yy, x + total, yy)
    cx = x
    for w in widths[:-1]:
        cx += w
        c.line(cx, y - row_h, cx, yy)
    c.rect(x, yy, total, y - yy, fill=0, stroke=1)
    return yy


def box(c, x, y, w, h, title):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.8)
    c.roundRect(x, y - h, w, h, 6, fill=0, stroke=1)
    c.setFillColor(SAGE)
    c.roundRect(x, y - 20, w, 20, 6, fill=1, stroke=0)
    c.rect(x, y - 20, w, 8, fill=1, stroke=0)
    label(c, x + 8, y - 14, title.upper(), 9, white)


def lines_in(c, x, y, w, h, gap=20):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    yy = y - 20 - gap
    while yy > y - h + 6:
        c.line(x + 8, yy, x + w - 8, yy)
        yy -= gap


# ---------------------------------------------------------------- pages
def cover(c):
    c.setFillColor(SAGE)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(HexColor("#4E7A69"))
    c.circle(W - 60, H - 80, 190, fill=1, stroke=0)
    c.circle(70, 120, 140, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.rect(M, H / 2 + 92, 80, 6, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 54)
    c.drawString(M, H / 2 + 30, "THE HUSTLE")
    c.drawString(M, H / 2 - 30, "MONEY PLANNER")
    c.setFont("Helvetica", 15)
    c.drawString(M, H / 2 - 70, "Budget  •  Track  •  Pay Off Debt  •  Grow Side Income")
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(GOLD)
    c.drawString(M, 70, "PRINTABLE  |  UNDATED  |  US LETTER")
    c.showPage()


def how_to(c):
    header(c, "How to Use This Planner", "Print what you need. Reprint monthly. Stay consistent.", month=False)
    steps = [
        ("1. Set your yearly goals", "Write 3 money goals and your why. Keep it visible."),
        ("2. Build a monthly budget", "Give every dollar a job before the month starts."),
        ("3. Log income & expenses", "Track every dollar in and out. Takes 2 minutes a day."),
        ("4. Audit subscriptions", "List every recurring charge. Cancel what you don't use."),
        ("5. Attack debt", "Use the snowball (smallest first) or avalanche (highest rate first)."),
        ("6. Track side-hustle sales", "Know your real profit after fees, shipping and costs."),
        ("7. Save on autopilot", "Color in the savings challenge as you hit each amount."),
        ("8. Review monthly", "What worked, what didn't, and one thing to change."),
    ]
    y = H - 130
    for t, d in steps:
        c.setFillColor(GOLD)
        c.circle(M + 6, y + 4, 4, fill=1, stroke=0)
        label(c, M + 20, y, t, 13)
        label(c, M + 20, y - 17, d, 10.5, MUTED, bold=False)
        y -= 62
    c.setFillColor(SAGE_LT)
    c.roundRect(M, 60, W - 2 * M, 60, 8, fill=1, stroke=0)
    label(c, M + 14, 95, "TIP:", 11, SAGE)
    label(c, M + 50, 95, "Print the monthly pages 12x, or save as a PDF and fill in on a tablet", 10.5, INK, False)
    label(c, M + 50, 79, "with GoodNotes, Notability, or Xodo.", 10.5, INK, False)
    footer(c)
    c.showPage()


def yearly_goals(c):
    header(c, "Yearly Money Goals", "Where do you want to be 12 months from now?", month=False)
    bw = (W - 2 * M - 14) / 2
    y = H - 104
    for i, t in enumerate(["Goal #1", "Goal #2", "Goal #3", "My Why"]):
        x = M + (i % 2) * (bw + 14)
        yy = y - (i // 2) * 200
        box(c, x, yy, bw, 186, t)
        lines_in(c, x, yy, bw, 186)
    y2 = y - 412
    label(c, M, y2, "NET WORTH SNAPSHOT", 11, SAGE)
    table(c, M, y2 - 8, [180, 116, 116, 116], ["", "Jan", "Jun", "Dec"], 0)
    rows = ["Total Assets", "Total Debts", "Net Worth"]
    yy = y2 - 28
    for r in rows:
        c.setStrokeColor(LINE)
        c.rect(M, yy - 22, 528, 22, fill=0, stroke=1)
        for cx in (M + 180, M + 296, M + 412):
            c.line(cx, yy - 22, cx, yy)
        label(c, M + 6, yy - 15, r, 9.5)
        yy -= 22
    footer(c)
    c.showPage()


def monthly_budget(c):
    header(c, "Monthly Budget", "Income minus expenses should equal zero. Every dollar gets a job.")
    y = H - 100
    bw = (W - 2 * M - 14) / 2
    label(c, M, y, "INCOME", 11, SAGE)
    table(c, M, y - 6, [bw - 140, 70, 70], ["Source", "Planned", "Actual"], 6)
    x2 = M + bw + 14
    label(c, x2, y, "SAVINGS & DEBT", 11, SAGE)
    table(c, x2, y - 6, [bw - 140, 70, 70], ["Item", "Planned", "Actual"], 6)
    y = y - 170
    label(c, M, y, "FIXED EXPENSES", 11, SAGE)
    table(c, M, y - 6, [bw - 140, 70, 70], ["Bill", "Planned", "Actual"], 12)
    label(c, x2, y, "VARIABLE EXPENSES", 11, SAGE)
    table(c, x2, y - 6, [bw - 140, 70, 70], ["Category", "Planned", "Actual"], 12)
    y = y - 290
    c.setFillColor(INK)
    c.roundRect(M, y - 70, W - 2 * M, 70, 8, fill=1, stroke=0)
    cols = ["TOTAL INCOME", "TOTAL EXPENSES", "SAVED / PAID", "LEFT OVER"]
    cw = (W - 2 * M) / 4
    for i, t in enumerate(cols):
        label(c, M + i * cw + 14, y - 22, t, 9, GOLD)
        c.setStrokeColor(white)
        c.line(M + i * cw + 14, y - 52, M + (i + 1) * cw - 14, y - 52)
        label(c, M + i * cw + 14, y - 48, "$", 13, white)
    footer(c)
    c.showPage()


def tracker(c, title, sub, headers, widths):
    header(c, title, sub)
    table(c, M, H - 100, widths, headers, 30, row_h=20.5)
    footer(c)
    c.showPage()


def subscriptions(c):
    header(c, "Subscription Tracker", "Every recurring charge in one place. Keep it, cancel it, or downgrade it.")
    bottom = table(c, M, H - 100, [150, 70, 70, 70, 90, 78],
                   ["Service", "Cost", "Billing", "Due Day", "Payment Card", "Keep?"], 22)
    y = bottom - 26
    c.setFillColor(SAGE_LT)
    c.roundRect(M, y - 70, W - 2 * M, 70, 8, fill=1, stroke=0)
    label(c, M + 14, y - 22, "MONTHLY TOTAL:  $__________", 12)
    label(c, M + 290, y - 22, "YEARLY TOTAL:  $__________", 12)
    label(c, M + 14, y - 48, "CANCELLED THIS MONTH = SAVED:  $__________", 12, SAGE)
    footer(c)
    c.showPage()


def bills(c):
    header(c, "Bill Payment Checklist", "Check off each bill as it's paid. Never pay a late fee again.")
    months = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]
    table(c, M, H - 100, [150, 54, 40] + [23.7] * 12, ["Bill", "Amount", "Due"] + months, 28, row_h=21)
    footer(c)
    c.showPage()


def debt_payoff(c):
    header(c, "Debt Payoff Plan", "List debts, pick a method, then attack one at a time.")
    y = H - 100
    table(c, M, y, [140, 80, 60, 80, 80, 88],
          ["Debt", "Balance", "Rate %", "Min Pay", "Payoff Order", "Paid Off Date"], 8)
    y = y - 210
    label(c, M, y, "METHOD:   [  ] SNOWBALL (smallest balance first)     [  ] AVALANCHE (highest rate first)", 10.5)
    y -= 26
    label(c, M, y, "PAYOFF THERMOMETER — color in each box as you pay down $____ each", 11, SAGE)
    y -= 14
    size = 26
    cols = int((W - 2 * M) // size)
    c.setStrokeColor(SAGE)
    for r in range(8):
        for col in range(cols):
            c.rect(M + col * size, y - (r + 1) * size, size - 3, size - 3, fill=0, stroke=1)
    y = y - 8 * size - 22
    label(c, M, y, "DEBT-FREE DATE GOAL:  _______________          TOTAL DEBT START:  $___________", 11)
    footer(c)
    c.showPage()


def debt_tracker(c):
    header(c, "Single Debt Tracker", "One page per debt. Watch the balance drop.")
    label(c, M, H - 104, "DEBT: __________________   STARTING BALANCE: $__________   RATE: _____%", 10.5)
    table(c, M, H - 116, [90, 110, 110, 110, 108], ["Date", "Payment", "Interest", "New Balance", "Notes"], 28)
    footer(c)
    c.showPage()


def savings_challenge(c):
    header(c, "$5,000 Savings Challenge", "Color in a box each time you save that amount. 100 boxes = $5,000.")
    amounts = ([10] * 20 + [25] * 20 + [50] * 29 + [75] * 10 + [100] * 21)
    assert sum(amounts) == 5000 and len(amounts) == 100
    # shuffle deterministically for a playful layout
    order = [(i * 37) % 100 for i in range(100)]
    amounts = [amounts[i] for i in order]
    cols, size = 10, (W - 2 * M) / 10
    top = H - 112
    for i, a in enumerate(amounts):
        r, col = divmod(i, cols)
        x, y = M + col * size, top - (r + 1) * size
        c.setStrokeColor(SAGE)
        c.setFillColor(SAGE_LT if (r + col) % 2 == 0 else white)
        c.roundRect(x + 3, y + 3, size - 6, size - 6, 6, fill=1, stroke=1)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(x + size / 2, y + size / 2 - 5, f"${a}")
    footer(c)
    c.showPage()


def sinking_funds(c):
    header(c, "Sinking Funds", "Save a little each month for big expenses you KNOW are coming.")
    bw = (W - 2 * M - 14) / 2
    funds = ["Car Repairs", "Holidays & Gifts", "Emergency Fund", "Vacation", "Medical", "Fund: ________"]
    for i, f in enumerate(funds):
        x = M + (i % 2) * (bw + 14)
        y = H - 100 - (i // 2) * 210
        box(c, x, y, bw, 198, f)
        label(c, x + 8, y - 38, "Goal: $________    By: ________", 9, MUTED, False)
        table(c, x + 8, y - 48, [70, (bw - 16 - 70) / 2, (bw - 16 - 70) / 2], ["Date", "Added", "Total"], 6, row_h=19)
    footer(c)
    c.showPage()


def hustle_sales(c):
    header(c, "Side Hustle Sales Log", "Know your REAL profit: sale price minus fees, shipping and cost of goods.")
    table(c, M, H - 100, [56, 132, 62, 58, 62, 62, 96],
          ["Date", "Item / Service", "Platform", "Price", "Fees+Ship", "Cost", "Profit"], 28, row_h=20.5)
    footer(c)
    c.showPage()


def hustle_dashboard(c):
    header(c, "Side Hustle Dashboard", "Treat it like a business. Measure it like a business.")
    bw = (W - 2 * M - 28) / 3
    y = H - 104
    for i, t in enumerate(["Gross Sales", "Total Costs", "Net Profit"]):
        x = M + i * (bw + 14)
        c.setFillColor(SAGE_LT)
        c.roundRect(x, y - 70, bw, 70, 8, fill=1, stroke=0)
        label(c, x + 12, y - 22, t.upper(), 9, SAGE)
        label(c, x + 12, y - 54, "$ __________", 16)
    y -= 92
    bw2 = (W - 2 * M - 14) / 2
    box(c, M, y, bw2, 200, "Best Sellers / Top Clients")
    lines_in(c, M, y, bw2, 200)
    box(c, M + bw2 + 14, y, bw2, 200, "Where Leads Came From")
    lines_in(c, M + bw2 + 14, y, bw2, 200)
    y -= 214
    box(c, M, y, bw2, 200, "What Worked")
    lines_in(c, M, y, bw2, 200)
    box(c, M + bw2 + 14, y, bw2, 200, "Next Month's Goals")
    lines_in(c, M + bw2 + 14, y, bw2, 200)
    footer(c)
    c.showPage()


def monthly_review(c):
    header(c, "Monthly Review", "Ten minutes of honesty saves hundreds of dollars.")
    qs = ["My biggest win this month was...", "Where did I overspend, and why?",
          "What subscription or bill can I cut or lower?", "How much did I put toward debt and savings?",
          "One thing I will do differently next month:"]
    y = H - 100
    for q in qs:
        box(c, M, y, W - 2 * M, 112, q)
        lines_in(c, M, y, W - 2 * M, 112)
        y -= 124
    footer(c)
    c.showPage()


def thanks(c):
    c.setFillColor(SAGE)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 40)
    c.drawCentredString(W / 2, H / 2 + 40, "THANK YOU!")
    c.setFont("Helvetica", 13)
    c.drawCentredString(W / 2, H / 2, "If this planner helps you, a quick review means the world.")
    c.drawCentredString(W / 2, H / 2 - 20, "Tag your progress so we can cheer you on.")
    c.setFillColor(GOLD)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(W / 2, 70, "Personal use only. Please do not resell or redistribute.")
    c.showPage()


def build():
    c = canvas.Canvas(OUT, pagesize=letter)
    c.setTitle("The Hustle Money Planner")
    c.setAuthor("The Hustle Money Planner")
    cover(c)
    how_to(c)
    yearly_goals(c)
    monthly_budget(c)
    tracker(c, "Income Tracker", "Every dollar that comes in: job, side hustle, refunds, gifts.",
            ["Date", "Source", "Category", "Amount", "Notes"], [70, 160, 100, 80, 118])
    tracker(c, "Expense Tracker", "Every dollar that goes out. Small leaks sink big ships.",
            ["Date", "Description", "Category", "Paid With", "Amount"], [70, 180, 100, 90, 88])
    subscriptions(c)
    bills(c)
    debt_payoff(c)
    debt_tracker(c)
    savings_challenge(c)
    sinking_funds(c)
    hustle_sales(c)
    hustle_dashboard(c)
    monthly_review(c)
    thanks(c)
    c.save()
    print("wrote", OUT, "pages:", page_no[0] + 2)


if __name__ == "__main__":
    build()
