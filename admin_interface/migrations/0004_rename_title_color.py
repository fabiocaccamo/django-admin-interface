# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_interface', '0003_add_logo_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theme',
            old_name='css_header_title_color',
            new_name='title_color',
        ),
    ]
