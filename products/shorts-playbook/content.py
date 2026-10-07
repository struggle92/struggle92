"""All written content for the Faceless Shorts Playbook. Edit here, then run build_playbook.py."""

TITLE = "The Faceless Shorts Playbook"
SUBTITLE = "30 Shorts in 30 days. No face, no gear, free apps only."

START_HERE = [
    "This playbook gives you one system: pick a niche, use five faceless formats, open every video "
    "with a tested hook, edit in under 30 minutes with free apps, post daily for 30 days, and review "
    "once a week.",
    "Read it once in about 45 minutes. Then keep three pages open while you work: the hook bank, the "
    "30-day calendar and the batch-day checklist.",
    "<b>An honest note before you start.</b> Most new Shorts channels get very few views in the first "
    "weeks, and most people who post short-form video earn little or nothing from it. Views and money "
    "depend on your niche, your consistency and platform rules that change often. What this playbook "
    "does is get you posting consistently with videos that are built correctly, which is the part "
    "most people never get past.",
]

NICHE_INTRO = (
    "Your niche is the topic you'll post about for the next 90 days. The right niche is one you can "
    "make 90 videos about without running out of ideas, and one where viewers can act on what you show "
    "them (buy a tool, try a recipe, save money). Score each idea from 1 to 5 on each question below. "
    "Pick the highest total. A tie goes to the one you'd enjoy more."
)
NICHE_QUESTIONS = [
    "Can I list 30 video ideas for this in 15 minutes?",
    "Do I already know more about it than a beginner?",
    "Are there products, apps or services people buy in this niche?",
    "Do faceless channels in this niche get views? (search it on Shorts and TikTok)",
    "Would I still be making these videos in month three?",
]

FORMATS = [
    ("1. List / countdown",
     "On-screen text counts through 3 to 5 items over stock footage, screenshots or simple graphics.",
     "Viewers stay to see the last item. Lists are easy to script and easy to batch.",
     "Hook (0-2s) > item 1 > item 2 > item 3 > best item last > call to action.",
     "\"3 free apps that replace ones you pay for. Number 3 saved me $120 a year.\""),
    ("2. Screen-record tutorial",
     "Record your phone or computer screen while you show how to do one specific task.",
     "It's useful, so people save and share it, and saves tell the platform to push the video.",
     "Show the result first (0-2s) > the steps, sped up > the result again > call to action.",
     "\"Turn this iPhone setting on and your battery lasts longer.\" Then record yourself doing it."),
    ("3. Text-story over B-roll",
     "A short story told entirely in on-screen text, over calm footage such as driving, cooking or city scenes.",
     "People read to the end to find out what happened, which raises watch time.",
     "Tension in line one > 3 to 5 lines of story > a twist or lesson > a question for comments.",
     "\"My boss said I'd never get promoted. Six months later...\""),
    ("4. Voiceover explainer",
     "You narrate a short explanation over stock clips, screenshots or simple animations. Your voice, not your face.",
     "A voice builds trust faster than text, and you can make a lot of these from one research session.",
     "Bold claim (0-3s) > why it's true > one example > what to do about it.",
     "\"The 50/30/20 rule, explained in 30 seconds.\""),
    ("5. Hands-only demo",
     "Film only your hands doing something: cooking, unboxing, writing, building, cleaning.",
     "It feels real, it's satisfying to watch, and you never show your face.",
     "Finished result (0-1s) > the process in quick cuts > the result again > call to action.",
     "\"A $6 dinner that feeds four.\" Overhead shot of your hands cooking."),
]

HOOK_RULES = [
    "<b>Say the payoff in the first two seconds.</b> Promise one specific result and deliver it.",
    "<b>Put the hook on screen as text too.</b> Many people scroll with the sound off.",
    "<b>Start mid-action.</b> Cut every \"hey guys\", logo and slow intro.",
    "<b>Be specific.</b> \"3 apps\" beats \"some apps\" and \"$120 a year\" beats \"money\".",
    "<b>Keep the promise.</b> A hook the video doesn't deliver loses viewers and trust.",
]

