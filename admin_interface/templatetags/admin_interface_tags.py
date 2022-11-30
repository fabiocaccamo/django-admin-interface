# -*- coding: utf-8 -*-

import hashlib
import re

import django
from django import template
from django.conf import settings
from django.template.loader import get_template
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


@simple_tag()
def get_admin_interface_theme():
    theme = get_cached_active_theme()
    if not theme:
        theme = Theme.get_active_theme()
        set_cached_active_theme(theme)
    return theme


@simple_tag()
def get_admin_interface_setting(setting):
    theme = get_admin_interface_theme()
    return getattr(theme, setting)


@simple_tag()
def get_admin_interface_inline_template(template):
    template_path = template.split("/")
    template_path[-1] = "headerless_" + template_path[-1]
    return "/".join(template_path)


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


@simple_tag()
def admin_interface_clear_filter_qs(changelist, list_filter):
    return changelist.get_query_string(remove=list_filter.expected_parameters())


@simple_tag()
def admin_interface_filter_removal_link(changelist, list_filter):
    template = get_template("admin_interface/list_filter_removal_link.html")
    title = list_filter.title
    choices = [
        choice for choice in list_filter.choices(changelist) if choice.get("selected")
    ]
    try:
        value = choices[0]["display"]
    except (IndexError, KeyError):
        value = "..."

    return template.render(
        {
            "cl": changelist,
            "spec": list_filter,
            "selected_value": value,
            "title": title,
        }
    )


@simple_tag()
def admin_interface_use_changeform_tabs(adminform, inline_forms):
    theme = get_admin_interface_theme()
    has_fieldset_tabs = theme.show_fieldsets_as_tabs and len(adminform.fieldsets) > 1
    has_inline_tabs = theme.show_inlines_as_tabs and len(inline_forms) > 0
    has_tabs = has_fieldset_tabs or has_inline_tabs
    return has_tabs
