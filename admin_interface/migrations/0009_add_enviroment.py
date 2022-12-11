from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0008_change_related_modal_background_opacity_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="env",
            field=models.CharField(
                choices=[
                    ("development", "Development"),
                    ("testing", "Testing"),
                    ("staging", "Staging"),
                    ("production", "Production"),
                ],
                default="development",
                max_length=50,
                verbose_name="enviroment",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="env_visible",
            field=models.BooleanField(default=True, verbose_name="visible"),
        ),
    ]
