from rest_framework import serializers
from .models import Cart, CartItem
from store.models import Product


class CartItemProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']


class CartItemSerializer(serializers.ModelSerializer):
    product = CartItemProductSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart_item:CartItem):
        return cart_item.quantity * cart_item.product.unit_price

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    cart_items = CartItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart):
        sum([cart_item.quantity * cart_item.product.unit_price for cart_item in cart.cart_items.all()])

    class Meta:
        model = Cart
        fields = ['id', 'cart_items']

        read_only_fields = ['id']
