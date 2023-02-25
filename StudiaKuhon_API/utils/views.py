from datetime import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi

from .messaging import send_telegram
from .models import Palette, Style, Handle, Material, Photo
from .serializers import StyleSerializer, MaterialSerializer, ColourSerializer, HandleSerializer, PhotoSerializer


class StylesViewSet(viewsets.ModelViewSet):
    serializer_class = StyleSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Style.objects.all()
        return queryset


class MaterialsViewSet(viewsets.ModelViewSet):
    serializer_class = MaterialSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Material.objects.all()
        return queryset


class ColoursViewSet(viewsets.ModelViewSet):
    serializer_class = ColourSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Palette.objects.all()
        return queryset


class HandlesViewSet(viewsets.ModelViewSet):
    serializer_class = HandleSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Handle.objects.all()
        return queryset


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Photo.objects.all()
        return queryset


class Messaging(APIView):
    renderer_classes = [JSONRenderer]

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Order message'),
            'user': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Product title'),
        }))
    def post(self, request):
        message = request.data['message']
        if request.data['user']:
            user = request.user
            send_telegram("User: " + user.username + "\n" + message)
            return Response(status=200)
        else:
            send_telegram(message)
            return Response(status=200)


sets = [("styles", StylesViewSet), ("materials", MaterialsViewSet), ("colors", ColoursViewSet),
        ("handles", HandlesViewSet), ("photo", PhotoViewSet)]
