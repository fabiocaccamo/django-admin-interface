from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase, override_settings

from admin_interface.settings import check_installed_apps


class AdminInterfaceSettingsTestCase(TestCase):
    DJANGO_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.messages",
        "django.contrib.sessions",
    ]

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __test_installed_apps(self):
        installed_apps = settings.INSTALLED_APPS

        if "colorfield" not in installed_apps:
            self.assertRaises(ImproperlyConfigured, check_installed_apps)
        else:
            check_installed_apps()

    @override_settings(
        INSTALLED_APPS=[
            "admin_interface",
            "colorfield",
        ]
        + DJANGO_APPS
    )
    def test_installed_apps_all(self):
        self.__test_installed_apps()

    @override_settings(
        INSTALLED_APPS=[
            "admin_interface",
            # 'colorfield',
        ]
        + DJANGO_APPS
    )
    def test_installed_apps_no_colorfield(self):
        self.__test_installed_apps()
