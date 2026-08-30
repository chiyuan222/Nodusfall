from django import forms

from .models import MEDIA_CATEGORY_CHOICES


class MediaItemForm(forms.Form):
    url = forms.URLField(
        label="视频链接",
        help_text="支持 B 站视频链接（含 BV 号）与 YouTube 链接",
    )
    title = forms.CharField(
        label="标题", max_length=200, required=False, help_text="留空则先用视频 ID 作为临时标题"
    )
    category = forms.ChoiceField(label="分类", choices=MEDIA_CATEGORY_CHOICES)
    author_name = forms.CharField(label="UP 主/频道", max_length=100, required=False)
    language = forms.CharField(label="语言", max_length=20, initial="zh")
    license_note = forms.CharField(label="授权备注", max_length=200, required=False)
