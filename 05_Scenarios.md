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

### Plunder Stakes

Winner gains bonus treasure (gp) beyond standard loot extraction.

| Battle Type | Force balance | Description | Reward |
|---|---|---|---|
| **Pillage Town** | Asymmetric, raider-favored | A village or trading post. Loot tokens placed densely on the table; defender protects. Raider's victory condition: extract X loot tokens off own edge. | Standard loot at 5 gp each + 30 gp bonus on win. |
| **Wagon Train Ambush** | Asymmetric, ambusher-favored | A defender's wagon train crosses the table; ambusher must capture or destroy wagons. | Winner gains +50 gp tribute one-time. Standard loot if any wagons looted. |
| **Cattle Raid** | Asymmetric, raider-favored | Defender protects 3 livestock bases; raider attempts to drive 2+ off the opposite edge. Uses Pillage's prisoner-escort movement rules for livestock. | Winner gains the **Cattle Fold Holding** (+10 gp/Winter + 1 free livestock figure in any subsequent Pillage Town or Wagon Train scenario). |

### Glory Stakes

Winner gains significant Renown and triggers a Soubriquet roll. No standard loot expected.

| Battle Type | Force balance | Description | Reward |
|---|---|---|---|
| **Saga Duel** | Asymmetric, attackers smaller | Jarl-vs-Jarl ceremonial fight with retinues that may intervene under specific triggers. Each side fields their Chieftain + 4-6 figures. | Winner gains +3 Renown + free Soubriquet roll. Loser gains +1 Renown for the spectacle. |
| **Rival Warband Feud** | Symmetric | Two equally-budgeted warbands meet on neutral ground for a personal score-settling. | Winner gains +2 Renown + Soubriquet trigger. Standard loot if any present. |
| **Pitched Battle** | Symmetric | Open-field even-budget battle, no specific terrain or objective. Victory by casualty differential. | Winner gains +1 Renown. Standard loot. |

### Holding Stakes

Winner gains a persistent Holding (see §5).

| Battle Type | Force balance | Description | Reward |
|---|---|---|---|
| **Sack the Hall** | Asymmetric, raider-favored | A great hall, lord's seat. Raider must set fire to the primary hall building. Defender protects. | Winner gains the **Burned Hall Holding** (+30 gp + 1 Renown per Winter). Standard loot. |
| **Coast Watch Tower** | Asymmetric, raider-favored | A watch tower with a rolling reinforcement timer. Raider must silence the tower (eliminate all defenders inside) before reinforcements arrive. | Winner gains the **Watch Tower Holding** (+20 gp per Winter). |
| **Storm the Keep** | Asymmetric, defender-favored | A stone keep, fortified building. Attacker storms; defender holds. Uses siege ladder rules from Winding Ways. | Winner gains the **Stone Keep Holding** (+40 gp + 1 Renown per Winter). |

### Relic Stakes

Winner gains a Relic.

| Battle Type | Force balance | Description | Reward |
|---|---|---|---|
| **Sack the Monastery** | Asymmetric, raider-favored | A monastery or abbey holding a relic. Raider must extract the relic figure off their edge OR burn the monastery (if no relic available). Defender's choice: hide-the-relic mode (Christ's Sandals style) or extract-the-relic mode (Sack of Saint Lunaire style). | Winner gains a random unassigned **Relic** from the campaign pool, OR if no Relics are available, gain the **Holy Site Holding** (+20 gp + 1 free Boast draw per Winter). |

### Tribute Stakes

Winner forces a tribute on the loser, paid in the next post-game.

| Battle Type | Force balance | Description | Reward |
|---|---|---|---|
| **Rescue the Hostage** | Asymmetric | A captive (Named Character or civilian) is held in the defender's deployment area. Attacker must extract the captive to their edge. | If attacker wins: defender pays 30 gp tribute or -2 Renown. If defender wins: attacker pays 30 gp or -2 Renown. |
| **Defend the Longship** | Asymmetric, defender-favored | Defender's longship is grounded on the beach; attacker must reach and burn it. Inverse of Landing. | If attacker wins: defender cannot deploy cavalry in their next battle. If defender wins: attacker cannot deploy cavalry in their next battle. |

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

16 Twists. Each Twist applies to one battle and is discarded after.

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
| **Cavalry Arrives** | At the start of turn 5, defender places 3 free cavalry figures within 6" of their table edge (faction-appropriate). |

### Terrain

| Twist | Effect |
|---|---|
| **Marshlands** | Half the table is marshy terrain. Saxon warbands ignore the movement penalty (per Pillage Saxon special rules). |
| **Hilltop Defence** | Defender deploys on a hill (counts as elevation per Pillage's elevation rules). |
| **Burning Building** | One building (defender's choice) starts the game on fire. |
| **Sheep Loose** | 1-2 flocks of sheep on the table per Pillage's Sheep & Beehives rules. Roll d3: 1 flock on 1, 2 flocks on 2-3. |
| **Beehive** | 1 beehive on the table per Pillage's Sheep & Beehives rules. Placed by mutual agreement or coin flip. |

### Force and Composition

| Twist | Effect |
|---|---|
| **Hidden Force** | Defender gains the King of Ambushes Talent free for this battle (may hide up to 25% of their figures per the Talent rules). |
| **Armed Civilians** | 5 NPC armed peasant figures (UA, improvised weapons, 1 HP each) are placed by the defender within their deployment area. They cannot leave the area but defend it normally. They count toward neither side's army size. |

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

**Meanwhile:** Sven proposes a Cattle Raid in Riverbank to Cynewulf, who counter-proposes a Rival Warband Feud in Forest Edge. Sven accepts the counter, no Twist. They play. Cynewulf wins among the trees, gaining +2 Renown and a Soubriquet trigger.

---

## 9. TODO (v0.4)

- [ ] Expand Twist deck to ~25 cards. Current 16 is enough for first playtest but variety will quickly become an issue.
- [ ] Add 3 more Locations: Market Square, Henge, Frozen Lake. (15 in v0.3; aiming for 18 in v0.4.)
- [ ] Add **multi-player Battle Types** for Feuds Mode club nights with odd numbers: a 3-player free-for-all and a 4-player team (2 vs 2).
- [ ] Add faction-flavored Battle Types: a Viking longship raid that only Norse warbands can propose; a "Defend the Pilgrimage" only Christian warbands can defend; etc.
- [ ] Balance the asymmetric force budgets. Default assumption: even gp budgets. Battle Types like Storm the Keep may want explicit asymmetric budgets (defender at 75% of attacker) to be playable.
- [ ] Decide whether the Twist Deck is drawn-and-shuffled (some twists rarer than others) or open-pick (acceptor sees full list and picks). v0.3 says draw 2, keep 1; v0.4 may move to open-pick.
- [ ] Holdings yield cadence: per post-game vs per Winter. v0.3 says per post-game for fast clubs. Locked decision needed before publication.
- [ ] Build a sample first-season set of 6 scenarios as a "ready to play" starter chain for clubs that don't want to compose.