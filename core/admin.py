from django.contrib import admin

from .models import FeaturedItem, HomeSlide, OfficialLink, SiteAppearance


@admin.register(HomeSlide)
class HomeSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "image_url", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(FeaturedItem)
class FeaturedItemAdmin(admin.ModelAdmin):
    list_display = ("title", "link_url", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(OfficialLink)
class OfficialLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "order")
    list_editable = ("order",)


@admin.register(SiteAppearance)
class SiteAppearanceAdmin(admin.ModelAdmin):
    """单例设置：已有记录时不允许重复添加。"""

    list_display = (
        "site_name",
        "logo_image",
        "accent_color",
        "background_color",
        "background_image",
        "overlay_opacity",
    )

    def has_add_permission(self, request):
        return not SiteAppearance.objects.exists()

# Register your models here.
