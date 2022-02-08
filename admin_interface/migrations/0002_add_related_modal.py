# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models

import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="theme",
            name="list_filter_dropdown",
            field=models.BooleanField(default=False, verbose_name=b"use dropdown"),
        ),
        migrations.AddField(
            model_name="theme",
            name="related_modal_active",
            field=models.BooleanField(default=True, verbose_name=b"active"),
        ),
        migrations.AddField(
            model_name="theme",
            name="related_modal_background_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default=b"#000000",
                help_text=b"#000000",
                max_length=10,
                verbose_name=b"background color",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="related_modal_background_opacity",
            field=models.FloatField(
                choices=[
                    (0.1, b"10%"),
                    (0.2, b"20%"),
                    (0.3, b"30%"),
                    (0.4, b"40%"),
                    (0.5, b"50%"),
                    (0.6, b"60%"),
                    (0.7, b"70%"),
                    (0.8, b"80%"),
                    (0.9, b"90%"),
                ],
                default=0.2,
                help_text=b"20%",
                verbose_name=b"background opacity",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="related_modal_rounded_corners",
            field=models.BooleanField(default=True, verbose_name=b"rounded corners"),
        ),
    ]
