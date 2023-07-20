from django.core.validators import MinValueValidator
from django.db import models
from uuid import uuid4
from store.models import Product
from authentication.models import Customer


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        unique_together = [['cart', 'product']]
