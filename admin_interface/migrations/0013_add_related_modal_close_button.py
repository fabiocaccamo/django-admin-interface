# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_interface', '0012_update_verbose_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='related_modal_close_button_visible',
            field=models.BooleanField(
                default=True,
                verbose_name='close button visible'),
        ),
    ]
