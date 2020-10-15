# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_interface', '0017_change_list_filter_dropdown'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='list_filter_sticky',
            field=models.BooleanField(default=True, verbose_name='sticky position'),
        ),
    ]
