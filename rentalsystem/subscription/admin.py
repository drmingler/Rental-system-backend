from django.contrib import admin

# Register your models here.
from rentalsystem.subscription.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "planType",
        "amount",
        "subscribedOn",
        "expires_on",
        "is_subscription_active",
    ]


admin.site.register(Subscription, SubscriptionAdmin)
