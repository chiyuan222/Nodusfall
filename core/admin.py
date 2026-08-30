from django.contrib import admin

from .models import FeaturedItem, HomeSlide, OfficialLink


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

# Register your models here.
