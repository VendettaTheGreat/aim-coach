# VOD Analysis: FFA Tracer (Oct 2026)

**Video:** https://www.youtube.com/watch?v=42oR5fPEG_k (unlisted, 360p, OW2 FFA custom AIM ARENA Z V3.0, webcam overlay)
**Method:** 49 frames extracted at 2-second intervals across 10 fights. Programmatic pixel-level detection of red health bars (enemy position) + white crosshair pixels near screen center + frame-to-frame offset tracking. 5 parallel vision subagents dispatched; 1 got visual confirmation of 6 frames (Ashe Duel + Tracer Duel 2). Vision backend (z-ai/glm-5.2) intermittently rejected image input.

## Primary Diagnosis

**Systematic tracking lag — crosshair sits consistently lower-left of the target.**

- 88% of frames (43/49): enemy target to the RIGHT of crosshair
- 86% of frames (42/49): enemy target ABOVE crosshair
- 0% of frames: crosshair within 20px of target
- Mean crosshair-to-target distance: 170px (~27% of 640px frame width)
- Offset is directional and consistent, NOT random — this is not jitter or overshoot
- Crosshair rarely crosses through target (0-1 horizontal sign changes per fight)

## Secondary Finding (visual confirmation)

**Reactive overcorrection after perceived miss** (Ashe Duel): crosshair starts significantly left of target (~15-20°), player recognizes miss, grip shifts from relaxed palm → firm claw, correction overshoots above-right. Consistent with MattyOW: "sometimes flicking slightly slower is faster because it preserves smooth transition into tracking."

## Grip Tension

- Generally well-controlled (relaxed palm/claw, no white-knuckling observed)
- Tension accumulates during sustained tracking (Cassidy Duel: webcam edge density rose 29.7→32.7→25.3)
- Genji Duel showed declining tension (26.4→23.8) — possible disengagement from fast-moving target
- Grip is NOT the primary driver of aim errors; movement calibration is

## Fight-by-Fight Data

| Fight | Frames | Mean DX | Mean DY | Mean Dist | Right | Above | Pattern |
|---|---|---|---|---|---|---|---|
| Tracer Duel 1 | 5 | -6 | +47 | 173 | 4/5 | 4/5 | Chaotic, swings wildly |
| Soldier 76 Duel 1 | 5 | -97 | +33 | 185 | 5/5 | 3/5 | Large divergence at 1:17 |
| Vendetta Duel | 5 | -62 | +79 | 140 | 4/5 | 4/5 | Converges, stabilizes above |
| Emre Duel | 5 | -86 | +71 | 157 | 5/5 | 4/5 | Consistent right-above, never crosses |
| Ashe Duel | 5 | -44 | +101 | 167 | 3/5 | 5/5 | Overcorrection: miss left → overshoot right |
| Tracer Duel 2 | 5 | -80 | +121 | 201 | 3/5 | 5/5 | Most consistent vertical bias (std=12) |
| Soldier 76 Duel 2 | 5 | -119 | +95 | 214 | 5/5 | 5/5 | Consistent right-above, no sign changes |
| Kiriko Duel | 4 | -121 | +48 | 169 | 4/5 | 3/5 | Most consistent horizontal bias (std=18) |
| Genji Duel | 5 | -86 | +53 | 139 | 5/5 | 4/5 | Converges at 6:01, stabilizes |
| Cassidy Duel | 5 | -81 | +78 | 159 | 5/5 | 5/5 | Consistent right-above, tension accumulates |

## User-Reported Secondary Deficit (not captured in VOD)

**Wide-arc speed-matching (Mercy Guardian Angel).** User reports shoulder usage is not smooth on wide-arc airborne targets like Mercy GA — not good at speed-matching the arc. The FFA Tracer VOD did not capture this because Tracer fights are ground-level strafes; Mercy GA is a wide airborne arc requiring arm/shoulder to carry the sweep. This is a Class 1 deficit distinct from the Class 2 ground lag.

## Updated Prescribed Plan (Oct 10 v3 — 7-skill course progression)

**Playlist naming convention:** Single linear Skill 1–7 progression (not Week 1–N, not parallel Skill A/B tracks). Each skill is a course module — master Skill N before advancing to Skill N+1. Each skill builds on demonstrated control from the prior skill. Files in KovaaK's Playlists dir: `HermesAimCoach_Skill1-7_*.json`.

