# -*- coding: utf-8 -*-

from django.core.files import File
from django.db import models
from django.db.models.signals import post_delete, post_save

from colorfield.fields import ColorField

import os


class Theme(models.Model):

    @staticmethod
    def post_migrate_handler(sender, **kwargs):
        Theme.get_active_theme()

    @staticmethod
    def post_delete_handler(instance, **kwargs):
        Theme.get_active_theme()

    @staticmethod
    def post_save_handler(instance, created, **kwargs):
        Theme.get_active_theme()

    @staticmethod
    def get_active_theme():

        objs_active_qs = Theme.objects.filter( active = True )

        #get or create default theme and enforce default logo if deleted
        default_obj_active = (objs_active_qs.count() == 0)
        default_obj, default_obj_created = Theme.objects.get_or_create(pk = '1', defaults = { 'active':default_obj_active })

        if not default_obj_created and default_obj_active:
            default_obj.set_active()

        if not default_obj.logo:
            default_obj.set_default_logo()

        obj = objs_active_qs.last()
        objs_active_count = objs_active_qs.count()

        if objs_active_count > 1:
            obj.set_active()

        return obj


    name = models.CharField( max_length = 50, default = 'Django' )
    active = models.BooleanField( default = True )

    title = models.CharField( max_length = 50, default = 'Django administration', blank = True )
    title_visible = models.BooleanField( default = True, verbose_name = 'visible' )

    logo = models.FileField( upload_to = 'admin-interface/logo/', blank = True )
    logo_visible = models.BooleanField( default = True, verbose_name = 'visible' )

    css_header_background_color = ColorField( blank = True, default = '#0C4B33', help_text = '#0C4B33', verbose_name = 'background color' )
    css_header_title_color = ColorField( blank = True, default = '#F5DD5D', help_text = '#F5DD5D', verbose_name = 'title color' )
    css_header_text_color = ColorField( blank = True, default = '#44B78B', help_text = '#44B78B', verbose_name = 'text color' )
    css_header_link_color = ColorField( blank = True, default = '#FFFFFF', help_text = '#FFFFFF', verbose_name = 'link color' )
    css_header_link_hover_color = ColorField( blank = True, default = '#C9F0DD', help_text = '#C9F0DD', verbose_name = 'link hover color' )

    css_module_background_color = ColorField( blank = True, default = '#44B78B', help_text = '#44B78B', verbose_name = 'background color' )
    css_module_text_color = ColorField( blank = True, default = '#FFFFFF', help_text = '#FFFFFF', verbose_name = 'text color' )
    css_module_link_color = ColorField( blank = True, default = '#FFFFFF', help_text = '#FFFFFF', verbose_name = 'link color' )
    css_module_link_hover_color = ColorField( blank = True, default = '#C9F0DD', help_text = '#C9F0DD', verbose_name = 'link hover color' )
    css_module_rounded_corners = models.BooleanField( default = True, verbose_name = 'rounded corners' )

    css_generic_link_color = ColorField( blank = True, default = '#0C3C26', help_text = '#0C3C26', verbose_name = 'link color' )
    css_generic_link_hover_color = ColorField( blank = True, default = '#156641', help_text = '#156641', verbose_name = 'link hover color' )

    css_save_button_background_color = ColorField( blank = True, default = '#0C4B33', help_text = '#0C4B33', verbose_name = 'background color' )
    css_save_button_background_hover_color = ColorField( blank = True, default = '#0C3C26', help_text = '#0C3C26', verbose_name = 'background hover color' )
    css_save_button_text_color = ColorField( blank = True, default = '#FFFFFF', help_text = '#FFFFFF', verbose_name = 'text color' )

    css_delete_button_background_color = ColorField( blank = True, default = '#BA2121', help_text = '#BA2121', verbose_name = 'background color' )
    css_delete_button_background_hover_color = ColorField( blank = True, default = '#A41515', help_text = '#A41515', verbose_name = 'background hover color' )
    css_delete_button_text_color = ColorField( blank = True, default = '#FFFFFF', help_text = '#FFFFFF', verbose_name = 'text color' )

    css = models.TextField( blank = True )

    related_modal_active = models.BooleanField( default = True, verbose_name = 'active' )
    related_modal_background_color = ColorField( blank = True, default = '#000000', help_text = '#000000', verbose_name = 'background color' )
    related_modal_background_opacity_choices = (
        (0.1, '10%', ),
        (0.2, '20%', ),
        (0.3, '30%', ),
        (0.4, '40%', ),
        (0.5, '50%', ),
        (0.6, '60%', ),
        (0.7, '70%', ),
        (0.8, '80%', ),
        (0.9, '90%', ),
    )
    related_modal_background_opacity = models.FloatField( choices = related_modal_background_opacity_choices, default = 0.2, help_text = '20%', verbose_name = 'background opacity' )
    related_modal_rounded_corners = models.BooleanField( default = True, verbose_name = 'rounded corners' )

    list_filter_dropdown = models.BooleanField( default = False, verbose_name = 'use dropdown'  )

    def set_active(self):

        Theme.objects.exclude( pk = self.pk ).update( active = False )

        if not self.active:
            self.active = True
            self.save()

    def set_default_logo(self):

        logo_filename = 'logo-django.svg'
        logo_path = os.path.normpath(os.path.dirname(__file__) + '/data/' + logo_filename)
        logo_file = open(logo_path)

        self.logo = File(logo_file, logo_filename)
        self.save()

        logo_file.close()

    class Meta:

        app_label = 'admin_interface'

        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'

    def __unicode__(self):

        return unicode(u'%s' % (self.name, ))


post_delete.connect(Theme.post_delete_handler, sender = Theme)
post_save.connect(Theme.post_save_handler, sender = Theme)

