from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0010_add_localization"),
    ]

    operations = [
        migrations.RenameField(
            model_name="theme",
            old_name="env",
            new_name="env_name",
        ),
        migrations.AlterField(
            model_name="theme",
            name="env_name",
            field=models.CharField(blank=True, max_length=50, verbose_name="name"),
        ),
        migrations.AddField(
            model_name="theme",
            name="env_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#E74C3C",
                help_text="(red: #E74C3C, orange: #E67E22, yellow: #F1C40F, green: #2ECC71, blue: #3498DB)",
                max_length=10,
                verbose_name="color",
            ),
        ),
        migrations.RenameField(
            model_name="theme",
            old_name="env_visible",
            new_name="env_visible_in_header",
        ),
        migrations.AlterField(
            model_name="theme",
            name="env_visible_in_header",
            field=models.BooleanField(
                default=True, verbose_name="visible in header (marker and name)"
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="env_visible_in_favicon",
            field=models.BooleanField(
                default=True, verbose_name="visible in favicon (marker)"
            ),
        ),
    ]
