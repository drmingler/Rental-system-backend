from rest_framework.routers import SimpleRouter

from rentalsystem.properties.views import (
    SimplePropertySearchViewSet,
    CurrentLocationViewSet,
    EditPropertyDetailsViewSet,
    ViewPropertyDetailsViewSet,
    PropertyImageViewSet,
)

router = SimpleRouter()
router.register("property/search", SimplePropertySearchViewSet)
router.register("location", CurrentLocationViewSet, basename="location")
router.register("property/view", ViewPropertyDetailsViewSet)
router.register("property/edit", EditPropertyDetailsViewSet)
router.register("property/upload", PropertyImageViewSet, basename="upload")

urlpatterns = router.urls