- **Skill 1 — Ground Smooth Tracking (NEW foundation):** Centering I Easy → gp close long strafes easy invincible → Thin Gauntlet Easy. Smooth, relaxed mouse movement on predictable GROUND targets with long strafes and low reactivity. Prerequisite for all reactive work. User feedback (Oct 11): `GP Close Long Strafes Easy` (non-invincible) caused reacquisition tension that bled into the next bot's tracking after bot death; swapped to `gp close long strafes easy invincible` (same geometry, no bot death). First in-game transfer signal came from Centering I Easy and Thin Gauntlet Easy.
- **Skill 2 — Ground Reactive Tracking (Class 2):** GP Sparky v3 OW Easier → GP Sparky v3 OW Easy → CFS Easy Inv 15% slower. Primary deficit: systematic tracking lag (crosshair lower-left of target, 88% right, 86% above, 0% on target).
- **Skill 3 — Wide-Arc Speed-Matching (Class 1):** Smoothsphere Viscose Easier 80% → Smoothsphere Viscose Easier → Whisphere Viscose Easier. Secondary deficit: Mercy GA wide-arc shoulder speed-matching.
- **Skill 4 — Faster OW Reactive (Class 2):** GP Sparky v3 OW Invincible 4 → CFS Easy Invincible OW → CFS Invincible. Full-speed ground reactive, surpassing OW2 threshold.
- **Skill 5 — Air Smooth Arc Tracking (NEW foundation):** Air Angelic 4 Voltaic Easy Horizontal Only → PGTI Voltaic Easy Smoother → PGTI Voltaic Easy Smoother 90%. Smooth vertical arc foundation before air reactivity; tension release at arc peaks.
- **Skill 6 — Air Reactive Tracking (Class 1/3):** Air CELESTIAL No UFO Easier Bot 3 → Air CELESTIAL No UFO Easy → Air Voltaic Easy Invincible 4 80%. Bridges smooth air to reactive air with a less-reactive transition.
- **Skill 7 — Ground Movement Tracking (Class 2 + WASD):** Close LS Easy Dodge → Close FS Easy Dodge → Close LS Dodge. Final integration: adds player WASD movement after all stationary tracking skills are mastered.
- **Day 7:** Active rest / OW2 VAXTA Easy bridge (5 min)
- **Cues:** Skill 1: "Keep the crosshair moving smoothly with the target — don't let it stall, don't grip tight." Skill 2/4: "Stay with the target through each direction change — smoothly rejoin, don't snap." Skill 3: "Match the target's speed as it arcs around you — keep the crosshair moving smoothly through the whole arc." Skill 5: "Release grip at the arc peak — let the mouse glide through the direction change, don't clamp." Skill 6: "Stay with the target through the air — release grip at each direction change." Skill 7: "Keep tracking smooth while moving — keyboard movement must not cause mouse-hand grip spikes."
- **Grip ceiling:** 2/10, reset at 3/10, pause 3s + drop speed
- **Advancement:** 3 consecutive focus sessions per skill, zero grip spikes, target motion feels visually easy

## Files
- Frames: `cache/scratch/frames/` (49 PNGs)
- Analysis JSON: `cache/scratch/frame_analysis.json`
- Subagent transcripts: `cache/delegation/live/deleg_c80f9514/`
- Video: `cache/scratch/ffa_tracer_vod.mp4` (360p, 93MB)

## Progress Log

### Oct 11, 2026 — First in-game transfer signal (Skill 1) + user-driven Skill 1 revision
- **Session:** Skill 1 Ground Smooth Tracking (Centering I Easy → GP Close Long Strafes Easy → Thin Gauntlet Easy), ~35 min KovaaK's + VAXTA on VXEAT map (easy strafes, tried to speed up).
- **Transfer:** User reports tracking felt "less effortful / less tense overall" in-game after the session — the first in-game transfer from any coaching approach after months of failed transfer with Serf, PSEV, 4BK, Shotty, Bobo, Shah.
- **Grip:** Mostly calm (≤2/10), a few spikes but user could reset quickly. Not yet zero-spike across a full session.
- **Scores:** No PBs yet. Thin Gauntlet Easy came close: 895 vs 896 PB from 2022.
- **Key user insight — speed-matching is multi-dimensional:** User corrected the Skill 1 framing from "smooth tracking" (one-dimensional, slow) to "speed-matching across a range of speeds." Speed-matching has layers: slow, fast, ground, air. The foundation should train across the range, not just at the slow end, so the base carries into reactive (Skill 2). "The idea is to be smooth but fast cause that way you can translate the skills to reactive better as you'll be able to pick up the pace."
- **GP Close Long Strafes Easy diagnosed:** The bot makes the same strafe at the same speed every time — no tension-transition practice. The reacquisition tension after bot death bled into the next bot's tracking. But the bot death isn't the problem — the lack of variable speed is. The invincible variant was tried and rejected: same strafe, same speed, same tension profile = monotonous, no skill growth.
- **VSS (Variable Speed Strafes) identified by user:** Scenarios where the bot changes its strafe SPEED, forcing the player to read velocity and match tension dynamically. Smooth/non-reactive = the bot changes speed, not direction abruptly, giving processing time to feel and calibrate tension level. This is the speed-matching foundation that carries into reactive.
- **Skill 1 REVISED:** Centering I Easy (slow baseline, one speed) → VSS Close-Mid Long (variable speed, ground, smooth) → Thin Gauntlet Easy (variable speed + precision). Spans the speed-matching range from constant → variable → variable + precision. Playlist updated and verified.
- **Assessment:** Foundation is working but not fully automatic (grip spikes remain). Advancement gate not yet met (needs 3 consecutive sessions with grip ≤2/10 and zero spikes + speed-matching feels calibrated). Plan: 2 more Skill 1 sessions with revised playlist to lock the foundation, then advance to Skill 2 (Ground Reactive). Do not add reactivity until the speed-matching foundation requires zero conscious grip management.

