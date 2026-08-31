from django.db import migrations


def update_colors(apps, schema_editor):
    SiteAppearance = apps.get_model("core", "SiteAppearance")
    SiteAppearance.objects.update(
        background_color="#0f1117",
        accent_color="#6366f1",
        panel_color="#14161f",
        text_color="#e8eaf2",
        muted_color="#9aa0b0",
        border_color="#262a38",
    )


def revert_colors(apps, schema_editor):
    SiteAppearance = apps.get_model("core", "SiteAppearance")
    SiteAppearance.objects.update(
        background_color="#12141a",
        accent_color="#c9a86a",
        panel_color="#1b1e27",
        text_color="#e6e3da",
        muted_color="#8b8fa0",
        border_color="#2c3140",
    )


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_alter_siteappearance_site_slogan"),
    ]

    operations = [
        migrations.RunPython(update_colors, revert_colors),
    ]
