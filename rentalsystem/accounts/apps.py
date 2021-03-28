from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "rentalsystem.accounts"
    verbose_name = _("Users")

    def ready(self):
        try:
            import rentalsystem.accounts.signals  # noqa F401
        except ImportError:
            pass
