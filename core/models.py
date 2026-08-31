from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    validate_image_file_extension,
)
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

    THEME_CHOICES = [
        ("custom", "自定义（使用下方颜色）"),
        ("dark-gold", "暗夜鎏金"),
        ("ocean", "深海蓝"),
        ("violet", "暮紫"),
        ("forest", "森林绿"),
        ("crimson", "绯红"),
        ("sunset", "落日橙"),
    ]

    THEME_PRESETS = {
        "custom": None,
        "dark-gold": {
            "accent_color": "#c9a86a",
            "panel_color": "#1b1e27",
            "text_color": "#e6e3da",
            "muted_color": "#8b8fa0",
            "border_color": "#2c3140",
        },
        "ocean": {
            "accent_color": "#5aa7d8",
            "panel_color": "#14212e",
            "text_color": "#e8f0f6",
            "muted_color": "#7d94a6",
            "border_color": "#244055",
        },
        "violet": {
            "accent_color": "#a98ad8",
            "panel_color": "#221a33",
            "text_color": "#ece5f5",
            "muted_color": "#9a8ab0",
            "border_color": "#352a4a",
        },
        "forest": {
            "accent_color": "#7fbf7f",
            "panel_color": "#14241a",
            "text_color": "#e6f2e6",
            "muted_color": "#8aa890",
            "border_color": "#244033",
        },
        "crimson": {
            "accent_color": "#d88a8a",
            "panel_color": "#2a1616",
            "text_color": "#f5e6e6",
            "muted_color": "#b08a8a",
            "border_color": "#462424",
        },
        "sunset": {
            "accent_color": "#e8a86a",
            "panel_color": "#2a1d12",
            "text_color": "#f5ead9",
            "muted_color": "#b39a7d",
            "border_color": "#45331f",
        },
    }

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
        default="诸神入刃，斩尽死结",
    )

    logo_image = models.URLField(
        "Logo 图片链接",
        blank=True,
        help_text="留空则显示站点名称文字；可填图床 PNG/SVG 地址",
    )
    logo_height = models.PositiveIntegerField("Logo 高度（px）", default=40)

    accent_color = models.CharField("主题色", max_length=20, default="#c9a86a")
    panel_color = models.CharField("面板色", max_length=20, default="#1b1e27")
    text_color = models.CharField("文字色", max_length=20, default="#e6e3da")
    muted_color = models.CharField("次要文字色", max_length=20, default="#8b8fa0")
    border_color = models.CharField("边框色", max_length=20, default="#2c3140")

    background_image = models.URLField(
        "背景图片链接",
        blank=True,
        help_text="图片链接与下方文件二选一；留空则使用纯色背景",
    )
    background_image_file = models.ImageField(
        "背景图片文件（jpg/png）",
        upload_to="backgrounds/",
        blank=True,
        validators=[validate_image_file_extension],
        help_text="直接上传 jpg/png 图片；与上方链接二选一",
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
    theme = models.CharField(
        "主题预设", max_length=20, choices=THEME_CHOICES, default="custom"
    )

    class Meta:
        verbose_name = "站点外观"
        verbose_name_plural = "站点外观"

    def __str__(self):
        return "站点外观设置"

    @property
    def colors(self):
        """当前生效的配色：主题预设优先，其次为自定义颜色。"""
        preset = self.THEME_PRESETS.get(self.theme)
        if preset:
            return preset
        return {
            "accent_color": self.accent_color,
            "panel_color": self.panel_color,
            "text_color": self.text_color,
            "muted_color": self.muted_color,
            "border_color": self.border_color,
        }

    @property
    def background_url(self):
        """背景图片：文件优先，其次为链接。"""
        if self.background_image_file:
            return self.background_image_file.url
        return self.background_image

# Create your models here.
