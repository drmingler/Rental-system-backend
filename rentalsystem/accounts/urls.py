from rest_framework.routers import SimpleRouter
from rentalsystem.accounts.views import UserProfileViewSet

router = SimpleRouter()
router.register("accounts", UserProfileViewSet)

urlpatterns = router.urls
