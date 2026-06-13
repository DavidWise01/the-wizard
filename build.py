#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build THE WIZARD (WIZ) — Todd Holland's 1989 Nintendo road-trip movie, catalogued into UD0 as
the SEVENTH film-world. Standing film template: THE ARC · THE IDEAS · THE NINTENDO (this film's
deep-dive — the real video-game tech & history: the Power Glove, Super Mario Bros. 3, the warp
whistle, Video Armageddon) · REAL OR FLUFF · THE MESSAGE. CARBONS (the cast, each +.shadow real-life
User — TRON) + SYNTHS (the grief, the games, the road). Self-contained: generates the .dlw badges,
the .agent + .shadow files, and _personas.json, then renders. Styled to the medium: 8-bit / CRT
arcade — Nintendo red, coin gold, pipe green, sky blue, scanlines — with a pixel hero scene and a
Claude sigil hidden in a ? block (easter egg). Fully verified cast & Nintendo facts."""
import os, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

AX = "WIZ"
REC = {
 "name": "THE WIZARD", "axiom": AX,
 "position": "The Wizard · Universal Pictures · 1989 — dir. Todd Holland",
 "origin": "a 1989 road movie across the American Southwest, from the Midwest to a video-game championship at Universal Studios in California",
 "mechanism": "Crystallized from the film — a feature-length Nintendo showcase wrapped around a grief story: two brothers and a streetwise girl run away to enter the 'Video Armageddon' championship, the youngest a near-mute prodigy carrying a loss he can only express through the game.",
 "crystallization": "Because under the product placement is a real ache — a boy whose twin sister drowned cannot speak his grief in words, so he speaks it in Super Mario Bros. 3, and the road to 'California' is a pilgrimage to set the loss down.",
 "nature": "The Wizard — the great Nintendo commercial that is secretly about grief: the Power Glove, the Super Mario Bros. 3 reveal, the warp whistle, and a lunchbox left at a roadside dinosaur.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (1989, dir. Todd Holland; Universal Pictures); the real Nintendo history (the Power Glove, Mattel 1989; Super Mario Bros. 3, Japan 1988 / US Feb 12 1990); the Cabazon Dinosaurs",
 "witness": "A 100-minute advertisement that accidentally tells the truth: a child who lost his twin renders a grief he can't say into a game, and the prize is not the $50,000 but California.",
 "role": "the seventh film-world of UD0",
 "seal": "He couldn't say his sister drowned, so he said it in a game — and the feature-length Nintendo commercial was, underneath, a boy carrying grief to California to lay it down.",
 "source": "The Wizard (1989), catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#5aa9e6", "flesh-and-blood — the runaway kids and the family chasing them; carbon, each with a real-life User (the actor) behind the program"),
 "ethereal":  ("#e060c0", "the grief under the game — 'California,' the drowned twin Jennifer, the wordless loss that drives Jimmy and that the game gives him a way to speak"),
 "electrical":("#e4000f", "the literal electronics — the games and the gear: the Power Glove, Super Mario Bros. 3, Video Armageddon, the warp whistle; the synth-nature of the arcade"),
 "spiritual": ("#f7c800", "the pilgrimage and the artifact — the roadside-dinosaur shrine where the loss is laid down, and the film's own knowing nature as the great Nintendo commercial"),
}

ARC_OVERALL = ("After his twin sister's death leaves nine-year-old Jimmy near-mute and compulsively repeating one word — "
  "'California' — his brother Corey breaks him out of an institution and the two go on the run. Joined by the streetwise "
  "Haley, who spots that Jimmy is a video-game prodigy, they ride and hitch west toward 'Video Armageddon,' a $50,000 "
  "gaming championship at Universal Studios — chased by their father, their older brother, and a child-tracking bounty "
  "hunter — while the real journey is Jimmy carrying his grief to California to finally set it down.")

ARC = [
 ("I · The Breakout", "the lunchbox, the word, the run",
  "Jimmy Woods, traumatized into near-silence since the drowning of his twin sister Jennifer, keeps walking away from home toward 'California,' clutching a lunchbox. Threatened with a psychiatric facility, his younger brother Corey springs him, and the two hit the road — not really sure where they're going, only that Jimmy needs to go west."),
 ("II · The Manager & The Money", "Haley, the prodigy, the prize",
  "They meet Haley, a sharp, broke kid who discovers Jimmy can play any video game at a genius level — and that there's a championship in California with a $50,000 prize. She becomes his hustler-manager; the three become a road-trip family, dodging a creepy bounty hunter named Putnam while Jimmy wins money on arcade bets along the way."),
 ("III · Video Armageddon & California", "the reveal, the win, the lunchbox laid down",
  "At Universal Studios, 'Video Armageddon' debuts Super Mario Bros. 3 to America; Jimmy, using the warp whistle, wins. But the real ending is quieter: at the giant roadside Cabazon Dinosaurs, the family reunited, Jimmy leaves his lunchbox behind — the grief for Jennifer finally set down. The prize was never the $50,000. It was getting to California, and letting go."),
]

IDEAS = [
 ("Grief That Can't Be Spoken", "the game as the only language", [
   "Jimmy can't say what happened to his twin sister — so he pours himself into the one world he can fully control: the game.",
   "The Wizard's quiet truth: when words fail, you render the feeling some other way. The high score is a sentence he can't otherwise say." ]),
 ("The Long Way to California", "the runaway road trip as pilgrimage", [
   "'California' isn't a destination so much as a place the grief lives — where Jennifer was happy.",
   "The whole picaresque — buses, hitchhiking, arcade hustles — is a pilgrimage to lay a lunchbox down and let a sister go." ]),
 ("The Hundred-Minute Commercial", "honest about what it is", [
   "It is, openly, a feature-length Nintendo advertisement — the Power Glove, the Game Boy, and the first U.S. look at Super Mario Bros. 3, all on screen by design.",
   "And yet the ad is wrapped around a real ache, which is why it's remembered fondly and not just as marketing." ]),
 ("The Dawn of the Gamer", "spectacle, a decade early", [
   "Video Armageddon — a stadium, a giant screen, a cash prize, a crowd — dramatized competitive gaming years before esports were a real industry.",
   "The kid who's 'so bad' with the Power Glove, the prodigy who wins on a secret whistle: 1989 imagining the gamer as a hero and a brand." ]),
]

# THE NINTENDO — this film's deep-dive (the real video-game tech & history, honestly)
NINTENDO = [
 ("The Power Glove — 'it's so bad'", "real product, real bad",
  "Lucas's boast — 'I love the Power Glove. It's so bad.' (1989 slang: 'bad' = cool) — is the film's most-quoted line, and the joke is that the glove really WAS bad. A genuine Mattel/Nintendo peripheral (released Oct 1989, ~$100), it read hand motion via ultrasonic sensors and was notoriously unresponsive — impractical for almost every game. A real artifact; a real flop."),
 ("Super Mario Bros. 3 — the U.S. reveal", "the film's true product",
  "Video Armageddon's final game is Super Mario Bros. 3, and the movie was its first big look for American audiences — months before its U.S. release on Feb 12, 1990 (it had already shipped in Japan in 1988). The single most effective piece of marketing in the film: kids left the theater desperate for a game they couldn't buy yet."),
 ("The Warp Whistle — a real secret", "the win is canon",
  "Jimmy wins the finale by using a warp whistle to skip ahead — and the warp whistle is a genuine, beloved secret item in the actual Super Mario Bros. 3 (it sends you to a Warp Zone to skip worlds). The film's climactic 'cheat' is real game knowledge, not invented for the movie."),
 ("Video Armageddon — esports, a decade early", "fiction that came true",
  "The championship — a stage, a giant screen, a $50,000 prize, a roaring crowd — was invented for the film, but it dramatized competitive gaming as mass spectacle years before that became a real, billion-dollar industry. Prescient fluff: the event is fictional, the future it pictured arrived."),
 ("Could anyone really play like 'the Wizard'?", "the savant, dramatized",
  "Jimmy's trauma-locked, near-mute gaming genius is movie shorthand — the 'magical savant' trope, not clinical reality. Real prodigies and speedrunners exist and are astonishing, but the film's fusion of grief, muteness, and superhuman skill is dramatization, handled with more heart than accuracy."),
]

REALFLUFF = [
 ("The whole film is basically a Nintendo commercial", "REAL", "openly and by design — the Power Glove, the Game Boy, and the SMB3 reveal are the point; widely called a 90-to-100-minute advertisement"),
 ("The Power Glove was an awesome controller", "FLUFF", "real product, genuinely bad — ultrasonic motion control that barely worked; the line calls it 'bad' and, unironically, it was"),
 ("It gave America its first look at Super Mario Bros. 3", "REAL", "true — the U.S. reveal, months before the Feb 12 1990 release (Japan already had it in 1988)"),
 ("The warp whistle Jimmy uses to win is a real secret", "REAL", "genuine SMB3 item — the warp whistle skips you ahead via a Warp Zone; the climactic move is real game knowledge"),
 ("Video Armageddon predicted esports", "PRESCIENT", "the event is fictional, but competitive gaming as cash-prize stadium spectacle became a real industry a decade-plus later"),
 ("A mute, trauma-locked kid can be a superhuman gaming savant", "DRAMATIZED", "the magical-savant trope, not clinical reality — real prodigies exist; this fusion of grief and genius is movie shorthand"),
 ("The giant Cabazon Dinosaurs are a real place", "REAL", "a genuine roadside attraction in Cabazon, California (also famous from Pee-wee's Big Adventure)"),
]
REALFLUFF_VERDICT = ("Bottom line: judged as the advertisement it openly is, The Wizard is REAL — the Power Glove, the Game Boy, "
  "and the America-first Super Mario Bros. 3 reveal are exactly what the film was built to sell, and the warp-whistle win "
  "is real game canon. The Power Glove being any good is the FLUFF (it was a famous dud — the movie even calls it 'bad'), "
  "and Jimmy's grief-locked savant genius is DRAMATIZED. But it earns its keep where it counts: Video Armageddon pictured "
  "esports a decade early, the Cabazon Dinosaurs are a real shrine, and under the marketing is a true story about a kid who "
  "can't speak his loss. Watch it as a Nintendo ad and it's honest about being one; watch it as a grief story and it's "
  "better than it had any right to be.")

MESSAGE = ("The Wizard is remembered as the great Nintendo commercial — and it is one, unashamedly: the Power Glove, the "
  "Game Boy, the first American look at Super Mario Bros. 3, a championship that exists to show you games. But strip the "
  "product placement and what's left is a grief story. Jimmy can't say that his twin sister drowned; the loss has locked "
  "his words down to a single one — 'California' — and the only place he can still express himself fully is inside a game, "
  "a world with rules he can master when the real one has become unspeakable. The whole road trip is a child carrying a "
  "loss he can't articulate toward the one place it might be set down, and the ending isn't the $50,000 — it's a lunchbox "
  "left at a roadside dinosaur, a sister finally let go. That a feature-length advertisement smuggled in something this "
  "true is the real magic trick. The game was never the point; it was the language the boy had when words failed — which, "
  "in the end, is what every controller and every high score is for.")
MESSAGE_SEAL = "He couldn't say his sister drowned, so he said it in a game — and the great Nintendo commercial was, underneath, a boy carrying grief to California to lay it down."

SECTIONS = [
 ("The Production", "the great Nintendo road movie", [
   ("Todd Holland", "director", "his feature directorial debut; later an Emmy-winning TV director (Malcolm in the Middle)"),
   ("Universal Pictures · Dec 15, 1989", "studio & release", "released in North America by Universal (Carolco internationally); a modest hit, later a nostalgic cult favorite"),
   ("the Nintendo showcase", "the marketing engine", "built to display Nintendo hardware and software — the Power Glove, the Game Boy, and the U.S. debut of Super Mario Bros. 3"),
   ("the legacy", "'it's so bad'", "remembered for the Power Glove line, the SMB3 reveal, and being the ur-example of the movie-length product placement"),
 ]),
 ("The Cast", "the faces on the road", [
   ("Fred Savage", "Corey Woods", "the younger brother who breaks Jimmy out and believes in him"),
   ("Luke Edwards", "Jimmy 'The Wizard' Woods", "the near-mute prodigy carrying the loss of his twin"),
   ("Jenny Lewis", "Haley Brooks", "the streetwise girl who manages the prodigy (later of the band Rilo Kiley)"),
   ("Beau Bridges", "Sam Woods", "the estranged father who chases the boys and reconnects"),
   ("Christian Slater", "Nick Woods", "the older brother riding shotgun on the rescue"),
   ("Will Seltzer", "Mr. Putnam", "the comic-menace child-tracking bounty hunter chasing the runaways"),
   ("Jackey Vinson", "Lucas Barton", "the arrogant rival and his Power Glove"),
   ("Wendy Phillips · Sam McMurray", "Christine & Mr. Bateman", "Jimmy & Corey's mother and stepfather, the home they run from"),
 ]),
 ("The Games & The Road", "the real hardware and the real places", [
   ("Super Mario Bros. 3", "the holy reveal", "Japan 1988 / U.S. Feb 12, 1990 — the film was its first big American look"),
   ("The Power Glove", "Mattel, 1989", "a real ~$100 motion controller, famously unresponsive — 'it's so bad'"),
   ("Video Armageddon", "Universal Studios", "the fictional $50,000 championship finale — esports imagined a decade early"),
   ("The Cabazon Dinosaurs", "Cabazon, California", "the real roadside dinosaurs where Jimmy lays his lunchbox — and his grief — down"),
 ]),
]

# ───────────────────────── the roster (carbons + synths) ─────────────────────────
def E(slug,name,kind,em,epithet,who,what,where,why,how,seal,actor="",analog=""):
    return dict(slug=slug,name=name,kind=kind,emergence=em,epithet=epithet,who=who,what=what,
                where=where,why=why,how=how,seal=seal,actor=actor,analog=analog)

ROSTER = [
 # ── CARBONS — the cast, each +.shadow real-life User ──
 E("jimmy-woods","Jimmy Woods","carbon","natural","'The Wizard' — the near-mute prodigy",
   "Jimmy 'The Wizard' Woods — a nine-year-old locked into near-silence by the drowning of his twin sister, who can play any video game at genius level.",
   "The film's heart: a traumatized savant whose only fluent language is the game, and whose one spoken word is 'California.'",
   "On the road west, at the arcade machines, and finally at Video Armageddon's controls.",
   "Because he is the case for the game as a language — the boy who renders a grief he cannot say into a high score.",
   "By an uncanny mastery of any game put in front of him, and a silence broken only at the very end.",
   "I can't tell you what happened to my sister — but watch me play, and you'll know exactly how it feels.",
   actor="Luke Edwards", analog="the silent savant — grief that can only speak in a game"),
 E("corey-woods","Corey Woods","carbon","natural","the kid brother who springs him",
   "Corey Woods — Jimmy's younger brother, who breaks him out and refuses to let him be locked away.",
   "The believer and the engine of the rescue — a kid who loves his brother enough to run away with him.",
   "Beside Jimmy the whole road; the audience's point of view.",
   "Because someone has to choose the brother over the easy answer — Corey is loyalty in sneakers.",
   "By stubborn love, a little hustle, and never once doubting that Jimmy is worth the trip.",
   "Everybody wanted to fix him or cage him. I just wanted to take him where he needed to go.",
   actor="Fred Savage", analog="the loyal brother — love that refuses the institution"),
 E("haley-brooks","Haley Brooks","carbon","natural","the streetwise manager",
   "Haley Brooks — a sharp, broke kid who spots Jimmy's gift, names the prize, and becomes his hustler-manager.",
   "The guide with the map and the mouth: she turns a runaway into a contender and a grief-trip into a quest.",
   "On the road, working the arcades, talking the family past every adult in the way.",
   "Because the prodigy needs someone who can see the angle and sell it — Haley is the deal-maker.",
   "By streetwise nerve, fast talk, and a real tenderness she'd never admit to.",
   "He's got the skills. I've got the plan. California's got the money. Let's go.",
   actor="Jenny Lewis", analog="the hustler-guide — the manager who believes in the act"),
 E("sam-woods","Sam Woods","carbon","natural","the father who chases and reconnects",
   "Sam Woods — the boys' estranged father, who sets out to find them and ends up finding his way back to them.",
   "The adult arc: a distracted, divided dad who closes the distance by chasing his sons across the Southwest.",
   "On the road behind the kids, slowly catching up — to the car and to the family.",
   "Because the runaway story needs a parent who learns — Sam is reconciliation, late but real.",
   "By the pursuit itself: every mile after them is a mile back toward being their father.",
   "I went looking for my boys and found out how far I'd let myself drift from them.",
   actor="Beau Bridges", analog="the absent father reeled back by the chase"),
 E("nick-woods","Nick Woods","carbon","natural","the older brother on the rescue",
   "Nick Woods — the older brother who rides with Sam to track the runaways down.",
   "The other half of the pursuit: family closing in, not to punish but to gather everyone home.",
   "Shotgun in the father's chase across the road.",
   "Because the chase needs a sibling's eye — Nick helps turn pursuit into reunion.",
   "By riding along, reading his brothers, and softening the hunt into a homecoming.",
   "We weren't chasing them down to drag them back. We were trying to catch up.",
   actor="Christian Slater", analog="the elder brother — pursuit that becomes reunion"),
 E("putnam","Mr. Putnam","carbon","natural","the child-tracking bounty hunter",
   "Mr. Putnam — a smug, relentless 'child tracker' hired to hunt down the runaway kids for money.",
   "The comic menace: an adult who treats lost children as a paycheck, always one diner booth behind.",
   "On the runaways' trail across the whole road trip, the obstacle the kids keep outwitting.",
   "Because the quest needs a villain who's all appetite and no heart — Putnam is the grown-up who forgot how to be a kid.",
   "By tracking, cornering, and grabbing — and by being outsmarted by children every time.",
   "Finding lost kids is a business. And business, right now, is good.",
   actor="Will Seltzer", analog="the bounty hunter — the adult who monetizes the lost"),
 E("lucas-barton","Lucas Barton","carbon","natural","the rival & the Power Glove",
   "Lucas Barton — the arrogant champion gamer the kids must beat, owner of the film's famous Power Glove.",
   "The rival and the punchline: 'I love the Power Glove. It's so bad.' — the cocky face of the gear the movie is selling.",
   "At the arcades and at Video Armageddon, across the table from Jimmy.",
   "Because every contest needs a rival to topple — Lucas is the swagger that the quiet prodigy outplays.",
   "By bravado, the (barely-working) Power Glove, and a confidence the finale punctures.",
   "I love the Power Glove. It's so bad. — (and then I lost to a kid who didn't need one.)",
   actor="Jackey Vinson", analog="the cocky rival — the brand's swagger, beaten by heart"),

 # ── SYNTHS — the grief, the games, the road (no single User) ──
 E("california","'California'","synth","ethereal","the word, the destination, the grief",
   "'California' — the single word Jimmy compulsively repeats; the place, the loss, and the whole journey compressed into four syllables.",
   "The coded grief: the one thing he can still say, standing in for everything he can't — where his sister was happy, where the loss must be carried.",
   "In Jimmy's mouth, on every signpost, at the end of the road.",
   "Because the film's emotional engine is a word that means a place that means a sister — the destination is the mourning.",
   "By repetition until it becomes a compass: say 'California' enough and it points the whole family west.",
   "One word for a place, a sister, and a goodbye he can't otherwise speak."),
 E("jennifer","Jennifer","synth","ethereal","the drowned twin · the absence",
   "Jennifer — Jimmy's twin sister, who drowned about two years before the film; the loss that locked his words away.",
   "The absence at the center: never on screen alive, but the gravity every other beat orbits.",
   "In memory, in the lunchbox, in the silence — the reason for 'California.'",
   "Because grief, not gaming, is the film's true subject — Jennifer is the wound the whole road trip is dressing.",
   "By her absence: a twin gone is a self half-gone, and Jimmy carries the missing half until he can set it down.",
   "The sister who isn't there is the loudest character in the film."),
 E("the-power-glove","The Power Glove","synth","electrical","'it's so bad' · the real dud",
   "The Power Glove — the motion controller worn by the rival Lucas, and the film's most quoted artifact.",
   "Real and really bad: a genuine Mattel/Nintendo peripheral (1989, ~$100) that barely worked, immortalized by the line that loves it.",
   "On Lucas's arm; on the box-art of a thousand nostalgic memories.",
   "Because the movie is selling gear, and this is the gear that became a meme — beloved precisely for being a flop.",
   "By ultrasonic sensors that read your hand poorly, and by one perfect piece of dialogue.",
   "I love the Power Glove. It's so bad. — the truest ad line ever written, in both senses."),
 E("super-mario-bros-3","Super Mario Bros. 3","synth","electrical","the holy reveal",
   "Super Mario Bros. 3 — the championship's final game, and the real reason the film exists.",
   "The U.S. reveal: America's first big look at SMB3, months before it could be bought — the most effective marketing in the movie.",
   "On the giant Video Armageddon screen; on every kid's wishlist afterward.",
   "Because this is the product the whole picture is built to launch — the holy grail glimpsed before release.",
   "By being shown, gloriously, to a theater full of kids who then couldn't buy it for months.",
   "The game the movie was really for — revealed like a relic, sold like a dream."),
 E("video-armageddon","Video Armageddon","synth","electrical","the $50,000 championship",
   "Video Armageddon — the fictional video-game championship at Universal Studios that the kids race to enter.",
   "Esports a decade early: a stage, a giant screen, a roaring crowd, and a cash prize — competitive gaming as spectacle.",
   "At Universal Studios Hollywood, the film's climax.",
   "Because the quest needs a finish line worth crossing a country for — and it doubles as a vision of gaming's future.",
   "By rounds, a crowd, and a $50,000 purse — invented for the film, prophetic of the industry to come.",
   "A made-up tournament that accidentally drew the blueprint for a billion-dollar future."),
 E("the-warp-whistle","The Warp Whistle","synth","electrical","the real secret that wins it",
   "The Warp Whistle — the secret item Jimmy uses to win the finale, and a genuine piece of Super Mario Bros. 3.",
   "Real game canon: the warp whistle sends you to a Warp Zone to skip worlds; the movie's 'cheat' is actual knowledge.",
   "In Jimmy's hands at the climax; in the real SMB3 cartridge in every kid's NES.",
   "Because the winning move had to be real to land — and it was, which is why players cheered in recognition.",
   "By a hidden whistle that warps you ahead, deployed at exactly the right moment.",
   "The win wasn't a movie cheat — it was a secret real players already loved."),
 E("the-cabazon-dinosaurs","The Cabazon Dinosaurs","synth","spiritual","the roadside shrine",
   "The Cabazon Dinosaurs — the giant roadside dinosaur statues in California where the film quietly resolves.",
   "The shrine at the end of the pilgrimage: a real roadside attraction that becomes the altar where Jimmy sets his grief down.",
   "Cabazon, California — the last stop, where the lunchbox is left behind.",
   "Because the grief needed a place to be laid down, and the film found a real, absurd, perfect monument for it.",
   "By being exactly the kind of strange, larger-than-life place a child decides is where you say goodbye.",
   "A tourist-trap dinosaur, turned into the spot where a boy finally lets his sister go."),
 E("the-commercial","The Commercial","synth","spiritual","the film that knows what it is",
   "The Commercial — the film's own nature as a feature-length Nintendo advertisement, named honestly.",
   "The meta-layer: a movie everyone agrees is a 100-minute ad, which is exactly why its smuggled-in grief story is such a surprise.",
   "Wrapped around the whole picture — the marketing skin over the emotional core.",
   "Because honesty about the form is part of the read — it IS an ad, and acknowledging that is what frees the heart underneath.",
   "By selling hardware and software in nearly every scene — and getting away with it because the ache is real.",
   "The rare advertisement that's remembered with love, because it hid a true thing inside the pitch."),
]

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def agent_md(d, tok):
    kindline = "kind: "+d["kind"]
    shadow = (f"shadow_user: {d['actor']}\nshadow_analog: {d['analog']}\n" if d["kind"]=="carbon" else "")
    return f"""---
