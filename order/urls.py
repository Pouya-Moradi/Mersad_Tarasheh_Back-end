from rest_framework_nested import routers
from .views import OrderViewSet, OrderItemViewSet


router = routers.DefaultRouter()


router.register('orders', OrderViewSet, basename='orders')
orders_router = routers.NestedDefaultRouter(router, 'orders', lookup='order')
orders_router.register('order-items', OrderItemViewSet, basename='order-items')