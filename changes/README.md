# Change logs

Every fix skill that writes to a site records what it did here, one file per run, grouped by host and then by site:

```
changes/<provider>/<slug>/<stamp>-<skill>-<target>-<mode>.md     # the change log (committed)
changes/<provider>/<slug>/<stamp>-<skill>-<target>-options.md  # companion report, where a skill produces one (committed)
changes/<provider>/<slug>/backup/<stamp>-<skill>-<target>.json  # full before/after content (git-ignored: client content)
```

`<provider>` is `hosting.provider` from the client file (`kinsta`, `wpengine`; `other` when unknown). `<target>` is `staging` or `live`; `<mode>` is `dry` or `apply`.

Nothing is written to a site without a change log, and every log carries enough before/after detail to reverse the run. Commit the `.md` files after each run; the `backup/` folders stay local.
