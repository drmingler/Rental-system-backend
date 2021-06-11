from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from rentalsystem.accounts.models import User
from rentalsystem.accounts.serializers import (
    UserSerializer,
    LandlordSerializer,
    SimpleUserSerializer,
)
from rentalsystem.common.permission import IsOwnProfile


class RetrieveProfileViewSet(RetrieveModelMixin, GenericViewSet):
    """Returns a user's profile either a landlord or tenant"""

    serializer_class = SimpleUserSerializer
    queryset = User.objects.all()


class UpdateProfileViewSet(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsOwnProfile]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LandlordProfileViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = LandlordSerializer
    queryset = User.objects.all()

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(userType=User.LANDLORD)
