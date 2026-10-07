---
name: hermes-profile-backup
description: "Use when restoring a Hermes profile from GitHub."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [windows, macos, linux]
metadata:
  hermes:
    tags: [hermes, profiles, backup, restore, github, migration, secrets]
    category: autonomous-ai-agents
---

# Hermes Profile Backup and Migration

## Procedure

1. **Inspect local prerequisites before changing anything.** Run `git --version`, `gh --version`, `hermes --version`, `hermes profile list`, and `hermes profile --help`. Git may already be installed; do not reinstall it unnecessarily.
2. **Install only the missing GitHub client.** On Windows, install GitHub CLI with `winget install --id GitHub.cli --exact --source winget --accept-source-agreements --accept-package-agreements`. Re-check `gh --version` in a shell whose PATH includes `C:/Program Files/GitHub CLI` if the current shell has not refreshed PATH.
3. **Authenticate without collecting secrets in chat.** Run `gh auth status`; if unauthenticated, use `gh auth login --hostname github.com --git-protocol https --web`, accept Git credential setup, and complete GitHub's device authorization in the browser. Never ask the user to paste a one-time code, token, password, or recovery code into chat.
4. **Verify authentication before accessing the repository.** Run `gh auth status` and stop if it is not authenticated. Use the repository's exact `OWNER/REPO` identifier; do not guess a repository from a vague description.
5. **Clone the private repository into a separate staging directory.** Prefer `gh repo clone OWNER/REPO C:/Users/<user>/hermes-backup` (or an equivalent platform path). Do not overwrite the active Hermes home during download.
6. **Inventory and classify the backup before restoration.** Locate archives and manifests, then determine whether the artifact is a Hermes profile export (`.tar.gz`) or a full Hermes backup (`.zip`). A profile export is imported with `hermes profile import ARCHIVE --name NAME`; a full backup requires inspecting Hermes's current backup/import help and its archive layout before copying files.
7. **Restore profile exports through Hermes.** Use `hermes profile import C:/path/profile.tar.gz --name PROFILE_NAME`, then verify with `hermes profile list`, `hermes profile show PROFILE_NAME`, and, if requested, `hermes profile use PROFILE_NAME`.
8. **Treat full backups as sensitive migrations.** Review the archive contents and identify `.env`, `auth.json`, session databases, and other credentials before restoring. Never publish or echo their contents. If credentials were committed to a public repository, revoke and regenerate them before use; private visibility reduces exposure but does not make secrets safe to redistribute.
9. **Verify the restored state, not just the command exit code.** Confirm the profile appears, its expected files exist, and Hermes can start or run a harmless status/doctor check under the restored profile. Keep the original active profile untouched until verification succeeds.

## Decision rules and pitfalls

- **Use the archive type to choose the restore path:** `profile import` accepts a local `.tar.gz`; do not pass a GitHub URL or a full `.zip` to it because the CLI contract is archive-specific.
- **Keep GitHub authentication separate from Hermes credentials:** `gh auth` authenticates repository access, while Hermes `.env`/`auth.json` contain provider credentials; mixing the two can overwrite or leak unrelated secrets.
- **Stage before restoring:** clone and inspect outside `$HERMES_HOME`, because directly replacing the active home can destroy the currently working profile before the backup is validated.
- **Verify private-repository access with `gh auth status` before cloning:** a clone failure can otherwise be mistaken for a bad repository name or corrupt backup.
- **Use a PTY and submit a real Enter for interactive `gh auth login` on Windows:** ConPTY/prompt-style prompts can ignore a bare newline sent as raw input; `process(submit)` delivers the carriage-return line ending the prompt expects.
- **Do not report restoration success from a successful clone or import alone:** read back the profile list and run a harmless Hermes check, because archive acceptance does not prove the profile is usable.

## References

See `references/private-github-restore.md` for the compact private-repository command recipe and archive decision table.
