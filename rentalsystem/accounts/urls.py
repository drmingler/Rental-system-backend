from rest_framework.routers import SimpleRouter
from rentalsystem.accounts.views import (
    RetrieveProfileViewSet,
    LandlordProfileViewSet,
    UpdateProfileViewSet,
)

router = SimpleRouter()
router.register("retrieve-profile", RetrieveProfileViewSet)
router.register("update-profile", UpdateProfileViewSet)
router.register("landlord", LandlordProfileViewSet)

urlpatterns = router.urls
