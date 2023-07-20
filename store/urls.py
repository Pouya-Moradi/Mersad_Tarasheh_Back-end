from rest_framework_nested import routers
from .views import CollectionViewSet, ProductViewSet, ProductImageViewSet

router = routers.DefaultRouter()

router.register('collections', CollectionViewSet)

router.register('products', ProductViewSet)
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('product-images', ProductImageViewSet, basename='product-images')


urlpatterns = router.urls + products_router.urls
