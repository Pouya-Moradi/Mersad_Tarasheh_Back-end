from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Cart
from .serializers import CartSerializer


class CartViewSet(CreateModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
