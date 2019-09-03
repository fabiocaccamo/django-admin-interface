# -*- coding: utf-8 -*-

import django
from django import template, VERSION
from django.conf import settings
if django.VERSION < (1, 10):
    from django.core.urlresolvers import reverse
else:
    from django.urls import reverse
from django.utils import translation

from admin_interface.cache import get_cached_active_theme, set_cached_active_theme
from admin_interface.models import Theme
from admin_interface.version import __version__

import re


register = template.Library()

if VERSION < (1, 9):
    simple_tag = register.assignment_tag
else:
    simple_tag = register.simple_tag


@register.inclusion_tag('admin_interface/language_chooser.html', takes_context=True)
def get_admin_interface_language_chooser(context):
    langs_data = []
    if settings.USE_I18N and len(settings.LANGUAGES) > 1:
        request = context.get('request')
        full_path = request.get_full_path()
        default_lang_code = settings.LANGUAGE_CODE
        current_lang_code = translation.get_language() or default_lang_code
        for language in settings.LANGUAGES:
            lang_code = language[0].lower()
            lang_name = language[1].title()
            lang_data = {
                'code': lang_code,
                'name': lang_name,
                'default': bool(lang_code == default_lang_code),
                'active': bool(lang_code == current_lang_code),
            }
            with translation.override(lang_code):
                lang_set_url = '{}?language={}'.format(
                    reverse('set_language'), lang_code)
                lang_next_url = re.sub(
                    r'^\/[\w\-\_]+', '/{}'.format(lang_code), full_path)
                lang_activation_url = '{}&next={}'.format(
                    lang_set_url, lang_next_url)
                lang_data['activation_url'] = lang_activation_url
            langs_data.append(lang_data)
    return { 'languages':langs_data }


@simple_tag(takes_context=True)
def get_admin_interface_theme(context):
    theme = get_cached_active_theme()
    if not theme:
        theme = Theme.get_active_theme()
        set_cached_active_theme(theme)
    return theme


@simple_tag(takes_context=False)
def get_admin_interface_version():
    return __version__
