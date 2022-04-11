from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS

from django.contrib.auth.models import User

from .models import HX2021, HX2022, USensor


class HX2021Serializer(serializers.ModelSerializer):

    class Meta:
        model = HX2021
        exclude = ['originalvalue', 'lasttime', 'valuestate', 'valuetype', 'lastvalue', 'flag']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']


class HX2022Serializer(HX2021Serializer):

    class Meta(HX2021Serializer.Meta):
        model = HX2022


class USensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = USensor
        fields = ['autoid', 'code', 'sensortypename', 'address']
