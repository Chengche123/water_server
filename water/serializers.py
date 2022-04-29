from numpy import source
from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import HX2021, HX2022, USensor, UserExtend, AlarmThreshold


class HX2021Serializer(serializers.ModelSerializer):

    class Meta:
        model = HX2021
        exclude = ['originalvalue', 'lasttime', 'valuestate', 'valuetype', 'lastvalue', 'flag']


class UserSerializer(serializers.ModelSerializer):
    # 只读字段
    is_superuser = serializers.ReadOnlyField()
    # 手机号
    telephone_number = serializers.CharField(source="extend.telephone_number", required=False)
    # is_access 只读
    is_access = serializers.ReadOnlyField(source='extend.is_access')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'telephone_number', 'is_superuser', 'is_access']


# 创建用户时的字段
class UserCreateSerializer(UserSerializer):

    # AssertionError: The `.create()` method does not support writable dotted-source fields by default.
    # Write an explicit `.create()` method for serializer `water.serializers.UserCreateSerializer`,
    # or set `read_only=True` on dotted-source serializer fields.
    def create(self, validated_data):
        # 从已验证数据中取出 extend 字段
        extend = validated_data.get('extend', {})
        if extend:
            del validated_data['extend']

        validated_data['password'] = make_password(validated_data['password'])
        user = User(**validated_data)
        user.save()

        user_extend = UserExtend(user=user, **extend)
        user_extend.save()

        return user

    class Meta(UserSerializer.Meta):
        fields = ['username', 'password', 'email', 'telephone_number']


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
