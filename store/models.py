from django.db import models
from django.utils import timezone
from jdatetime import datetime as jdatetime_datetime
from authentication.models import Customer


class Collection(models.Model):
    title = models.CharField(max_length=32, verbose_name='عنوان دسته بندی')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به روزرسانی')

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
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    title = models.CharField(max_length=64, verbose_name='عنوان محصول')
    description = models.CharField(max_length=255, blank=True, verbose_name='توضیحات')

    unit_price = models.DecimalField(max_digits=15, decimal_places=3, verbose_name='قیمت هرواحد')
    discount_percentage = models.DecimalField(blank=True, max_digits=5, decimal_places=2, default=0.0,
                                              verbose_name='درصد تخفیف')

    inventory = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name='تعداد موجودی در انبار')
    is_available = models.BooleanField(default=False, verbose_name='موجود بودن')

    is_featured = models.BooleanField(default=False, verbose_name='سفارشی بودن')

    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name='products',
                                   verbose_name='دسته بندی')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به روزرسانی')

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

        if self.inventory == 0:
            self.is_available = False;

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images', verbose_name='محصول')
    image = models.ImageField(upload_to='store/images', verbose_name='تصویر')

    class Meta:
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'تصاویر محصول'


class ProductComment(models.Model):
    content = models.CharField(max_length=1024, verbose_name='متن نظر')

    display_name = models.CharField(max_length=32, verbose_name='نام نمایشی')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name='محصول')

    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='comments', verbose_name='مشتری')

    is_approved = models.BooleanField(default=False, null=False, blank=False, verbose_name='وضعیت تایید')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    created_at_jalali = models.CharField(max_length=32, verbose_name='تاریخ شمسی ایجاد')

    def save(self, *args, **kwargs):
        if not self.id:
            now_local = timezone.localtime(timezone.now())
            now_jdatetime = jdatetime_datetime.fromgregorian(datetime=now_local)
            self.created_at_jalali = now_jdatetime.strftime('%Y/%m/%d %H:%M:%S')

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.title} | {self.display_name}'

    class Meta:
        verbose_name = 'نظر محصول'
        verbose_name_plural = 'نظرات محصول'


class ProductRating(models.Model):
    score = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], default=1, verbose_name='امتیاز')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings', verbose_name='محصول')

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='ratings', verbose_name='مشتری')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به روزرسانی')

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
        return f'{self.product.title} | {self.customer.__str__()}'

    class Meta:
        unique_together = [['product', 'customer']]
        verbose_name = 'امتیاز محصول'
        verbose_name_plural = 'امتیازات محصول'
