from rest_framework.routers import SimpleRouter

from rentalsystem.properties.views import (
    SimplePropertySearchViewSet,
    CurrentLocationViewSet,
)

router = SimpleRouter()
router.register("properties", SimplePropertySearchViewSet)
router.register("location", CurrentLocationViewSet, basename="location")

urlpatterns = router.urls
