from django.db import models

# Create your models here.
class Cafe(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=250)
    adress = models.CharField(max_length=250)
    info = models.TextField()
    link = models.URLField()