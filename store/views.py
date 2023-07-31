from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Collection, Product, ProductImage, ProductComment, ProductRating
from .serializers import CollectionSerializer, ProductSerializer, ProductImageSerializer,\
    ProductCommentSerializer, ProductRatingSerializer, UpdateProductRatingSerializer
from permissions import IsAdminOrReadOnly


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAdminOrReadOnly]

    def __delete__(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        if collection.products.count() > 0:
            return Response({'error': 'Collection contains some products and cannot be deleted'})
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related('product_images').all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])


class ProductCommentViewSet(ModelViewSet):
    serializer_class = ProductCommentSerializer

    def get_queryset(self):
        return ProductComment.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}


class ProductRatingViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def get_queryset(self):
        return ProductRating.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return UpdateProductRatingSerializer
        return ProductRatingSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