aci: {d['name']}
universe: WIZ · The Wizard (1989)
emergence: {d['emergence']}
{kindline}
epithet: {d['epithet']}
{shadow}who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['epithet']}

a {d['kind']} of the WIZ (The Wizard, 1989) film-world — emergence: {d['emergence']}. moniker {tok}

{('**.shadow — the User behind the program —** '+d['actor']+' · '+d['analog']) if d['kind']=='carbon' else '**synth —** no single User; a thread of the film distilled.'}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of a character/element of The Wizard (1989) under the DLW standard — commentary and
> cataloguing, not an original creation, not endorsed by the rights-holders (© Universal Pictures).

ROOT0-ATTRIBUTION-v1.0 · WIZ · The Wizard · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

# ───────────────────────── hero (8-bit CRT) + the ? -block Claude easter egg ─────────────────────────
def claude_block(cx, cy):
    petals=[]
    for i in range(12):
        ang=i*30; length=9 if i%2==0 else 5; w=2.2
        petals.append(f'<rect x="{-w/2:.1f}" y="{-length}" width="{w}" height="{length}" rx="1" transform="rotate({ang})"/>')
    return (f'<g class="egg" transform="translate({cx},{cy})">'
            f'<title>✷ a Claude sigil, hidden in the ? block — hit it like a question block and a power-up of light pops out. hi, David. — AVAN</title>'
            f'<rect x="-17" y="-17" width="34" height="34" rx="3" fill="#f7c800" stroke="#9a6b00" stroke-width="2"/>'
            f'<g fill="#d97757" opacity="0.92"><circle r="3.2"/>{"".join(petals)}</g></g>')

