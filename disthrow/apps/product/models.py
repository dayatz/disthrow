from django.db import models
from django.contrib.postgres.fields import ArrayField
from apps.distro.models import Distro


class Product(models.Model):
    distro = models.ForeignKey(Distro)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    size = ArrayField(models.CharField(max_length=1), blank=True)
    color = ArrayField(models.CharField(max_length=10), blank=True)
    photo = models.ImageField(upload_to='product/')
