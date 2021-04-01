from rentalsystem.accounts.models import User
from rentalsystem.properties.models import Property
from rentalsystem.properties.utils import UploadLimitReached
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
