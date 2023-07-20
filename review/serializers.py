from rest_framework import serializers
from .models import Comment, Rating


class CommentSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Comment.objects.create(product_id=product_id, **validated_data)

    class Meta:
        model = Comment
        fields = ['id', 'content']


class RatingSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Rating.objects.create(product_id=product_id, **validated_data)

    class Meta:
        model = Rating
        fields = ['id', 'score']
