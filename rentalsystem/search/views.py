from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from rentalsystem.common.models import CREATED_AT, ID
from rentalsystem.properties.models import Property, PropertyRules
from rentalsystem.search.documents.property import PropertyDocument
from rentalsystem.search.serializers import PropertyDocumentSerializer
from rentalsystem.search.utils import NUMBER_LOOKUP, STRING_LOOKUP


class PropertyDocumentView(BaseDocumentViewSet):
    """The PropertyDocumentView."""

    document = PropertyDocument
    serializer_class = PropertyDocumentSerializer
    pagination_class = PageNumberPagination
    lookup_field = ID
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        Property.MONTHLY_RENT,
        Property.NUMBER_OF_BEDROOMS,
        Property.NUMBER_OF_BATHROOMS,
        Property.PROPERTY_TYPE,
        PropertyRules.PROPERTY_RULES
        # 'houseAddress'
        # 'amenities'
        # 'longitude'
        # 'latitude'
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
        Property.MONTHLY_RENT: {
            "field": "monthlyRent",
            "lookups": NUMBER_LOOKUP,
        },
        Property.SECURITY_DEPOSIT: {
            "field": "securityDeposit",
            "lookups": NUMBER_LOOKUP,
        },
        Property.PROPERTY_NAME: Property.PROPERTY_NAME,
        Property.AVAILABLE_FROM: Property.AVAILABLE_FROM,
        Property.LISTING_DESCRIPTION: Property.LISTING_DESCRIPTION,
        Property.IS_OWNERSHIP_VERIFIED: Property.IS_OWNERSHIP_VERIFIED,
        PropertyRules.SMOKING: "propertyRules.smoking",
        PropertyRules.PET: "propertyRules.pet",
        PropertyRules.MUSICAL_INSTRUMENTS: "propertyRules.musicalInstruments",
        CREATED_AT: CREATED_AT,
    }
    # Define ordering fields
    ordering_fields = {
        Property.ID: Property.ID,
        Property.MONTHLY_RENT: Property.MONTHLY_RENT,
        CREATED_AT: CREATED_AT,
    }
    # default ordering
    ordering = (
        Property.ID,
        CREATED_AT,
    )
