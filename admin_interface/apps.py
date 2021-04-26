# -*- coding: utf-8 -*-

from admin_interface.compat import gettext_lazy as _

from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AdminInterfaceConfig(AppConfig):

    name = 'admin_interface'
    verbose_name = _('Admin Interface')
    default_auto_field = 'django.db.models.AutoField'

    def ready(self):

        from admin_interface import settings
        from admin_interface.models import Theme

        settings.check_installed_apps()
        post_migrate.connect(
            Theme.post_migrate_handler, sender=self)
