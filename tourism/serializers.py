from .models import *
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'email', 'fam', 'name', 'otc', 'phone',
        ]


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = [
            'latitude', 'longitude', 'hight',
        ]


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = [
            'winter', 'summer', 'autumn', 'spring',
        ]


class ImegesSerializer(serializers.ModelSerializer):
    data = serializers.URLField
    class Meta:
        model = Imeges
        fields = [
            'data', 'title',
        ]


class PerevalSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Pereval
        fields = [
            'beauty_title', 'title', 'other_titles', 'connect',
            'user', 'coords', 'level', 'imeges',
        ]

    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    imeges = ImegesSerializer(many=True)
