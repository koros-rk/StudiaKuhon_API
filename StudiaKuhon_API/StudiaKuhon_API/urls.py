from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from shop.product_gallery import ProductGallery
from .yasg import urlpatterns as doc_urls
from utils.views import sets, Messaging, CustomOrder
from shop.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
for title, VSet in sets:
    router.register(r""+title, VSet, basename=title)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/order', Messaging.as_view()),
    path('api/v1/customorder', CustomOrder.as_view()),
    path('api/v1/auth2', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/productgallery/', ProductGallery.as_view()),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),
]

urlpatterns += doc_urls
