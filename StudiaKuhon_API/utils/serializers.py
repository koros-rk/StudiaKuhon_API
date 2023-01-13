from abc import ABC
from rest_framework import serializers
from django.conf import settings

from .models import *


class PhotoListingField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return value.url


class TagListingField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return value.title


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ('title', )


class ColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = ('title', )


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('title', )


class HandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handle
        fields = ('title', )


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('url', )


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('username', 'email', 'id')
