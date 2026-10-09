---
name: kovaaks-playlist-builder
description: Use when making KovaaK's playlist JSON files.
version: 0.1.0
author: Gabriel, Hermes Agent
license: MIT
platforms: [windows]
metadata:
  hermes:
    tags: [KovaaK's, playlists, JSON, aim-training]
    related_skills: [aim-coaching]
---
# KovaaK's Playlist Builder
Create and validate KovaaK's playlist JSON from user-provided scenario names and repetitions. Match the exact schema of the user's supplied template; do not silently rename keys or assume fields from another playlist version.

## When to Use
- The user requests a KovaaK's playlist file, playlist JSON validation, or loading a generated playlist into their game folder.
- Don't use for aim diagnosis alone; load `aim-coaching` for scenario selection and workload fit.

## Prerequisites
- Obtain a sample playlist JSON or identify a known-good playlist in the target game folder.
- Obtain intended playlist name, scenario names, and `play_Count` (repetitions per scenario). If context already supplies these, use it rather than re-asking.
- Only copy into a user-nominated local game directory when the user explicitly authorizes it.

## Procedure
1. **Inspect the template.** Read the complete attached JSON and, if installing, one existing playlist from the target folder. Record exact property casing, required metadata, version, and scenario entry keys. If schemas differ, prefer the user's supplied template as directed and flag uncertainty about game import compatibility rather than silently translating it.
2. **Select and scale scenarios.** For coaching-derived playlists, load `aim-coaching` and consult the user's current difficulty-scaled `Recommended KovaaKs Scenarios` sheet (`https://docs.google.com/spreadsheets/d/1AKdZJrjfpfsoFBdN71dS2vCSKS1NKNFFbiQ3_XJnHko/edit?usp=sharing`) for archetype-specific difficulty; do not use the previously supplied Voltaic scenario sheet. Select the archetype's scenario difficulty tier from the observed issue/coaching notes and whether the easier variation still challenges the intended skill; no user Voltaic rank is required. Design the progression toward smooth AND quick tracking/reacquisition: easier/slower variants are temporary technique launchpads, not a hard speed cap or endpoint. Increase one demand at a time within matching geometry, ordering verified speed variants from slower to faster only where their exact titles/settings support that order. Then verify every exact title through KovaaK's general scenario interface (`https://kovaaks.com/kovaaks/scenarios`) or a current official cache entry. Keep ordinary Tracking distinct from Movement/Keyboard Strafes (WASD/dodge); moving targets do not prove player movement. Parse target geometry, player locomotion, aim mechanic, precision/size and difficulty independently. Check `aim-coaching/references/scenario-cache.md` before searching; after an official search, cache exact title, URL, verified details, and inference labels. Use compact scenario-family keywords, not the full issue description; a query returning fewer than 10 results is unoptimal and must be broadened or changed. No user rank is required; document the selected difficulty band and the observed issue it addresses. Prefer verified Invincible variants for continuous tracking when they match the mechanic; for VAI, interpret the number as the target angle in degrees and choose angles deliberately rather than repeating one blindly. Preserve exact scenario spelling; do not invent aliases or difficulty labels.
3. **Build minimal playlist entries.** Use one scenario object per entry, with the template's exact scenario-name property and play-count property. `play_Count` is the number of repetitions for that scenario entry. Set metadata explicitly using values consistent with the sample; avoid duplicate names unless intentional.
4. **Validate before writing.** Parse with Python's `json` module. Check required root keys against the supplied template, required entry keys, correct types (`scenarioList` list, scenario name string, play count positive integer), non-empty playlist name, unique scenario entries unless intentional, and no comments/trailing commas. Compare generated schema keys to the template. Report the scenario count and total repetitions.
5. **Write safely.** Never overwrite an existing playlist without explicit approval. Write to a new filename in the nominated Playlists directory, or create a draft elsewhere if the format is uncertain. Keep file encoding UTF-8.
6. **Verify the install.** After copying/writing into the game directory, read the exact target file back and parse it again. Confirm path, playlist name, scenario names, repetitions, and parse success before claiming it is installed. Do not claim the game itself imported it unless verified in-game.

## Program architecture: progressive overload toward a clean performance goal
- Design related playlists as an ordered, criteria-based progression toward the user's in-game task, not necessarily as calendar weeks. Document the ultimate task (e.g., smooth, quick Tracer tracking/reacquisition through angle changes and WASD) and what each playlist adds.
- Begin with a manageable, geometry-matched version to establish clean technique, then progressively increase one demand (speed, acceleration, angular range, unpredictability, precision, duration, or player movement) while keeping the core task specific. Every playlist should inherit a demonstrated capability from the prior phase and add a deliberate overload; avoid a collection of unrelated easy drills.
- Include form checks and advancement criteria based on observable control (accuracy/time on target, lag vs overshoot/reacquisition, relaxed mouse control, and game transfer), not score alone. If form breaks, step back one increment and rebuild; easy variants are not a permanent speed cap. The endpoint is the quickest representative task the player can execute cleanly.
- Keep speed suffix semantics grounded in verified active settings; otherwise mark speed ordering as a coaching interpretation, not a proven scenario property.
- For ground tracking, consult `aim-coaching/references/jade-palace-ground-benchmark.md` to distinguish Reading, Hybrid, Technique, and Fluidity demands and to interpret Entry/Easy/Hard as scenario bands rather than player ranks. Treat its scenario lists as benchmark examples, not literal routine prescriptions; verify active titles and choose variants that progressively overload the user's task.

## Generated-file discoverability and revisions
- Prefix every generated KovaaK's playlist filename with the stable, searchable tag `HermesAimCoach_`; use a clear suffix such as `HermesAimCoach_Skill1_Ground_Reactive_Tracking_YYYYMMDD.json`. Keep this tag in the filename, not as an invented JSON field, so the user's playlist schema remains unchanged.
- **Naming convention:** Use a single linear Skill 1–N progression (not Week 1–N, not parallel Skill A/B tracks). Each skill builds on the previous one — master Skill N before advancing to Skill N+1. The `playlistName` inside the JSON must match the filename's Skill number. This makes the progression chain visible in both the file system and in-game.
- When the user gives feedback, search for prior generated files by the `HermesAimCoach_` prefix and revise the relevant scenario entries. Week 1–5 plans are not frozen: update them when feedback calls for a change, even if the plan/file has already been shared or posted elsewhere.
- Preserve the prior version by default and create a clearly named revision; only overwrite a user's file when they explicitly request replacement. Prepare the local playlist file with the revised scenarios and deliver it for the user to upload/update on KovaaK's with the in-game button. Do not attempt to edit or publish the online playlist yourself unless the user separately requests that workflow.

## Benchmark playlists and review
- Keep a benchmark short and diagnostic: usually 3–5 scenarios, one run each, spanning only the skills the user wants to monitor. Avoid turning it into another high-volume training routine.
- Freeze scenario variants, ordering, sensitivity/FOV, and repetitions across checks. Run after a training phase or about every two weeks, preferably rested and not immediately after a long FFA/QP session.
- Select benchmark items from separate dimensions when relevant (smooth tracking, ground/air reactive tracking, player-dodge movement, precision). Don't mistake a scenario's easy/hard or rank for its task category.
- Pair the playlist with a short VOD note sheet: scenario start/end times, score/accuracy if visible, first clear overshoot/undercorrection, first sustained crosshair loss, and when the player notices tension rising. Ask for hand-cam only if direct grip observation is needed; gameplay-only video cannot prove grip mechanics.
- After writing, validate the file as usual and tell the user the benchmark's in-game acceptance has not been tested unless it was actually opened in KovaaK's.

## Online publication and account metadata
- A locally written JSON does not create a valid online `playlistId`, `authorSteamId`/author name, or `shareCode`; KovaaK's assigns these when the user uploads the playlist under their signed-in game account.
- The normal workflow is to prepare and validate the revised local playlist, then deliver it for the user to upload/update on KovaaK's with the in-game button. Do not attempt an online edit or upload on the user's behalf unless separately requested.
- Never invent online metadata or write a guessed share code. If the user later asks for direct online publication, use only the authenticated in-game UI when available, get explicit approval for that publication, and verify the resulting online listing before claiming success.

## Pitfalls
- Playlist formats may vary between game versions. Observed templates can use different spellings (for example, `scenario_name`/`play_Count` versus `scenarioName`/`playCount`); preserve the user's chosen template literally.
- A JSON parse passing proves syntax, not that the game accepts a playlist or that every scenario is installed. Use exact scenario names and distinguish file validation from in-game verification.
- Do not assume `play_Count` means minutes; it means scenario repetitions when the supplied format documents it that way.
- Never overwrite or delete user playlists during cleanup.

## Verification
- Generated JSON parses successfully.
- Root and scenario-entry property names exactly match the selected template.
- Every `play_Count` is a positive integer and entry scenario name is preserved verbatim.
- The destination file is read back after install and its parsed contents match the generated playlist.
- Report file path, number of scenarios, total repetitions, and any unverified in-game compatibility.