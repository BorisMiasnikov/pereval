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
'''По умолчанию ModelSerializer не поддерживает создание или обновление объектов моделей вложенных сериалайзеров.
Для создания таких объектов мы явно указали метод create в PerevalSerializer. Для обновления объектов нужно также явно
указать метод update или воспользоваться drf_writable_nested, унаследовав PerevalSerializer от WritableNestedModelSerializer,
чтобы избавить себя от написания дополнительного функционала в ручную. Класс данной библиотеке возьмёт эту обязанность на себя.'''


class PerevalSerializer(WritableNestedModelSerializer):  # автоматическая распаковка джасона
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    imeges = ImegesSerializer(many=True)
    add_data = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Pereval
        fields = (
            'id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_data',
            'user', 'coords', 'level', 'imeges', 'status',
        )

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get("user")
            valudating_user_field = [
                instance_user.fam != data_user['fam'],
                instance_user.name != data_user['name'],
                instance_user.otc != data_user['otc'],
                instance_user.phone != data_user['phone'],
                instance_user.email != data_user['email'],
            ]
            if data_user is not None and any(valudating_user_field):
                raise serializers.ValidationError({"отклонено": "Нельзя менять данные пользователя"})
        return data

# class PerevalSerializer(serializers.ModelSerializer):  # ручная распаковка джасона
#     user = UsersSerializer()
#     coords = CoordsSerializer()
#     level = LevelSerializer()
#     imeges = ImegesSerializer(many=True)
#     add_data = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
#
#     class Meta:
#         model = Pereval
#         fields = (
#             'id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_data',
#             'user', 'coords', 'level', 'imeges', 'status',
#         )
#
#     def create(self, validated_data, **kwargs):
#         user_dict = validated_data.pop('user')
#         coords_dict = validated_data.pop('coords')
#         level_dict = validated_data.pop('level')
#         imeges_list = validated_data.pop('imeges')
#
#         # user_add = Users.objects.filter(email = user['email']) # тут может быть проверка, если пользователь уже существует
#
#         user = Users.objects.create(**user_dict)  # ** - распаковывает словарь
#         coords = Coords.objects.create(**coords_dict)
#         level = Level.objects.create(**level_dict)
#         pereval = Pereval.objects.create(
#             **validated_data,
#             user=user,
#             coords=coords,
#             level=level,
#         )
#         for imege in imeges_list:
#             Imeges.objects.create(
#                 pereval=pereval,
#                 data=imege.pop("data"),
#                 title=imege.pop("title"),
#             )
#         return pereval
#
#     def validate(self, data):
#         if self.instance is not None:
#             instance_user = self.instance.user
#             data_user = data.get("user")
#             valudating_user_field = [
#                 instance_user.fam != data_user['fam'],
#                 instance_user.name != data_user['name'],
#                 instance_user.otc != data_user['otc'],
#                 instance_user.phone != data_user['phone'],
#                 instance_user.email != data_user['email'],
#
#             ]
#             if data_user is not None and any(valudating_user_field):
#                 raise serializers.ValidationError({"отклонено": "Нельзя менять данные пользователя"})
#         return data