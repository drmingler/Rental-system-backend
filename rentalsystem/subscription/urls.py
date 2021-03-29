from rest_framework.routers import SimpleRouter

from rentalsystem.subscription.views import (
    TransactionHistoryViewSet,
    SubscriptionViewSet,
)

router = SimpleRouter()
router.register("transactions", TransactionHistoryViewSet)
router.register("subscription", SubscriptionViewSet, basename="subscription")

urlpatterns = router.urls
