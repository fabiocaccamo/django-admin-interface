# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_interface', '0014_name_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='language_chooser_active',
            field=models.BooleanField(
                default=True,
                verbose_name='active'),
        ),
    ]
