import datetime
import hashlib
import re
import warnings

from django import template
from django.conf import settings
from django.contrib.admin.utils import get_fields_from_path
from django.urls import NoReverseMatch, reverse
from django.utils import translation
from slugify import slugify

from admin_interface.cache import get_cached_active_theme, set_cached_active_theme
from admin_interface.metadata import __version__
from admin_interface.models import Theme

register = template.Library()


@register.inclusion_tag("admin_interface/language_chooser.html", takes_context=True)
def admin_interface_language_chooser(context):
    if not settings.USE_I18N:
        # i18n disabled
        return None
    if len(settings.LANGUAGES) < 2:
        # less than 2 languages
        return None
    if "django.middleware.locale.LocaleMiddleware" not in settings.MIDDLEWARE:
        warnings.warn(
            "Language chooser requires 'django.middleware.locale.LocaleMiddleware' "
            "in your MIDDLEWARE to work.",
            stacklevel=1,
        )
        return None
    try:
        context["set_language_url"] = reverse("set_language")
    except NoReverseMatch:
        warnings.warn(
            "Language chooser requires Django's `set_language` view: "
            "`urlpatterns += [url(r'^i18n/', include('django.conf.urls.i18n'))]`.",
            stacklevel=1,
        )
        return None
    request = context.get("request", None)
    if not request:
        return None
    context["LANGUAGES"] = settings.LANGUAGES

    full_path = request.get_full_path()
    admin_nolang_url = re.sub(r"^\/([\w]{2})([\-\_]{1}[\w]{2,4})?\/", "/", full_path)

    default_lang_code = settings.LANGUAGE_CODE
    current_lang_code = translation.get_language() or default_lang_code
    context["LANGUAGE_CODE"] = current_lang_code
    context["next"] = admin_nolang_url
    return context


@register.simple_tag()
def get_admin_interface_theme():
    theme = get_cached_active_theme()
    if not theme:
        theme = Theme.objects.get_active()
        set_cached_active_theme(theme)
    return theme


@register.simple_tag()
def get_admin_interface_setting(setting):
    theme = get_admin_interface_theme()
    return getattr(theme, setting)


@register.simple_tag()
def get_admin_interface_inline_template(template):
    template_path = template.split("/")
    if template_path[0] != "admin":
        # return costume inline template for other packages
        return template
    template_path[-1] = "headerless_" + template_path[-1]
    return "/".join(template_path)


@register.simple_tag()
def get_admin_interface_version():
    return __version__


def hash_string(text):
    hash_object = hashlib.sha224(text.encode())
    sha224_hash = hash_object.hexdigest()
    return sha224_hash


@register.simple_tag()
def get_admin_interface_nocache():
    return hash_string(__version__)


@register.simple_tag(takes_context=False)
def get_admin_interface_active_date_hierarchy(changelist):
    date_field_name = changelist.date_hierarchy
    if not date_field_name:
        return

    params = changelist.get_filters_params()
    # link to clear all filters contains f'{date_field_name}__gte',
    # only filters with specific year are really active
    if f"{date_field_name}__year" not in params:
        return

    return date_field_name


@register.inclusion_tag("admin_interface/list_filter_removal_link.html")
def admin_interface_filter_removal_link(changelist, list_filter):
    title = list_filter.title
    choices = [
        choice for choice in list_filter.choices(changelist) if choice.get("selected")
    ]
    try:
        value = choices[0]["display"]
    except (IndexError, KeyError):
        value = "..."

    removal_link = changelist.get_query_string(remove=list_filter.expected_parameters())

    return {
        "cl": changelist,
        "spec": list_filter,
        "selected_value": value,
        "title": title,
        "removal_link": removal_link,
    }


@register.inclusion_tag("admin_interface/date_hierarchy_removal_link.html")
def admin_interface_date_hierarchy_removal_link(changelist, date_field_name):
    date_field_path = get_fields_from_path(changelist.model, date_field_name)
    # date_field = date_field_path[-1]
    date_labels = [str(field.verbose_name) for field in date_field_path]
    date_label = " ".join(date_labels).lower()

    params = changelist.get_filters_params()
    date_params = [param for param in params if param.startswith(date_field_name)]

    date_args = [datetime.datetime.now().year, 1, 1]
    date_format = "Y"
    date_filters = (
        ("year", "Y"),
        ("month", "YEAR_MONTH_FORMAT"),
        ("day", "DATE_FORMAT"),
    )
    for index, date_filter in enumerate(date_filters):
        date_filter_key, date_filter_format = date_filter
        date_filter_param = f"{date_field_name}__{date_filter_key}"
        if date_filter_param in params:
            param = params[date_filter_param]
            date_args[index] = (
                int(param[0]) if isinstance(param, (list, tuple)) else int(param)
            )
            date_format = date_filter_format
            continue
        break
    date_value = datetime.date(*date_args)

    removal_link = changelist.get_query_string(remove=date_params)

    return {
        "cl": changelist,
        "date_label": date_label,
        "date_value": date_value,
        "date_format": date_format,
        "removal_link": removal_link,
    }


@register.simple_tag()
def admin_interface_use_changeform_tabs(adminform, inline_forms):
    theme = get_admin_interface_theme()
    has_fieldset_tabs = (
        theme.show_fieldsets_as_tabs and adminform and len(adminform.fieldsets) > 1
    )
    has_inline_tabs = (
        theme.show_inlines_as_tabs and inline_forms and len(inline_forms) > 0
    )
    has_tabs = has_fieldset_tabs or has_inline_tabs
    return has_tabs


@register.filter
def admin_interface_slugify(name):
    return slugify(str(name or ""))
