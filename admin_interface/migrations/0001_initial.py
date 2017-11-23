# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations

import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id',
                    models.AutoField(
                        verbose_name='ID',
                        serialize=False,
                        auto_created=True,
                        primary_key=True)),
                ('name',
                    models.CharField(
                        default=b'Django',
                        max_length=50)),
                ('active',
                    models.BooleanField(
                        default=True)),
                ('title',
                    models.CharField(
                        default=b'Django administration',
                        max_length=50,
                        blank=True)),
                ('title_visible',
                    models.BooleanField(
                        default=True,
                        verbose_name=b'visible')),
                ('logo',
                    models.FileField(
                        upload_to=b'admin-interface/logo/',
                        blank=True)),
                ('logo_visible',
                    models.BooleanField(
                        default=True,
                        verbose_name=b'visible')),
                ('css_header_background_color',
                    colorfield.fields.ColorField(
                        default=b'#0C4B33',
                        help_text=b'#0C4B33',
                        max_length=10,
                        verbose_name=b'background color',
                        blank=True)),
                ('css_header_title_color',
                    colorfield.fields.ColorField(
                        default=b'#F5DD5D',
                        help_text=b'#F5DD5D',
                        max_length=10,
                        verbose_name=b'title color',
                        blank=True)),
                ('css_header_text_color',
                    colorfield.fields.ColorField(
                        default=b'#44B78B',
                        help_text=b'#44B78B',
                        max_length=10,
                        verbose_name=b'text color',
                        blank=True)),
                ('css_header_link_color',
                    colorfield.fields.ColorField(
                        default=b'#FFFFFF',
                        help_text=b'#FFFFFF',
                        max_length=10,
                        verbose_name=b'link color',
                        blank=True)),
                ('css_header_link_hover_color',
                    colorfield.fields.ColorField(
                        default=b'#C9F0DD',
                        help_text=b'#C9F0DD',
                        max_length=10,
                        verbose_name=b'link hover color',
                        blank=True)),
                ('css_module_background_color',
                    colorfield.fields.ColorField(
                        default=b'#44B78B',
                        help_text=b'#44B78B',
                        max_length=10,
                        verbose_name=b'background color',
                        blank=True)),
                ('css_module_text_color',
                    colorfield.fields.ColorField(
                        default=b'#FFFFFF',
                        help_text=b'#FFFFFF',
                        max_length=10,
                        verbose_name=b'text color',
                        blank=True)),
                ('css_module_link_color',
                    colorfield.fields.ColorField(
                        default=b'#FFFFFF',
                        help_text=b'#FFFFFF',
                        max_length=10,
                        verbose_name=b'link color',
                        blank=True)),
                ('css_module_link_hover_color',
                    colorfield.fields.ColorField(
                        default=b'#C9F0DD',
                        help_text=b'#C9F0DD',
                        max_length=10,
                        verbose_name=b'link hover color',
                        blank=True)),
                ('css_module_rounded_corners',
                    models.BooleanField(
                        default=True,
                        verbose_name=b'rounded corners')),
                ('css_generic_link_color',
                    colorfield.fields.ColorField(
                        default=b'#0C3C26',
                        help_text=b'#0C3C26',
                        max_length=10,
                        verbose_name=b'link color',
                        blank=True)),
                ('css_generic_link_hover_color',
                    colorfield.fields.ColorField(
                        default=b'#156641',
                        help_text=b'#156641',
                        max_length=10,
                        verbose_name=b'link hover color',
                        blank=True)),
                ('css_save_button_background_color',
                    colorfield.fields.ColorField(
                        default=b'#0C4B33',
                        help_text=b'#0C4B33',
                        max_length=10,
                        verbose_name=b'background color',
                        blank=True)),
                ('css_save_button_background_hover_color',
                    colorfield.fields.ColorField(
                        default=b'#0C3C26',
                        help_text=b'#0C3C26',
                        max_length=10,
                        verbose_name=b'background hover color',
                        blank=True)),
                ('css_save_button_text_color',
                    colorfield.fields.ColorField(
                        default=b'#FFFFFF',
                        help_text=b'#FFFFFF',
                        max_length=10,
                        verbose_name=b'text color',
                        blank=True)),
                ('css_delete_button_background_color',
                    colorfield.fields.ColorField(
                        default=b'#BA2121',
                        help_text=b'#BA2121',
                        max_length=10,
                        verbose_name=b'background color',
                        blank=True)),
                ('css_delete_button_background_hover_color',
                    colorfield.fields.ColorField(
                        default=b'#A41515',
                        help_text=b'#A41515',
                        max_length=10,
                        verbose_name=b'background hover color',
                        blank=True)),
                ('css_delete_button_text_color',
                    colorfield.fields.ColorField(
                        default=b'#FFFFFF',
                        help_text=b'#FFFFFF',
                        max_length=10,
                        verbose_name=b'text color',
                        blank=True)),
                ('css',
                    models.TextField(
                        blank=True)),
                ('list_filter_dropdown',
                    models.BooleanField(
                        default=False)),
            ],
            options={
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Themes',
            },
        ),
    ]
