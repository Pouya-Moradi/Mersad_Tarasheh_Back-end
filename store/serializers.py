from rest_framework import serializers
from .models import Collection, Product, ProductImage


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ProductImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductImage.objects.create(product_id=product_id, **validated_data)

    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)

    # def create(self, validated_data):
    #     product_images_data = validated_data.pop('product_images', [])
    #     product = Product.objects.create(**validated_data)
    #
    #     for image_data in product_images_data:
    #         ProductImage.objects.create(product=product, **image_data)
    #
    #     return product

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'unit_price', 'discount_percentage', 'is_available', 'collection',
                  'product_images', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
