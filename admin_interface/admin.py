# -*- coding: utf-8 -*-

from admin_interface.models import Theme

import django
from django.contrib import admin
if django.VERSION < (2, 0):
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _


class ThemeAdmin(admin.ModelAdmin):

    list_display = ('name', 'active', )
    list_editable = ('active', )
    list_per_page = 100
    show_full_result_count = False

    fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('name', 'active', )
        }),
        (_('Environment'), {
            'classes': ('wide', ),
            'fields': (
                'env_name',
                'env_color',
                'env_visible_in_header',
                'env_visible_in_favicon',
            )
        }),
        (_('Language chooser'), {
            'classes': ('wide', ),
            'fields': (
                'language_chooser_active',
                'language_chooser_display',
            )
        }),
        (_('Logo'), {
            'classes': ('wide', ),
            'fields': (
                'logo',
                'logo_color',
                'logo_visible',
            )
        }),
        (_('Favicon'), {
            'classes': ('wide', ),
            'fields': ('favicon', )
        }),
        (_('Title'), {
            'classes': ('wide', ),
            'fields': (
                'title',
                'title_color',
                'title_visible',
            )
        }),
        (_('Header'), {
            'classes': ('wide', ),
            'fields': (
                'css_header_background_color',
                'css_header_text_color',
                'css_header_link_color',
                'css_header_link_hover_color',
            )
        }),
        (_('Breadcrumbs / Module headers'), {
            'classes': ('wide', ),
            'fields': (
                'css_module_background_color',
                'css_module_text_color',
                'css_module_link_color',
                'css_module_link_hover_color',
                'css_module_rounded_corners',
            )
        }),
        (_('Generic Links'), {
            'classes': ('wide', ),
            'fields': (
                'css_generic_link_color',
                'css_generic_link_hover_color',
            )
        }),
        (_('Save Buttons'), {
            'classes': ('wide', ),
            'fields': (
                'css_save_button_background_color',
                'css_save_button_background_hover_color',
                'css_save_button_text_color',
            )
        }),
        (_('Delete Buttons'), {
            'classes': ('wide', ),
            'fields': (
                'css_delete_button_background_color',
                'css_delete_button_background_hover_color',
                'css_delete_button_text_color',
            )
        }),
        (_('Related Modal'), {
            'classes': ('wide', ),
            'fields': (
                'related_modal_active',
                'related_modal_background_color',
                'related_modal_background_opacity',
                'related_modal_rounded_corners',
                'related_modal_close_button_visible',
            )
        }),
        (_('Form Controls'), {
            'classes': ('wide', ),
            'fields': (
                'form_submit_sticky',
                'form_pagination_sticky',
            )
        }),
        (_('List Filter'), {
            'classes': ('wide', ),
            'fields': (
                'list_filter_dropdown',
                'list_filter_sticky',
            )
        }),
        (_('Recent Actions'), {
            'classes': ('wide', ),
            'fields': ('recent_actions_visible', )
        }),
    )

    save_on_top = True


admin.site.register(Theme, ThemeAdmin)
