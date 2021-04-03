from rest_framework.routers import SimpleRouter

from rentalsystem.properties.views import (
    SimplePropertySearchViewSet,
    CurrentLocationViewSet,
    EditPropertyDetailsViewSet,
    ViewPropertyDetailsViewSet,
    ImageUploadViewSet,
)

router = SimpleRouter()
router.register("property/search", SimplePropertySearchViewSet)
router.register("location", CurrentLocationViewSet, basename="location")
router.register("property/view", ViewPropertyDetailsViewSet)
router.register("property/edit", EditPropertyDetailsViewSet)
router.register("property/upload", ImageUploadViewSet, basename="upload")

urlpatterns = router.urls
