# 01 — Core Rules

## 1. Core concept

Each player runs a persistent **warband** through a **season** of 6 to 8 battles. Between battles, warbands collect treasure, recruit replacements, earn reputations, and complete private boasts. The season ends in a **Grand Finale** that fields each warband's full strength in one climactic battle.

> **Loot token value (campaign-specific).** Pillage's core rulebook values a loot token at 5 gp ("this value has no effect on the battle, it does open up opportunities for stories and campaigns based on the game's currency" — Pillage p.69). This campaign **doubles that to 10 gp per loot token** so that an 8-game season is financially sustainable. The 5 gp baseline drained Treasury too quickly (3-5 battles to broke). Detailed math in [07_Design_Notes.md](07_Design_Notes.md). If your group finds the 10 gp rate still too tight after playtest, organisers may raise to 15 gp.

Three currencies drive the campaign:

| Currency | Earned by | Spent on |
|---|---|---|
| **Treasure (gp)** | Loot tokens carried off the board at **10 gp each** (campaign rate; see note below), ransoms, holdings tribute, raid scenario rewards | Recruiting replacements, buying equipment, buying Stores, refreshing Boasts, ransoming captured characters back from rivals |
| **XP** | Per Named Character, per battle, based on participation and feats | Talents, individual skills, named-weapon unlocks, personal Saga unlocks (see [02_XP_and_Advancement.md](02_XP_and_Advancement.md)) |
| **Renown** | Per battle: kills, objectives, completed Boasts, holding terrain, captures | Campaign leaderboard, plus optional spends on Bards, Feasts, Skalds, and saga immortalization (see §5 below) |

---

## 2. Campaign modes

Players pick one mode at campaign start. Modes change the wrapping; the core engine is the same.

### 2a. Feuds Mode (free-for-all)

Each player runs an independent warband. Pairings each round are random, chosen, or arranged by mutual challenge. Renown is individual. At season's end the highest-Renown player is **Jarl of the Year** (or equivalent title appropriate to their faction).

### 2b. Two Sides Mode

Warbands are split into two loose coalitions at campaign start (Northmen vs Christendom is the obvious theme, but any two-side narrative works). All scheduled battles are cross-side. Side-aggregate Renown decides a **Season Victory**, and within the winning side an individual **Champion** is named. Within each side, individuals still compete on personal Renown.

### 2c. Holdings are universal, not a separate mode

Both Feuds Mode and Two Sides Mode include **Holdings** — abstract named places a warband wins through specific Battle Types. There is no campaign map; Holdings are won, named, and held in each warband's portfolio. See [05_Scenarios.md §5](05_Scenarios.md) for the full mechanic. Holdings are won during the season (no pre-seeding at campaign start) and grant passive yield (gp and/or Renown) per Winter or per post-game.

In Feuds Mode, Holdings count toward individual Renown. In Two Sides Mode, Holdings count toward side Renown for season-end victory, but remain personal property of the warband that won them.

---

## 3. The warband

Each player maintains a warband sheet with these sections:

### 3a. Treasury (gp)

Starts at **300 gp** at campaign creation, in addition to the standard army-building budget for game one. Persistent between battles. The Treasury is *separate* from the army budget each battle, which is drawn from the Treasury for each game.

### Glossary note: Jarl and Chieftain

The Norse-flavored term **Jarl** and the rules-mechanic term **Chieftain** are used interchangeably throughout these documents. They refer to the same role: the Named Character a player has designated as their army's leader for a given battle. Use whichever reads better in context.

### 3b. Named Roster

Each warband carries a **Named Roster** of warriors who persist between battles. They are *people* with personal sagas — they earn XP, hold Talents and Skills, accumulate Titles, and pass into legend. They are not locked into fixed combat roles; you decide how they are kitted out each battle.

The Named Roster has two kinds of members:

