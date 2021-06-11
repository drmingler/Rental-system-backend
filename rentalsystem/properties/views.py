from rest_framework import status, permissions
from rest_framework.filters import SearchFilter
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
from rentalsystem.properties.models import Property, AvailableLocation, PropertyImage
from rentalsystem.properties.service import PropertyService
from rentalsystem.properties.serializers import (
    ViewablePropertiesSerializer,
    AvailableLocationSerializer,
    EditablePropertySerializer,
    PropertyBaseSerializer,
    ImageUploaderSerializer,
    FileUploaderSerializer,
)


### using advance search
## search for  properties by address
## search for  properties by long and lat state
## use search for similar properties
## crit  based filtering

## get recent properties
## get newest properties
## get low to high price properties
## get high to low price properties

# To be added
# Make listing expired after a month if owner has an expired sub,


class PropertyDetailsViewSet(
    CreateModelMixin, DestroyModelMixin, UpdateModelMixin, GenericViewSet
):
    property_service = PropertyService()
    permission_classes = [IsLandlord]
    queryset = property_service.get_properties()
    serializer_class = EditablePropertySerializer

    def create(self, request, *args, **kwargs):
        self.property_service.can_user_upload_more_houses(request.user)
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PropertyMediaUploadViewSet(CreateModelMixin, DestroyModelMixin, GenericViewSet):
    permission_classes = [IsLandlord]

    def create(self, request, *args, **kwargs):
        payload = request.data
        model_name = payload["modelName"]
        serializer = (
            ImageUploaderSerializer(data=payload)
            if model_name == "PropertyImage"
            else FileUploaderSerializer(data=payload)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        instance = PropertyImage.objects.get(id=pk)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ViewPropertyDetailsViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Property.objects.all()
    serializer_class = ViewablePropertiesSerializer


class SimplePropertySearchViewSet(ListModelMixin, GenericViewSet):
    property_service = PropertyService()
    queryset = property_service.get_properties()
    serializer_class = PropertyBaseSerializer
    filter_backends = [SearchFilter]
    search_fields = ["landlord__id", "propertyAddress__stateName"]


class CurrentLocationViewSet(ListModelMixin, GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = AvailableLocationSerializer
    queryset = AvailableLocation.objects.all()
