from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    location = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    favorite = models.BooleanField(default=False)
    slug =models.SlugField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Container(models.Model):
    name = models.CharField(max_length=100)
    things = models.ManyToManyField(Thing, blank=True)
    slug =models.SlugField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    containers = models.ManyToManyField(Container, blank=True)
    things = models.ManyToManyField(Thing, blank=True)
    slug =models.SlugField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Collection(models.Model):
    name = models.CharField(max_length=100)
    things = models.ManyToManyField(Thing, blank=True)
    slug =models.SlugField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name