from django.db import models
from django.utils import timezone
from jdatetime import datetime as jdatetime_datetime
from store.models import Product
from authentication.models import Customer


class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')

    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETED = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETED, 'Completed'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_at_jalali = models.CharField(max_length=32, verbose_name='تاریخ شمسی ایجاد')
    updated_at_jalali = models.CharField(max_length=32, verbose_name='تاریخ شمسی به روزرسانی')

    def save(self, *args, **kwargs):
        if not self.id:
            now_local = timezone.localtime(timezone.now())
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at_jalali = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
            self.updated_at_jalali = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')
        else:
            now_local = timezone.localtime(timezone.now())
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.updated_at_jalali = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')

        super().save(*args, **kwargs)


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='order_items')

    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')

    quantity = models.PositiveSmallIntegerField()

    unit_price = models.DecimalField(max_digits=15, decimal_places=3)
