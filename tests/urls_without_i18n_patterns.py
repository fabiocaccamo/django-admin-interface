# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django
from django.contrib import admin
if django.VERSION < (2, 0):
    from django.conf.urls import url as re_path
else:
    from django.urls import re_path


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
]
