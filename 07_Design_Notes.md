# 07 — Design Notes

Running design log: open questions, decisions deferred, and the inspirations that shaped the design. Update this file as we resolve questions.

---

## 1. Open design questions

Tracked here so we don't lose threads. Resolved items move to the **Decisions Made** section below.

### Campaign structure

- [ ] **Campaign mode lock-in**: pick one at start vs. let it evolve mid-season? Recommend: lock at start.
- [ ] **Season length**: 6 raids is brisk, 8 is meatier. Open-ended option?
- [ ] **Roster size and budget**: is 600-800 gp per battle and 2-4 Named Characters the right scale?
- [ ] **Painting requirement**: yes vs. no? (Hobby gate, not rules gate.)

### Boasts

- [ ] **Boast claim**: public-on-trigger (current default, recommended) vs. fully secret until game end?
- [ ] **Hand size**: 1 active (recommended) vs. 2 vs. 3?

### XP and Talents

*(Resolved in v0.3 by removing class-locked Named Characters except for Healer/Banner-bearer/Warhorn-bearer — see Decisions Made.)*

### Renown

- [ ] **Renown spend cap per Winter**: yes (recommend 5) vs. no?

### Injuries

*(Resolved in v0.2 — see Decisions Made.)*

### Stores and Relics

- [ ] **Store balance**: which Stores are gp-bought vs. Saga-Roll-only?
- [ ] **Christendom-flavored Stores**: add a set to balance the Norse list?
- [ ] **Relic seeding at campaign start**: random draw, scenario-based, or player choice with restrictions?
- [ ] **Relic histories**: do Relics accumulate effects from prior wielders, or stay as-printed?

### Scenarios

*(Architectural shift in v0.3 — see Decisions Made. Open questions for v0.4:)*
- [ ] **Twist Deck size**: 15 in v0.3 is minimal; expand to ~25 in v0.4?
- [ ] **Twist draw vs open-pick**: v0.3 draws 2 keeps 1; v0.4 may switch to open-pick from the full Twist list.
- [ ] **Holdings yield cadence**: per post-game (fast clubs) vs per Winter (longer arcs)? Recommended: per post-game default, organiser can switch.
- [ ] **Multi-player Battle Types**: 3-player free-for-all and 2v2 team Battle Types for odd club counts.
- [ ] **Faction-flavored Battle Types**: longship raids for Norse only, defend-the-pilgrimage for Christians only.

### Titles

*(Resolved in v0.2 — see Decisions Made.)*

---

## 2. Decisions made

Once an open question is settled, move it here with a brief note on the resolution.

### v0.2

