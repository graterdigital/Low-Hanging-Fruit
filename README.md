# Low-Hanging-Fruit

Grater Digital's toolkit of Claude Code skills and agents for the repetitive parts of technical SEO, analytics, and PPC work across client sites.

The plan, decisions, and standards live in [`docs/plan.md`](docs/plan.md). Read that first.

## The one rule

**Skills hold the how. Client files hold the what.** A skill never contains anything specific to one site; a client file never contains a procedure. Running a skill against a new site means adding one file to `clients/`, nothing else.

## Layout

```
.claude-plugin/   plugin and marketplace manifests (what makes this installable)
skills/           one folder per skill, each with a SKILL.md
agents/           subagents for noisy jobs (crawling, network capture)
clients/          one YAML per site; _template.yaml shows every field; never credentials
reports/          what skills found, per site, per crawl date
changes/          what fix skills changed, grouped by host then site, per run, with rollback detail
docs/             plan, standards, decisions
```

## Install on a machine

```
claude plugin marketplace add graterdigital/Low-Hanging-Fruit
claude plugin install low-hanging-fruit@graterdigital
```

Update later with `claude plugin update low-hanging-fruit`. The same skills also run in the Claude app when added to the account's skills.

## Credentials

Never in this repo. SSH hosts, ports, and usernames live in `~/.ssh/config` on the machine that runs fixes; client files record only the alias name. API keys live in environment variables.

## Skills

| Skill | Tier | Status |
|---|---|---|
| `site-triage` | read-only | v1, tested on two sites |
| `fix-redirect-links` | AUTO | next |
| `fix-meta` | APPROVE | planned |
| `fix-images` | APPROVE | planned |
| `indexation-review` | APPROVE | planned |
| `schema-check` | FLAG | planned |
| `verify` | read-only | planned |
