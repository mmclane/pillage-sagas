# 07 — Design Notes

Running design log: open questions, decisions deferred, and the inspirations that shaped the design. Update this file as we resolve questions.

---

## 1. Open design questions

Tracked here so we don't lose threads. Resolved items move to the **Decisions Made** section below.

### Campaign structure

*(Locked in v0.3 — see Decisions Made.)*

### Boasts

*(Locked in v0.3 — see Decisions Made.)*

### XP and Talents

*(Resolved in v0.3 by removing class-locked Named Characters except for Healer/Banner-bearer/Warhorn-bearer — see Decisions Made.)*

### Renown

*(Locked in v0.3 — see Decisions Made.)*

### Injuries

*(Resolved in v0.2 — see Decisions Made.)*

### Stores and Relics

*(Locked in v0.3 — see Decisions Made. Some items deferred to v0.5.)*

### Scenarios

*(Locked in v0.3 — see Decisions Made. Open items for v0.5:)*
- [ ] **Twist draw vs open-pick**: v0.3 stays at draw 2 keeps 1. Open-pick deferred for playtest.
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

### v0.3 policy locks

A pass to close out remaining policy-shaped open questions before v0.4 / playtest.

- **Campaign mode → locked at start.** Players pick Feuds Mode or Two Sides Mode at campaign creation. No mid-season mode shifts.
- **Season length → Short Season default (6 raids + Grand Finale, 7-8 meetings).** Standard Season (8 raids + Finale, 9-10 meetings) is an option for clubs that want longer. Open-ended seasons are not officially supported (the Grand Finale and Title gathering are the closure mechanism).
- **Roster size → 4-5 Named Characters + 0 to 3 specialists (max 1 each).** Already in 01_Core_Rules.md §3; explicitly confirmed.
- **Painting requirement → NO rules gate.** Painting is purely a hobby preference per club. Recommended minimum: figures should be table-ready (assembled, at minimum primed) for visibility, but not strictly enforced. Some clubs may add their own painting requirement as a house rule.
- **Boast claim → public-on-trigger.** The player reveals the Boast card the moment the trigger condition is met. Renown awarded immediately. Opponent sees what was claimed.
- **Boast hand size → 1 active Boast plus up to 1 extra slot for multi-game 🌙 Boasts (max 2 cards in hand total).** Already in 03_Boasts.md §1; explicitly confirmed.
- **Renown spend cap per Winter → NO hard cap.** Players may spend Renown freely on the spend menu (Bards, Feasts, Sagas, Boast draws, Mead-Hall taunts). The campaign organiser may flag and discuss if a single warband is monopolizing Renown-spend advantages, but the system trusts the player to spend wisely. (Earlier recommendation was a cap of 5; removed for simplicity.)
- **Holdings yield cadence → per post-game by default; organiser can switch to per-Winter at campaign start.** Already documented in 05_Scenarios.md §6 and 09_Quick_Start.md §2. Explicitly confirmed as the default.
- **Store balance → all gp-bought for v0.3.** Saga Roll grants supplement the gp economy by occasionally awarding free Stores. No Stores are Saga-Roll-only (the existing entries in 06_Tables.md §2 are free *grants*, not unique acquisitions).
- **Christendom-flavored Stores → deferred to v0.5.** Current Stores list is faction-neutral; Christian flavor (Holy Oil, Saint's Banner, Indulgence Letter) is a future expansion. (Note: Mushrooms were drafted as a Norse-flavored Store in v0.3 but removed in v0.5 per peer review.)
- **Relic seeding at campaign start → organiser's choice between three methods** (random draw assigned, scenario-based pool, or player-choice with organiser veto). All three documented in 04_Stores_and_Relics.md §8a. Organiser picks per campaign.
- **Relic histories → NO.** Relics are as-printed; they don't accumulate prior-wielder effects. Keeps tracking minimal. (Saga journal can still record a Relic's full provenance for narrative.)
- **Twist draw mechanic → stays at draw-2-keep-1.** Open-pick from full Twist list deferred for playtest data.
- **Warband Sheet → dedicated file added ([10_Warband_Sheet.md](10_Warband_Sheet.md)).** Full printable-friendly tracking sheet with all fields: identity, resources, Holdings, Stores inventory, 5 Named Character entries (each with XP, Titles, Talents, Skills, Stat Improvements, Named-Weapon Unlock, Personal Saga, Injuries, Relic), 3 specialist entries (Healer, Banner-bearer, Warhorn-bearer), current Boast hand, an 8-battle + Grand Finale battle log, and a Saga Journal section. Markdown table format intended for digital tracking; a printable PDF version is a v0.4 TODO.

