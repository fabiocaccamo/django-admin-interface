import django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def check_installed_app(app, max_dj_version=None):
    dj_version = django.VERSION
    installed_apps = settings.INSTALLED_APPS
    if max_dj_version is None:
        if app not in installed_apps:
            raise ImproperlyConfigured(
                f"'{app}' is required, add it to settings.INSTALLED_APPS."
            )
    elif dj_version < max_dj_version:
        if app not in installed_apps:
            raise ImproperlyConfigured(
                "'{}' is required before django {}.{}, "
                "add it to settings.INSTALLED_APPS.".format(app, *max_dj_version)
            )
    else:
        if app in installed_apps:
            raise ImproperlyConfigured(
                "'{}' is no more required since django {}.{}, "
                "remove it from settings.INSTALLED_APPS.".format(app, *max_dj_version)
            )


def check_installed_apps():
    check_installed_app("colorfield")
