# Setting up a machine to run fixes

One-time per machine. After this, every skill that writes to a site works through `ssh <slug>`.

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
