from rest_framework import serializers
from typing import List, Dict
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework.request import Request

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
        exclude = [
            "property",
        ]


class PropertyRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyRules
        exclude = [
            "property",
        ]


class PropertyAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAmenities
        exclude = [
            "property",
        ]


# class PropertyBaseSerializer(WritableNestedModelSerializer):
class PropertyBaseSerializer(serializers.ModelSerializer):
    """Base serializer for property. Every property serializer inherits from this"""

    propertyAddress = PropertyAddressSerializer()
    propertyImage = PropertyImageSerializer(many=True)

    class Meta:
        model = Property
        fields = [
            Property.ID,
            # Property.LANDLORD,
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

    class Meta:
        model = Property
        new_fields: List = [
            PropertyAmenities.PROPERTY_AMENITIES,
            PropertyRules.PROPERTY_RULES,
        ]
        fields = PropertyBaseSerializer.Meta.fields + new_fields


class EditablePropertySerializer(PropertyBaseSerializer):
    property_service = PropertyService()
    propertyAmenities = PropertyAmenitiesSerializer()
    propertyRules = PropertyRulesSerializer()

    class Meta:
        model = Property
        new_fields: List = [
            PropertyAmenities.PROPERTY_AMENITIES,
            PropertyRules.PROPERTY_RULES,
        ]
        fields = PropertyBaseSerializer.Meta.fields + new_fields

    def create(self, validated_data):
        request: Request = self.context.get("request")
        return self.property_service.create_property(
            validated_data=validated_data, request=request
        )

    # def update(self, instance, validated_data):
    #     print(instance.propertyAddress)
    #     instance.propertyAddress = validated_data.get(PropertyAddress.PROPERTY_ADDRESS, instance.propertyAddress)
    #     instance.propertyAmenities = validated_data.get(PropertyAmenities.PROPERTY_AMENITIES, instance.propertyAmenities)
    #     instance.propertyRules = validated_data.get(PropertyRules.PROPERTY_RULES, instance.propertyRules)
    #     instance.propertyImage  = validated_data.get(PropertyImage.PROPERTY_IMAGE, instance.propertyImage)
    #     instance.save()
    #
    #     print(instance)
    #     print(validated_data)
    #     request: Request = self.context.get("request")
    #     pass


class AvailableLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableLocation
        fields = [
            AvailableLocation.STATE_NAME,
            AvailableLocation.COUNTRY,
            AvailableLocation.LONGITUDE,
            AvailableLocation.LATITUDE,
        ]
