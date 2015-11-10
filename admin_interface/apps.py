# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.db.models.signals import post_migrate

from admin_interface.models import Theme


class AdminInterfaceConfig(AppConfig):
    
    name = 'admin_interface'
    verbose_name = 'Admin Interface'
    
    def ready(self):
        
        post_migrate.connect(Theme.post_migrate_handler, sender = self)
        
        