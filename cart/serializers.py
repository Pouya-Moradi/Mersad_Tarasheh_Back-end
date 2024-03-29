from django.core.validators import MinValueValidator
from rest_framework import serializers
from .models import Cart, CartItem
from store.models import Product
from store.serializers import SimpleProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.unit_price

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    cart_items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart):
        sum([cart_item.quantity * cart_item.product.unit_price for cart_item in cart.cart_items.all()])

    class Meta:
        model = Cart
        fields = ['id', 'cart_items', 'total_price', 'created_at', 'created_at_jalali']
        read_only_fields = ['created_at', 'created_at_jalali']


class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value):
            raise serializers.ValidationError('No product with the given ID was found')
        return value

    def validate_quantity(self, value):
        product_id = self.initial_data.get('product_id')  # Access from initial_data
        product = Product.objects.get(pk=product_id)

        if value > product.inventory:
            raise serializers.ValidationError(f"Requested quantity exceeds available inventory for {product.title}.")

        return value

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)

        return self.instance

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']
