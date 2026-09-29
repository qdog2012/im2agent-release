# im2agent v2026.0929.1223

源代码提交：ff65b8f19f3e49fffc4a60af64bb5d6f59b5f278

## 更新内容

- 修复 macOS 更新 Codex 桌面应用后，因内置 CLI 移至 `codex-cli/CodexCLI.app` 而反复提示“Codex 未连接”的问题；服务现在自动识别新旧应用目录，无需手工配置 CLI 路径。
- 保持对 `ChatGPT.app`、`Codex.app` 及用户目录安装的兼容；恢复连接时不主动终止正在运行的 Codex 桌面任务。

## 下载

- Windows amd64：im2agent-windows-amd64.zip
- macOS Intel：im2agent-macos-amd64.tar.gz
- macOS Apple Silicon：im2agent-macos-arm64.tar.gz

每个压缩包包含根目录程序、README.md、LICENSE 和 config.example.yaml。
