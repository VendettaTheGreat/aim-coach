---
name: aim-coaching
description: Use when diagnosing aim and building practice plans.
version: 0.1.0
author: Gabriel, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [aim-training, motor-learning, KovaaKs, Overwatch]
    related_skills: []
---

# Aim Coaching Skill

Turn coach notes and player feedback into cautious, evidence-based motor diagnoses and sustainable aim practice. Match drills to the actual movement geometry, verify scenarios in KovaaK's official database, and account for the player's game workload instead of stacking aim volume automatically.

## When to Use
- Use for aim-coaching notes, VOD observations, player-reported aim errors, and KovaaK's/Overwatch practice plans.
- Don't treat subjective labels such as “bad reading” or “shaky” as a diagnosis without observable evidence.

## Procedure
1. **Extract observations.** Separate what the coach/player directly observed (overshoot, shake, delayed correction, finger clenching, tension growing over a match) from explanations (“reading issue,” joint-use theory, or presumed root cause). State hypotheses as hypotheses; self-report alone cannot establish causation.
2. **Classify the motor skill (Gentile, 2000).** Is the in-game task discrete (static clicking, dynamic click-timing) or continuous (tracking, visual pursuit)? Mercy tracking is continuous. Discrete and continuous skills use different motor programs (PMC3773509) — do not train one to fix the other. Describe a technique as plain task phases, not a coined label or a named player's style. For static clicking, use neutral language such as “initial movement → small correction to finish alignment → confirm alignment → click.” Treat the correction as the usual step; omit it only when the initial movement lands accurately enough to confirm. Do not imply the initial movement alone should routinely land perfectly, or tell the player to flick/snap. For dynamic click-timing, preserve the specific rule: smooth pre-tracking and a silent click, never flicking or snapping. When building speed, improve the whole sequence by removing unnecessary path, corrections, or pauses while preserving alignment and accuracy—not by rushing one phase in isolation.
3. **Identify the target movement pattern.** What shape does the target trace through space? (Leap, bounce, strafe, air/3D, smooth arc, centering/orbit.) This is the primary scenario-selection filter because specificity of practice (Schmidt, 1975) drives transfer — the practiced movement pattern must match the target task's kinematic demands. See the movement-pattern keyword table in `references/weekly-routine.md`.
4. **Identify the smallest testable bottleneck.** Look for when the error begins: target acceleration, reversal, wide displacement, vertical motion, WASD input, session duration, or accumulated fatigue. For reactive tracking, distinguish lag, overshoot at reversals, reacquisition loss, axis-specific errors, and player-input coupling; do not collapse these into generic “slow reaction time.” Do not claim a visual deficit is disproven by errors in other scenarios; scenario performance alone rarely isolates perception from mechanics. Apply the neutral, evidence-calibrated comparison in `references/reactive-tracking-evidence.md`; don't center named players or playstyles.
5. **Ask the player about prior practice before evaluating a routine.** For playlist reviews, routine checks, or coach-note analysis, do not jump straight from the coach's observation to a diagnosis. Use any already-shared experience first, then ask a small number of targeted questions about what the player felt during/after practice, exactly when tension or loss of control began, what target/player movement was happening, and what changed in-game. Avoid asking for information already supplied; distinguish their felt experience from their interpretation of the cause. A player description is valid evidence; gameplay VOD is optional, not a prerequisite. If the user explicitly wants an immediate provisional read, give it with uncertainty and ask follow-up questions for refinement.
6. **Select one physical skill class per session.** Map target geometry and motor demand to the Viscose taxonomy in `references/weekly-routine.md`; never substitute a different class merely to fill a drill slot. Reserve blending for cleared isolated gates. Use Viscose classes as scenario-selection shorthand (which joint complex carries the movement), but ground the diagnostic reasoning in motor learning science (specificity, variable practice, practice load) — not in aim-community buzzwords as the causal model.
7. **Scale and verify scenarios.** Use the new `Recommended KovaaKs Scenarios` sheet's archetype-specific difficulty tiers, chosen from the observed bottleneck and the current variation's challenge/purpose; no player Voltaic rank is required. Treat Novice/Intermediate/Advanced/Elite as scenario-scaling bands, not user labels. Do not use the prior Voltaic scenario spreadsheet. Search candidates through the official general interface at `https://kovaaks.com/kovaaks/scenarios`, using compact family keywords and movement-pattern keywords (leap, bounce, strafe, air, smooth, centering); broaden any query returning fewer than 10 results. Confirm exact active title, task geometry, player movement, and variant settings. Progress within the same archetype when an easier variation no longer challenges the player or has served its purpose and control remains stable; increase one demand at a time. Report official queries and links.
8. **Build the dose around the whole week.** Ask/consider whether the player also does VAXTA, FFA, or QP. Keep the requested 15-minute focused block (three same-class variations, five minutes each) only when it fits their workload. Three same-class variants are a practical way to add controlled variability, not a guaranteed contextual-interference benefit. Evidence on transfer varies by task and setting; keep variants within the required movement pattern and skill demand, and use them only while control remains stable (see `references/reactive-tracking-evidence.md`). Treat an existing 20-minute VAXTA practice as the OW2 translation bridge; do not automatically append another five-minute bridge. Prefer KovaaK's on days without FFA/QP when the player reports tension accumulation.
9. **Ramp one variable at a time.** Start with the easiest verified scenario/speed the player can control. Keep the cue external and simple (smoothly match target motion); avoid simultaneous joint-routing instructions. Apply the grip ceiling/reset/speed gates in the reference when appropriate. Do not invent precision thresholds such as overshoot radii or claim exact “percent speed” settings exist unless verified in the scenario.
10. **Close with a short, actionable plan.** Match answer length to the request: brief symptom update gets a brief adjustment; a requested weekly program gets the full day-by-day structure, progression gates, and OW2 bridge.

