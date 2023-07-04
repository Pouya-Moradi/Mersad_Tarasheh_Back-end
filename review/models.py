from django.db import models


class Comment(models.Model):

    content = models.CharField(max_length=1023, verbose_name="متن نظر")

    is_approved = models.BooleanField(default=False, null=False, blank=False, verbose_name="وضعیت تایید نظر")

    created_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان ثبت")


class Rating(models.Model):

    score = models.PositiveSmallIntegerField(choices=range(1, 6), default=1, verbose_name="امتیاز")