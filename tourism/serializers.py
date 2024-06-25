from .models import *
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'email', 'fam', 'name', 'otc', 'phone',
        ]


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'latitude', 'longitude', 'hight',
        ]


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'winter', 'summer', 'autumn', 'spring',
        ]


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'beauty_title', 'title', 'other_titles', 'connect',
            'users_id', 'coords_id', 'level_id', 'status',
        ]


class ImegesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'pereval_id', 'data', 'title',
        ]
