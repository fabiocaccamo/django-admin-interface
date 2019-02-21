# -*- coding: utf-8 -*-

from django.test import TestCase
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
