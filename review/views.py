from rest_framework.viewsets import ModelViewSet
from .models import Comment, Rating
from .serializers import CommentSerializer, RatingSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