### Oct 11, 2026 — MattyOW VOD analysis: perception-overreaction root cause identified
- **Source:** Twitch VOD 2897460273 (routine building + error ID for Fortnite subscriber Murti, 34cm/360, wrist-oriented).
- **Key finding — perception overreaction:** Matty identified that players misperceive target movement as faster than it actually is → upper-hand tension → less fingertip attention. In-game visual clutter (abilities, building, effects) compounds this. Aim breakdown per Matty: ~50% mental, ~20% perception, ~30% mechanical.
- **User diagnostic insight:** "Targets in VAXTA feel much easier to aim at — in-game, players are actively using their abilities." This is the perception-overreaction pattern: VAXTA = clean perception → accurate speed judgment → no spike. In-game = cluttered perception → speed overestimate → tension overshoot → grip spike → amplified at 20cm/360 (~1.8x crosshair displacement vs 34cm) → tracking degrades.
- **FFA Aim Arena confirmation (Oct 11):** User reports the same grip spikes happen in FFA on Aim Arena (OW physics) but NOT in VAXTA. Same game, same engine, same sensitivity. User clarification: FFA Aim Arena doesn't have much ability visual clutter (no AOE abilities like Sombra's new ability — just primaries, secondaries, and ultimates). The spike is NOT from visual clutter. Three distinct factors contribute:
  1. **Player unpredictability:** VAXTA bots move in readable patterns (predictable strafes, telegraphed direction changes → pre-calibrate tension). FFA players juke, dash, stop suddenly, reverse without telegraph → can't pre-read → forced reactive tension calibration in real-time → spike.
  2. **Competitive pressure:** FFA is a high-pressure scenario — you're getting shot at, there are consequences, physiological arousal is higher. VAXTA is zero-stakes. The body tenses because the situation is tense, not just because the target is unpredictable. This elevated baseline tension means less headroom before a spike.
  3. **Active scanning + engagement load:** In VAXTA, the bot is right in front of you. In FFA, you must actively scan the environment, find players, decide to engage, then track — all while their character movement abilities (dash, blink, jump, wall-ride) change the tracking geometry mid-engagement. The cognitive load before the engagement is higher, so by the time you're tracking, tension is already elevated from the scanning + decision + engagement sequence. Character movement abilities add mid-engagement geometry changes that VAXTA bots don't have.
  - **Refined root cause:** The grip spike is a combination of (1) reactive tension from unpredictability, (2) elevated baseline tension from competitive pressure, and (3) pre-engagement cognitive load from active scanning + movement-ability geometry changes. VAXTA has none of these; FFA has all three. The Skill 1 foundation (VSS) trains pre-read speed calibration in a zero-pressure, predictable, single-target environment. The progression to Skill 2 (reactive) adds unpredictability. In-game (FFA/QP) adds pressure + scanning + movement abilities. Each layer adds a demand that can trigger the spike if the foundation isn't solid enough to absorb it.
- **Root cause revised:** Grip spikes are downstream of perceptual overload, not a pure mechanical deficit. Pure tension-management cues ("relax your grip") address the symptom; the cause is speed misperception under visual complexity. FFA Aim Arena = the perceptual overload environment where this manifests in OW2 specifically.
- **Space-exhaustion cascade (NOT applicable to this player):** Matty's subscriber (34cm) ran out of pad space → upper muscle engaged → burst speed without control → instability. Fix was to raise sensitivity. At 20cm/360, this player is already at the sensitivity level Matty would prescribe — fingertips are forced into micro corrections, pad space is not the constraint. The cascade doesn't apply.
- **Routine structure confirmed:** Matty's "reflex/speed first, precision later, control bleeds into passive tracking" ordering directly validates the current Skill 1→2→3→4 progression. No structural change needed.
- **Revised Skill 1 cue:** "The movement is slower than it feels — match it with tension, not speed. If you feel your grip tighten, the target didn't get faster, your perception did."
- **Full analysis saved to:** `references/mattyow-vod-oct11-stream.md` (10 sections, cross-referenced against `references/mattyow-tension-management.md`).
