import os,json
CTA='<div class="big" style="font-size:96px">Overnight Pimple Patches</div><div style="margin:60px 0">'+''.join(f'<span class="dot" style="width:{s}px;height:{s}px;margin:0 18px"></span>' for s in (110,150,190))+'</div><div class="sub">36 clear patches · 3 sizes · $14.99<br>Free US shipping over $25</div><div class="pill">Link in bio 🔗</div>'
def num(n,t,s): return f'<div class="num">{n}</div><div class="mid">{t}</div><div class="sub">{s}</div>'
C={
"1-stop-doing":[
 '<div class="big">5 things to STOP doing to a pimple</div><div class="sub">#3 is the one everyone does</div><div class="swipe">swipe →</div>',
 num(1,"Squeezing it","Pushes bacteria deeper and can leave a mark that lasts for weeks."),
 num(2,"Touching it all day","Your hands carry oil and dirt straight to it."),
 num(3,"Piling on makeup","Thick layers trap more gunk on top of it."),
 num(4,"Drying it out with 5 products","Over-drying irritates the skin around it."),
 num(5,"Leaving it uncovered overnight","You pick in your sleep without noticing."),
 '<div class="mid">Do this instead:</div><div class="sub">Cover it with a hydrocolloid patch before bed. It protects the spot, soaks up gunk and keeps your fingers off.</div>',
 CTA],
"2-size-guide":[
 '<div class="big">Which pimple patch size do you need?</div><div class="sub">Most people pick wrong</div><div class="swipe">swipe →</div>',
 '<span class="dot" style="width:260px;height:260px"></span><div class="mid" style="margin-top:70px">8mm</div><div class="sub">Tiny whiteheads and small spots. The one you can wear to work.</div>',
 '<span class="dot" style="width:340px;height:340px"></span><div class="mid" style="margin-top:70px">10mm</div><div class="sub">Your everyday spot. You\'ll use this size most.</div>',
 '<span class="dot" style="width:420px;height:420px"></span><div class="mid" style="margin-top:70px">12mm</div><div class="sub">Bigger, angry spots. Fully cover the red area.</div>',
 '<div class="mid">The rule:</div><div class="sub">Pick the <b>smallest</b> patch that covers the whole spot. Too small and the edges lift. Too big and it shows.</div>',
 CTA],
"3-myths":[
 '<div class="big">Pimple patch myths vs facts</div><div class="swipe">swipe →</div>',
 '<div class="card"><div class="mid x">MYTH</div><div class="sub">"Patches cure acne."</div><div class="mid ok" style="margin-top:50px">FACT</div><div class="sub">They cover and protect individual spots. For ongoing acne, see a dermatologist.</div></div>',
 '<div class="card"><div class="mid x">MYTH</div><div class="sub">"The white stuff means it didn\'t work."</div><div class="mid ok" style="margin-top:50px">FACT</div><div class="sub">White means the hydrocolloid absorbed fluid. That\'s the material doing its job.</div></div>',
 '<div class="card"><div class="mid x">MYTH</div><div class="sub">"Put it on a dry, flat bump."</div><div class="mid ok" style="margin-top:50px">FACT</div><div class="sub">They work best on spots that have come to a head.</div></div>',
 '<div class="card"><div class="mid x">MYTH</div><div class="sub">"1 hour is enough."</div><div class="mid ok" style="margin-top:50px">FACT</div><div class="sub">Leave it 6+ hours. Overnight is easiest.</div></div>',
 CTA],
"4-night-routine":[
 '<div class="big">My 4-step "pimple tonight, date tomorrow" routine</div><div class="swipe">swipe →</div>',
 num(1,"Gentle wash","Lukewarm water and a mild cleanser. No scrubbing."),
 num(2,"Pat totally dry","Patches won't stick to damp skin."),
 num(3,"Patch it","Press on for 5 seconds. Pick the size that covers it."),
 num(4,"Sleep. Peel in the AM.","Toss the patch and move on with your day."),
 CTA],
"5-price":[
 '<div class="big">Stop paying $0.40+ per pimple patch</div><div class="sub">Do the math with me</div><div class="swipe">swipe →</div>',
 '<div class="card"><div class="mid">Typical drugstore box</div><div class="sub">~36 patches for $13–17<br><b>≈ $0.36–0.47 per patch</b></div></div>',
 '<div class="card"><div class="mid">Our 1 case</div><div class="sub">36 patches for $14.99<br><b>≈ $0.42 per patch</b></div></div>',
 '<div class="card" style="outline:10px solid #3b2a26"><div class="mid">Our 3-case bundle</div><div class="sub">108 patches for $29.99<br><b>≈ $0.28 per patch</b><br>+ free shipping</div></div>',
 CTA],
"6-no-picking":[
 '<div class="big">How I finally stopped picking my face</div><div class="swipe">swipe →</div>',
 '<div class="mid">Picking is a habit, not a choice</div><div class="sub">Most people do it without noticing: on the phone, in bed, at red lights.</div>',
 '<div class="mid">So make it physically impossible</div><div class="sub">A clear patch covers the spot. Your fingers hit plastic, not skin.</div>',
 '<div class="mid">Keep them everywhere</div><div class="sub">Nightstand. Bag. Car. Gym locker. Do it before the urge hits.</div>',
 '<div class="mid">Give it 2 weeks</div><div class="sub">The less you touch, the less you want to touch.</div>',
 CTA],
}
for name,slides in C.items():
    os.makedirs(f"carousels/{name}",exist_ok=True)
    for i,b in enumerate(slides,1):
        open(f"carousels/{name}/{i}.html","w").write(f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../../style.css"></head><body>{b}</body></html>')
json.dump({k:len(v) for k,v in C.items()},open("carousels/index.json","w"))
