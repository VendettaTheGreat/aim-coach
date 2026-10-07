# Aim Routine Design: Taxonomy, Search, and Workload

## Viscose kinetic-chain taxonomy

Map by target geometry and movement demand, not by scenario title alone:

| Class | Target demand | Example anchors | Do not substitute |
|---|---|---|---|
| 1 — Arm/shoulder | Wide arcs / gross trajectory, especially beyond comfortable wrist rotation | Smoothsphere Viscose, Whisphere Viscose, SmoothBot Perfected | A mid-FOV control drill does not satisfy a wide-arc need. |
| 2 — Wrist/pivot | Mid-FOV movement and directional reversals, with the arm acting as a quiet anchor | Leapstrafes Control, Controlsphere SuperbAim Viscose, VT Controlsphere Viscose | A wide 180-degree drill is not a wrist-reversal substitute. |
| 3 — Fingertip/stiction | Small targets, micro-corrections, or delicate movement | Air Angelic 4 Voltaic Easy, cloverRawControl Viscose, Flower | Do not force fingertip drills when the error is primarily wide-arc geometry. |
| 4 — Blending | Multi-joint integration after isolated gates are cleared | PGTI Voltaic Easy Smoother, Air CELESTIAL, RawControlSphere | Use PGTI only when the exact profile fits blending; many PGTI variants are jumper-target tasks, not continuous lines. Do not use as a shortcut around unresolved isolated mechanics. |

Treat this as a coaching taxonomy, not a medical model. A class assignment is a training hypothesis to test, not proof of which joint the player must consciously move.

## Task separation and difficulty-scaled reference

Use the user's current **Recommended KovaaKs Scenarios** sheet (reworked by m0narcS) as an archetype-specific scenario difficulty progression guide: `https://docs.google.com/spreadsheets/d/1AKdZJrjfpfsoFBdN71dS2vCSKS1NKNFFbiQ3_XJnHko/edit?usp=sharing`. Do not use the previously supplied Voltaic scenario sheet. The guide's Novice, Intermediate, Advanced, and Elite tabs are scenario-scaling bands, not a required player rank. Pick the relevant archetype column from the observed issue/coaching notes, then select the easiest suitable variant that still serves the practice purpose. Move to the next appropriate variation when the current one stops being challenging or its purpose has been served, while preserving stable control; no Voltaic rank is needed.

- Treat sheet entries as difficulty-tiered candidates, not proof that the active KovaaK's listing still exists or has the same settings. Search each chosen title in the official KovaaK's general scenario interface and verify the exact current variant before recommending it.
- Separate target movement from player movement: ordinary target tracking does not imply player WASD/dodge; the sheet's Keyboard Strafes/Movement columns are clues to player locomotion, which must be confirmed on the exact official listing.
- The older sheet's difficulty marks, scenario links, and placements are retired as a selection source. Keep the new guide's archetype difficulty tiers as the scaling reference; continue to validate scenarios through KovaaK's.
- In a staged plan, train isolated tracking first; then find a difficulty-appropriate Movement/Keyboard Strafes scenario to test mouse/keyboard decoupling. Cue only: “Dodge as the task asks; keep the mouse movement smooth.”
- Keep vertical-heavy/advanced movement tasks out until easier movement tracking is controlled.

The tab gids and selected difficulty-tier examples are summarized in `references/rank-scaled-scenario-guide.md`.

## Scenario keyword and progression cues

Treat these as **search clues**, then verify the exact scenario/variant because scenario families can mix task types:

