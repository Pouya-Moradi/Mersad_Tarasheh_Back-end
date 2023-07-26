from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse

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
    list_display = ['title', 'products_count', 'created_at', 'updated_at']
    list_per_page = 10

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = reverse('admin:store_product_changelist') + '?' + urlencode(
            {
                'collection__id': str(collection.id)
            }
        )
        return format_html('<a href="{}">{}</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('products')
        )
