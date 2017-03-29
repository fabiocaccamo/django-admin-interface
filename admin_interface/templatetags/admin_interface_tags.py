# -*- coding: utf-8 -*-

from django import template

from admin_interface.models import Theme


register = template.Library()


@register.assignment_tag(takes_context = True)
def get_admin_interface_theme(context):

    return Theme.get_active_theme()

