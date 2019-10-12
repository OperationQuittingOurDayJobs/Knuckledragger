from django.shortcuts import render

import requests
import os

from .models import Character
# from .actions import Attack *

def index(request):
    return render(request, 'site/index.html')

def test(request):
    character_list = Character.objects.filter(first_name='Test')

    context = {'character_list' : character_list }
    return render(request, 'site/test/test.html', context)

def attack(request):
    print('You are attacking!')