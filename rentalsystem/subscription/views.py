from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from rentalsystem.common.permission import IsOwner
from rentalsystem.subscription.models import Subscription
from rentalsystem.subscription.serializers import (
    TransactionHistorySerializer,
    SubscriptionSerializer,
)


class TransactionHistoryViewSet(ListModelMixin, GenericViewSet):
    permission_classes = [IsOwner]
    serializer_class = TransactionHistorySerializer

    def get_queryset(self, *args, **kwargs):
        return Subscription.objects.filter(user=self.request.user)


class SubscriptionViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_200_OK)
