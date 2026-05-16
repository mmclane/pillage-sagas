# 05 — Scenarios and Composition

This system replaces the v0.1 random-draw Scenario Deck with a **composition** approach inspired by Blood Eagle's scenario × complication × landscape model. Instead of drawing a card, players compose each battle through a brief negotiation: one player proposes a Battle Type, the other accepts with a Twist. Weather is rolled or chosen. Each Battle Type grants a thematic reward category beyond loot.

There is no map. Holdings — abstract named places a warband controls — accumulate over the season as rewards from specific Battle Types. The campaign's geography lives in the holdings each player has won.

---

## 1. The Composition Procedure

Before each battle, the two players who will fight resolve four steps:

### Step 1: Propose

The **challenger** announces:

- A **Battle Type** from the catalog (§3)
- Their **role** in it (raider or defender, attacker or defender — for asymmetric types only)
- The **target** of the proposal (which opposing player they're challenging)

In Two Sides Mode the target must be on the opposite side. In Feuds Mode the target may be any other player.

The proposal is made openly. Flavor encouraged: "I propose Sack the Hall — I am the raider, you are the defender, I will burn your seat of power for the killing of my kinsman Olaf last summer." A clear in-fiction grievance makes the campaign sing.

### Step 2: Respond

The **target** chooses one of four responses:

- **Accept clean.** No Twist, no modification. The target takes the role the challenger left them. This is rare; the target usually gains an edge by adding a Twist.
- **Accept with a Twist.** The target draws **2 Twist cards** from the Twist Deck (§4), keeps 1, discards the other. The Twist applies to this battle only and is discarded after.
- **Counter-propose.** The target refuses the proposed Battle Type but proposes a different one. The challenger now becomes the target of the counter-proposal and may accept (clean, twist, or counter again). After **2 rounds of counter-proposal**, both players either agree on a third Battle Type or refuse the engagement.
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

Resolve the battle per Pillage rules with the agreed Battle Type, Twist, and Weather. The reward (per §3) is awarded in the post-game sequence.

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

## 4. The Twist Deck

15 Twists. Each Twist applies to one battle and is discarded after.

When accepting a proposal with a Twist, draw 2 and keep 1.

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

---

## 5. Holdings — no map, accumulated rewards

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

## 6. Two-mode interaction

### In Feuds Mode

Any player may propose to any other player. Holdings are individual property and count toward individual Renown.

### In Two Sides Mode

Proposals must be cross-side. Holdings are individual property (the player who won the battle gets the Holding) but Holding bonuses count toward side Renown at season's end.

---

## 7. Worked example

A club meeting with 4 players. Saga Season, Two Sides Mode (Northmen vs Christendom).

**Players:** Erik (Northman), Sven (Northman), Aelfric (Christendom), Cynewulf (Christendom).

**Erik proposes:** "I challenge Aelfric. Sack the Hall — I am the raider, you defend. I want to burn your hall in retaliation for the cattle your men stole last month."

**Aelfric responds:** "I accept with a Twist." He draws 2 Twists: *Snowfall* and *Hidden Force*. He picks *Hidden Force* — gives him the ambush advantage in his own hall.

**Weather:** rolled, comes up 4 (Heavy Rain).

**They play.** Erik wins, burning Aelfric's hall.

**Reward:** Erik gains the **Burned Hall of Cyneford** Holding (+30 gp + 1 Renown per Winter). Erik adds it to his warband sheet.

**Meanwhile:** Sven proposes a Cattle Raid to Cynewulf, who counter-proposes a Rival Warband Feud. Sven accepts the counter, no Twist. They play. Cynewulf wins, gaining +2 Renown and a Soubriquet trigger.

---

## 8. TODO (v0.4)

- [ ] Expand Twist deck to ~25 cards. Current 15 is enough for first playtest but variety will quickly become an issue.
- [ ] Add **multi-player Battle Types** for Feuds Mode club nights with odd numbers: a 3-player free-for-all and a 4-player team (2 vs 2).
- [ ] Add faction-flavored Battle Types: a Viking longship raid that only Norse warbands can propose; a "Defend the Pilgrimage" only Christian warbands can defend; etc.
- [ ] Balance the asymmetric force budgets. Default assumption: even gp budgets. Battle Types like Storm the Keep may want explicit asymmetric budgets (defender at 75% of attacker) to be playable.
- [ ] Decide whether the Twist Deck is drawn-and-shuffled (some twists rarer than others) or open-pick (acceptor sees full list and picks). v0.3 says draw 2, keep 1; v0.4 may move to open-pick.
- [ ] Holdings yield cadence: per post-game vs per Winter. v0.3 says per post-game for fast clubs. Locked decision needed before publication.
- [ ] Build a sample first-season set of 6 scenarios as a "ready to play" starter chain for clubs that don't want to compose.