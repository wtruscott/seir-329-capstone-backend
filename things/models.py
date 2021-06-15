from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    location = models.CharField(max_length=100)
    favorite = models.BooleanField(default=False)


class Collection(models.Model):
    name = models.CharField(max_length=100)
    things = models.ManyToManyField(Thing)
