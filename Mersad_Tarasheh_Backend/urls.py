"""
URL configuration for Mersad_Tarasheh_Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from cart.views import CartViewSet, CartItemViewSet
from store.views import CollectionViewSet, ProductViewSet, ProductImageViewSet
from review.views import CommentViewSet, RatingViewSet
from order.views import OrderViewSet, OrderItemViewSet
from store.urls import router as product_router


admin.site.site_header = 'Mersad Tarasheh Admin'
admin.site.index_title = 'Admin'


router = routers.DefaultRouter()
router.register('carts', CartViewSet)
carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('cart-items', CartItemViewSet, basename='cart-items')

router.registry.extend(product_router.registry)


router.register('collections', CollectionViewSet)
# router.register('products', ProductViewSet)
# products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
# products_router.register('product-comments', CommentViewSet, basename='product-comments')
# products_router.register('product-ratings', RatingViewSet, basename='product-ratings')
# products_router.register('product-images', ProductImageViewSet, basename='product-images')


router.register('orders', OrderViewSet, basename='orders')
orders_router = routers.NestedDefaultRouter(router, 'orders', lookup='order')
orders_router.register('orde-items', OrderItemViewSet, basename='order-items')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('authentication/', include('authentication.urls')),
    # path('carts/', include('cart.urls')),
    # path('order/', include('order.urls')),
    # path('review/', include('review.urls')),
    # path('store/', include('store.urls')),
    path('', router.urls)
] + router.urls + carts_router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
