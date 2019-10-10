from django.shortcuts import render

import requests
import os

from .models import Character

def index(request):
    return render(request, 'site/index.html')

def test(request):
    character_list = Character.objects.order_by('id')
    context = {'character_list':character_list }
    return render(request, 'site/test/test.html', context)