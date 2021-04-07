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


class EditPropertyDetailsViewSet(
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


class PropertyImageViewSet(CreateModelMixin, DestroyModelMixin, GenericViewSet):
    property_service = PropertyService()
    permission_classes = [IsLandlord]

    def create(self, request, *args, **kwargs):
        payload = request.data
        user = request.user
        self.property_service.is_own_property(user, payload)
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
        payload = request.data
        user = request.user
        self.property_service.is_own_property(user, payload)
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


class CurrentLocationViewSet(viewsets.ViewSet, GenericViewSet):
    def list(self, request):
        location_name: str = self.request.query_params.get("location_name")
        location_object = get_object_or_404(
            AvailableLocation, stateName=location_name.capitalize()
        )
        serializer = AvailableLocationSerializer(location_object)
        return Response(serializer.data)
