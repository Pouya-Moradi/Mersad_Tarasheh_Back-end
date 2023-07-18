from django.db import models


class Collection(models.Model):

    title = models.CharField(max_length=32, verbose_name="عنوان دسته بندی")

    created_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان ثبت")
    updated_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان به روزرسانی")


class Product(models.Model):

    title = models.CharField(max_length=31, verbose_name="نام")
    description = models.CharField(max_length=255, blank=True, verbose_name='توضیحات')

    unit_price = models.DecimalField(max_digits=15, decimal_places=3, verbose_name='قیمت')
    discount_percentage = models.DecimalField(blank=True, max_digits=5, decimal_places=2, default=0.0,
                                              verbose_name='درصد تخفیف')

    inventory = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name='تعداد موجودی')
    is_available = models.BooleanField(default=True, verbose_name='موجود بودن')

    is_featured = models.BooleanField(default=False, null=True, verbose_name='پیشنهادی بودن')

    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name='products',
                                   verbose_name='دسته بندی')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='زمان به روزرسانی')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='store/images')