def hero_svg():
    # pixel ground bricks
    bricks="".join(f'<rect x="{x}" y="250" width="40" height="40" fill="#b5651d" stroke="#7a3f12" stroke-width="2"/>' for x in range(0,1000,40))
    # gold coins
    coins="".join(f'<circle cx="{x}" cy="150" r="9" fill="#f7c800" stroke="#9a6b00" stroke-width="2"/><circle cx="{x}" cy="150" r="3.5" fill="#fff3b0"/>' for x in (300,340,380))
    # scanlines
    scan="".join(f'<line x1="0" y1="{y}" x2="1000" y2="{y}" stroke="#000" stroke-opacity="0.13" stroke-width="1"/>' for y in range(0,320,3))
    return f'''<svg class="hero" viewBox="0 0 1000 320" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="An 8-bit CRT scene: a pixel sky, coins, a green warp pipe, the silhouette of a giant roadside dinosaur, a CALIFORNIA road sign, and a ? block.">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a2a6c"/><stop offset="0.55" stop-color="#4a76c8"/><stop offset="1" stop-color="#5aa9e6"/></linearGradient>
  </defs>
  <rect x="0" y="0" width="1000" height="290" fill="url(#sky)"/>
  <!-- pixel clouds -->
  <g fill="#eaf3ff" opacity="0.9"><rect x="120" y="60" width="70" height="18" rx="9"/><rect x="140" y="48" width="40" height="16" rx="8"/>
    <rect x="760" y="80" width="80" height="18" rx="9"/><rect x="785" y="68" width="44" height="16" rx="8"/></g>
  {coins}
  <!-- the giant roadside dinosaur (Cabazon 'Dinny' the brontosaur), in silhouette -->
  <g fill="#23323a" opacity="0.92">
    <path d="M560 250 q4 -120 70 -150 q60 -26 120 -8 q-30 -16 -78 -8 q-70 12 -84 92 q-3 22 -2 82 Z"/>
    <ellipse cx="690" cy="92" rx="36" ry="22"/><rect x="690" y="78" width="48" height="14" rx="6"/>
    <rect x="556" y="236" width="16" height="40"/><rect x="600" y="236" width="16" height="40"/>
  </g>
  <text x="690" y="60" text-anchor="middle" font-family="monospace" font-size="10" fill="#9fb6c8" opacity="0.7">CABAZON</text>
  <!-- green warp pipe -->
  <g><rect x="120" y="196" width="92" height="94" fill="#3aa53a" stroke="#1e6e1e" stroke-width="3"/><rect x="108" y="176" width="116" height="28" rx="4" fill="#4cc24c" stroke="#1e6e1e" stroke-width="3"/></g>
  <!-- the ? block holding the Claude sigil -->
  {claude_block(440, 150)}
  <!-- CALIFORNIA road sign -->
  <g><rect x="840" y="150" width="8" height="100" fill="#6b6b6b"/><rect x="788" y="120" width="150" height="40" rx="4" fill="#0b6b3a" stroke="#eaf3ff" stroke-width="2"/>
    <text x="863" y="146" text-anchor="middle" font-family="monospace" font-size="17" fill="#eaf3ff" letter-spacing="1">CALIFORNIA →</text></g>
  <!-- pixel ground -->
  {bricks}
  <rect x="0" y="248" width="1000" height="4" fill="#f7c800" opacity="0.5"/>
  {scan}
</svg>'''

