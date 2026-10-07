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
2. **Select and scale scenarios.** For coaching-derived playlists, load `aim-coaching` and consult the user's current difficulty-scaled `Recommended KovaaKs Scenarios` sheet (`https://docs.google.com/spreadsheets/d/1AKdZJrjfpfsoFBdN71dS2vCSKS1NKNFFbiQ3_XJnHko/edit?usp=sharing`) for archetype-specific difficulty; do not use the previously supplied Voltaic scenario sheet. Select the archetype's scenario difficulty tier from the observed issue/coaching notes and whether the easier variation still challenges the intended skill; no user Voltaic rank is required. Progress within that archetype when the easier option stops being challenging or has served its purpose, keeping control stable and changing one demand at a time. Then verify every exact title through KovaaK's general scenario interface (`https://kovaaks.com/kovaaks/scenarios`) or a current official cache entry. Keep ordinary Tracking distinct from Movement/Keyboard Strafes (WASD/dodge); moving targets do not prove player movement. Parse target geometry, player locomotion, aim mechanic, precision/size and difficulty independently. Check `aim-coaching/references/scenario-cache.md` before searching; after an official search, cache exact title, URL, verified details, and inference labels. Use compact scenario-family keywords, not the full issue description; a query returning fewer than 10 results is unoptimal and must be broadened or changed. No user rank is required; document the selected difficulty band and the observed issue it addresses. Prefer verified Invincible variants for continuous tracking when they match the mechanic; for VAI, interpret the number as the target angle in degrees and choose angles deliberately rather than repeating one blindly. Preserve exact scenario spelling; do not invent aliases or difficulty labels.
3. **Build minimal playlist entries.** Use one scenario object per entry, with the template's exact scenario-name property and play-count property. `play_Count` is the number of repetitions for that scenario entry. Set metadata explicitly using values consistent with the sample; avoid duplicate names unless intentional.
4. **Validate before writing.** Parse with Python's `json` module. Check required root keys against the supplied template, required entry keys, correct types (`scenarioList` list, scenario name string, play count positive integer), non-empty playlist name, unique scenario entries unless intentional, and no comments/trailing commas. Compare generated schema keys to the template. Report the scenario count and total repetitions.
5. **Write safely.** Never overwrite an existing playlist without explicit approval. Write to a new filename in the nominated Playlists directory, or create a draft elsewhere if the format is uncertain. Keep file encoding UTF-8.
6. **Verify the install.** After copying/writing into the game directory, read the exact target file back and parse it again. Confirm path, playlist name, scenario names, repetitions, and parse success before claiming it is installed. Do not claim the game itself imported it unless verified in-game.

## Benchmark playlists and review
- Keep a benchmark short and diagnostic: usually 3–5 scenarios, one run each, spanning only the skills the user wants to monitor. Avoid turning it into another high-volume training routine.
- Freeze scenario variants, ordering, sensitivity/FOV, and repetitions across checks. Run after a training phase or about every two weeks, preferably rested and not immediately after a long FFA/QP session.
- Select benchmark items from separate dimensions when relevant (smooth tracking, ground/air reactive tracking, player-dodge movement, precision). Don't mistake a scenario's easy/hard or rank for its task category.
- Pair the playlist with a short VOD note sheet: scenario start/end times, score/accuracy if visible, first clear overshoot/undercorrection, first sustained crosshair loss, and when the player notices tension rising. Ask for hand-cam only if direct grip observation is needed; gameplay-only video cannot prove grip mechanics.
- After writing, validate the file as usual and tell the user the benchmark's in-game acceptance has not been tested unless it was actually opened in KovaaK's.

## Online publication and account metadata
- A locally written JSON does not create a valid online `playlistId`, `authorSteamId`/author name, or `shareCode`. Those are assigned by KovaaK's when the playlist is uploaded under the signed-in game account.
- The official FAQ does not document a public upload API. Publish only through the authenticated in-game UI when available; never invent metadata or write a guessed share code.
- Get explicit approval for each online publication because it creates account-linked external content. After upload, read back the generated IDs/share code from the local playlist and verify the online listing before claiming success. If the game UI/account is unavailable, provide the local file and leave the upload click to the user.

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