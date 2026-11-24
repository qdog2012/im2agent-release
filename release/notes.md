# im2agent v2026.1124.1243

源代码提交：`9d4070732f1e5329ff7ec5d8c95bd522865f588a`

## 更新内容

- 飞书机器人输入 `/` 即可查看并补全全部 25 个指令入口。子指令支持下划线写法，例如 `/task_search`，也可继续用空格输入。
- 飞书只提供一个 `/restart` 入口。在 Windows 和 macOS 上，立即启动或重启本机共享 App Server，再以共享连接模式重启 Codex 桌面。确认桌面接入同一后台后，中转服务重新连接，`/help` 卡片也提供同一个重启按钮。正在运行的本机任务可能中断。
- 服务启动时自动同步飞书指令，扫码创建和补齐权限时会申请指令读取与写入权限。

## 下载

- Windows amd64：`im2agent-windows-amd64.zip`
- macOS Intel：`im2agent-macos-amd64.tar.gz`
- macOS Apple Silicon：`im2agent-macos-arm64.tar.gz`
