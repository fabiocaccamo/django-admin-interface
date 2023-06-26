from datetime import date
from unittest.mock import Mock

from django.contrib.admin.views.main import ChangeList
from django.template import Context, Template
from django.test import TestCase, override_settings
from django.test.client import RequestFactory

from admin_interface.metadata import __version__
from admin_interface.models import Theme
from admin_interface.templatetags import admin_interface_tags as templatetags
from admin_interface.templatetags.admin_interface_tags import hash_string


class AdminInterfaceTemplateTagsTestCase(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def tearDown(self):
        pass

    def __render_template(self, string, context=None):
        return Template(string).render(Context(context or {}))

    def test_get_admin_interface_languages(self):
        context = Context({"request": self.request_factory.get("/en/admin/")})
        languages = templatetags.get_admin_interface_languages(context)
        expected_languages = [
            {
                "code": "de",
                "name": "Deutsch",
                "default": False,
                "active": False,
                "activation_url": "/i18n/setlang/?next=/de/admin/",
            },
            {
                "code": "en",
                "name": "English",
                "default": True,
                "active": True,
                "activation_url": "/i18n/setlang/?next=/en/admin/",
            },
            {
                "code": "es",
                "name": "Español",
                "default": False,
                "active": False,
                "activation_url": "/i18n/setlang/?next=/es/admin/",
            },
            {
                "code": "fa",
                "name": "Farsi",
                "default": False,
                "active": False,
                "activation_url": "/i18n/setlang/?next=/fa/admin/",
            },
            {
                "code": "fr",
                "name": "Français",
                "default": False,
                "active": False,
                "activation_url": "/i18n/setlang/?next=/fr/admin/",
            },
            {
                "code": "it",
                "name": "Italiano",
                "default": False,
                "active": False,
                "activation_url": "/i18n/setlang/?next=/it/admin/",
            },
            {
                "code": "pl",
                "name": "Polski",
                "default": False,
                "active": False,
                "activation_url": "/i18n/setlang/?next=/pl/admin/",
            },
            {
                "code": "pt-BR",
                "name": "Português",
                "default": False,
                "active": False,
                "activation_url": "/i18n/setlang/?next=/pt-br/admin/",
            },
            {
                "code": "ru",
                "name": "Русский",
                "default": False,
                "active": False,
                "activation_url": "/i18n/setlang/?next=/ru/admin/",
            },
            {
                "code": "tr",
                "name": "Türk",
                "default": False,
                "active": False,
                "activation_url": "/i18n/setlang/?next=/tr/admin/",
            },
        ]
        self.assertEqual(len(languages), len(expected_languages))
        self.assertEqual(languages[0], expected_languages[0])
        self.assertEqual(languages[1], expected_languages[1])

    @override_settings(
        USE_I18N=False,
    )
    def test_get_admin_interface_languages_with_i18n_disabled(self):
        context = Context({"request": self.request_factory.get("/en/admin/")})
        languages = templatetags.get_admin_interface_languages(context)
        self.assertEqual(languages, None)

    @override_settings(
        ROOT_URLCONF="tests.urls_without_i18n_patterns",
    )
    def test_get_admin_interface_languages_without_i18n_url_patterns(self):
        context = Context({"request": self.request_factory.get("/en/admin/")})
        languages = templatetags.get_admin_interface_languages(context)
        self.assertEqual(languages, None)

    @override_settings(
        LANGUAGES=(("en", "English"),),
    )
    def test_get_admin_interface_languages_without_multiple_languages(self):
        context = Context({"request": self.request_factory.get("/en/admin/")})
        languages = templatetags.get_admin_interface_languages(context)
        self.assertEqual(languages, None)

    def test_get_admin_interface_languages_without_request(self):
        context = Context({})
        languages = templatetags.get_admin_interface_languages(context)
        self.assertEqual(languages, None)

    def test_get_admin_interface_languages_without_language_prefix_in_url(self):
        context = Context({"request": self.request_factory.get("/admin/")})
        languages = templatetags.get_admin_interface_languages(context)
        self.assertEqual(languages, None)

    def test_get_theme(self):
        Theme.objects.all().delete()
        context = Context({})
        theme = templatetags.get_admin_interface_theme()
        self.assertEqual(theme.name, "Django")
        rendered = self.__render_template(
            "{% load admin_interface_tags %}"
            "{% get_admin_interface_theme as theme %}"
            "{{ theme.name }}",
            context,
        )
        self.assertEqual(rendered, "Django")

    def test_get_setting(self):
        title = templatetags.get_admin_interface_setting("title")
        self.assertEqual(title, "Django administration")

    def test_get_version(self):
        version = templatetags.get_admin_interface_version()
        self.assertEqual(version, __version__)
        rendered = self.__render_template(
            "{% load admin_interface_tags %}"
            "{% get_admin_interface_version as version %}"
            "{{ version }}"
        )
        self.assertEqual(rendered, __version__)

    def test_get_version_nocache(self):
        hash_from_tag = templatetags.get_admin_interface_nocache()
        hash_manual = hash_string(__version__)
        self.assertEqual(hash_from_tag, hash_manual)

        rendered = self.__render_template(
            "{% load admin_interface_tags %}"
            "{% get_admin_interface_nocache as version_md5_hash %}"
            "{{ version_md5_hash }}"
        )
        self.assertEqual(rendered, hash_manual)

    def test_get_admin_interface_inline_template(self):
        headless_template = templatetags.get_admin_interface_inline_template(
            "admin/edit_inline/stacked.html"
        )
        self.assertEqual(headless_template, "admin/edit_inline/headerless_stacked.html")

    def test_get_active_date_hierarchy_none(self):
        changelist = Mock()
        changelist.date_hierarchy = None

        date_field = templatetags.get_admin_interface_active_date_hierarchy(changelist)

        self.assertIsNone(date_field)

    def test_get_active_date_hierarchy_inactive(self):
        changelist = Mock()
        changelist.date_hierarchy = "last_login"
        changelist.get_filters_params.return_value = {}

        date_field = templatetags.get_admin_interface_active_date_hierarchy(changelist)

        self.assertIsNone(date_field)

    def test_get_active_date_hierarchy_active(self):
        changelist = Mock()
        changelist.date_hierarchy = "last_login"
        params = {"some_field": 2, "last_login__year": 2022}
        changelist.get_filters_params.return_value = params

        date_field = templatetags.get_admin_interface_active_date_hierarchy(changelist)

        self.assertEqual(date_field, "last_login")

    def _add_changelist_methods(self, mock, params):
        def get_query_string(**kwargs):
            return ChangeList.get_query_string(mock, **kwargs)

        def get_filters_params(**kwargs):
            return ChangeList.get_filters_params(mock, **kwargs)

        mock.get_query_string = get_query_string
        mock.get_filters_params = get_filters_params
        mock.params = params

    def test_filter_removal_link(self):
        changelist = Mock()
        params = {"shape": "pointy", "size": "small"}
        self._add_changelist_methods(changelist, params)
        list_filter = Mock()
        list_filter.title = "Shape filter"
        choices = [{"display": "Round"}, {"display": "Pointy", "selected": True}]
        list_filter.choices.return_value = choices
        list_filter.expected_parameters.return_value = ("shape",)

        ctx = templatetags.admin_interface_filter_removal_link(changelist, list_filter)

        self.assertEqual(ctx["removal_link"], "?size=small")
        self.assertEqual(ctx["title"], "Shape filter")
        self.assertEqual(ctx["selected_value"], "Pointy")

    def test_filter_removal_link_no_display(self):
        changelist = Mock()
        params = {"shape": "pointy", "size": "small"}
        self._add_changelist_methods(changelist, params)
        list_filter = Mock()
        list_filter.title = "Shape filter"
        choices = [{"other": "Round"}, {"other": "Pointy", "selected": True}]
        list_filter.choices.return_value = choices
        list_filter.expected_parameters.return_value = ("shape",)

        ctx = templatetags.admin_interface_filter_removal_link(changelist, list_filter)

        self.assertEqual(ctx["removal_link"], "?size=small")
        self.assertEqual(ctx["title"], "Shape filter")
        self.assertEqual(ctx["selected_value"], "...")

    def test_date_hierarchy_removal_link_year(self):
        changelist = Mock()
        params = {"shape": "pointy", "last_login__year": 2022}
        self._add_changelist_methods(changelist, params)
        changelist.model._meta.get_field.return_value.verbose_name = "last login"

        ctx = templatetags.admin_interface_date_hierarchy_removal_link(
            changelist, "last_login"
        )

        self.assertEqual(ctx["removal_link"], "?shape=pointy")
        self.assertEqual(ctx["date_label"], "last login")
        self.assertEqual(ctx["date_value"], date(2022, 1, 1))

    def test_date_hierarchy_removal_link_year_month(self):
        changelist = Mock()
        changelist.model._meta.get_field.return_value.verbose_name = "last login"
        params = {"last_login__year": 2022, "last_login__month": "11"}
        self._add_changelist_methods(changelist, params)

        ctx = templatetags.admin_interface_date_hierarchy_removal_link(
            changelist, "last_login"
        )

        self.assertEqual(ctx["removal_link"], "?")
        self.assertEqual(ctx["date_label"], "last login")
        self.assertEqual(ctx["date_value"], date(2022, 11, 1))

    def test_date_hierarchy_removal_link_year_month_day(self):
        changelist = Mock()
        changelist.model._meta.get_field.return_value.verbose_name = "last login"
        params = {
            "last_login__year": 2022,
            "last_login__month": "11",
            "last_login__day": "30",
            "shape": "round",
            "size": "small",
        }
        self._add_changelist_methods(changelist, params)

        ctx = templatetags.admin_interface_date_hierarchy_removal_link(
            changelist, "last_login"
        )

        self.assertEqual(ctx["removal_link"], "?shape=round&size=small")
        self.assertEqual(ctx["date_label"], "last login")
        self.assertEqual(ctx["date_value"], date(2022, 11, 30))