- **Saga Injury Table lethality dial → 1.75 on a 1-5 scale (1 = very lethal, 5 = very low lethal).** 3 of 20 slots are direct "Dead" (15% per knockdown), plus chronic death-spiral mechanics from Death's Door (slot 4) and Infection (slot 8) add another ~5% effective permanent removal. Total effective permanent removal per knockdown: ~20-21%. Over a typical 8-game season, expect most warbands to lose at least one Named Character to permanent death. Vikings die; this is the Norse saga tone. (Lethality dialed up from 1.0 = 5% effective in initial v0.2 spec.)
- **Death's Door mechanic.** Slot 4 of the Injury Table. Miss 2 battles, then roll d6 each subsequent post-game: 1-2 die, 6 recover, 3-5 persist. Effective death rate ~67%. After 4 failed recovery rolls in a row, the character's wyrd is sealed and they die at the next post-game with no roll.
- **Lasting Injury follow-up rolls → only for Death's Door (slot 4) and Infection (slot 8).** Both follow chronic-condition mechanics (d6 per post-game). All other permanent results are simply permanent; no follow-up roll required. Keeps bookkeeping minimal.
- **Healer mitigation → re-roll one Injury per battle if the warband's Healer survived.** Trades the Healer's tactical impact (in-game healing) for strategic insurance (post-game injury insurance).
- **Feast and Wise Woman bonuses to chronic conditions.** Both grant +1 to the next d6 recovery roll on Death's Door or Infection. Gives players ways to nurse a beloved character back from the brink.
- **Boast deck size for first playtest → 50 cards.** Split: 25 Common (1 Renown), 18 Bold (2 Renown), 7 Legendary (3 Renown). Three Legendary cards are multi-game 🌙. Faction-flavored and Holdings-specific Boasts deferred to v0.4.
- **Boast deck expanded to 67 cards.** Added 17 cards: 12 faction-flavored (3 Vikings, 1 Anglo-Saxons, 2 Normans, 2 Picts, 2 Welsh, 1 Romans/Romano-British, 1 Merovingian Franks/Saxons/Visigoths) and 5 Holdings-specific (Cattle Drive, Tower's Voice, Hall-Ash, Sacred Theft, Keep-Crown). Final distribution: 33 Common (49%), 24 Bold (36%), 10 Legendary (15%). Faction-locked and Battle-Type-locked cards count as "clearly impossible" for the once-per-game mulligan when the matchup doesn't fit, so players aren't punished for drawing an unfittable card.
- **Saga Advancement Table → five-path open-choice menu.** Talents (1-8 XP, max 2, gated by Chieftain) + Skills (2-3 XP, max 4) + Stat Improvements (5 XP, capped +2 cumulative per stat) + Named-Weapon Unlocks (3 XP, max 1) + Personal Sagas (4 XP, max 1). 25 Skills across 6 sub-categories, 3 Stat Improvements, 6 Named-Weapon Unlocks, 10 Personal Sagas. Open-choice for v0.3 (Mordheim-style draw-from-deck deferred to v0.4).
- **Personal Sagas as passive Renown generators.** Each character can hold 1 for life, generating +1 (sometimes +2) Renown per game when their trigger fires. Encourages thematic play (Wave-Rider for sea raids, Foe-Stalker for elite hunting, Ash-Faced for arsonists) without forcing it.
- **Scenario system → composition, not deck.** Major architectural shift in v0.3. Inspired by Blood Eagle's scenario × complication × landscape model. Each battle is composed of four layers: **Battle Type + Location + Twist + Weather**. The challenger proposes Battle Type + Location; the acceptor responds (clean / with a Twist / counter-proposes / refuses); weather is rolled. Doubles as the pairing mechanism for a club meeting.
- **Battle Types grant thematic rewards beyond loot.** Five reward categories: Plunder (gp), Glory (Renown + Title), Holding (passive yield), Relic, Tribute. 12 Battle Types for v0.3.
- **No campaign map.** Holdings are abstract named places in each warband's portfolio, won through specific Battle Types. Each player may hold at most one of each Holding type. Holdings count toward individual Renown (Feuds Mode) or side Renown (Two Sides Mode).
- **Refusing a challenge → -1 Renown + cannot be targeted until the refuser proposes.** Discourages camp-and-grind play; rewards aggressive proposals.
- **Locations as the venue layer.** 15 Locations for v0.3 (3 open country, 5 wilderness, 5 settled, 2 special), each with default terrain and a light mechanical effect. Challenger picks Location at proposal time alongside Battle Type. Acceptor can swap Locations via the *Change Venue* Twist. Locations may be banned by either player at campaign start if they lack the terrain (mutual veto). Twists may not duplicate the chosen Location's effect.
- **Naval and elevation Locations added.** Lone Hilltop (single dominant hill, slope rules), Tidal Estuary (half-table shallow water, no swim roll, beached ships allowed), Longship Boarding (two ships rail-to-rail, no cavalry, figures push off into the water). Cover the boat/river/hill terrain gaps in v0.3.
- **Stretch Locations added.** Market Square (Settled — standalone marketplace with Hecatomb-style stalls and a well), Henge (Special — ring of standing stones, sacred ground bonuses and Renown shifts for kills inside), Frozen Lake (Special — half-table ice with break-through risk, auto-Snow weather). Catalog now at 18 Locations: 3 Open country, 5 Wilderness, 6 Settled, 4 Special.
- **Quick Start guide added** ([09_Quick_Start.md](09_Quick_Start.md)). Onboarding document covering: materials needed, Day 0 setup (campaign mode, season length, warband creation, ban list, yield cadence, Relic seeding), first-meeting walkthrough, a sample 6-meeting season ("The Cold Coast"), campaign-organiser tips, a Warband Sheet template, common questions, and a one-page quick reference card. Designed to get a club from "we want to try this" to running a battle in ~30 minutes of setup.
- **Annual Events deck originally 20 cards, expanded to 30 in v0.3.** Distributed across 4 categories: Hazards (8), Boons (8), Faction-divergent (7), Shake-ups & Holdings (7). New cards added: Wolves Stir in the Wilds (warrior loss roll, mitigation 1 Renown), Old Curses Wake (Chieftain Lingering Wound: Aim risk, mitigation 2 Renown), Sea-Storm at the Coast (no ships next battle, mitigation 1 Renown), A Treasure Found (d6 4+ for 40 gp), Diplomatic Envoy (choose 20 gp or 1 Renown), Festival of the Year (free Feast + 1 Boast draw next battle), Norse Raid Far Away (Norse +1 Renown, Christians cannot deploy cavalry next battle, mitigation 1 Renown), Holy Feast Day (Christians' Healers heal on 3+ next battle, Norse get 20 gp), A New Hall Rises (next Sack the Hall win gives double Burned Hall yield), The Saga Journal (cumulative Renown bonus: +2 for Legendary Boast, +1 for Title, +1 per Holding). Mitigation via Renown spend on most Hazards; some are unavoidable. Effects stay flat regardless of player count. Renown never goes negative; floors at 0.
- **Named Characters are class-flexible** except for three locked-role specialists. Generals (4-5 max) have no fixed class; their kit is chosen fresh each battle from any warrior/Chieftain/Berserker-equipped option per Pillage's army-building rules. One General is designated Chieftain per battle and only their Talents fire. Healer, Banner-bearer, and Warhorn-bearer are class-locked specialists (max 1 each) who always play in their role when fielded; they do not earn Talents but can earn role-restricted Skills (4 Healer Skills, 3 Banner Skills, 3 Warhorn Skills added to the Saga Advancement Table).
- **Berserker becomes equipment, not a class.** Any figure can be equipped as a Berserker for a battle by paying the Pillage Berserker cost (faction-restricted to Vikings per Pillage core). They get the full Berserker profile and game-long mushroom rage per Pillage's existing rules.
- **Hallucinogenic Mushrooms Store reworked.** No longer Berserker-only. Now: any figure may eat them once per game during a non-melee turn. Roll d6 for **Confusion**: on a 1, the figure goes Wild and must charge the nearest figure (friend or foe), no rage benefits; on a 2+, they gain one-turn rage effects (auto-pass morale, +1 attack). A Berserker-equipped figure can stack this on top of their normal Berserker rage but still rolls for Confusion. The 1-in-6 friendly-fire risk balances the Store against the more expensive but reliable Berserker equipment line.
- **No Chieftain succession mechanic.** Replaced by per-battle Chieftain designation. If all your Generals die, you must recruit a fresh one for 50 gp from Treasury before your next battle. A free Title roll is granted to the new Chieftain after a battle in which the previous Chieftain died, representing the warband's new leadership.
- **Cool Head Skill removed.** Overlapped with the Swift As Lightning Talent. Use the Talent path for Chieftain-level initiative bonuses.
- **Battle Type detail completed.** All 12 Battle Types in [05_Scenarios.md](05_Scenarios.md) §3 now have full playable detail: force balance (gp ratios), turn limit, deployment instructions, initiative, victory conditions (winner/loser/tie/major), special rules referencing Pillage core mechanics, and reward. Includes a quick-reference table at the top of §3 for at-a-glance composition planning.
- **Custom Battle Types** allowed via a homebrew clause at the end of §3. Players may propose entirely custom scenarios in place of catalog picks, declaring name + reward category (from the 5 standard ones) + force balance + turn limit + special elements + victory conditions + special rules. Target may accept clean, accept with a Twist, counter-amend, or refuse. Constraints: reward must map to a standard category; force budgets capped around 1600 gp combined; campaign organiser may veto unbalanced submissions. Custom Battle Types both players enjoy may be archived into the campaign's house-rules supplement, growing the catalog over time.
- **Twist deck expanded to 25.** Added 9 new Twists in v0.3: First Light (extends game by 2 turns), Foreign Mercenary (d6 4+ for free figure at turn 3), Burning Field (a field starts on fire), Treacherous Footing (charges roll d6, 1 = trip and fail), Sacred Stone (impassable center stone, +1 morale in contact), Roving Hounds (1d3 ownerless warhounds attack nearest figures per Pillage's masterless-warhound rules), No Cavalry (neither side fields cavalry), Bowmen in Cover (3 free stationary archers for defender), A Wandering Skald (neutral NPC scatters d6 per turn; kill = -2 Renown, escort off your edge = +2 Renown). New Narrative category added. Final categories: Weather (4), Timing/Reinforcements (6), Terrain (9), Force/Composition (4), Narrative (1), Composition (1). Open Pit was drafted but removed per user preference.
- **Saga Roll mitigation → 1 Renown per season to re-roll once.** Gives some agency over bad luck without softening the table. Wyrd is Cruel (slots 70-71) ignores this protection by design.
- **Title trigger threshold → major victory** = win + (50%+ casualty differential OR Legendary Boast OR killed/captured enemy Chieftain). Multiple trigger paths so the system doesn't favor only kill-heavy playstyles.
- **Title stacking → max 2 per character.** A third forces the player to drop one. Keeps names readable.
- **Inflicting titles on losers → costs 1 Renown.** Makes the "Dungbreath" effect a deliberate spend, not a free insult.
- **Faction-flavored Title sub-tables → deferred to v0.3.** The current table has faction-tinted entries in row 7 but is otherwise faction-neutral. Will revisit if playtest shows Christendom and Norse warbands feel undifferentiated.

---

## 3. Sources mined for inspiration

| Source | Type | What we lifted |
|---|---|---|
| **Pillage core rulebook** (Triskell Interactive) | Tactical engine | Tactical engine, faction lists, gp economy, loot mechanics, base scenarios, the Talent list as the seed for XP-purchased advancement |
| **Pillage supplements** | Tactical | *Hecatomb*, *Winding Ways*, *Sheep & Beehives*, *Fall of Rome* — additional scenarios, terrain events, expanded factions, the Sack of Saint Lunaire relic mechanic |
| **Dux Britanniarum** (Too Fat Lardies) | Campaign system | D6 raid scenario template, Title/Reputation table, Annual Events, recovery-time-as-currency, career path with status unlocks (deferred for v0.2+) |
| **Blood Eagle** (Ministry of Gentlemanly Warfare) | Light campaign | Points Pool warband model (informed our Treasury-as-budget), ransom-at-half-cost, scripted saga structure, Grand Finale concept |
| **Port Royal / Blood & Plunder** (Firelock Games) | Full warband progression | The 10-step post-game sequence skeleton; Officer Injury Table; XP/Advancement system; d100 Exploration Table (became Saga Roll); Infamy/Renown as victory metric; Mutiny/Oathbreaking check |
| **SimpleMinis VSGMR** | Light tactical | Scenario archetype menu (Escape, Transport, Ambush, Fortress Assault) for new raid types |
| **Shieldwall zine** | Linked narrative | Linked-narrative scenario template (the Alba campaign structure) for Sides Mode arcs |
| **Xenotactics skirmish rules** | Sci-fi tactical | Point-buy formula concepts (minor, tangential — not used directly) |

---

## 4. Design principles

Stated explicitly so future revisions can check against them.

1. **Don't rewrite Pillage.** The tactical engine works; the campaign sits on top. We never modify how Pillage plays mid-battle, only what happens between battles. The one exception is the XP-conversion of Talents, which changes when (not how) Talents are acquired.
2. **Theme is the master.** If a mechanic is balanced but un-Norse, it's wrong. Vikings boast, raid, ransom, feast, and die badly. The system rewards each of those.
3. **Player vs player only.** No NPC defenders. Every battle pits two warbands of two players.
4. **The bench matters.** Named Characters other than the Jarl should be worth investing in. Talents-as-XP-rewards is the keystone mechanic here.
5. **Renown is the carrot, not the stick.** Players who fall behind on Renown should still feel like they're in their own saga. The system never crushes a player; it just rewards another more.
6. **Bookkeeping budget is small.** A player should be able to update their warband sheet in 10 minutes after a battle. If the post-game sequence creeps over 15 minutes, simplify.
7. **The scenarios do the heavy lifting.** Most campaign flavor comes from the variety of battles, not from the meta-game. The scenario composition system (propose / twist / weather) plus a rich Battle Type catalog with distinct rewards makes the engine sing.
