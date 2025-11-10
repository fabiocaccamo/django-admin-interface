from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_interface", "0031_theme_form_actions_sticky"),
    ]

    operations = [
        migrations.AlterField(
            model_name="theme",
            name="form_actions_sticky",
            field=models.BooleanField(
                default=True,
                verbose_name="sticky actions",
            ),
        ),
        migrations.AlterField(
            model_name="theme",
            name="form_pagination_sticky",
            field=models.BooleanField(
                default=True,
                verbose_name="sticky pagination",
            ),
        ),
        migrations.AlterField(
            model_name="theme",
            name="form_submit_sticky",
            field=models.BooleanField(
                default=True,
                verbose_name="sticky submit",
            ),
        ),
        migrations.AlterField(
            model_name="theme",
            name="list_filter_removal_links",
            field=models.BooleanField(
                default=True,
                verbose_name="quick remove links for active filters at top of sidebar",
            ),
        ),
    ]
