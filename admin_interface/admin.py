# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from admin_interface.models import Theme


class ThemeAdmin(admin.ModelAdmin):

    list_display = ('name', 'active', )
    list_editable = ('active', )

    fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('name', 'active', )
        }),
        (_('Environment'), {
            'classes': ('wide', ),
            'fields': (
                'env',
                'env_visible',
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
            )
        }),
        (_('List Filter'), {
            'classes': ('wide', ),
            'fields': ('list_filter_dropdown', )
        }),
        (_('Recent Actions'), {
            'classes': ('wide', ),
            'fields': ('recent_actions_visible', )
        }),
    )

    save_on_top = True


admin.site.register(Theme, ThemeAdmin)
