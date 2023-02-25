from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category, PartColor, Furniture
from .serializers import CategorySerializer, ColorSerializer, FurnitureSerializer
from .filters import FurnitureFilter
from shop.paginations import SetPaginationProducts


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset


class PartColorViewSet(viewsets.ModelViewSet):
    queryset = PartColor.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset


class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FurnitureFilter
    serializer_class = FurnitureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        product_obj = Furniture.objects.filter(~Q(id=instance.id), category=instance.category.id).order_by("?")[:5]
        related = []
        for k in product_obj:
            ser = self.get_serializer(k)
            related.append(ser.data)
        related_data = serializer.data
        related_data["related"] = related
        return Response(related_data)
