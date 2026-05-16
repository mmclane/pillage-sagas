# 07 — Design Notes

Running design log: open questions, decisions deferred, and the inspirations that shaped the design. Update this file as we resolve questions.

---

## 1. Open design questions

Tracked here so we don't lose threads. Resolved items move to the **Decisions Made** section below.

### Campaign structure

- [ ] **Campaign mode lock-in**: pick one at start vs. let it evolve mid-season? Recommend: lock at start.
- [ ] **Season length**: 6 raids is brisk, 8 is meatier. Open-ended option?
- [ ] **Annual Events**: deck of about 20 cards, or rolled on a table, or scheduled by the organiser?
- [ ] **Roster size and budget**: is 600-800 gp per battle and 2-4 Named Characters the right scale?
- [ ] **Painting requirement**: yes vs. no? (Hobby gate, not rules gate.)

### Boasts

- [ ] **Boast claim**: public-on-trigger (current default, recommended) vs. fully secret until game end?
- [ ] **Hand size**: 1 active (recommended) vs. 2 vs. 3?
- [ ] **v0.1 deck size**: 50 cards before first playtest?

### XP and Talents

- [ ] **Berserker- and Healer-specific Talents**: add them, or stick to Pillage's existing Talent list?
- [ ] **Optional starting Talent for non-Chieftain Named Characters**: yes vs. no?

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

- [ ] **Asymmetric raid scenarios**: how heavily do we lean on them vs. balanced fights?
- [ ] **Scenario Deck composition**: equal probability, weighted, or hand-picked?
- [ ] **Draw mechanic**: random shuffle, weighted random, or player picks from hand?

### Soubriquets

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
- **Saga Roll mitigation → 1 Renown per season to re-roll once.** Gives some agency over bad luck without softening the table. Wyrd is Cruel (slots 70-71) ignores this protection by design.
- **Soubriquet trigger threshold → major victory** = win + (50%+ casualty differential OR Legendary Boast OR killed/captured enemy Chieftain). Multiple trigger paths so the system doesn't favor only kill-heavy playstyles.
- **Soubriquet stacking → max 2 per character.** A third forces the player to drop one. Keeps names readable.
- **Inflicting soubriquets on losers → costs 1 Renown.** Makes the "Dungbreath" effect a deliberate spend, not a free insult.
- **Faction-flavored Soubriquet sub-tables → deferred to v0.3.** The current table has faction-tinted entries in row 7 but is otherwise faction-neutral. Will revisit if playtest shows Christendom and Norse warbands feel undifferentiated.

---

## 3. Sources mined for inspiration

| Source | Type | What we lifted |
|---|---|---|
| **Pillage core rulebook** (Triskell Interactive) | Tactical engine | Tactical engine, faction lists, gp economy, loot mechanics, base scenarios, the Talent list as the seed for XP-purchased advancement |
| **Pillage supplements** | Tactical | *Hecatomb*, *Winding Ways*, *Sheep & Beehives*, *Fall of Rome* — additional scenarios, terrain events, expanded factions, the Sack of Saint Lunaire relic mechanic |
| **Dux Britanniarum** (Too Fat Lardies) | Campaign system | D6 raid scenario template, Soubriquet/Reputation table, Annual Events, recovery-time-as-currency, career path with status unlocks (deferred for v0.2+) |
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
7. **The scenario deck does the heavy lifting.** Most campaign flavor comes from the variety of battles, not from the meta-game. A great Scenario Deck makes a passable engine sing.
