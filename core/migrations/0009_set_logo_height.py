from django.db import migrations


def set_logo_height(apps, schema_editor):
    SiteAppearance = apps.get_model("core", "SiteAppearance")
    SiteAppearance.objects.update(logo_height=40)


def unset_logo_height(apps, schema_editor):
    SiteAppearance = apps.get_model("core", "SiteAppearance")
    SiteAppearance.objects.update(logo_height=32)


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_alter_siteappearance_logo_height"),
    ]

    operations = [
        migrations.RunPython(set_logo_height, unset_logo_height),
    ]
