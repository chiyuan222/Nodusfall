# 源神小窝 —— 《源初之结》（NODUSFALL）粉丝 Wiki

非官方粉丝站点。现阶段提供 Wiki（信息收录）与视频库（B 站 / YouTube 收录）；
架构上为未来的「个人攻略空间」与「玩家论坛」预留扩展接口。

## 技术栈

- Python 3.12 + Django 6.1
- 开发环境默认 SQLite（零配置）；生产通过 `DATABASE_URL` 切换 PostgreSQL
- 模块化结构：`accounts`（账号权限）、`wiki`（词条）、`media`（视频收录）、`core`（公共底座）

## 快速开始

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

访问 http://127.0.0.1:8000 ，管理后台在 http://127.0.0.1:8000/admin/ 。

## 目录结构

```text
config/        Django 项目配置
accounts/      用户与权限（自定义 User）
wiki/          词条、修订、分类（含命名空间，预留攻略/用户空间）
media/         视频与媒体收录
core/          公共底座（首页等）
templates/     站点模板
static/        样式与静态资源
```

## 内容规范

- 词条与视频均需注明来源，禁止直接搬运官方素材。
- 推测信息使用「待确认」标记（规范详见建站方案文档）。
