from django.db import models

# Create your models here.

class Message(models.Model):
    value = models.CharField(max_length=10000)
    datetime = models.DateTimeField(max_length=10000000000)
    room = models.CharField(max_length=1000)
    user = models.CharField(max_length=10000)

class Room(models.Model):
    room = models.CharField(max_length=1000)

class User(models.Model):
    name = models.CharField(max_length=1000)