### v0.5 polish and content expansion

**Polish:**
- **Edge Cases and Rulings document added** ([11_Edge_Cases_and_Rulings.md](11_Edge_Cases_and_Rulings.md)). ~40 proactive rulings on ambiguous interactions across Named Characters, XP/Talents/Advancement, Boasts, Stores, Relics, Holdings, Saga Roll/Injury Table, Annual Events, composition/proposals, multi-warband interactions, and Grand Finale tiebreakers. Designed to grow with play.
- **Terminology audit completed.** Stale references to "Huscarl as a Named Character class" cleaned up; resolved open design questions on Berserker/Healer Talents and Path B-E flavoring marked as closed.
- **Glossary note added** to 01_Core_Rules.md clarifying that Jarl and Chieftain are used interchangeably.

**Lower-priority mechanics:**
- **Forgo Advancement option** (Path F: Donate to the Warband). 3 XP → +1 Renown. Safety valve for capped characters and specialists.
- **Legendary Grand Finale Titles** (new §4 in 06_Tables.md). 5 super-Titles only awarded after Grand Finale victory: the Saga-Bound, the Wyrd-Touched, the Eternal, the Crown-Maker, the Saga-King. Deliberately narrative-heavy; the Eternal and Saga-Bound have light mechanical hooks.
- **Lasting Injury → automatic Title mappings.** Characters who roll permanent Injuries get free Titles (the One-Eyed, the Maimed, the Broken-Backed, the Scarred, the Twice-Born, the Iron-Bellied, the Haunted) that inherit the Injury's mechanical effect — no new power, just consistent naming.
- **Optional Title mechanical effects layer** for ~10 Titles (the Bold, the Mighty, the Cunning, the Magnanimous, the Generous, the Pious, the Coward, the Drunken, Dungbreath). Disabled by default; campaign organiser opts in at campaign start.
- **Title Negation (optional):** loser spends 1 Renown to negate a forced Title from a winner. Default off.

**Content expansion:**
- **3 Multi-player Battle Types added:** The Althing (4-player Jarl-vs-Jarl secret targets, from Winding Ways supplement), Three-Way Free-For-All (3 players, temporary alliances allowed), Coalition Battle (2v2 with shared budgets per side). Use a separate sign-up mechanic outside the standard proposal flow.
- **3 Faction-flavored Battle Types added:** Longship Raid (Norse-only raider, beached ship that must remain intact for escape), Defend the Pilgrimage (Christian-only defender, escort 4 NPC pilgrims off the edge), Forest Ambush (Pict/Welsh/Irish-Scots-only ambusher, free King of Ambushes Talent).
- **6 Christendom-flavored Stores added:** Holy Oil, Saint's Banner, Indulgence Letter (Christian-only), Confessor's Vial (Christian-only), Pilgrim's Sandal, Blessed Sword. Two are faction-locked; the rest are open.
- **Relic list expanded from 10 to 17:** Caladbolg (Irish push-back), Aelfric's Bane (generated by L01 Boast on first completion), Glove of the Pict (ignore difficult terrain), Norse Drinking Horn (+1 morale aura), Hilt of Charles Martel (+1 vs cavalry), Saxon War Helm of Cynehelm (ignore first Dane Axe hit), Cloak of Skuld (one-game move through difficult terrain freely).
- **Annual Events deck expanded from 30 to 35 cards:** AE31 The Hall is Rebuilt (d6 to regain lost Burned Hall), AE32 The Watch Tower is Reinforced (no challenges next meeting), AE33 The Skalds Gather (Grand Finale Approaches: +1 Boast per battle rest of season), AE34 The High King's Court Summons (Grand Finale Approaches: 1.5x Renown for Finale only), AE35 The Druid Stirs (d6 omen per warband).
- **6 more Boast cards added** for under-represented factions: Wolf-Friend (Irish/Scots/Picts, C34), Breton Stalker (Bretons, C35), The Free Northman (Generic, C36), Palace Guard's Charge (Carolingian Franks, B25), Storm of the Steppe (Huns, B26), Tribute of the Hostage (Rescue the Hostage only, B27). Final deck size: **73 cards** (36/27/10 across tiers).

