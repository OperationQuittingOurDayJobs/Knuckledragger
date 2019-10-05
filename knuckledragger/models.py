from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Don't forget to register models and commit changes to server

####################((Site Models))####################
class Room(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

####################((Game Mechanics))####################
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
    x_dimension = models.PositiveSmallIntegerField(default = 0)
    y_dimension = models.PositiveSmallIntegerField(default = 0)
    def __str__(self):
        return self.name

####################((Attributes and Skills))####################
class Attributes(models.Model):
    brawny = models.PositiveSmallIntegerField(default = 0)
    sturdy = models.PositiveSmallIntegerField(default = 0)
    speedy = models.PositiveSmallIntegerField(default = 0)
    nerdy = models.PositiveSmallIntegerField(default = 0)
    balky = models.PositiveSmallIntegerField(default = 0)
    wily = models.PositiveSmallIntegerField(default = 0)
    pritty = models.PositiveSmallIntegerField(default = 0)
    gritty = models.PositiveSmallIntegerField(default = 0)
    witty = models.PositiveSmallIntegerField(default = 0)
    beastly = models.PositiveSmallIntegerField(default = 0)
    techy = models.PositiveSmallIntegerField(default = 0)
    outdoorsy = models.PositiveSmallIntegerField(default = 0)

class Skills(models.Model):
    hittin = models.PositiveSmallIntegerField(default = 0)
    liftin = models.PositiveSmallIntegerField(default = 0)
    brawny_special = models.PositiveSmallIntegerField(default = 0)
    gettin_hit = models.PositiveSmallIntegerField(default = 0)
    not_dyin = models.PositiveSmallIntegerField(default = 0)
    sturdy_special = models.PositiveSmallIntegerField(default = 0)
    troubleshottin = models.PositiveSmallIntegerField(default = 0)
    smarts = models.PositiveSmallIntegerField(default = 0)
    nerdy_special = models.PositiveSmallIntegerField(default = 0)
    trackin = models.PositiveSmallIntegerField(default = 0)
    backbone = models.PositiveSmallIntegerField(default = 0)
    balky_special = models.PositiveSmallIntegerField(default = 0)
    stashin = models.PositiveSmallIntegerField(default = 0)
    sensin = models.PositiveSmallIntegerField(default = 0)
    wily_special = models.PositiveSmallIntegerField(default = 0)
    smooth_talkin = models.PositiveSmallIntegerField(default = 0)
    moxie = models.PositiveSmallIntegerField(default = 0)
    pritty_special = models.PositiveSmallIntegerField(default = 0)
    scarin = models.PositiveSmallIntegerField(default = 0)
    leadin = models.PositiveSmallIntegerField(default = 0)
    gritty_special = models.PositiveSmallIntegerField(default = 0)
    swindlin = models.PositiveSmallIntegerField(default = 0)
    blendin = models.PositiveSmallIntegerField(default = 0)
    witty_special = models.PositiveSmallIntegerField(default = 0)
    tamin = models.PositiveSmallIntegerField(default = 0)
    tendin = models.PositiveSmallIntegerField(default = 0)
    beastly_special = models.PositiveSmallIntegerField(default = 0)
    big_booms = models.PositiveSmallIntegerField(default = 0)
    loud_vrooms = models.PositiveSmallIntegerField(default = 0)
    techy_special = models.PositiveSmallIntegerField(default = 0)
    scroungin = models.PositiveSmallIntegerField(default = 0)
    navigatin = models.PositiveSmallIntegerField(default = 0)
    outdoorsy_special = models.PositiveSmallIntegerField(default = 0)

class Type(models.Model):
    number = models.PositiveSmallIntegerField(default = 0)

####################((RACES))####################
class Races(models.Model):
    Arrivad = models.CharField(max_length = 16)

class Brawny(models.Model):
    type = models.ForeignKey(Type, on_delete = models.CASCADE)

class Inventory(models.Model):
    head = models.BooleanField()
    neck = models.BooleanField()
    shoulder = models.BooleanField()
    chest = models.BooleanField()
    arm = models.BooleanField()
    hand = models.BooleanField()
    belt = models.BooleanField()
    waist = models.BooleanField()
    leg = models.BooleanField()
    feet = models.BooleanField()
    accessory = models.BooleanField()
    wallet = models.PositiveSmallIntegerField(default = 0)


class Character(models.Model):
    race = models.ForeignKey(Races, on_delete = models.CASCADE)
    attributes = models.ForeignKey(Attributes, on_delete = models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete = models.CASCADE)
    weight = models.PositiveSmallIntegerField(default = 0)
    age = models.PositiveSmallIntegerField(default = 0)
    hit_points = models.PositiveSmallIntegerField(default = 0)
    name = models.CharField(max_length = 16)
    #connections
    speed = models.PositiveSmallIntegerField(default = 0)