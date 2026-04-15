from django.core.management import call_command
from django.db.migrations.exceptions import IrreversibleError
from django.test import TransactionTestCase


class MigrationsTestCase(TransactionTestCase):
    """
    Generic test case that verifies all migrations for a given app can be
    applied forward and reversed (to zero) without errors.

    Reusable in other projects: just subclass and set ``app_label``.
    """

    app_label = "admin_interface"

    def tearDown(self):
        # Restore migrations to the latest state even if the test fails
        # so that subsequent tests find the DB in the expected state.
        call_command("migrate", self.app_label, verbosity=0)
        super().tearDown()

    def test_migrate_forward_and_backward(self):
        try:
            call_command("migrate", self.app_label, "zero", verbosity=0)
        except IrreversibleError as e:
            self.fail(
                f"Migrations for '{self.app_label}' are not fully reversible: {e}"
            )
        call_command("migrate", self.app_label, verbosity=0)
