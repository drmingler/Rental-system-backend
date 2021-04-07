from django.db.models import ForeignKey, CASCADE
from django.db.models.fields import TextField

from rentalsystem.accounts.tasks import User
from rentalsystem.common.models import AbstractBaseModel


class Chat(AbstractBaseModel):
    sender = ForeignKey(User, related_name="sender", on_delete=CASCADE)
    receiver = ForeignKey(User, related_name="receiver", on_delete=CASCADE)
    message = TextField("Message text")
