from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

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


# Don't forget to register models and commit changes to server!!!