HOOK_FORMULA = (
    "<b>The formula:</b> [Specific number or result] + [who it's for or what it stops] + [a reason to "
    "stay]. For example: \"3 apps (number) that replace ones you pay for (result). Number 3 saved me "
    "$120 a year (reason to stay).\""
)

HOOKS = {
    "Money": [
        "Stop doing [habit] if you want to save $[amount] this year.",
        "3 money rules I wish I knew at [age].",
        "The subscription you forgot you're paying for.",
        "I tracked every dollar for 30 days. Here's where it went.",
        "One habit that quietly keeps people broke.",
        "How to [money goal] on a $[amount] paycheck.",
        "Don't open a [account type] until you watch this.",
        "[Number] side hustles you can start with $0 this weekend.",
        "The 50/30/20 rule, explained in 30 seconds.",
        "What I'd do with my first $1,000 if I started over.",
    ],
    "Fitness": [
        "Do this before every workout if your [body part] hurts.",
        "3 exercises that are wasting your time at the gym.",
        "I did [exercise] every day for 30 days. Here's what changed.",
        "The easiest high-protein breakfast you can make in 5 minutes.",
        "You're doing [exercise] wrong. Here's the fix.",
        "No gym? Here's a 10-minute [goal] workout.",
        "What [amount] grams of protein actually looks like on a plate.",
        "Stop stretching like this before you run.",
        "Beginner mistake number one at the gym.",
        "If you only have 20 minutes, do this.",
    ],
    "Cooking": [
        "A $[amount] dinner that feeds [number].",
        "Stop throwing out [ingredient]. Do this instead.",
        "3 ingredients, 10 minutes, almost no dishes.",
        "The restaurant trick for [dish] nobody tells you.",
        "What I meal prep for a week on $[amount].",
        "You've been cutting [food] wrong.",
        "The air fryer recipe I make every single week.",
        "Turn leftover [food] into [new dish].",
        "One-pan [dish] for nights you can't be bothered.",
        "Rate this $[amount] grocery haul.",
    ],
    "Tech": [
        "Your phone can do this and you didn't know.",
        "[Number] free apps that replace ones you pay for.",
        "Turn this setting off right now.",
        "The [app] shortcut that saves me an hour a week.",
        "Stop paying for [software]. Use this free one.",
        "How to [task] in 10 seconds.",
        "I asked AI to [task]. Here's what happened.",
        "3 browser extensions I use every single day.",
        "Your [device] battery dies fast because of this.",
        "Hidden [iPhone/Android] feature: [feature].",
    ],
    "Motivation": [
        "Nobody's coming to save you. Here's what to do instead.",
        "Read this if you feel behind in life.",
        "The 2-minute rule that ended my procrastination.",
        "What I'd tell my 20-year-old self.",
        "Discipline isn't what you think it is.",
        "If you're starting over at [age], watch this.",
        "One habit that changed my mornings.",
        "Stop waiting to feel ready.",
        "3 signs you're closer than you think.",
        "Do this when you don't feel like doing anything.",
    ],
    "Local": [
        "[Number] spots in [city] locals keep to themselves.",
        "Best [food] in [city] under $[amount].",
        "Things to do in [city] this weekend.",
        "I tried every [food] spot on [street]. Here's the winner.",
        "Free things to do in [city].",
        "Moving to [city]? Watch this first.",
        "The most underrated [place] in [city].",
        "[City] date night ideas under $[amount].",
        "What $[amount] gets you at [local place].",
        "Rating [city]'s [food] spots out of 10.",
    ],
}

