# Aim Theory & Routine Architecture Database

Use this reference to turn a diagnosed aim bottleneck into a low-noise progression. It synthesizes two practitioner sources as hypotheses, not scientific proof, and combines them with task-specific motor-learning principles and live KovaaK's scenario checks. Do not copy a source video's scenario list as a prescription; search the official database by task keyterms and select only what the current weakness needs.

## Source material and limits

- 4BangerKovaaks, **Aim Theory: a Deep Dive in Structure & Aim (Part 1)**, https://www.youtube.com/watch?v=t4MiYcDqYdQ&t=5s — provided transcript discusses evidence-based diagnosis, speed masking errors, confirmation, deceleration, micro-adjustment, overflicking, target switching, and smooth pre-tracking before click timing.
- 4BangerKovaaks, **Aim Theory: a Deep Dive in Structure & Aim (Part 2)**, https://www.youtube.com/watch?v=phLYpHChmnM — provided transcript distinguishes reactive response from post-change smooth tracking, recommends identifying whether the failure is reactivity or the movement after reacting, and separates smooth tracking, speed matching, precision, and mouse/keyboard coordination.
- These are practitioner explanations and programming heuristics. Their specific cues, score targets, scenario counts, and claims are not automatically validated for every player. Use observable performance, task similarity, and transfer checks to decide whether a recommendation fits.

## Core principles

### 1. Diagnose the repeatable failure, not an isolated miss

Record what happens repeatedly and when: lag, overrun at a reversal, delayed reacquisition, shaking, loss of crosshair-on-target time, inaccurate confirmation, or mouse/keyboard decoupling. A whiff, score, hit percentage, or the player's label (“reading issue”) alone does not establish the cause. Ask whether the limit is movement speed, precision, confirmation, reactive response, smooth follow-through, vertical range, or player-input coupling.

### 2. Speed can mask a different bottleneck

Before treating overflicking as a braking problem, test whether movement speed is sufficient for the task. If the player is slow/hesitant, an overly small precision drill may conceal the speed limitation; if accuracy is unstable, first lower one task demand or use a more forgiving target while preserving the required movement. Do not use “go faster” as a universal cue: compare speed and error together, and preserve clean target contact/confirmation.

### 3. Dynamic tension is a controllable spectrum, not a binary

- Aim quality depends on the ability to keep unnecessary baseline clamping low while permitting enough transient activation for controlled movement, braking, and precision. “Relax” does not mean limp; “tense” is not automatically effective or harmful in every instant.
- Train regulation through task design and a simple external cue, not body-part routing, per-bot tension percentages, or continuous conscious pressure changes. This user has a history of high tension and jitter under explicit joint/tension instructions.
- Use the player's subjective grip report as a coaching signal, not an instrumented measure. Current practical guardrail: aim for <=2/10; above 3/10 pause briefly and reset; reduce task demand by one step. If tension persists or control degrades, stop rather than grind.
- At a visible deceleration/arc peak, experiment with releasing the old movement instead of clamping against it, then smoothly follow the new direction. Keep the cue concise: “Stay with the target through the change.” Do not prescribe a specific muscle to tense or release.

### 4. Build the movement before adding reactivity

A reactive task can combine motion range, reversals, acceleration, size/precision, and unpredictability. If the core movement is not yet controlled, adding reactivity merely reproduces the in-game failure at greater complexity. Progress in this order when it matches the observed error:

