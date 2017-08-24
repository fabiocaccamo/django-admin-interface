# -*- coding: utf-8 -*-

from django.conf import settings
from django.test import TestCase
from django.test.client import RequestFactory
from django.template import Context, Template

import random
import shutil

from admin_interface.models import Theme
from admin_interface.templatetags import admin_interface_tags as templatetags
from admin_interface.version import __version__


class AdminInterfaceTestCase(TestCase):

    def setUp(self):
        self.request_factory = RequestFactory()
        pass

    def tearDown(self):
        shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)
        pass

    def __render_template(self, string, context):
        return Template(string).render(context)

    def __test_active_theme(self):
        theme = Theme.get_active_theme()
        print( theme )
        self.assertTrue(theme != None)
        self.assertTrue(theme.active)
        self.assertEqual(Theme.objects.filter( active = True ).count(), 1);

    def test_default_theme_created_if_no_themes(self):
        Theme.objects.all().delete()
        self.__test_active_theme()

    def test_default_theme_created_if_all_themes_deleted(self):
        Theme.objects.all().delete()
        self.__test_active_theme()

    def test_default_theme_activated_on_save_if_no_active_themes(self):
        Theme.objects.all().delete()
        theme = Theme.get_active_theme()
        theme.active = False
        theme.save()
        self.__test_active_theme()

    def test_default_theme_activated_after_update_if_no_active_themes(self):
        Theme.objects.all().delete()
        Theme.objects.all().update( active = False )
        self.__test_active_theme()

    def test_default_theme_activated_after_update_if_multiple_active_themes(self):
        Theme.objects.all().delete()
        theme_1 = Theme.objects.create( name = 'Custom 1', active = True )
        theme_2 = Theme.objects.create( name = 'Custom 2', active = True )
        theme_3 = Theme.objects.create( name = 'Custom 3', active = True )
        Theme.objects.update( active = False )
        Theme.objects.update( active = True )
        self.__test_active_theme()

    def test_default_theme_activated_on_active_theme_deleted(self):
        Theme.objects.all().delete()
        theme_1 = Theme.objects.create( name = 'Custom 1', active = True )
        theme_2 = Theme.objects.create( name = 'Custom 2', active = True )
        theme_3 = Theme.objects.create( name = 'Custom 3', active = True )
        Theme.objects.filter( pk = Theme.get_active_theme().pk ).delete()
        self.__test_active_theme()

    def test_last_theme_activated_on_multiple_themes_created(self):
        Theme.objects.all().delete()
        theme_1 = Theme.objects.create( name = 'Custom 1', active = True )
        theme_2 = Theme.objects.create( name = 'Custom 2', active = True )
        theme_3 = Theme.objects.create( name = 'Custom 3', active = True )
        self.assertEqual( Theme.get_active_theme().pk, theme_3.pk )
        self.__test_active_theme()

    def test_last_theme_activated_on_multiple_themes_activated(self):
        Theme.objects.all().delete()
        theme_1 = Theme.objects.create( name = 'Custom 1', active = True )
        theme_2 = Theme.objects.create( name = 'Custom 2', active = True )
        theme_3 = Theme.objects.create( name = 'Custom 3', active = True )
        theme_4 = Theme.objects.create( name = 'Custom 4', active = True )
        theme_5 = Theme.objects.create( name = 'Custom 5', active = True )
        themes = [ theme_1, theme_2, theme_3, theme_4, theme_5 ]
        for i in range(5):
            random.shuffle(themes)
            for theme in themes:
                theme.set_active()
                self.assertEqual( Theme.get_active_theme().pk, theme.pk )
        self.__test_active_theme()

    def test_templatetags_get_theme(self):
        Theme.objects.all().delete()
        context = Context({})
        theme = templatetags.get_admin_interface_theme(context)
        self.assertEqual(theme.name, 'Django')
        rendered = self.__render_template('{% load admin_interface_tags %}{% get_admin_interface_theme as theme %}{{ theme.name }}', context)
        self.assertEqual(rendered, 'Django')

    def test_templatetags_get_theme_with_request(self):
        Theme.objects.all().delete()
        context = Context({
            'request': self.request_factory.get('/')
        })
        theme = templatetags.get_admin_interface_theme(context)
        self.assertEqual(theme.name, 'Django')
        rendered = self.__render_template('{% load admin_interface_tags %}{% get_admin_interface_theme as theme %}{{ theme.name }}', context)
        self.assertEqual(rendered, 'Django')

    def test_templatetags_get_version(self):
        context = Context({})
        version = templatetags.get_admin_interface_version(context)
        self.assertEqual(version, __version__)
        rendered = self.__render_template('{% load admin_interface_tags %}{% get_admin_interface_version as version %}{{ version }}', context)
        self.assertEqual(rendered, __version__)

    def test_repr(self):
        theme = Theme.get_active_theme()
        self.assertEqual( '{0}'.format(theme), 'Django' )

