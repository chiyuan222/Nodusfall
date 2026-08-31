import json

from .models import SiteAppearance


def site_appearance(request):
    """向所有模板注入站点外观设置（背景等）。"""
    appearance = SiteAppearance.objects.first()
    presets = {}
    for key, colors in SiteAppearance.THEME_PRESETS.items():
        if colors:
            presets[key] = {
                "label": dict(SiteAppearance.THEME_CHOICES).get(key, key),
                "colors": colors,
            }
    return {
        "site_appearance": appearance,
        "theme_presets": presets,
        "theme_presets_json": json.dumps(presets, ensure_ascii=False),
    }
