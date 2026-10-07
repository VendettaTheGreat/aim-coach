---
name: hermes-profile-backup-restore
description: "Use when restoring Hermes profiles from GitHub."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [windows, macos, linux]
metadata:
  hermes:
    tags: [hermes, profiles, backup, restore, github, migration]
    category: software-development
---

# Hermes Profile Backup and Restore

Restore Hermes backups from GitHub without destroying the current installation or importing credentials accidentally.

## Procedure

1. **Authenticate and identify the source.**
   - Run `gh auth status` before accessing a private repository.
   - Identify the repository and default branch with `gh repo view OWNER/REPO`.
   - Use `git clone --depth 1 https://github.com/OWNER/REPO.git DESTINATION` for a local working copy.
   - Inspect `README.md`, `RESTORE.md`, `.gitignore`, and the top-level tree before copying anything.

2. **Classify the backup format.**
   - A Hermes profile export is a local `.tar.gz` and can be restored with `hermes profile import ARCHIVE --name NAME`.
   - A repository containing `config.yaml`, `SOUL.md`, and `profiles/<name>/` is a directory-style setup backup, not a profile archive. Recreate it by copying the profile components; do not pass the repository or directory to `hermes profile import`.
   - A full `hermes backup` is a `.zip`; treat it separately from a profile export and inspect its restore instructions before replacing the Hermes home.

3. **Protect the current installation.**
   - Create a local rollback archive before state-changing work: `hermes backup -o PATH/pre-restore.zip -k 0`.
   - Keep the existing `default` profile intact unless the user explicitly requests full replacement.
   - Never copy `.env`, `auth.json`, session databases, gateway state, logs, or other credential/runtime files from a repository into the active installation without explicit, verified intent.

4. **Create an isolated target profile.**
   - Use `hermes profile create NAME --no-skills --description DESCRIPTION` so the current profile is not overwritten and bundled skills are not silently mixed with the backup.
   - Copy only the backup profile metadata, prompt, and skills into the target profile: `profile.yaml`, `SOUL.md`, and `skills/` (including hidden manifests when present).
   - Preserve the target profile's local `.env`; credentials are configured separately.
   - If the backup provides a model/provider in root `config.yaml`, apply the needed values through `hermes config set KEY VALUE` while the target profile is active instead of hand-editing YAML.

5. **Verify before activation.**
   - Run `hermes profile show NAME` and confirm the path, model, provider, prompt, and skill count.
   - Compare source and destination skill-file counts.
   - Run `hermes config check`.
   - Keep the gateway stopped until credentials and channel configuration are deliberately restored.
   - Only after verification, use `hermes profile use NAME` if the user wants the restored profile to become the active profile.

6. **Finish credentials and runtime setup.**
   - Run the profile's setup command, for example `NAME setup`, to configure model credentials without placing secrets in Git.
   - If the user explicitly requests reusing the currently working Hermes credentials, copy the current profile's `.env` and `auth.json` into the target profile without printing them, then verify the files are identical and run `hermes auth status PROVIDER`; do not assume GitHub authentication is the same as Hermes provider authentication.
   - Configure messaging channels separately; a backup that excludes tokens cannot recreate a working gateway by itself.
   - Test the profile with a harmless query before starting a gateway.
   - Refresh and validate the live model catalog after migration; backup model IDs can expire or lose free access even when credentials are valid. Use `hermes model --refresh`, choose a currently available model, and run a harmless query to verify it.

## Rules and pitfalls

- **Distinguish archive restoration from directory restoration**, because `hermes profile import` accepts a `.tar.gz`, not a GitHub repository tree.
- **Prefer an isolated profile over replacing `default`**, because a setup repository may contain behavior or model settings that change the user's current assistant.
- **Use Hermes configuration commands rather than hand-editing `config.yaml`**, because YAML edits can corrupt the live configuration and bypass profile-aware handling.
- **Treat a private repository as sensitive even when it excludes credentials**, because prompts, memories, contact workflows, and configuration can contain personal or operational data.
- **Do not claim the bot is ready after copying files**, because credentials and gateway/channel configuration are intentionally absent from secure backups.
- **Verify the repository tree before following its restore document**, because documentation can list optional directories that are absent from the actual backup.

## References

- `references/repository-layouts.md` — format decision table and safe copy recipes for GitHub-backed Hermes setups.
