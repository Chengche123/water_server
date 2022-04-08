from django.contrib.auth import login
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .models import HX2021
from .serializers import HX2021Serializer, UserSerializer


class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class MyBasicAuthentication(authentication.BasicAuthentication):
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        # 如果认证成功，返回 cookie
        if user_auth_tuple:
            user, _ = user_auth_tuple
            login(request._request, user)
        return user_auth_tuple


class HX2021ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HX2021.objects.all()
    serializer_class = HX2021Serializer
    # 分页
    pagination_class = BookLimitOffsetPagination
    # 过滤
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    # 认证
    authentication_classes = [authentication.SessionAuthentication, MyBasicAuthentication]
    # 权限
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_authenticate_header(self, request):
        return {}

    @action(detail=False,
            methods=['GET'],
            permission_classes=[permissions.IsAuthenticated],
            authentication_classes=[MyBasicAuthentication])
    def login(self, request, pk=None):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([authentication.SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def user(request):
    """ Get the authenticated user """

    instance = request.user
    serializer = UserSerializer(instance)
    return Response(serializer.data)