## Pitfalls
- **Do not turn a plausible mechanism into a certain diagnosis.** Tension can accompany degraded tracking without proving it caused every miss or excluding a reading component.
- **Do not prescribe more aim work after fatigue signs without checking recovery.** Finger clenching, rising tension, and deteriorating tracking are cues to pause or end that block, not to grind through it.
- **Do not stack 15 minutes of KovaaK's, 20 minutes of VAXTA, and FFA/QP by default.** Total workload and the player's reported deterioration matter more than completing every protocol component.
- **Do not require shoulder/wrist/finger micromanagement or continuous finger motion.** Use one low-tension cue and let the player report whether movement stays relaxed.
- **Do not present arbitrary grip scales as objective measurements.** A 2/10 ceiling is a subjective coaching cue, not a clinical or instrumented reading.

## Verification
- Every diagnosis is traceable to a stated observation, with uncertainty identified.
- Every recommended scenario is live-verified and matches the intended geometry/class.
- The plan preserves one skill class per session and accounts for existing VAXTA/FFA/QP volume.
- The player has a clear stop/reset rule for tension escalation and a measurable, non-fabricated speed progression gate.

For the class taxonomy, scenario search method, and routine integration, read `references/weekly-routine.md`.
For ground-tracking subcategories (Reading, Hybrid, Technique, Fluidity), difficulty bands, and benchmark scenario-role examples, read `references/jade-palace-ground-benchmark.md`; use it as taxonomy, not a literal playlist.
For per-archetype scenario difficulty scaling, read `references/rank-scaled-scenario-guide.md`.
For MattyOW's tension-budget model and speed-matching principles, read `references/mattyow-tension-management.md`.
For reactive tracking diagnosis and the evidence crosswalk between competing correction/target-position ideas, read `references/reactive-tracking-evidence.md`. Treat creator/video strategies as hypotheses, not player-type prescriptions. The source-specific transcript notes remain in `references/riddbtw-smooth-reactive-tracking.md`.
For the Aim Theory & Routine Architecture Database (diagnosis-to-ladder structure, dynamic tension, core-before-reactivity progression, joint-class shorthand, source synthesis, and live scenario candidates), read `references/aim-theory-routine-architecture.md`. Use it as an architecture reference, not a fixed playlist.

## Tension management integration

When the player reports tension rising over a match (not just at one moment), apply MattyOW's tension-budget model:

- **Tension is a budget, not a binary.** Each muscle group (arm, wrist, fingertips) has an independent budget. Using one doesn't exhaust the others — but never releasing any of them leads to gradual lockout.
- **Release tension at direction changes, don't counteract it.** When the target decelerates, let the mouse glide to a near-stop by releasing tension, then redirect in the new direction. Do not fight old momentum with new tension.
- MattyOW describes muscle groups as having separate tension budgets, but treat this as an explanatory model, not an instruction to consciously route joints. Don't infer from this user's finger clenching that a particular arm/wrist budget is depleted.
- **Habitually release tension between engagements.** After a high-tensity exchange, consciously relax before the next one. Nerves encourage holding tension; the habit of releasing is what refills the budget.
- **Minimize tension changes during long strafes.** Any change in tension (how much or where) introduces jitter. Keep tension constant during sustained tracking.
- MattyOW distinguishes lateral from downward grip forces and notes that downward pressure can make tracking feel sticky. Treat this as a cue to experiment gently, not a universal grip prescription; don't ask the player to squeeze the mouse.
- **Finger clenching is an observable warning signal for this player.** Use it as a cue to pause or end the block; it does not prove the cause of their aim errors or which muscle group is responsible.