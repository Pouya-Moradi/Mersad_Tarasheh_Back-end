from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'discount_percentage', 'inventory', 'is_available', 'is_featured',
                    'collection', 'created_at', 'updated_at']
    list_editable = ['unit_price', 'discount_percentage', 'inventory', 'is_available', 'is_featured',
                     'collection']
    list_per_page = 10


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    list_editable = []
    list_per_page = 10
