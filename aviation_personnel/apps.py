from django.apps import AppConfig
from django.core.signals import setting_changed


class AviationPersonnelConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "aviation_personnel"

    # def ready(self):
    #     setting_changed.connect()
