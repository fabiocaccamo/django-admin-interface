# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import override_settings, TestCase
from django.test.client import RequestFactory
from django.template import Context, Template

from admin_interface.models import Theme
from admin_interface.templatetags import admin_interface_tags as templatetags
from admin_interface.version import __version__


class AdminInterfaceTemplateTagsTestCase(TestCase):

    def setUp(self):
        self.request_factory = RequestFactory()

    def tearDown(self):
        pass

    def __render_template(self, string, context=None):
        return Template(string).render(Context(context or {}))

    def test_get_admin_interface_languages(self):
        context = Context({
            'request': self.request_factory.get('/en/admin/'),
        })
        languages = templatetags.get_admin_interface_languages(context)
        expected_languages = [
            {'code': 'en', 'name': 'English', 'default': True, 'active': True, 'activation_url': '/i18n/setlang/?next=/en/admin/'},
            {'code': 'it', 'name': 'Italian', 'default': False, 'active': False, 'activation_url': '/i18n/setlang/?next=/it/admin/'}
        ]
        self.assertEqual(len(languages), len(expected_languages))
        self.assertEqual(languages[0], expected_languages[0])
        self.assertEqual(languages[1], expected_languages[1])

    @override_settings(
        USE_I18N = False,
    )
    def test_get_admin_interface_languages_with_i18n_disabled(self):
        context = Context({
            'request': self.request_factory.get('/en/admin/'),
        })
        languages = templatetags.get_admin_interface_languages(context)
        self.assertEqual(languages, None)

    @override_settings(
        ROOT_URLCONF = 'tests.urls_without_i18n_patterns',
    )
    def test_get_admin_interface_languages_without_i18n_url_patterns(self):
        context = Context({
            'request': self.request_factory.get('/en/admin/'),
        })
        languages = templatetags.get_admin_interface_languages(context)
        self.assertEqual(languages, None)

    @override_settings(
        LANGUAGES = (
            ('en', 'English'),
        ),
    )
    def test_get_admin_interface_languages_without_multiple_languages(self):
        context = Context({
            'request': self.request_factory.get('/en/admin/'),
        })
        languages = templatetags.get_admin_interface_languages(context)
        self.assertEqual(languages, None)

    def test_get_admin_interface_languages_without_request(self):
        context = Context({})
        languages = templatetags.get_admin_interface_languages(context)
        self.assertEqual(languages, None)

    def test_get_admin_interface_languages_without_language_prefix_in_url(self):
        context = Context({
            'request': self.request_factory.get('/admin/'),
        })
        languages = templatetags.get_admin_interface_languages(context)
        self.assertEqual(languages, None)

    def test_get_theme(self):
        Theme.objects.all().delete()
        context = Context({})
        theme = templatetags.get_admin_interface_theme(context)
        self.assertEqual(theme.name, 'Django')
        rendered = self.__render_template(
            '{% load admin_interface_tags %}'\
            '{% get_admin_interface_theme as theme %}'\
            '{{ theme.name }}', context)
        self.assertEqual(rendered, 'Django')

    def test_get_theme_with_request(self):
        Theme.objects.all().delete()
        context = Context({
            'request': self.request_factory.get('/')
        })
        theme = templatetags.get_admin_interface_theme(context)
        self.assertEqual(theme.name, 'Django')
        rendered = self.__render_template(
            '{% load admin_interface_tags %}'\
            '{% get_admin_interface_theme as theme %}'\
            '{{ theme.name }}', context)
        self.assertEqual(rendered, 'Django')

    def test_get_version(self):
        version = templatetags.get_admin_interface_version()
        self.assertEqual(version, __version__)
        rendered = self.__render_template(
            '{% load admin_interface_tags %}'\
            '{% get_admin_interface_version as version %}'\
            '{{ version }}')
        self.assertEqual(rendered, __version__)
