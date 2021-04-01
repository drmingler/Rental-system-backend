from rest_framework import serializers
from typing import List

from rentalsystem.properties.models import (
    Property,
    PropertyAddress,
    PropertyImage,
    AvailableLocation,
    PropertyAmenities,
    PropertyRules,
)


class PropertyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAddress
        fields = [
            PropertyAddress.PROPERTY,
            PropertyAddress.ADDRESS,
            PropertyAddress.STATE_NAME,
            PropertyAddress.LATITUDE,
            PropertyAddress.LONGITUDE,
        ]


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = "__all__"
        read_only_fields = [
            Property.ID,
        ]


class PropertyRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyRules
        fields = "__all__"
        read_only_fields = [
            Property.ID,
        ]


class PropertyAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAmenities
        fields = "__all__"
        read_only_fields = [
            Property.ID,
        ]


class PropertyBaseSerializer(serializers.ModelSerializer):
    """Base serializer for property. Every property serializer inherits from this"""

    propertyAddress = PropertyAddressSerializer()
    propertyImage = PropertyImageSerializer(many=True)

    class Meta:
        PROPERTY_ADDRESS = "propertyAddress"
        PROPERTY_IMAGE = "propertyImage"

        model = Property
        fields = [
            Property.ID,
            Property.LANDLORD,
            Property.PROPERTY_NAME,
            Property.NUMBER_OF_BEDROOMS,
            Property.NUMBER_OF_BATHROOMS,
            Property.LISTING_DESCRIPTION,
            Property.AVAILABLE_FROM,
            Property.IS_OWNERSHIP_VERIFIED,
            Property.UNIT,
            Property.SIZE,
            Property.PROPERTY_TYPE,
            Property.MONTHLY_RENT,
            Property.SECURITY_DEPOSIT,
            PROPERTY_ADDRESS,
            PROPERTY_IMAGE,
        ]
        read_only_fields = [
            Property.ID,
            Property.LANDLORD,
        ]


class ViewablePropertiesSerializer(PropertyBaseSerializer):
    propertyAmenities = PropertyAmenitiesSerializer()
    propertyRules = PropertyRulesSerializer()

    class Meta:
        model = Property
        PROPERTY_AMENITIES = "propertyAmenities"
        PROPERTY_RULES = "propertyRules"

        new_fields: List = [PROPERTY_AMENITIES, PROPERTY_RULES]
        fields = PropertyBaseSerializer.Meta.fields + new_fields


class EditablePropertySerializer(PropertyBaseSerializer):
    propertyAmenities = PropertyAmenitiesSerializer()
    propertyRules = PropertyRulesSerializer()

    class Meta:
        model = Property
        PROPERTY_AMENITIES = "propertyAmenities"
        PROPERTY_RULES = "propertyRules"

        new_fields: List = [PROPERTY_AMENITIES, PROPERTY_RULES]
        fields = PropertyBaseSerializer.Meta.fields + new_fields


class AvailableLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableLocation
        fields = [
            AvailableLocation.STATE_NAME,
            AvailableLocation.COUNTRY,
            AvailableLocation.LONGITUDE,
            AvailableLocation.LATITUDE,
        ]
