from rest_framework.routers import SimpleRouter

from rentalsystem.properties.views import (
    SimplePropertySearchViewSet,
    CurrentLocationViewSet,
    EditPropertyDetailsViewSet,
    ViewPropertyDetailsViewSet,
)

router = SimpleRouter()
router.register("property/search", SimplePropertySearchViewSet)
router.register("location", CurrentLocationViewSet, basename="location")
router.register("property/view", ViewPropertyDetailsViewSet)
router.register("property/edit", EditPropertyDetailsViewSet)

urlpatterns = router.urls
