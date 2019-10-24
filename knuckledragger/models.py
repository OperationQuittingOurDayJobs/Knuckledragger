# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User


# #--------------(ALPHA)#--------------#
# class MailingList(models.Model):
#     first_name = models.CharField(max_length=16)
#     email = models.EmailField(max_length=254)


# class Item(models.Model):
#     name = models.CharField(max_length=16)


# class Character(models.Model):
#     first_name = models.CharField(max_length=16)
#     last_name = models.CharField(max_length=16)
#     max_health = models.PositiveSmallIntegerField(default=0)
#     current_health = models.PositiveSmallIntegerField(default=0)
#     weight = models.PositiveSmallIntegerField(default=0)
#     age = models.PositiveSmallIntegerField(default=0)
#     authored_by = models.ForeignKey(User, on_delete=models.CASCADE)

#     # Equipment Slots + Inventory
#     head = models.BooleanField(default=False)
#     neck = models.BooleanField(default=False)
#     shoulder = models.BooleanField(default=False)
#     chest = models.BooleanField(default=False)
#     arm = models.BooleanField(default=False)
#     hand = models.BooleanField(default=False)
#     belt = models.BooleanField(default=False)
#     waist = models.BooleanField(default=False)
#     leg = models.BooleanField(default=False)
#     feet = models.BooleanField(default=False)
#     accessory = models.BooleanField(default=False)
#     wallet = models.IntegerField(default=0)

#     # Attributes
#     brawny = models.PositiveSmallIntegerField(default=0)
#     sturdy = models.PositiveSmallIntegerField(default=0)
#     speedy = models.PositiveSmallIntegerField(default=0)
#     nerdy = models.PositiveSmallIntegerField(default=0)
#     balky = models.PositiveSmallIntegerField(default=0)
#     wily = models.PositiveSmallIntegerField(default=0)
#     pritty = models.PositiveSmallIntegerField(default=0)
#     gritty = models.PositiveSmallIntegerField(default=0)
#     witty = models.PositiveSmallIntegerField(default=0)
#     beastly = models.PositiveSmallIntegerField(default=0)
#     techy = models.PositiveSmallIntegerField(default=0)
#     outdoorsy = models.PositiveSmallIntegerField(default=0)

#     # Race
#     arrivad = models.BooleanField(default=False)
#     basahnin = models.BooleanField(default=False)
#     ferrick = models.BooleanField(default=False)
#     holeg = models.BooleanField(default=False)
#     human = models.BooleanField(default=False)
#     illawmi = models.BooleanField(default=False)
#     kassari = models.BooleanField(default=False)
#     khura = models.BooleanField(default=False)
#     mogo = models.BooleanField(default=False)

#     def __str__(self):
#         return self.first_name + self.last_name


# class Room(models.Model):
#     # General Info
#     room_name = models.CharField(max_length=16)
#     authored_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     description = models.CharField(max_length=200)
#     date_created = models.DateField(auto_now_add=True)
#     max_players = models.PositiveSmallIntegerField(default=4)
    
#     # Schedule
#     sunday = models.BooleanField(default=False)
#     monday = models.BooleanField(default=False)
#     tuesday = models.BooleanField(default=False)
#     wednesday = models.BooleanField(default=False)
#     thursday = models.BooleanField(default=False)
#     friday = models.BooleanField(default=False)
#     saturday = models.BooleanField(default=False)
#     time = models.TimeField()
    