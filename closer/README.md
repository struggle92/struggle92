# Closer

A private, single-file intimacy guide for a couple — positions with step-by-step
how-tos, tips, difficulty levels, a "Surprise Us" random pick, and a date-night
spin wheel.

## Features

- **20 positions** (plus your own) across Easy / Medium / Adventurous, each with how-to steps, tips, and a vibe.
- **Search + filters** — difficulty, favorites, wishlist, tried.
- **Favorites** — tap the ♥ on any card.
- **Surprise Us** — random pick from the current filter/search.
- **Surprise Date Night** — shuffles a full plan: vibe, where to go, what to do, a little touch, and a nightcap position.
- **Spicy Dares** — a shuffle deck of playful prompts.
- **Position Wheel** — spin to let it choose, with its own filters.
- **Add Your Own** — add positions, date ideas, and dares; they merge into everything and sync between partners.
- **Journal** — a shared history of what you've tried (with dates and ratings) and a shared wishlist of what you want to try.
- **Shared log** — mark tried, "want to try", rate 1–5 stars, and keep notes.

## How the log syncs

- **Opened inside Claude** (the published artifact): the log (favorites, tried,
  ratings, notes) is stored in the artifact's shared database, so both partners
  see each other's changes live. To let a second person write, the owner invites
  them by email as an editor/contributor from the artifact's Share menu (not via
  a public link).
- **Opened anywhere else** (e.g. a static host like this file on its own): there
  is no Claude runtime, so the app falls back to the browser's `localStorage` and
  the log is saved on that one device only. The header shows which mode is active.
- Theme choice is always per-device. No third-party servers are involved either way.

## Run it

It is one self-contained file. Open `index.html` in any browser, or host it for
free on GitHub Pages, Vercel, or Netlify. The only external request is the Google
Fonts stylesheet; everything else is inline.
