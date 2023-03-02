from django.test import TestCase

from admin_interface.models import Theme

from .routers import DatabaseAppsRouter

try:
    from django.test.testcases import DatabaseOperationForbidden
except ImportError:
    DatabaseOperationForbidden = AssertionError


class AdminInterfaceModelsWithDBRoutingTestCase(TestCase):
    databases = ["replica"]

    def test_standard_dbrouter(self):
        router = DatabaseAppsRouter()
        db_for_theme = router.db_for_read(Theme)
        self.assertEqual(db_for_theme, "default")

    def test_dbrouter_selects_correct_db(self):
        DATABASE_APPS_MAPPING = {
            "admin_interface": "replica",
        }
        router = DatabaseAppsRouter(db_map=DATABASE_APPS_MAPPING)
        db_for_theme = router.db_for_read(Theme)
        self.assertEqual(db_for_theme, "replica")

    def test_dbrouter_errors_when_fetching_from_default(self):
        with self.assertRaises(DatabaseOperationForbidden):
            Theme.objects.get_active()

    def test_dbrouter_fetches_db(self):
        DATABASE_APPS_MAPPING = {
            "admin_interface": "replica",
        }
        router = DatabaseAppsRouter(db_map=DATABASE_APPS_MAPPING)
        with self.settings(DATABASE_ROUTERS=[router]):
            Theme.objects.get_active()
