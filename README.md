# Struggle92 Funnels

Four video-sales-letter (VSL) funnels on one page, plus ready-to-post copy for each.

| Offer | Page link | Copy pack |
|---|---|---|
| Done-for-you short videos for local businesses | `funnel/index.html#service` | `copy/service.md` |
| Faceless Shorts Playbook ($27) | `funnel/index.html#digital` | `copy/digital.md` |
| Affiliate bridge page (Canva Pro example) | `funnel/index.html#affiliate` | `copy/affiliate.md` |
| Mobile detailing (local business example) | `funnel/index.html#local` | `copy/local.md` |

## Go live checklist

1. **Edit the config** at the top of the `<script>` in `funnel/page.html`: brand, contact, prices and copy.
2. **Rebuild the standalone page:** `./build.sh` (wraps `page.html` into `index.html`).
3. **Record the VSL** from the script in the copy pack. Upload it to YouTube (unlisted is fine), then set the player's link to the video URL.
4. **Capture leads:** in Zapier, create a Zap with "Webhooks by Zapier → Catch Hook", then add actions for Google Sheets (add row) and Gmail (send the email-1 reply). Paste the hook URL into `WEBHOOK_URL`.
5. **Replace testimonial slots** with real quotes from real customers, and only with their permission.
6. **Set `SHOW_SWITCHER: false`** and host each offer separately: GitHub Pages, Vercel or Netlify (all free). Link directly to `#service`, `#local` and so on.
7. **Affiliate:** join the program first and paste your tracking link into `afterLink`.

## Rules that keep ad accounts and payouts safe

- No income guarantees, fake countdown timers or made-up testimonials.
- Keep the disclosures in the page footers.
- Don't use celebrity or brand names or likenesses to imply an endorsement.

## Pocket Gram Scale (`scale/index.html`)

A 0.00 g scale display: zero, tare, hold, units (g, ct, oz, ozt, dwt, gr), a spoons-to-grams spice converter, price per gram, calibration and a reading log with CSV copy.
A phone has no weight sensor, so the numbers come from a real scale: type the reading from any 0.01 g pocket scale, or plug in a lab/jewelry balance with USB or RS-232 output (Chrome or Edge on a computer). Demo mode is simulated.
Edit `scale/page.html`, then run `./build.sh`.

## Faceless Shorts Playbook (`products/shorts-playbook/`)

The $27 product behind the `#digital` funnel: an 18-page PDF plus `hook_bank.csv` and `30_day_calendar.csv`, zipped as `Faceless_Shorts_Playbook.zip`.
Edit text in `content.py`, then run `python3 build_playbook.py` (output is git-ignored) (needs `pip install reportlab`). Listing copy and setup steps are in `LISTING.md`.

## Shop (`shop/index.html`)

A storefront page for the playbook ($27), the planner ($4.99) and both together ($31.99, one checkout).
Every buy button goes to the Shopify store (qfs1-store.myshopify.com). Shopify takes the payment and Digital Products emails the download, so files stay behind the payment.

- Each product needs its file attached in Shopify (Apps > Digital Products) or buyers receive nothing.
- To change a link, edit `checkout` in `PRODUCTS` at the top of the script in `shop/page.html`, then run `./build.sh` and redeploy.
- Never commit paid files: this repo and the site are public. Build them locally with each product's build script; `.gitignore` keeps them out.

## Content engine (`content/`)

30 days of faceless image posts (1080x1350 cards) that point to the shop. Text lives in `content/posts.py`; run `python3 content/build_posts.py` to redraw `content/cards/` and `content/queue.json`.
The cards are served from the site, so a scheduler (Metricool) can pull them by URL. `queue.json` marks which days are already scheduled.

## Quick Fix Studios booking page (`qfs/index.html`)

Services, prices, monthly plans and a booking form for the handyman, yard and pet waste business. The form opens the customer's text app (or email) with the request filled in, so it needs no server.
Set `PHONE` (and optionally `EMAIL`) in `CONFIG` at the top of the script in `qfs/page.html`, then run `./build.sh` and redeploy. Prices live in `SERVICES` and `PLANS` in the same script. Add " · Insured" to `LEGAL` only once the liability policy is active.
The print flyer is `qfs/flyer.pdf`, with `qfs/flyer.png` for posting. To put your number on it, run `node qfs/build_flyer.js "(704) 555-1234"`.
