# 06 — Random Tables

Three tables drive the post-game sequence's stochastic elements. All are placeholders for v0.2 with example entries and design notes.

---

## 1. The Saga Injury Table (d20)

Rolled in **Step 1 of the post-game sequence** for each Named Character who fell during the battle. Adapted (and compressed) from Port Royal's d100 Officer Injury Table.

### Design notes

- **Lethality dial:** 1 of 20 slots is "Dead" (5% per knockdown). Over a typical 8-game season, with each Named Character likely going down 2 to 4 times, expect 1 or 2 permanent deaths per warband per season. Enough to keep stakes high; rare enough that named characters can be genuine recurring heroes.
- **Lingering Wounds** are stat penalties that persist until cleared by a Feast Renown spend or by certain Saga Roll results.
- **Permanent results** (lost limbs, scars, vendettas) cannot be removed by a Feast and stay on the character sheet for the rest of the campaign.
- **Healer mitigation:** if your warband includes a surviving Healer at the end of the battle, you may re-roll one Saga Injury result per battle. Pick which character benefits before re-rolling.
- **Multiple knockdowns:** if a Named Character is knocked out and revived (e.g., by Healer effect mid-game) and then knocked out again, they roll on the Injury Table once at the end of the battle, not per knockdown.
- **Modifiers:** none for v0.2. Faction-specific resilience can be added later as Talents (e.g., "Hardy: re-roll one Saga Injury result per season").

### The Table

| d20 | Result | Effect |
|---|---|---|
| 1 | **Dead** | Character is removed from the roster permanently. Triggers Succession if the Chieftain (per [02_XP_and_Advancement.md](02_XP_and_Advancement.md) §6). Any Relic the character wielded drops to the warband's general inventory and may be reassigned. |
| 2 | **Spinal Injury** | Miss the next 2 battles entirely. Returns to play with a permanent -1" movement. |
| 3 | **Lost a Hand** | Miss the next battle. Permanent. Player chooses one when this result is rolled: (a) -1 to all rolls to hit in melee, or (b) character can no longer use a shield. The chosen option is locked in. |
| 4 | **Lost an Eye** | Miss the next battle. Permanent -1 to all ranged hit rolls. Note: characters who never use ranged weapons can convert this to a permanent -1 to defence against missile fire instead. |
| 5 | **Infection** | Miss the next battle. Then at each subsequent post-game, roll d6: on 1, the character dies; on 6, the infection clears; on 2-5, the infection persists and the character cannot field next battle. |
| 6 | **Psychological Trauma** | Permanent. At the start of each subsequent battle, roll a morale check for the character. On a 1, the character flees for the first turn (cannot act). Subsequent turns play normally. |
| 7 | **Bitter Enmity** | Permanent. Character gains a personal Vendetta against the warband that put them down: +1 to hit rolls against any figure from that warband for the rest of the campaign. The targeted warband is recorded on the character sheet. |
| 8 | **Lost Equipment** | Character drops their non-Relic equipment on the battlefield. Repurchase at standard gp cost in the Recruit and Re-equip step. Relics stay with the character (assumed retrieved by retainers). |
| 9 | **Lingering Wound: Movement** | -1" movement until cleared by a Feast (Renown spend per [01_Core_Rules.md](01_Core_Rules.md) §5) or a relevant Saga Roll result. |
| 10 | **Lingering Wound: Aim** | -1 to all rolls to hit (melee and ranged) until cleared by a Feast. |
| 11 | **Lingering Wound: Stance** | -1 to all defence rolls until cleared by a Feast. |
| 12 | **Slow Recovery** | Miss the next battle. No lasting effect after that. |
| 13 | **Slow Recovery** | Miss the next battle. No lasting effect after that. |
| 14 | **Concussion** | Available for the next battle, but cannot act in the first turn (treat as deployed but Down for turn 1, then recovers normally). |
| 15 | **Concussion** | Available for the next battle, but cannot act in the first turn (treat as deployed but Down for turn 1, then recovers normally). |
| 16 | **Full Recovery** | No lasting effect. Cleaned up and back at full strength. |
| 17 | **Full Recovery** | No lasting effect. |
| 18 | **Full Recovery** | No lasting effect. |
| 19 | **Impressive Scar** | Permanent. Character gains the *Inspiring* trait: friendlies within 6" of this character get +1 to their morale checks. Stacks with banners. |
| 20 | **Inspiring Recovery** | Permanent narrative reward: the character's return from the brink stirs the warband. Draw 1 free Boast and add it to your hand for the next battle (respecting the hand size cap). Also gains +1 XP next battle if they deploy. |

