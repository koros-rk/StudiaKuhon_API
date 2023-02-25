from rest_framework.pagination import PageNumberPagination


class SetPaginationProducts(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class SetPaginationFurniture(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
