# im2agent v2026.0916.1035

源代码提交：0367d4bfee15516d2c0b6b8261c07e396cd78596

## 更新内容

- 修复 /compact 因 Codex 桌面端内部 5 秒确认超时而误报压缩失败的问题；请求已提交时继续等待真实完成或失败结果，不重复发起压缩。
- 上下文压缩最多等待 15 分钟；等待结束、取消等待或连接中断后仍未获得明确结果时，卡片显示“结果待确认”，提示先检查桌面端状态，避免重复操作。
- 按压缩轮次匹配执行结果，避免其他轮次的错误干扰；压缩项尚未生成时也能返回该轮次的真实失败原因，包括模型网关错误。

## 下载

- Windows amd64：im2agent-windows-amd64.zip
- macOS Intel：im2agent-macos-amd64.tar.gz
- macOS Apple Silicon：im2agent-macos-arm64.tar.gz

每个压缩包包含根目录程序、README.md、LICENSE 和 config.example.yaml。
