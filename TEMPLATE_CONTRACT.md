# 模板契约（TEMPLATE_CONTRACT）

本文件是「后端（Codex）」与「前端（Kimi）」之间的接口约定。
后端承诺：凡是本文件列出的变量与 URL，前端都可以直接使用，不会随意改名。
前端承诺：只使用本文件列出的变量，不自行发明上下文变量。

## 1. 文件所有权

| 归属 | 文件 |
| --- | --- |
| 后端（Codex） | `*.py`、`config/`、各 app 的 `models/views/urls/forms/admin`、`requirements.txt`、`migrations/` |
| 前端（Kimi） | `templates/**`、`static/css/**`、`static/js/**`、`static/img/**` |
| 双方 | 本契约文档改动需双方知晓 |

> 前端需要新的数据/URL 时，不要自己改后端代码，写进交接记录，由后端实现后再更新本契约。

## 2. 全局可用（所有页面，来自 context processor）

| 变量 | 说明 |
| --- | --- |
| `site_appearance` | 站点外观对象，常用字段见下 |
| `theme_presets` | 访客主题预设字典（key → {label, colors}） |
| `theme_presets_json` | 同上的 JSON 字符串（已内嵌到 base.html 的脚本） |
| `user` | Django 默认，未登录时是 AnonymousUser |
| `request` | Django 默认，可读 `request.GET.q` 等 |

`site_appearance` 常用字段：
`site_name`、`site_slogan`、`logo_image`、`logo_height`、
`colors.accent_color` / `colors.panel_color` / `colors.text_color` / `colors.muted_color` / `colors.border_color`、
`background_url`、`background_size`、`background_position`、`overlay_opacity`。

## 3. URL 名称（用 `{% url '...' %}`，禁止硬编码路径）

| 名称 | 路径 |
| --- | --- |
| `core:home` | `/` |
| `core:search` | `/search/` |
| `core:login` / `core:logout` | `/accounts/login/` / `/accounts/logout/` |
| `accounts:register` | `/accounts/register/` |
| `wiki:worldview` | `/wiki/worldview/` |
| `wiki:page_list` | `/wiki/` |
| `wiki:page_create` | `/wiki/new/` |
| `wiki:page_detail` | `/wiki/<namespace>/<slug>/` |
| `wiki:page_edit` | `/wiki/<namespace>/<slug>/edit/` |
| `wiki:page_history` | `/wiki/<namespace>/<slug>/history/` |
| `media:media_list` | `/media/` |
| `media:media_add` | `/media/add/` |
| `media:media_detail` | `/media/<id>/` |
| `forum:forum_home` | `/forum/` |
| `forum:board_detail` | `/forum/<slug>/` |

## 4. 各页面上下文变量

| 页面 | 变量 |
| --- | --- |
| 首页 `core:home` | `slides`、`featured`、`official_links`、`latest_pages`、`latest_videos` |
| 搜索 `core:search` | `q`、`pages`、`videos` |
| 词条列表 `wiki:page_list` | `pages` |
| 世界观 `wiki:worldview` | `pages` |
| 词条详情 `wiki:page_detail` | `page` |
| 编辑页 `wiki:page_edit` / `page_create` | `form`、`page`（新建时为 None）、`preview_source` |
| 历史 `wiki:page_history` | `page`、`revisions` |
| 视频列表 `media:media_list` | `items` |
| 视频详情 `media:media_detail` | `item` |
| 收录视频 `media:media_add` | `form` |
| 论坛首页 `forum:forum_home` | `boards` |
| 版块页 `forum:board_detail` | `board` |

## 5. 样式约定

- 颜色一律使用 CSS 变量：`--bg` `--panel` `--border` `--text` `--muted` `--accent`，禁止硬编码色值。
- 字体用系统栈，不引入外部字体。
- 响应式断点：900px（网格转单列）、720px（头部换行）。
- 新图片放 `static/img/`，用 `{% load static %}` + `{% static '...' %}` 引用。
