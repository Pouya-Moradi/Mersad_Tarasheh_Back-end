from rest_framework.viewsets import ModelViewSet
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order
    serializer_class = OrderSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem
    serializer_class = OrderItemSerializer