WORKFLOW = [
    ("Step 1. Script (5 min)",
     ["Pick today's idea from the calendar and a hook from the hook bank.",
      "Write 4 to 6 short lines. One idea per line. Read it aloud: aim for 20 to 40 seconds.",
      "End with one call to action: follow, save, or comment a word."]),
    ("Step 2. Gather footage (5 min)",
     ["Screen-record, film your hands, or pull free clips from Pexels or Pixabay (check each site's license).",
      "Film vertical, in good daylight, with your phone lens wiped clean.",
      "Grab two or three more clips than you think you need."]),
    ("Step 3. Edit in CapCut (10 min)",
     ["Start a new project and drop clips in order. Trim every pause and \"um\".",
      "Record a voiceover in the app or add text lines one at a time.",
      "Add auto captions (look for Captions or Text, then Auto captions). Check spelling; auto captions get names wrong.",
      "Keep each shot between 1 and 3 seconds. A cut every couple of seconds keeps attention.",
      "Use music from the app's own library, or the platform's sound library when you post, so you stay within licensing."]),
    ("Step 4. Design in Canva (5 min, optional)",
     ["Make a 1080 x 1920 design for a title card, list graphics or a cover frame.",
      "Save one branded template (fonts, colors, logo spot) and duplicate it for every video.",
      "Download as MP4 or PNG and drop it into CapCut."]),
    ("Step 5. Export and post (5 min)",
     ["Export at 1080 x 1920 (9:16), 30 fps. Higher frame rates make bigger files for little gain.",
      "Write a title or caption that repeats the hook in plain words, plus 2 or 3 relevant hashtags.",
      "Upload the same video natively to YouTube Shorts, TikTok, Instagram Reels and Facebook Reels. "
      "Export from CapCut without a watermark where the app allows it, since some platforms limit reach for reposted, watermarked clips."]),
]

SAFE_ZONES = (
    "<b>Safe zones.</b> Each app covers parts of the screen with buttons and captions. Keep important text "
    "inside the middle of the frame: stay out of roughly the top 10%, the bottom 20% and the right-hand 15%. "
    "Before posting, preview the video in the app and check that nothing is hidden behind the like button or caption."
)

# (day, format, idea, hook bank tip)
CALENDAR = [
    (1, "List", "3 mistakes beginners make in [niche]", "Use a \"Stop doing\" hook"),
    (2, "Text-story", "The moment I realized [lesson about niche]", "Tension in line one"),
    (3, "Tutorial", "How to [basic task] in under 60 seconds", "\"How to [task] in X seconds\""),
    (4, "Voiceover", "Why [common belief in niche] is wrong", "Bold claim first"),
    (5, "Hands-only", "Watch me [simple task] start to finish", "Show the result first"),
    (6, "List", "5 tools I use every week for [niche]", "Number + payoff"),
    (7, "Review", "Weekly review. Repost your best video with a new hook", "Swap the first line only"),
    (8, "Tutorial", "The [tool] setting most people never change", "\"Turn this on/off right now\""),
    (9, "Voiceover", "[Niche term] explained in 30 seconds", "\"Explained in 30 seconds\""),
    (10, "List", "3 things nobody tells you about [niche]", "\"Nobody tells you\""),
    (11, "Hands-only", "Before and after: [result]", "Show the after first"),
    (12, "Text-story", "I tried [niche thing] for 7 days. Here's what happened", "\"I tried X\""),
    (13, "List", "[Number] cheap or free alternatives to [expensive thing]", "Price in the hook"),
    (14, "Review", "Weekly review. Make a part 2 of your top video", "\"Part 2\" in the hook"),
    (15, "Tutorial", "Beginner's first step in [niche]", "\"If you're starting at zero\""),
    (16, "Voiceover", "The biggest myth in [niche]", "\"Stop believing\""),
    (17, "Hands-only", "My [niche] setup / routine", "\"What my X looks like\""),
    (18, "List", "Rate these [niche items] out of 10", "Ask viewers to disagree"),
    (19, "Text-story", "A comment that changed how I think about [niche]", "Quote the comment"),
    (20, "Tutorial", "Fix this common [niche] problem in 3 steps", "\"You're doing X wrong\""),
    (21, "Review", "Weekly review. Answer your best comment in a video", "Show the comment on screen"),
    (22, "List", "What I'd do if I started [niche] again", "\"If I started over\""),
    (23, "Voiceover", "[Number] numbers every [niche] beginner should know", "Specific number"),
    (24, "Hands-only", "Satisfying [niche] process, sped up", "No talking, strong first frame"),
    (25, "Tutorial", "The fastest way to [task]", "\"In 10 seconds\""),
    (26, "Text-story", "My biggest [niche] mistake (and what it cost)", "Cost in line one"),
    (27, "List", "[Niche] products worth the money vs. not", "\"Worth it or not\""),
    (28, "Review", "Weekly review. Remake your weakest video with a new hook", "Change the first 2 seconds"),
    (29, "Voiceover", "Answer: the most common question in [niche]", "Ask the question as the hook"),
    (30, "List", "What I learned posting 30 days in a row", "\"30 days\" in the hook"),
]

