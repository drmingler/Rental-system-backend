from rest_framework.routers import SimpleRouter
from rentalsystem.accounts.views import AllUserProfileViewSet, LandlordPropertiesViewSet

router = SimpleRouter()
router.register("accounts", AllUserProfileViewSet)
router.register("landlord", LandlordPropertiesViewSet)

urlpatterns = router.urls
