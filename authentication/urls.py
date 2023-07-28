from rest_framework_nested import routers
from .views import CustomerViewSet

router = routers.DefaultRouter()

router.register('customers', CustomerViewSet)

urlpatterns = router.urls
