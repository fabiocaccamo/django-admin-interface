# -*- coding: utf-8 -*-

from django.contrib import admin

from admin_interface.models import Theme


class ThemeAdmin(admin.ModelAdmin):

    list_display = ('name', 'active', )
    list_editable = ('active', )

    fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('name', 'active', )
        }),
        ('Logo', {
            'classes': ('wide', ),
            'fields': ('logo', 'logo_visible', )
        }),
        ('Title', {
            'classes': ('wide', ),
            'fields': ('title', 'title_visible', )
        }),
        ('Header', {
            'classes': ('wide', ),
            'fields': ('css_header_background_color', 'css_header_title_color', 'css_header_text_color', 'css_header_link_color', 'css_header_link_hover_color', )
        }),
        ('Breadcrumbs / Module headers', {
            'classes': ('wide', ),
            'fields': ('css_module_background_color', 'css_module_text_color', 'css_module_link_color', 'css_module_link_hover_color', 'css_module_rounded_corners', )
        }),
        ('Generic Links', {
            'classes': ('wide', ),
            'fields': ('css_generic_link_color', 'css_generic_link_hover_color', )
        }),
        ('Save Buttons', {
            'classes': ('wide', ),
            'fields': ('css_save_button_background_color', 'css_save_button_background_hover_color', 'css_save_button_text_color', )
        }),
        ('Delete Buttons', {
            'classes': ('wide', ),
            'fields': ('css_delete_button_background_color', 'css_delete_button_background_hover_color', 'css_delete_button_text_color', )
        }),
        ('Extras', {
            'classes': ('wide', ),
            'fields': ('list_filter_dropdown', )
        }),
    )

    save_on_top = True

admin.site.register(Theme, ThemeAdmin)