1. **Isolate the geometric component:** for a vertical-air deficit, start with a horizontal-only air version as a baseline/check; for other errors isolate only the failing dimension that can be removed without changing the task into something unrelated.
2. **Build the core movement:** practice predictable continuous vertical arcs / smooth pursuit without adding abrupt reactive changes. Establish steady crosshair contact and relaxed control through the top/bottom or plane transition.
3. **Scale speed within the same task:** use exact available scenario variants, e.g. title-labeled 80% → 90% → base (interpreted as 100% only when the listing/family supports that relation). Change speed alone; keep geometry and target size stable. Never fabricate an in-game speed slider or infer that an arbitrary title's percentage has universal semantics.
4. **Add controlled variation:** vary one related pattern or direction while preserving the core task; avoid excessive scenario hopping if it obscures the error signal.
5. **Add reactivity:** once smooth core tracking is stable, introduce less predictable/sharper changes to train recognition, release/reorientation, and smooth continuation after the change. The reactive phase tests whether the core skill survives the added demand; it is not a replacement for the core movement phase.
6. **Transfer:** test the same observable outcome in OW2. For the current vertical-arcing deficit, goal = fewer/shorter off-target intervals and cleaner crosshair uptime through the arc and ensuing direction change. Add WASD separately if it is a distinct bottleneck.

This ladder is a task progression, not a calendar promise. Advance on repeatable control, not score alone. If the task breaks down, step back one demand increment.

### 5. Keep skill and scenario task distinct

Use two labels for every drill:

- **Aim mechanic:** continuous tracking, dynamic click-timing, static clicking, target switching, or movement tracking.
- **Movement demand / class hypothesis:** the geometry and scale the mouse movement must cover. Use the local shorthand below to select scenarios; it does not prove that a particular joint must consciously move.

Dynamic click-timing remains smooth pre-tracking with a quiet/silent click; never turn it into flicking or snapping. Target-switching is not continuous tracking just because bots move in arcs. Do not treat scenario tags, title words, ACC, or “Invincible” alone as conclusive: inspect the exact active listing, description, task tags, score/accuracy convention, and whether targets die/switch. For B180 specifically, the user's observed convention is that non-Invincible variants are target-switching/clicking rather than continuous tracking; do not recommend them as smooth tracking without exact verification.

## Joint-class selection shorthand (not a causal anatomy claim)

| Class | Selection role | Geometry/task clue | Guardrail |
|---|---|---|---|
| **1 — Shoulder / forearm** | Broad trajectory and larger arcs | Wide, continuous arcs, air paths, large angular range; vertical or 360-degree pursuit | Keep mouse movement broad enough that a mid-FOV pivot drill cannot substitute for the needed arc. Avoid consciously routing shoulder/forearm. |
| **2 — Wrist** | Mid-FOV control and reversals | Moderate-range changes, controlled directional transitions | Use only when this is the diagnosed demand; a Controlsphere's circular arena may itself include vertical motion, so it can add rather than isolate that demand. |
| **Class 3 — Fingertip** | Small-scale precision / stiction | Tiny targets, micro-corrections, delicate movement | Do not send a player to micro drills for a wide vertical tracking deficit unless precision itself is the limiting factor. |

A scenario can contain blended movement; classify by its dominant intended geometry and identify additional task loads separately. “Class” is a scenario-selection hypothesis, not a claim that one body part alone should act.

### Mechanic-to-class crosswalk (conditional, not anatomical fact)

Aim mechanic and movement class are separate axes; neither “reactive” nor “clicking” has one fixed class. Use the movement's range/scale to make a provisional class assignment:

| Mechanic | Class assignment rule | Example interpretation |
|---|---|---|
| Continuous smooth tracking / speed matching | Class 1 for broad air/vertical arcs; Class 2 for mid-FOV pivots; Class 3 only when micro-scale precision is the diagnosed demand | PGTI/air arcs = Class 1; a mid-FOV Controlsphere task = Class 2 |
| Reactive tracking | Reactivity is an added demand, not a class; assign Class 1/2/3 from the same geometry/scale rule as the core tracking task | Smoothbot Voltaic Reactive = Class 1 because of broad 360-degree air path; a close-range reactive control drill may be Class 2 |
| Target switching | Switching is a distinct task mechanic; assign movement class by cursor travel range and target size, not by target death/ACC | A wide B180 switch task may use Class 1 movement geometry but is not continuous tracking |
| Dynamic click-timing | The click mechanic does not select a class; map the smooth pre-tracking path by its movement range/scale, and preserve quiet confirmation | Broad tracking-to-click path can be Class 1; tiny local pre-track may be Class 3 |
| Static clicking / initial movement and confirmation | Cursor travel and target size determine any movement-class hypothesis; do not equate a static task with Class 3 by default | Wide-wall targets can require broad movement (Class 1); tiny near targets may stress Class 3 precision |
| Mouse + WASD / movement tracking | Player movement is a separate task variable; map mouse range/scale to a class and mark player locomotion independently | A wide dodge-and-track task can be Class 1 plus player movement; do not infer WASD from moving targets |

