from django.db import models


class Board(models.Model):
    """论坛版块。"""

    name = models.CharField("版块名称", max_length=50)
    slug = models.SlugField("路径标识", max_length=60, unique=True)
    description = models.TextField("版块说明", blank=True)
    order = models.PositiveIntegerField("排序", default=0)
    is_active = models.BooleanField("启用", default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "论坛版块"
        verbose_name_plural = "论坛版块"

    def __str__(self):
        return self.name

# Create your models here.
