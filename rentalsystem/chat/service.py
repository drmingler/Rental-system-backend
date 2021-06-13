from django.db.models import Q

from rentalsystem.accounts.models import User
from rentalsystem.chat.models import Chat


class ChatService:
    def __init__(self):
        self.chat = Chat

    def get_conversation(self, user: User, user_id: str) -> Chat:
        conversations = Chat.objects.filter(
            Q(sender=user) & Q(receiver_id=user_id)
            | Q(sender_id=user_id) & Q(receiver=user)
        )
        return conversations.order_by("created_at")

    def get_last_message(self, user: User) -> Chat:
        last_messages = (
            Chat.objects.filter(Q(sender=user) | Q(receiver=user))
            .order_by("conversation_code", "-created_at")
            .distinct("conversation_code")
        )
        return last_messages
