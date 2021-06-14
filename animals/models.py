from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    legs = models.IntegerField(default=2)

# Create your models here.
