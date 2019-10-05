from django.shortcuts import render
from django.http import HttpResponse

import requests
import os

# Create your views here.
def index(request):
    return HttpResponse('knuckledragger! ')