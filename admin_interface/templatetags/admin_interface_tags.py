# -*- coding: utf-8 -*-

from django import template

from admin_interface.models import Theme


register = template.Library()


@register.assignment_tag(takes_context = True)
def get_admin_interface_theme(context):

    obj_qs = Theme.objects.filter(active = True)[:1]
    obj_ls = list(obj_qs)
    obj = None

    if len(obj_ls):
        obj = obj_ls[0]
    else:
        obj = Theme.get_or_create_default_theme()

    return obj

