from django_filters import rest_framework as filters
from .models import Furniture


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class FurnitureFilter(filters.FilterSet):
    furniture = CharFilterInFilter(field_name="furniture__title", lookup_expr="in")

    class Meta:
        model = Furniture
        fields = ['furniture']
