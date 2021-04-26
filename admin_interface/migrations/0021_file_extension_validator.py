# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from admin_interface.compat import FileExtensionValidator

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_interface', '0020_module_selected_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='favicon',
            field=models.FileField(
                blank=True,
                help_text='(.ico|.png|.gif - 16x16|32x32 px)',
                upload_to='admin-interface/favicon/',
                validators=[
                    FileExtensionValidator(allowed_extensions=[
                        'gif', 'ico', 'jpg', 'jpeg', 'png', 'svg'
                    ])
                ],
                verbose_name='favicon'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='logo',
            field=models.FileField(
                blank=True,
                help_text='Leave blank to use the default Django logo',
                upload_to='admin-interface/logo/',
                validators=[
                    FileExtensionValidator(allowed_extensions=[
                        'gif', 'jpg', 'jpeg', 'png', 'svg'
                    ])
                ],
                verbose_name='logo'),
        ),
    ]
