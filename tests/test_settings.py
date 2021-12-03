# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.test import override_settings, TestCase

from admin_interface.settings import check_installed_apps


class AdminInterfaceSettingsTestCase(TestCase):

    DJANGO_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.messages',
        'django.contrib.sessions',
    ]

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __test_installed_apps(self):
        dj_version = django.VERSION
        installed_apps = settings.INSTALLED_APPS

        if 'colorfield' not in installed_apps:
            self.assertRaises(ImproperlyConfigured, check_installed_apps)

        elif 'flat' not in installed_apps and dj_version < (1, 9):
            self.assertRaises(ImproperlyConfigured, check_installed_apps)

        elif 'flat' in installed_apps and dj_version >= (1, 9):
            self.assertRaises(ImproperlyConfigured, check_installed_apps)

        elif 'flat_responsive' not in installed_apps and dj_version < (2, 0):
            self.assertRaises(ImproperlyConfigured, check_installed_apps)

        elif 'flat_responsive' in installed_apps and dj_version >= (2, 0):
            self.assertRaises(ImproperlyConfigured, check_installed_apps)

        else:
            check_installed_apps()

    @override_settings(
        INSTALLED_APPS = [
            'admin_interface',
            'colorfield',
            'flat',
            'flat_responsive',
        ] + DJANGO_APPS
    )
    def test_installed_apps_all(self):
        self.__test_installed_apps()

    @override_settings(
        INSTALLED_APPS = [
            'admin_interface',
            # 'colorfield',
            'flat',
            'flat_responsive',
        ] + DJANGO_APPS
    )
    def test_installed_apps_no_colorfield(self):
        self.__test_installed_apps()

    @override_settings(
        INSTALLED_APPS = [
            'admin_interface',
            'colorfield',
            # 'flat',
            'flat_responsive',
        ] + DJANGO_APPS
    )
    def test_installed_apps_no_flat(self):
        self.__test_installed_apps()

    @override_settings(
        INSTALLED_APPS = [
            'admin_interface',
            'colorfield',
            'flat',
            # 'flat_responsive',
        ] + DJANGO_APPS
    )
    def test_installed_apps_no_flat_responsive(self):
        self.__test_installed_apps()

