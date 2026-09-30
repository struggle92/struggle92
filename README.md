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
