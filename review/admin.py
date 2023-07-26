from django.contrib import admin
from .models import Comment, Rating


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'is_approved', 'created_at']
    list_editable = ['is_approved']
    list_filter = ['product']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['product', 'created_at']
    list_filter = ['product']