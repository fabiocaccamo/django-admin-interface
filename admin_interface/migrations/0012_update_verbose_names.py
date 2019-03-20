# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import colorfield.fields

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_interface', '0011_add_environment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='logo_color',
            field=colorfield.fields.ColorField(blank=True, default='#FFFFFF', help_text='#FFFFFF', max_length=10, verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='title_color',
            field=colorfield.fields.ColorField(blank=True, default='#F5DD5D', help_text='#F5DD5D', max_length=10, verbose_name='color'),
        ),
    ]
