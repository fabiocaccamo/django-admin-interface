from django.core.management import call_command
from django.test import TestCase

from admin_interface.models import Theme


class AdminInterfaceFixturesTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __load_theme(self, theme_name):
        call_command("loaddata", f"admin_interface_theme_{theme_name}.json")

    def test_import_initial_data(self):
        call_command("loaddata", "initial_data.json")
        self.assertEqual(Theme.objects.count(), 1)

    def test_import_all(self):
        self.__load_theme("django")
        self.__load_theme("bootstrap")
        self.__load_theme("foundation")
        self.__load_theme("uswds")
        self.assertEqual(Theme.objects.count(), 4)

    def test_import_idempotency(self):
        self.__load_theme("django")
        self.__load_theme("django")
        self.__load_theme("django")
        self.__load_theme("django")
        self.__load_theme("django")
        self.assertEqual(Theme.objects.count(), 1)
        self.__load_theme("bootstrap")
        self.__load_theme("bootstrap")
        self.__load_theme("bootstrap")
        self.assertEqual(Theme.objects.count(), 2)

    def test_import_override(self):
        obj1 = Theme.objects.get_active()
        obj1.title = "Custom 1"
        obj1.save()
        self.__load_theme("django")
        obj2 = Theme.objects.get_active()
        self.assertEqual(obj1.pk, obj2.pk)
        self.assertTrue(obj1.title != obj2.title)
