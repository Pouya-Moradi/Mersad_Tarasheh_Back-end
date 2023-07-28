from rest_framework.viewsets import ModelViewSet
from .models import Comment, Rating
from .serializers import CommentSerializer, RatingSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}


class RatingViewSet(ModelViewSet):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
