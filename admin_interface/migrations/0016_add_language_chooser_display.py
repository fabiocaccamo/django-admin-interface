# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_interface', '0015_add_language_chooser_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='language_chooser_display',
            field=models.CharField(choices=[('code', 'code'), ('name', 'name')], default='code', max_length=10, verbose_name='display'),
        ),
    ]