**Characters** (1 to 5; class-flex)
- No fixed class. Each battle, the player chooses how each fielded Character is equipped from any options available to their faction (warrior with Dane Axe, archer, Berserker per Pillage's army-building rules, light cavalry, etc.), paid from the battle's army budget.
- One Character is designated as **Chieftain** at the start of each battle. They take the Chieftain profile from their faction for that battle (more HP, Chieftain-only equipment options). Only that character's Talents fire that game.
- The Chieftain designation does **not persist between battles**. Erik may be Chieftain in Game 1, Sven in Game 2, Erik again in Game 3 — the player picks fresh each time.

**Class-Locked Specialists** (max 1 of each, optional)
- **Healer** — always plays as a Healer when fielded, per Pillage's Healer profile.
- **Banner-bearer** — always carries the army's banner when fielded, per Pillage's Banner rules.
- **Warhorn-bearer** — always carries the warhorn when fielded, per Pillage's Warhorn rules.

A typical warband holds 4 to 5 Characters plus 0 to 3 specialists. Total Named Roster size is therefore roughly 4 to 8 characters.

**Each member of the Named Roster has:**

- A name (player's choice).
- An **XP track**.
- A **Skill list** (max 4; see [02_XP_and_Advancement.md](02_XP_and_Advancement.md)). Some Skills are restricted to specific specialist roles.
- **Stat improvements** (capped per stat).
- A **Named-Weapon Unlock** (max 1; rarely useful for specialists).
- A **Personal Saga** (max 1).
- An **Injury record** (Saga Injury Table results; see [06_Tables.md](06_Tables.md)).
- A **wielded Relic**, if any (see [04_Stores_and_Relics.md](04_Stores_and_Relics.md)).
- **Characters also have** a **Talent slot list** (max 2). Specialists do not earn Talents — they're focused on their craft.

**The bring-or-bench decision:** You choose which Named Characters to deploy each battle. Bringing them earns XP (per [02_XP_and_Advancement.md §2](02_XP_and_Advancement.md)) but risks injury, death, or capture. Bench them, no XP, no risk.

**If all your Characters die in a campaign:** You cannot field a battle without at least one Character (someone must be Chieftain). Recruit a fresh Character for 50 gp from Treasury; they start with 0 XP and no Skills/Talents/etc.

**Army economy (rebuy-then-refund).** Each battle, you assemble your army by paying full Pillage gp prices from your Treasury for every figure you field, equipment and all. After the battle, the gp value of every **surviving figure** returns to your Treasury (this happens in the **Collect Treasure** step of the post-game sequence — see [§6 step 3](#6-the-post-game-sequence)). You effectively pay only for casualties.

- **Surviving figure** = a figure still on the table at game end, OR a figure who went Down but survived their Saga Injury Table roll (Injury results other than "Dead").
- **Killed figure** = a Named Character who rolled "Dead," "Death's Door" resolving to death, or "Infection" resolving to death; or a rank-and-file figure killed during the battle. Their gp value is lost.
- **Captured figure** = held by the enemy, resolved in the **Ransom step** (see [§6 step 4](#6-the-post-game-sequence)). Captured figures' value is NOT auto-refunded — it's either ransomed back or lost.

This framing means:
- Rank-and-file warriors don't have a persistent roster between battles. You just have Treasury, your Named Characters, and a free hand to assemble whatever army your gp affords each game.
- Re-equipping is free between battles (just choose different gear at the next army-build).
- A warband that fights cautiously and loses few figures sees Treasury grow over time. A warband that takes heavy losses bleeds gp.

A Named Character may be equipped from the same options as a rank-and-file warrior (or as a Chieftain / Berserker / etc. when faction rules permit) — only their persistent Skills, Talents, Stat improvements, Named-Weapon Unlocks, and Personal Saga distinguish them.

> **Note on the economy (v0.5):** The rebuy-then-refund model replaces the earlier "buy a fresh army each battle with no refund" rule, which made Treasury unsustainable in 2-3 games. Math examples and balance assumptions are tracked in [07_Design_Notes.md](07_Design_Notes.md).

### 3c. Renown

A running total. Tracked for the campaign leaderboard. May also be spent (see §5).

---

## 4. The season structure

A season is a sequence of **6 to 8 battles**, ending with a **Grand Finale**. The exact cadence depends on how often the club meets.

| Phase | Cadence | What happens |
|---|---|---|
| **Raid** | One per club meeting (or per week) | A single Pillage battle composed via the proposal/accept/twist procedure (see [05_Scenarios.md](05_Scenarios.md)). Post-game sequence resolved after each. |
| **Annual Event** | Every other club meeting (4 per typical season) | The campaign organiser draws and reveals a card from the Annual Events deck before proposals begin (see [08_Annual_Events.md](08_Annual_Events.md)). Affects every warband at once. |
| **Grand Finale** | Season's final battle | A climactic closing battle. **Note (v0.5): current "field your full Treasury and Roster" spec is too big and is being reworked. Direction: expand The Althing Battle Type ([05_Scenarios.md §3 Multi-player Battle Types](05_Scenarios.md)) into a season-ending climax — secret targets, all surviving Chieftains, season-ending stakes. Full design deferred to a later revision.** |

---

## 5. Renown spends

Renown is the campaign leaderboard metric, but it is also spendable between battles for tactical or narrative advantages:

| Spend | Cost | Effect |
|---|---|---|
| **Hire a Bard** | 1 Renown | One-shot for next battle: re-roll one initiative roll. |
| **Commission a Saga** | 3 Renown | Immortalize a Named Character. Even if killed permanently, they grant +1 morale aura to your warband for the rest of the season. |
| **Throw a Feast** | 2 Renown | All Named Characters in your roster heal one Injury (clear one lingering wound from the Saga Injury Table). |
| **Buy an Extra Boast Draw** | 1 Renown | Draw and keep an extra Boast for next game (respecting hand size cap). |
| **Brag at the Mead-Hall** | 1 Renown | Force a rival to draw a multi-game Boast you select from a small pool. (Mean. Optional.) |

---

## 6. The post-game sequence

After every battle, resolve in order. Skip any step that doesn't apply.

1. **Wound Rolls.** Each Named Character who fell rolls on the **Saga Injury Table** ([06_Tables.md](06_Tables.md)).
2. **Tally Renown.** Add up Renown earned during the battle (kills, scenario objectives, terrain held, captures, Boasts completed mid-game).
3. **Collect Treasure.** Three sub-steps:
   - **Loot:** Loot tokens carried off the board convert to gp at **10 gp each** (campaign rate; doubled from Pillage canonical 5 gp for sustainability). Add scenario-specific gold (Plunder Stakes bonuses, etc.).
   - **Refund Survivors:** Add the full gp value (figure + equipment) of every **surviving figure** in your army back to your Treasury. A surviving figure is one still on the table at game end OR a Named Character who went Down but survived their Saga Injury Table roll (any result other than "Dead").
   - **Casualties Lost:** Dead figures' gp value is lost; no refund. Captured figures are not refunded — they're resolved in the Ransom step (next).
4. **Ransom and Relic Transfer.** Resolve captured figures and Relic moves. Captured figures' gp value is **not refunded** in step 3 — their fate is resolved here:
   - **Captured Named Characters**: the original owner may pay half the character's gp cost (figure + equipment) to the captor to ransom them back. The ransomed character returns to the owner's roster (full gp value not refunded — the owner paid half to recover them). Alternatively, the captor may execute the character (captor gains Renown, character is removed from the roster permanently; no gp to either side) or hold indefinitely (character is effectively dead from owner's view; captor gains no gp). See [04_Stores_and_Relics.md §8c](04_Stores_and_Relics.md) for Relic-specific transfer rules.
   - **Captured rank-and-file warriors**: same as Named Characters — owner pays half the figure's gp cost to the captor to ransom. If declined or unaffordable, the captor may sacrifice (+1 Renown to captor) or hold (warrior is lost from owner's view; captor gains no gp). Captured warriors cannot be recruited into the captor's warband — captured enemies don't switch sides.
   - **Net effect of ransom**: ransomed figures save the owner ~50% of replacement cost vs buying a fresh figure. Captors may prefer Renown (sacrifice) over gp (ransom) depending on the warband's needs.
   - **Resolve Relic transfers** per [04_Stores_and_Relics.md](04_Stores_and_Relics.md).
5. **Saga Roll.** Roll d100 on the Saga Roll Table ([06_Tables.md](06_Tables.md)) for a between-game event.
6. **Divide Shares.** Pay your Named Characters their winter share. Shortfall triggers an **Oathbreaking Check**: roll d10 plus shortfall in gp/10; on a fail, one or more Named Characters leave the warband (and may be recruited by a rival next Winter).
7. **Mead-Hall.** Optional: spend gp or Renown to refresh Boasts (see [03_Boasts.md](03_Boasts.md)).
8. **Recruit and Re-equip.** Spend gp on persistent things between battles:
   - **Stores** (single-use consumables, kept until used) per [04_Stores_and_Relics.md Part A](04_Stores_and_Relics.md).
   - **New Named Characters** (replacements for any who died this season; 50 gp each per [02_XP_and_Advancement.md §6](02_XP_and_Advancement.md)).
   - **New class-locked Specialists** (Healer, Banner-bearer, Warhorn-bearer; 50 gp each if not already on the roster).
   - **Permanent equipment upgrades** on Named Characters that you want to lock in (rare — usually you choose equipment fresh each battle since rank-and-file are rebuilt anyway).

   Rank-and-file warriors are not recruited here — they're built fresh from Treasury at army-build before each battle. The rebuy-then-refund model (see [§3b](#3b-named-roster)) handles their economics.
9. **Advancement.** XP-eligible Named Characters spend XP per [02_XP_and_Advancement.md](02_XP_and_Advancement.md).
10. **Reputation Check.** Players whose victory margin was wide enough (TBD threshold) roll on the **Title Table** ([06_Tables.md](06_Tables.md)) for a new epithet. Victors may also assign unflattering titles to losers.
11. **Holdings Updates.** Pay yield (gp + Renown) from any Holdings still held (per [05_Scenarios.md §5](05_Scenarios.md)). If this battle contested a Holding, resolve the change of control.
12. **Draw Next Boasts.** Each player draws 2 and keeps 1 (carried-over multi-game Boasts stay; see [03_Boasts.md](03_Boasts.md)).
