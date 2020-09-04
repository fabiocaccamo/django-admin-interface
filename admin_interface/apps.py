# -*- coding: utf-8 -*-

import django
from django.apps import AppConfig
from django.db.models.signals import post_migrate
if django.VERSION < (2, 0):
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _


class AdminInterfaceConfig(AppConfig):

    name = 'admin_interface'
    verbose_name = _('Admin Interface')

    def ready(self):

        from admin_interface import settings
        from admin_interface.models import Theme

        settings.check_installed_apps()
        post_migrate.connect(
            Theme.post_migrate_handler, sender=self)
