from rest_framework import viewsets
from .models import Palette, Style, Handle, Material, Photo
from .serializers import StyleSerializer, MaterialSerializer, ColourSerializer, HandleSerializer, PhotoSerializer
from django.conf import settings


class StylesViewSet(viewsets.ModelViewSet):
    serializer_class = StyleSerializer

    def get_queryset(self):
        queryset = Style.objects.all()
        return queryset


class MaterialsViewSet(viewsets.ModelViewSet):
    serializer_class = MaterialSerializer

    def get_queryset(self):
        queryset = Material.objects.all()
        return queryset


class ColoursViewSet(viewsets.ModelViewSet):
    serializer_class = ColourSerializer

    def get_queryset(self):
        queryset = Palette.objects.all()
        return queryset


class HandlesViewSet(viewsets.ModelViewSet):
    serializer_class = HandleSerializer

    def get_queryset(self):
        queryset = Handle.objects.all()
        return queryset


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = Photo.objects.all()
        return queryset


sets = [("styles", StylesViewSet), ("materials", MaterialsViewSet), ("colors", ColoursViewSet),
        ("handles", HandlesViewSet), ("photo", PhotoViewSet)]
