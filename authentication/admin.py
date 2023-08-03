from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import User, Customer


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    search_fields = ['username']
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'password1', 'password2', 'email', 'phone_number', 'first_name', 'last_name'),
            },
        ),
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['first_name', 'last_name', 'display_name', 'state', 'city', 'orders_count', 'created_at',
                    'updated_at', 'created_at_jalali', 'updated_at_jalali']
    readonly_fields = ['created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['user__first_name__istartswith', 'user__last_name__istartswith']
    list_per_page = 10

    @admin.display(ordering='orders_count')
    def orders_count(self, customer):
        url = reverse('admin:order_order_changelist') + '?' + urlencode(
            {
                'customer__id': str(customer.id)
            }
        )
        return format_html('<a href="{}">{}</a>', url, customer.orders_count)

    # @admin.display(ordering='comments_count')
    # def comments_count(self, customer):
    #     url = reverse('admin:review_comment_changelist') + '?' + urlencode(
    #         {
    #             'customer__id': str(customer.id)
    #         }
    #     )
    #     return format_html('<a href="{}">{}</a>', url, customer.comments_count)
    #
    # @admin.display(ordering='ratings_count')
    # def ratings_count(self, customer):
    #     url = reverse('admin:review_rating_changelist') + '?' + urlencode(
    #         {
    #             'customer__id': str(customer.id)
    #         }
    #     )
    #     return format_html('<a href="{}">{}</a>', url, customer.ratings_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count=Count('orders'),
            # comments_count=Count('comments'),
            # ratings_count=Count('ratings')
        )
