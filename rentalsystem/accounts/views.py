from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import User
from .serializers import UserSerializer
from ..common.permission import IsOwnProfile


## get user add permission to allow only user see only his own profile
## update user
## get landlord profile
## get properties by landlord id


class ProfileViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """Returns a user's profile either a landlord or tenant"""

    permission_classes = [IsOwnProfile]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LandlordProfileViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(userType=User.LANDLORD)
