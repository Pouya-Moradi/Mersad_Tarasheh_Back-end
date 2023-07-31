from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'created_at']
    readonly_fields = ['created_at', 'created_at_jalali']
    list_per_page = 10
