from django.db import models


class Users(models.Model):
    email = models.EmailField(max_length=255)
    fam = models.CharField(max_length=255, default="Иванов")
    name = models.CharField(max_length=255, default="Иван")
    otc = models.CharField(max_length=255, default="Иванович")
    phone = models.CharField(max_length=255, default="8 800 555 35 35")


class Coords(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    hight = models.IntegerField(max_length=4)





class Pereval(models.Model):  # сущность объявления
    # атрибуты объявления
    beauty_title = models.CharField(max_length=255, default="пер.")
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, null=True)
    connect = models.CharField(max_length=255)
    add_time = models.DateTimeField(auto_now_add=True)
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    coords_id = models.ForeignKey(Coords, on_delete=models.CASCADE)

class Level(models.Model):
    winter = models.CharField(max_length=3, null=True)
    summer = models.CharField(max_length=3, null=True)
    autumn = models.CharField(max_length=3, null=True)
    spring = models.CharField(max_length=3, null=True)
    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE)

class Imeges(models.Model):
    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE)
    data = models.ImageField(upload_to='pereval/', nell=True, blank=True)
    title = models.CharField(max_length=255, null=True)
