from typing import Dict, List

from rest_framework.exceptions import PermissionDenied
from rest_framework.request import Request
from django.apps import apps

from rentalsystem.accounts.models import User
from rentalsystem.properties.models import (
    Property,
    PropertyAddress,
    PropertyRules,
    PropertyAmenities,
)
from rentalsystem.properties.utils import UploadLimitReached, InvalidPayload
from rentalsystem.subscription.models import Subscription


class PropertyService:
    def __init__(self):
        self.property = Property
        self.subscription = Subscription

    def get_properties(self) -> List[Property]:
        return Property.objects.all()

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

    def get_model_instance(self, model_name: str):
        instance = next(
            filter(lambda model: model.__name__ == model_name, apps.get_models())
        )
        return instance

    def is_own_property(self, user: User, payload: Dict):
        property_exist = Property.objects.filter(
            landlord=user, id=payload["id"]
        ).exists()
        if property_exist:
            return
        raise PermissionDenied()

    def create_property(self, validated_data: Dict, request: Request) -> Property:
        property_amenities: Dict = validated_data.pop(
            PropertyAmenities.PROPERTY_AMENITIES
        )
        property_address: Dict = validated_data.pop(PropertyAddress.PROPERTY_ADDRESS)
        property_rules: Dict = validated_data.pop(PropertyRules.PROPERTY_RULES)

        new_property = Property.objects.create(**validated_data, landlord=request.user)
        try:
            PropertyAddress.objects.create(**property_address, property=new_property)
            PropertyRules.objects.create(**property_rules, property=new_property)
            PropertyAmenities.objects.create(
                **property_amenities, property=new_property
            )

        except Exception:
            raise InvalidPayload()

        return new_property

    def upload_image(self, validated_data: Dict):
        model_name: str = validated_data.pop("modelName")
        media_files: List = validated_data.pop("image", "document")

        try:
            property_instance = Property.objects.get(**validated_data)
            instance = self.get_model_instance(model_name=model_name)
            for file in media_files:
                if model_name == "PropertyImage":
                    instance.objects.create(image=file, property=property_instance)
                else:
                    instance.objects.create(document=file, property=property_instance)

        except Exception:
            raise InvalidPayload()

        return instance
