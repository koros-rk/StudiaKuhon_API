from rest_framework import viewsets
from .models import *
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all().filter(show=True)
        return queryset
