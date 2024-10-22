from django.contrib.gis.gdal.prototypes.srs import clone_srs
from django.db import models
# Create your models here.
class Product(models.Model):# commom chars in django app, if u want to store on db
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)


