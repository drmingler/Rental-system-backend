from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from rentalsystem.common.permission import IsOwner
from rentalsystem.subscription.models import Subscription
from rentalsystem.subscription.serializers import (
    TransactionHistorySerializer,
    SubscriptionSerializer,
)


class TransactionHistoryViewSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = [IsOwner]
    serializer_class = TransactionHistorySerializer
    queryset = Subscription.objects.all()


class SubscriptionViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_200_OK)
