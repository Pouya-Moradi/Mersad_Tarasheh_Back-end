from django.db import models


class Collection(models.Model):

    title = models.CharField(max_length=32, verbose_name="عنوان دسته بندی")

    created_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان ثبت")
    updated_at = models.CharField(max_length=31, null=True, blank=True, verbose_name="زمان به روزرسانی")

    class Meta:
        verbose_name_plural = "دسته بندی ها"
        verbose_name = "دسته بندی"