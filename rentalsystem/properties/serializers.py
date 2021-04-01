from rest_framework import serializers
from rentalsystem.properties.models import (
    Property,
    PropertyAddress,
    PropertyImage,
    AvailableLocation,
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


class PropertySerializer(serializers.ModelSerializer):
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
        ]


class AvailableLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableLocation
        fields = [
            AvailableLocation.STATE_NAME,
            AvailableLocation.COUNTRY,
            AvailableLocation.LONGITUDE,
            AvailableLocation.LATITUDE,
        ]
