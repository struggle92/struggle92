"""Builds 'The Marketplace Flipper Kit' — a sellable PDF (US Letter)."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

W, H = letter
M = 48
INK = HexColor("#1F2A2E")
SAGE = HexColor("#5E8C7A")
SAGE_LT = HexColor("#E6EFEB")
GOLD = HexColor("#D9A441")
LINE = HexColor("#C9D3CF")
MUTED = HexColor("#6B7A80")
RED = HexColor("#B5452F")
OUT = "Marketplace_Flipper_Kit.pdf"
TITLE = "The Marketplace Flipper Kit"
c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle(TITLE)
c.setAuthor("QFS")
page = [0]
y = [0]
open_page = [False]


def new_page(title, sub=None):
    if open_page[0]:
        footer()
        c.showPage()
    open_page[0] = True
    page[0] += 1
    c.setFillColor(SAGE)
    c.rect(0, H - 80, W, 80, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.rect(0, H - 84, W, 4, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(M, H - 48, title.upper())
    if sub:
        c.setFont("Helvetica", 10.5)
        c.drawString(M, H - 67, sub)
    y[0] = H - 112


def footer():
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(M, 24, TITLE + "  |  For personal use only. Not for resale.")
    c.drawRightString(W - M, 24, str(page[0]))


def ensure(h, title):
    if y[0] - h < 50:
        new_page(title + " (cont.)")


def para(text, size=10.5, color=INK, bold=False, gap=6, indent=0, lead=None):
    font = "Helvetica-Bold" if bold else "Helvetica"
    lead = lead or size * 1.4
    lines = simpleSplit(text, font, size, W - 2 * M - indent)
    c.setFillColor(color)
    c.setFont(font, size)
    for ln in lines:
        c.drawString(M + indent, y[0], ln)
        y[0] -= lead
    y[0] -= gap


def h2(text):
    y[0] -= 4
    c.setFillColor(SAGE)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(M, y[0], text.upper())
    y[0] -= 6
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.5)
    c.line(M, y[0], M + 60, y[0])
    y[0] -= 16


def bullets(items, size=10.5, mark="•", color=INK):
    for it in items:
        lines = simpleSplit(it, "Helvetica", size, W - 2 * M - 16)
        c.setFillColor(SAGE if color == INK else color)
        c.setFont("Helvetica-Bold", size)
        c.drawString(M + 2, y[0], mark)
        c.setFillColor(INK)
        c.setFont("Helvetica", size)
        for ln in lines:
            c.drawString(M + 16, y[0], ln)
            y[0] -= size * 1.4
        y[0] -= 3
    y[0] -= 4


def card(title, body, section, tag=None):
    """Script/template card with a tinted box."""
    lines = []
    for p in body.split("\n"):
        lines += simpleSplit(p, "Helvetica", 9.8, W - 2 * M - 24) or [""]
    h = 30 + len(lines) * 13.5
    ensure(h + 10, section)
    top = y[0] + 8
    c.setFillColor(SAGE_LT)
    c.setStrokeColor(LINE)
    c.roundRect(M, top - h, W - 2 * M, h, 6, fill=1, stroke=1)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(M + 12, top - 18, title)
    if tag:
        c.setFont("Helvetica-Oblique", 8.5)
        c.setFillColor(MUTED)
        c.drawRightString(W - M - 12, top - 18, tag)
    c.setFont("Helvetica", 9.8)
    c.setFillColor(INK)
    yy = top - 34
    for ln in lines:
        c.drawString(M + 12, yy, ln)
        yy -= 13.5
    y[0] = top - h - 14


# ---------------- Cover ----------------
page[0] = 1
c.setFillColor(SAGE)
c.rect(0, 0, W, H, fill=1, stroke=0)
c.setFillColor(GOLD)
c.rect(0, H * 0.42, W, 6, fill=1, stroke=0)
c.setFillColor(white)
c.setFont("Helvetica-Bold", 15)
c.drawString(M, H - 120, "FACEBOOK MARKETPLACE  •  OFFERUP  •  CRAIGSLIST")
c.setFont("Helvetica-Bold", 50)
c.drawString(M, H - 200, "The Marketplace")
c.drawString(M, H - 258, "Flipper Kit")
c.setFont("Helvetica", 16)
c.drawString(M, H - 300, "Find it cheap. List it right. Sell it fast. Stay safe.")
c.setFont("Helvetica", 12.5)
items = ["Sourcing guide: where to find underpriced stuff", "The profit check: what to pay, what to ask",
         "25 copy-and-paste listing templates", "30 buyer message scripts",
         "Photo checklist + title formula", "Scam red flags + safe meetup rules", "Printable flip log + weekly plan"]
yy = H * 0.42 - 40
for it in items:
    c.drawString(M, yy, "-  " + it)
    yy -= 22
c.setFont("Helvetica", 9)
c.drawString(M, 30, "For personal use only. Not for resale.")
c.showPage()

# ---------------- How to use ----------------
new_page("How to use this kit", "Read it once. Then keep it open on your phone while you list.")
para("Flipping is simple: buy something for less than people will pay for it, make it look good, and sell it. "
     "Most people fail at three spots: they pay too much, their listings are lazy, and they waste hours on "
     "buyers who never show up. This kit fixes all three.")
h2("The 4-step loop")
bullets(["SOURCE: Hunt in the places on page 3. Use the Profit Check (page 4) before you hand over a dollar.",
         "PREP: Clean it, fix the small stuff, and take 8 photos with the checklist on page 5.",
         "LIST: Copy the matching template (pages 6-8), fill in the blanks, and post at the times on page 5.",
         "SELL: Answer every message with the scripts (pages 9-11). Meet safely (page 12). Log the flip (page 13)."])
h2("Your first 30 days")
bullets(["Week 1: Start with stuff you already own. List 10 items you don't use. This is free inventory and practice.",
         "Week 2: Use that cash to buy 3-5 items under $30 each that pass the Profit Check.",
         "Week 3: Relist anything that hasn't sold in 7 days with a new first photo and a 10% lower price.",
         "Week 4: Look at your flip log. Double down on the category that sold fastest."])
h2("Ground rules")
bullets(["Only sell what you own and have in hand. No drop-shipping on Marketplace.",
         "Follow the platform's commerce rules. Some items are banned outright (see page 3).",
         "Keep records. Flip income is taxable income. Use a tracker (the Side Hustle Profit Tracker works with this kit)."])

# ---------------- Sourcing ----------------
new_page("Where to find inventory", "The money is made when you buy, not when you sell.")
h2("Best places to source")
bullets(["Facebook Marketplace 'Free' section: search your area daily. Furniture, bikes, grills and kids' gear show up constantly.",
         "Curb alerts and move-out days: end of month, end of semester near colleges, and spring cleaning season.",
         "Garage, yard and estate sales: go early for selection, go late for deals ('Make me an offer on the whole table').",
         "Thrift stores: check the furniture, tools, small appliance and sporting goods sections. Learn their discount-tag day.",
         "Retail clearance: end-of-season patio, holiday, outdoor and toy clearance resells well next season.",
         "Underpriced Marketplace listings: search with misspellings, 'moving must go', and bad-photo listings.",
         "Your own house and your family's: the easiest first profit you'll ever make."])
h2("What sells fast")
bullets(["Furniture: solid wood dressers, nightstands, dining sets, desks, outdoor/patio sets.",
         "Tools & yard: power tools, pressure washers, lawn mowers, generators, ladders.",
         "Kids & baby (allowed items only): wagons, ride-ons, play kitchens, toy lots, high chairs.",
         "Fitness: dumbbells, weight benches, bikes, treadmills (local pickup only).",
         "Electronics & gaming: consoles, games, speakers, monitors. Test everything in front of the buyer."])
h2("Avoid or skip")
bullets(["Anything recalled. Check cpsc.gov/recalls before you buy kids' items, heaters or appliances.",
         "Items Marketplace bans: weapons and ammo, alcohol, tobacco/vapes, medical items, animals, and more. Read Meta's Commerce Policies.",
         "Car seats and cribs: safety standards change and you can't verify history. Most flippers skip them.",
         "Counterfeits ('inspired' brand-name items), mattresses with stains, and anything with bed bugs. Inspect seams with a flashlight.",
         "Big, heavy items you can't move alone, unless you have a truck and a plan."], color=RED, mark="x")

# ---------------- Profit check ----------------
new_page("The Profit Check", "Run these numbers before you buy anything.")
h2("Step 1: Find the real selling price")
para("Search Marketplace (and eBay 'Sold' listings) for the same item. Ignore asking prices that have sat for weeks. "
     "Look for what similar items actually sold for, or what gets listed and disappears quickly. That's your Sell Price.")
h2("Step 2: The 3x rule (for beginners)")
para("Aim to pay no more than one third of the Sell Price, including any repair cost.", bold=True)
card("Example", "Solid wood dresser. Similar ones sell for $150.\n"
     "Max you pay (incl. paint & hardware): $150 ÷ 3 = $50\n"
     "Bought for $25 + $18 paint & knobs = $43.  Sold for $125.  Profit: $82.", "The Profit Check")
h2("Step 3: Ask the 5 questions")
bullets(["Can I sell it within 2 weeks? (Lots of similar sold items = yes.)",
         "Can I move it and store it?",
         "Does it work? Can I test it right now?",
         "Is the profit worth my time? Aim for at least $20-$25 per hour of work, including driving.",
         "Is it allowed and safe to sell? (Page 3.)"])
h2("Quick math table")
rows = [("If it sells for", "Pay max (3x)", "Pay max (2x, experienced)"),
        ("$30", "$10", "$15"), ("$60", "$20", "$30"), ("$100", "$33", "$50"),
        ("$150", "$50", "$75"), ("$250", "$83", "$125"), ("$400", "$133", "$200")]
x0, cw = M, [(W - 2 * M) / 3] * 3
for i, row in enumerate(rows):
    top = y[0] + 12
    c.setFillColor(INK if i == 0 else (SAGE_LT if i % 2 else white))
    c.rect(x0, top - 20, sum(cw), 20, fill=1, stroke=0)
    c.setFillColor(white if i == 0 else INK)
    c.setFont("Helvetica-Bold" if i == 0 else "Helvetica", 10)
    xx = x0
    for w, v in zip(cw, row):
        c.drawString(xx + 10, top - 14, v)
        xx += w
    y[0] -= 20
y[0] -= 12
para("Leave room for fees. Marketplace local pickup with cash has no selling fee; shipped orders and checkout payments do. "
     "Check the current fee on the platform before you price.", size=9.5, color=MUTED)

# ---------------- Photos & titles ----------------
new_page("Photos, titles & timing", "Listings with great first photos get the messages.")
h2("The 8-photo checklist")
bullets(["1. Hero shot: whole item, straight on, clean background, daylight, phone held at the item's middle height.",
         "2. Angle shot: 45 degrees to show depth.",
         "3. Brand/model label close-up (builds trust and helps search).",
         "4. Item working: screen on, lights on, engine running (a short video is even better).",
         "5. Size reference: tape measure across it, or next to a common object.",
         "6. Details: drawers open, inside, accessories, extras included.",
         "7. Flaws: show every scratch honestly. It prevents haggling at pickup.",
         "8. Bundle shot: everything included in one photo."])
h2("Title formula")
card("[Brand] + [Item] + [Key feature] + [Condition/size]",
     "Bad:  Dresser\n"
     "Good: Solid Wood 6-Drawer Dresser - Refinished Matte Black, New Hardware\n"
     "Good: DeWalt 20V Drill + 2 Batteries & Charger - Works Great\n"
     "Good: Graco 4-in-1 High Chair - Clean, Folds Flat", "Photos, titles & timing")
h2("Pricing & timing")
bullets(["Price 10-15% above your lowest acceptable number. Buyers expect to negotiate.",
         "End prices in 5 or 0 ($45, $120). Locals pay cash in round numbers.",
         "Post on weekday evenings (6-9 pm) and weekend mornings when people browse.",
         "No messages in 3 days: new first photo. No sale in 7 days: drop 10% and renew the listing.",
         "List in several places: Marketplace, OfferUp, Craigslist, local buy/sell groups. Delete everywhere once it sells."])

# ---------------- Listing templates ----------------
new_page("Listing templates", "Copy, paste, fill in the [brackets]. Delete lines that don't apply.")
T = "Listing templates"
templates = [
    ("1. Furniture (refinished)", "Solid wood [item] - refinished in [color] with new [hardware/top coat].\n"
     "Measures [W x D x H] inches. Drawers slide smoothly. No wobble.\n"
     "Smoke-free home. Pickup in [area]. Can help load.\nAsking $[price]. Serious buyers only, first to show up takes it."),
    ("2. Furniture (as-is)", "[Brand] [item] in good used condition. [Number] small scuffs shown in photos.\n"
     "Size: [W x D x H]. Sturdy, everything works.\nPickup only in [area], [day/time window]. $[price] cash."),
    ("3. Patio / outdoor set", "[Material] patio set: [table + 4 chairs / sectional / etc.]. Cushions [included/clean/washed].\n"
     "Weather-ready and sturdy. Great for this season.\nPickup in [area]. $[price]."),
    ("4. Power tool", "[Brand] [model] [tool]. Tested and works great.\nIncludes: [battery count + charger + case + bits].\n"
     "Battery holds a charge. Happy to show it running at pickup.\n$[price] firm for the set."),
    ("5. Lawn mower / yard equipment", "[Brand] [type] [model], [engine/size].\nStarts on [first/second] pull. Fresh oil and sharpened blade.\n"
     "Video of it running in photos. Pickup in [area]. $[price]."),
    ("6. Pressure washer / generator", "[Brand] [PSI/watts] [item]. Runs strong, tested [date].\n"
     "Includes [hose, wand, tips / cords]. Pickup and see it run. $[price]."),
    ("7. Video game console", "[Console + storage size]. Factory reset and ready to go.\n"
     "Includes: [controllers, cables, games].\nTested: plays discs, connects online, no drift. Can test at pickup. $[price]."),
    ("8. Game lot", "Lot of [number] [platform] games. All discs clean and tested.\n"
     "Titles: [list]. $[bundle price] for all or $[each] each. Bundle gets priority."),
    ("9. TV / monitor", "[Brand] [size]\" [type] [TV/monitor], [resolution].\nNo dead pixels, no lines. Includes [remote, stand, power cord].\n"
     "Can turn it on for you at pickup. $[price]."),
    ("10. Speaker / audio", "[Brand] [model]. Sounds great, no crackle.\nIncludes [cables/remote]. Tested with Bluetooth and aux. $[price]."),
    ("11. Phone / tablet", "[Brand model, storage], [color]. Unlocked / [carrier].\nBattery health [%]. Screen [condition]. Factory reset, removed from my account.\n"
     "Meet at a public place or police station exchange zone. $[price]."),
    ("12. Kids' ride-on / wagon", "[Brand] [item]. Clean, all parts included, [batteries hold charge].\n"
     "Ages [range]. Pickup in [area]. $[price]."),
    ("13. Toy lot", "Big lot of [brand/type] toys - [number]+ pieces. All washed and sanitized.\n"
     "From a smoke-free, pet-free home. $[price] for everything."),
    ("14. Baby gear (allowed items)", "[Brand] [item]. Clean, washed, works perfectly.\n"
     "Not recalled (checked cpsc.gov). Folds for storage. $[price]."),
    ("15. Bike", "[Brand] [model], [wheel size], [speeds].\nTires aired, brakes adjusted, chain lubed. Fits about [height range].\n"
     "Test ride welcome with ID held. $[price]."),
    ("16. Fitness equipment", "[Brand] [item] - [weight/size].\nGreat condition, [no rust / all parts].\nYou pick up from [ground floor/garage]. $[price]."),
    ("17. Small kitchen appliance", "[Brand] [appliance]. Clean, works perfectly, tested today.\nIncludes [parts/attachments]. Pet and smoke-free home. $[price]."),
    ("18. Large appliance", "[Brand] [washer/dryer/fridge], [size]. Works great, [reason for selling].\n"
     "Clean inside and out. Must bring help + a truck/dolly. $[price]."),
    ("19. Home decor lot", "[Style] decor bundle: [mirror, lamps, frames, vases...].\nPerfect for a new apartment. $[price] for all, or ask about singles."),
    ("20. Rug", "[Size] [brand/material] rug. Clean, no stains, no odors. Just vacuumed.\nColors: [colors]. Rolled and ready. $[price]."),
    ("21. Clothing lot", "[Size] [men's/women's/kids'] clothing lot - [number] pieces.\nBrands include [brands]. Washed, no stains or holes.\n$[price] for everything."),
    ("22. Sneakers / shoes", "[Brand model], size [size], [color].\nWorn [number] times, [condition]. [Box included / no box].\nAuthentic - receipt available. $[price]."),
    ("23. Tool / hardware lot", "Garage cleanout lot: [hand tools, sockets, screws, etc.].\nAll in [bins/toolbox]. Great starter set. $[price] for all."),
    ("24. Storage / shelving", "[Brand] [shelving/cabinet], [size].\nSturdy, holds [weight]. [Disassembled / ready to load]. $[price]."),
    ("25. Free-to-flip bundle", "Moving sale! Everything in photos for $[price] or best offer.\n"
     "Includes [list]. Must take it all, pickup [date] only in [area]."),
]
for t, b in templates:
    card(t, b, T)

# ---------------- Scripts ----------------
new_page("Buyer message scripts", "Fast, friendly, firm. Copy, paste, send.")
S = "Buyer message scripts"
scripts = [
    ("'Is this still available?'", "Yes, it's available! I can do pickup [today after 5 / tomorrow morning] in [area]. What time works for you?"),
    ("They ask a question answered in the listing", "Yep! [Answer]. It's still available. Want to set a pickup time?"),
    ("Lowball offer (way too low)", "Thanks for the offer! I can't go that low. Lowest I can do is $[price]. Let me know if that works."),
    ("Reasonable offer", "I can do $[price] if you can pick up by [day]. Deal?"),
    ("Price is firm", "Thanks! The price is firm, since it's [refinished / tested / priced below retail]. It's yours at $[price] if you want it."),
    ("'What's your lowest?'", "What did you have in mind? I'm open to reasonable offers for a quick pickup."),
    ("Bundle offer", "If you take [item] and [item] together, I'll do $[price] for both."),
    ("Confirm pickup", "Great! See you [day] at [time] at [public place / my address]. Cash or [app] works. Please message if anything changes."),
    ("Day-of reminder", "Hey, just confirming we're still on for [time] today. See you then!"),
    ("They're late", "Hi, I'm here. Are you still coming? I can wait until [time]."),
    ("No-show (move on)", "No worries. I'm going to offer it to the next person in line. If you still want it, message me and I'll let you know if it's still available."),
    ("Next in line", "Hi! The first buyer didn't show, so it's available again. Can you pick up [today/tomorrow]?"),
    ("Hold request", "I don't hold items without a pickup time, sorry! First person to show up gets it. When could you come?"),
    ("Delivery request", "I can deliver within [X] miles for $[fee]. Payment at drop-off. Want me to schedule it?"),
    ("'Can you send more pictures?'", "Sure! Here are a few more. [Send photos.] Anything specific you want to see?"),
    ("'Does it work?'", "Yes, tested it today. You're welcome to test it at pickup before you pay."),
    ("They want to haggle at pickup", "We agreed on $[price] in messages. That's the price. If it doesn't work for you, no problem at all."),
    ("They want to pay later / IOU", "Sorry, I only release items when paid in full at pickup."),
    ("Ask for the next sale", "Thanks again! I flip [furniture/tools] all the time. Want me to message you if I find [their interest]?"),
    ("Pending sale", "Someone is coming at [time]. If they don't show, you're next and I'll message you."),
    ("It's sold", "Sorry, it just sold! I'll have more [category] soon. Follow my listings to see new stuff first."),
    ("Item has a flaw they ask about", "Good question. There's [flaw], shown in photo [#]. It doesn't affect [how it works]. That's why it's priced at $[price]."),
    ("Buyer asks for your phone number", "I keep everything in Messenger for now. Easiest way to reach me is right here."),
    ("Buyer wants to ship", "Local pickup only for this one, sorry!"),
    ("Price drop alert to past askers", "Hi! You asked about the [item] earlier. I dropped it to $[price]. Still interested?"),
    ("Multiple people interested", "Thanks! A few people are interested, so it goes to whoever picks up first. When can you come?"),
    ("Counter a counteroffer", "Let's meet in the middle at $[price], and it's yours."),
    ("Final ask before relisting", "Last call: I'm taking this down to relist tonight. $[price] if you want it today."),
    ("Asking for a rating", "Thanks for buying! If you have a sec, a rating on Marketplace helps me a ton."),
    ("Polite no", "Thanks for reaching out, but I'm going to pass. Good luck with your search!"),
]
for t, b in scripts:
    card(t, b, S)

# ---------------- Safety ----------------
new_page("Scams & safe meetups", "If something feels off, walk away. No sale is worth it.")
h2("Scam red flags")
bullets([
    "They ask you to send a verification code from your phone (Google Voice scam). Never share any code.",
    "They want to pay with a cashier's check, money order or more than the price, then ask you to refund the difference.",
    "'My mover / cousin will pick it up, I'll pay with [app] now' combined with fake payment emails. Check your actual app or bank balance, not an email.",
    "They push you to ship an item that's listed as local pickup, especially with a prepaid label they send.",
    "They want to move to email or text right away, or send links to 'confirm' or 'receive' a payment.",
    "Payment-app 'business account upgrade' messages. Real payment apps don't email you to unlock funds.",
], color=RED, mark="!")
h2("Safe payment")
bullets(["Cash is king for local sales. Count it in front of them. Check large bills.",
         "Instant payment apps: only accept once you see it in your app balance, not in an email or screenshot.",
         "Never accept checks from strangers."])
h2("Safe meetups")
bullets(["Meet at a police station 'safe exchange zone' or a busy store parking lot in daylight.",
         "For big items at home: move the item to your garage or porch, have someone with you, and don't invite buyers inside.",
         "Tell someone where you'll be and when. Share your location.",
         "Trust your gut. Cancel any meetup that feels wrong."])
para("Report scam accounts to the platform and at reportfraud.ftc.gov.", size=9.5, color=MUTED)

# ---------------- Flip log + weekly plan ----------------
new_page("Flip log", "Print this page, or use the Side Hustle Profit Tracker spreadsheet.")
cols = [("Item", 150), ("Paid", 50), ("Fixes", 50), ("Listed", 55), ("Sold", 55), ("Profit", 55), ("Days", 51)]
top = y[0] + 10
rh = 22
c.setFillColor(INK)
c.rect(M, top - rh, W - 2 * M, rh, fill=1, stroke=0)
c.setFillColor(white)
c.setFont("Helvetica-Bold", 9)
xx = M
for name, w in cols:
    c.drawString(xx + 5, top - 15, name.upper())
    xx += w
c.setStrokeColor(LINE)
yy = top - rh
for i in range(26):
    if i % 2 == 0:
        c.setFillColor(SAGE_LT)
        c.rect(M, yy - rh, W - 2 * M, rh, fill=1, stroke=0)
    yy -= rh
    c.line(M, yy, W - M, yy)
xx = M
for name, w in cols[:-1]:
    xx += w
    c.line(xx, top - rh, xx, yy)
c.rect(M, yy, W - 2 * M, top - yy, fill=0, stroke=1)

new_page("Weekly flip plan", "One page, every week. Check it off.")
week = [("MONDAY", "Relist anything older than 7 days with a new first photo."),
        ("TUESDAY", "Source online: Free section, underpriced listings, misspellings."),
        ("WEDNESDAY", "Clean, fix and photograph new items."),
        ("THURSDAY", "List new items in the evening (6-9 pm). Cross-post to OfferUp and groups."),
        ("FRIDAY", "Plan weekend route: garage sales, estate sales, thrift discount days."),
        ("SATURDAY", "Source in person early. Do pickups and sales."),
        ("SUNDAY", "Log every buy and sale. Count profit. Set next week's goal.")]
for d, t in week:
    top = y[0] + 10
    c.setFillColor(SAGE_LT)
    c.roundRect(M, top - 62, W - 2 * M, 62, 6, fill=1, stroke=0)
    c.setFillColor(SAGE)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(M + 12, top - 20, d)
    c.setFillColor(INK)
    c.setFont("Helvetica", 10)
    c.drawString(M + 110, top - 20, t)
    c.setStrokeColor(LINE)
    c.rect(W - M - 26, top - 28, 14, 14, fill=0, stroke=1)
    c.line(M + 110, top - 46, W - M - 40, top - 46)
    y[0] -= 72
para("This week's profit goal: $________     Actual: $________", bold=True, size=11)

footer()
c.save()
print("saved", OUT, "pages:", page[0])
