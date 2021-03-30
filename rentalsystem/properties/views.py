from rest_framework.filters import SearchFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rentalsystem.properties.models import Property
from rentalsystem.properties.serializers import PropertySerializer


## get property
## create property
## update property
## delete property


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


class SimplePropertySearchViewSet(ListModelMixin, GenericViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [SearchFilter]
    search_fields = ["landlord__id", "propertyAddress__stateName"]
