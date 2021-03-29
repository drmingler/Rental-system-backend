from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from rentalsystem.common.permission import IsOwner
from rentalsystem.subscription.models import Subscription
from rentalsystem.subscription.serializers import TransactionHistorySerializer


# Create your views here.
## Create transaction
## Get tx history


class TransactionHistoryViewSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = [IsOwner]
    serializer_class = TransactionHistorySerializer
    queryset = Subscription.objects.all()
