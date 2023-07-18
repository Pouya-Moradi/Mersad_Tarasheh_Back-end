from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from utilities.constants import STATE_CHOICES


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, max_length=11)


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    display_name = models.CharField(max_length=64, null=False, blank=False)

    state = models.PositiveIntegerField(choices=STATE_CHOICES)
    city = models.CharField(max_length=32, null=False, blank=False)
    address = models.CharField(max_length=256, null=False, blank=False)
    zip_code = models.CharField(max_length=10, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
