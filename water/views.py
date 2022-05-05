from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.utils.translation import gettext_lazy
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework import exceptions
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_extensions.cache.decorators import cache_response
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .models import HX2021, HX2022, USensor, AlarmThreshold
from .serializers import HX2021Serializer, UserSerializer, HX2022Serializer, USensorSerializer, UserCreateSerializer, AlarmThresholdSerializer


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class HX2021ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HX2021.objects.all()
    serializer_class = HX2021Serializer
    # 分页
    pagination_class = CustomLimitOffsetPagination
    # 过滤
    filter_backends = [DjangoFilterBackend]
    # Note that using filterset_fields and filterset_class together is not supported.
    filterset_fields = '__all__'
    # 认证
    authentication_classes = [authentication.SessionAuthentication]
    # 权限
    permission_classes = [permissions.IsAuthenticated]


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class HX2022Filter(filters.FilterSet):
    udatetime = filters.IsoDateTimeFromToRangeFilter()

    class Meta:
        model = HX2022
        fields = '__all__'


class HX2022ViewSet(CacheResponseMixin, viewsets.ModelViewSet, HX2021ViewSet):
    queryset = HX2022.objects.all()
    serializer_class = HX2022Serializer
    # 权限
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # 认证
    # 去掉 csrf 验证，因为要在脚本中定时发送 POST 请求
    authentication_classes = [CsrfExemptSessionAuthentication]
    # 过滤
    filter_backends = [DjangoFilterBackend]
    # Note that using filterset_fields and filterset_class together is not supported.
    filterset_class = HX2022Filter

    @cache_response(key_func='list_cache_key_func', timeout=60)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class UserPermission(permissions.IsAdminUser):
    def has_permission(self, request, view):
        # 用户对自己的个人信息有 CRUD 权限
        try:
            if request.user.id == int(view.kwargs['pk']):
                return True
        except:
            pass

        # POST 接口允许匿名用户调用
        if view.action == 'create':
            return True
        return super().has_permission(request, view)


class MyBasicAuthentication(authentication.BasicAuthentication):
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        # 账号和密码验证成功
        user, _ = user_auth_tuple
        # 验证访问站点权限
        if not user.is_superuser and not user.extend.is_access:
            raise exceptions.AuthenticationFailed(gettext_lazy('无进入站点权限，请等待管理员审核'))
        if user_auth_tuple:
            login(request._request, user)
        return user_auth_tuple


class UserFilter(filters.FilterSet):
    is_access = filters.BooleanFilter(field_name='extend__is_access', lookup_expr='exact')

    class Meta:
        model = User
        fields = ['is_access']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # 去掉 csrf 验证
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [UserPermission]
    # 定制序列化
    serializer_action_classes = {
        'create': UserCreateSerializer,
    }
    # 过滤
    filter_backends = [DjangoFilterBackend]
    # Note that using filterset_fields and filterset_class together is not supported.
    # https://docs.djangoproject.com/zh-hans/4.0/topics/db/queries/#lookups-that-span-relationships-1
    filterset_fields = ['extend__is_access']

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    # 防止浏览器弹登录窗口
    def get_authenticate_header(self, request):
        return {}

    # session 相关接口 login 和 logout
    @action(detail=False,
            methods=['GET'],
            permission_classes=[permissions.IsAuthenticated],
            authentication_classes=[MyBasicAuthentication])
    def login(self, request, pk=None):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @action(detail=False,
            methods=['GET'],
            permission_classes=[permissions.IsAuthenticated],
            authentication_classes=[authentication.SessionAuthentication])
    def logout(self, request, pk=None):
        user = request.user
        logout(request._request)
        serializer = UserSerializer(user)
        return Response(serializer.data)


# GET /user 获取已经登录的用户
@api_view(['GET'])
@authentication_classes([authentication.SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def user(request):
    """ Get the authenticated user """

    instance = request.user
    serializer = UserSerializer(instance)
    return Response(serializer.data)


class USensorViewSet(CacheResponseMixin, viewsets.ReadOnlyModelViewSet):
    queryset = USensor.objects.all()
    serializer_class = USensorSerializer
    # 认证
    authentication_classes = [authentication.SessionAuthentication]
    # 权限
    permission_classes = [permissions.IsAuthenticated]
    # 分页
    pagination_class = CustomLimitOffsetPagination
    # 过滤
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    @cache_response(key_func='list_cache_key_func', timeout=600)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AlarmThresholdViewSet(viewsets.ModelViewSet):
    queryset = AlarmThreshold.objects.all()
    serializer_class = AlarmThresholdSerializer
    # 认证
    authentication_classes = [CsrfExemptSessionAuthentication]
    # 权限
    permission_classes = [permissions.IsAuthenticated]
    # 分页
    pagination_class = CustomLimitOffsetPagination
    # 过滤
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
