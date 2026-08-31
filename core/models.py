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
        ("dark-gold", "深空靛蓝"),
        ("ocean", "海蓝"),
        ("violet", "紫罗兰"),
        ("forest", "薄荷绿"),
        ("crimson", "珊瑚红"),
        ("sunset", "琥珀橙"),
    ]

    THEME_PRESETS = {
        "custom": None,
        "dark-gold": {
            "accent_color": "#6366f1",
            "panel_color": "#14161f",
            "text_color": "#e8eaf2",
            "muted_color": "#9aa0b0",
            "border_color": "#262a38",
        },
        "ocean": {
            "accent_color": "#38bdf8",
            "panel_color": "#0f172a",
            "text_color": "#e8f1fb",
            "muted_color": "#8aa3bf",
            "border_color": "#1e3a5f",
        },
        "violet": {
            "accent_color": "#a78bfa",
            "panel_color": "#171322",
            "text_color": "#ece9f8",
            "muted_color": "#a39ab8",
            "border_color": "#322a4a",
        },
        "forest": {
            "accent_color": "#34d399",
            "panel_color": "#0f1a17",
            "text_color": "#e6f4ef",
            "muted_color": "#8fb3a7",
            "border_color": "#1f3a32",
        },
        "crimson": {
            "accent_color": "#fb7185",
            "panel_color": "#1a1216",
            "text_color": "#f9eef0",
            "muted_color": "#bd9aa1",
            "border_color": "#40242c",
        },
        "sunset": {
            "accent_color": "#fbbf24",
            "panel_color": "#1a1510",
            "text_color": "#f8f1e4",
            "muted_color": "#b8a88c",
            "border_color": "#3a3123",
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
        default="《源初之结》（NODUSFALL）粉丝资料站 —— 收录设定、视频与资讯",
    )

    logo_image = models.URLField(
        "Logo 图片链接",
        blank=True,
        help_text="留空则显示站点名称文字；可填图床 PNG/SVG 地址",
    )
    logo_height = models.PositiveIntegerField("Logo 高度（px）", default=40)

    accent_color = models.CharField("主题色", max_length=20, default="#6366f1")
    panel_color = models.CharField("面板色", max_length=20, default="#14161f")
    text_color = models.CharField("文字色", max_length=20, default="#e8eaf2")
    muted_color = models.CharField("次要文字色", max_length=20, default="#9aa0b0")
    border_color = models.CharField("边框色", max_length=20, default="#262a38")

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
        "背景颜色", max_length=20, default="#0f1117", help_text="十六进制颜色，如 #0f1117"
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
