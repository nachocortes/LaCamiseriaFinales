from django.apps import AppConfig


class CrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.CRM'

    def ready(self):
        import core.CRM.signals