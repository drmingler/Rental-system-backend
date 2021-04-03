from rest_framework import serializers
from typing import List
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework.fields import IntegerField, ListField, ImageField, CharField
from rest_framework.request import Request

from rentalsystem.accounts.serializers import UserSerializer
from rentalsystem.properties.models import (
    Property,
    PropertyAddress,
    PropertyImage,
    AvailableLocation,
    PropertyAmenities,
    PropertyRules,
)
from rentalsystem.properties.service import PropertyService


class PropertyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAddress
        exclude = [
            "property",
        ]


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        exclude = ["property", "created_at", "updated_at"]


class PropertyRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyRules
        exclude = ["property", "created_at", "updated_at"]


class PropertyAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAmenities
        exclude = ["property", "created_at", "updated_at"]


COMMON_PROPERTY_FIELDS = [
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
]


class PropertyBaseSerializer(serializers.ModelSerializer):
    """Base serializer for property. Every property serializer inherits from this"""

    propertyAddress = PropertyAddressSerializer()
    propertyImage = PropertyImageSerializer(many=True)

    class Meta:
        model = Property
        fields = COMMON_PROPERTY_FIELDS + [
            PropertyAddress.PROPERTY_ADDRESS,
            PropertyImage.PROPERTY_IMAGE,
        ]

        read_only_fields = [
            Property.ID,
            Property.LANDLORD,
            Property.IS_OWNERSHIP_VERIFIED,
        ]


class ViewablePropertiesSerializer(PropertyBaseSerializer):
    propertyAmenities = PropertyAmenitiesSerializer()
    propertyRules = PropertyRulesSerializer()
    landlord = UserSerializer()

    class Meta:
        model = Property
        new_fields: List = [
            PropertyAmenities.PROPERTY_AMENITIES,
            PropertyRules.PROPERTY_RULES,
            Property.LANDLORD,
        ]
        fields = PropertyBaseSerializer.Meta.fields + new_fields


class EditablePropertySerializer(WritableNestedModelSerializer):
    property_service = PropertyService()
    propertyAmenities = PropertyAmenitiesSerializer()
    propertyRules = PropertyRulesSerializer()
    propertyAddress = PropertyAddressSerializer()
    propertyImage = PropertyImageSerializer(many=True)

    class Meta:
        model = Property
        fields = COMMON_PROPERTY_FIELDS + [
            PropertyAddress.PROPERTY_ADDRESS,
            PropertyImage.PROPERTY_IMAGE,
            PropertyAmenities.PROPERTY_AMENITIES,
            PropertyRules.PROPERTY_RULES,
        ]

        read_only_fields = [
            Property.ID,
            Property.LANDLORD,
            Property.IS_OWNERSHIP_VERIFIED,
        ]

    def create(self, validated_data):
        request: Request = self.context.get("request")
        return self.property_service.create_property(
            validated_data=validated_data, request=request
        )


class AvailableLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableLocation
        exclude = ["property", "created_at", "updated_at"]


class ImageUploaderSerializer(serializers.Serializer):
    property_service = PropertyService()
    id = IntegerField(min_value=1, required=True)
    modelName = CharField(min_length=2, required=True)
    image = ListField(child=ImageField(), required=True)

    def create(self, validated_data):
        return self.property_service.upload_image(validated_data=validated_data)
