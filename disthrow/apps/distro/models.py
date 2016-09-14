from django.db import models


class Distro(models.Model):
    name = models.CharField(max_length=25)
    owner = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='distro/')

    email = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    fb = models.CharField(max_length=15, null=True, blank=True)
    tw = models.CharField(max_length=15, null=True, blank=True)

    lng = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)

    def __str__(self):
        return self.name
