from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from rentalsystem.common.permission import IsLandlord
from rentalsystem.properties.models import Property, AvailableLocation
from rentalsystem.properties.serializers import (
    ViewablePropertiesSerializer,
    AvailableLocationSerializer,
    EditablePropertySerializer,
)


## get property everybody retrieve
## create property landlord create
## update property landlord update
## delete property landlord delete

### using advance search
## search for  properties by address
## search for  properties by long and lat state
## use search for similar properties
## crit  based filtering

## get recent properties
## get newest properties
## get low to high price properties
## get high to low price properties

## get properties by landlord id
## get properties by state
## get current state


class EditPropertyDetailsViewSet(
    CreateModelMixin, DestroyModelMixin, UpdateModelMixin, GenericViewSet
):
    permission_classes = [IsLandlord]
    queryset = Property.objects.all()
    serializer_class = EditablePropertySerializer


class ViewPropertyDetailsViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Property.objects.all()
    serializer_class = EditablePropertySerializer


class SimplePropertySearchViewSet(ListModelMixin, GenericViewSet):
    queryset = Property.objects.all()
    serializer_class = ViewablePropertiesSerializer
    filter_backends = [SearchFilter]
    search_fields = ["landlord__id", "propertyAddress__stateName"]


class CurrentLocationViewSet(viewsets.ViewSet, GenericViewSet):
    def list(self, request):
        location_name: str = self.request.query_params.get("location_name")
        location_object = get_object_or_404(
            AvailableLocation, stateName=location_name.capitalize()
        )
        serializer = AvailableLocationSerializer(location_object)
        return Response(serializer.data)
