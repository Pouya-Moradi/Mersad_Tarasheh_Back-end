from rest_framework_nested import routers
from .views import CustomerViewSet

router = routers.DefaultRouter()

router.register('customer', CustomerViewSet)

urlpatterns = router.urls
