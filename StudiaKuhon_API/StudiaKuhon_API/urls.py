from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from utils.views import sets
from shop.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
for title, VSet in sets:
    router.register(r""+title, VSet, basename=title)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
