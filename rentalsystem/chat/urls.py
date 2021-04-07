from rest_framework.routers import SimpleRouter

from rentalsystem.chat.views import ConversationViewSet, LastMessagesViewSet

router = SimpleRouter()
router.register("conversation", ConversationViewSet, basename="chat")
router.register("last-message", LastMessagesViewSet, basename="last_message")

urlpatterns = router.urls
