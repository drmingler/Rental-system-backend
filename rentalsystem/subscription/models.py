# Create your models here.
from datetime import datetime, timedelta
from typing import Union

from django.db.models import (
    CharField,
    ForeignKey,
    OneToOneField,
    DecimalField,
    DateTimeField,
    CASCADE,
)

from rentalsystem.accounts.models import User
from rentalsystem.common.models import AbstractBaseModel


class Subscription(AbstractBaseModel):
    """ Property Listing Subscription  Model """

    FREE = "Free"
    MONTHLY = "Monthly"
    YEARLY = "Yearly"

    PLAN_TYPE = (
        (FREE, "Free"),
        (MONTHLY, "Monthly"),
        (YEARLY, "Yearly"),
    )

    user = OneToOneField(User, related_name="subscription", on_delete=CASCADE)
    planType = CharField(choices=PLAN_TYPE, default=FREE, max_length=20)
    amount = DecimalField(default=0.00, max_digits=10, decimal_places=2)
    subscribedOn = DateTimeField(blank=True)

    def expires_on(self) -> Union[datetime, None]:
        if self.subscribedOn:
            return self.subscribedOn + timedelta(30)

    def is_subscription_active(self) -> bool:
        expiry_date = self.expires_on()
        if expiry_date:
            return expiry_date <= datetime.now()
        return False
