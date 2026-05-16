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

- The table should have a mix of **outright bonuses, conditional opportunities, hazards, and narrative texture**.
- Entries can grant or remove Boasts, Stores, Relics, gp, Renown, Named Characters, or Injuries.
- Some entries should reference scenarios in [05_Scenario_Deck.md](05_Scenario_Deck.md), making them mini-quests.

### Sample entry categories (to be assigned to d100 slots in v0.2)

- **Boast grants** — "A skald sings of your prowess. Draw an extra Boast for next battle."
- **Store grants** — "A trader passes through. Add 1 Store of your choice to your inventory, free."
- **Relic generation** — "An ancient sword is found in a burial mound. Add the Relic [random or chosen] to your warband."
- **Recruitment opportunities** — "A washed-up berserker offers his service. Hire him as a Named Berserker at no Treasury cost."
- **Hostage/ransom hooks** — "Your warband captures a wandering monk. Hold for ransom (50 gp from any other player who wants him) or sacrifice for 1 Renown."
- **Wealth grants** — "A successful trading season. +50 gp to Treasury."
- **Wealth penalties** — "Rats spoil your stores. -25 gp from Treasury." OR "A thief steals from your hoard."
- **Healing** — "A wise woman tends your wounded. Clear one Injury from any Named Character."
- **Hazards** — "Wolves attack your camp. Lose 1 random rank-and-file warrior (no replacement cost) but gain a wolf pelt worth 30 gp."
- **Bitter Enmity removal** — "Blood-price paid" (Norse) or "Confessor's absolution" (Christian): remove one Bitter Enmity mark.
- **Mercenary opportunities** — "A traveling Huscarl offers his sword for 1 battle, 75 gp."
- **Prophetic dreams** — "Peek at the next scenario card before draw."
- **Faction-flavored events** — "An emissary from [random rival faction] requests parley. Make a deal: spend 1 Renown to gain temporary alliance for next battle, or refuse."
- **Holdings hooks** (Holdings Mode) — "Your spies report on a rival's hall. +1 to win conditions if you raid that Holding next."

### TODO

- [ ] Build the full d100 table with one entry per slot.
- [ ] Balance distribution: ~40% positive, ~30% neutral/conditional, ~20% mixed, ~10% hazards/penalties.
- [ ] Decide if the player rolls or draws — d100 implies rolling, but a card deck (Exploration deck) is more tactile.
- [ ] Consider a "re-roll once per season" mechanic so players have some agency over genuinely bad rolls.

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
