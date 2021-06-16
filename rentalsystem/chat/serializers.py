from rest_framework import serializers

from rentalsystem.accounts.serializers import SimpleUserSerializer
from rentalsystem.chat.models import Chat
from rentalsystem.common.models import ID


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        exclude = [ID]


class LastMessageSerializer(serializers.ModelSerializer):
    receiver = SimpleUserSerializer()
    sender = SimpleUserSerializer()

    class Meta:
        model = Chat
        exclude = [ID]
