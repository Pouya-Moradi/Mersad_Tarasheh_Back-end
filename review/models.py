from django.db import models
from store.models import Product


class Comment(models.Model):

    content = models.CharField(max_length=1024)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    is_approved = models.BooleanField(default=False, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):

    score = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], default=1)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')

    created_at = models.DateTimeField(auto_now_add=True)