from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_interface", "0030_theme_collapsible_stacked_inlines_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="form_actions_sticky",
            field=models.BooleanField(
                default=False,
                verbose_name="sticky actions",
            ),
        ),
    ]
