from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Customer


@admin.register(User)
class UserAdmin(BaseUserAdmin):
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
    list_display = ['first_name', 'last_name', 'created_at', 'updated_at']
    list_editable = []
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    list_per_page = 10
