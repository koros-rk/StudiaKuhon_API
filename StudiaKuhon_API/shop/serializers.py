from rest_framework import serializers
from .models import Product
from utils.serializers import TagListingField


class ProductSerializer(serializers.ModelSerializer):
    gallery = TagListingField(many=True, read_only=True)
    styles = TagListingField(many=True, read_only=True)
    colours = TagListingField(many=True, read_only=True)
    materials = TagListingField(many=True, read_only=True)
    handle = TagListingField(read_only=True)
    main_colour = TagListingField(read_only=True)
    main_style = TagListingField(read_only=True)
    main_material = TagListingField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description_shorted', 'description_full', 'main_photo', 'thumbnail_photo', 'gallery',
                  'styles', 'colours', 'materials', 'handle', 'main_colour', 'main_style', 'main_material',)
