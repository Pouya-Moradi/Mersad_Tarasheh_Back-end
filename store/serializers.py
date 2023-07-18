from rest_framework import serializers
from .models import Collection, Product, ProductImage


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'unit_price', 'discount_percentage', 'is_available', 'collection',
                  'created_at', 'updated_at']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']