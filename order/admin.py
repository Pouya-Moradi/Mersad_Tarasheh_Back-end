from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment_status', 'customer', 'created_at', 'updated_at', 'created_at_jalali',
                    'updated_at_jalali']
    readonly_fields = ['created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']
    list_editable = ['payment_status']
    list_per_page = 10
