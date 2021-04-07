from django.db.models import ForeignKey, CASCADE
from django.db.models.fields import TextField, CharField

from rentalsystem.accounts.tasks import User
from rentalsystem.common.models import AbstractBaseModel


class Chat(AbstractBaseModel):
    class Meta:
        ordering = ["-created_at"]

    sender = ForeignKey(User, related_name="sender", on_delete=CASCADE)
    receiver = ForeignKey(User, related_name="receiver", on_delete=CASCADE)
    message = TextField("Message text")
    conversation_code = CharField(max_length=50)
