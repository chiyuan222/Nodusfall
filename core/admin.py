from django import forms
from django.contrib import admin

from .models import FeaturedItem, HomeSlide, OfficialLink, SiteAppearance


def color_widget():
    """颜色字段使用原生调色盘选择器。"""
    return forms.TextInput(
        attrs={
            "type": "color",
            "style": "height:38px;width:90px;padding:2px 4px;cursor:pointer;",
        }
    )


class SiteAppearanceForm(forms.ModelForm):
    class Meta:
        model = SiteAppearance
        fields = "__all__"
        widgets = {
            "background_color": color_widget(),
            "accent_color": color_widget(),
            "panel_color": color_widget(),
            "text_color": color_widget(),
            "muted_color": color_widget(),
            "border_color": color_widget(),
        }


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

    form = SiteAppearanceForm

    list_display = (
        "site_name",
        "theme",
        "logo_image",
        "accent_color",
        "background_color",
        "background_image",
        "overlay_opacity",
    )

    def has_add_permission(self, request):
        return not SiteAppearance.objects.exists()

# Register your models here.
