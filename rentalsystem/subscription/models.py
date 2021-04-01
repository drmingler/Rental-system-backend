# Create your models here.
from datetime import datetime, timedelta
from typing import Union

from django.db.models import (
    CharField,
    OneToOneField,
    DecimalField,
    DateTimeField,
    CASCADE,
)

from rentalsystem.accounts.models import User
from rentalsystem.common.models import AbstractBaseModel


class Subscription(AbstractBaseModel):
    """ Property Listing Subscription  Model """

    USER = "user"
    PLAN_TYPE = "planType"
    AMOUNT = "amount"
    SUBSCRIBED_ON = "subscribedOn"
    EXPIRES_ON = "expiresOn"
    IS_SUBSCRIPTION_ACTIVE = "isSubscriptionActive"

    FREE = "FREE"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"

    PLAN_TYPES = (
        (FREE, "FREE"),
        (MONTHLY, "MONTHLY"),
        (YEARLY, "YEARLY"),
    )

    user = OneToOneField(User, related_name="subscription", on_delete=CASCADE)
    planType = CharField("Plan type", choices=PLAN_TYPES, default=FREE, max_length=20)
    amount = DecimalField(default=0.00, max_digits=10, decimal_places=2)
    subscribedOn = DateTimeField("Subscribed on", blank=True, null=True)

    def expires_on(self) -> Union[datetime, None]:
        if self.subscribedOn and self.planType == self.MONTHLY:
            return self.subscribedOn + timedelta(30)

        if self.subscribedOn and self.planType == self.YEARLY:
            return self.subscribedOn + timedelta(365)

    def is_subscription_active(self) -> bool:
        expiry_date = self.expires_on()
        if expiry_date:
            return expiry_date.utcnow() <= datetime.utcnow()
        return False
