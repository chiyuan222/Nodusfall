from django import forms

from .models import WikiPage


class PageForm(forms.ModelForm):
    summary = forms.CharField(
        label="编辑摘要",
        max_length=200,
        required=False,
        help_text="简短说明本次修改内容（可选）",
    )

    class Meta:
        model = WikiPage
        fields = ["namespace", "slug", "title", "content_md"]
        widgets = {
            "content_md": forms.Textarea(attrs={"rows": 20, "class": "editor"}),
        }
        help_texts = {
            "content_md": "支持 Markdown 语法；用 [[词条slug|显示文字]] 创建词条内链。",
        }
