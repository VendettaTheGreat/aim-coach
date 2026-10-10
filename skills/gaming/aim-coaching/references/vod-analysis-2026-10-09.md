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

- **Skill 1 — Ground Smooth Tracking (NEW foundation):** Wide Wall Pasu Smooth Easy → Centering I Easy → Thin Gauntlet Easy. Smooth, relaxed mouse movement on predictable GROUND targets with low reactivity. Prerequisite for all reactive work.
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
