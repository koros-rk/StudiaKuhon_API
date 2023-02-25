from rest_framework import serializers
from rest_framework.utils import model_meta

from .models import PartColor, Category, Furniture


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', )


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartColor
        fields = ('title', )


class FurnitureSerializer(serializers.ModelSerializer):
    obj_dict = {
        'colors': PartColor.objects,
        'category': Category.objects,
    }

    colors = ColorSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Furniture
        fields = ('title', 'description_short', 'description_full', 'size', 'price', 'colors', 'category', )

    def create(self, validated_data):
        new_item = Furniture.objects.create(
            title=validated_data['title'],
            description_short=validated_data['description_short'],
            description_full=validated_data['description_full'],
            size=validated_data['size'],
            price=validated_data['price'],
            category=Category.objects.get(title=validated_data['category']['title'])
        )

        for color in validated_data['colors']:
            color_obj = PartColor.objects.get_or_create(title=color['title'])[0].id
            new_item.colors.add(color_obj)

        serializer = FurnitureSerializer(new_item)
        return serializer.data

    def update(self, instance, validated_data):
        info = model_meta.get_field_info(instance)

        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            elif attr in info.relations:
                for k, v in value.items():
                    setattr(instance, attr, self.obj_dict[attr].get(title=v))
            else:
                setattr(instance, attr, value)

        instance.save()

        for attr, value in m2m_fields:
            for i in value:
                for k, v in i.items():
                    if attr == 'colors':
                        instance.colors.add(PartColor.objects.get_or_create(title=v)[0].id)

        return instance
