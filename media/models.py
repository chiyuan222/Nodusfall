from django.conf import settings
from django.db import models

PROVIDER_BILIBILI = "bilibili"
PROVIDER_YOUTUBE = "youtube"
PROVIDER_CHOICES = [
    (PROVIDER_BILIBILI, "哔哩哔哩"),
    (PROVIDER_YOUTUBE, "YouTube"),
]

MEDIA_CATEGORY_OFFICIAL = "official_pv"
MEDIA_CATEGORY_GAMEPLAY = "gameplay"
MEDIA_CATEGORY_PREVIEW = "preview"
MEDIA_CATEGORY_INTERVIEW = "interview"
MEDIA_CATEGORY_FANWORK = "fanwork"
MEDIA_CATEGORY_CHOICES = [
    (MEDIA_CATEGORY_OFFICIAL, "官方 PV / 预告"),
    (MEDIA_CATEGORY_GAMEPLAY, "实机演示"),
    (MEDIA_CATEGORY_PREVIEW, "试玩评测"),
    (MEDIA_CATEGORY_INTERVIEW, "开发组采访"),
    (MEDIA_CATEGORY_FANWORK, "二创作品"),
]


class MediaItem(models.Model):
    """视频/媒体条目：B 站、YouTube 等平台的收录与索引。"""

    provider = models.CharField("平台", max_length=20, choices=PROVIDER_CHOICES)
    video_id = models.CharField("视频 ID", max_length=80)
    title = models.CharField("标题", max_length=200)
    cover_url = models.URLField("封面链接", blank=True)
    source_url = models.URLField("来源链接")
    category = models.CharField(
        "分类", max_length=20, choices=MEDIA_CATEGORY_CHOICES, default=MEDIA_CATEGORY_OFFICIAL
    )
    author_name = models.CharField("UP 主/频道", max_length=100, blank=True)
    language = models.CharField("语言", max_length=20, default="zh")
    published_at = models.DateField("发布时间", null=True, blank=True)
    license_note = models.CharField("授权备注", max_length=200, blank=True)
    pages = models.ManyToManyField(
        "wiki.WikiPage", related_name="videos", blank=True, verbose_name="关联词条"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="收录人",
    )
    created_at = models.DateTimeField("收录时间", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "视频条目"
        verbose_name_plural = "视频条目"

    def __str__(self):
        return self.title

    @property
    def embed_url(self):
        if self.provider == PROVIDER_BILIBILI:
            return f"https://player.bilibili.com/player.html?bvid={self.video_id}"
        if self.provider == PROVIDER_YOUTUBE:
            return f"https://www.youtube-nocookie.com/embed/{self.video_id}"
        return ""

# Create your models here.
