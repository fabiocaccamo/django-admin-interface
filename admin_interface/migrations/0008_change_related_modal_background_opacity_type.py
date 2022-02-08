# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0007_add_favicon"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="theme", name="related_modal_background_opacity"
        ),
        migrations.AddField(
            model_name="theme",
            name="related_modal_background_opacity",
            field=models.CharField(
                choices=[
                    ("0.1", "10%"),
                    ("0.2", "20%"),
                    ("0.3", "30%"),
                    ("0.4", "40%"),
                    ("0.5", "50%"),
                    ("0.6", "60%"),
                    ("0.7", "70%"),
                    ("0.8", "80%"),
                    ("0.9", "90%"),
                ],
                default="0.3",
                help_text="20%",
                max_length=5,
                verbose_name="background opacity",
            ),
        ),
    ]
