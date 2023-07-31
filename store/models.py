from django.db import models
from django.utils import timezone
from jdatetime import datetime as jdatetime_datetime
from authentication.models import Customer


class Collection(models.Model):
    title = models.CharField(max_length=32)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_at_jalali = models.CharField(max_length=32, null=True, blank=True, verbose_name='تاریخ شمسی ایجاد')
    updated_at_jalali = models.CharField(max_length=32, null=True, blank=True, verbose_name='تاریخ شمسی به روزرسانی')

    def __str__(self):
        return self.title

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

    class Meta:
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=31)
    description = models.CharField(max_length=255, blank=True)

    unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    discount_percentage = models.DecimalField(blank=True, max_digits=5, decimal_places=2, default=0.0)

    inventory = models.PositiveSmallIntegerField(default=0, blank=True)
    is_available = models.BooleanField(default=False)

    is_featured = models.BooleanField(default=False)

    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name='products')

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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='store/images')


class ProductComment(models.Model):
    content = models.CharField(max_length=1024)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='comments')

    is_approved = models.BooleanField(default=False, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)

    created_at_jalali = models.CharField(max_length=32, verbose_name='تاریخ شمسی ایجاد')

    def save(self, *args, **kwargs):
        if not self.id:
            now_local = timezone.localtime(timezone.now())
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at_jalali = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')

        super().save(*args, **kwargs)


class ProductRating(models.Model):
    score = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], default=1)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='ratings')

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

    class Meta:
        unique_together = [['product', 'customer']]
