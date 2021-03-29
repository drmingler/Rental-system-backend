from rest_framework import serializers

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
