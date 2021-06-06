from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from rentalsystem.common.models import CREATED_AT, PROPERTY, ID
from rentalsystem.properties.models import (
    Property,
    PropertyRules,
    PropertyAddress,
    PropertyAmenities,
    PropertyImage,
)
from rentalsystem.search.documents.propertyaddress import PropertyAddressDocument
from rentalsystem.search.documents.propertyamenities import PropertyAmenitiesDocument
from rentalsystem.search.documents.propertyimage import PropertyImageDocument
from rentalsystem.search.documents.propertyrules import PropertyRulesDocument
from rentalsystem.search.documents.property import PropertyDocument


class PropertyRulesDocumentSerializer(DocumentSerializer):
    class Meta:
        document = PropertyRulesDocument
        exclude = [ID, PROPERTY]


class PropertyAddressDocumentSerializer(DocumentSerializer):
    class Meta:
        document = PropertyAddressDocument
        exclude = [ID, PROPERTY]


class PropertyAmenitiesDocumentSerializer(DocumentSerializer):
    class Meta:
        document = PropertyAmenitiesDocument
        exclude = [ID, PROPERTY]


class PropertyImageDocumentSerializer(DocumentSerializer):
    class Meta:
        document = PropertyImageDocument
        exclude = [PROPERTY]


class PropertyDocumentSerializer(DocumentSerializer):
    """Serializer for the Property document."""

    propertyRules = PropertyRulesDocumentSerializer()
    propertyAddress = PropertyAddressDocumentSerializer()
    propertyAmenities = PropertyAmenitiesDocumentSerializer()
    propertyImage = PropertyImageDocumentSerializer(many=True)

    class Meta:
        document = PropertyDocument
        fields = (
            ID,
            Property.LANDLORD,
            Property.PROPERTY_NAME,
            Property.NUMBER_OF_BEDROOMS,
            Property.NUMBER_OF_BATHROOMS,
            Property.LISTING_DESCRIPTION,
            Property.AVAILABLE_FROM,
            Property.PROPERTY_STATUS,
            Property.UNIT,
            Property.SIZE,
            Property.PROPERTY_TYPE,
            Property.MONTHLY_RENT,
            Property.SECURITY_DEPOSIT,
            CREATED_AT,
            PropertyRules.PROPERTY_RULES,
            PropertyAddress.PROPERTY_ADDRESS,
            PropertyAmenities.PROPERTY_AMENITIES,
            PropertyImage.PROPERTY_IMAGE,
        )
