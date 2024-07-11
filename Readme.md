Приложение с условным названием Pereval.

По ТЗ подразумевается, что пользователи, находясь где - то в походе, заносят в клиентское приложение данные об этом перевале.
Таким образом Федерация спортивного туризма России собирает данные о перевалах, для предоставления информации путешественникам, которые только планируют или хотят ознакомится с каким - то маршрутом и имеющимся на нем перевалах.
Турист через мобильное клиентское приложение отправляет на сервер определенные данные:


Информацию о себе:
Фамилия;
Имя;
Отчество;
Электронная почта;
Номер телефона.
Название объекта;
Координаты объекта и его высоту;
Уровень сложности в зависимости от времени года;
Несколько фотографий.

Клиент и сервер работают по принципу REST API и клиент отправляет запрос типа JSON, тем самым вызывая метод submitData, и с помощью WritableNestedModelSerializer десериализует его:

Метод: POST /api/submitData/

{
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "", //что соединяет, текстовое поле
 
  "add_time": "2021-09-22 13:18:13",
  "user": {"email": "qwerty@mail.ru", 		
        "fam": "Пупкин",
		 "name": "Василий",
		 "otc": "Иванович",
        "phone": "+7 555 55 55"}, 
 
   "coords":{
  "latitude": "45.3842",
  "longitude": "7.1525",
  "height": "1200"}
 
 
  level:{"winter": "", //Категория трудности. В разное время года перевал может иметь разную категорию трудности
  "summer": "1А",
  "autumn": "1А",
  "spring": ""},
 
   images: [{data:"<картинка1>", title:"Седловина"}, {data:"<картинка>", title:"Подъём"}]
}

В выполнения без ошибок, сервер возвращает:
{
    "status": 200,
    "massage": "OK",
    "id": 10
}

В случае неудач ответ зависит от ошибок, например:
{ "status": 500, "message": "Ошибка подключения к базе данных","id": null}

Метод GET /api/submitData/10/ возвращает созданный перевал с id = 10

Метод GET /api/submitData/?user__email=qwerty%40mail.ru возвращает все добавленные перевалы пользователя с email - qwerty@mail.ru

Метод PATCH /api/submitData/10/ изменяет данные о перевале пользователем, пока перевал имеет статус "new", так же пользователь не может менять данные о себе в этом запросе.


Автодокументация реализована с помощью библиотеки drf-yasg, доступные ендпоинты :

    path('swagger<format>\.json\.yaml', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

API и сериалайзер покрыты тестами на основе расширений django.test - TestCase
rest_framework.test-APITestCase в файле tests.py
Результат покрытия тестов собран библиотекой coverage 
Name                                                                                 Stmts   Miss  Cover
--------------------------------------------------------------------------------------------------------
manage.py                                                                               11      2    82%
pereval\__init__.py                                                                      0      0   100%
pereval\asgi.py                                                                          4      4     0%
pereval\settings.py                                                                     24      0   100%
pereval\urls.py                                                                         14      0   100%
pereval\wsgi.py                                                                          4      4     0%
tourism\__init__.py                                                                      0      0   100%
tourism\admin.py                                                                         1      0   100%
tourism\apps.py                                                                          4      0   100%
tourism\migrations\0001_initial.py                                                       6      0   100%
tourism\migrations\0002_remove_level_pereval_id_pereval_level_id_and_more.py             5      0   100%
tourism\migrations\0003_alter_pereval_connect.py                                         4      0   100%
tourism\migrations\0004_alter_pereval_coords_id_alter_pereval_level_id_and_more.py       5      0   100%
tourism\migrations\0005_rename_coords_id_pereval_coords_and_more.py                      4      0   100%
tourism\migrations\0006_rename_users_pereval_user.py                                     4      0   100%
tourism\migrations\0008_alter_imeges_title_alter_level_autumn_and_more.py                4      0   100%
tourism\migrations\0009_alter_pereval_status.py                                          4      0   100%
tourism\migrations\__init__.py                                                           0      0   100%
tourism\models.py                                                                       32      0   100%
tourism\serializers.py                                                                  38      0   100%
tourism\tests.py                                                                        58      0   100%
tourism\views.py                                                                         1      1     0%
tourism\viewsets.py                                                                     40      9    78%
--------------------------------------------------------------------------------------------------------
TOTAL                                                                                  272     20    93%


