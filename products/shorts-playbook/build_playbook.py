"""Builds 'The Faceless Shorts Playbook' PDF plus CSV bonuses (hook bank, 30-day calendar)."""
import csv

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table,
                                TableStyle)

import content as C

W, H = letter
M = 50
INK = HexColor("#1B1F24")
CORAL = HexColor("#E8553E")
CORAL_LT = HexColor("#FCE9E5")
LINE = HexColor("#D6D9DE")
MUTED = HexColor("#5F6872")
BAND = HexColor("#F4F5F7")

OUT = "Faceless_Shorts_Playbook.pdf"

body = ParagraphStyle("body", fontName="Helvetica", fontSize=10.5, leading=15.5, textColor=INK,
                      spaceAfter=8, alignment=TA_LEFT)
small = ParagraphStyle("small", parent=body, fontSize=9, leading=12.5, spaceAfter=0)
cell = ParagraphStyle("cell", parent=body, fontSize=9, leading=12, spaceAfter=0)
cell_b = ParagraphStyle("cellb", parent=cell, fontName="Helvetica-Bold")
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=24, leading=28, textColor=INK, spaceAfter=6)
kicker = ParagraphStyle("kicker", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=CORAL,
                        spaceAfter=4)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=13.5, leading=18, textColor=INK,
                    spaceBefore=10, spaceAfter=5)
bullet = ParagraphStyle("bullet", parent=body, leftIndent=14, bulletIndent=2, spaceAfter=4)
callout = ParagraphStyle("callout", parent=body, backColor=CORAL_LT, borderPadding=(9, 10, 9, 10),
                         spaceBefore=6, spaceAfter=14)


def chapter(n, title):
    return [Paragraph(f"PART {n}", kicker), Paragraph(title, h1),
            Table([[""]], colWidths=[48], rowHeights=[4],
                  style=[("BACKGROUND", (0, 0), (-1, -1), CORAL)], hAlign="LEFT"),
            Spacer(1, 14)]


def bullets(items, style=bullet):
    return [Paragraph(t, style, bulletText="•") for t in items]


