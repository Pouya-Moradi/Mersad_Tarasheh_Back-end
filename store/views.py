from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Collection, Product, ProductImage, ProductComment, ProductRating
from .serializers import CollectionSerializer, ProductSerializer, ProductImageSerializer,\
    ProductCommentSerializer, ProductRatingSerializer


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def __delete__(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        if collection.products.count() > 0:
            return Response({'error': 'Collection contains some products and cannot be deleted'})
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related('product_images').all()
    serializer_class = ProductSerializer


class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])


class CommentViewSet(ModelViewSet):
    serializer_class = ProductCommentSerializer

    def get_queryset(self):
        return ProductComment.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}


class RatingViewSet(ModelViewSet):
    serializer_class = ProductRatingSerializer

    def get_queryset(self):
        return ProductRating.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

