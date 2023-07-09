from django.db import models
from uuid import uuid4
from store.models import Product


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items', verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    quantity = models.PositiveSmallIntegerField(verbose_name='تعداد')

    class Meta:
        unique_together = [['cart', 'product']]
