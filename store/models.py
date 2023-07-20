from django.db import models


class Collection(models.Model):

    title = models.CharField(max_length=32)

    created_at = models.CharField(max_length=31, null=True, blank=True)
    updated_at = models.CharField(max_length=31, null=True, blank=True)


class Product(models.Model):

    title = models.CharField(max_length=31)
    description = models.CharField(max_length=255, blank=True)

    unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    discount_percentage = models.DecimalField(blank=True, max_digits=5, decimal_places=2, default=0.0)

    inventory = models.PositiveSmallIntegerField(default=0, blank=True)
    is_available = models.BooleanField(default=True)

    is_featured = models.BooleanField(default=False, null=True)

    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name='products')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='store/images')