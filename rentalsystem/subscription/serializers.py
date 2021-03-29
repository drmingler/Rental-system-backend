from rest_framework import serializers
from rest_framework.fields import CharField, DateField

from rentalsystem.subscription.models import Subscription


class TransactionHistorySerializer(serializers.ModelSerializer):
    expiresOn = serializers.CharField(source="expires_on")
    isSubscriptionActive = serializers.CharField(source="is_subscription_active")

    class Meta:
        model = Subscription
        fields = [
            Subscription.PLAN_TYPE,
            Subscription.AMOUNT,
            Subscription.IS_SUBSCRIPTION_ACTIVE,
            Subscription.SUBSCRIBED_ON,
            Subscription.EXPIRES_ON,
        ]


class SubscriptionSerializer(serializers.Serializer):
    cardHolderName = CharField(min_length=4, max_length=40, required=True)
    cardNumber = CharField(min_length=16, max_length=40, required=True)
    expiry = DateField(required=True)
    cvc = CharField(max_length=4, required=True)
