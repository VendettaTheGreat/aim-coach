# Repository Layouts and Safe Copy Recipes

## Decision table

| Source tree | Restore method | Do not do |
|---|---|---|
| `profile-export.tar.gz` | `hermes profile import profile-export.tar.gz --name NAME` | Do not unpack it into the live home first |
| `config.yaml`, `SOUL.md`, `profiles/NAME/` | Create an isolated profile, then copy `profile.yaml`, `SOUL.md`, and `skills/` | Do not pass the repository directory to `hermes profile import` |
| `hermes-backup-*.zip` | Follow the full-backup restore workflow after making a rollback copy | Do not merge blindly over a running Hermes home |

## Directory-style profile recipe

```bash
# Source and destination are examples; inspect them first.
hermes profile create NAME --no-skills --description "..."
cp SOURCE/profiles/NAME/SOUL.md DESTINATION/profiles/NAME/SOUL.md
cp SOURCE/profiles/NAME/profile.yaml DESTINATION/profiles/NAME/profile.yaml
rm -rf DESTINATION/profiles/NAME/skills
mkdir -p DESTINATION/profiles/NAME/skills
cp -a SOURCE/profiles/NAME/skills/. DESTINATION/profiles/NAME/skills/
```

On Windows, use equivalent PowerShell or Git Bash paths, and verify the actual destination with `hermes profile show NAME` rather than assuming `~/.hermes`.

## Safe verification

```bash
find SOURCE/profiles/NAME/skills -type f | wc -l
find DESTINATION/profiles/NAME/skills -type f | wc -l
hermes profile show NAME
hermes config check
```

Keep `.env`, `auth.json`, sessions, databases, gateway state, logs, and caches out of the copy. Restore credentials through Hermes setup/auth commands after the profile structure is verified.
