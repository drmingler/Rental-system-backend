from rest_framework.routers import SimpleRouter

from rentalsystem.properties.views import SimplePropertySearchViewSet

router = SimpleRouter()
router.register("properties", SimplePropertySearchViewSet)

urlpatterns = router.urls
