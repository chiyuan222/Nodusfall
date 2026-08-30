from django.db import migrations


def seed_slides(apps, schema_editor):
    HomeSlide = apps.get_model("core", "HomeSlide")
    slides = [
        ("示例推荐位 1", "/static/img/slide-1.svg", 1),
        ("示例推荐位 2", "/static/img/slide-2.svg", 2),
        ("示例推荐位 3", "/static/img/slide-3.svg", 3),
    ]
    for title, image_url, order in slides:
        HomeSlide.objects.get_or_create(
            image_url=image_url,
            defaults={"title": title, "order": order, "is_active": True},
        )


def unseed_slides(apps, schema_editor):
    HomeSlide = apps.get_model("core", "HomeSlide")
    HomeSlide.objects.filter(image_url__startswith="/static/img/slide-").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_slides, unseed_slides),
    ]
