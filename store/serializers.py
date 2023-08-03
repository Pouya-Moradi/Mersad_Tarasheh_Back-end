from rest_framework import serializers
from .models import Collection, Product, ProductImage, ProductComment, ProductRating
from authentication.models import Customer


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']
        read_only_fields = ['created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']


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
                  'product_images', 'created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']
        read_only_fields = ['created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']


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
        fields = ['id', 'display_name', 'content', 'created_at', 'created_at_jalali']
        read_only_fields = ['created_at', 'created_at_jalali']


class ProductRatingSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductRating.objects.create(product_id=product_id, **validated_data)

    class Meta:
        model = ProductRating
        fields = ['id', 'score', 'created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']
        read_only_fields = ['created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']


class CreateOrUpdateProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = ['id', 'score', 'created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']
        read_only_fields = ['created_at', 'updated_at', 'created_at_jalali', 'updated_at_jalali']

    def create(self, validated_data):
        product_id = self.context['product_id']
        user_id = self.context['user_id']

        # Check if the user has already rated the product
        try:
            existing_rating = ProductRating.objects.get(product_id=product_id, customer__user_id=user_id)
            existing_rating.score = validated_data['score']
            existing_rating.save()
            return existing_rating
        except ProductRating.DoesNotExist:
            # If the user hasn't rated the product, create a new rating
            (customer, created) = Customer.objects.get_or_create(user_id=user_id)
            return ProductRating.objects.create(product_id=product_id, customer=customer, **validated_data)
