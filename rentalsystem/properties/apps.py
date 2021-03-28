from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PropertiesConfig(AppConfig):
    name = "rentalsystem.properties"

    verbose_name = _("Properties")