### Distribution summary

| Tone | Slots | Probability |
|---|---|---|
| Dead | 1 | 5% |
| Permanent negative (Spinal, Hand, Eye, Infection, Trauma) | 5 | 25% |
| Permanent mixed (Bitter Enmity, Lost Equipment) | 2 | 10% |
| Lingering Wound (recoverable) | 3 | 15% |
| Miss-time only (Slow Recovery, Concussion) | 4 | 20% |
| Full Recovery (clean) | 3 | 15% |
| Permanent positive (Impressive Scar, Inspiring Recovery) | 2 | 10% |

### Interactions with other systems

- A **Healer** in the warband at the end of the battle lets you re-roll **one** Injury result per battle. Pick which character benefits before re-rolling. You must take the second result. Healers do not benefit from their own ability (a wounded Healer is still wounded).
- The **Throw a Feast** Renown spend (2 Renown) clears one Injury per Named Character. This works on Lingering Wounds (slots 9-11) and on miss-time effects from Slow Recovery (12-13) or Concussion (14-15) only if they have not yet resolved. It does NOT clear Permanent results (1-8) or affect Permanent positive results (19-20).
- The **Saga Roll** ([§2 below](#2-the-saga-roll-d100)) may contain entries that clear specific Injury types, including Permanent ones in rare cases.
- A **Commission a Saga** Renown spend (3 Renown) immortalises a Named Character. If they later die (result 1), they still grant +1 morale aura to the warband for the rest of the season.
- Multiple lingering wounds on a single character stack as -1 each in their relevant area. A character with two Movement results loses 2" of movement.

### Edge cases

- **Chieftain killed (result 1):** see [02_XP_and_Advancement.md §6](02_XP_and_Advancement.md). Succession promotes a Named Character to Chieftain; their dormant Talents become active.
- **Healer killed (result 1):** the warband loses Healer access for the rest of the campaign unless a new Healer is recruited from Treasury (standard gp cost).
- **Banner-bearer killed (result 1):** the warband can recruit a new Banner-bearer normally; the existing Banner gp item is recovered (it stayed with retainers).
- **Character with no eyes left (rolls Lost an Eye result while already missing one):** roll the result again. If Lost an Eye comes up a second time, the character is functionally blind and goes Dead.
- **Character with no hands left:** same as above; second Lost a Hand result kills the character.
- **Multiple Bitter Enmity marks:** a character can hold multiple Vendettas against different warbands. The +1 to hit stacks only against the specific warband each mark targets.

---

## 2. The Saga Roll (d100)

Rolled in **Step 5 of the post-game sequence**, once per player. Adapted from Port Royal's Exploration Table and rethemed for Norse/Christendom. This is the connective tissue between Stores, Relics, Boasts, and warband life.

### Design notes

- Distribution: ~40% positive outcomes, ~25% mixed/conditional, ~25% hazards or losses, ~10% rare/special.
- Many entries span multiple d100 slots (common minor effects) while rare/dramatic results occupy single slots.
- Faction-flavored entries appear in the 95+ range, gated by faction or warband composition.
- Two re-roll mechanisms exist for genuinely bad luck: see Mitigation below.

### Mitigation

- A player may **spend 1 Renown to re-roll the Saga Roll once per season** and take the second result. Apply this before any effects resolve.
- The **Throw a Feast** Renown spend (per [01_Core_Rules.md](01_Core_Rules.md) §5) does not affect the Saga Roll directly but can clear Injuries inflicted by it.
- Wyrd is cruel (slots 70–71) explicitly rolls the Saga Roll again and applies the worse result — do not Renown-mitigate within an active Wyrd roll; the re-roll is mandatory.

### The Table

#### Wealth gains (15 slots)

| d100 | Name | Effect |
|---|---|---|
| 01–03 | Successful Trading Season | +50 gp to Treasury. |
| 04–05 | Plundered Hoard | +100 gp to Treasury. |
| 06–07 | Captured Monk | Add a Captured Monk hostage to your warband. He may be sold to another player for 50 gp, ransomed back to a Christian player who holds Bitter Enmity for you for 75 gp, or sacrificed for +1 Renown (Christian faction warbands gain -1 Renown instead). |
| 08–09 | Generous Gift from a Jarl | +30 gp to Treasury, +1 Renown. |
| 10–11 | Sea-Trade Returns | +40 gp to Treasury. |
| 12–13 | Lucky Cache | A buried find. +20 gp to Treasury. |
| 14–15 | Tribute from Vassals | +30 gp to Treasury. |

#### Wealth losses (10 slots)

| d100 | Name | Effect |
|---|---|---|
| 16–17 | Rats Spoil Stores | -25 gp from Treasury (minimum 0). |
| 18–19 | Thief in Camp | -50 gp from Treasury (minimum 0). |
| 20 | Bad Winter | -50 gp from Treasury (minimum 0). |
| 21–22 | Cattle Blight | -30 gp from Treasury (minimum 0). |
| 23 | Famine | Your max army budget for the next battle is reduced by 100 gp. Treasury unchanged. |
| 24 | Your Hall Burns | -50 gp from Treasury, -1 Renown (minimums 0). |
| 25 | A Retainer Flees with Gold | -30 gp from Treasury (minimum 0). |

#### Recruitment and specialists (10 slots)

| d100 | Name | Effect |
|---|---|---|
| 26–27 | Wandering Berserker | A Berserker offers his service. Add a free Named Berserker to your roster (no Treasury cost). He starts with 0 XP. If your roster is full, decline or replace a current Berserker. |
| 28 | Healer Arrives | A Healer joins your warband. Add a free Named Healer to your roster, fully equipped. If your roster already has a Healer, decline or replace. |
| 29 | Warhorn-Bearer | A herald joins. Add a Warhorn special equipment to your inventory, free. He persists between battles. |
| 30–31 | A War-Band Joins | 3 free rank-and-file warriors for the next battle only (full kit, faction-appropriate). They do not count toward your standard army budget. |
| 32 | A Skald Joins | A skald takes residence in your hall. Gain +1 Boast draw per battle for the rest of the season (drawn at the start of each battle, respecting hand size cap). |
| 33–34 | Mercenary Contract | One specialist (Huscarl, Berserker, Pack Master, or Healer; your choice from your faction's list) joins for the next battle at half gp cost from Treasury. After that battle they leave. |
| 35 | Wandering Pack-Master | A dog handler with 3 warhounds joins for one battle, free. After that battle, you may keep him at standard gp cost or release him. |

#### Healing and recovery (10 slots)

| d100 | Name | Effect |
|---|---|---|
| 36–38 | Wise Woman Tends Wounded | Clear 1 Lingering Wound from any Named Character on your roster. |
| 39–40 | Bone-Setter Passes Through | Clear 1 miss-time Injury (Slow Recovery or Concussion) from any Named Character whose effect has not yet resolved. |
| 41–42 | Healing Spring | Clear all Lingering Wounds from one chosen Named Character. |
| 43 | Prayer Answered | Choose one Permanent Injury (slots 2–8 of the Injury Table) on one Named Character. Roll d6: on a 5+, the Injury is cleared. On 1–4, nothing happens. May be attempted once per character per season. |
| 44–45 | Tend the Wounded | Clear 1 Injury of any type (Lingering, miss-time, or permanent-non-fatal) from a Named Character. Permanent results require a d6 5+ as above. |

#### Boasts and inspiration (8 slots)

| d100 | Name | Effect |
|---|---|---|
| 46–48 | A Skald Sings of Your Prowess | Draw +1 Boast for the next battle (respecting hand size cap). |
| 49–50 | A Rival's Challenge | Pick a rival warband. Draw a Bold Boast specific to defeating that warband in your next battle vs them. If you do not face them within 3 battles, the Boast expires unfulfilled. |
| 51–52 | Prophetic Dream | Peek at the next scenario card before its formal draw. May not be shared with other players. |
| 53 | Confessor's Blessing | If you currently hold a captured monk (any source), +1 Renown. Otherwise, draw +1 Boast for next battle. |

#### Relic and Store grants (8 slots)

| d100 | Name | Effect |
|---|---|---|
| 54–55 | Barrow Found | A burial mound is opened. Gain a random unassigned Relic from the campaign's Relic pool. If no Relics remain unassigned, gain 1 free Store of your choice instead. |
| 56–57 | Smith Forges Fine Work | Choose +1 Fire Arrows OR +1 Rune-Stone Store, free. |
| 58–59 | Berserker Mushroom Harvest | +1 Hallucinogenic Mushrooms Store, free. |
| 60 | Saint's Bone Recovered | +1 Captured Saint's Bone Store, free. |
| 61 | Old Weapon Dug Up | Choose +1 Hand Firepot OR +1 Snares Store, free. |

#### Hazards (10 slots)

| d100 | Name | Effect |
|---|---|---|
| 62–63 | Wolves Attack Camp | Lose 1 rank-and-file warrior from your warband (counts as already dead, no replacement needed; if you had no warriors, nothing happens). Gain a wolf pelt worth 30 gp. |
| 64–65 | Storm at Sea | Cannot field cavalry figures in the next battle. |
| 66 | Disease in Camp | One random Named Character (player rolls to determine) gains a Lingering Wound: Stance result. |
| 67 | Rival Raids Your Holdings | Holdings Mode: lose 1 minor Holding you currently control (controlling player chooses which). Otherwise: -50 gp from Treasury (minimum 0). |
| 68–69 | Curse from a Hostile Priest | In your next battle, your opponent gets +1 to their initiative roll for the first 2 turns. |
| 70–71 | Wyrd is Cruel | Roll the Saga Roll again and apply the **worse** result of the two (player decides which is worse). The first roll has no effect. |

#### Reputation and Vendetta (8 slots)

| d100 | Name | Effect |
|---|---|---|
| 72–74 | Blood-Price Paid | Clear 1 Bitter Enmity mark from any Named Character on your roster. |
| 75 | Confessor's Absolution | Clear 1 Bitter Enmity mark from any Named Character on your roster (Norse and Christian warbands both qualify; the absolution may be sought from any priest). |
| 76 | Wandering Avenger Seeks You | One random Named Character on your roster gains a Bitter Enmity mark against a random other warband in the campaign (campaign organiser determines randomly). |
| 77–78 | Your Jarl's Name Spreads | +1 Renown. |
| 79 | Rumor Reaches the Kingdom | Force a re-roll on your next Soubriquet Table result (yours or one inflicted on you). May be banked indefinitely until used. |

#### Narrative and flavor (15 slots)

| d100 | Name | Effect |
|---|---|---|
| 80–81 | Ravens Spotted Overhead | In your next battle, your Jarl gets +1 to their morale check on the first charge they make or receive. |
| 82–83 | A Wandering Monk Asks for Protection | Choose: pay -30 gp to host him (he leaves with blessings), or +2 Renown to refuse and continue raiding (Norse only; Christian factions take -1 Renown instead). |
| 84 | Strange Omens | The campaign organiser adds +1 weather effect to your next battle's weather roll (organiser's choice of which). |
| 85–86 | A Famous Warrior Visits Your Hall | At your next club meeting, you and one consenting opponent may play an extra "duel" mini-scenario (Jarl-vs-Jarl, no retinues). Winner gains +2 Renown, loser gains +1 Renown for the spectacle. |
| 87 | A Bard Composes a Verse | If your Jarl killed an enemy Named Character in your last battle, +1 Renown. Otherwise, no effect. |
| 88–89 | Pilgrim Party Passes Through | Choose: offer hospitality for +1 Renown, or raid them for +30 gp. |
| 90–91 | Strange Weather | In your next battle, you (not the standard roll) choose the weather effect. |
| 92 | Local Thingstead Invites Your Jarl | Your next Renown spend (per [01_Core_Rules.md](01_Core_Rules.md) §5) costs 1 less Renown (minimum 0). |
| 93–94 | Allied Tribute Arrives | +30 gp from a friendly alliance. |

#### Special and faction-flavored (6 slots)

| d100 | Name | Effect |
|---|---|---|
| 95 | Odin's Favor (Vikings only; if not Viking, treat as Pillage rune-mark and gain +20 gp) | In your next battle, one chosen figure ignores their first failed morale check. |
| 96 | Saint's Intercession (Christian factions only — Anglo-Saxons, Normans, Franks, Bretons, Welsh, Romano-British; otherwise treat as omen and gain +1 Boast draw) | In your next battle, one chosen figure may re-roll one failed defence roll. |
| 97 | Fresh Horses (cavalry-heavy warbands — Normans, Huns, or those with 25% cavalry; otherwise treat as +20 gp) | In your next battle, all your cavalry figures gain +1" movement. |
| 98 | A Wise Old Veteran Arrives | Gain a free Bold-tier Boast specific to defeating an "old rival" — the player to your left in turn order. Bonus: +2 Renown instead of +2 if completed. |
| 99 | Council with a Rival | One opponent of your choice may, if both agree, swap one Injury result on a Named Character with one on yours (must be the same Injury tier or worse). Pure negotiation; no forced trade. |
| 100 | The Saga Grows | Roll twice more on the Saga Roll and apply **both** effects (good or bad). If either result is 100, do not roll again — apply twice and stop. |

### TODO (v0.3)

- [ ] Playtest balance. Especially watch slots 06-07 (Captured Monk) for unintended Renown farming.
- [ ] Decide if the player rolls openly or draws privately. d100 implies a roll; a printed Saga Deck is more tactile and lets entries be flavored with art and text.
- [ ] Consider adding 3-5 entries that explicitly trigger a mini-scenario (Cattle Raid, Wagon Train) instead of a flat reward. Could make the Saga Roll a major source of scenario variety.
- [ ] Faction-specific positive entries are concentrated at 95-97; consider spreading mild faction flavor through more slots so factions feel distinct over the season.
- [ ] Holdings Mode interactions are thin. Should slots 67, 92, and others have richer Holdings hooks?
- [ ] Balance check: are wealth gains too generous vs losses? Current ratio is 15:10 in slots, but plunder is also flowing in from raids themselves. May want to soften wealth gains.

---

## 3. The Soubriquet Table (d10 × d6)

Rolled in **Step 10 of the post-game sequence** for players whose victory margin was wide enough. Adapted from Dux Britanniarum's Reputation system.

### Design notes

- Generates a two-part epithet: a d10 roll for an adjective or descriptor, a d6 roll for a noun or qualifier. Player chooses an adjacent cell on either roll (gives narrative control).
- Victors may also assign **unflattering soubriquets** to losers — pick a different cell, applies as a permanent name component for the loser's Chieftain.
- A character with a soubriquet uses it as part of their name forever (Erik becomes *Erik the Bold*, *Sven Bone-breaker*, *Aelfric Dungbreath*).

### Sample d10 table (adjectives — to be expanded)

| d10 | Result |
|---|---|
| 1 | the Cruel |
| 2 | the Bold |
| 3 | the Magnanimous |
| 4 | the Cunning |
| 5 | the Coward |
| 6 | the Pious |
| 7 | the Reckless |
| 8 | the Bald |
| 9 | Dungbreath |
| 10 | the Just |

### Sample d6 table (qualifier — to be expanded)

| d6 | Result |
|---|---|
| 1 | Bone-breaker |
| 2 | Skull-splitter |
| 3 | Raven-friend |
| 4 | Shield-biter |
| 5 | Oath-keeper |
| 6 | Wolf-among-sheep |

### Resolution

A Chieftain typically gets one or the other (not both) from a single roll. If the victor was very dominant, they can grant both halves to themselves. Optional: a Legendary Boast completion grants both halves.

### TODO

- [ ] Build the full d10 table with 10 adjectives and the full d6 table with 6 qualifiers.
- [ ] Decide the victory margin threshold for triggering a roll. (Dux uses +5 or greater victory.)
- [ ] Decide the rule for "loser is named by winner": is it automatic, optional, or a Renown spend?
- [ ] Decide if soubriquets are stackable — does a Chieftain accumulate multiple over a season ("*Erik the Bold, Wolf-among-sheep*"), or just one?
- [ ] Consider faction-flavored sub-tables (Christian soubriquets vs Norse soubriquets).
