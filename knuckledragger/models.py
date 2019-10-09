from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


##### character, race, attributes, inventory and connections #####
class Race(models.Model):
    arrivad = models.BooleanField(default=False)
    basahnin = models.BooleanField(default=False)
    ferrick = models.BooleanField(default=False)
    holeg = models.BooleanField(default=False)
    human = models.BooleanField(default=False)
    illawmi = models.BooleanField(default=False)
    kassari = models.BooleanField(default=False)
    khura = models.BooleanField(default=False)
    mogo = models.BooleanField(default=False)

class Attributes(models.Model):
    brawny = models.PositiveSmallIntegerField(default=0)
    sturdy = models.PositiveSmallIntegerField(default=0)
    speedy = models.PositiveSmallIntegerField(default=0)
    nerdy = models.PositiveSmallIntegerField(default=0)
    balky = models.PositiveSmallIntegerField(default=0)
    wily = models.PositiveSmallIntegerField(default=0)
    pritty = models.PositiveSmallIntegerField(default=0)
    gritty = models.PositiveSmallIntegerField(default=0)
    witty = models.PositiveSmallIntegerField(default=0)
    beastly = models.PositiveSmallIntegerField(default=0)
    techy = models.PositiveSmallIntegerField(default=0)
    outdoorsy = models.PositiveSmallIntegerField(default=0)

class EquipmentSlots(models.Model):
    head = models.BooleanField(default=False)
    neck = models.BooleanField(default=False)
    shoulder = models.BooleanField(default=False)
    chest = models.BooleanField(default=False)
    arm = models.BooleanField(default=False)
    hand = models.BooleanField(default=False)
    belt = models.BooleanField(default=False)
    waist = models.BooleanField(default=False)
    leg = models.BooleanField(default=False)
    feet = models.BooleanField(default=False)
    accessory = models.BooleanField(default=False)
    wallet = models.IntegerField(default=0)

# class Friends(models.Model):
#     friend = models.ForeignKey(Character, on_delete=models.CASCADE)
#     relation = models.CharField(max_length=16)

# class Family(models.Model):
#     family = models.ForeignKey(Character, on_delete=models.CASCADE)
#     relation = models.CharField(max_length=16)

# class Enemies(models.Model):
#     enemies = models.ForeignKey(Character, on_delete=models.CASCADE)
#     relation = models.CharField(max_length=16)

# class Connections(models.Model):
#     friends = models.ForeignKey(Friends, on_delete=models.CASCADE)
#     family = models.ForeignKey(Family, on_delete=models.CASCADE)
#     enemies = models.ForeignKey(Enemies, on_delete=models.CASCADE)

class Character(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    health = models.PositiveSmallIntegerField(default=0)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    attributes = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    equipment_slots = models.ForeignKey(EquipmentSlots, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField(default=0)
    age = models.PositiveSmallIntegerField(default=0)
    #connections = models.ForeignKey(Connections, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name + self.last_name

# TODO add Skills model