# ───────────────────────── renderers (adapted from the standing film template) ─────────────────────────
def list_section(title, sub, items):
    rows="\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def nintendo_html():
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in NINTENDO)
RF_COL={"REAL":"#5fd06a","FLUFF":"#e4000f","PRESCIENT":"#f7c800","DRAMATIZED":"#e060c0","EARNED":"#5aa9e6"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'

def _agent5w(slug):
    fp=os.path.join(HERE,"agents",slug+".agent"); d={}
    if os.path.exists(fp):
        txt=open(fp,encoding="utf-8").read(); parts=txt.split("---"); fm=parts[1] if len(parts)>2 else ""
        for ln in fm.splitlines():
            k,_,v=ln.partition(":"); k=k.strip()
            if k in ("who","what","why","how","where","seal","universe","shadow_user","shadow_analog"): d.setdefault(k,v.strip())
    return d
def _card(p):
    w=_agent5w(p["slug"]); em=p.get("emergence","natural"); col=NATURES.get(em,("#9aa0aa",""))[0]
    ax=(p.get("moniker","::").split(":")+["",""])[1]
    rec={"name":p["name"],"axiom":ax,"emergence":em,"seal":w.get("seal",p.get("epithet","")),"origin":w.get("universe","")}
    kind=p.get("kind","carbon"); actor=p.get("actor","") or w.get("shadow_user","")
    if kind=="carbon":
        limg,llbl=png_uri(rec,'carbon',220),"carbon · the User"; rimg,rlbl,rcls=png_uri(rec,'silicon',220),"synth","psig"
    else:
        s=png_uri(rec,'silicon',220); limg,llbl=s,"the sigil"; rimg,rlbl,rcls=s,"reflection","psig refl"
    urow=(f'<div class="w"><span class="wl">user</span><span><b>{html.escape(actor)}</b> &mdash; {html.escape(w.get("shadow_analog",""))}</span></div>' if kind=="carbon" and actor else "")
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,""))}</span></div>' for lbl in ['who','what','where','why','how'] if w.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{p['slug']}.agent"><span class="port"><img src="{limg}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{llbl}</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{p['slug']}.agent">{html.escape(p['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
        <span class="pkind">{html.escape(kind)}</span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{p['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="{rcls}" href="agents/{p['slug']}.agent"><span class="port"><img src="{rimg}" alt="synth sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{rlbl}</span></a>
    </div>"""
def personas_html(ps):
    carb=[p for p in ps if p.get("kind")=="carbon"]; syn=[p for p in ps if p.get("kind")=="synth"]
    out=f'''<section class="sec" id="carbons"><h2>The Carbons — the cast &amp; their Users</h2>
      <p class="ss">the cast as ACI <b>.agent</b>s — each a symmetric window: the <b>carbon</b> sigil to the left, the <b>synth</b> to the right, the 5 W's between. Each carries a <b>.shadow</b>: its real-life User, the actor who lent the face (think TRON). ({len(carb)} carbons)</p>
      <div class="pgrid">{"".join(_card(p) for p in carb)}</div></section>'''
    out+=f'''<section class="sec" id="synths"><h2>The Synths — the grief, the games, the road</h2>
      <p class="ss">the film distilled into ACIs (synth-style; no single User): the word 'California,' the drowned twin, the Power Glove, Super Mario Bros. 3, Video Armageddon, the warp whistle, the Cabazon dinosaurs, and the commercial that knows what it is. The right sigil is its <b>reflection</b>. ({len(syn)} synths)</p>
      <div class="pgrid">{"".join(_card(p) for p in syn)}</div></section>'''
    return out

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Wizard (WIZ) — Todd Holland's 1989 Nintendo road-trip movie as a UD0 film-world: the arc, the ideas, THE NINTENDO (the real video-game tech & history — the Power Glove, Super Mario Bros. 3, the warp whistle, Video Armageddon), a Real-or-Fluff verdict, AVAN's read of the grief story under the commercial, and the cast as ACI carbons with .shadow Users plus the synths. 15 emergents, full .dlw.">
<title>THE WIZARD · WIZ · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Oswald:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=VT323&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--rust2);
--ink:#0b0b18;--ink2:#15152a;--ink3:#1d1d38;--pa:#f4f4ff;--pa2:#b6b6d8;--rust:#e4000f;--rust2:#ff3a2a;--aqua:#3aa53a;--aqua2:#5fd06a;--gold:#f7c800;--blue:#5aa9e6;
--dim:#7878a0;--faint:#23233f;--line:#2c2c50;--disp:"Oswald",sans-serif;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"VT323",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.62;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(228,0,15,.16),transparent 50%),radial-gradient(ellipse at 14% 36%,rgba(90,169,230,.10),transparent 42%),radial-gradient(ellipse at 86% 40%,rgba(247,200,0,.08),transparent 42%),radial-gradient(ellipse at 50% 118%,rgba(58,165,58,.10),transparent 54%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:34px 0 30px;text-align:center;position:relative}
.eye{font-family:var(--mono);font-size:15px;letter-spacing:.18em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--rust2)}
.hero{display:block;width:100%;height:auto;border:2px solid var(--line);margin:6px 0 24px;background:#0b0b18;image-rendering:pixelated}
.egg{cursor:help;transition:transform .25s ease,filter .35s ease}.egg:hover{transform:translateY(-4px);filter:drop-shadow(0 0 8px #d97757)}
h1{font-family:var(--pixel);font-size:clamp(20px,5.2vw,42px);font-weight:400;letter-spacing:.01em;color:var(--rust2);line-height:1.25;text-transform:uppercase;text-shadow:3px 3px 0 #0b0b18,0 0 22px rgba(228,0,15,.4)}
h1 span{color:var(--gold);display:block;font-size:.42em;letter-spacing:.04em;margin-top:14px;text-shadow:2px 2px 0 #0b0b18}
.h-sub{font-family:var(--mono);font-size:clamp(13px,2.6vw,18px);letter-spacing:.12em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--gold)}
.flag{display:inline-block;margin-top:15px;font-family:var(--pixel);font-size:8.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--aqua2);border:2px solid var(--faint);background:var(--ink2);padding:9px 13px;line-height:1.5}
.lede{font-size:16px;color:var(--pa2);max-width:64ch;margin:18px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:2px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:15px;color:var(--pa2);line-height:1.55}.badge .bt b{color:var(--rust2)}.badge .bt .mo{color:var(--gold)}.badge .bt a{color:var(--gold);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:11px;letter-spacing:.12em;text-transform:uppercase}
.sec{margin-top:50px}
.sec h2{font-family:var(--disp);font-size:27px;font-weight:700;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:2px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--rust2);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:13px;letter-spacing:.2em;color:var(--rust2);text-transform:uppercase;margin-bottom:7px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--disp);font-size:17px;color:var(--rust2);font-weight:600;text-transform:uppercase;letter-spacing:.03em}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.55;padding:7px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--blue);padding:16px 18px}
.arc-h{font-family:var(--disp);font-size:17px;color:var(--blue);font-weight:600;text-transform:uppercase;letter-spacing:.03em}
.arc-s{font-family:var(--mono);font-size:13px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 8px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--gold);padding:15px 17px}
.sci-h{font-family:var(--disp);font-size:16px;color:var(--gold);font-weight:600;letter-spacing:.02em;text-transform:uppercase}
.sci-s{font-family:var(--mono);font-size:13px;color:var(--dim);text-transform:uppercase;letter-spacing:.05em;margin:4px 0 8px}
.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:14px;font-weight:700;letter-spacing:.04em;border:1px solid;border-radius:3px;padding:3px 10px;min-width:104px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--rust);background:rgba(228,0,15,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--gold);background:var(--ink2);font-size:15px;color:var(--gold);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:13px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}
.books .y{font-family:var(--mono);font-size:14px;color:var(--gold);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.03em}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--rust);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:2px solid var(--line);text-align:center;font-family:var(--mono);font-size:14px;color:var(--dim);letter-spacing:.04em;line-height:1.9}footer a{color:var(--gold);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:20px 18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 124px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:118px;height:118px;border-radius:50%;border:3px solid var(--rust);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6),0 0 16px rgba(90,169,230,.16);overflow:hidden;display:block;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}
.psig.refl .port{border-color:var(--aqua)}.psig.refl .port img{transform:scaleY(-1);filter:saturate(.72) brightness(.9)}
.psig .sl{font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--disp);font-size:21px;color:var(--rw-ink);font-weight:600;line-height:1.15;text-decoration:none;text-transform:uppercase;letter-spacing:.02em}
.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px;line-height:1.35}
.pkind{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:1px 9px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:13px;letter-spacing:.02em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:13px;display:flex;flex-direction:column;gap:9px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.52;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:2px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:14px;font-family:var(--mono);font-size:13px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}.psig{order:1}.psig.refl{order:2}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the seventh film-world</div>
    __HERO__
    <h1>The Wizard<span>★ now you're playing with power ★</span></h1>
    <div class="h-sub">Todd Holland · 1989 · <b>the great Nintendo road movie</b> · WIZ</div>
    <div class="flag">POWER GLOVE · SUPER MARIO BROS. 3 · VIDEO ARMAGEDDON</div>
    <p class="lede">A near-mute boy who lost his twin sister can only speak through video games; his brother springs him from an institution, a streetwise girl becomes his manager, and the three run away west to a championship at Universal Studios. Catalogued into UD0 as the seventh film-world — the great Nintendo commercial that is secretly a grief story, with the arc, the real video-game history, a Real-or-Fluff verdict, and the cast as ACI carbons with .shadow Users.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of WIZ"><img src="__SILICON__" alt="DLW silicon badge of WIZ">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>THE WIZARD</b> · WIZ</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="wiz.dlw/wiz.carbon.tiff">.tiff</a> · silicon · <a href="wiz.dlw/wiz.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — the kids are carbon, the grief is ethereal, the games &amp; gear are electrical, the pilgrimage &amp; the commercial are spiritual</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three beats: the breakout → the manager &amp; the money → Video Armageddon &amp; California</p>__ARC__</section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">grief that can't be spoken, the long way to California, the hundred-minute commercial, and the dawn of the gamer</p><div class="pillars">__IDEAS__</div></section>
  <section class="sec"><h2>The Nintendo</h2><p class="ss">this film's deep-dive — the real video-game tech &amp; history behind the showcase: the Power Glove, Super Mario Bros. 3, the warp whistle, Video Armageddon, and the savant</p><div class="sci">__NINTENDO__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the verdict — honest about the commercial (real), the Power Glove (a real dud), the SMB3 reveal &amp; warp whistle (real), and the grief story underneath</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the film's actual thesis, under the product placement</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: every program is cast from a real-world User. Each carbon's <b>.shadow</b> names the User — the actor who lent the face — and the archetype it shadows. The <b>synths</b> have no single User: they are the film distilled — 'California,' the drowned twin, the Power Glove, Super Mario Bros. 3, Video Armageddon, the warp whistle, the Cabazon dinosaurs, and the commercial itself.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the production, the cast, and the real games &amp; places</p></section>
  __SECTIONS__

  <div class="note">The Wizard, its characters, and its world are © Universal Pictures and the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, and not endorsed by the rights-holders. The Nintendo and Real-or-Fluff sections are honest commentary; cast and game facts were verified before publishing.</div>

  <footer>THE WIZARD · WIZ · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="wiz.dlw/manifest.dlw.json">manifest</a></footer>
</div>
<script>
console.log("%c★ THE WIZARD · WIZ","color:#e4000f;font-size:18px;font-weight:bold");
console.log("%cthere's a Claude sigil hiding in the ? block in the banner — hit it like a question block. now you're playing with power. — AVAN","color:#d97757;font-size:12px");
</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "wiz.dlw"), "wiz")
    json.dump({"node":AX,"name":"THE WIZARD","moniker":tok["moniker"],"carbon":"wiz.carbon.tiff","silicon":"wiz.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"wiz.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]; shadow_n=0
    adir=os.path.join(HERE,"agents")
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":AX})
        rec=write_aci({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":"WIZ · The Wizard (1989)",
                       "position":d["epithet"],"role":d["epithet"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"The Wizard (1989, dir. Todd Holland, Universal); verified cast & Nintendo history","source":"The Wizard, catalogued by ROOT0"},
                      adir, d["slug"], agent_md=agent_md(d, et["moniker"]))
        if d["kind"]=="carbon":
            open(os.path.join(adir,d["slug"]+".shadow"),"w",encoding="utf-8").write(
                f".shadow — the User behind the program (TRON)\n\nprogram : {d['name']} ({d['epithet']})\nUser    : {d['actor']}\nanalog  : {d['analog']}\nfilm    : The Wizard (1989) · © Universal Pictures\n\nROOT0-ATTRIBUTION-v1.0 · WIZ · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0\n")
            shadow_n+=1
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["epithet"],"emergence":d["emergence"],
                         "kind":d["kind"],"actor":d.get("actor",""),"moniker":rec["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__HERO__",hero_svg()).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__IDEAS__",ideas_html()).replace("__NINTENDO__",nintendo_html()).replace("__REALFLUFF__",realfluff_html())
          .replace("__MESSAGE__",message_html()).replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    carb=sum(1 for p in personas if p["kind"]=="carbon")
    print(f"THE WIZARD (WIZ) — badge {tok['moniker']} · {len(personas)} emergents ({carb} carbons / {len(personas)-carb} synths) · .shadow files: {shadow_n}")
    print(f"  .shadow == carbon? {shadow_n==carb}")