BATCH_DAY = [
    "Pick 7 ideas from the calendar and assign a hook to each.",
    "Write all 7 scripts in one sitting (about 35 minutes).",
    "Film or record all footage in one session. Change your shirt or background between videos if your hands are on camera.",
    "Edit all 7 in CapCut with the same caption style and template.",
    "Name files Day01, Day02 and so on so you never post one twice.",
    "Schedule them, or set a daily phone alarm to post at the same time each day.",
    "Rough time: one afternoon of 3 to 4 hours for a whole week of videos.",
]

MONETIZATION = [
    ("YouTube Partner Program",
     "Pays a share of ad revenue, including from Shorts, once your channel meets the subscriber and view "
     "requirements and is approved. The thresholds change, so check the current ones.",
     "support.google.com/youtube/answer/72851"),
    ("TikTok Creator Rewards Program",
     "Pays for qualifying videos, which have generally needed to be longer than one minute, once your "
     "account meets follower, view and age requirements. Rules and regions change often.",
     "TikTok Help Center: search \"Creator Rewards Program\""),
    ("Facebook and Instagram",
     "Meta runs content monetization programs for Reels that change often and are invite-only in some regions.",
     "Professional Dashboard > Monetization in the Facebook or Instagram app"),
    ("Affiliate links",
     "You earn a commission when viewers buy through your link. This can work from your first video, before "
     "you qualify for any platform program. Options include Amazon Associates and the affiliate programs most "
     "apps and tools run.",
     "affiliate-program.amazon.com"),
    ("Disclose every paid link",
     "In the US the FTC requires a clear disclosure when you earn from a link or were paid or gifted a product. "
     "Say it in the video or put it at the top of the caption, for example \"#ad\" or \"I earn from this link\".",
     "ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers"),
    ("Your own product",
     "Once people ask the same questions in your comments, package the answers into a checklist, template or "
     "guide and link it in your bio. This is often the highest-margin option.",
     "Gumroad, Payhip, Stan or Shopify"),
]

REVIEW_QUESTIONS = [
    "Which video had the highest average view duration or percentage viewed? Why do I think it worked?",
    "Which video had the lowest? Was it the hook, the topic or the pacing?",
    "Which format performed best this week?",
    "What did people ask or argue about in the comments?",
    "Repeat: one thing I'll do again next week.",
    "Drop: one thing I'll stop doing.",
    "Test: one new hook or format I'll try.",
]

STATS_COLS = ["Video", "Views", "Avg % viewed", "Likes", "Saves/shares", "New followers"]

FINAL = [
    "Post for 30 days before judging the results. Early numbers swing a lot.",
    "Change one thing at a time so you know what made the difference.",
    "Your first 10 videos teach you to make videos. Your next 20 teach you what your audience wants.",
    "Never buy views, followers or engagement. It breaks platform rules and wrecks your reach.",
]
