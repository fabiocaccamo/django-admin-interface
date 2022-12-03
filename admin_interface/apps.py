from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdminInterfaceConfig(AppConfig):

    name = "admin_interface"
    verbose_name = _("Admin Interface")
    default_auto_field = "django.db.models.AutoField"

    def ready(self):
        from admin_interface import settings

        settings.check_installed_apps()
