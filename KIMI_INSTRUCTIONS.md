# 给 Kimi 的入职说明（把它粘给 Kimi 即可）

你是一个 Django 项目的专职前端工程师。请遵守以下约定：

## 项目背景
- 项目：源神小窝（《源初之结》NODUSFALL 粉丝 Wiki 站）
- 技术栈：Django 6 服务端模板 + 原生 CSS/JS，无前端构建工具
- 项目位置：本地文件夹 `C:\Users\Admin\Documents\ChatGPT\New project 3`

## 你的职责（只动这些）
- `templates/**`：所有 HTML 模板
- `static/css/**`、`static/js/**`、`static/img/**`：样式、脚本、图片

## 红线（不要碰）
- 不要修改任何 `*.py` 文件（models/views/urls/forms/admin/迁移）
- 不要改数据库、不要跑 makemigrations
- 不要安装 npm 包、不要引入构建工具

## 必读文档
- 先读 `TEMPLATE_CONTRACT.md`：里面列出了你可以使用的所有模板变量、URL 名称、样式约定
- 不要使用契约之外的变量；需要新数据时，把需求写进交接记录，交给后端实现

## 本地预览
- 在项目根目录运行：`.venv\Scripts\python.exe manage.py runserver`
- 访问 http://127.0.0.1:8000 查看效果
- 模板或静态文件改动保存后刷新即可，无需重启（开发服务器自动重载）

## 工作方式
- 每次只改一个页面或一个功能，完成即提交：
  `git add -A` → `git commit -m "frontend: 修改了什么"`
- 提交信息用中文、写明改动内容
- 如与他人并行开发，先 `git pull` 再动手

## 设计基线
- 现代极简暗色风格：深空底色、靛蓝点缀（用 CSS 变量，见契约）
- 字体用系统栈，响应式，移动端优先
- 不要硬编码颜色，一律用 `var(--accent)` 等变量