- **Bounce, B180, Popcorn, Frog**: usually indicate vertical/leaping/jumping target motion. Distinguish the target's vertical path from whether the player also dodges.
- **VT Plaza, GP, Ground Plaza, Plaza**: ground-only target tracking; these labels describe the target plane, not necessarily smoothness or reactivity. Use the new difficulty guide's Tracking → Reactivity column to choose a tier, then verify the exact Ground Plaza profile on KovaaK's.
- **Controlsphere**: use the new difficulty guide's Tracking → Smoothness & Control column for difficulty-appropriate precision/control candidates; treat Controlsphere as controlled smooth reversals, not a stand-in for Overwatch's sharper ground acceleration.
- Cover both ground and air tracking over a full progression for broad hero transfer, but keep them in separate early sessions: ground isolates horizontal acceleration; air adds vertical target motion. First establish an easy ground reactive baseline, then add an easy Air reactive scenario on another day. Combine ground/air variability only after both are controlled. Keep player-dodge/WASD Air Dodge scenarios distinct from stationary Air tracking scenarios.
- **CLOSE FS/LS Dodge, Supra, FuglaaLGC3/LGC3 Reborn, Stralroom**: ground dodge tracking; player movement is part of the task.
- **Air Dodge, XY, Arc Dodge**: verticality plus dodge; inspect whether each exact variant is tracking, target switching, or clicking.
- **Revolving Strafes, Bounce House, Auto Strafes**: may impose engine-prescribed player movement; separate that from voluntary WASD dodging and from target movement.
- **SmoothBot, Centering, Thin Aiming Long, Long Strafes, Smooth variants**: generally signal speed-matching / smooth tracking. `Thin` and `Small` also signal extra precision demand.

Difficulty and size are separate axes. The guide's Novice/Intermediate/Advanced/Elite tabs scale scenario variations by archetype; they do not require assigning a user rank. Choose the tier from the observed issue and whether the current drill still challenges the intended skill. Start with the easiest variation that serves the goal; when it feels controlled and visually easy, or its purpose has been served, move one step up within that archetype and change only one demand at a time. Use tier changes to supply progressively richer, still-relevant task demands once an easier variation no longer challenges the target skill or has served its purpose; keep control and learning quality ahead of difficulty alone. Keep small/thin precision variants for a deliberate precision phase rather than treating them as automatically bad.

Selection order: (1) aim mechanic, (2) target geometry, (3) player-movement mode, (4) target size/precision, (5) speed and scenario difficulty. Change one of the last two at a time.

### Coach-note scenario selection

A coach note saying “mirror” or suggesting incidental strafes does not make a task a dedicated WASD/dodge scenario. Use the new difficulty guide's Movement → Keyboard Strafes column to identify candidates for player movement, then search the exact title through KovaaK's official scenario interface and verify that the current listing actually includes player WASD/dodge. Do not infer locomotion from a moving target.


## Scenario search terms, official lookup, and cache workflow

**Source rule:** use the user's new `Recommended KovaaKs Scenarios` sheet (`https://docs.google.com/spreadsheets/d/1AKdZJrjfpfsoFBdN71dS2vCSKS1NKNFFbiQ3_XJnHko/edit?usp=sharing`) to calibrate scenario archetypes by the user's observed skill level, replacing the previously supplied Voltaic scenario sheet. Read the matching Novice/Intermediate/Advanced/Elite tab and task column. Then search every chosen candidate through KovaaK's general scenario interface at `https://kovaaks.com/kovaaks/scenarios`; the official active listing remains authoritative for exact title, current availability, description, and settings. EVXL remains secondary only when useful for taxonomy/variant discovery; it does not override the new rank guide or official listing.

Use scenario/category keywords, not the user's full symptom sentence or a long copied phrase. Search queries should return at least 10 results; if a query yields fewer than 10, treat the keyword combination as unoptimal and broaden or switch to a related scenario-family term. The threshold is for finding a useful search space—not permission to choose an unrelated result. Inspect titles/details and preserve the exact mechanic after broadening.

Primary keyword families (starting points, not proof of classification):
- Control/precision tracking: `ControlSphere`, `cloverRawControl`.
- Player-movement aiming: `Dodge` (verify player movement in the exact entry).
- Reactive tracking: `Fast Strafes`, `Short Strafes`, `FS`.
- Smoothness/speedmatching: `Pasu Smooth`, `Smoothbot`, `GliderTrack`, `Smoothsphere`, `Smoothness`, `Smooth`.
- Continuous diagonal/long-angle tracking: search `VAI` (Variable Angle Invincible) and verify a suitable Easy/TE variant. Prefer an Invincible variant for uninterrupted tracking time when the exact entry supports it.
- Jumping diagonal targets: `PGTI` (Popcorn Goated Tracking Invincible) includes jumper-style target motion in relevant variants; do not treat those as continuous-line tracking without checking the exact profile.
- Horizontal continuous tracking: `Centering`, `Thin Gauntlet`, `Thin Long Strafes`.
- Static/click timing: `1wall`, `pokeball`, `static`.
- Target switching: `TS`, `TargetSwitch`, or family terms such as `CowserTS`, `canTS`, `PatTS`, `DevTS`.

