from rest_framework.routers import SimpleRouter

from rentalsystem.properties.views import (
    SimplePropertySearchViewSet,
    CurrentLocationViewSet,
    PropertyDetailsViewSet,
    ViewPropertyDetailsViewSet,
    PropertyMediaUploadViewSet,
)

router = SimpleRouter()
router.register("property", PropertyDetailsViewSet)
router.register("property-search", SimplePropertySearchViewSet)
router.register("property-view", ViewPropertyDetailsViewSet)
router.register("property-media-upload", PropertyMediaUploadViewSet, basename="upload")
router.register("location", CurrentLocationViewSet, basename="location")

urlpatterns = router.urls
