# im2agent v2026.1009.1231

源代码提交：418f8dfb9bbda2f056c2fb903ad73e5d29cb8ba3

## 更新内容

- 修复 PDF 预览只显示第一页的问题：Windows 和 macOS 通过系统 PDF 渲染器读取并渲染全部页面，支持本机 PDF 和以 `.pdf` 结尾的 HTTP/HTTPS 链接（可带查询参数），无需另装 PDF 工具。
- 多页 PDF 默认按页码从上到下无损合并为一张完整长图，保留每页原始比例和清晰度，加入浅灰页间分隔，不裁切后续页面。
- 合并图片超过飞书单张图片限制（12000 × 12000、10 MB）或内存安全限额时，明确提示并自动回退为按页发送全部内容；文件过大、加密不可读、渲染失败或超时会明确报错，分页上传失败时提示失败页码和已发送页数。

## 下载

- Windows amd64：im2agent-windows-amd64.zip
- macOS Intel：im2agent-macos-amd64.tar.gz
- macOS Apple Silicon：im2agent-macos-arm64.tar.gz

每个压缩包包含根目录程序、README.md、LICENSE 和 config.example.yaml。

