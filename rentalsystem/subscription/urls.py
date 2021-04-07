from rest_framework.routers import SimpleRouter

from rentalsystem.subscription.views import (
    TransactionHistoryViewSet,
    SubscriptionViewSet,
)

router = SimpleRouter()
router.register(
    "transaction-history", TransactionHistoryViewSet, basename="transactions"
)
router.register("subscription", SubscriptionViewSet, basename="subscription")

urlpatterns = router.urls
