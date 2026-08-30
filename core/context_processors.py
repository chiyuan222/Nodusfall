from .models import SiteAppearance


def site_appearance(request):
    """向所有模板注入站点外观设置（背景等）。"""
    return {"site_appearance": SiteAppearance.objects.first()}
