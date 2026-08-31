from django.db import migrations


def seed_categories(apps, schema_editor):
    Category = apps.get_model("wiki", "Category")
    rows = [
        ("世界观", "worldview", "神权陨落、织者、神格之力等世界设定"),
        ("英雄与职业", "heroes", "可操作英雄与职业资料"),
        ("神话生灵", "creatures", "源自全球神话的巨兽与生灵"),
        ("玩法系统", "gameplay", "组队、任务、养成等玩法资料"),
        ("新闻时间线", "news", "官方发布与开发动态"),
        ("编辑指南", "guide", "站点编辑规范与帮助"),
    ]
    for name, slug, description in rows:
        Category.objects.get_or_create(
            slug=slug, defaults={"name": name, "description": description}
        )


def unseed_categories(apps, schema_editor):
    Category = apps.get_model("wiki", "Category")
    Category.objects.filter(slug__in=["worldview", "heroes", "creatures", "gameplay", "news", "guide"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("wiki", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_categories, unseed_categories),
    ]
