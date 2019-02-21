# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_delete, post_save
from django.utils.encoding import python_2_unicode_compatible, force_text
from django.utils.translation import ugettext_lazy as _

from colorfield.fields import ColorField


@python_2_unicode_compatible
class Theme(models.Model):

    @staticmethod
    def post_migrate_handler(**kwargs):
        Theme.get_active_theme()

    @staticmethod
    def post_delete_handler(**kwargs):
        Theme.get_active_theme()

    @staticmethod
    def post_save_handler(instance, **kwargs):
        if instance.active:
            Theme.objects.exclude(pk=instance.pk).update(active=False)
        Theme.get_active_theme()

    @staticmethod
    def get_active_theme():
        objs_manager = Theme.objects
        objs_active_qs = objs_manager.filter(active=True)
        objs_active_ls = list(objs_active_qs)
        objs_active_count = len(objs_active_ls)

        if objs_active_count == 0:
            obj = objs_manager.all().first()
            if obj:
                obj.set_active()
            else:
                obj = objs_manager.create()

        elif objs_active_count == 1:
            obj = objs_active_ls[0]

        elif objs_active_count > 1:
            obj = objs_active_ls[-1]
            obj.set_active()

        return obj

    name = models.CharField(
        max_length=50,
        default='Django',
        verbose_name=_('name'))
    active = models.BooleanField(
        default=True,
        verbose_name=_('active'))

    title = models.CharField(
        max_length=50,
        default=_('Django administration'),
        blank=True,
        verbose_name=_('title'))
    title_color = ColorField(
        blank=True,
        default='#F5DD5D',
        help_text='#F5DD5D',
        max_length=10,
        verbose_name=_('title color'))
    title_visible = models.BooleanField(
        default=True,
        verbose_name=_('visible'))

    logo = models.FileField(
        upload_to='admin-interface/logo/',
        blank=True,
        help_text=_('Leave blank to use the default Django logo'),
        verbose_name=_('logo'))
    logo_color = ColorField(
        blank=True,
        default='#FFFFFF',
        help_text='#FFFFFF',
        max_length=10,
        verbose_name=_('logo color'))
    logo_visible = models.BooleanField(
        default=True,
        verbose_name=_('visible'))

    favicon = models.FileField(
        upload_to='admin-interface/favicon/',
        blank=True,
        help_text=_('(.ico|.png|.gif - 16x16|32x32 px)'),
        verbose_name=_('favicon'))

    envs = (
        'development',
        'testing',
        'staging',
        'production',
    )
    env_choices = (
        (envs[0], _('Development'), ),
        (envs[1], _('Testing'), ),
        (envs[2], _('Staging'), ),
        (envs[3], _('Production'), ),
    )
    env = models.CharField(
        max_length=50,
        choices=env_choices,
        default=env_choices[0][0],
        verbose_name=_('environment'))
    env_visible = models.BooleanField(
        default=True,
        verbose_name=_('visible'))
    env_colors = {
        envs[0]: '#e74c3c',
        envs[1]: '#e67e22',
        envs[2]: '#f1c40f',
        envs[3]: '#2ecc71',
    }
    @property
    def env_color(self):
        return Theme.env_colors.get(self.env, '')

    css_header_background_color = ColorField(
        blank=True,
        default='#0C4B33',
        help_text='#0C4B33',
        max_length=10,
        verbose_name=_('background color'))
    css_header_text_color = ColorField(
        blank=True,
        default='#44B78B',
        help_text='#44B78B',
        max_length=10,
        verbose_name=_('text color'))
    css_header_link_color = ColorField(
        blank=True,
        default='#FFFFFF',
        help_text='#FFFFFF',
        max_length=10,
        verbose_name=_('link color'))
    css_header_link_hover_color = ColorField(
        blank=True,
        default='#C9F0DD',
        help_text='#C9F0DD',
        max_length=10,
        verbose_name=_('link hover color'))

    css_module_background_color = ColorField(
        blank=True,
        default='#44B78B',
        help_text='#44B78B',
        max_length=10,
        verbose_name=_('background color'))
    css_module_text_color = ColorField(
        blank=True,
        default='#FFFFFF',
        help_text='#FFFFFF',
        max_length=10,
        verbose_name=_('text color'))
    css_module_link_color = ColorField(
        blank=True,
        default='#FFFFFF',
        help_text='#FFFFFF',
        max_length=10,
        verbose_name=_('link color'))
    css_module_link_hover_color = ColorField(
        blank=True,
        default='#C9F0DD',
        help_text='#C9F0DD',
        max_length=10,
        verbose_name=_('link hover color'))
    css_module_rounded_corners = models.BooleanField(
        default=True,
        verbose_name=_('rounded corners'))

    css_generic_link_color = ColorField(
        blank=True,
        default='#0C3C26',
        help_text='#0C3C26',
        max_length=10,
        verbose_name=_('link color'))
    css_generic_link_hover_color = ColorField(
        blank=True,
        default='#156641',
        help_text='#156641',
        max_length=10,
        verbose_name=_('link hover color'))

    css_save_button_background_color = ColorField(
        blank=True,
        default='#0C4B33',
        help_text='#0C4B33',
        max_length=10,
        verbose_name=_('background color'))
    css_save_button_background_hover_color = ColorField(
        blank=True,
        default='#0C3C26',
        help_text='#0C3C26',
        max_length=10,
        verbose_name=_('background hover color'))
    css_save_button_text_color = ColorField(
        blank=True,
        default='#FFFFFF',
        help_text='#FFFFFF',
        max_length=10,
        verbose_name=_('text color'))

    css_delete_button_background_color = ColorField(
        blank=True,
        default='#BA2121',
        help_text='#BA2121',
        max_length=10,
        verbose_name=_('background color'))
    css_delete_button_background_hover_color = ColorField(
        blank=True,
        default='#A41515',
        help_text='#A41515',
        max_length=10,
        verbose_name=_('background hover color'))
    css_delete_button_text_color = ColorField(
        blank=True,
        default='#FFFFFF',
        help_text='#FFFFFF',
        max_length=10,
        verbose_name=_('text color'))

    css = models.TextField(
        blank=True,
        verbose_name=_('text color'))

    related_modal_active = models.BooleanField(
        default=True,
        verbose_name=_('active'))
    related_modal_background_color = ColorField(
        blank=True,
        default='#000000',
        help_text='#000000',
        max_length=10,
        verbose_name=_('background color'))
    related_modal_background_opacity_choices = (
        ('0.1', '10%', ),
        ('0.2', '20%', ),
        ('0.3', '30%', ),
        ('0.4', '40%', ),
        ('0.5', '50%', ),
        ('0.6', '60%', ),
        ('0.7', '70%', ),
        ('0.8', '80%', ),
        ('0.9', '90%', ),
    )
    related_modal_background_opacity = models.CharField(
        max_length=5,
        choices=related_modal_background_opacity_choices,
        default='0.3',
        help_text='20%',
        verbose_name=_('background opacity'))
    related_modal_rounded_corners = models.BooleanField(
        default=True,
        verbose_name=_('rounded corners'))

    list_filter_dropdown = models.BooleanField(
        default=False,
        verbose_name=_('use dropdown'))
    recent_actions_visible = models.BooleanField(
        default=True,
        verbose_name=_('visible'))

    def set_active(self):
        self.active = True
        self.save()

    class Meta:
        app_label = 'admin_interface'

        verbose_name = _('Theme')
        verbose_name_plural = _('Themes')

    def __str__(self):
        return force_text(self.name)


post_delete.connect(Theme.post_delete_handler, sender=Theme)
post_save.connect(Theme.post_save_handler, sender=Theme)