**Version bumped to 0.5** in README.
- **Annual Events deck originally 20 cards, expanded to 30 in v0.3.** Distributed across 4 categories: Hazards (8), Boons (8), Faction-divergent (7), Shake-ups & Holdings (7). New cards added: Wolves Stir in the Wilds (warrior loss roll, mitigation 1 Renown), Old Curses Wake (Chieftain Lingering Wound: Aim risk, mitigation 2 Renown), Sea-Storm at the Coast (no ships next battle, mitigation 1 Renown), A Treasure Found (d6 4+ for 40 gp), Diplomatic Envoy (choose 20 gp or 1 Renown), Festival of the Year (free Feast + 1 Boast draw next battle), Norse Raid Far Away (Norse +1 Renown, Christians cannot deploy cavalry next battle, mitigation 1 Renown), Holy Feast Day (Christians' Healers heal on 3+ next battle, Norse get 20 gp), A New Hall Rises (next Sack the Hall win gives double Burned Hall yield), The Saga Journal (cumulative Renown bonus: +2 for Legendary Boast, +1 for Title, +1 per Holding). Mitigation via Renown spend on most Hazards; some are unavoidable. Effects stay flat regardless of player count. Renown never goes negative; floors at 0.
- **Named Characters are class-flexible** except for three locked-role specialists. Characters (4-5 max) have no fixed class; their kit is chosen fresh each battle from any warrior/Chieftain/Berserker option per Pillage's army-building rules. One Character is designated Chieftain per battle and only their Talents fire. Healer, Banner-bearer, and Warhorn-bearer are class-locked specialists (max 1 each) who always play in their role when fielded; they do not earn Talents but can earn role-restricted Skills (4 Healer Skills, 3 Banner Skills, 3 Warhorn Skills added to the Saga Advancement Table).
- **Berserker (and Huscarl) are troop types, not equipment** (clarified in v0.5 peer review). Pillage's army-building lists Warrior, Chieftain, Berserker, Huscarl, Healer, etc. as separate troop types with their own base costs. Any Named Character can be fielded as any troop type their faction allows, paying the corresponding base cost + equipment, for a given battle. Berserker's printed Pillage abilities (game-long rage when conditions are met per the core rulebook) work as printed.
- **Hallucinogenic Mushrooms Store: REMOVED in v0.5** (peer review feedback). Either too powerful or tread on Berserker's specialness. Berserker rage now comes only from being fielded as a Berserker troop type per Pillage's core rules. The Confusion roll mechanic added in v0.3 is also gone with the Store.
- **No Chieftain succession mechanic.** Replaced by per-battle Chieftain designation. If all your Characters die, you must recruit a fresh one for 50 gp from Treasury before your next battle. A free Title roll is granted to the new Chieftain after a battle in which the previous Chieftain died, representing the warband's new leadership.
- **Cool Head Skill removed.** Overlapped with the Swift As Lightning Talent. Use the Talent path for Chieftain-level initiative bonuses.
- **Battle Type detail completed.** All 12 Battle Types in [05_Scenarios.md](05_Scenarios.md) §3 now have full playable detail: force balance (gp ratios), turn limit, deployment instructions, initiative, victory conditions (winner/loser/tie/major), special rules referencing Pillage core mechanics, and reward. Includes a quick-reference table at the top of §3 for at-a-glance composition planning.
- **Custom Battle Types** allowed via a homebrew clause at the end of §3. Players may propose entirely custom scenarios in place of catalog picks, declaring name + reward category (from the 5 standard ones) + force balance + turn limit + special elements + victory conditions + special rules. Target may accept clean, accept with a Twist, counter-amend, or refuse. Constraints: reward must map to a standard category; force budgets capped around 1600 gp combined; campaign organiser may veto unbalanced submissions. Custom Battle Types both players enjoy may be archived into the campaign's house-rules supplement, growing the catalog over time.
- **Twist deck expanded to 25.** Added 9 new Twists in v0.3: First Light (extends game by 2 turns), Foreign Mercenary (d6 4+ for free figure at turn 3), Burning Field (a field starts on fire), Treacherous Footing (charges roll d6, 1 = trip and fail), Sacred Stone (impassable center stone, +1 morale in contact), Roving Hounds (1d3 ownerless warhounds attack nearest figures per Pillage's masterless-warhound rules), No Cavalry (neither side fields cavalry), Bowmen in Cover (3 free stationary archers for defender), A Wandering Skald (neutral NPC scatters d6 per turn; kill = -2 Renown, escort off your edge = +2 Renown). New Narrative category added. Final categories: Weather (4), Timing/Reinforcements (6), Terrain (9), Force/Composition (4), Narrative (1), Composition (1). Open Pit was drafted but removed per user preference.
- **Saga Roll mitigation → 1 Renown per season to re-roll once.** Gives some agency over bad luck without softening the table. Wyrd is Cruel (slots 70-71) ignores this protection by design.
- **Title trigger threshold → major victory** = win + (50%+ casualty differential OR Legendary Boast OR killed/captured enemy Chieftain). Multiple trigger paths so the system doesn't favor only kill-heavy playstyles.
- **Title stacking → max 2 per character.** A third forces the player to drop one. Keeps names readable.
- **Inflicting titles on losers → costs 1 Renown.** Makes the "Dungbreath" effect a deliberate spend, not a free insult.
- **Faction-flavored Title sub-tables → deferred to v0.3.** The current table has faction-tinted entries in row 7 but is otherwise faction-neutral. Will revisit if playtest shows Christendom and Norse warbands feel undifferentiated.

### v0.5+ peer-review feedback fixes

**Army economy reworked as rebuy-then-refund (peer feedback round 1).** The previous "buy a fresh army each battle, no refund" rule was financially unsustainable — Treasury drained in 2-3 games. The intermediate "persistent rank-and-file roster" idea worked mathematically but added bookkeeping overhead. Final model per peer feedback: each battle the player assembles their army from Treasury paying full Pillage gp prices for everyone fielded. Post-battle, surviving figures' gp value refunds to Treasury. Killed figures' gp is lost. Captured figures are resolved separately in the Ransom step.

This framing is mathematically equivalent to a persistent-roster model but simpler at the table:
- No need to track individual rank-and-file figures between battles.
- Re-equipping happens naturally at the next army-build (just buy different gear).
- Players can scale their army size up or down by choosing how much Treasury to commit per battle.

**Captured figures may be ransomed back** at half their gp cost (paid by the original owner to the captor) in the Ransom step. Declined or unaffordable ransoms leave the captor with the prisoner; captor may sacrifice for +1 Renown or hold indefinitely. Captured warriors cannot be recruited into the captor's warband — captured enemies don't switch sides. The half-cost ransom saves the owner ~50% vs replacement when they can pay.

**Loot token campaign value: 10 gp (was Pillage canonical 5 gp).**

Detailed math for the increase:

Per-battle casualty cost analysis:
- A typical warrior fully equipped: spear + shield + armor = 25-35 gp (varies by faction).
- A Berserker or kit-heavy figure: 50-80 gp.
- Average gp value of a casualty: ~35 gp.
- Casualty rate per battle: 2-3 figures dead = **70-105 gp lost per battle**.

Per-battle income needed for sustainability: ~70-105 gp (matching casualty cost).

Income comparison at different loot values, for a winning Pillage Town (4 loot extracted + 30 gp Battle Type bonus):

| Loot value | Win income | Net vs casualties | Verdict |
|---|---|---|---|
| 5 gp (Pillage canon) | 4×5 + 30 = 50 gp | -20 to -55 gp | Treasury bleeds out in 3-5 games |
| **10 gp (2× canon)** | **4×10 + 30 = 70 gp** | **0 to -35 gp** | **Break-even on wins; Holdings yield buffers** |
| 15 gp (3× canon) | 4×15 + 30 = 90 gp | +20 to -15 gp | Mild surplus on wins; comfortable |
| 20 gp (4× canon) | 4×20 + 30 = 110 gp | +40 to +5 gp | Possibly too generous |

Decision: **10 gp per loot token** for the campaign baseline. Doubles Pillage canonical without making players rich. Hits break-even on Plunder Stakes wins, and Holdings yield (10-40 gp per cadence) covers the slow drain. If playtest shows it's still too tight, organisers may bump to 15 gp.

Non-Plunder battles (Glory Stakes, Holding Stakes, Relic Stakes) yield no immediate gp from loot — they trade gp income for Renown, Holdings income, or Relic acquisition. Warbands that win primarily non-Plunder battles need to lean on Holdings yield and ransom income. This is intentional pressure that encourages diverse Battle Type selection.

**Other assumptions for a typical battle:**
- Army built fresh from Treasury: ~400 gp (1 Chieftain + 7-9 warriors + 1 Banner-bearer, ~8-12 figures total, varies by faction equipment costs). Battle Type force balances range 250-500 gp.
- Why 400 gp instead of Pillage's standard ~800 gp: Pillage's army budget includes Talent costs (5-60 gp each, 2 per chieftain). This campaign moves Talents to XP rewards, so the same army equipment costs ~half the gp. 400 gp now buys what 800 gp used to.
- Casualty rate: 20-30% per battle = 2-3 figures dead per battle (similar absolute numbers in smaller armies, similar percentages).
- Average gp value of a casualty: ~35 gp.
- Loot earnings per battle: 70-100 gp on Plunder Stakes wins (at 10 gp/token rate); 20-40 gp on losses; 0-20 gp on non-Plunder battles.
- Holdings yield: persistent Holdings add 10-40 gp per cadence cycle.

Per-battle Treasury accounting (rebuy-then-refund, 400 gp army, 10 gp/token):
- Step 1: Spend full army cost. Treasury -400 gp.
- Step 2: Battle happens. Some figures die.
- Step 3 (Collect Treasure): Add loot gp (e.g., +70-90 gp on a Plunder win at 10 gp/token) AND refund surviving figures' value (e.g., 330 gp returned from 8/10 figures alive at ~40 gp/figure on average if we assume 2 died).
- Step 4 (Ransom): Resolve any captures. Owner pays half cost if ransoming back.
- **Net Treasury change**: ~+70-90 gp loot - 70 gp casualty value = roughly **break-even on Plunder wins** when 2-3 figures die.
- A 4-casualty bad battle costs ~140 gp; partly offset by loot.
- A perfect-victory zero-casualty battle nets ~+70-90 gp (rare; usually some attrition).
- Starting Treasury 600 gp absorbs the first ~3 bad battles before requiring Holdings income or smarter play.

Sustainability check:
- 6-battle Short Season with 3 wins (2 casualties each) + 3 losses (3 casualties each):
  - Wins: 3 × ~break-even = ~0 gp net
  - Losses: 3 × ~-50 to -80 gp = -150 to -240 gp
  - Holdings: 2 small Holdings × 6 cadences × 25 gp = +300 gp
  - **Net season**: roughly +60 to +150 gp Treasury growth over 6 battles. Sustainable.
- Holdings income is the buffer; warbands with no Holdings will feel pressure.
- Starting Treasury 600 gp covers ~3-5 bad battles' worth of casualties (at ~70-100 gp drain per loss) even before Holdings income.

**TODO — write a simulation script** (`simulate_campaign.py`) that runs many randomized seasons and reports sustainability metrics across parameter sweeps. The current math is analytical (best/typical/worst case); a Monte Carlo simulation will validate the actual distribution of outcomes.

Parameters to vary:
- Starting Treasury (300, 500, 600, 800, 1000 gp)
- Loot token value (5, 10, 15, 20 gp)
- Army budget (300, 400, 500 gp)
- Casualty rate (15%, 20%, 25%, 30% per battle)
- Holdings acquired during season (0, 1, 2, 3+)
- Win/loss ratio (50/50, 60/40, 40/60)
- Healer presence (with/without injury re-roll mitigation)

Metrics to measure per simulated season:
- Treasury trajectory across battles (mean, median, percentiles)
- Bankruptcy rate (% of warbands unable to field a 300+ gp army at any battle)
- Named Character permanent death count (lethality of the Saga Injury Table)
- Final Renown distribution
- Ransom decisions taken (count and aggregate gp)

Goal: find the **starting Treasury value** where ≥80% of warbands can sustain themselves through an 8-game season without going bankrupt, given typical play (mixed wins/losses, 2 Holdings acquired mid-season, no extreme bad luck on Annual Events). Validate the recommended 600 gp or recommend an adjustment.

Implementation sketch: a Python script reading parameters from a config dict, running `N=1000` seasons per parameter set, outputting a results table or CSV. Could re-use the `md_to_docx.py` style structure (single Python file in the project root).

This is a deferred task; it doesn't block playtest but will sharpen the numbers before publication.

Ransom impact:
- Without ransom: captured figure = dead = 40 gp replacement cost.
- With ransom: captured figure ransomed for 20 gp = saves 20 gp per ransom.
- Captor's call: ransom (+20 gp) or sacrifice (+1 Renown, no gp). Renown-rich warbands tend to take gp; Renown-poor tend to sacrifice for the Renown bump.

Open math questions to playtest:
- Is 50% ransom rate fair to both sides, or does it advantage the captor too much? Consider 40% or 60%.
- Should the Healer's heal mechanic prevent some casualties from becoming permanent deaths? Currently it does (heals during the battle).
- Should there be a "campaign salary" — a small per-meeting Treasury injection (e.g., +30 gp from your domain) to soften the squeeze? Currently no.
- Should starting Treasury be raised from 300 to 400-500 gp to give more cushion for the first 3 battles?
- Does the rebuy-then-refund framing actually feel cleaner at the table than persistent-roster, or do players want to keep the same warriors visibly between battles for narrative reasons? Playtest will tell.

**Grand Finale needs rework (v0.5+).** The current spec ("all players field their full Treasury and Roster in one battle") is too large for a single tabletop session. Marked as a placeholder in 01_Core_Rules.md §4. **Design direction (per peer feedback):** expand The Althing Multi-player Battle Type into the season climax — secret targets among all Chieftains, with season-ending stakes (Legendary Titles, side victory in Two Sides Mode, Renown multipliers). Each surviving Chieftain participates with a smaller retinue rather than full warband strength. Full design deferred to a later revision.

**DOCX export CSS improved.** The Google Docs / Word table overflow was caused by missing `width: 100%` and `table-layout: fixed` in the export script's CSS. Updated `md_to_docx.py` to apply 9pt font, 0.75in page margins, and fixed-layout tables that wrap content. Regenerated all 12 DOCX files.

**v0.5 peer review round 2 (XP and Advancement, Stores, Skills):**

- **Berserker and Huscarl are troop types** (not equipment, not "equipped as"). Terminology updated across all 12 files. References like "Berserker-equipped figure" → "Berserker figure"; "equipped as a Berserker" → "fielded as a Berserker."
- **Hallucinogenic Mushrooms Store removed.** Too powerful and stepped on Berserker's specialness. Berserker rage now exclusively comes from the Berserker troop type per Pillage's printed rules. Confusion roll mechanic removed with it. Affected Boast cards (B08 Bared Teeth, B19 Mead-Tested), the Berserker's Friend Personal Saga, Saga Roll slot 58-59 (replaced with A Trader's Bargain, +40 gp), the Warband Sheet inventory, and edge cases all cleaned up.
- **Wise Woman Healer Skill** replaced. The intermediate "free first heal" version (from removing the "casting" language) was based on a wrong premise — in Pillage, Healers don't take an action to heal in the first place. The new Wise Woman (4 XP, up from 3 XP) gives Healers a meaningful upgrade: "this Healer may move their full movement AND heal in the same turn." Pairs naturally with Cunning Folk (2 XP, once per game, half movement + heal) which is the cheaper, limited-use version.
- **Field Surgeon Healer Skill** replaced. The old version ("may heal a figure currently engaged in melee") was based on another wrong premise — Healers aren't restricted from healing figures in melee in Pillage; they may even require base contact (effectively being in melee themselves) to heal. New Field Surgeon (2 XP, down from 3 XP): "Once per game, this Healer may re-roll a failed healing roll." Matches the re-roll cost pattern of Quick Strike / Iron Stance / Bone Density (all 2 XP).
- **Wall-Breaker Melee Skill** replaced. Too situational — fired only when the enemy formed a Shieldwall, which doesn't happen every battle. Replaced with **Shield-Splitter** (2 XP): "+1 to melee hit rolls against figures with a shield (SA-with-shield or FA)." Fires whenever the opponent has a shield, which is common across factions. Mirrors Pin-Point (the ranged +1 vs FA Skill) for symmetry.
- **Beast-Bane Melee Skill** target corrected. The Skill is named for harming the beast (horse), not the rider, but the old wording said "rider." Updated: "+1 to melee hit rolls when targeting a cavalry figure's mount (the horse), per Pillage's cavalry rules that allow melee to target either the horse or the rider."
- **Backswing Melee Skill** made charge-conditional. The previous "+1 to all melee hits with a hand weapon" was too broadly applicable — would have been an auto-take. New version (Option A from the peer review): "When this character charges into melee with a hand weapon, +1 to all melee hit rolls for that turn. Does not apply when defending against a charge." Fires on aggressive turns only; rewards a charging playstyle and pairs with the other situational +1 hit Skills (Beast-Bane vs horse, Shield-Splitter vs shielded, Pin-Point vs FA at range).
- **Counter-Strike Melee Skill** added (2 XP, peer review): "When this character is the target of a charge, +1 to all melee hit rolls for that turn. Does not apply on turns this character is the charger." Defensive mirror to Backswing — Backswing rewards aggressive charges; Counter-Strike rewards positioning to receive a charge. Each is situational (charging vs being charged), so neither is auto-take.
- **Two-Fisted Melee Skill removed.** Dual-wielding hand weapons isn't a standard Pillage mechanic outside the Rus faction's specific rule; the Skill was redundant with or overlapping with that faction rule. Removed in v0.5 peer review. Combat — Melee section now has 7 Skills.
- **Boast draw safety nets added.** Concern: a player could draw two Boasts that are both faction-locked to wrong factions or Battle-Type-locked to the wrong battle, leaving them stuck with an unusable card. New rules: (1) "both-impossible redraw" — if both initial draws are objectively impossible (faction lock or Battle-Type lock mismatch), auto-discard both and draw 2 fresh ones, repeating as needed; doesn't count against the mulligan; (2) the per-game mulligan remains for soft-impossible cards (Location-feature requirements, equipment requirements, etc.); (3) "no-Boast last resort" — if after all redraws and mulligans a player still has nothing usable, they may play with no Boast that battle (no Renown gained, no penalty). Auto-redraw probability calc: ~4% chance per attempt to draw 2 locked cards both mismatched; multi-redraw is vanishingly rare with 73-card deck.
- **Dogged Pursuit (C12) reworded** to match Pillage's actual Flee mechanic. Old text ("catches and kills a Fleeing enemy") didn't map to a real Pillage rule — Flee is a charge reaction, not a persistent state. New text (Option A from peer review): "An enemy figure attempts to Flee from your figure's charge, fails their Flee roll (1-3), and is destroyed when your figure makes contact." Triggers on the auto-destruction outcome of a failed Flee, which is a real Pillage mechanic.
- **Closing Volley (B28) added** as a dedicated Bold Boast for killing the charger with a closing shot. Defender's Right (C17, Common) covers "any kill of the charger"; Closing Volley specifically rewards the harder closing-shot kill (-1 to hit per Pillage FAQ). Deck size now 74 cards.
- **Defiant Standard Banner-bearer Skill** reworked. The old wording ("pass morale on 2+") was redundant with Pillage's default morale (you only fail on 1). New version: "Once per battle, friendly figures within 6" of the banner-bearer may re-roll a failed morale roll (a 1)."
- **Quartermaster Skill** reworded for clarity. Was: "field 4 Stores this battle instead of 3." Now: "bring up to 4 items from the warband's Stores into this battle instead of the standard cap of 3."
- **Stoic Skill removed and replaced with Battle Sense.** Old Stoic ("treat morale 1 as Stoic") was effectively morale immunity, which is already the case for some scenarios. New Battle Sense: "+1 to defence rolls against a charging figure for that round of melee" — focused, useful.

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
