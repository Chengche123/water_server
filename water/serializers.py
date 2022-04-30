from rest_framework import serializers
from rest_framework.fields import empty
from drf_writable_nested.mixins import UniqueFieldsMixin
from drf_writable_nested.serializers import WritableNestedModelSerializer


from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import HX2021, HX2022, USensor, UserExtend, AlarmThreshold


class HX2021Serializer(serializers.ModelSerializer):

    class Meta:
        model = HX2021
        exclude = ['originalvalue', 'lasttime', 'valuestate', 'valuetype', 'lastvalue', 'flag']


class UserExtendSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExtend
        exclude = ['user', 'id']


# 匿名用户注册时不能改变 is_access 字段
class UserExtendCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExtend
        exclude = ['user', 'id', 'is_access']

    def get_value(self, dictionary):
        # 在创建用户时，不带 extend 字段也会创建一个该模型的实例
        value = super().get_value(dictionary)
        if value == empty:
            return {}
        return value


class UserSerializer(WritableNestedModelSerializer):
    # 只读字段
    is_superuser = serializers.ReadOnlyField()
    # 可写 extend
    extend = UserExtendSerializer(many=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superuser', 'is_staff', 'extend']


# 创建用户时的字段
class UserCreateSerializer(UserSerializer):

    extend = UserExtendCreateSerializer(many=False)

    class Meta(UserSerializer.Meta):
        fields = ['username', 'password', 'email', 'extend']

    # 密码加盐
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class HX2022Serializer(HX2021Serializer):

    class Meta(HX2021Serializer.Meta):
        model = HX2022


class USensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = USensor
        fields = ['autoid', 'code', 'sensortypename', 'address', 'measurename']


class AlarmThresholdSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlarmThreshold
        fields = '__all__'
