from django.db.models.query_utils import Q
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from rentalsystem.chat.models import Chat
from rentalsystem.chat.serializers import ChatSerializer


class ChatViewSet(ListModelMixin, GenericViewSet):
    serializer_class = ChatSerializer

    def get_queryset(self):
        user_id: str = self.request.query_params.get("user_id")
        user = self.request.user
        return Chat.objects.filter(
            Q(sender=user) & Q(receiver_id=user_id)
            | Q(sender_id=user_id) & Q(receiver=user)
        )
