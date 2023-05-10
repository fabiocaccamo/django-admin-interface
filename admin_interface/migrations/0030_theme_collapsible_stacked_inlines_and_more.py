from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_interface", "0029_theme_css_generic_link_active_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="collapsible_stacked_inlines",
            field=models.BooleanField(
                default=False,
                verbose_name="collapsible stacked inlines",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="collapsible_stacked_inlines_collapsed",
            field=models.BooleanField(
                default=True,
                verbose_name="collapsible stacked inlines collapsed",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="collapsible_tabular_inlines",
            field=models.BooleanField(
                default=False,
                verbose_name="collapsible tabular inlines",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="collapsible_tabular_inlines_collapsed",
            field=models.BooleanField(
                default=True,
                verbose_name="collapsible tabular inlines collapsed",
            ),
        ),
    ]
