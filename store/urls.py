from rest_framework_nested import routers
from .views import CollectionViewSet, ProductViewSet, ProductImageViewSet
from review.views import CommentViewSet, RatingViewSet

router = routers.DefaultRouter()

router.register('collections', CollectionViewSet)

router.register('products', ProductViewSet)
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('product-comments', CommentViewSet, basename='product-comments')
products_router.register('product-ratings', RatingViewSet, basename='product-ratings')
products_router.register('product-images', ProductImageViewSet, basename='product-images')


urlpatterns = router.urls + products_router.urls
