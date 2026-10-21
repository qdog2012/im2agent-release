# im2agent v2026.1021.2311

源代码提交：`6df317d09bf5861f9e6d41ee90b5353a9aee80cd`

## 更新内容

- 修复本机及 SSH 远程任务列表因默认模型供应商过滤而漏项的问题，显式查询全部供应商的任务并统一排序、分页，不再遗漏 Server-25 等主机上使用不同供应商的任务。
- 简化远程任务名称前缀，统一显示为 `[主机名称]任务名称`，例如 `[Server-25]远程Jev`，移除协议类型和多余空格；本机任务名称保持不变。

## 下载

- Windows amd64：`im2agent-windows-amd64.zip`
- macOS Intel：`im2agent-macos-amd64.tar.gz`
- macOS Apple Silicon：`im2agent-macos-arm64.tar.gz`