When a task's range/scale is unknown, record the class as unverified rather than guessing.

## Architecture by diagnosed weakness

| Observable issue | First low-noise test | Progression idea | Do not confuse with |
|---|---|---|---|
| Lag / poor speed match on predictable motion | Smooth, continuous motion at manageable speed | Increase speed within same geometry; then add related variation | A pure visual-reading deficit from score alone |
| Excess motion / overrun at changes | Predictable deceleration and smooth continuation | Then controlled reversals/reactivity at stable speed | Solving by going slower indefinitely or by consciously clamping |
| Vertical arc tension spike | Horizontal-only air baseline → predictable smooth vertical arc | Speed tiers of same arc → reactive vertical change | Reactive air as the starting drill |
| Shaking while still hitting | Simplify one demand; check target contact and size/precision | Reintroduce the pressure-causing demand after smooth contact | “Bad aim” or accuracy alone |
| Poor click confirmation | Pre-track smoothly, confirm target, quiet click; consider low-miss-cost practice | Increase speed only while confirmation persists | Flick/snap instructions; changing continuous tracking dose |
| Mouse aim breaks during WASD | Stationary mouse-only baseline first | Add player movement/keyboard as a distinct variable | Target strafing as proof of player movement practice |
| Target switching accuracy or speed issue | Verify whether task is switching and inspect target count/TTK/size | Increase speed or vary size one step at a time | Treating low-ACC target-switching as continuous tracking |

These are conditional starting tests, not fixed prescriptions. Select only the row supported by repeated observations.

## Routine / “myelin ladder” construction

“Myelin ladder” here is an informal label for progressive, repeatable task practice, not a claim that a specific scenario directly measures myelination.

1. Choose one primary weakness and one external cue.
2. Keep the mechanic and geometry stable across the opening steps; use two or three variants only if each preserves the target skill and improves signal clarity.
3. Start at the easiest verified version that still exposes the movement. If it is too easy, progress the task rather than chasing a score; if form/control fails, step back.
4. Increase one demand at a time: speed, target size, path range, acceleration/unpredictability, duration, then player movement only when appropriate. The order may differ if the diagnosed error requires it, but never combine several new demands without a reason.
5. Exact title-labeled tiers such as PGTI Smoother 80% → 90% → base can form a within-family speed ladder. Treat these as named variants, verify exact titles, and do not infer exact percentage physics beyond what the official listing/title actually establishes.
6. Use a concise observable gate: crosshair remains on or quickly rejoins the target; no repeated clamp/pressure spike; the target feels trackable; errors do not worsen across the block. Scores may supplement but cannot replace this.
7. Keep dose sustainable. Stop/reset on tension escalation, fatigue, or deteriorating control. Do not require the player to complete all listed scenarios if the current workload already includes VAXTA, FFA, or QP.
8. Check transfer with a brief representative OW2 task. Do not claim transfer from a better KovaaK's score alone.

## Live official KovaaK's lookups (Oct 10, 2026)

