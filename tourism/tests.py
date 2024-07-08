from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

from tourism.models import Pereval, Users, Coords, Level, Imeges
from tourism.serializers import PerevalSerializer


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        self.user_1 = Users.objects.create(email="try@try.ru", fam = "Петрров", name = "Петр", otc= "Петрович", phone = "88005553535")
        self.coords_1 = Coords.objects.create(latitude=45.3842, longitude = 7.1525, height = 1200)
        self.level_1 = Level.objects.create(winter= "1A", summer= "1A", autumn= "1A", spring= "1A",)
        self.pereval_1 = Pereval.objects.create(beauty_title= "perev.", title= "123gora", connect= "connect", user= self.user_1, coords= self.coords_1, level = self.level_1)
        self.imeges_1 = Imeges.objects.create(pereval=self.pereval_1,)

    def test_get_list(self):
        url = reverse("pereval-list")
        response = self.client.get(url)
        serializer_data = PerevalSerializer([])