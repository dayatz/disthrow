from django.db import models


class Distro(models.Model):
    name = models.CharField(max_length=25)
    owner = models.CharField(max_length=25)

    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    fb = models.CharField(max_length=15)
    tw = models.CharField(max_length=15)

    lng = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)


    def __str__(self):
        return self.name

