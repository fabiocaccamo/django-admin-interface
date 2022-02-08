# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0016_add_language_chooser_display"),
    ]

    operations = [
        migrations.AlterField(
            model_name="theme",
            name="list_filter_dropdown",
            field=models.BooleanField(default=True, verbose_name="use dropdown"),
        ),
    ]
