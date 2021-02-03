# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from admin_interface.cache import del_cached_active_theme

from colorfield.fields import ColorField

import django
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
if django.VERSION < (2, 0):
    from django.utils.encoding import force_text as force_str
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.encoding import force_str
    from django.utils.translation import gettext_lazy as _

from six import python_2_unicode_compatible


@python_2_unicode_compatible
class Theme(models.Model):

    @staticmethod
    def post_migrate_handler(**kwargs):
        del_cached_active_theme()
        Theme.get_active_theme()

    @staticmethod
    def post_delete_handler(**kwargs):
        del_cached_active_theme()
        Theme.get_active_theme()

    @staticmethod
    def post_save_handler(instance, **kwargs):
        del_cached_active_theme()
        if instance.active:
            Theme.objects.exclude(pk=instance.pk).update(active=False)
        Theme.get_active_theme()

    @staticmethod
    def pre_save_handler(instance, **kwargs):
        if instance.pk is None:
            try:
                obj = Theme.objects.get(name=instance.name)
                if obj:
                    instance.pk = obj.pk
            except Theme.DoesNotExist:
                pass

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
        unique=True,
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
        verbose_name=_('color'))
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
        verbose_name=_('color'))
    logo_visible = models.BooleanField(
        default=True,
        verbose_name=_('visible'))

    favicon = models.FileField(
        upload_to='admin-interface/favicon/',
        blank=True,
        help_text=_('(.ico|.png|.gif - 16x16|32x32 px)'),
        verbose_name=_('favicon'))

    env_name = models.CharField(
        blank=True,
        max_length=50,
        verbose_name=_('name'))
    env_color = ColorField(
        blank=True,
        default='#E74C3C',
        help_text=_('(red: #E74C3C, orange: #E67E22, yellow: #F1C40F, green: #2ECC71, blue: #3498DB)'),
        max_length=10,
        verbose_name=_('color'))
    env_visible_in_header = models.BooleanField(
        default=True,
        verbose_name=_('visible in header (marker and name)'))
    env_visible_in_favicon = models.BooleanField(
        default=True,
        verbose_name=_('visible in favicon (marker)'))

    language_chooser_active = models.BooleanField(
        default=True,
        verbose_name=_('active'))
    language_chooser_display_choices = (
        ('code', _('code'), ),
        ('name', _('name'), ),
    )
    language_chooser_display = models.CharField(
        max_length=10,
        choices=language_chooser_display_choices,
        default='code',
        verbose_name=_('display'))

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
    related_modal_close_button_visible = models.BooleanField(
        default=True,
        verbose_name=_('close button visible'))

    list_filter_dropdown = models.BooleanField(
        default=True,
        verbose_name=_('use dropdown'))
    list_filter_sticky = models.BooleanField(
        default=True,
        verbose_name=_('sticky position'))

    recent_actions_visible = models.BooleanField(
        default=True,
        verbose_name=_('visible'))

    form_submit_sticky = models.BooleanField(
        default=False,
        verbose_name=_('sticky submit'))
    form_pagination_sticky = models.BooleanField(
        default=False,
        verbose_name=_('sticky pagination'))

    def set_active(self):
        self.active = True
        self.save()

    class Meta:
        app_label = 'admin_interface'

        verbose_name = _('Theme')
        verbose_name_plural = _('Themes')

    def __str__(self):
        return force_str(self.name)


post_delete.connect(Theme.post_delete_handler, sender=Theme)
post_save.connect(Theme.post_save_handler, sender=Theme)
pre_save.connect(Theme.pre_save_handler, sender=Theme)
