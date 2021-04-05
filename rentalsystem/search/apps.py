from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SearchConfig(AppConfig):
    name = "rentalsystem.search"
    verbose_name = _("Searches")

    def ready(self):
        try:
            import rentalsystem.search.signals  # noqa F401
        except ImportError:
            pass
