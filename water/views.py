from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import HX2021
from .serializers import HX2021Serializer


class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class HX2021ViewSet(viewsets.ModelViewSet):
    queryset = HX2021.objects.all()
    serializer_class = HX2021Serializer
    # 分页
    pagination_class = BookLimitOffsetPagination
    # 过滤
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
