# 05 — Scenarios and Composition

This system replaces the v0.1 random-draw Scenario Deck with a **composition** approach inspired by Blood Eagle's scenario × complication × landscape model. Instead of drawing a card, players compose each battle through a brief negotiation: one player proposes a Battle Type and a Location, the other accepts with a Twist. Weather is rolled or chosen. Each Battle Type grants a thematic reward category beyond loot.

A composed battle has four layers: **Battle Type** (the objective and reward), **Location** (the venue, with light terrain rules), **Twist** (an acceptor-chosen complication), and **Weather** (rolled).

There is no map. Holdings — abstract named places a warband controls — accumulate over the season as rewards from specific Battle Types. The campaign's geography lives in the holdings each player has won.

---

## 1. The Composition Procedure

Before each battle, the two players who will fight resolve four steps:

### Step 1: Propose

The **challenger** announces:

- A **Battle Type** from the catalog (§3)
- A **Location** from the catalog (§4)
- Their **role** in the Battle Type (raider or defender, attacker or defender — for asymmetric types only)
- The **target** of the proposal (which opposing player they're challenging)

In Two Sides Mode the target must be on the opposite side. In Feuds Mode the target may be any other player.

The proposal is made openly. Flavor encouraged: "I propose Sack the Hall at the Hall Compound — I am the raider, you are the defender, I will burn your seat of power for the killing of my kinsman Olaf last summer." A clear in-fiction grievance makes the campaign sing.

Some Battle Types pair more naturally with some Locations (Sack the Monastery in Monastery Grounds, Storm the Keep at a Stone Keep, etc.). Each Location's entry includes a "Best For" hint, but no pairing is forbidden. A Pillage Town set in Snowy Tundra (a winter raid on an isolated steading) is a different story than the same Battle Type in a Coastal Village — that variety is the whole point.

### Step 2: Respond

The **target** chooses one of four responses:

- **Accept clean.** No Twist, no modification. The target takes the role the challenger left them. This is rare; the target usually gains an edge by adding a Twist.
- **Accept with a Twist.** The target draws **2 Twist cards** from the Twist Deck (§5), keeps 1, discards the other. The Twist applies to this battle only and is discarded after. Some Twists (notably *Change Venue*) modify the Location rather than the battle itself.
- **Counter-propose.** The target refuses the proposed Battle Type and/or Location but proposes a different combination. The challenger now becomes the target of the counter-proposal and may accept (clean, twist, or counter again). After **2 rounds of counter-proposal**, both players either agree on a third combination or refuse the engagement.
- **Refuse the challenge.** The target declines to fight. They lose **1 Renown** (cost of dishonor). The challenger may roll on the Saga Roll for a consolation event. After a refusal, the refusing player may not be a target of any proposal until they propose at least one Battle Type themselves.

### Step 3: Roll Weather

Roll d6 on Pillage's standard weather table (rulebook p.86):

| d6 | Weather |
|---|---|
| 1 | Clear Skies |
| 2 | Fog |
| 3 | Strong Winds |
| 4 | Heavy Rain |
| 5 | Snow |
| 6 | Night |

**Override:** if the Twist imposed a specific weather, skip the roll. If both players agree, weather may be set to Clear Skies without rolling.

### Step 4: Play

Resolve the battle per Pillage rules with the agreed Battle Type, Location, Twist, and Weather. The reward (per §3) is awarded in the post-game sequence.

### Pairing for club meetings

The proposal mechanic doubles as the **pairing mechanism** for a club meeting:

- When players arrive, anyone who wants to fight publicly proposes to a specific opponent.
- Once a proposal is accepted (clean or with a Twist), those two players are paired and head to a table.
- Other players pair up similarly. A club night with 6 players typically generates 3 simultaneous battles.
- If a player isn't proposed to and doesn't propose, the campaign organiser may step in with a randomized pairing or a "you two haven't fought yet" pairing.

---

## 2. Existing Pillage scenarios

The existing Pillage scenarios all slot into the new Battle Type framework as starting points or variants. They are still fully playable:

| Source | Scenario | Maps to Battle Type |
|---|---|---|
| Pillage core | Pitched Battle | Pitched Battle |
| Pillage core | Pillage! | Pillage Town |
| Pillage core | St. Brice's Day Massacre | Sack the Hall (variant) |
| Pillage core | Landing | Pillage Town (variant: coastal) |
| Pillage core | Pilgrimage | Sack the Monastery (variant) |
| Winding Ways | Stamford Bridge | Storm the Keep (variant: bridge defence) |
| Winding Ways | Raise the Flag! | Storm the Keep |
| Winding Ways | The Althing | Saga Duel (variant: 4-player) |
| Winding Ways | Sack of Saint Lunaire | Sack the Monastery |
| Winding Ways | Christ's Sandals | Sack the Monastery (variant: hide-the-relic) |
| Hecatomb | Market Brawl | Rival Warband Feud |

When players agree on a Battle Type, they may use a specific published scenario as the basis or improvise from the Battle Type's description.

---

## 3. Battle Types

12 Battle Types organized by reward category. Each has: a name, reward category, default force balance, brief description, and a target turn limit.

### Quick reference

| Battle Type | Category | Force | Turns | Reward |
|---|---|---|---|---|
| Pillage Town | Plunder | even (800 gp) | 8 | Loot (5 gp each) + 30 gp bonus on win |
| Wagon Train Ambush | Plunder | 600/700 (ambusher / defender) | 6 | 50 gp tribute on win |
| Cattle Raid | Plunder | even (700 gp) + livestock | 6 | Cattle Fold Holding (+10 gp/Winter + free livestock) |
| Saga Duel | Glory | each: Chieftain + 4 fig | 6 | +3 Renown + Title, +1 Renown to loser |
| Rival Warband Feud | Glory | even (700 gp) | 8 | +2 Renown + Title |
| Pitched Battle | Glory | even (800 gp) | 10 | +1 Renown |
| Sack the Hall | Holding | 800/600 (raider / defender) | 8 | Burned Hall Holding (+30 gp + 1 Renown/Winter) |
| Coast Watch Tower | Holding | 700/500 (raider / defender) + reinf. | 6 | Watch Tower Holding (+20 gp/Winter) |
| Storm the Keep | Holding | 1000/700 (attacker / defender) | 10 | Stone Keep Holding (+40 gp + 1 Renown/Winter) |
| Sack the Monastery | Relic | 800/600 (raider / defender) | 8 | A Relic; or Holy Site Holding if pool empty |
| Rescue the Hostage | Tribute | even (700 gp) | 6 | Loser pays 30 gp or -2 Renown |
| Defend the Longship | Tribute | 800/600 (attacker / defender) | 6 | Loser cannot deploy cavalry next battle |

---

### Plunder Stakes

Winner gains bonus treasure (gp) beyond standard loot extraction.

#### Pillage Town

A village or trading post is sacked for whatever wealth can be carried off.

- **Force balance:** Even gp (recommended 800 gp each). Raider may be advantaged by Location (Coastal Village, Trading Town).
- **Turn limit:** 8 turns.
- **Special elements:** 6 to 8 loot tokens placed across the table — in buildings (use Pillage's search rules), at market stalls, on wagons. Half should be visible loot tokens; half should be search-required tokens in buildings or chests.
- **Deployment:** Defender deploys first within 6" of their chosen table edge, OR scattered inside buildings (defender's choice). Raider deploys second within 6" of the opposite table edge.
- **Initiative:** Raider has initiative on turn 1.
- **Victory:**
  - **Raider wins** if 4 or more loot tokens are carried off the raider's own table edge by game end.
  - **Defender wins** if fewer than 4 loot tokens have been extracted by game end.
  - **Tie** if exactly 4 are extracted AND raider has lost more figures than defender (the raid was technically a loss for the raider).
- **Special rules:** Standard Pillage rules for loot tokens, search, building entry, fire, and morale apply. Defender may set their own buildings on fire to deny loot (any defender figure may declare arson on a building they occupy at the start of their movement phase).
- **Reward:** Each extracted loot token converts to 5 gp per Pillage's standard rule (already in the rulebook). If the raider wins, they gain +30 gp bonus to Treasury.

#### Wagon Train Ambush

An ambusher springs from cover on a slow-moving wagon train escorted across the countryside.

- **Force balance:** Ambusher 600 gp, Defender (escort) 700 gp.
- **Turn limit:** 6 turns.
- **Special elements:** 2 wagons (per Pillage's wagon rules) on the table, moving along a "road" path that crosses the table from one edge to the other.
- **Deployment:** Defender places the 2 wagons along the road path, then deploys their escort within 6" of either wagon. Ambusher deploys in 2 separate zones, one on each flank of the road, anywhere more than 8" from a wagon.
- **Initiative:** Ambusher has initiative on turn 1.
- **Victory:**
  - **Ambusher wins** if at least 1 wagon is captured (taken to ambusher's edge or stopped under ambusher control) OR both wagons destroyed (burned).
  - **Defender wins** if both wagons exit through the opposite "road" edge intact.
- **Special rules:** Wagons move 4" per turn unless captured (treat as standard wagon rules). Wagons are flammable (per Pillage's fire rules, ignite on 5+). A wagon is "captured" when a non-defender figure ends its movement phase in base contact with it AND no defender figures are within 2" of the wagon. Once captured, the wagon may be moved by the ambusher at 3" per turn.
- **Reward:** Winner gains +50 gp tribute (one-time, on win). Standard loot if any wagons were captured for their cargo.

#### Cattle Raid

A defender's herd is the target. Raiders attempt to drive the livestock off the table.

- **Force balance:** Even gp (recommended 700 gp each).
- **Turn limit:** 6 turns.
- **Special elements:** 3 livestock figures (cows, pigs, or sheep) placed in the defender's deployment zone. Use Pillage's prisoner-escort rules for moving captured livestock.
- **Deployment:** Defender deploys first within 6" of their edge along with the 3 livestock. Raider deploys second within 6" of the opposite edge.
- **Initiative:** Raider has initiative on turn 1.
- **Victory:**
  - **Raider wins** if 2 or more livestock are driven off the raider's table edge by game end.
  - **Defender wins** if fewer than 2 livestock leave the raider's edge by game end.
- **Special rules:** A defender figure in base contact with livestock prevents capture by the raider; the raider must defeat the guarding figure in melee first. Livestock use Pillage's captured-being movement (4" per turn for cattle/oxen, 6" for adult civilian-equivalents). A figure can escort 1 livestock at a time per Pillage's prisoner rules. Livestock may be killed (to deny the raid, defender takes -1 Renown for each killed). Killed livestock yield no Renown to the raider.
- **Reward:** Winner gains the **Cattle Fold Holding** (+10 gp per Winter, plus 1 free livestock figure to add to any subsequent Pillage Town or Wagon Train Ambush scenario the holder fights in).

---

### Glory Stakes

Winner gains significant Renown and triggers a Title roll. Standard loot is incidental.

#### Saga Duel

Two Jarls and their elite retinues meet in a personal score-settling. Honor is on the line.

- **Force balance:** Each side fields their Chieftain (must be a Named Character) plus exactly 4 figures. Total per side limited to 5 figures regardless of gp cost (each player may field whichever 4 figures they wish from their roster, including additional Named Characters). Optional: each side has a 500 gp soft cap on the 4 figures.
- **Turn limit:** 6 turns.
- **Special elements:** A "duel zone" 6"×6" in the center of the table, marked clearly. Both Chieftains must enter the duel zone by turn 2 or take a -1 to all rolls until they do.
- **Deployment:** Both sides deploy simultaneously within 4" of their respective table edges.
- **Initiative:** Roll-off on turn 1.
- **Victory:**
  - **Side wins** if their Chieftain still stands at game end AND the opposing Chieftain is dead or has fled the table.
  - **If both Chieftains die,** the side with more figures alive wins.
  - **If both Chieftains die and forces are equal,** draw (both sides gain +1 Renown for the spectacle, no Title).
- **Special rules:** Retinue figures may not target the enemy Chieftain in any way (melee, ranged, fire) until turn 3 (the honor of the duel forbids it). Retinues may freely fight each other before then. Chieftains may target each other from turn 1.
- **Reward:** Winner gains +3 Renown and triggers a Title roll for their Chieftain. Loser gains +1 Renown for the spectacle.

#### Rival Warband Feud

A grudge match. Two warbands meet on neutral ground to settle it with steel.

- **Force balance:** Even gp (recommended 700 gp each).
- **Turn limit:** 8 turns.
- **Special elements:** None required beyond Location defaults.
- **Deployment:** Both sides deploy within 6" of opposite edges (chosen by mutual agreement or coin flip).
- **Initiative:** Roll-off on turn 1.
- **Victory:** Side with more figures alive at game end wins. Tie if equal figure counts (no Renown to either side).
- **Special rules:** A major victory is awarded if the winner has 50% or more figures alive than the loser. Major victories grant the Title roll trigger; minor victories grant only the Renown.
- **Reward:** Winner gains +2 Renown. On a major victory, also triggers a Title roll.

#### Pitched Battle

A traditional open-field engagement. No subtlety, just steel and shields.

- **Force balance:** Even gp (recommended 800 gp each).
- **Turn limit:** 10 turns.
- **Special elements:** None required beyond Location defaults.
- **Deployment:** Both sides deploy within 6" of opposite edges (chosen by mutual agreement or coin flip).
- **Initiative:** Roll-off on turn 1.
- **Victory:** Side with more figures alive at game end wins. Margin determines clear vs. minor victory (50%+ margin is clear).
- **Special rules:** Standard Pillage Pitched Battle scenario rules apply (per the core rulebook).
- **Reward:** Winner gains +1 Renown.

---

### Holding Stakes

Winner gains a persistent Holding. The Holding's name is chosen at the moment of victory (Olaf's Hall, the Watch Tower of Cyneford, etc.) and recorded on the winner's warband sheet.

#### Sack the Hall

A great hall, lord's seat, the symbol of a rival's power. Burn it.

- **Force balance:** Raider 800 gp, Defender 600 gp.
- **Turn limit:** 8 turns.
- **Special elements:** 1 great hall building (the primary objective) plus 2-3 outbuildings. The great hall is a fortified building (per Pillage's fortified building rules — fire ignites on 7+ rather than 4+). Defender deploys inside/around the hall.
- **Deployment:** Defender deploys first within 6" of the hall (interior or exterior). Raider deploys second within 6" of any one table edge (defender may dictate which edge if they wish to use terrain to their advantage).
- **Initiative:** Raider has initiative on turn 1.
- **Victory:**
  - **Raider wins** if the great hall is on fire AND still burning at game end.
  - **Defender wins** if the great hall is not burning at game end.
- **Special rules:** The great hall counts as a fortified building. Defender may place loot tokens inside the hall (up to 3) and the raider may attempt to extract them for the standard 5 gp each. The hall's door must be broken to enter (per Pillage's fortified building rules) unless the raider enters through a window (counts as climbing).
- **Reward:** Winner gains the **Burned Hall Holding** (+30 gp + 1 Renown per Winter). The Holding is named at this moment.

#### Coast Watch Tower

A watch tower must be silenced before reinforcements arrive from the village beyond.

- **Force balance:** Raider 700 gp, Defender 500 gp + reinforcements at turn 7.
- **Turn limit:** 6 turns of raid + 2 turns of reinforcement window (8 turns max).
- **Special elements:** 1 watch tower (a small fortified building) where the defender's force starts. Best paired with Highland Crags, Coastal Village, or Lone Hilltop Locations.
- **Deployment:** Defender deploys all figures inside the watch tower or within 4" of it. Raider deploys second within 6" of any one opposite table edge.
- **Initiative:** Raider has initiative on turn 1.
- **Victory:**
  - **Raider wins** if by turn 6 they have either (a) eliminated all defender figures within 4" of the tower or (b) set the tower on fire.
  - **Defender wins** if neither raider victory condition is met by turn 6.
  - From turn 7 onward, defender's reinforcements arrive — 3 free rank-and-file warriors (faction-appropriate, UA, hand weapon) per turn, deploying within 2" of any defender table edge. Raider must withdraw or be overwhelmed. Game ends turn 8 at latest with whatever state stands.
- **Special rules:** The watch tower is a fortified building. The defender begins each turn within the tower with one figure designated as "lookout" — that figure shoots first in the shooting phase (advantage of high ground).
- **Reward:** Winner gains the **Watch Tower Holding** (+20 gp per Winter).

#### Storm the Keep

A stone keep is the seat of regional power. Walls must fall.

- **Force balance:** Attacker 1000 gp, Defender 700 gp (the attacker has the gp advantage to balance the keep's fortifications).
- **Turn limit:** 10 turns.
- **Special elements:** 1 stone keep at the table center surrounded by an outer wall + small courtyard with 1-2 outbuildings. The keep is a fortified building. The outer wall is high — climbable only via siege ladders or dangerous climb (Pillage rules).
- **Deployment:** Defender deploys all figures inside the walls (in the keep, on its roof, in the courtyard, or atop the outer wall). Attacker deploys within 8" of any one table edge.
- **Initiative:** Attacker has initiative on turn 1.
- **Victory:**
  - **Attacker wins** if any of their figures ends a turn on the keep's roof OR all defender figures are eliminated.
  - **Defender wins** if attacker fails to achieve either condition by turn 10.
- **Special rules:** Attacker may purchase up to 3 siege ladders for 50 gp each from their attacker budget. Siege ladders allow figures to climb the outer wall in 2" of movement (per Winding Ways' Raise the Flag rules). Each ladder requires 2+ figures to carry. The keep's door is a fortified door (FA, 1 HP, no defence roll).
- **Reward:** Winner gains the **Stone Keep Holding** (+40 gp + 1 Renown per Winter).

---

### Relic Stakes

Winner gains a Relic from the campaign pool.

#### Sack the Monastery

An abbey holds a sacred relic. Raiders come for it.

- **Force balance:** Raider 800 gp, Defender 600 gp.
- **Turn limit:** 8 turns.
- **Special elements:** A chapel building (the primary objective) plus 2-3 monastic outbuildings. The chapel contains a relic, treated as loot (1 loot token, but worth +3 Renown if extracted alive). Defender's choice of mode at proposal time:
  - **Extract Mode** (default, Sack of Saint Lunaire style): the relic starts inside the chapel; raider searches and extracts.
  - **Hide Mode** (Christ's Sandals style): the relic starts in the chapel; defender attempts to move and hide it during the game; raider must find it before it's hidden.
- **Deployment:** Defender deploys within 6" of the chapel (inside or near). Raider deploys within 6" of the opposite table edge.
- **Initiative:** Raider has initiative on turn 1.
- **Victory:**
  - **Extract Mode:** Raider wins if the relic is carried off the raider's table edge by game end. Defender wins if the relic remains on the table at game end OR is destroyed (chapel burned with relic inside).
  - **Hide Mode:** Defender wins if the relic is hidden before raiders find it (defender's figure carrying the relic ends a turn out of line of sight of all raider figures and declares it hidden). Raider wins if the relic is found and extracted before being hidden.
- **Special rules:** The relic is found in the chapel via a search roll (4+ on Pillage's search table; if rolled 1, the chapel is empty and the raider may try the chapel's other altar/coffer with another search). Once found, the relic is a single loot token. In Hide Mode, the defender may declare the relic hidden if their carrier ends a turn with no enemy line of sight to them; once hidden, raider may still search the chapel for treasure but the relic cannot be found.
- **Reward:** Winner gains a random unassigned **Relic** from the campaign's Relic pool (organiser draws). If no Relics are available, instead the winner gains the **Holy Site Holding** (+20 gp + 1 free Boast draw per Winter).

---

### Tribute Stakes

Winner forces a tribute on the loser. The loser pays in the next post-game sequence.

#### Rescue the Hostage

A captive is held in enemy territory. Pull them out.

- **Force balance:** Even gp (recommended 700 gp each).
- **Turn limit:** 6 turns.
- **Special elements:** 1 captive figure (rank-and-file marker; UA, no equipment, no weapons, 1 HP, cannot attack). The captive is placed in the defender's deployment zone.
- **Deployment:** Defender deploys around the captive within their zone. Attacker deploys within 6" of the opposite table edge.
- **Initiative:** Attacker has initiative on turn 1.
- **Victory:**
  - **Attacker wins** if the captive is extracted off the attacker's table edge.
  - **Defender wins** if the captive remains in defender's territory at game end, OR the captive is killed (intentionally by defender to deny victory, OR by collateral damage from either side).
- **Special rules:** The captive moves at 5" per turn under the standard prisoner-escort rules (Pillage); an attacker figure in base contact may escort them. The captive cannot defend themselves. Defender may attempt to kill the captive in melee or ranged attack (no Renown penalty in this scenario — the defender is desperate). If the captive is killed mid-game, the game continues but defender immediately wins the scenario at game end regardless of other conditions.
- **Reward:** Loser pays 30 gp tribute (immediate, in the post-game sequence) OR -2 Renown if they cannot pay or refuse.

#### Defend the Longship

A defender's longship is grounded on the beach. The attacker must burn it before the tide turns.

- **Force balance:** Attacker 800 gp, Defender 600 gp.
- **Turn limit:** 6 turns.
- **Special elements:** 1 longship (24" × 6" per Pillage's ship rules) beached or grounded on the defender's table edge (or center, depending on Location — Tidal Estuary and Coastal Village pair well). Defender's force begins around or aboard the longship.
- **Deployment:** Defender deploys around the longship within 6". Attacker deploys within 6" of the opposite table edge.
- **Initiative:** Attacker has initiative on turn 1.
- **Victory:**
  - **Attacker wins** if the longship is on fire AND still burning at game end.
  - **Defender wins** if the longship is not burning at game end.
- **Special rules:** The longship counts as a flammable wooden structure. Fire on a longship spreads at +1 to the roll (the timbers are tarred). Defender's figures aboard the longship may shoot from the rails (per Pillage's naval rules) and fight as if defending an obstacle when an attacker boards.
- **Reward:** Loser cannot deploy cavalry figures in their next battle.

---

### Custom Battle Types

The 12 codified Battle Types cover the common cases, but the proposal mechanic was always a negotiation. Players who want a specific scenario the catalog doesn't cover may propose a **Custom Battle Type** in place of a catalog pick.

#### How to propose

In Step 1 of the Composition Procedure (§1), the challenger may declare a Custom Battle Type instead of choosing from the catalog. The challenger specifies:

- A **name** for the scenario (e.g., "Burn the Bridge," "The Witch's Grove").
- A **reward category** from the 5 standard categories: Plunder (gp bonus), Glory (Renown + Title trigger), Holding (a new Holding the winner gains), Relic (a Relic from the campaign pool), or Tribute (forced cost on the loser).
- **Force balance** (gp budgets per side).
- **Turn limit.**
- **Special elements** (any custom terrain pieces, NPC figures, loot placements, etc.).
- **Deployment instructions.**
- **Victory conditions** for both sides.
- **Special rules** (any scenario-specific mechanics).
- **Their role** (raider, defender, attacker — whatever the scenario uses).
- **The reward specifics** (exact gp / Renown / Holding type / Relic / tribute).

#### Response

The target responds as usual but with one extra option:

- **Accept clean** — play as proposed.
- **Accept with a Twist** — same as catalog Battle Types.
- **Counter-amend** — propose changes to any element of the Custom Battle Type (force balance, victory conditions, reward, etc.). The challenger then accepts the amended version, counter-amends back, or refuses. After 2 rounds of amendment, both sides agree on a final form or refuse the engagement.
- **Refuse** — same as refusing any other proposal: -1 Renown to the refuser, locked out of being a target until they propose.

#### Constraints

To keep custom Battle Types fair and consistent with the campaign economy:

- The reward **must map to one of the 5 standard categories**. No inventing rewards like "+10 Renown and a free Relic." A Custom Battle Type cannot grant more than the standard Holding/Relic/Tribute amounts unless both players explicitly agree it's a "Major Stakes" engagement (in which case raise the difficulty proportionally — e.g., add asymmetric force budgets that favor the disadvantaged side).
- **Force budgets** for both sides should sum to no more than about 1600 gp (the average of catalog Battle Types). Higher budgets are allowed if both players want a "Pitched Battle" scale fight.
- **Turn limits** should fall within 4 to 12 turns (catalog range).
- **The campaign organiser may veto** a Custom Battle Type they consider unbalanced or exploitative (e.g., a "Saga Duel" reward category attached to a Pitched Battle setup that gives the proposer easy access to Titles).

#### Archiving

If both players enjoy a Custom Battle Type, they may **submit it to the campaign organiser** for inclusion in the campaign's house-rules supplement. The organiser may then make it available to all warbands for future proposals — effectively growing the catalog from 12 codified Battle Types to 12 plus N homebrew. This is how a campaign's local flavor develops over multiple seasons.

#### Example

Erik wants to fight over a specific battlefield: a frozen river crossing where his Jarl swore an oath to confront Aelfric. None of the 12 catalog Battle Types capture the precise vibe. He proposes a Custom Battle Type:

- **Name:** Oath at the Frozen Ford.
- **Reward category:** Glory.
- **Force balance:** 700 gp each.
- **Turn limit:** 6 turns.
- **Special elements:** 1 frozen river bisecting the table; figures break through on a natural 1 movement roll (Frozen Lake-style mechanic).
- **Deployment:** Both sides deploy within 6" of opposite edges. Both Jarls must be deployed.
- **Initiative:** Roll-off turn 1.
- **Victory:** The side whose Jarl kills the enemy Jarl in single combat (no supporting attackers) wins +3 Renown + Title. If both Jarls survive, side with more figures alive wins +1 Renown. If both Jarls die, the side that drew first blood on the enemy Jarl wins +2 Renown.
- **Special rules:** A Jarl killed by anyone but the enemy Jarl grants the enemy side no Renown bonus.
- **Reward:** Glory (per Saga Duel scaling).

Aelfric responds: "Counter-amend. I want the budgets at 600 gp each instead of 700 — fewer retinue figures so the Jarls actually fight. Otherwise accepted." Erik accepts. They play.

---

## 4. Locations

15 Locations for v0.3. Each Location sets the table's base terrain and applies a light mechanical effect for the duration of the battle. The challenger picks the Location at proposal time; the acceptor may swap it via the *Change Venue* Twist.

A Location's terrain rules apply throughout the battle unless overridden by a Twist (e.g., *Burning Building* still adds a fire to whatever Location is chosen).

### Open country

| Location | Default terrain | Effect | Best for |
|---|---|---|---|
| **Open Steppe** | Flat grassland with 1-2 scattered features (lone tree, scrub, rocks). | Cavalry charge rolls gain +1" to charge distance. Visibility unobstructed. | Pitched Battle, Wagon Train Ambush, Cattle Raid |
| **Snowy Tundra** | Snow-covered plain, 1-2 small drifts or rocks. | Weather is automatically **Snow** for the duration (overrides weather roll). | Pitched Battle, Sack the Hall (winter raid), Wagon Train Ambush |
| **Lone Hilltop** | A single dominant hill rises in the center of the table, roughly 12"-18" across at the base, with gentle slopes on all sides. 1-2 small features elsewhere (a lone tree, a roadside shrine, scattered rocks). | The hill counts as elevation per Pillage's slope rules: figures fighting uphill take -1 to melee hit rolls; figures fighting downhill take no penalty. Charges uphill do not gain the charge bonus. The summit provides clear line of sight across the table. | Pitched Battle, Coast Watch Tower (the tower sits on the hill), Rival Warband Feud, Pilgrimage (uphill shrine) |

### Wilderness

| Location | Default terrain | Effect | Best for |
|---|---|---|---|
| **Marshlands** | Half the table is marshy lowlands; a few firm patches and scattered low trees. | Marsh areas count as difficult terrain. Saxon warbands ignore the penalty per their core rules. | Pillage Town, Defend the Longship, Rival Warband Feud |
| **Forest Edge** | A clearing with dense forest on 2-3 edges, covering ~30% of the table. | Wooded areas count as difficult terrain. Picts and Welsh ignore the penalty. Bows take an additional -1 to hit at long range due to obstruction. | Sack the Monastery (a forest monastery), Saga Duel, Rival Warband Feud |
| **Highland Crags** | 2-3 elevated areas (rocky outcrops, hills), some impassable rocks. | Multiple line-of-sight breakers. Cavalry takes -1" movement on elevated terrain. Picts ignore difficult terrain on rocks per their core rules. | Coast Watch Tower, Rival Warband Feud |
| **Riverbank** | A river bisects the table; 1-2 fords or shallow crossings. | Crossing the river requires a swimming roll (per Pillage's swimming rules) except at the fords, which count as passable obstacles. | Cattle Raid, Rescue the Hostage |
| **Tidal Estuary** | A wide muddy river mouth where freshwater meets the sea. Roughly half the table is shallow water (ankle to knee deep), interspersed with sandbars, low islets, and reed beds. 1-2 beached longships sit on the muddy shore. | Shallow water counts as difficult terrain (per Pillage's marsh rules). No swimming roll is required — the water is too shallow to drown. Saxons ignore the movement penalty per their special rule. Cavalry takes -1" movement throughout. Fire-starting rolls take an additional -2 (everything is damp). Ships may be deployed on the beach edges. | Pillage Town (coastal raid), Defend the Longship, Cattle Raid (cattle bogged crossing) |

### Settled

| Location | Default terrain | Effect | Best for |
|---|---|---|---|
| **Coastal Village** | Beach on one table edge with water beyond; 4-6 small buildings inland; 1-2 fences. | Ships (per Pillage's ship rules) may be deployed by either player on the beach edge. Water counts as impassable except for swimming. | Pillage Town, Coast Watch Tower, Defend the Longship |
| **Trading Town** | 6-8 buildings with lanes between them; market in the center with 2-3 stalls (per Hecatomb supplement) and a well. | Closing shots take an additional -1 penalty due to crowded lanes. Stalls may be used per the Hecatomb scenario rules (barrels, grain sacks, projectile stalls). | Pillage Town, Rival Warband Feud, Market Brawl |
| **Monastery Grounds** | 1 large chapel + 3-4 smaller buildings (dorms, kitchen, scriptorium) + low garden walls. | The chapel always contains a relic-search opportunity (per Pillage's search rules). All buildings are flammable. Civilian non-combatants may be added by the defender as flavor. | Sack the Monastery, Pilgrimage |
| **Hall Compound** | 1 great hall + 2-3 outbuildings (barn, byre, sheds) + low palisade wall around the compound. | The palisade counts as a passable obstacle (2" of movement to cross). The defender deploys inside the compound. | Sack the Hall, Rescue the Hostage |
| **Stone Keep** | 1 fortified stone keep dominating the table + outer wall + small courtyard with 1-2 outbuildings. | The keep is a fortified building (per Pillage's special building rules — fire ignites on 7+, doors must be broken). The outer wall is high (passable only by ladders or dangerous climb). | Storm the Keep |

### Special

| Location | Default terrain | Effect | Best for |
|---|---|---|---|
| **Bridge** | A river bisects the table; 1 main bridge + 0-1 smaller bridges. Steep banks. | Most figures cross via the bridge(s); swimming is possible but bank climbing counts as a passable obstacle. A narrow bridge limits combat to 1-3 figures abreast (player agreement on bridge width). | Pillage Town (coastal raid), Pitched Battle, Storm the Keep (Stamford Bridge style) |
| **Longship Boarding** | Two longships are lashed rail-to-rail in open water, forming a continuous fighting platform. Each ship is approximately 24" long and 6" wide. The deck counts as difficult terrain (per Pillage's ship rules). Water surrounds the ships entirely. | Cavalry may not be deployed. Per Pillage's naval combat rules: the rails between the two ships count as a single passable obstacle (2" of movement to cross), and figures may charge across. Figures pushed off (per Push Back rule) fall overboard — apply Pillage's swimming rules (figures in armor face significant risk). Loot tokens may be placed on enemy deck or below decks. Fire on a ship spreads at +1 to the roll (the timbers are tarred). | Saga Duel, Rival Warband Feud, Defend the Longship (boarding variant), Pillage Town (interception at sea) |

### Notes

- Locations may be re-used freely across the season. There is no "once per season" limit.
- Each player may, before the campaign starts, ban one Location from their personal battles (e.g., "I don't have terrain for a Stone Keep yet"). Bans are mutual: if either player has banned a Location, it can't appear in their battles.
- Pillage's core scenarios that called for specific terrain (Stamford Bridge, Sack of Saint Lunaire, etc.) map naturally onto specific Locations; players may use those scenarios' published terrain layouts when matching Battle Types and Locations.

> **TODO (v0.4):** Add Market Square (a Hecatomb-style standalone marketplace), Henge (sacred stone circle with single-shot effects), and Frozen Lake (figures break through ice on a 1) — three Locations cut from v0.3 for scope.

---

## 5. The Twist Deck

25 Twists. Each Twist applies to one battle and is discarded after.

When accepting a proposal with a Twist, draw 2 and keep 1.

> **Constraint:** Twists may not duplicate the Location's existing effect. For example, you cannot play the *Marshlands* Twist on a Marshlands Location (already marshy); the *Snowfall* Twist on Snowy Tundra (already snowing); etc. If a drawn Twist is redundant with the chosen Location, discard and draw another.

### Weather Twists

| Twist | Effect |
|---|---|
| **Snowfall** | Weather is automatically Snow this battle (no roll). |
| **Storm Rising** | Weather is automatically Heavy Rain. |
| **Night Falls** | Weather is automatically Night. |
| **Foggy Morning** | Weather is automatically Fog. |

### Timing and Reinforcements

| Twist | Effect |
|---|---|
| **Surprise Attack** | Attacker has initiative for the first 2 turns AND defender starts in a single 6"×6" deployment zone instead of their usual area. |
| **Forced March** | Attacker is fatigued: -1 to morale checks for the first 3 turns. |
| **Late Hour** | Game length is reduced by 2 turns from the default. |
| **First Light** | Game length is extended by 2 turns from the default. Both sides have more time to develop their positions. |
| **Cavalry Arrives** | At the start of turn 5, defender places 3 free cavalry figures within 6" of their table edge (faction-appropriate). |
| **Foreign Mercenary** | At the start of turn 3, the acceptor rolls d6: on 4+, a free rank-and-file figure (faction-appropriate, UA, hand weapon + shield + armor, no Named status) appears within 2" of their table edge. On 1-3, no figure appears. |

### Terrain

| Twist | Effect |
|---|---|
| **Marshlands** | Half the table is marshy terrain. Saxon warbands ignore the movement penalty (per Pillage Saxon special rules). |
| **Hilltop Defence** | Defender deploys on a hill (counts as elevation per Pillage's elevation rules). |
| **Burning Building** | One building (defender's choice) starts the game on fire. |
| **Burning Field** | One field on the table starts the game on fire. Counts as a piece of burning scenery for fire spread purposes (per Pillage's fire rules). |
| **Sheep Loose** | 1-2 flocks of sheep on the table per Pillage's Sheep & Beehives rules. Roll d3: 1 flock on 1, 2 flocks on 2-3. |
| **Beehive** | 1 beehive on the table per Pillage's Sheep & Beehives rules. Placed by mutual agreement or coin flip. |
| **Treacherous Footing** | Mud, ice, loose scree, frostbite. Every charge roll this game requires a follow-up d6: on a 1, the charging figure trips. Their charge fails entirely (they don't reach the target) and they cannot attack or take any other action this turn. |
| **Sacred Stone** | A standing stone or ancient marker is placed in the center of the table (impassable). A figure ending a turn in base contact with the stone gains +1 to their next morale check. Killing an enemy in base contact with the stone grants the killer +1 Renown (one-time, first such kill only). |
| **Roving Hounds** | Roll 1d3 at deployment for the number of ownerless warhound figures. Place them at the center of the table, clustered within 2" of each other. They follow Pillage's masterless-warhound rules (FAQ p.80): each hound charges the closest figure of any side within 8" each turn. They never flee and never check morale. Killing a hound grants +1 Renown to the killing warband. |

### Force and Composition

| Twist | Effect |
|---|---|
| **Hidden Force** | Defender gains the King of Ambushes Talent free for this battle (may hide up to 25% of their figures per the Talent rules). |
| **Armed Civilians** | 5 NPC armed peasant figures (UA, improvised weapons, 1 HP each) are placed by the defender within their deployment area. They cannot leave the area but defend it normally. They count toward neither side's army size. |
| **No Cavalry** | Neither side may field cavalry figures this battle. If a player's army was built with cavalry, those figures sit this one out. |
| **Bowmen in Cover** | Defender gains 3 free archer figures (UA, bow, hand weapon, faction-appropriate) placed within their deployment zone. These figures may not move from their starting positions for the duration of the battle. They count toward neither side's army size. |

### Narrative

| Twist | Effect |
|---|---|
| **A Wandering Skald** | A neutral NPC skald figure (UA, no equipment, 1 HP, cannot attack) starts in the center of the table. At the end of each turn, the skald moves d6 inches in a randomly determined direction (scatter die or 1=N, 2=NE, 3=SE, 4=S, 5=SW, 6=NW). If killed by any figure, that warband loses 2 Renown (the gods note ill omens). If escorted off a warband's own table edge using Pillage's prisoner-escort rules, that warband gains 2 Renown (the skald sings their saga). The skald is loot to no one — they're a person. |

### Composition

| Twist | Effect |
|---|---|
| **Change Venue** | The acceptor picks a different Location from the catalog. This overrides the challenger's proposed Location entirely. The new Location's effects apply for the battle. |

---

## 6. Holdings — no map, accumulated rewards

Holdings are abstract named places a warband controls. They are won via specific Battle Types and grant passive yield each Winter (post-game).

### Holding types (v0.3)

| Holding | Source Battle Type | Yield per Winter |
|---|---|---|
| **Cattle Fold** | Cattle Raid | +10 gp + 1 free livestock figure in next applicable battle |
| **Burned Hall** | Sack the Hall | +30 gp + 1 Renown |
| **Watch Tower** | Coast Watch Tower | +20 gp |
| **Stone Keep** | Storm the Keep | +40 gp + 1 Renown |
| **Holy Site** | Sack the Monastery (when no Relic available) | +20 gp + 1 free Boast draw per battle |

### Rules

- Each Holding has a **name** chosen by the holder at the moment of victory (Olaf's Hall, the Hall of Brokenmoor, etc.). The name persists.
- Each player may hold at most **one Holding of each type** at any time. To gain a second Watch Tower, they must first lose their current one.
- Holdings yield in the **Winter** between seasons OR after each post-game (player choice when the campaign starts; recommended: per post-game for fast clubs, per Winter for longer arcs).
- Holdings are **challenge-able**. Any opponent may propose a Battle Type that matches the Holding's source: "I propose Sack the Hall against your Burned Hall of Brokenmoor." Win to take it.
- If the holder loses the challenge, the Holding is destroyed (lost permanently). It does not transfer to the challenger automatically; the challenger may, however, claim it via their victory of the same Battle Type in the future.
- Holdings count toward **Side Renown** in Two Sides Mode (each Holding adds +5 to side score at season's end) and toward **individual Renown** in Feuds Mode (each Holding adds +5 to individual score at season's end).

### Why no map

Pillage's tactical layer doesn't reward map-based campaign play (no movement on a strategic level, no province adjacency, no siege duration). Holdings as abstractions deliver the same flavor — territorial control, places named for the warband — without the bookkeeping overhead. Players who want a map can layer one on top by labeling each Holding with a real-world or fictional location.

---

## 7. Two-mode interaction

### In Feuds Mode

Any player may propose to any other player. Holdings are individual property and count toward individual Renown.

### In Two Sides Mode

Proposals must be cross-side. Holdings are individual property (the player who won the battle gets the Holding) but Holding bonuses count toward side Renown at season's end.

---

## 8. Worked example

A club meeting with 4 players. Saga Season, Two Sides Mode (Northmen vs Christendom).

**Players:** Erik (Northman), Sven (Northman), Aelfric (Christendom), Cynewulf (Christendom).

**Erik proposes:** "I challenge Aelfric. Sack the Hall at the Hall Compound — I am the raider, you defend. I want to burn your hall in retaliation for the cattle your men stole last month."

**Aelfric responds:** "I accept with a Twist." He draws 2 Twists: *Snowfall* and *Hidden Force*. He picks *Hidden Force* — gives him the ambush advantage in his own hall.

**Weather:** rolled, comes up 4 (Heavy Rain).

**They play.** Battle is Sack the Hall in a Hall Compound during Heavy Rain, with Aelfric using Hidden Force to hide a quarter of his defenders. Erik wins, burning Aelfric's hall.

**Reward:** Erik gains the **Burned Hall of Cyneford** Holding (+30 gp + 1 Renown per Winter). Erik adds it to his warband sheet.

**Meanwhile:** Sven proposes a Cattle Raid in Riverbank to Cynewulf, who counter-proposes a Rival Warband Feud in Forest Edge. Sven accepts the counter, no Twist. They play. Cynewulf wins among the trees, gaining +2 Renown and a Title trigger.

---

## 9. TODO (v0.4)

- [x] **Twist deck expanded to 25 cards in v0.3.** Categories: Weather (4), Timing and Reinforcements (6), Terrain (9), Force and Composition (4), Narrative (1), Composition (1). May still want to push to 30+ in v0.4 for richer multi-season play.
- [ ] Add 3 more Locations: Market Square, Henge, Frozen Lake. (15 in v0.3; aiming for 18 in v0.4.)
- [ ] Add **multi-player Battle Types** for Feuds Mode club nights with odd numbers: a 3-player free-for-all and a 4-player team (2 vs 2).
- [ ] Add faction-flavored Battle Types: a Viking longship raid that only Norse warbands can propose; a "Defend the Pilgrimage" only Christian warbands can defend; etc.
- [x] **Battle Type detail completed in v0.3 (each Battle Type has force balance, turn limit, deployment, initiative, victory conditions, special rules, and reward).** Future playtest may adjust gp budgets.
- [ ] Decide whether the Twist Deck is drawn-and-shuffled (some twists rarer than others) or open-pick (acceptor sees full list and picks). v0.3 says draw 2, keep 1; v0.4 may move to open-pick.
- [ ] Holdings yield cadence: per post-game vs per Winter. v0.3 says per post-game for fast clubs. Locked decision needed before publication.
- [ ] Build a sample first-season set of 6 scenarios as a "ready to play" starter chain for clubs that don't want to compose.