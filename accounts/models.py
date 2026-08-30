from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """站点用户。Wiki、论坛、个人攻略共用同一账号体系。"""

    nickname = models.CharField("昵称", max_length=50, blank=True)
    bio = models.TextField("个人简介", blank=True)
    avatar = models.URLField("头像链接", blank=True)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.nickname or self.username

# Create your models here.
