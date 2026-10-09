#!/bin/sh
# Wrap each app's page.html into a standalone index.html for any static host.
cd "$(dirname "$0")"
for dir in funnel scale shop qfs; do
  { echo '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"></head><body>'; cat "$dir/page.html"; echo '</body></html>'; } > "$dir/index.html"
done
