from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_interface", "0026_theme_list_filter_highlight"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="list_filter_removal_links",
            field=models.BooleanField(
                default=False,
                verbose_name="quick remove links for active filters at top of sidebar",
            ),
        ),
    ]
