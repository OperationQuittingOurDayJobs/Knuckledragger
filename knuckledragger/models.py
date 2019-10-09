from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Character(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    health = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.first_name

