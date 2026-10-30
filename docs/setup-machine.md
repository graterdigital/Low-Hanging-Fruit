# Setting up a machine to run fixes

One-time per machine. After this, every skill that writes to a site works through `ssh <slug>`.

**Status on Greg's PC (2026-10-30):** sections 1-4 (SSH key, Kinsta API, SSH config, test) and the Ahrefs key are DONE; if `ssh hsfamilylaw "wp --info"`
works, skip to whichever section is new. The Google service account section (bottom) is the only one still to do.

## 1. SSH key (once, ever)

You probably already have one at `~/.ssh/id_ed25519`. If `ssh-keygen` says it exists, keep it. Otherwise:

    ssh-keygen -t ed25519 -C "grater-toolkit"

Add the **public** key (`~/.ssh/id_ed25519.pub`) to each host, once per host account:

- Kinsta: MyKinsta → your name → User Settings → SSH Keys → Add
- WP Engine: my.wpengine.com → profile → SSH Keys (my.wpengine.com/ssh_keys) → New SSH Key

Windows: `Get-Content ~\.ssh\id_ed25519.pub | Set-Clipboard` copies it. macOS: `pbcopy < ~/.ssh/id_ed25519.pub`.

## 2. API credentials (once per machine)

- Kinsta: MyKinsta → Company settings → API Keys → create one. The company ID is on Company settings → Billing details.
- WP Engine: my.wpengine.com/api_access → generate an API user and password.

Set them as environment variables. Windows PowerShell (persists for your user):

    [Environment]::SetEnvironmentVariable("KINSTA_API_KEY", "paste", "User")
    [Environment]::SetEnvironmentVariable("KINSTA_COMPANY_ID", "paste", "User")
    [Environment]::SetEnvironmentVariable("WPENGINE_API_USER", "paste", "User")
    [Environment]::SetEnvironmentVariable("WPENGINE_API_PASSWORD", "paste", "User")

Then open a new PowerShell window. macOS/Linux: add `export NAME=value` lines to `~/.zshrc` or `~/.bashrc`.

## 3. Generate the SSH config

    pip install requests pyyaml
    python scripts/ssh_config_sync.py            # preview
    python scripts/ssh_config_sync.py --apply    # write

It writes `~/.ssh/grater_hosts` (one entry per environment, aliased by client slug) and fills in the hosting block of each matching client file. Re-run it when a site is added or moved.

## 4. Test

    ssh hsfamilylaw "wp --info"

A WP-CLI version means the chain works. "Permission denied (publickey)" means the key hasn't propagated at the host yet, or the key file name differs from `~/.ssh/id_ed25519` (edit `KEY_FILE` at the top of the script if so).

Sites on other hosts: fill `hosting:` in their client file by hand and add a `Host <slug>` block to `~/.ssh/config` yourself.

## Ahrefs API key

`scripts/build_redirect_map.py` and the batch runner read `AHREFS_API_KEY` from the environment or from a `.env` file at the repo root (git-ignored). Create it once:

```powershell
Set-Content -Path .env -Value "AHREFS_API_KEY=paste-the-key-here"
```

The key comes from Ahrefs → Account settings → API keys. Never put it in a client file or commit it.

## Google service account (review sheets)

`scripts/review_sheets.py` keeps one Google Sheet per client for APPROVE-tier review and reads decisions back without a human
exporting anything. It authenticates as a service account. One-time setup, ~10 minutes:

1. Google Cloud Console (console.cloud.google.com), signed in as the Google account you normally work in (overwatch@graterdigital.com) → create a project (e.g. `grater-lhf`) or pick one. Which account owns the project does not matter; what matters is who the sheets get shared with (step 5).
2. APIs & Services → Enable APIs → enable **Google Sheets API** and **Google Drive API**.
3. IAM & Admin → Service Accounts → Create: name `lhf-review-sheets`. No roles needed. Open it → Keys → Add key → JSON. Save the file as
   `C:\Users\greg\Documents\Low-Hanging-Fruit\secrets\google-service-account.json` (the folder is git-ignored).
4. `pip install gspread google-auth`
5. Service accounts cannot own files, so make a folder in your own Drive (e.g. **LHF Review Sheets**), share it with the service
   account's email (`client_email` in the JSON) as Editor, and put its id (the part of the folder URL after `/folders/`) in `.env`:
   `Add-Content .env "GOOGLE_SHEETS_FOLDER=<folder id>"`. Service accounts cannot create files either, so for each client make a blank
   Google Sheet in that folder named exactly `<slug> review` (e.g. `fenceworksofga review`), then run
   `python scripts/review_sheets.py setup <slug>`: it finds the sheet by name, records its id in the client file, and adds the `alt text` tab.
   `push <slug>` then fills it.
   For a sheet that already exists in a human's Drive, share it with the service account's email (`client_email` in the JSON) as Editor
   and put its id in `clients/<slug>.yaml` under `review.alt_sheet_id`.
6. `python scripts/review_sheets.py status` lists every client's sheet and its pending / merged / applied counts.
