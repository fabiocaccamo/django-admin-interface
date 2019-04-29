# -*- coding: utf-8 -*-

from django import template, VERSION

from admin_interface.cache import get_cached_active_theme, set_cached_active_theme
from admin_interface.models import Theme
from admin_interface.version import __version__

register = template.Library()

if VERSION < (1, 9):
    simple_tag = register.assignment_tag
else:
    simple_tag = register.simple_tag


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
