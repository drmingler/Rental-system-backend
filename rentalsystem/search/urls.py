from rest_framework.routers import SimpleRouter

from rentalsystem.search.views import PropertyDocumentView

router = SimpleRouter()
router.register("search", PropertyDocumentView, basename="propertyDocument")

urlpatterns = router.urls
