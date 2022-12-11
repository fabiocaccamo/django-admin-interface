from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0021_file_extension_validator"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="logo_max_height",
            field=models.PositiveSmallIntegerField(
                blank=True, default=100, verbose_name="max height"
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="logo_max_width",
            field=models.PositiveSmallIntegerField(
                blank=True, default=400, verbose_name="max width"
            ),
        ),
    ]
