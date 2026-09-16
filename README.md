## v2026.0916.1035 更新内容

- 修复 /compact 因 Codex 桌面端内部 5 秒确认超时而误报压缩失败的问题；请求已提交时继续等待真实完成或失败结果，不重复发起压缩。
- 上下文压缩最多等待 15 分钟；等待结束、取消等待或连接中断后仍未获得明确结果时，卡片显示“结果待确认”，提示先检查桌面端状态，避免重复操作。
- 按压缩轮次匹配执行结果，避免其他轮次的错误干扰；压缩项尚未生成时也能返回该轮次的真实失败原因，包括模型网关错误。

---

## v2026.0915.2038 更新内容

- 修复飞书预览因首选浏览器启动失败而直接报错的问题：自动尝试本机其他 Chrome、Edge 或 Chromium，兼容浏览器策略指定的数据目录被占用等情况。
- 预览启动失败时显示实际浏览器路径和启动诊断，补充空白错误与连接超时提示；IM2AGENT_BROWSER 可指定优先使用的浏览器。
- 优化 Windows 截图浏览器启动方式，使用隐藏窗口、新版无头模式和禁用 GPU 的配置，并补充新电脑缺少可用浏览器时的处理说明。

---

## v2026.0915.1808 更新内容

- 切换到正在处理的任务后，完成时按飞书发起任务的方式自动发送最终回复、链接预览和生成图片；没有最终正文时发送完成通知，无需再手动执行 /last。
- 原飞书发起消息与切换后的跟踪共用去重记录，同一用户在同一聊天中只接收一次同一轮结果，避免重复切换或卡片刷新造成重复回复。
- 最终回复发送失败时自动重试，卡片更新失败不会重复发送已成功的结果；跟踪期间保留已完成轮次的快照，后续读取暂时失败仍可继续发送。
- 发布成功后自动将中文更新说明置于 im2agent-release 仓库 README 顶部；源码仓库只保留最近 10 个版本，发布仓库永久保留全部历史，同版本重试不重复插入。

---

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
