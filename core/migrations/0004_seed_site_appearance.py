from django.db import migrations


def seed_appearance(apps, schema_editor):
    SiteAppearance = apps.get_model("core", "SiteAppearance")
    if not SiteAppearance.objects.exists():
        SiteAppearance.objects.create(
            background_image="",
            background_color="#12141a",
            background_size="cover",
            background_position="center center",
        )


def unseed_appearance(apps, schema_editor):
    SiteAppearance = apps.get_model("core", "SiteAppearance")
    SiteAppearance.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_siteappearance"),
    ]

    operations = [
        migrations.RunPython(seed_appearance, unseed_appearance),
    ]
