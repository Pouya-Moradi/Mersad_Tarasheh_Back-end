from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.conf import settings
from utilities.constants import STATE_CHOICES
from django.core.validators import MinLengthValidator
from jdatetime import datetime as jdatetime_datetime
from django.utils import timezone


# from django.db.models.signals import post_save
# from django.dispatch import receiver


class User(AbstractUser):
    # first_name = models.CharField(max_length=32, verbose_name='نام')
    # last_name = models.CharField(max_length=32, verbose_name='نام خانوادگی')

    # email = models.EmailField(unique=True, verbose_name='ایمیل')

    phone_number = models.CharField(unique=True, max_length=11, validators=[MinLengthValidator(11)],
                                    verbose_name='شماره تلفن همراه')


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='کاربر')

    # display_name = models.CharField(max_length=64, null=True, blank=True, verbose_name='نام نمایشی')

    # state = models.PositiveIntegerField(choices=STATE_CHOICES, null=True, blank=True, verbose_name='استان')
    # city = models.CharField(max_length=32, null=True, blank=True, verbose_name='شهر')
    # address = models.CharField(max_length=256, null=True, blank=True, verbose_name='آدرس')
    # zip_code = models.CharField(max_length=10, null=True, blank=True, verbose_name='کد پستی')

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
        return f'{self.user.username}'

    @admin.display(ordering='user__username')
    def username(self):
        return self.user.username

    # @admin.display(ordering='user__first_name')
    # def first_name(self):
    #     return self.user.first_name
    #
    # @admin.display(ordering='user__last_name')
    # def last_name(self):
    #     return self.user.last_name

    # # this method to generate profile when user is created
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Customer.objects.create(user=instance)
    #
    # # this method to update profile when user is updated
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'
