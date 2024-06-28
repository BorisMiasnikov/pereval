from .models import *
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'email', 'fam', 'name', 'otc', 'phone',
        )


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = (
            'latitude', 'longitude', 'hight',
        )


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = (
            'winter', 'summer', 'autumn', 'spring',
        )


class ImegesSerializer(serializers.ModelSerializer):
    data = serializers.URLField()
    class Meta:
        model = Imeges
        fields = (
            'data', 'title',
        )


# class PerevalSerializer(WritableNestedModelSerializer):# WritableNestedModelSerializer - библиотека для автоматической распаковки джасона
class PerevalSerializer(serializers.ModelSerializer): # ручная распаковка джасона
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    imeges = ImegesSerializer(many=True)
    add_data = serializers.DateTimeField(format= "%d-%m-%Y %H:%M:%S", read_only= True)
    class Meta:
        model = Pereval
        fields = (
            'beauty_title', 'title', 'other_titles', 'connect', 'add_data',
            'user', 'coords', 'level', 'imeges',
        )
    def create(self, validated_data, **kwargs):
        user_dict = validated_data.pop('user')
        coords_dict = validated_data.pop('coords')
        level_dict = validated_data.pop('level')
        imeges_list = validated_data.pop('imeges')

        # user_add = Users.objects.filter(email = user['email'])

        user = Users.objects.create(**user_dict)# ** - распаковывает словарь
        coords = Coords.objects.create(**coords_dict)
        level = Level.objects.create(**level_dict)
        pereval = Pereval.objects.create(
            **validated_data,
            user=user,
            coords=coords,
            level=level,
        )
        for imege in imeges_list:
            Imeges.objects.create(
                pereval = pereval,
                data=imege.pop("data"),
                title=imege.pop("title"),
            )
        return pereval
