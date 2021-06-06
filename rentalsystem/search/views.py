from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    CompoundSearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet

from rentalsystem.common.models import CREATED_AT, ID
from rentalsystem.common.paginator import CustomPaginator
from rentalsystem.properties.models import (
    Property,
    PropertyRules,
    PropertyAddress,
    PropertyAmenities,
)
from rentalsystem.search.documents.property import PropertyDocument
from rentalsystem.search.serializers import PropertyDocumentSerializer
from rentalsystem.search.utils import NUMBER_LOOKUP, STRING_LOOKUP


class PropertyDocumentView(BaseDocumentViewSet):
    """The PropertyDocumentView."""

    document = PropertyDocument
    serializer_class = PropertyDocumentSerializer
    pagination_class = CustomPaginator
    lookup_field = ID
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        PropertyRules.PROPERTY_RULES,
        PropertyAddress.PROPERTY_ADDRESS,
        PropertyAmenities.PROPERTY_AMENITIES,
    )
    # Define filter fields
    filter_fields = {
        ID: {
            "field": ID,
            "lookups": NUMBER_LOOKUP,
        },
        Property.LANDLORD: {
            "field": Property.LANDLORD,
            "lookups": NUMBER_LOOKUP,
        },
        Property.NUMBER_OF_BATHROOMS: {
            "field": Property.NUMBER_OF_BATHROOMS,
            "lookups": NUMBER_LOOKUP,
        },
        Property.NUMBER_OF_BEDROOMS: {
            "field": Property.NUMBER_OF_BEDROOMS,
            "lookups": NUMBER_LOOKUP,
        },
        Property.UNIT: {
            "field": Property.UNIT,
            "lookups": NUMBER_LOOKUP,
        },
        Property.SIZE: {
            "field": Property.SIZE,
            "lookups": NUMBER_LOOKUP,
        },
        Property.PROPERTY_TYPE: {
            "field": Property.PROPERTY_TYPE,
            "lookups": STRING_LOOKUP,
        },
        Property.PROPERTY_STATUS: {
            "field": Property.PROPERTY_STATUS,
            "lookups": STRING_LOOKUP,
        },
        Property.MONTHLY_RENT: {
            "field": Property.MONTHLY_RENT,
            "lookups": NUMBER_LOOKUP,
        },
        Property.SECURITY_DEPOSIT: {
            "field": Property.SECURITY_DEPOSIT,
            "lookups": NUMBER_LOOKUP,
        },
        Property.PROPERTY_NAME: Property.PROPERTY_NAME,
        Property.AVAILABLE_FROM: Property.AVAILABLE_FROM,
        Property.LISTING_DESCRIPTION: Property.LISTING_DESCRIPTION,
        CREATED_AT: CREATED_AT,
        # Access PropertyRules nested fields
        PropertyRules.SMOKING: "propertyRules.smoking",
        PropertyRules.PET: "propertyRules.pet",
        PropertyRules.MUSICAL_INSTRUMENTS: "propertyRules.musicalInstruments",
        # Access PropertyAddress nested fields
        PropertyAddress.STATE_NAME: "propertyAddress.stateName",
        PropertyAddress.ADDRESS: "propertyAddress.address",
        PropertyAddress.LONGITUDE: "propertyAddress.longitude",
        PropertyAddress.LATITUDE: "propertyAddress.latitude",
        # Access PropertyAmenities nested fields
        PropertyAmenities.POOL: "propertyAmenities.pool",
        PropertyAmenities.GARDEN: "propertyAmenities.garden",
        PropertyAmenities.ELEVATOR: "propertyAmenities.elevator",
        PropertyAmenities.DOORMAN: "propertyAmenities.doorman",
        PropertyAmenities.DECK: "propertyAmenities.deck",
        PropertyAmenities.WASHER: "propertyAmenities.washer",
        PropertyAmenities.GYM: "propertyAmenities.gym",
        PropertyAmenities.PARKING: "propertyAmenities.parking",
        PropertyAmenities.FIRE_PLACE: "propertyAmenities.firePlace",
        PropertyAmenities.AIR_CONDITION: "propertyAmenities.airCondition",
        PropertyAmenities.DISH_WASHER: "propertyAmenities.dishWasher",
        PropertyAmenities.ITEM_STORAGE: "propertyAmenities.itemStorage",
        PropertyAmenities.WHEELCHAIR: "propertyAmenities.wheelchair",
        PropertyAmenities.BALCONY: "propertyAmenities.balcony",
        PropertyAmenities.HARD_FLOOR: "propertyAmenities.hardFloor",
        PropertyAmenities.FURNISHED: "propertyAmenities.furnished",
        PropertyAmenities.VIEW: "propertyAmenities.view",
        PropertyAmenities.HIGH_RISE: "propertyAmenities.highRise",
        PropertyAmenities.STUDENT_FRIENDLY: "propertyAmenities.studentFriendly",
        PropertyAmenities.UTILITIES: "propertyAmenities.utilities",
    }
    # Define ordering fields
    ordering_fields = {
        ID: ID,
        Property.MONTHLY_RENT: Property.MONTHLY_RENT,
        CREATED_AT: CREATED_AT,
    }
    # default ordering
    ordering = (
        ID,
        CREATED_AT,
    )
