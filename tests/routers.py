DATABASE_APPS_MAPPING = {
    "admin_interface": "default",
}


class DatabaseAppsRouter:
    """
    arouter to control all database operations on models for different
    databases.

    in case an app is not set in DATABASE_APPS_MAPPING, the router
    will fallback to the `default` database.

    Settings example:

    DATABASE_APPS_MAPPING = {'app1': 'db1', 'app2': 'db2'}
    """

    def __init__(self, db_map=DATABASE_APPS_MAPPING):
        """
        If routers is not specified, default to DATABASE_APPS_MAPPING
        """
        self.db_map = db_map

    def db_for_read(self, model, **hints):
        """Point all read operations to the specific database"""
        if model._meta.app_label in self.db_map:
            return self.db_map[model._meta.app_label]

        return None

    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database"""
        if model._meta.app_label in self.db_map:
            return self.db_map[model._meta.app_label]

        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation between apps that use the same database"""
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure that apps only appear in the related database"""
        return None