def grid(rows, widths, header=True, zebra=True, row_h=None):
    t = Table(rows, colWidths=widths, rowHeights=row_h, repeatRows=1 if header else 0)
    st = [("GRID", (0, 0), (-1, -1), 0.5, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]
    if header:
        st += [("BACKGROUND", (0, 0), (-1, 0), INK), ("TEXTCOLOR", (0, 0), (-1, 0), white),
               ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"), ("FONTSIZE", (0, 0), (-1, 0), 8.5)]
    if zebra:
        for r in range(1 if header else 0, len(rows), 2):
            st.append(("BACKGROUND", (0, r), (-1, r), BAND))
    t.setStyle(TableStyle(st))
    return t


def write_lines(n, width=W - 2 * M):
    return grid([[""]] * n, [width], header=False, zebra=False, row_h=[24] * n)


def cover(c, _doc):
    c.saveState()
    c.setFillColor(INK)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(CORAL)
    # stylised 9:16 phone frames
    for i, (x, y, s) in enumerate([(W - 230, H - 420, 1.0), (W - 140, H - 330, 0.7)]):
        c.setFillColor(CORAL if i == 0 else HexColor("#F08A78"))
        c.roundRect(x, y, 135 * s, 240 * s, 16 * s, fill=1, stroke=0)
        c.setFillColor(INK)
        c.circle(x + 67 * s, y + 120 * s, 26 * s, fill=1, stroke=0)
        c.setFillColor(white)
        p = c.beginPath()
        p.moveTo(x + 59 * s, y + 132 * s)
        p.lineTo(x + 59 * s, y + 108 * s)
        p.lineTo(x + 80 * s, y + 120 * s)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(CORAL)
    c.rect(M, H / 2 - 20, 80, 6, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 50)
    c.drawString(M, H / 2 - 80, "FACELESS")
    c.drawString(M, H / 2 - 135, "SHORTS")
    c.setFillColor(CORAL)
    c.drawString(M, H / 2 - 190, "PLAYBOOK")
    c.setFillColor(white)
    c.setFont("Helvetica", 14)
    c.drawString(M, H / 2 - 225, C.SUBTITLE)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(HexColor("#AEB6BF"))
    c.drawString(M, 60, "5 FORMATS  |  60 HOOKS  |  30-DAY CALENDAR  |  FREE-TOOLS WORKFLOW")
    c.restoreState()


def page(c, doc):
    c.saveState()
    c.setFillColor(CORAL)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(M, 26, C.TITLE + "  |  For personal use only")
    c.drawRightString(W - M, 26, str(doc.page))
    c.restoreState()


def story():
    s = [PageBreak()]
    fw = W - 2 * M

    # Contents
    s += [Paragraph("What's inside", h1), Spacer(1, 8)]
    toc = ["Start here", "Pick your niche (worksheet)", "The 5 faceless formats", "Hooks: the formula and 60 templates",
           "The free-tools workflow: CapCut and Canva", "Batch day: a week of videos in one afternoon",
           "The 30-day calendar", "Monetization map", "The 5-minute weekly review", "Final rules"]
    s.append(grid([[Paragraph(f"<b>{i + 1:02d}</b>", cell), Paragraph(t, cell)] for i, t in enumerate(toc)],
                  [40, fw - 40], header=False))
    s += [Spacer(1, 16), Paragraph("<b>Bonus files included with this download:</b> hook_bank.csv and "
                                   "30_day_calendar.csv. Import them into Google Sheets or Notion "
                                   "(File > Import) to tick off each day.", callout), PageBreak()]

    # 1 Start here
    s += chapter(1, "Start here") + [Paragraph(p, body) for p in C.START_HERE[:2]]
    s.append(Paragraph(C.START_HERE[2], callout))
    s += [Paragraph("Your 30-day promise to yourself", h2),
          Paragraph("Niche: ________________________________   Start date: ______________", body),
          Paragraph("Time I'll post every day: ____________   Batch day each week: ______________", body),
          PageBreak()]

    # 2 Niche
    s += chapter(2, "Pick your niche") + [Paragraph(C.NICHE_INTRO, body), Spacer(1, 6)]
    rows = [["Question", "Idea A", "Idea B", "Idea C"]]
    rows.append([Paragraph("<b>Niche idea</b>", cell), "", "", ""])
    rows += [[Paragraph(q, cell), "", "", ""] for q in C.NICHE_QUESTIONS]
    rows.append([Paragraph("<b>Total (out of 25)</b>", cell), "", "", ""])
    s.append(grid(rows, [fw - 3 * 80, 80, 80, 80]))
    s += [Spacer(1, 12), Paragraph("My niche, in one sentence: \"I post about ______ for ______ who want ______.\"", body),
          Paragraph("Write 10 video ideas now:", h2), write_lines(10), PageBreak()]

    # 3 Formats
    s += chapter(3, "The 5 faceless formats")
    s.append(Paragraph("Rotate these five formats. Each needs nothing more than a phone, free apps and, at most, your hands on camera.", body))
    for name, what, why, struct, ex in C.FORMATS:
        rows = [[Paragraph("<b>What it is</b>", cell), Paragraph(what, cell)],
                [Paragraph("<b>Why it works</b>", cell), Paragraph(why, cell)],
                [Paragraph("<b>Structure</b>", cell), Paragraph(struct, cell)],
                [Paragraph("<b>Example</b>", cell), Paragraph(ex, cell)]]
        s.append(KeepTogether([Paragraph(name, h2), grid(rows, [95, fw - 95], header=False)]))
    s.append(PageBreak())

    # 4 Hooks
    s += chapter(4, "Hooks: the formula and 60 templates")
    s.append(Paragraph("Viewers decide in the first two or three seconds whether to keep watching. The hook is the most important line you'll write.", body))
    s.append(Paragraph(C.HOOK_FORMULA, callout))
    s += bullets(C.HOOK_RULES)
    s.append(Paragraph("Swap the [brackets] for your own details. Templates from other niches often work in yours too.", body))
    n = 1
    for niche, hooks in C.HOOKS.items():
        rows = [["#", niche + " hooks"]]
        for h in hooks:
            rows.append([str(n), Paragraph(h, cell)])
            n += 1
        s.append(KeepTogether([Spacer(1, 8), grid(rows, [30, fw - 30])]))
    s.append(PageBreak())

    # 5 Workflow
    s += chapter(5, "The free-tools workflow: CapCut and Canva")
    s.append(Paragraph("Target: about 30 minutes per video, less once you've made ten. Both apps have free plans; "
                       "menu names change between versions, so look for the closest match.", body))
    for i, (title, steps) in enumerate(C.WORKFLOW):
        extra = [Paragraph(C.SAFE_ZONES, callout)] if i == len(C.WORKFLOW) - 1 else []
        s.append(KeepTogether([Paragraph(title, h2)] + bullets(steps) + extra))
    s.append(PageBreak())

    # 6 Batch day
    s += chapter(6, "Batch day: a week of videos in one afternoon")
    s.append(Paragraph("Making one video a day from scratch is how most people quit. Make seven at once, then post one a day.", body))
    s.append(grid([["Done", "Step"]] + [["", Paragraph(t, cell)] for t in C.BATCH_DAY], [40, fw - 40]))
    s += [Spacer(1, 12), Paragraph("This week's 7 videos", h2)]
    s.append(grid([["Day", "Idea", "Format", "Hook #", "Posted"]] + [[str(i), "", "", "", ""] for i in range(1, 8)],
                  [40, fw - 40 - 100 - 60 - 55, 100, 60, 55], row_h=[20] + [26] * 7))
    s.append(PageBreak())

    # 7 Calendar
    s += chapter(7, "The 30-day calendar")
    s.append(Paragraph("Replace [niche] with your topic. Days 7, 14, 21 and 28 are review days: no new idea, just improve what worked.", body))
    rows = [["Day", "Format", "Video idea", "Hook tip", "Done"]]
    rows += [[str(d), Paragraph(f, cell_b), Paragraph(i, cell), Paragraph(t, cell), ""] for d, f, i, t in C.CALENDAR]
    s.append(grid(rows, [32, 72, fw - 32 - 72 - 140 - 36, 140, 36]))
    s.append(PageBreak())

    # 8 Monetization
    s += chapter(8, "Monetization map")
    s.append(Paragraph("Platforms change their payout rules often, so this map points you to the official source "
                       "instead of quoting numbers that go out of date. Check each one before you plan around it.", body))
    rows = [["Option", "How it pays", "Where to check"]]
    rows += [[Paragraph(f"<b>{a}</b>", cell), Paragraph(b, cell), Paragraph(c_, cell)] for a, b, c_ in C.MONETIZATION]
    s.append(grid(rows, [110, fw - 110 - 150, 150]))
    s.append(Paragraph("Realistic order for a new channel: affiliate links you'd recommend anyway, then your own "
                       "small product, then platform payouts once you qualify.", callout))
    s.append(PageBreak())

    # 9 Weekly review
    s += chapter(9, "The 5-minute weekly review")
    s.append(Paragraph("Every 7th day, open your analytics and fill this in. Print one copy per week.", body))
    s.append(grid([C.STATS_COLS] + [[""] * 6 for _ in range(7)], [fw / 6] * 6, row_h=[20] + [22] * 7))
    s.append(Spacer(1, 10))
    for q in C.REVIEW_QUESTIONS:
        s.append(KeepTogether([Paragraph(q, ParagraphStyle("q", parent=body, fontName="Helvetica-Bold", fontSize=9.5,
                                                            spaceAfter=3)), write_lines(1)]))
        s.append(Spacer(1, 4))
    s.append(PageBreak())

    # 10 Final
    s += chapter(10, "Final rules")
    s += bullets(C.FINAL)
    s.append(Spacer(1, 14))
    s.append(Paragraph("<b>Day 1 starts now:</b> score your niche, write 10 ideas, and batch your first 7 videos this week.", callout))
    s.append(Paragraph("<font size=8 color='#5F6872'>Disclaimer: this guide is for education only. No income or results "
                       "are promised. Platform names and features belong to their owners; this guide is not affiliated "
                       "with or endorsed by YouTube, TikTok, Meta, CapCut, Canva or any other company named.</font>", body))
    return s


def write_csvs():
    with open("hook_bank.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["#", "Niche", "Hook template"])
        n = 1
        for niche, hooks in C.HOOKS.items():
            for h in hooks:
                w.writerow([n, niche, h])
                n += 1
    with open("30_day_calendar.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Day", "Format", "Video idea", "Hook tip", "Hook # used", "Posted", "Views after 48h"])
        for row in C.CALENDAR:
            w.writerow(list(row) + ["", "", ""])


if __name__ == "__main__":
    doc = SimpleDocTemplate(OUT, pagesize=letter, leftMargin=M, rightMargin=M, topMargin=50, bottomMargin=50,
                            title=C.TITLE, author="Struggle92 Media")
    doc.build(story(), onFirstPage=cover, onLaterPages=page)
    write_csvs()
    print("built", OUT)
