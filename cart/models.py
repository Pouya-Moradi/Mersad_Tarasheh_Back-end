from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from uuid import uuid4
from jdatetime import datetime as jdatetime_datetime
from store.models import Product
from authentication.models import Customer


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    created_at_jalali = models.CharField(max_length=32, verbose_name='تاریخ شمسی ایجاد')

    def save(self, *args, **kwargs):
        if not self.id:
            now_local = timezone.localtime(timezone.now())
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at_jalali = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name='سبد خرید'
        verbose_name_plural='سبدهای خرید'


class CartItem(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items', verbose_name='سبد خرید')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')

    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], verbose_name='تعداد')

    class Meta:
        unique_together = [['cart', 'product']]
        verbose_name='آیتم سبد خرید'
        verbose_name_plural='آیتم های سبد خرید'
