from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ChatConfig(AppConfig):
    name = "rentalsystem.chat"

    verbose_name = _("Chats")
