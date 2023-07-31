from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import Collection, Product, ProductImage, ProductComment, ProductRating


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ''


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    inlines = [ProductImageInline]
    list_display = ['title', 'unit_price', 'discount_percentage', 'inventory', 'is_available', 'is_featured',
                    'collection', 'created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']
    readonly_fields = ['created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']
    list_editable = ['unit_price', 'discount_percentage', 'inventory', 'is_available', 'is_featured',
                     'collection']
    list_filter = ['collection']
    list_per_page = 10

    class Media:
        css = {
            'all': 'store/styles.css'
        }


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count', 'created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']
    readonly_fields = ['created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']
    search_fields = ['title']
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
            products_count=Count('products')
        )


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'is_approved', 'created_at', 'created_at_jalali']
    readonly_fields = ['created_at', 'created_at_jalali']
    list_editable = ['is_approved']
    list_filter = ['product']


@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['product', 'created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']
    readonly_fields = ['created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']
    list_filter = ['product']
