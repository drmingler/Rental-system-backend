from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from rentalsystem.chat.serializers import ChatSerializer, LastMessageSerializer
from rentalsystem.chat.service import ChatService


class ConversationViewSet(ListModelMixin, GenericViewSet):
    """ This view returns the last message for each conversation"""

    chat_service = ChatService()
    serializer_class = ChatSerializer

    def get_queryset(self):
        user_id: str = self.request.query_params.get("user_id")
        user = self.request.user
        result = self.chat_service.get_conversation(user=user, user_id=user_id)
        return result


class LastMessagesViewSet(ListModelMixin, GenericViewSet):
    """ This view  returns all the  messages from various conversations"""

    chat_service = ChatService()
    serializer_class = LastMessageSerializer

    def get_queryset(self):
        user = self.request.user
        result = self.chat_service.get_last_message(user=user)
        return result
