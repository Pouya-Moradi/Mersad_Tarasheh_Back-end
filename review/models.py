from django.db import models
from store.models import Product


class Comment(models.Model):

    content = models.CharField(max_length=1023, verbose_name="متن نظر")

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name='کالا')

    is_approved = models.BooleanField(default=False, null=False, blank=False, verbose_name='وضعیت تایید نظر')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت')


class Rating(models.Model):


    score = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], default=1, verbose_name="امتیاز")

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings', verbose_name='کالا')
