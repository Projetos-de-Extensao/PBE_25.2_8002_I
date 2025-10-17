from rest_framework.routers import DefaultRouter
from .views import ContentViewSet

router = DefaultRouter()
router.register('contents', ContentViewSet)

urlpatterns = router.urls