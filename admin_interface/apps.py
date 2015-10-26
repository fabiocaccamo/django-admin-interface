# -*- coding: utf-8 -*-

from django.apps import AppConfig


class AdminInterfaceConfig(AppConfig):
    
    name = 'admin_interface'
    verbose_name = 'Admin Interface'
    
    def ready(self):
        pass
        