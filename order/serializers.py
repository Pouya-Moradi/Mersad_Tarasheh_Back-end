from django.db import transaction
from rest_framework import serializers
from .models import Order, OrderItem
from authentication.models import Customer
from cart.models import Cart, CartItem
from store.serializers import SimpleProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'unit_price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'state', 'city', 'address', 'zip_code', 'payment_status', 'order_items', 'created_at',
                  'updated_at',
                  'created_at_jalali', 'updated_at_jalali']


class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    state = serializers.CharField(max_length=32)
    city = serializers.CharField(max_length=32)
    address = serializers.CharField(max_length=256)
    zip_code = serializers.CharField(max_length=10)

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('No cart with the given ID was found.')
        if CartItem.objects.filter(cart_id=cart_id).count() == 0:
            raise serializers.ValidationError('The cart is empty.')
        return cart_id

    def validate(self, data):
        cart_id = data['cart_id']
        cart_items = CartItem.objects.select_related('product').filter(cart_id=cart_id)

        for cart_item in cart_items:
            product = cart_item.product
            if cart_item.quantity > product.inventory:
                raise serializers.ValidationError(
                    f"Requested quantity for product {product.title} exceeds available inventory.")
        return data

    def save(self, **kwargs):
        with transaction.atomic():
            cart_id = self.validated_data['cart_id']
            state = self.validated_data['state']
            city = self.validated_data['city']
            address = self.validated_data['address']
            zip_code = self.validated_data['zip_code']

            customer = Customer.objects.get(user_id=self.context['user_id'])
            order = Order.objects.create(customer=customer, state=state, city=city, address=address, zip_code=zip_code)

            cart_items = CartItem.objects.select_related('product').filter(cart_id=self.validated_data['cart_id'])

            order_items = []
            for cart_item in cart_items:
                product = cart_item.product
                order_item = OrderItem(
                    order=order,
                    product=product,
                    unit_price=product.unit_price,
                    quantity=cart_item.quantity
                )
                order_items.append(order_item)

                # Decrease product inventory
                product.inventory -= cart_item.quantity
                product.save()

            OrderItem.objects.bulk_create(order_items)

            Cart.objects.filter(pk=cart_id).delete()

            return order


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['payment_status']
