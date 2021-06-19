from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    location = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    favorite = models.BooleanField(default=False)
    slug =models.SlugField(unique=True, null=True, blank=False)
    

class Container(models.Model):
    name = models.CharField(max_length=100)
    things = models.ManyToManyField(Thing)

class Place(models.Model):
    name = models.CharField(max_length=100)
    containers = models.ManyToManyField(Container)
    things = models.ManyToManyField(Thing)
    

class Collection(models.Model):
    name = models.CharField(max_length=100)
    things = models.ManyToManyField(Thing)