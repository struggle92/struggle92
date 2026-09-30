#!/bin/sh
# Wrap funnel/page.html into a standalone funnel/index.html for any static host.
cd "$(dirname "$0")/funnel"
{ echo '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"></head><body>'; cat page.html; echo '</body></html>'; } > index.html
