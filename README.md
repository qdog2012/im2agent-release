## v2026.0926.1018 更新内容

- macOS 后台服务新增绿色 C 菜单栏图标，悬停显示运行状态和版本；点击后可查看版本、检查更新、重启或退出服务。
- Windows 托盘菜单同样将“Codex转飞书”置于首项，点击弹出当前版本信息。
- 菜单更新继续使用下载校验、备份与失败回滚流程；重启或退出服务不会主动停止 Codex 桌面端正在执行的任务。

---

## v2026.0924.1631 更新内容

- Windows 后台服务改用无终端窗口的启动器，开机登录和服务重启时不再弹出 Windows Terminal；服务日志继续保存在配置目录。
- 新增绿色背景、白色 C 的系统托盘图标，悬停显示“飞书转codex服务：运行中，版本：xxx”；右键可检查并确认更新、重启或退出服务，Explorer 重启后图标自动恢复。
- 更新和退出只停止 im2agent 服务，不主动终止 Codex 桌面端及其正在执行的任务；更新失败时沿用备份回滚流程。

---

## v2026.0924.0943 更新内容

- 飞书 `/model` 新增 GPT-6 Sol（`gpt-6-sol`）选项；Codex 桌面端模型列表暂未提供该型号时使用兼容条目，现有新任务默认模型保持不变。
- 支持切换到 GPT-6 Sol 并选择 none、low、medium、high、xhigh、max 推理强度，兼容条目的默认强度为 medium。模型能否实际启动仍取决于本机 Codex 与账号权限。

---

## v2026.0924.0126 更新内容

- Codex 桌面端启动请求确认超时后，保留并持续跟踪原请求；中转服务重连时恢复跟踪，不会重复发送消息或误启动第二轮。
- 对启动结果尚未确认的任务，/stop 可停止等待确认；若桌面端随后出现轮次，仍由 Codex 保留其执行状态，不盲目终止正在运行的任务。
- 修复停止轮次后重新发送消息可能出现“active turn already ended”补充失败的问题：确认旧轮次结束后自动开启新轮次；若仍有活动轮次则保留任务并提示稍后重发。
- 补充并发完成事件的去重保护，避免旧轮次结果重复交付。

---

## v2026.0920.1034 更新内容

- 修复从飞书切换到正在处理的 Codex 任务时，因当前活动轮次未关联到最新用户消息而误判任务已经结束、自动发送上一轮最终回复的问题。
- 切换任务时统一检查真实活动轮次并绑定其轮次 ID；任务信息会显示“处理中”并持续跟踪当前进度，本轮完成后再发送本轮最终结果。

---

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
