from datetime import datetime

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

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
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        message = ""
        for item in request.data["products"]:
            message += "User: {0}\n" \
                       "Title: {1}\n" \
                       "url: {2}\n" \
                       "----------\n".format(user, item["title"],
                                             "http://127.0.0.1:8000/api/v1/products/" + str(item["id"]))

        send_telegram(message)
        return Response(message)


class CustomOrder(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message = "Name: {0}\n" \
                  "Phone: {1}\n" \
                  "Email: {2}\n" \
                  "Auth_time: {3}:\n".format(request.data["name"], request.data["phone"], request.data["email"],
                                             datetime.now())
        send_telegram(message)
        return Response(message)


sets = [("styles", StylesViewSet), ("materials", MaterialsViewSet), ("colors", ColoursViewSet),
        ("handles", HandlesViewSet), ("photo", PhotoViewSet)]
