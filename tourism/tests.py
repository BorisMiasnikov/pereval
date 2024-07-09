from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from tourism.models import Pereval, Users, Coords, Level, Imeges
from tourism.serializers import PerevalSerializer

'''python manage.py test . - Запускает все тесты
 python manage.py test tourism.tests.PerevalApiTestCase.test_get_list - для запуска одного конкретного теста
 coverage run --source='.' manage.py test . - создает слепок .coverage, при изменении теста команду повторить
 coverage report - по слепку создает отчет в консоли
coverage html - создает папку htmlcov\index.html и в ней отчет
 '''


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        self.user_1 = Users.objects.create(email="try@try.ru", fam="Петрров", name="Петр", otc="Петрович",
                                           phone="88005553535")
        self.coords_1 = Coords.objects.create(latitude=45.3842, longitude=7.1525, hight=1200)
        self.level_1 = Level.objects.create(winter="1A", summer="1A", autumn="1A", spring="1A", )
        self.pereval_1 = Pereval.objects.create(beauty_title="perev.", title="123gora", connect="connect",
                                                user=self.user_1, coords=self.coords_1, level=self.level_1)
        self.imeges_1 = Imeges.objects.create(pereval=self.pereval_1, )

    def test_get_list(self):
        url = reverse("pereval-list")
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, ], many=True).data
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse("pereval-detail", args=(self.pereval_1.id,))
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_1).data
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)


class PerevalSerializerTestCase(TestCase):
    def setUp(self):
        self.user_1 = Users.objects.create(email="try@try.ru", fam="Петрров", name="Петр", otc="Петрович",
                                           phone="88005553535")
        self.coords_1 = Coords.objects.create(latitude=45.3842, longitude=7.1525, hight=1200)
        self.level_1 = Level.objects.create(winter="1A", summer="1A", autumn="1A", spring="1A", )
        self.pereval_1 = Pereval.objects.create(beauty_title="perev.", title="123gora", other_titles="pereval",
                                                connect="connect", user=self.user_1, coords=self.coords_1,
                                                level=self.level_1, )
        self.imeges_1 = Imeges.objects.create(pereval=self.pereval_1, data="https://www.yandex.ru/search.jpg",
                                              title="Седловина")
        self.imeges_1_2 = Imeges.objects.create(pereval=self.pereval_1, data="https://www.yandex.ru/search.jpg",
                                                title="Подъём")

    def test_check(self):
        serializer_data = PerevalSerializer(self.pereval_1).data
        expected_data = {
            "id": 3,
            "beauty_title": "perev.",
            "title": "123gora",
            "other_titles": "pereval",
            "connect": "connect",
            "user": {
                "email": "try@try.ru",
                "fam": "Петрров",
                "name": "Петр",
                "otc": "Петрович",
                "phone": "88005553535"
            },
            "coords": {
                "latitude": "45.38420000",
                "longitude": "7.15250000",
                "hight": 1200
            },
            "level": {
                "winter": "1A",
                "summer": "1A",
                "autumn": "1A",
                "spring": "1A"
            },
            "imeges": [
                {
                    "data": "https://www.yandex.ru/search.jpg",
                    "title": "Седловина"
                },
                {
                    "data": "https://www.yandex.ru/search.jpg",
                    "title": "Подъём"
                }
            ],
            "status": "new"
        }
        self.assertEquals(serializer_data, expected_data)
