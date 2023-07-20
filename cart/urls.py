from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register('carts', CartViewSet)
router.register('cart-items', CartItemViewSet, basename='cart-items')

urlpatterns = router.urls
