# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0004_rename_title_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="recent_actions_visible",
            field=models.BooleanField(default=True, verbose_name="visible"),
        ),
    ]
