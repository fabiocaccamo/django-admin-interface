# -*- coding: utf-8 -*-

import django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def check_installed_app(app, app_dj_version_limit):
    dj_version = django.VERSION
    installed_apps = settings.INSTALLED_APPS
    if dj_version < app_dj_version_limit:
        if app not in installed_apps:
            raise ImproperlyConfigured(
                '\'{}\' needed before django {}.{}, '
                'add it to settings.INSTALLED_APPS.'.format(
                    app, *app_dj_version_limit))
    else:
        if app in installed_apps:
            raise ImproperlyConfigured(
                '\'{}\' not needed since django {}.{}, '
                'remove it from settings.INSTALLED_APPS.'.format(
                    app, *app_dj_version_limit))


def check_installed_apps():
    check_installed_app('colorfield', (4, 0))
    check_installed_app('flat', (1, 9))
    check_installed_app('flat_responsive', (2, 0))
