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

# Create your models here.
