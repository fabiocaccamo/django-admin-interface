# -*- coding: utf-8 -*-

import django

if django.VERSION >= (1, 11):
    from django.core.validators import FileExtensionValidator
else:

    def FileExtensionValidator(*args, **kwargs):
        def noop(*args, **kwargs):
            pass

        return noop


if django.VERSION < (1, 10):
    from django.core.urlresolvers import NoReverseMatch, reverse
else:
    from django.urls import NoReverseMatch, reverse

if django.VERSION < (2, 0):
    from django.utils.encoding import force_text as force_str
    from django.utils.translation import ugettext_lazy as gettext_lazy
else:
    from django.utils.encoding import force_str
    from django.utils.translation import gettext_lazy
