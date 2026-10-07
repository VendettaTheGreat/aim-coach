# Private GitHub Restore Recipe

## Access

```bash
git --version
gh --version
hermes --version
gh auth status
```

If `gh` is missing on Windows:

```bash
winget install --id GitHub.cli --exact --source winget \
  --accept-source-agreements --accept-package-agreements
```

Authenticate interactively:

```bash
gh auth login --hostname github.com --git-protocol https --web
gh auth status
gh repo clone OWNER/REPO C:/Users/<user>/hermes-backup
```

Complete device authorization in the browser; never transfer its code or any token through chat.

## Archive decision table

| Artifact | Action |
|---|---|
| `*.tar.gz` produced by `hermes profile export` | `hermes profile import PATH --name NAME` |
| `*.zip` produced by `hermes backup` | Inspect archive and current Hermes backup/import help before restoring files; do not pass it to `profile import` |
| Raw config/session files | Stop and inventory them; do not overwrite the active Hermes home blindly |

## Verification

```bash
hermes profile list
hermes profile show NAME
hermes doctor
```

Run verification while the original profile remains available. Do not expose `.env`, `auth.json`, API keys, OAuth tokens, or session contents when listing or reporting files.
