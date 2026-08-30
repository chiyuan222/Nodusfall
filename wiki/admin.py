from django.contrib import admin

from .models import Category, PageCategory, PageRevision, WikiPage


class PageRevisionInline(admin.TabularInline):
    model = PageRevision
    extra = 0
    readonly_fields = ("created_at",)


class PageCategoryInline(admin.TabularInline):
    model = PageCategory
    extra = 0


@admin.register(WikiPage)
class WikiPageAdmin(admin.ModelAdmin):
    list_display = ("title", "namespace", "slug", "status", "is_protected", "updated_at")
    list_filter = ("namespace", "status", "is_protected")
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PageRevisionInline, PageCategoryInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

# Register your models here.