For static/clicking scenario names, use the user's suffix rules as provisional decoding clues: number tokens may indicate simultaneous target count; `TE` may mean target small/medium; `S/s` small; `ES/es` extra-small; `Wide` expanded spawn area; `Micro` compact spawn area. Verify each actual scenario page before treating a suffix as universal.

Before searching, check `references/scenario-cache.md` for an existing exact scenario/category. Avoid redundant searches for cached entries unless the user needs a new variant, official listing may have changed, or the cache marks uncertainty. For each new query, use the official general search interface, inspect the exact active result, and record: exact title, canonical page URL, category/task, target geometry, whether player movement is included, precision/size and difficulty labels, and only settings the official page actually states. Label mappings inferred from names or user-provided taxonomy as interpretations, not verified official mechanics. Append/update the cache after the search; do not store unverified spreadsheet-only names as confirmed.

1. Search only within the official interface using scenario-family keywords, never a full issue paragraph. Aim for at least 10 result entries; if fewer, broaden/swap keywords and search again before judging availability. Then inspect the exact variant and narrow by an officially listed Easy/Easier tier where appropriate.
2. Verify spelling, current existence, page/creator, category and description, and distinguish target motion from player movement. Prefer Invincible variants for continuous tracking when the official entry confirms the intended task; distinguish VAI long-angle lines from PGTI jumper trajectories.
3. For a 15-minute practice block, choose up to three verified variants from the same skill class, five minutes each. Start at the easiest appropriate size/speed.
4. If fewer than three appropriate variants are verified, do not substitute another class or invent variants; repeat a verified suitable scenario or use fewer and state the limitation.
5. Report exact terms used and direct official listing links; do not infer settings not shown on the page.

## Session and weekly structure

- A focused KovaaK's block is 15 minutes: three five-minute variations of one class only. Avoid mixing arm, wrist, and fingertip work in one session.
- A six-focus-day rotation can alternate Class A on days 1/3/5 and Class B on days 2/4/6; day 7 is rest or low-intensity game translation. Choose A/B from the observed bottlenecks rather than automatically selecting two classes.
- When the player already does at least 20 minutes of VAXTA, count that as the OW2 translation bridge; do not append a duplicate five-minute bridge unless requested.
- On FFA/QP days, favor the game session plus the player's normal VAXTA warm-up over extra KovaaK's, especially if tension has been building. Do not make a missed KovaaK's block a catch-up obligation.
- If a player says tension increases as a match progresses, test shorter blocks with hands-off breaks and record when the clenching begins. End the block if it returns quickly; don't train through deteriorating control.
- For Tracer/game transfer, check that mouse-hand tension does not spike during WASD, Blink, or target changes. Avoid asking the player to consciously route each joint at once.
- Isolate vertical/bouncing movement as flat horizontal tracking first, then add vertical demand after the horizontal version is controlled.
- For click-timing, train smooth pre-tracking and a quiet click; do not prescribe flicking or snapping.

## Grip and progression gates

- Use a subjective grip ceiling of 2/10 as a simple cue, not an objective measurement. If pressure crosses 3/10, pause for three seconds, reset, and reduce task speed by 5% where the scenario supports speed control. If tension persists, stop the block rather than forcing repetitions.
- Raise speed by 5% only after three consecutive clean two-minute runs in one session with no grip spike above 3/10.
- Advance a skill only after three separate focus sessions at 60% target speed with grip pressure at or below 2/10, no pre-emptive bracing, and target motion feeling easy to track.
- Do not claim the player can configure a percentage speed unless the scenario exposes that control. If not, use a verified easier/slower variant or describe a perceived-speed cue and label it accordingly.
- When FFA produces low initial tension but later clenching and degraded tracking, treat the time course as evidence of accumulating load. Do not declare this proves a mechanical cause or rules out reading demands.
