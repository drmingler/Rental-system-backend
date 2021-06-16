from rest_framework.routers import SimpleRouter
from django.urls import path, include
from rentalsystem.accounts.views import (
    RetrieveProfileViewSet,
    LandlordProfileViewSet,
    UpdateProfileViewSet,
    Profile,
)

router = SimpleRouter()
router.register("retrieve-profile", RetrieveProfileViewSet)
router.register("update-profile", UpdateProfileViewSet)
router.register("landlord", LandlordProfileViewSet)

urlpatterns = [
    path("profile/", Profile.as_view(), name="profile"),
    path("", include(router.urls)),
]