Queries used (keyterms, not copied source-video lists):
- `site:kovaaks.com/kovaaks/scenarios "Smoothbot Voltaic Easy"`
- `site:kovaaks.com/kovaaks/scenarios "PGTI Voltaic Easy Smoother"`
- `site:kovaaks.com/kovaaks/scenarios "Air CELESTIAL No UFO Easier Bot"`
- `site:kovaaks.com/kovaaks/scenarios "Smoothbot Voltaic Reactive"`
- `site:kovaaks.com/kovaaks/scenarios "Whisphere Small & Slow"`
- `site:kovaaks.com/kovaaks/scenarios "Vertical Smoothing 120 Altered Easy"`
- `site:kovaaks.com/kovaaks/scenarios "VT Controlsphere Viscose Easier"`
- `site:kovaaks.com/kovaaks/scenarios "B180 Voltaic Easy Tracking"`

| Official candidate | Live-observed details | Mechanic / class mapping (interpretation) | Use in a ladder |
|---|---|---|---|
| [`PGTI Voltaic Easy Smoother`](https://kovaaks.com/kovaaks/scenarios?scenarioName=PGTI%20Voltaic%20Easy%20Smoother) | Active; 62,340 entries; Tracking tag; description says tweaked map/bot behavior to feel less RNG/reset-heavy and bot is bigger. Family listing shows 80%, 90%, 70%, and 60% variants alongside base. | Continuous tracking; **Class 1 dominant** where large/vertical arcs are the target demand. Tracking tag and high ACC context align with continuous tracking, but exact bot path still needs in-game inspection. | Strong core movement candidate. Use 80% → 90% → base only as title-labeled family steps and only if each remains controllable. This exact family is directly relevant to current smooth-vertical-first phase. |
| [`Air CELESTIAL No UFO Easier Bot 3`](https://kovaaks.com/kovaaks/scenarios?scenarioName=Air%20CELESTIAL%20No%20UFO%20Easier%20Bot%203) | Active; Tracking tag; description: Air Divine style on Air VL Sparky map, 6% larger and slightly slower than original Air CELESTIAL No UFO Easy. | Continuous air tracking; **Class 1 dominant** by 3D/large-path geometry. | Core/bridge option after PGTI if its path matches and control remains stable. This is easier/larger/slower than its named Easy parent per listing, not a validated exact speed percent. |
| [`Smoothbot Voltaic Easy`](https://kovaaks.com/kovaaks/scenarios?scenarioName=Smoothbot%20Voltaic%20Easy) | Active; Tracking/Smooth Tracking tags. Description: bot spawns at crosshair height, jumps within 1 second of landing, speed capped to reduce prior inconsistencies. Named 80%, 90%, 92%, and other variants appear in family results. | Continuous smooth tracking with jumping/air transitions; **Class 1 dominant**. | Optional clean-core variation if the exact task path matches. Do not infer it is purely vertical or identical to PGTI from the family name. |
| [`Voltaic AC 24 - Smoothbot Voltaic Reactive`](https://kovaaks.com/kovaaks/scenarios?scenarioName=Smoothbot%20Voltaic%20Reactive) | Active; Tracking/Smooth Tracking tags. Description: arm aiming/360-degree air tracking; bot changes direction more frequently and is evasive to promote reactivity. ACC examples roughly 68–76%. | Continuous tracking **with reactive changes**; **Class 1 dominant**, reactive layer added. | Phase 2 candidate only after predictable vertical arc control. Strong example of the same broad movement with more reactivity; not the first isolation drill. |
| [`Whisphere Small & Slow`](https://www.kovaaks.com/kovaaks/scenarios?scenarioName=Whisphere%20Small%20%26%20Slow) | Official result description calls it like Fuglaa XYZ reactive but smooth and without blinks; designed to combine reactive and Air Angelic-like qualities. Exact page details not separately captured in this lookup. | Likely smooth-reactive air tracking; **Class 1 dominant**, but mixed reactive demand. | Do not use as the isolated core step; possible later bridge only after confirming exact listing and path. |
| [`VT Controlsphere Viscose Easier`](https://kovaaks.com/kovaaks/scenarios?scenarioName=VT%20Controlsphere%20Viscose%20Easier) | Prior official cache verification: Tracking listing; invincible flying target moves in varied directions around a circular arena and is repelled from roof/floor. | Tracking with controlled reversals and vertical components; **Class 2 dominant** by taxonomy, but includes vertical travel. | Not a substitute for the Class 1 broad-arc core. Possible later wrist/control variation if the user's vertical handling tolerates it. |
| [`B180 Voltaic Easy Tracking`](https://kovaaks.com/kovaaks/scenarios?scenarioName=B180%20Voltaic%20Easy%20Tracking) | Active page showed 165 entries, ACC around 47–52%, and “Clicking” tag. User's task-specific correction: this exact non-Invincible B180 family member is target switching, not continuous tracking; do not trust the title/tag alone. Its accuracy range is useful only in this scenario's scoring context, not a universal cutoff for identifying other tasks. | Target switching, not continuous tracking; broad arc may be **Class 1 movement geometry**, but mechanic is switching. | Exclude from smooth continuous vertical tracking. Consider only for a separately diagnosed switching goal after exact task verification. |
| `Air Angelic 4 Voltaic Easy Horizontal Only` | Official description says it isolates the horizontal movement of Air Angelic 4 Voltaic; Tracking/Smooth Tracking tags. | Continuous air tracking; broad path can make it **Class 1 by geometry**, while small-target precision may add a Class 3 demand. The dominant class depends on what the session is isolating; do not treat the title as proof of a single joint class. | Useful horizontal baseline/isolation before restoring vertical arcs; not the core vertical step. |
| [`Vertical Smoothing 120 Altered Easy`](https://www.kovaaks.com/kovaaks/scenarios?scenarioName=Vertical%20Smoothing%20120%20Altered%20Easy) | Search result established an active family title but not enough exact description/task detail in this lookup. | Class/mechanic **unverified**. | Do not recommend until exact active page confirms continuous tracking, target path, and difficulty. |

The official categories and score/accuracy data are evidence, not definitive task classifiers. When uncertain, open the exact listing and inspect what the player does, whether targets die/reset, target path and size, and whether keyboard movement is required. Do not infer player WASD from airborne target motion.

## Current case application: vertical tension / Juno arc deficit

The user's current report: horizontal adjustment improved; tension spikes while following continuous vertical arcs/plane changes (Juno circle/oval, Genji and other airborne targets). This is reported as loss of smooth control under vertical path demand; it is not yet proof of a purely mechanical cause or absence of a perception component.

- **Phase 1 — core movement (current):** horizontal-only baseline → PGTI Voltaic Easy Smoother at an appropriate title-labeled speed → same-family faster step, then optionally Air CELESTIAL No UFO Easier Bot 3 if the geometry remains relevant. Cue: “Stay with the target through the arc; keep the crosshair on it at the peak.” Do not add reactive air until this is stable.
- **Phase 2 — reactivity (later):** add a verified reactive air tracking variant (e.g., Smoothbot Voltaic Reactive) to test whether smooth follow-through and tension regulation survive sharper/unpredictable direction changes. This is the 1:1-like transfer layer for Juno, not the foundational movement drill.
- **Success signal:** fewer/shorter crosshair losses through vertical peaks and subsequent direction changes, stable low reported grip, and improved crosshair uptime in the same OW2 context. Do not define success by a target score alone.
- **Do not conflate:** Air reactive scenarios are not automatically “better” because they resemble the fight; first make the base movement controllable, then add the reactive stressor.

## References

- Motor-learning application and cautious evidence framing: `reactive-tracking-evidence.md`.
- Scenario taxonomy, workload, and weekly structure: `weekly-routine.md`.
- User-specific past coaching/transfer history: `past-coaching-history.md`.
