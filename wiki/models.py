from django.conf import settings
from django.db import models

# 内容命名空间：未来新增空间（如 user:）只需加前缀，不改表结构
NAMESPACE_MAIN = "main"
NAMESPACE_GUIDE = "guide"
NAMESPACE_USER = "user"
NAMESPACE_META = "meta"
NAMESPACE_CHOICES = [
    (NAMESPACE_MAIN, "主空间（信息收录）"),
    (NAMESPACE_GUIDE, "攻略空间（预留）"),
    (NAMESPACE_USER, "用户空间（预留）"),
    (NAMESPACE_META, "站务空间"),
]

PAGE_STATUS_DRAFT = "draft"
PAGE_STATUS_PUBLISHED = "published"
PAGE_STATUS_ARCHIVED = "archived"
PAGE_STATUS_CHOICES = [
    (PAGE_STATUS_DRAFT, "草稿"),
    (PAGE_STATUS_PUBLISHED, "已发布"),
    (PAGE_STATUS_ARCHIVED, "已归档"),
]


class WikiPage(models.Model):
    """词条：主空间 / 攻略空间（预留）共用此表。"""

    namespace = models.CharField(
        "命名空间", max_length=20, choices=NAMESPACE_CHOICES, default=NAMESPACE_MAIN
    )
    slug = models.SlugField("路径标识", max_length=120)
    title = models.CharField("标题", max_length=200)
    content_md = models.TextField("Markdown 正文", blank=True)
    status = models.CharField(
        "状态", max_length=20, choices=PAGE_STATUS_CHOICES, default=PAGE_STATUS_PUBLISHED
    )
    is_protected = models.BooleanField("受保护", default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="作者",
    )
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        unique_together = ("namespace", "slug")
        ordering = ["-updated_at"]
        verbose_name = "词条"
        verbose_name_plural = "词条"

    def __str__(self):
        return f"{self.namespace}:{self.slug}"


class PageRevision(models.Model):
    """词条修订：每次保存追加一条，支持历史与回滚。"""

    page = models.ForeignKey(
        WikiPage, on_delete=models.CASCADE, related_name="revisions", verbose_name="词条"
    )
    content_md = models.TextField("Markdown 正文")
    summary = models.CharField("编辑摘要", max_length=200, blank=True)
    editor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="编辑者",
    )
    created_at = models.DateTimeField("修订时间", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "词条修订"
        verbose_name_plural = "词条修订"

    def __str__(self):
        return f"{self.page} @ {self.created_at:%Y-%m-%d %H:%M}"


class Category(models.Model):
    name = models.CharField("分类名", max_length=50, unique=True)
    slug = models.SlugField("路径标识", max_length=60, unique=True)
    description = models.TextField("描述", blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "分类"
        verbose_name_plural = "分类"

    def __str__(self):
        return self.name


class PageCategory(models.Model):
    page = models.ForeignKey(
        WikiPage, on_delete=models.CASCADE, related_name="categories", verbose_name="词条"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="pages", verbose_name="分类"
    )

    class Meta:
        unique_together = ("page", "category")
        verbose_name = "词条分类"
        verbose_name_plural = "词条分类"

# Create your models here.
