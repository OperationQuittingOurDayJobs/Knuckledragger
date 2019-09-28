from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Don't forget to register models and commit changes to server!!!

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

# SITE MODELS
class Room(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

# GAME MODELS
class Status(models.Model):
    state = models.CharField(max_length = 16, default = 'normal')

class Rarity(models.Model):
    quality = models.CharField(max_length = 16, default = 'mundane')

class Item(models.Model):
    weight = models.FloatField(default = 0)
    max_durability = models.FloatField(default = 0)
    current_durability = models.FloatField(default = 0)
    name = models.CharField(max_length = 50)
    price = models.FloatField(default = 0)
    description = models.TextField(max_length = 300)
    status = models.ForeignKey(Status, on_delete = models.CASCADE)
    material = models.CharField(max_length = 20)
    rarity = models.ForeignKey(Rarity, on_delete = models.CASCADE)
    x_dimension = models.IntegerField(default = 0)
    y_dimension = models.IntegerField(default = 0)
    def __str__(self):
        return self.name

class Attributes(models.Model):
    brawny = models.CharField(max_length = 16)

class Type(models.Model):
    number = models.IntegerField(default = 0)

class Races(models.Model):
    Arrivad = models.CharField(max_length = 16)

class Brawny(models.Model):
    type = models.ForeignKey(Type, on_delete = models.CASCADE)

class Character(models.Model):
    race = models.ForeignKey(Races, on_delete = models.CASCADE)
    attributes = models.ForeignKey(Attributes, on_delete = models.CASCADE)
    #inventory
    weight = models.IntegerField(default = 0)
    age = models.IntegerField(default = 0)
    hit_points = models.IntegerField(default = 0)
    name = models.CharField(max_length = 16)
    #connections
    speed = models.IntegerField(default = 0)


