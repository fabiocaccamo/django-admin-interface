# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_interface', '0009_add_enviroment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='active',
            field=models.BooleanField(
                default=True,
                verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css',
            field=models.TextField(
                blank=True,
                verbose_name='text color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='env',
            field=models.CharField(
                choices=[
                    ('development', 'Development'),
                    ('testing', 'Testing'),
                    ('staging', 'Staging'),
                    ('production', 'Production')
                ],
                default='development',
                max_length=50,
                verbose_name='environment'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='logo',
            field=models.FileField(
                blank=True,
                help_text='Leave blank to use the default Django logo',
                upload_to='admin-interface/logo/',
                verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(
                default='Django',
                max_length=50,
                verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='title',
            field=models.CharField(
                blank=True,
                default='Django administration',
                max_length=50,
                verbose_name='title'),
        ),
    ]
