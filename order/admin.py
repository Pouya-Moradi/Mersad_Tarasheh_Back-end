from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment_status', 'customer', 'created_at', 'updated_at']
    list_editable = ['payment_status']
    list_per_page = 10
