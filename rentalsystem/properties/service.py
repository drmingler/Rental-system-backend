from typing import Dict, List
from rest_framework.request import Request

from rentalsystem.accounts.models import User
from rentalsystem.properties.models import (
    Property,
    PropertyAddress,
    PropertyRules,
    PropertyAmenities,
    PropertyImage,
)
from rentalsystem.properties.utils import UploadLimitReached, InvalidPayloadReached
from rentalsystem.subscription.models import Subscription


class PropertyService:
    def __init__(self):
        self.property = Property
        self.subscription = Subscription

    def get_property_count(self, user: User) -> int:
        return self.property.objects.filter(landlord=user).count()

    def get_user_plan(self, user: User) -> Subscription:
        subscription, created = self.subscription.objects.get_or_create(user=user)
        return subscription.planType

    def can_user_upload_more_houses(self, user: User) -> bool:
        plan_type = self.get_user_plan(user)
        if plan_type != Subscription.FREE:
            return True

        number_of_properties = self.get_property_count(user)
        if number_of_properties >= 3:
            raise UploadLimitReached()
        return False

    def create_property(self, validated_data: Dict, request: Request) -> Property:
        property_address: Dict = validated_data.pop(PropertyAddress.PROPERTY_ADDRESS)
        property_amenities: Dict = validated_data.pop(
            PropertyAmenities.PROPERTY_AMENITIES
        )
        property_rules: Dict = validated_data.pop(PropertyRules.PROPERTY_RULES)
        property_image: List = validated_data.pop(PropertyImage.PROPERTY_IMAGE)

        new_property = Property.objects.create(**validated_data, landlord=request.user)
        try:
            PropertyAddress.objects.create(**property_address, property=new_property)
            PropertyAmenities.objects.create(
                **property_amenities, property=new_property
            )
            PropertyRules.objects.create(**property_rules, property=new_property)

            for image in property_image:
                PropertyImage.objects.create(image=image, property=new_property)

        except Exception:
            raise InvalidPayloadReached()

        return new_property
