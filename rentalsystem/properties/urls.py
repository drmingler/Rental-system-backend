from rest_framework.routers import SimpleRouter

from rentalsystem.properties.views import (
    SimplePropertySearchViewSet,
    CurrentLocationViewSet,
    EditPropertyDetailsViewSet,
    ViewPropertyDetailsViewSet,
    PropertyImageViewSet,
)

router = SimpleRouter()
router.register("property/create", EditPropertyDetailsViewSet)
router.register("property/search", SimplePropertySearchViewSet)
router.register("property/view", ViewPropertyDetailsViewSet)
router.register("property-image/upload", PropertyImageViewSet, basename="upload")
router.register("location", CurrentLocationViewSet, basename="location")

urlpatterns = router.urls
