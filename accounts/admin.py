from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

admin.site.site_header = "织者档案馆 · 管理后台"
admin.site.site_title = "织者档案馆"
admin.site.index_title = "站点管理"

admin.site.register(User, UserAdmin)

# Register your models here.
