# -*- coding: utf-8 -*-

import django
import hashlib
import re

from django import template
from django.conf import settings
from django.utils import translation

from admin_interface.cache import get_cached_active_theme, set_cached_active_theme
from admin_interface.compat import NoReverseMatch, reverse
from admin_interface.models import Theme
from admin_interface.version import __version__


register = template.Library()

if django.VERSION < (1, 9):
    simple_tag = register.assignment_tag
else:
    simple_tag = register.simple_tag


@simple_tag(takes_context=True)
def get_admin_interface_languages(context):
    if not settings.USE_I18N:
        # i18n disabled
        return None
    if len(settings.LANGUAGES) < 2:
        # less than 2 languages
        return None
    try:
        set_language_url = reverse("set_language")
    except NoReverseMatch:
        # ImproperlyConfigured - must include i18n urls:
        # urlpatterns += [url(r'^i18n/', include('django.conf.urls.i18n')),]
        return None
    request = context.get("request", None)
    if not request:
        return None
    full_path = request.get_full_path()
    admin_nolang_url = re.sub(r"^\/([\w]{2})([\-\_]{1}[\w]{2,4})?\/", "/", full_path)
    if admin_nolang_url == full_path:
        # ImproperlyConfigured - must include admin urls using i18n_patterns:
        # from django.conf.urls.i18n import i18n_patterns
        # urlpatterns += i18n_patterns(url(r'^admin/', admin.site.urls))
        return None
    langs_data = []
    default_lang_code = settings.LANGUAGE_CODE
    current_lang_code = translation.get_language() or default_lang_code
    for language in settings.LANGUAGES:
        lang_code = language[0].lower()
        lang_name = language[1].title()
        lang_data = {
            "code": lang_code,
            "name": lang_name,
            "default": lang_code == default_lang_code,
            "active": lang_code == current_lang_code,
            "activation_url": "{}?next=/{}{}".format(
                set_language_url, lang_code, admin_nolang_url
            ),
        }
        langs_data.append(lang_data)
    return langs_data


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


def hash_string(text):
    hash_object = hashlib.sha224(text.encode())
    sha224_hash = hash_object.hexdigest()
    return sha224_hash


@simple_tag(takes_context=False)
def get_admin_interface_nocache():
    return hash_string(__version__)
