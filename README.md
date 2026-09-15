## v2026.0915.1421 更新内容

- 处理中卡片新增“处理进展”，放在“工具调用”下方、“本次修改文件”上方，实时展示 Codex 对用户可见的过程说明；新发起任务和切换后跟踪的任务均支持。
- 流式文字按段落合并更新，避免重复显示；工具长时间没有新事件时仍会刷新最新说明，内容过长时保留最近进展，最终回复独立发送。
- 修复新版 Codex 桌面端因设置接口协议升级导致发送消息时报 no-client-found、任务启动失败的问题，同时兼容旧版协议并支持连接失效后的重新连接。
- /status 新增当前任务名称、ID、工作目录、模型、推理强度、权限、工作模式、目标及上下文用量，不包含对话记录，并能识别桌面端任务的执行状态。
- 未选择任务、Codex 离线或任务详情暂不可用时，/status 仍返回服务状态，并在已选择任务时保留任务 ID。
- 每次发布将本版中文更新说明置于 README.md 最上方，与 Release 保持一致，并随三个平台安装包一起提供。

---

# im2agent-release

This repository publishes the cross-platform binaries used by im2agent's `/update` command.

The `latest` GitHub Release is updated by `.github/workflows/publish-latest.yml`. Maintainers publish through SSH by force-pushing a `publish` branch containing:

- `release/manifest.json`
- `release/notes.md`
- `release/assets/im2agent-windows-amd64.zip`
- `release/assets/im2agent-macos-amd64.tar.gz`
- `release/assets/im2agent-macos-arm64.tar.gz`

The workflow validates version metadata, release notes, archive layout, sizes, SHA-256 digests, and embedded binary versions before replacing the Release assets. It uploads verified files first, then updates and verifies the public release notes. After that succeeds, it copies the Chinese changelog to the top of this repository's default-branch `README.md`, preserving previous versions and this introduction. Retrying a release updates its existing section without adding a duplicate.

Changes to the publishing workflow or its scripts on `main` run the README checks only; binary publication still requires the `publish` branch.
