import re

from django import template
from django.utils.safestring import mark_safe
from markdown_it import MarkdownIt

register = template.Library()

_md = MarkdownIt("js-default", {"html": False, "linkify": True})

# [[词条slug|显示文字]] 或 [[命名空间:slug]] 形式的词条内链
WIKILINK_RE = re.compile(r"\[\[([^\[\]|]+)(?:\|([^\[\]]+))?\]\]")


def _replace_wikilink(match):
    target = match.group(1).strip()
    label = (match.group(2) or target).strip()
    if ":" in target:
        namespace, slug = target.split(":", 1)
    else:
        namespace, slug = "main", target
    return f"[{label}](/wiki/{namespace}/{slug}/)"


@register.filter(name="markdown")
def render_markdown(text):
    """渲染 Markdown；禁用原始 HTML 防 XSS，支持 [[内链]] 语法。"""
    if not text:
        return ""
    text = WIKILINK_RE.sub(_replace_wikilink, text)
    return mark_safe(_md.render(text))
