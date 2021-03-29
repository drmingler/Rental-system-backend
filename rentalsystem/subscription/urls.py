from rest_framework.routers import SimpleRouter

from rentalsystem.subscription.views import TransactionHistoryViewSet

router = SimpleRouter()
router.register("transactions", TransactionHistoryViewSet)

urlpatterns = router.urls
