# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import colorfield.fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_interface', '0005_add_recent_actions_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='css_delete_button_background_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#BA2121',
                help_text='#BA2121',
                max_length=10,
                verbose_name='background color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_delete_button_background_hover_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#A41515',
                help_text='#A41515',
                max_length=10,
                verbose_name='background hover color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_delete_button_text_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#FFFFFF',
                help_text='#FFFFFF',
                max_length=10,
                verbose_name='text color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_generic_link_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#0C3C26',
                help_text='#0C3C26',
                max_length=10,
                verbose_name='link color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_generic_link_hover_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#156641',
                help_text='#156641',
                max_length=10,
                verbose_name='link hover color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_header_background_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#0C4B33',
                help_text='#0C4B33',
                max_length=10,
                verbose_name='background color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_header_link_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#FFFFFF',
                help_text='#FFFFFF',
                max_length=10,
                verbose_name='link color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_header_link_hover_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#C9F0DD',
                help_text='#C9F0DD',
                max_length=10,
                verbose_name='link hover color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_header_text_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#44B78B',
                help_text='#44B78B',
                max_length=10,
                verbose_name='text color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_module_background_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#44B78B',
                help_text='#44B78B',
                max_length=10,
                verbose_name='background color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_module_link_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#FFFFFF',
                help_text='#FFFFFF',
                max_length=10,
                verbose_name='link color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_module_link_hover_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#C9F0DD',
                help_text='#C9F0DD',
                max_length=10,
                verbose_name='link hover color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_module_rounded_corners',
            field=models.BooleanField(
                default=True,
                verbose_name='rounded corners'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_module_text_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#FFFFFF',
                help_text='#FFFFFF',
                max_length=10,
                verbose_name='text color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_save_button_background_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#0C4B33',
                help_text='#0C4B33',
                max_length=10,
                verbose_name='background color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_save_button_background_hover_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#0C3C26',
                help_text='#0C3C26',
                max_length=10,
                verbose_name='background hover color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_save_button_text_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#FFFFFF',
                help_text='#FFFFFF',
                max_length=10,
                verbose_name='text color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='list_filter_dropdown',
            field=models.BooleanField(
                default=False,
                verbose_name='use dropdown'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='logo_visible',
            field=models.BooleanField(
                default=True,
                verbose_name='visible'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(
                default='Django',
                max_length=50),
        ),
        migrations.AlterField(
            model_name='theme',
            name='related_modal_active',
            field=models.BooleanField(
                default=True,
                verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='related_modal_background_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#000000',
                help_text='#000000',
                max_length=10,
                verbose_name='background color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='related_modal_background_opacity',
            field=models.FloatField(
                choices=[
                    (0.1, '10%'), (0.2, '20%'), (0.3, '30%'),
                    (0.4, '40%'), (0.5, '50%'), (0.6, '60%'),
                    (0.7, '70%'), (0.8, '80%'), (0.9, '90%')],
                default=0.2,
                help_text='20%',
                verbose_name='background opacity'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='related_modal_rounded_corners',
            field=models.BooleanField(
                default=True,
                verbose_name='rounded corners'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='title',
            field=models.CharField(
                blank=True,
                default='Django administration',
                max_length=50),
        ),
        migrations.AlterField(
            model_name='theme',
            name='title_color',
            field=colorfield.fields.ColorField(
                blank=True,
                default='#F5DD5D',
                help_text='#F5DD5D',
                max_length=10,
                verbose_name='title color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='title_visible',
            field=models.BooleanField(
                default=True,
                verbose_name='visible'),
        ),
    ]
