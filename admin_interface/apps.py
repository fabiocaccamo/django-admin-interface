# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AdminInterfaceConfig(AppConfig):

    name = 'admin_interface'
    verbose_name = 'Admin Interface'

    def ready(self):

        from admin_interface.models import Theme
        post_migrate.connect(Theme.post_migrate_handler, sender = self)

