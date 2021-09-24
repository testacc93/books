from django.db import models
import datetime

class Book(models.Model):
    name = models.CharField(max_length=64)
    min_age = models.IntegerField()
    image = models.ImageField(upload_to='image', blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=64)
    age = models.IntegerField()
    password = models.CharField(max_length=256)
    created = models.DateTimeField(default=datetime.datetime.now())
    image = models.ImageField(upload_to='image', blank=True)

    def __str__(self):
        return self.username