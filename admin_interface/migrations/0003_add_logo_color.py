from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0002_add_related_modal"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="logo_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#FFFFFF",
                help_text="#FFFFFF",
                max_length=10,
                verbose_name="logo color",
            ),
        ),
        migrations.AlterField(
            model_name="theme",
            name="logo",
            field=models.FileField(
                blank=True,
                help_text="(leave blank to use the default Django logo)",
                upload_to="admin-interface/logo/",
            ),
        ),
    ]
