from rest_framework_nested import routers
from .views import CartViewSet, CartItemViewSet

router = routers.DefaultRouter()
# router.register('carts', CartViewSet)
router.register('', CartViewSet)
# carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router = routers.NestedDefaultRouter(router, '', lookup='cart')
carts_router.register('cart-items', CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + carts_router.urls
