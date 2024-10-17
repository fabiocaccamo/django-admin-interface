from datetime import date
from unittest.mock import Mock

from django.conf import settings
from django.contrib.admin.views.main import ChangeList
from django.template import Context, Template
from django.test import TestCase, override_settings
from django.test.client import RequestFactory

from admin_interface.models import Theme
from admin_interface.templatetags import admin_interface_tags as templatetags


class AdminInterfaceTemplateTagsTestCase(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def tearDown(self):
        pass

    def __render_template(self, string, context=None):
        return Template(string).render(Context(context or {}))

    def test_admin_interface_language_chooser(self):
        context = Context({"request": self.request_factory.get("/en/admin/")})
        context = templatetags.admin_interface_language_chooser(context)
        languages = context["LANGUAGES"]
        expected_languages = [
            ("de", "Deutsch"),
            ("en", "English"),
            ("es", "Español"),
            ("fa", "Farsi"),
            ("fr", "Français"),
            ("it", "Italiano"),
            ("pl", "Polski"),
            ("pt-BR", "Português"),
            ("ru", "Русский"),
            ("tr", "Türk"),
        ]
        self.assertEqual(len(languages), len(expected_languages))
        self.assertEqual(languages[0], expected_languages[0])
        self.assertEqual(languages[1], expected_languages[1])
        self.assertEqual(context["next"], "/admin/")

    @override_settings(
        USE_I18N=False,
    )
    def test_admin_interface_language_chooser_with_i18n_disabled(self):
        context = Context({"request": self.request_factory.get("/en/admin/")})
        tag_context = templatetags.admin_interface_language_chooser(context)
        self.assertEqual(tag_context, None)

    @override_settings(
        ROOT_URLCONF="tests.urls_without_i18n_patterns",
    )
    def test_admin_interface_language_chooser_without_i18n_url_patterns(self):
        context = Context({"request": self.request_factory.get("/en/admin/")})
        with self.assertWarnsMessage(UserWarning, "django.conf.urls.i18n"):
            tag_context = templatetags.admin_interface_language_chooser(context)
        self.assertEqual(tag_context, None)

    @override_settings(
        MIDDLEWARE=[],
    )
    def test_admin_interface_language_chooser_without_locale_middleware(self):
        context = Context({"request": self.request_factory.get("/en/admin/")})
        with self.assertWarnsMessage(UserWarning, "LocaleMiddleware"):
            tag_context = templatetags.admin_interface_language_chooser(context)
        self.assertEqual(tag_context, None)

    @override_settings(
        LANGUAGES=(("en", "English"),),
    )
    def test_admin_interface_language_chooser_without_multiple_languages(self):
        context = Context({"request": self.request_factory.get("/en/admin/")})
        tag_context = templatetags.admin_interface_language_chooser(context)
        self.assertEqual(tag_context, None)

    def test_admin_interface_language_chooser_without_request(self):
        context = Context({})
        tag_context = templatetags.admin_interface_language_chooser(context)
        self.assertEqual(tag_context, None)

    def test_admin_interface_language_chooser_without_language_prefix_in_url(self):
        context = Context({"request": self.request_factory.get("/admin/")})
        tag_context = templatetags.admin_interface_language_chooser(context)
        self.assertEqual(tag_context["next"], "/admin/")

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

    def test_get_static(self):
        path = "admin_interface/css/admin-interface.css"
        rendered = self.__render_template(
            "{% load admin_interface_tags %}"
            f"{{% get_admin_interface_static '{path}' %}}"
        )
        self.assertTrue(rendered.startswith(f"{settings.STATIC_URL}{path}?v="))

    @override_settings(
        STATIC_URL="https://bucket.s3.amazonaws.com/static/",
    )
    def test_get_static_with_s3_url(self):
        path = "admin_interface/css/admin-interface.css"
        rendered = self.__render_template(
            "{% load admin_interface_tags %}"
            f"{{% get_admin_interface_static '{path}' %}}"
        )
        self.assertEqual(rendered, f"{settings.STATIC_URL}{path}")

    def test_get_admin_interface_inline_template(self):
        headless_template = templatetags.get_admin_interface_inline_template(
            "admin/edit_inline/stacked.html"
        )
        self.assertEqual(headless_template, "admin/edit_inline/headerless_stacked.html")
        headless_template = templatetags.get_admin_interface_inline_template(
            "nesting/admin/inlines/tabular.html"
        )
        self.assertEqual(headless_template, "nesting/admin/inlines/tabular.html")

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

    def _get_changelist_mock(self, params=None):
        class ChangelistMock(Mock):
            def __init__(self, params=None, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # django < 5.0
                self.params = params or {}
                # django >= 5.0
                self.filter_params = params or {}

            def get_query_string(self, **kwargs):
                return ChangeList.get_query_string(self, **kwargs)

            def get_filters_params(self, **kwargs):
                return ChangeList.get_filters_params(self, **kwargs)

        return ChangelistMock(params=params)

    def test_filter_removal_link(self):
        params = {"shape": "pointy", "size": "small"}
        changelist = self._get_changelist_mock(params)
        list_filter = Mock()
        list_filter.title = "Shape filter"
        choices = [{"display": "Round"}, {"display": "Pointy", "selected": True}]
        list_filter.choices.return_value = choices
        list_filter.expected_parameters.return_value = ("shape",)

        context = templatetags.admin_interface_filter_removal_link(
            changelist, list_filter
        )

        self.assertEqual(context["removal_link"], "?size=small")
        self.assertEqual(context["title"], "Shape filter")
        self.assertEqual(context["selected_value"], "Pointy")

    def test_filter_removal_link_no_display(self):
        params = {"shape": "pointy", "size": "small"}
        changelist = self._get_changelist_mock(params)
        list_filter = Mock()
        list_filter.title = "Shape filter"
        choices = [{"other": "Round"}, {"other": "Pointy", "selected": True}]
        list_filter.choices.return_value = choices
        list_filter.expected_parameters.return_value = ("shape",)

        context = templatetags.admin_interface_filter_removal_link(
            changelist, list_filter
        )

        self.assertEqual(context["removal_link"], "?size=small")
        self.assertEqual(context["title"], "Shape filter")
        self.assertEqual(context["selected_value"], "...")

    def test_date_hierarchy_removal_link_year(self):
        params = {"shape": "pointy", "last_login__year": 2022}
        changelist = self._get_changelist_mock(params)
        changelist.model._meta.get_field.return_value.verbose_name = "last login"

        context = templatetags.admin_interface_date_hierarchy_removal_link(
            changelist, "last_login"
        )

        self.assertEqual(context["removal_link"], "?shape=pointy")
        self.assertEqual(context["date_label"], "last login")
        self.assertEqual(context["date_value"], date(2022, 1, 1))

    def test_date_hierarchy_removal_link_year_month(self):
        params = {"last_login__year": 2022, "last_login__month": "11"}
        changelist = self._get_changelist_mock(params)
        changelist.model._meta.get_field.return_value.verbose_name = "last login"

        context = templatetags.admin_interface_date_hierarchy_removal_link(
            changelist, "last_login"
        )

        self.assertEqual(context["removal_link"], "?")
        self.assertEqual(context["date_label"], "last login")
        self.assertEqual(context["date_value"], date(2022, 11, 1))

    def test_date_hierarchy_removal_link_year_month_day(self):
        params = {
            "last_login__year": 2022,
            "last_login__month": "11",
            "last_login__day": "30",
            "shape": "round",
            "size": "small",
        }
        changelist = self._get_changelist_mock(params)
        changelist.model._meta.get_field.return_value.verbose_name = "last login"

        context = templatetags.admin_interface_date_hierarchy_removal_link(
            changelist, "last_login"
        )

        self.assertEqual(context["removal_link"], "?shape=round&size=small")
        self.assertEqual(context["date_label"], "last login")
        self.assertEqual(context["date_value"], date(2022, 11, 30))
