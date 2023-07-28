from rest_framework import serializers
from .models import Collection, Product, ProductImage, ProductComment, ProductRating


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

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'unit_price', 'discount_percentage', 'is_available', 'collection',
                  'product_images', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']


class ProductCommentSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductComment.objects.create(product_id=product_id, **validated_data)

    class Meta:
        model = ProductComment
        fields = ['id', 'content']


class ProductRatingSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductRating.objects.create(product_id=product_id, **validated_data)

    class Meta:
        model = ProductRating
        fields = ['id', 'score']
