from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class HomeSlide(models.Model):
    """首页轮播图（推荐图片帖）。"""

    title = models.CharField("标题", max_length=100)
    image_url = models.URLField("图片链接", help_text="可填站外图片地址或站内 /static/ 路径")
    link_url = models.URLField("跳转链接", blank=True, help_text="点击图片后跳转的地址，可留空")
    order = models.PositiveIntegerField("排序", default=0)
    is_active = models.BooleanField("启用", default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "首页轮播图"
        verbose_name_plural = "首页轮播图"

    def __str__(self):
        return self.title


class FeaturedItem(models.Model):
    """首页「精华推荐」条目。"""

    title = models.CharField("标题", max_length=100)
    link_url = models.URLField("跳转链接")
    description = models.CharField("简介", max_length=200, blank=True)
    order = models.PositiveIntegerField("排序", default=0)
    is_active = models.BooleanField("启用", default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "精华推荐"
        verbose_name_plural = "精华推荐"

    def __str__(self):
        return self.title


class OfficialLink(models.Model):
    """首页「官方信息」链接。"""

    name = models.CharField("名称", max_length=50)
    url = models.URLField("链接")
    order = models.PositiveIntegerField("排序", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "官方信息链接"
        verbose_name_plural = "官方信息链接"

    def __str__(self):
        return self.name


class SiteAppearance(models.Model):
    """站点外观设置（单例，后台可修改背景等，前台立即生效）。"""

    BACKGROUND_SIZE_CHOICES = [
        ("cover", "铺满（cover）"),
        ("contain", "完整显示（contain）"),
        ("repeat", "原尺寸重复"),
    ]

    site_name = models.CharField("站点名称", max_length=50, default="源神小窝")
    site_slogan = models.CharField(
        "站点标语",
        max_length=120,
        blank=True,
        default="《源初之结》（NODUSFALL）粉丝资料站 —— 收录设定、视频与资讯",
    )

    logo_image = models.URLField(
        "Logo 图片链接",
        blank=True,
        help_text="留空则显示站点名称文字；可填图床 PNG/SVG 地址",
    )
    logo_height = models.PositiveIntegerField("Logo 高度（px）", default=32)

    accent_color = models.CharField("主题色", max_length=20, default="#c9a86a")
    panel_color = models.CharField("面板色", max_length=20, default="#1b1e27")
    text_color = models.CharField("文字色", max_length=20, default="#e6e3da")
    muted_color = models.CharField("次要文字色", max_length=20, default="#8b8fa0")
    border_color = models.CharField("边框色", max_length=20, default="#2c3140")

    background_image = models.URLField(
        "背景图片链接",
        blank=True,
        help_text="留空则使用纯色背景；可填图床图片地址",
    )
    background_color = models.CharField(
        "背景颜色", max_length=20, default="#12141a", help_text="十六进制颜色，如 #12141a"
    )
    background_size = models.CharField(
        "背景尺寸",
        max_length=20,
        choices=BACKGROUND_SIZE_CHOICES,
        default="cover",
    )
    background_position = models.CharField(
        "背景位置",
        max_length=30,
        default="center center",
        help_text="如 center center / top left",
    )
    overlay_opacity = models.FloatField(
        "背景遮罩不透明度",
        default=0.55,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        help_text="0 = 不遮罩，1 = 全黑遮罩；背景图存在时生效",
    )

    class Meta:
        verbose_name = "站点外观"
        verbose_name_plural = "站点外观"

    def __str__(self):
        return "站点外观设置"

# Create your models here.
