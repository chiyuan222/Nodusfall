from django.db import migrations


def update_slogan(apps, schema_editor):
    SiteAppearance = apps.get_model("core", "SiteAppearance")
    SiteAppearance.objects.update(site_slogan="诸神入刃，斩尽死结")


def revert_slogan(apps, schema_editor):
    SiteAppearance = apps.get_model("core", "SiteAppearance")
    SiteAppearance.objects.update(
        site_slogan="《源初之结》（NODUSFALL）粉丝资料站 —— 收录设定、视频与资讯"
    )


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_set_logo_height"),
    ]

    operations = [
        migrations.RunPython(update_slogan, revert_slogan),
    ]
