from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import User
from .serializers import UserSerializer
from ..common.permission import IsOwner


## get user add permission to allow only user see only his own profile
## update user
## get landlord profile
## get properties by landlord id


class AllUserProfileViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [IsOwner]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LandlordPropertiesViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(userType=User.LANDLORD)
