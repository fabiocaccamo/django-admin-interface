# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django
from django.contrib import admin
if django.VERSION < (2, 0):
    from django.conf.urls import include, url as re_path
else:
    from django.urls import include, re_path
from django.conf.urls.i18n import i18n_patterns


urlpatterns = []
urlpatterns += [
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    re_path(r'^admin/', admin.site.urls),
)
