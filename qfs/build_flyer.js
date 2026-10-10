// Renders qfs/flyer.html to flyer.pdf (print) and flyer.png (social).
// Usage: node qfs/build_flyer.js "(704) 555-1234"   (needs: npm i playwright)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const phone = process.argv[2] ? `?phone=${encodeURIComponent('Text: ' + process.argv[2])}` : '';
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 816, height: 1056 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'flyer.html') + phone, { waitUntil: 'networkidle' });
  await p.pdf({ path: path.join(__dirname, 'flyer.pdf'), width: '8.5in', height: '11in', printBackground: true });
  await p.screenshot({ path: path.join(__dirname, 'flyer.png') });
  await b.close();
})();
