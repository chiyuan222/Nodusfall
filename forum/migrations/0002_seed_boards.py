from django.db import migrations


def seed_boards(apps, schema_editor):
    Board = apps.get_model("forum", "Board")
    rows = [
        ("综合讨论", "general", "游戏感想、闲聊与自由讨论", 1),
        ("攻略心得", "strategy", "英雄评测、配装与打法分享", 2),
        ("组队招募", "party", "固定队与野队招募信息", 3),
        ("同人创作", "fanwork", "画作、小说与视频创作", 4),
        ("反馈建议", "feedback", "站务与功能反馈", 5),
        ("站务公告", "notice", "社区规则与活动公告", 6),
    ]
    for name, slug, description, order in rows:
        Board.objects.get_or_create(
            slug=slug,
            defaults={
                "name": name,
                "description": description,
                "order": order,
                "is_active": True,
            },
        )


def unseed_boards(apps, schema_editor):
    Board = apps.get_model("forum", "Board")
    Board.objects.filter(slug__in=["general", "strategy", "party", "fanwork", "feedback", "notice"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("forum", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_boards, unseed_boards),
    ]
