# im2agent-release

This repository publishes the cross-platform binaries used by im2agent's `/update` command.

The `latest` GitHub Release is updated by `.github/workflows/publish-latest.yml`. Maintainers publish through SSH by force-pushing a `publish` branch containing:

- `release/manifest.json`
- `release/notes.md`
- `release/assets/im2agent-windows-amd64.zip`
- `release/assets/im2agent-macos-amd64.tar.gz`
- `release/assets/im2agent-macos-arm64.tar.gz`

The workflow validates version metadata, release notes, archive layout, sizes, SHA-256 digests, and embedded binary versions before replacing the Release assets. It uploads verified files first and updates the public release notes last.
