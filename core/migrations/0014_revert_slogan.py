from django.db import migrations


def revert_slogan(apps, schema_editor):
    SiteAppearance = apps.get_model("core", "SiteAppearance")
    SiteAppearance.objects.update(
        site_slogan="《源初之结》（NODUSFALL）粉丝资料站 —— 收录设定、视频与资讯"
    )


def restore_new_slogan(apps, schema_editor):
    SiteAppearance = apps.get_model("core", "SiteAppearance")
    SiteAppearance.objects.update(site_slogan="诸神入刃，斩尽死结")


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0013_alter_siteappearance_accent_color_and_more"),
    ]

    operations = [
        migrations.RunPython(revert_slogan, restore_new_slogan),
    ]
