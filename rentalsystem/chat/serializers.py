from rest_framework import serializers

from rentalsystem.chat.models import Chat
from rentalsystem.common.models import ID


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        exclude = [ID]
